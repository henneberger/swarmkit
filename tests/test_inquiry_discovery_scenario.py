"""Scripted inquiry-swarm mechanism tests, NOT evidence of LLM discovery.

The invented Aster/Quartz episode has complementary private observations, a
plausible display-version rival, and a subsequently observed recovery. These
scripts specify the reasoning in advance: they test causal message routing,
action availability, source visibility, and lifecycle plumbing only. They do
not score an LLM's curiosity, causal identification, or real-world usefulness.
"""

from pathlib import Path

import pytest

from swarmkit.enron.corpus import EmailCorpus
from swarmkit.enron.replay import ReplayCorpus

FIXTURES = Path(__file__).parent / 'fixtures' / 'inquiry_demo'


@pytest.fixture
def fictional_corpus(tmp_path):
    path = tmp_path / 'fictional.sqlite'
    with EmailCorpus(path) as corpus:
        result = corpus.ingest_directory(FIXTURES)
        assert result.inserted == 12
        docs = {
            document.message_id.split('@')[0].lstrip('<'): document
            for document in corpus.search('synthetic', limit=50)
        }
        assert len(docs) == 12
        assert all(document.synthetic for document in docs.values())
    return path, docs


def span(view, document, quote, owner):
    start = document.body.index(quote)
    return view.evidence(document.id, start, start + len(quote), owner=owner)


def admit_through(replay, stamp):
    while replay.admit_until(stamp, batch_size=3):
        pass


def test_fictional_timeline_keeps_resolution_and_late_forward_in_future(
    fictional_corpus, tmp_path
):
    path, docs = fictional_corpus
    with EmailCorpus(path) as master:
        future = docs['10_observed_resolution']
        future_evidence = span(
            master, future, 'Kestrel quantity is 420.', 'operations'
        )
    with ReplayCorpus(path, tmp_path / 'arrived.sqlite') as replay:
        admit_through(replay, '2001-02-01T11:00:00Z')
        assert replay.count() == 3
        assert replay.get(docs['01_status_closed'].id) is not None
        assert replay.get(docs['04_regression'].id) is None
        assert not replay.verify_evidence(future_evidence)
        with pytest.raises(KeyError):
            replay.evidence(future.id, 0, 20)

        admit_through(replay, '2001-02-02T15:00:00Z')
        assert replay.count() == 9
        assert replay.search('revision 18', match='all')
        assert replay.get(future.id) is None
        assert not replay.verify_evidence(future_evidence)
        # The announcement expressly lacks observation of the next refresh.
        announced = replay.get(docs['09_patch_announced'].id)
        assert 'next scheduled refresh has not happened' in announced.body
        admit_through(replay, '2001-02-03T08:00:00Z')
        assert replay.verify_evidence(future_evidence)
        assert replay.get(docs['11_late_forward'].id) is None
        admit_through(replay, '2001-02-04T09:00:00Z')
        late = docs['11_late_forward']
        quoted = [part for part in replay.segments(late.id) if part.kind == 'forwarded']
        assert quoted
        assert any(part.claimed_date == 'January 31, 2001 16:00' for part in quoted)
        assert replay.observation(late.id)['date_utc'].startswith('2001-02-04')
        assert replay.get(late.id).date_utc.startswith('2001-02-04')
        assert late.id not in {
            document.id for document in replay.search('Quartz', cutoff='2001-02-01')
        }


def make_agenda(replay, docs):
    from swarmkit.enron.inquiries import InquiryAgenda
    from swarmkit.types import AgentState, SwarmState

    excerpts = {
        'closed': ('01_status_closed', 'I marked ticket A41 resolved.', 'operations'),
        'recurrence': (
            '04_regression', 'The board footer says destination QZ-7.', 'operations'
        ),
        'fresh': (
            '06_fresh_export',
            'It shows Kestrel quantity 0, destination QZ-7, and generated-at 02:03 today.',
            'operations',
        ),
        'receipt': (
            '07_import_receipt',
            'The job receipt says Quartz wrote destination QZ-7 at 02:03 today '
            'from vendor revision 16. Lot Kestrel had a missing quantity in that '
            'input and was written as zero.',
            'importer',
        ),
        'alternative': (
            '05_benign_alternative',
            'A saved browser tab could also be stale. These are possibilities, not findings:',
            'comparison',
        ),
    }
    evidence = {
        key: span(replay, docs[name], quote, owner)
        for key, (name, quote, owner) in excerpts.items()
    }
    state = SwarmState(agents={
        'operations': AgentState(
            'operations', private_evidence=tuple(evidence[k] for k in ('closed', 'recurrence', 'fresh'))
        ),
        'importer': AgentState(
            'importer', capabilities=frozenset({'import_receipts'}),
            private_evidence=(evidence['receipt'],),
        ),
        'comparison': AgentState('comparison', private_evidence=(evidence['alternative'],)),
    })

    def exposed(agent_id, item):
        # Exact source validity alone must not grant access to a peer's private fact.
        local = list(state.agents[agent_id].private_evidence)
        local.extend(e for message in state.agents[agent_id].inbox for e in message.evidence)
        local.extend(e for artifact in state.artifacts.values() for e in artifact.evidence)
        return any(item == existing for existing in local)

    agenda = InquiryAgenda(
        state, replay.verify_evidence, evidence_available=exposed
    )
    return agenda, state, evidence


