"""Offline chronological integration: temporal scopes, peer exchange and gating."""

import json
from types import SimpleNamespace

import pytest

from swarmkit.enron.corpus import EmailCorpus
from swarmkit.enron.replay import ReplayCorpus
from swarmkit.enron.store import InvestigationStore
from swarmkit.enron.stream import ChronologicalSwarm, StreamConfig, StreamOfflineClient
from swarmkit.types import Usage


@pytest.fixture
def stream_setup(tmp_path):
    files = tmp_path / "mail"
    files.mkdir()
    for index in range(12):
        (files / str(index)).write_text(
            f"From: colleague{index}@example.test\nTo: team@example.test\n"
            f"Message-ID: <replay-{index}@example.test>\nDate: Mon, 1 Jan 2001 {index:02}:00:00 +0000\n"
            f"Subject: Routine episode {index}\n\n"
            f"Episode number {index} records a separate ordinary handoff and a colleague asking for context.\n"
            "The recipient asks the original coordinator to explain the expected review sequence.\n"
        )
    master = tmp_path / "master.sqlite"
    with EmailCorpus(master) as corpus:
        corpus.ingest_directory(files)
    with ReplayCorpus(master, tmp_path / "arrived.sqlite") as replay:
        yield replay, InvestigationStore(tmp_path / "forum.sqlite")


class CaptureClient(StreamOfflineClient):
    def __init__(self):
        self.payloads = []

    async def complete(self, messages, **kwargs):
        self.payloads.append(json.loads(messages[-1]["content"]))
        return await super().complete(messages, **kwargs)


async def test_full_auto_coverage_snapshot_exchange_and_zero_paid_offline_calls(stream_setup):
    replay, store = stream_setup
    client = CaptureClient()
    engine = ChronologicalSwarm(replay, store, client, StreamConfig(max_windows=3, documents_per_window=4))
    run = await engine.run()
    assert run["status"] == "completed"
    assert run["replay"]["arrived"] == 12 and run["replay"]["coverage_complete"]
    assert run["replay"]["model_calls"] == 0
    assert run["runtime_usage"]["calls"] == 24
    assert [window["arrival_sequence"] for window in run["windows"]] == [4, 8, 12]
    assert len(run["posts"]) == 24
    assert all(
        len(payload["peer_messages"]) == 3 for payload in client.payloads if payload["phase"] == "revise"
    )
    for post in run["posts"]:
        for ev in post["evidence"]:
            assert replay.observation(ev["document_id"])["sequence"] <= post["arrival_sequence"]
            assert replay.get(ev["document_id"]).date_utc <= post["virtual_time"]
    for payload in client.payloads:
        for doc in payload["documents"]:
            assert replay.observation(doc["document_id"])["sequence"] <= payload["arrival_sequence"]
    assert any(event["kind"] == "prompt_exposure" for event in run["events"])


async def test_explicit_small_scope_partial_and_resume_rejected(stream_setup):
    replay, store = stream_setup
    run = await ChronologicalSwarm(
        replay, store, StreamOfflineClient(), StreamConfig(batch_size=2, max_windows=2)
    ).run()
    assert run["status"] == "partial"
    assert run["replay"]["arrived"] == 4
    assert not run["replay"]["coverage_complete"]
    with pytest.raises(ValueError, match="fresh membership"):
        ChronologicalSwarm(replay, store, StreamOfflineClient())


async def test_malformed_response_is_accounted_abstention_and_later_windows_continue(stream_setup):
    replay, store = stream_setup

    class Broken:
        calls = 0

        async def complete(self, *args, **kwargs):
            self.calls += 1
            return SimpleNamespace(text="invalid JSON", usage=Usage(calls=1, tokens=9, cost=0.001))

    client = Broken()
    run = await ChronologicalSwarm(replay, store, client, StreamConfig(max_windows=3)).run()
    assert run["status"] == "completed_with_rejections"
    assert run["replay"]["coverage_complete"] and run["replay"]["arrived"] == 12
    assert client.calls == run["replay"]["model_calls"] == 24
    assert run["reasoning_rejections"] == 24
    assert run["runtime_usage"]["tokens"] == 24 * 9
    assert run["runtime_usage"]["cost"] == pytest.approx(0.024)
    assert run["agent_errors"] == []
    assert len(run["windows"]) == 3
    assert all(not post["evidence"] and post["reasoning_rejection"] for post in run["posts"])


