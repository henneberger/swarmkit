"""Scripted offline integration, not a test of model discovery quality."""

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from swarmkit.enron.corpus import EmailCorpus
from swarmkit.enron.inquiry_experiment import InquiryExperiment, InquiryExperimentConfig
from swarmkit.enron.replay import ReplayCorpus
from swarmkit.enron.store import InvestigationStore
from swarmkit.types import AgentState, Usage


class Script:
    def __init__(self, actions=(), malformed=False):
        self.actions = list(actions)
        self.payloads = []
        self.malformed = malformed

    async def complete(self, messages, **kwargs):
        p = json.loads(messages[-1]["content"])
        self.payloads.append(p)
        action = self.actions.pop(0) if self.actions else {"kind": "wait"}
        if action.get("inquiry_id") == "current":
            action = {**action, "inquiry_id": p["inquiry_directory"][0]["inquiry_id"]}
        return SimpleNamespace(
            text="oops"
            if self.malformed
            else json.dumps({"update": "Scripted plumbing check.", "action": action}),
            usage=Usage(calls=0, tokens=12),
            finish_reason="stop",
        )


@pytest.fixture
def corpus(tmp_path):
    master = tmp_path / "master.sqlite"
    with EmailCorpus(master) as c:
        c.ingest_directory(Path(__file__).parent / "fixtures" / "inquiry_demo")
    with ReplayCorpus(master, tmp_path / "replay.sqlite") as r:
        yield r, InvestigationStore(tmp_path / "forum.sqlite")


async def test_sender_partition_temporal_exposure_and_no_forced_findings(corpus):
    replay, store = corpus
    client = Script()
    engine = InquiryExperiment(
        replay,
        store,
        client,
        InquiryExperimentConfig(batch_size=3, max_batches=4, actions_per_batch=4, max_actions=16),
    )
    run = await engine.run()
    assert run["status"] == "completed", run["errors"]
    assert run["metrics"]["model_calls"] == 0 and not run["inquiries"]
    assert run["metrics"]["scheduled_calls"] == len(client.payloads)
    for p in client.payloads:
        for d in p["documents"]:
            assert engine.owner_for(d["outer_sender"]) == p["investigator"]
            assert replay.observation(d["document_id"])["sequence"] <= p["arrival_sequence"]
        assert not p["addressed_messages"]
    assert len(client.payloads) < 16


async def test_agent_selected_search_and_watch_work_are_executed(corpus):
    replay, store = corpus
    client = Script(
        [
            {
                "kind": "open",
                "question": "Did a later import replace the status?",
                "why_matters": "An unresolved mismatch affects the next handoff.",
                "unresolved_premise": "Whether the overnight job changed it.",
            },
            {
                "kind": "search",
                "inquiry_id": "current",
                "query": "all: Quartz refresh",
                "unresolved_premise": "Which job supplied this version?",
            },
            {
                "kind": "watch",
                "inquiry_id": "current",
                "terms": ["Kestrel"],
                "unresolved_premise": "Will a fresh observed result resolve the mismatch?",
            },
        ]
    )
    engine = InquiryExperiment(
        replay,
        store,
        client,
        InquiryExperimentConfig(batch_size=3, max_batches=4, actions_per_batch=3, max_actions=12),
        agents=[AgentState("solo")],
    )
    run = await engine.run()
    assert run["status"] == "completed", run["errors"]
    assert run["metrics"]["action_rejections"] == 0
    assert any(e["kind"] == "historical_retrieval" for e in run["events"])
    assert any(e["kind"] == "watch_wake" for e in run["events"])
    assert any(p["task"]["metadata"]["assignment"]["kind"] == "watch" for p in client.payloads)
    assert run["inquiries"][0]["status"] == "watching"


async def test_malformed_draft_retains_usage_and_continues(corpus):
    replay, store = corpus
    engine = InquiryExperiment(
        replay,
        store,
        Script(malformed=True),
        InquiryExperimentConfig(batch_size=3, max_batches=2, max_actions=8),
    )
    run = await engine.run()
    assert run["status"] == "partial" and not run["errors"]
    assert run["metrics"]["reasoning_rejections"] > 0
    assert run["metrics"]["tokens"] == 12 * run["metrics"]["scheduled_calls"]
    assert run["metrics"]["arrived"] == 6


