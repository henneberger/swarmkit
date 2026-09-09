from copy import deepcopy
from dataclasses import replace

import pytest

from swarmkit.enron.inquiries import AgendaConfig, InquiryAgenda
from swarmkit.serialization import dumps, loads
from swarmkit.types import AgentState, Evidence, SwarmState


def setup(config=None):
    state = SwarmState(
        agents={a: AgentState(a, capabilities=frozenset({a})) for a in ("owner", "importer", "other")}
    )
    return state, InquiryAgenda(state, lambda e: e.source != "future", config=config)


def opened(agenda):
    return agenda.apply(
        "owner",
        {
            "kind": "open",
            "question": "Why did the status change?",
            "why_matters": "Two teams may be acting on incompatible versions.",
            "unresolved_premise": "Whether a later import replaced the status is unknown.",
        },
    ).metadata["inquiry_id"]


def test_recruitment_changes_dispatch_and_returns_only_addressed_message():
    state, agenda = setup()
    iid = opened(agenda)
    first = agenda.schedule()[0]
    result = agenda.apply(
        "owner",
        {
            "kind": "request_peer",
            "inquiry_id": iid,
            "capabilities": ["importer"],
            "unresolved_premise": "Who performed the overnight import?",
        },
    )
    assert result.messages[0].recipients == ("importer",)
    assert not state.messages and not state.agents["importer"].inbox
    second = agenda.schedule()[0]
    assert second["agent_id"] == "importer" and second["kind"] == "peer_review"
    assert not state.data.get("capability_router")  # no invented success feedback
    agenda.finish(first["id"])
    agenda.finish(second["id"])


def test_invalid_evidence_and_queue_overflow_leave_artifact_versions_unchanged():
    state, agenda = setup(AgendaConfig(max_pending=1))
    iid = opened(agenda)
    before = dumps(state)
    for change in (
        {"kind": "revise", "evidence": [Evidence("x", "future", "future", "owner")]},
        {"kind": "search", "query": "overnight import", "unresolved_premise": "Which job ran?"},
    ):
        with pytest.raises(ValueError):
            agenda.apply("owner", {"inquiry_id": iid, **change})
        assert dumps(state) == before


def test_watch_source_family_dedup_but_explicit_receipt_watch_tracks_forward():
    state, agenda = setup()
    iid = opened(agenda)
    agenda.finish(agenda.schedule()[0]["id"])
    agenda.apply(
        "owner",
        {
            "kind": "watch",
            "inquiry_id": iid,
            "terms": ["import", "resolved"],
            "unresolved_premise": "Did a fresh import preserve the fix?",
        },
    )
    e = Evidence(
        "e",
        "import resolved",
        "family",
        "owner",
        metadata={"document_id": "d1", "segment_source_family": "same"},
    )
    assert agenda.notify_arrival(e, "Import resolved") == [iid]
    agenda.finish(agenda.schedule()[0]["id"])
    assert (
        agenda.notify_arrival(
            replace(e, id="forward", metadata={"document_id": "d2", "segment_source_family": "same"}),
            "import resolved",
        )
        == []
    )
    agenda.apply(
        "owner",
        {
            "kind": "watch",
            "inquiry_id": iid,
            "terms": ["import"],
            "occurrences": True,
            "unresolved_premise": "Did another team receive this instruction?",
        },
    )
    assert agenda.notify_arrival(e, "import resolved") == [iid]
    assert agenda.notify_arrival(
        replace(e, id="forward", metadata={"document_id": "d2", "segment_source_family": "same"}),
        "import resolved",
    ) == [iid]


def test_budget_fairness_resume_and_no_refund():
    state, agenda = setup(AgendaConfig(max_actions=3, max_actions_per_inquiry=2, exploration_every=2))
    iid = opened(agenda)
    agenda.enqueue_exploration("other", {"document_ids": ["new"]})
    agenda.apply(
        "owner",
        {
            "kind": "search",
            "inquiry_id": iid,
            "query": "versions",
            "unresolved_premise": "Which version won?",
        },
    )
    a = agenda.schedule()[0]
    agenda.finish(a["id"])
    assert agenda.schedule()[0]["kind"] == "explore"
    restored = InquiryAgenda(loads(dumps(state)), lambda e: True)
    assert restored.data["actions_used"] == 2
    assert restored.schedule()[0]["kind"] == "search"
    assert restored.schedule(10) == []


