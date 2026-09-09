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
            set(q) <= {"inquiry_id", "question", "owner", "status"}
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