@pytest.mark.parametrize("exchange", [True, False])
async def test_addressed_recruitment_context_is_withheld_in_ablation(corpus, exchange):
    replay, store = corpus

    class Recruit(Script):
        async def complete(self, messages, **kwargs):
            p = json.loads(messages[-1]["content"])
            kind = p["task"]["metadata"]["assignment"]["kind"]
            action = {"kind": "wait"}
            if not p["inquiry_directory"]:
                action = {
                    "kind": "open",
                    "question": "Which import changed this status?",
                    "why_matters": "Two records may disagree.",
                    "unresolved_premise": "Which update took precedence?",
                }
            elif kind == "investigate":
                target = next(x["id"] for x in p["peer_directory"] if x["id"] != p["investigator"])
                action = {
                    "kind": "request_peer",
                    "inquiry_id": p["inquiry_directory"][0]["inquiry_id"],
                    "recipient": target,
                    "unresolved_premise": "Can your partition explain which refresh won?",
                    "evidence": [p["evidence"][0]["id"]] if p["evidence"] else [],
                }
            self.actions = [action]
            return await super().complete(messages, **kwargs)

    client = Recruit()
    engine = InquiryExperiment(
        replay,
        store,
        client,
        InquiryExperimentConfig(
            batch_size=12, max_batches=1, actions_per_batch=8, max_actions=8, peer_exchange=exchange
        ),
        agents=[AgentState("a"), AgentState("b")],
    )
    run = await engine.run()
    reviews = [p for p in client.payloads if p["task"]["metadata"]["assignment"]["kind"] == "peer_review"]
    assert reviews, run["errors"]
    for prompt in reviews:
        assigned = prompt['task']['metadata']['assignment']['inquiry_id']
        row = next(q for q in prompt['inquiry_directory'] if q['inquiry_id'] == assigned)
        assert not row['joined']
        assert 'join' in row['allowed_inquiry_actions'] and 'watch' not in row['allowed_inquiry_actions']
    assert (
        any(
            m["text"] == "Can your partition explain which refresh won?"
            for p in reviews
            for m in p["addressed_messages"]
        )
        == exchange
    )
    if not exchange:
        assert all(
            set(q) <= {"inquiry_id", "question", "owner", "status", "joined", "allowed_inquiry_actions"}
            for p in reviews
            for q in p["inquiry_directory"]
        )
    assert any(e["kind"] == "peer_message" for e in run["events"])


def test_cli_status_accepts_inquiry_peer_records(tmp_path, capsys):
    from swarmkit.enron.cli import main

    store = InvestigationStore(tmp_path / "forum.sqlite")
    store.save_run(
        {
            "id": "inquiry-test",
            "status": "partial",
            "mode": "inquiry_swarm",
            "peers": [{"id": "investigator-1", "capabilities": []}],
        }
    )
    main(["--workspace", str(tmp_path), "--ledger", str(tmp_path / "ledger.sqlite"), "status"])
    status = json.loads(capsys.readouterr().out)
    assert status["gate"]["peers"][0]["id"] == "investigator-1"


async def test_resume_keeps_membership_actions_private_state_and_batch_ceiling(corpus):
    replay, store = corpus

    class Interrupt(Script):
        async def complete(self, messages, **kwargs):
            if len(self.payloads) == 1:
                raise RuntimeError("simulated unavailable provider")
            return await super().complete(messages, **kwargs)

    config = InquiryExperimentConfig(batch_size=3, max_batches=4, actions_per_batch=1, max_actions=8)
    original = InquiryExperiment(replay, store, Interrupt(), config, agents=[AgentState("solo")])
    first = await original.run()
    assert first["status"] == "incomplete" and first["metrics"]["arrived"] == 6
    assert first["metrics"]["scheduled_calls"] == 2
    client = Script()
    resumed = InquiryExperiment(replay, store, client, resume_run_id=first["id"])
    assert resumed.state.agents["solo"].memory["evidence"]
    final = await resumed.run()
    assert final["id"] == first["id"] and final["metrics"]["arrived"] == 12
    assert final["resume_state"]["batches_processed"] == 4
    assert final["metrics"]["scheduled_calls"] == 4
    assert all(p["arrival_sequence"] > 6 for p in client.payloads)
    assert len(final["posts"]) == 3 and final["resume_history"][0]["prior_errors"]
    assert any(e["kind"] == "lost_assignment" for e in final["events"])
    assert final["metrics"]["tokens"] == 36


async def test_duplicate_read_proposal_never_queues_another_paid_read(corpus):
    replay, store = corpus

    class Repeater(Script):
        async def complete(self, messages, **kwargs):
            p = json.loads(messages[-1]["content"])
            if p["documents"]:
                docid = p["documents"][0]["document_id"]
                self.actions = [{"kind": "read", "document_id": docid, "offset": 0}]
            return await super().complete(messages, **kwargs)

    client = Repeater()
    engine = InquiryExperiment(
        replay,
        store,
        client,
        InquiryExperimentConfig(batch_size=3, max_batches=1, actions_per_batch=5, max_actions=5),
        agents=[AgentState("solo")],
    )
    result = await engine.run()
    assert len(client.payloads) == 2
    assert result["metrics"]["action_rejections"] == 1
    assert not engine.agenda.data["pending"]


