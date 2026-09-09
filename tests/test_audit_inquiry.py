import importlib.util
from copy import deepcopy
from pathlib import Path

import pytest

from swarmkit.enron.corpus import EmailCorpus
from swarmkit.enron.investigate import evidence_view
from swarmkit.enron.replay import ReplayCorpus
from swarmkit.serialization import to_data
from swarmkit.types import AgentState, Artifact, Message, SwarmState

spec = importlib.util.spec_from_file_location(
    "audit_inquiry", Path(__file__).parents[1] / "scripts" / "audit_inquiry.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.fixture
def sample(tmp_path):
    master = tmp_path / "master.sqlite"
    arrived = tmp_path / "replay.sqlite"
    with EmailCorpus(master) as corpus:
        corpus.ingest_directory(Path(__file__).parent / "fixtures" / "inquiry_demo")
    with ReplayCorpus(master, arrived) as replay:
        docs = replay.admit_next(2)
        ev = replay.evidence(docs[0].id, 0, 25)
        watermark = {"virtual_time": replay.stats()["virtual_time"], "arrival_sequence": 2}
        history = {"artifact_id": "q:v1", "evidence_ids": [ev.id], "event_sequence": 1, **watermark}
        artifact = Artifact("q:v1", "a", history, evidence=(ev,), tags=frozenset({"inquiry"}))
        message = Message("a", "Request", recipients=("b",), evidence=(ev,))
        state = SwarmState(
            agents={a: AgentState(a) for a in ["a", "b"]},
            artifacts={artifact.id: artifact},
            messages=[message],
        )
        event = {
            "kind": "peer_message",
            "message_id": message.id,
            "sender": "a",
            "recipients": ["b"],
            "evidence": [evidence_view(ev)],
            "event_sequence": 2,
            **watermark,
        }
        run = {
            "history": [history],
            "state_snapshot": to_data(state),
            "posts": [],
            "events": [
                event,
                {"kind": "prompt_exposure", "document_ids": [docs[0].id], "event_sequence": 3, **watermark},
            ],
        }
        yield run, master, arrived, replay, docs


def test_exact_peer_and_historical_artifact_audit(sample):
    run, master, arrived, _, _ = sample
    result = module.audit(run, master, arrived)
    assert result["passed"], result["failures"]
    assert result["checked_records"] == {"posts": 0, "peer_messages": 1, "artifact_versions": 1}
    assert result["checked_citations"] == 2 and result["checked_exposure_documents"] == 1


def test_peer_tamper_and_artifact_history_omission_fail(sample):
    run, master, arrived, _, _ = sample
    bad = deepcopy(run)
    bad["events"][0]["evidence"][0]["quote"] = "invented"
    reasons = {f["reason"] for f in module.audit(bad, master, arrived)["failures"]}
    assert "quote_mismatch" in reasons and "message_snapshot_mismatch" in reasons
    bad = deepcopy(run)
    bad["history"] = []
    assert any(
        f["reason"] == "artifact_versions_missing_from_history"
        for f in module.audit(bad, master, arrived)["failures"]
    )


def test_visibility_uses_recorded_sequence_even_after_admission(sample):
    run, master, arrived, replay, docs = sample
    bad = deepcopy(run)
    bad["events"][1]["document_ids"] = [docs[1].id]
    bad["events"][1]["arrival_sequence"] = 1
    result = module.audit(bad, master, arrived)
    assert not result["passed"]
    assert any(f["reason"] == "not_arrived_at_event_sequence" for f in result["failures"])