async def test_large_admission_request_is_chunked(stream_setup):
    replay, store = stream_setup
    batches = []
    original = replay.admit_next_metadata

    def logged(batch_size=100, **kwargs):
        batches.append(batch_size)
        return original(batch_size, **kwargs)

    replay.admit_next_metadata = logged
    run = await ChronologicalSwarm(
        replay, store, StreamOfflineClient(), StreamConfig(batch_size=22000, max_windows=1)
    ).run()
    assert batches and max(batches) <= 10000
    assert run["replay"]["arrived"] == 12


async def test_prediction_watermark_survives_revision_and_requires_later_sources(stream_setup):
    replay, store = stream_setup

    class Rules(StreamOfflineClient):
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            result = await super().complete(messages, **kwargs)
            data = json.loads(result.text)
            refs = [segment["span_id"] for doc in payload["documents"] for segment in doc["segments"]]
            refs += [ev["id"] for ev in payload["evidence"]]
            if refs:
                hypothesis = {
                    "unwritten_rule": "People appear to route unclear handoffs back to a coordinator.",
                    "applies_when": "The recipient lacks context.",
                    "exceptions": "Independent expertise may suffice.",
                    "alternative": "The visible cases may be a sample artifact.",
                    "uncertainty": f"Needs more cases at sequence {payload['arrival_sequence']}.",
                    "next_query": "all: coordinator context",
                    "supporting_evidence": [refs[0]],
                    "counter_evidence": [],
                    "prediction": "A later recipient will ask the coordinator for context.",
                }
                if payload["hypotheses"]:
                    hypothesis["hypothesis_id"] = payload["hypotheses"][0]["hypothesis_id"]
                data["hypotheses"] = [hypothesis]
                if payload["pending_predictions"]:
                    assert set(payload["pending_predictions"][0]) == {
                        "prediction_id",
                        "hypothesis_id",
                        "prediction",
                        "window",
                        "arrival_sequence",
                    }
                    data["prediction_checks"] = [
                        {
                            "hypothesis_id": payload["pending_predictions"][0]["hypothesis_id"],
                            "status": "supported",
                            "evidence_ids": [refs[0]],
                            "explanation": "A new arrival records a request.",
                        }
                    ]
            return SimpleNamespace(text=json.dumps(data), usage=Usage(calls=0), finish_reason="stop")

    run = await ChronologicalSwarm(
        replay, store, Rules(), StreamConfig(max_windows=3, documents_per_window=4)
    ).run()
    assert run["status"] == "completed"
    assert run["wiki"] and all(row["phase"] in ("observe", "revise") for row in run["wiki"])
    predictions = run["predictions"]
    assert len({item["hypothesis_id"] for item in predictions}) == len(predictions)
    first = predictions[0]
    assert first["arrival_sequence"] == 4
    checks = [event for event in run["events"] if event["kind"] == "prediction_check"]
    assert checks
    assert all(event["arrival_sequence"] > event["prediction_arrival_sequence"] for event in checks)
    assert any(post["prediction_checks"] for post in run["posts"])


async def test_diagnostics_separate_schema_rejections_from_valid_quotes_and_redact_keys(stream_setup):
    replay, store = stream_setup

    class WrongType(StreamOfflineClient):
        _api_key = "LOCAL-DIAGNOSTIC-SECRET"

        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            result = await super().complete(messages, **kwargs)
            data = json.loads(result.text)
            refs = [segment["span_id"] for doc in payload["documents"] for segment in doc["segments"]]
            if refs:
                data["hypotheses"] = [
                    {
                        "unwritten_rule": "LOCAL-DIAGNOSTIC-SECRET rule",
                        "applies_when": "A handoff happens.",
                        "exceptions": [],
                        "alternative": "Unknown.",
                        "uncertainty": "Unreviewed.",
                        "next_query": "coordinator context",
                        "supporting_evidence": [refs[0]],
                        "counter_evidence": [],
                    }
                ]
            return SimpleNamespace(text=json.dumps(data), usage=Usage(calls=0))

    run = await ChronologicalSwarm(
        replay,
        store,
        WrongType(),
        StreamConfig(batch_size=4, max_windows=1, turns_per_window=1, documents_per_window=4),
    ).run()
    assert run["quote_checks"] == {"accepted": 4, "rejected": 0}
    assert run["validation_rejections"]["hypotheses"] == 4
    rejected = [e for e in run["events"] if e["kind"] == "hypothesis_rejected"]
    assert all(e["invalid_fields"]["exceptions"] == "list" for e in rejected)
    assert all(e["candidate"]["exceptions"] == [] for e in rejected)
    assert len([e for e in run["events"] if e["kind"] == "reasoning_draft"]) == 4
    assert "LOCAL-DIAGNOSTIC-SECRET" not in json.dumps(run["events"])