def open_case(agenda, evidence):
    result = agenda.apply('operations', {
        'kind': 'open',
        'question': 'Why did the server value recur after ticket A41 was marked resolved?',
        'why_matters': 'The next refresh might erase another destination-only correction.',
        'evidence': tuple(evidence[k] for k in ('closed', 'recurrence', 'fresh')),
        'rivals': [
            'The apparent recurrence is a stale display or mismatched local revision.',
            'A later server-side writer replaced the correction.',
        ],
        'next_actions': ['Find which process wrote QZ-7 at 02:03.'],
    })
    initial = agenda.schedule()
    assert len(initial) == 1 and initial[0]['kind'] == 'investigate'
    agenda.finish(initial[0]['id'])
    return result.metadata['inquiry_id']


def test_scripted_peer_request_unlocks_connection_that_withheld_control_cannot_support(
    fictional_corpus, tmp_path
):
    """Ablate one reply with identical sources/requests; no model reasoning is tested."""
    from swarmkit.runtime import apply_result

    path, docs = fictional_corpus
    outcomes = {}
    for reply_enabled in (False, True):
        with ReplayCorpus(path, tmp_path / f'peer-{reply_enabled}.sqlite') as replay:
            admit_through(replay, '2001-02-02T11:00:00Z')
            agenda, state, evidence = make_agenda(replay, docs)
            iid = open_case(agenda, evidence)
            assert agenda.schedule() == []
            assert state.agents['importer'].inbox == []
            before = agenda.snapshot()
            with pytest.raises(ValueError, match='invalid or unarrived evidence'):
                agenda.apply('operations', {
                    'kind': 'revise', 'inquiry_id': iid, 'evidence': (evidence['receipt'],),
                    'change': 'Attempt to cite a peer-private receipt before delivery.',
                })
            assert agenda.snapshot() == before
            request = agenda.apply('operations', {
                'kind': 'request_peer', 'inquiry_id': iid,
                'capabilities': ['import_receipts'],
                'unresolved_premise': 'Which process wrote QZ-7 at 02:03? Inspect actual receipts.',
                'evidence': (evidence['fresh'],),
            })
            apply_result(state, request)
            assert state.agents['importer'].inbox[-1].recipients == ('importer',)
            assert state.agents['comparison'].inbox == []
            assignments = agenda.schedule()
            assert len(assignments) == 1
            assert assignments[0]['kind'] == 'peer_review'
            assert assignments[0]['agent_id'] == 'importer'
            if reply_enabled:
                reply = agenda.apply('importer', {
                    'kind': 'revise', 'inquiry_id': iid, 'evidence': (evidence['receipt'],),
                    'change': 'Actual Quartz write receipt connects the server destination and timestamp.',
                    'next_actions': ['Check upstream revision and observe a subsequent refresh.'],
                })
                apply_result(state, reply)
                delivered = state.agents['operations'].inbox[-1]
                assert delivered.recipients == ('operations',)
                assert evidence['receipt'] in delivered.evidence
                assert state.agents['comparison'].inbox == []
            agenda.finish(assignments[0]['id'])
            row = agenda.snapshot()['inquiries'][0]
            shared = state.artifacts[row['artifact_id']].evidence
            has_connection = evidence['receipt'] in shared
            # This branch is the explicitly scripted decision policy. The engine
            # has not independently inferred that these observations are causal.
            if has_connection:
                agenda.apply('operations', {
                    'kind': 'search', 'inquiry_id': iid,
                    'query': 'Quartz QZ-7 vendor revision 18',
                    'evidence': (evidence['fresh'], evidence['receipt']),
                    'unresolved_premise': 'Did the source change, and did a later refresh retain it?',
                })
            outcomes[reply_enabled] = {
                'connection': has_connection,
                'searches': [q for q in agenda.snapshot()['pending'] if q['kind'] == 'search'],
                'sources': {e.source for e in shared},
            }
            assert all(replay.verify_evidence(e) for e in shared)
            assert not state.agents['operations'].private_evidence == state.agents['importer'].private_evidence
    assert outcomes[True]['connection']
    assert len(outcomes[True]['searches']) == 1
    assert not outcomes[False]['connection']
    assert outcomes[False]['searches'] == []
    assert outcomes[False]['sources'] < outcomes[True]['sources']