def test_explicit_private_guard_and_revisions_notify_participants():
    state, agenda = setup()
    secret = Evidence("private", "import replaced status", "arrived", "importer")
    agenda.evidence_available = lambda actor, e: actor == e.owner
    iid = opened(agenda)
    with pytest.raises(ValueError):
        agenda.apply("owner", {"kind": "revise", "inquiry_id": iid, "evidence": [secret]})
    agenda.apply(
        "importer",
        {"kind": "join", "inquiry_id": iid, "unresolved_premise": "I can inspect the import record."},
    )
    result = agenda.apply(
        "importer",
        {
            "kind": "revise",
            "inquiry_id": iid,
            "evidence": [secret],
            "change": "Importer saw the replacement.",
        },
    )
    assert result.messages[0].recipients == ("owner",)
    assert result.artifacts[0].parents and not result.artifacts[0].verified
    assert result.artifacts[0].evidence == (secret,)


def test_standalone_source_acquisition_needs_no_theory_or_premise():
    state, agenda = setup()
    result = agenda.apply("owner", {"kind": "read", "document_id": "mail-123", "offset": 700})
    assert result.metadata["inquiry_id"] is None
    assert not result.artifacts and not state.artifacts and not agenda.data["inquiries"]
    work = agenda.schedule()[0]
    assert work["inquiry_id"] is None and work["payload"] == {"document_id": "mail-123", "offset": 700}
    agenda.finish(work["id"])
    agenda.apply("owner", {"kind": "search", "query": "all: overnight refresh"})
    assert agenda.schedule()[0]["kind"] == "search"


@pytest.mark.parametrize(
    "action",
    [
        {"kind": "read", "document_id": "../private", "offset": 0},
        {"kind": "read", "document_id": "mail-123", "offset": True},
        {"kind": "read", "document_id": "mail-123", "offset": -1},
        {"kind": "search", "query": "   "},
        {"kind": "search", "query": "refresh", "inquiry_id": "unknown"},
    ],
)
def test_malformed_standalone_retrieval_is_atomic(action):
    state, agenda = setup()
    before = dumps(state)
    with pytest.raises(ValueError):
        agenda.apply("owner", action)
    assert dumps(state) == before


def test_existing_watch_inherits_unresolved_premise():
    state, agenda = setup()
    iid = opened(agenda)
    expected = agenda.data["inquiries"][iid]["unresolved_premise"]
    for action in (
        {"kind": "watch", "terms": ["refresh"]},
    ):
        result = agenda.apply("owner", {"inquiry_id": iid, **action})
        assert result.artifacts[0].content["unresolved_premise"] == expected


@pytest.mark.parametrize('actor', ['owner', 'other'])
@pytest.mark.parametrize('action', [
    {'kind': 'read', 'document_id': 'mail-123', 'offset': 700},
    {'kind': 'search', 'query': 'overnight refresh'},
])
def test_linked_acquisition_preserves_theory_and_membership(actor, action):
    state, agenda = setup()
    iid = opened(agenda)
    agenda.finish(agenda.schedule()[0]['id'])
    artifact_before = deepcopy(state.artifacts)
    inquiry_before = deepcopy(agenda.data['inquiries'])
    history_before = deepcopy(agenda.data['history'])
    result = agenda.apply(actor, {**action, 'inquiry_id': iid})
    assert result.metadata['source_acquisition']
    assert result.metadata['inquiry_id'] == iid
    assert not result.artifacts and not result.messages
    assert deepcopy(state.artifacts) == artifact_before
    assert deepcopy(agenda.data['inquiries']) == inquiry_before
    assert deepcopy(agenda.data['history']) == history_before
    assert agenda.data['inquiries'][iid]['participants'] == ['owner']
    assert state.agents['other'].inbox == []
    work = agenda.schedule()[0]
    assert work['inquiry_id'] == iid and work['agent_id'] == actor
    assert work['kind'] == action['kind']
    assert work['payload'] == {k: v for k, v in action.items() if k != 'kind'}
    # Retrieving for a public question does not grant interpretive permissions.
    if actor == 'other':
        with pytest.raises(ValueError, match='join inquiry'):
            agenda.apply(actor, {'kind': 'revise', 'inquiry_id': iid,
                                 'unresolved_premise': 'I still need a source.'})


def test_linked_acquisition_rejects_closed_unknown_and_obeys_inquiry_work_cap():
    state, agenda = setup(AgendaConfig(max_actions_per_inquiry=2))
    iid = opened(agenda)
    agenda.finish(agenda.schedule()[0]['id'])
    agenda.apply('other', {'kind': 'search', 'inquiry_id': iid, 'query': 'first lookup'})
    agenda.finish(agenda.schedule()[0]['id'])
    agenda.apply('other', {'kind': 'read', 'inquiry_id': iid, 'document_id': 'mail-1'})
    assert agenda.schedule() == []  # linked acquisition consumed the same work cap
    agenda.apply('owner', {'kind': 'close', 'inquiry_id': iid,
                           'unresolved_premise': 'No further work warranted.'})
    for target in (iid, 'missing'):
        for action in ({'kind': 'read', 'document_id': 'mail-1'},
                       {'kind': 'search', 'query': 'lookup'}):
            before = dumps(state)
            with pytest.raises(ValueError, match='closed|unknown'):
                agenda.apply('other', {**action, 'inquiry_id': target})
            assert dumps(state) == before