@pytest.mark.parametrize("legacy", [False, True])
async def test_ledger_segments_resume_sum_once_and_exclude_between_session_activity(corpus, legacy):
    replay, store = corpus

    class FakeGate:
        calls = 0

        def status(self):
            return {"calls": self.calls, "tokens": self.calls * 10, "cost_usd": self.calls * 0.01}

    gate = FakeGate()

    class Metered(Script):
        def __init__(self, fail=False):
            super().__init__()
            self.gate = gate
            self.fail = fail

        async def complete(self, messages, **kwargs):
            gate.calls += 1
            if self.fail and gate.calls == 2:
                raise RuntimeError("simulated charged failure")
            return await super().complete(messages, **kwargs)

    config = InquiryExperimentConfig(batch_size=3, max_batches=4, actions_per_batch=1, max_actions=8)
    engine = InquiryExperiment(replay, store, Metered(fail=True), config, agents=[AgentState("solo")])
    first = await engine.run()
    assert first["shared_ledger_delta"]["calls"] == 2
    if legacy:
        del first["ledger_segments"]
        store.save_run({k: v for k, v in first.items() if k not in ("posts", "events")})
    gate.calls += 7  # unrelated activity while this run is stopped
    result = await InquiryExperiment(replay, store, Metered(), resume_run_id=first["id"]).run()
    assert result["shared_ledger_delta"]["calls"] == 4
    assert len(result["ledger_segments"]) == 2
    assert [s["delta"]["calls"] for s in result["ledger_segments"]] == [2, 2]
    assert result["resume_history"][-1]["prior_shared_ledger_delta"]["calls"] == 2
    assert result["ledger_accounting_complete"]
    assert result["ledger_segments"][0]["kind"] == ("imported_prior_aggregate" if legacy else "execution")


@pytest.mark.asyncio
async def test_factual_reply_reaches_requester_without_forcing_an_inquiry(corpus):
    replay, store = corpus

    class Conversation(Script):
        def __init__(self):
            super().__init__()
            self.asked = False

        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            assignment = payload["task"]["metadata"]["assignment"]
            action = {"kind": "wait"}
            if not self.asked:
                self.asked = True
                target = next(
                    peer["id"] for peer in payload["peer_directory"] if peer["id"] != payload["investigator"]
                )
                action = {
                    "kind": "request_peer",
                    "recipient": target,
                    "question": "Which refresh result did you observe?",
                }
            elif assignment["kind"] == "peer_review":
                question = next(
                    m for m in payload["addressed_messages"] if m["id"] == assignment["request_id"]
                )
                action = {
                    "kind": "reply",
                    "recipient": question["sender"],
                    "answer": "No relevant refresh evidence in my current context.",
                }
            self.actions = [action]
            return await super().complete(messages, **kwargs)

    client = Conversation()
    engine = InquiryExperiment(
        replay,
        store,
        client,
        InquiryExperimentConfig(batch_size=12, max_batches=1, actions_per_batch=8, max_actions=8),
        agents=[AgentState("a"), AgentState("b")],
    )
    run = await engine.run()
    assert not run["inquiries"] and not run["errors"]
    assert run["metrics"]["action_rejections"] == 0
    reactions = [p for p in client.payloads if p["task"]["metadata"]["assignment"]["kind"] == "react"]
    assert reactions
    assert any(
        m["text"].startswith("No relevant refresh evidence in my current context.")
        for p in reactions
        for m in p["addressed_messages"]
    )
    replies = [e for e in run["events"] if e["kind"] == "peer_message" and e["action"] == "reply"]
    assert len(replies) == 1 and replies[0]["evidence"] == []


async def test_no_watch_does_not_parse_every_arrived_document(corpus):
    replay,store=corpus
    original=replay.segments
    parsed=[]
    def tracked(docid):
        parsed.append(docid)
        return original(docid)
    replay.segments=tracked
    engine=InquiryExperiment(replay,store,Script(),InquiryExperimentConfig(batch_size=12,max_batches=1,
        actions_per_batch=1,max_actions=1,docs_per_agent=2),agents=[AgentState('solo')])
    result=await engine.run()
    assert result['metrics']['arrived']==12
    assert len(set(parsed))==2 # only prompt sample, not the full batch
    assert result['sampling_version']=='sender-partition-stable-hash-v2'