def test_source_aliases_stay_bound_across_document_order_and_claim_changes(stream_setup):
    from swarmkit.enron.stream import _stable_ref

    replay, store = stream_setup
    engine = ChronologicalSwarm(replay, store, StreamOfflineClient())
    docs = replay.admit_next(4)
    _, first = engine._prompt_sources(docs)
    _, reordered = engine._prompt_sources(list(reversed(docs)))
    assert set(first) == set(reordered)
    for key, evidence in first.items():
        assert key.startswith("v")
        assert evidence.metadata == reordered[key].metadata
        altered = replay.evidence(
            evidence.metadata["document_id"],
            evidence.metadata["start"],
            evidence.metadata["end"],
            claim="A different unverified claim.",
            owner="peer",
        )
        assert _stable_ref(altered.metadata) == key


def test_reworded_evidence_claim_alone_does_not_create_rule_revision(stream_setup):
    from swarmkit.types import AlgorithmResult, Artifact

    replay, store = stream_setup
    engine = ChronologicalSwarm(replay, store, StreamOfflineClient())
    doc = replay.admit_next(1)[0]
    one = replay.evidence(doc.id, 0, 50, claim="Initial claim.", owner="routines")
    two = replay.evidence(doc.id, 0, 50, claim="Changed claim attached to same quote.", owner="expertise")
    content = {
        "hypothesis_id": "h-fixed",
        "unwritten_rule": "An observed handoff.",
        "applies_when": "In this episode.",
        "exceptions": "Unknown.",
        "alternative": "One-off request.",
        "uncertainty": "Unreviewed.",
        "next_query": "other handoff",
        "prediction": "",
        "knowledge_type": "observation",
        "inference_gap": "",
        "evidence_basis": "One episode.",
        "counter_evidence": (),
        "window": 1,
        "phase": "observe",
        "virtual_time": doc.date_utc,
        "arrival_sequence": 1,
        "status": "provisional; transfer untested",
    }
    engine._publish(AlgorithmResult(artifacts=(Artifact("a-one", "routines", content, evidence=(one,)),)))
    engine._publish(AlgorithmResult(artifacts=(Artifact("a-two", "expertise", content, evidence=(two,)),)))
    assert len(engine.record["wiki"]) == 1


async def test_paging_keeps_exact_offsets_and_refuses_future_or_invalid_reads(tmp_path):
    from swarmkit.types import AgentContext, AgentState, Task

    files = tmp_path / "pages"
    files.mkdir()
    body = "A" * 697 + "get" + " the complete supporting context before interpreting this clause. " * 30
    for hour in (0, 1):
        (files / str(hour)).write_text(
            f"From: peer@example.test\nTo: team@example.test\n"
            f"Date: Mon, 1 Jan 2001 0{hour}:00:00 +0000\nSubject: Page {hour}\n\n{body}"
        )
    master = tmp_path / "master.sqlite"
    with EmailCorpus(master) as corpus:
        corpus.ingest_directory(files)
        future_id = next(doc.id for doc in corpus.search("Page", limit=2) if doc.subject == "Page 1")
    with ReplayCorpus(master, tmp_path / "membership.sqlite") as replay:
        store = InvestigationStore(tmp_path / "forum.sqlite")
        engine = ChronologicalSwarm(replay, store, StreamOfflineClient())
        doc = replay.admit_next(1)[0]
        views, refs = engine._prompt_sources([doc])
        first = views[0]["segments"][0]
        assert first["text"].endswith("get")
        assert first["start"] == 0 and first["end"] == 700 and first["truncated"]
        assert first["next_read"] == f"read: {doc.id} 700"
        engine._sequence, engine._virtual_time = 1, doc.date_utc

        def context(query):
            return AgentContext(
                Task("page", "Read context"),
                AgentState("routines", memory={"queries": [query]}),
                phase="revise",
            )

        output = await engine._act(context(first["next_read"]))
        evidence = output.messages[0].evidence[0]
        assert evidence.metadata["start"] == 700
        assert evidence.metadata["quote"] == doc.body[700:1400]
        assert evidence.metadata["excerpt_truncated"]
        assert evidence.metadata["next_read"] == f"read: {doc.id} 1400"
        assert output.memory_updates["evidence"][evidence.id].metadata == evidence.metadata
        assert replay.verify_evidence(evidence)
        for query in (
            f"read: {future_id} 0",
            f"read: {doc.id} 999999",
            f"read: {doc.id} -1",
            "read: ../../private-file 0",
        ):
            output = await engine._act(context(query))
            assert output.messages[0].evidence == ()
        rejected = [e for e in store.run(engine.id)["events"] if e["kind"] == "history_read_rejected"]
        assert len(rejected) == 4
        assert replay.count() == 1