def test_acquisition_does_not_weaken_interpretive_evidence_requirements():
    state, agenda = setup()
    iid = opened(agenda)
    for action in ({'kind': 'revise', 'inquiry_id': iid},
                   {'kind': 'open', 'question': 'Unsupported?', 'why_matters': 'Unknown.'}):
        before = dumps(state)
        with pytest.raises(ValueError, match='needs source evidence'):
            agenda.apply('owner', action)
        assert dumps(state) == before


def test_standalone_request_reply_routes_one_reaction_without_artifacts():
    state, agenda = setup()
    asked = agenda.apply('owner', {'kind': 'request_peer', 'recipient': 'importer',
                                  'question': 'Was the signature page faxed?'})
    request_id = asked.messages[0].id
    assert asked.messages[0].recipients == ('importer',)
    assert asked.metadata['inquiry_id'] is None
    assert not state.artifacts and not agenda.data['inquiries']
    job = agenda.schedule()[0]
    assert job['kind'] == 'peer_review'
    assert job['payload']['request_id'] == request_id
    assert job['payload']['requester'] == 'owner'
    reply = agenda.apply('importer', {'kind': 'reply', 'recipient': 'owner',
                                     'answer': 'I found no relevant record in my context.'})
    assert reply.messages[0].parents == (request_id,)
    assert reply.messages[0].metadata['semantic_validation'] is False
    assert reply.messages[0].metadata['source_backed'] is False
    agenda.finish(job['id'])
    reaction = agenda.schedule()[0]
    assert reaction['kind'] == 'react' and reaction['agent_id'] == 'owner'
    assert reaction['payload']['request_id'] == request_id
    agenda.finish(reaction['id'])
    assert agenda.schedule() == []
    assert not state.artifacts
    before = dumps(state)
    duplicate = agenda.apply('owner', {'kind': 'request_peer', 'recipient': 'importer',
                                      'question': 'Was the signature page faxed?'})
    assert duplicate.metadata['deduplicated'] and not duplicate.messages
    assert dumps(state) == before
    with pytest.raises(ValueError, match='unanswered'):
        agenda.apply('importer', {'kind': 'reply', 'recipient': 'owner', 'answer': 'Duplicate'})
    assert dumps(state) == before


def test_nonparticipant_question_and_source_reply_do_not_join_or_mutate_inquiry():
    state, agenda = setup()
    iid = opened(agenda)
    agenda.finish(agenda.schedule()[0]['id'])
    original = deepcopy(state.artifacts)
    original_row = deepcopy(agenda.data['inquiries'][iid])
    request = agenda.apply('other', {'kind': 'request_peer', 'inquiry_id': iid,
                                    'recipient': 'importer', 'request': 'Which receipt records the fax?'})
    source = Evidence('fax', 'The source records transmission.', 'arrived', 'importer')
    result = agenda.apply('importer', {'kind': 'reply', 'recipient': 'other',
        'request_id': request.metadata['request_id'], 'answer': 'Here is the matching receipt.',
        'evidence': [source]})
    assert result.messages[0].evidence == (source,)
    assert result.messages[0].recipients == ('other',)
    assert agenda.data['inquiries'][iid] == original_row
    assert state.artifacts == original
    assert all(not a.inbox for a in state.agents.values())
    assert all(q['inquiry_id'] == iid for q in agenda.data['pending'])


def test_reply_rejects_unknown_link_or_invalid_source_atomically():
    state, agenda = setup()
    agenda.apply('owner', {'kind': 'request_peer', 'recipient': 'importer', 'question': 'Any receipt?'})
    for action in [
        {'kind': 'reply', 'recipient': 'other', 'answer': 'Unsolicited answer'},
        {'kind': 'reply', 'recipient': 'owner', 'request_id': 'unknown', 'answer': 'Wrong link'},
        {'kind': 'reply', 'recipient': 'owner', 'answer': 'Future source',
         'evidence': [Evidence('x', 'future', 'future', 'importer')]},
    ]:
        before = dumps(state)
        with pytest.raises(ValueError):
            agenda.apply('importer', action)
        assert dumps(state) == before