def test_distinct_watches_same_inquiry_both_wake_in_one_batch(corpus):
    replay,store=corpus
    engine=InquiryExperiment(replay,store,Script(),agents=[AgentState('solo')])
    iid=engine.agenda.apply('solo',{'kind':'open','question':'Which version prevailed?',
        'why_matters':'The two systems could disagree.','unresolved_premise':'Which source and outcome explain this?'}).metadata['inquiry_id']
    for terms in (['ticket A41'],['destination QZ-7']):
        engine.agenda.apply('solo',{'kind':'watch','inquiry_id':iid,'terms':terms})
    arrivals=replay.admit_next_metadata(2)
    engine._process_arrivals(arrivals,{'solo':[]})
    queued=[q for q in engine.agenda.data['pending'] if q['kind']=='watch']
    assert {q['payload']['watch'] for q in queued}=={0,1}
    assert len({q['payload']['evidence'].metadata['document_id'] for q in queued})==2


def test_historical_peer_coverage_resurfaces_without_unobserved_or_future_sources(tmp_path):
    mail=tmp_path/'mail';mail.mkdir()
    for i in range(43):
        subject='Quartz vendor overwrite dependency' if i==0 else f'Unrelated catering timetable {i}'
        (mail/str(i)).write_text(f'From: sender{i}@example.test\nTo: team@example.test\nDate: Mon, 01 Jan 2001 00:{i:02}:00 +0000\nSubject: {subject}\nMessage-ID: <coverage-{i}@example.test>\n\nPrivate source body {i}: this quote must never appear in coverage descriptors.\n')
    path=tmp_path/'master.sqlite'
    with EmailCorpus(path) as master:
        master.ingest_directory(mail)
        future=next(d for d in master.search('timetable',limit=50) if d.subject.endswith('42'))
    with ReplayCorpus(path,tmp_path/'arrived.sqlite') as replay:
        store=InvestigationStore(tmp_path/'forum.sqlite')
        engine=InquiryExperiment(replay,store,Script(),agents=[AgentState('a'),AgentState('b')])
        docs=replay.admit_next(42)
        engine._on_exposure({'agent':'b','document_ids':[d.id for d in docs[:41]],**engine._watermark()})
        assert len(engine.coverage['b'])==8 and all('Quartz' not in d['subject'] for d in engine.coverage['b'])
        peers=engine._peer_directory('Which Quartz vendor overwrite dependency explains the mismatch?')
        result=next(p for p in peers if p['id']=='b')
        assert result['coverage'][0]['subject']=='Quartz vendor overwrite dependency'
        assert len(result['coverage'])==8 and result['coverage_descriptor_count']==41
        assert all(set(item)=={'sender','subject'} for item in result['coverage'])
        assert next(p for p in peers if p['id']=='a')['coverage']==[]
        assert docs[41].id not in engine.coverage_archive['b']
        with pytest.raises(ValueError):
            engine._record_coverage('b',future.id)
        engine._persist()
        saved=store.run(engine.id)
        del saved['resume_state']['coverage_archive'] # legacy checkpoint backfill from exposure events
        store.save_run({k:v for k,v in saved.items() if k not in ('posts','events')})
        restored=InquiryExperiment(replay,store,Script(),resume_run_id=engine.id)
        assert len(restored.coverage_archive['b'])==41
        assert restored._peer_directory('Quartz vendor')[1]['coverage'][0]['subject'].startswith('Quartz')


def test_fact_probe_opt_in_selective_once_and_no_auto_join(corpus):
    replay,store=corpus
    engine=InquiryExperiment(replay,store,Script(),agents=[AgentState('a'),AgentState('b')],peer_fact_probes=True)
    docs=replay.admit_next(2)
    engine._on_exposure({'agent':'b','document_ids':[docs[1].id],**engine._watermark()})
    iid=engine.agenda.apply('a',{'kind':'open','question':'Which Quartz importer destination explains the overwrite?',
        'why_matters':'The source may differ from the displayed correction.','unresolved_premise':'Which destination does Quartz overwrite?'}).metadata['inquiry_id']
    engine._maybe_fact_probe(iid)
    engine._maybe_fact_probe(iid)
    messages=[m for m in engine.state.messages if m.metadata.get('initiation')=='host_assisted_fact_probe_v1']
    assert len(messages)==1 and messages[0].recipients==('b',)
    assert engine.agenda.data['inquiries'][iid]['participants']==['a']
    assert engine.agenda.data['actions_used']==0 # queued work consumes budget on dispatch
    assert len([q for q in engine.agenda.data['pending'] if q['kind']=='peer_review'])==1
    other=engine.agenda.apply('a',{'kind':'open','question':'What explains the submarine expedition?',
        'why_matters':'An independent question.','unresolved_premise':'Which expedition returned?'}).metadata['inquiry_id']
    engine._maybe_fact_probe(other)
    assert engine.record['metrics']['host_assisted_fact_probes']==1