async def test_identical_rule_and_scope_reuse_existing_id_when_model_omits_it(stream_setup):
    from swarmkit.types import AgentContext, AgentState, AlgorithmResult, Task

    replay, store = stream_setup

    class Repeater(StreamOfflineClient):
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            ref = payload["documents"][0]["segments"][0]["span_id"]
            data = {
                "summary": "The same local observation.",
                "queries": [],
                "observations": [],
                "prediction_checks": [],
                "hypotheses": [
                    {
                        "unwritten_rule": "A recipient asks for context.",
                        "applies_when": "In this episode.",
                        "exceptions": "Unknown.",
                        "alternative": "One-off request.",
                        "uncertainty": "Needs comparison.",
                        "next_query": "different handoff",
                        "supporting_evidence": [ref],
                        "counter_evidence": [],
                    }
                ],
            }
            return SimpleNamespace(text=json.dumps(data), usage=Usage(calls=0))

    engine = ChronologicalSwarm(replay, store, Repeater())
    engine._selected = replay.admit_next(4)
    context = AgentContext(Task("same", "Observe"), AgentState("routines"), phase="observe")
    for _ in range(2):
        output = await engine._act(context)
        engine._publish(AlgorithmResult(messages=output.messages, artifacts=output.artifacts))
    assert len(engine.record["wiki"]) == 1


async def test_singleton_collections_do_not_invent_missing_hypothesis_support(stream_setup):
    replay, store = stream_setup

    class Singleton(StreamOfflineClient):
        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1]["content"])
            segments = [s for doc in payload["documents"] for s in doc["segments"]]
            data = {
                "summary": "A valid observation and an unsupported candidate.",
                "queries": ["use all: coordinator context"],
                "observations": {"span_id": segments[0]["span_id"], "claim": "Recorded request."}
                if segments
                else [],
                "hypotheses": {"unwritten_rule": "An unsupported rule with missing required fields."},
            }
            return SimpleNamespace(text=json.dumps(data), finish_reason="stop", usage=Usage(calls=0))

    run = await ChronologicalSwarm(
        replay, store, Singleton(), StreamConfig(batch_size=4, max_windows=1, documents_per_window=4)
    ).run()
    assert run["wiki"] == []
    assert run["reasoning_rejections"] == 0
    assert run["validation_rejections"]["hypotheses"] == 8
    assert run["quote_checks"]["accepted"] > 0 and run["quote_checks"]["rejected"] == 0
    searches = [e for e in run["events"] if e["kind"] == "historical_retrieval"]
    assert searches and all(e["match"] == "all" and e["query"] == "coordinator context" for e in searches)


async def test_hard_provider_failure_still_disables_later_reasoning(stream_setup):
    from swarmkit.providers.deepseek import ProviderError

    replay, store = stream_setup

    class Unavailable:
        calls = 0

        async def complete(self, *args, **kwargs):
            self.calls += 1
            raise ProviderError("provider unavailable")

    client = Unavailable()
    run = await ChronologicalSwarm(replay, store, client, StreamConfig(max_windows=3)).run()
    assert run["status"] == "incomplete"
    assert client.calls == 4
    assert run["replay"]["coverage_complete"]
    assert len(run["agent_errors"]) == 4