def test_watch_reopens_work_on_later_observation_without_forcing_a_rule(
    fictional_corpus, tmp_path
):
    from swarmkit.enron.inquiries import InquiryAgenda
    from swarmkit.types import AgentState, SwarmState

    path, docs = fictional_corpus
    with EmailCorpus(path) as master:
        observation = span(
            master, docs['10_observed_resolution'],
            'This one observed refresh retained the correction;', 'operations'
        )
    with ReplayCorpus(path, tmp_path / 'watch.sqlite') as replay:
        admit_through(replay, '2001-02-02T11:00:00Z')
        agenda, state, evidence = make_agenda(replay, docs)
        iid = open_case(agenda, evidence)
        agenda.apply('operations', {
            'kind': 'watch', 'inquiry_id': iid,
            'terms': ['Kestrel', 'revision 18'],
            'unresolved_premise': 'Wait for source changes, then distinguish a promise from an observed refresh.',
        })
        assert agenda.schedule() == []
        before = agenda.snapshot()
        with pytest.raises(ValueError, match='unarrived'):
            agenda.notify_arrival(observation, docs['10_observed_resolution'].body)
        assert agenda.snapshot() == before

        routine = docs['03_routine']
        routine_ev = span(replay, routine, 'I watered the office plants today.', 'operations')
        assert agenda.notify_arrival(routine_ev, routine.body) == []
        assert agenda.schedule() == []
        admit_through(replay, '2001-02-02T15:00:00Z')
        announced = docs['09_patch_announced']
        patch = span(
            replay, announced, 'the next scheduled refresh has not happened.', 'operations'
        )
        assert agenda.notify_arrival(patch, announced.body) == [iid]
        notice = agenda.schedule()[0]
        assert notice['kind'] == 'watch' and notice['agent_id'] == 'operations'
        assert notice['payload']['evidence'] == patch
        assert agenda.snapshot()['inquiries'][0]['status'] != 'closed'
        # Executing this authorized notification makes its exact span locally
        # available. A callback decision, not the watch, determines what it means.
        state.agents['operations'].private_evidence += (patch,)
        agenda.apply('operations', {
            'kind': 'revise', 'inquiry_id': iid, 'evidence': (patch,),
            'change': 'Source patch announced; still awaiting observed post-refresh retention.',
        })
        agenda.finish(notice['id'])
        assert agenda.notify_arrival(patch, announced.body) == []
        assert agenda.schedule() == []

        admit_through(replay, '2001-02-03T08:00:00Z')
        assert agenda.notify_arrival(observation, docs['10_observed_resolution'].body) == [iid]
        observed = agenda.schedule()[0]
        assert observed['kind'] == 'watch'
        state.agents['operations'].private_evidence += (observed['payload']['evidence'],)
        result = agenda.apply('operations', {
            'kind': 'close', 'inquiry_id': iid, 'evidence': (observation,),
            'change': 'One observed refresh retained the correction; no universal future guarantee.',
        })
        agenda.finish(observed['id'])
        assert result.artifacts[0].content['status'] == 'closed'
        assert not result.artifacts[0].verified
        assert result.artifacts[0].metadata['semantic_validation'] is False
        assert 'rule' not in result.artifacts[0].tags
        assert agenda.schedule() == []

        # Arrivals alone are allowed to produce no inquiry or knowledge artifact.
        quiet = SwarmState(agents={'scout': AgentState('scout')})
        empty_agenda = InquiryAgenda(quiet, replay.verify_evidence)
        assert empty_agenda.notify_arrival(routine_ev, routine.body) == []
        assert empty_agenda.schedule() == []
        assert quiet.artifacts == {}
        assert empty_agenda.snapshot()['inquiries'] == []