async def test_exploration_does_not_inject_full_unassigned_owned_inquiries(corpus):
    replay,store=corpus;client=Script()
    engine=InquiryExperiment(replay,store,client,agents=[AgentState('solo')])
    docs=replay.admit_next(2)
    iid=engine.agenda.apply('solo',{'kind':'open','question':'An older unrelated question?',
        'why_matters':'Old context not relevant to the new source.','unresolved_premise':'A prior missing fact.'}).metadata['inquiry_id']
    initial=engine.agenda.schedule()[0];engine.agenda.finish(initial['id'])
    engine.agenda.enqueue_exploration('solo',{'document_ids':[docs[1].id]})
    await engine._dispatch()
    p=client.payloads[0]
    assert 'Scout NEW developments' in p['task']['description']
    row=next(q for q in p['inquiry_directory'] if q['inquiry_id']==iid)
    assert 'why_matters' not in row and 'unresolved_premise' not in row
    assert not any(m['text']=='Subscribed inquiry context.' for m in p['addressed_messages'])


def test_resume_enabling_probe_does_not_recruit_for_old_questions(corpus):
    replay,store=corpus
    engine=InquiryExperiment(replay,store,Script(),agents=[AgentState('a'),AgentState('b')])
    replay.admit_next(1)
    engine.agenda.apply('a',{'kind':'open','question':'An existing inquiry?',
        'why_matters':'Previously opened.','unresolved_premise':'A prior unknown.'})
    engine._persist()
    restored=InquiryExperiment(replay,store,Script(),resume_run_id=engine.id,peer_fact_probes=True)
    assert restored.peer_fact_probes
    assert not any(q['kind']=='peer_review' for q in restored.agenda.data['pending'])
    assert any(e['kind']=='protocol_intervention' for e in store.run(engine.id)['events'])


async def test_assigned_owned_artifact_is_context_not_a_synthetic_message(corpus):
    replay,store=corpus;client=Script()
    engine=InquiryExperiment(replay,store,client,agents=[AgentState('solo')])
    doc=replay.admit_next(1)[0]
    evidence=replay.evidence(doc.id,0,min(80,len(doc.body)),owner='solo')
    iid=engine.agenda.apply('solo',{'kind':'open','question':'Which correction actually persisted?',
        'why_matters':'The observed outcome is incomplete.','evidence':[evidence]}).metadata['inquiry_id']
    await engine._dispatch()
    p=client.payloads[0]
    assert p['task']['metadata']['assignment']['inquiry_id']==iid
    assert p['addressed_messages']==[]
    assert any(q['inquiry_id']==iid and 'why_matters' in q for q in p['inquiry_directory'])
    assert any(e['document_id']==doc.id for e in p['evidence'])


def test_host_probe_requires_observed_named_matter_anchor(corpus):
    replay,store=corpus
    engine=InquiryExperiment(replay,store,Script(),agents=[AgentState('a'),AgentState('b')],peer_fact_probes=True)
    # Public descriptor-only unit fixture: generic paperwork cannot establish ABB coverage.
    engine.coverage_archive['b']={'old':{'sender':'legal@example.test','subject':'Project execution confirmation letter document email signing'}}
    def open_question(text):
        return engine.agenda.apply('a',{'kind':'open','question':text,'why_matters':'Determine what actually happened.',
            'unresolved_premise':'Whether the authorization was executed.'}).metadata['inquiry_id']
    iid=open_question('Was the ABB authorization letter for the Austin Project executed?')
    engine._maybe_fact_probe(iid)
    assert not engine.state.messages
    # An actually observed descriptor is the input boundary, tested separately by coverage tests.
    engine.coverage_archive['b']['older-relevant']={'sender':'counterparty@example.test','subject':'ABB Austin authorization'}
    next_id=open_question('Did ABB authorize the Austin installation despite signing uncertainty?')
    engine._maybe_fact_probe(next_id)
    assert len(engine.state.messages)==1
    assert set(engine.state.messages[0].metadata['matched_named_anchors'])=={'abb','austin'}
    nameless=open_question('Did the authorization confirmation letter get executed?')
    engine._maybe_fact_probe(nameless)
    assert len(engine.state.messages)==1
