from pathlib import Path
from types import SimpleNamespace

from swarmkit.enron.corpus import EmailCorpus
from swarmkit.enron.inquiry_experiment import InquiryExperiment
from swarmkit.enron.inquiry_recovery import recover_peer_requests
from swarmkit.enron.replay import ReplayCorpus
from swarmkit.enron.store import InvestigationStore
from swarmkit.types import AgentState, Message


def test_recovery_preserves_original_request_and_does_not_charge_or_repeat(tmp_path):
    corpus_path = tmp_path / "corpus.sqlite"
    with EmailCorpus(corpus_path) as corpus:
        corpus.ingest_directory(Path(__file__).parent / "fixtures" / "inquiry_demo")
    with ReplayCorpus(corpus_path, tmp_path / "arrivals.sqlite") as replay:
        store = InvestigationStore(tmp_path / "forum.sqlite")
        engine = InquiryExperiment(
            replay, store, SimpleNamespace(), agents=[AgentState("a"), AgentState("b")]
        )
        replay.admit_next(3)
        action = {"kind": "request_peer", "recipient": "b", "question": "Which refresh was observed?"}
        original = Message("a", "Ask for the missing fact.", recipients=("a",), metadata={"action": action})
        engine.state.messages.append(original)
        engine._persist()
        store.post(
            engine.id,
            {
                "id": original.id,
                "action": action,
                "reasoning_rejected": True,
                "virtual_time": "2001-02-01T09:00:00+00:00",
            },
        )
        assert recover_peer_requests(engine) == 1
        assert engine.state.agents["b"].inbox[0].content == action["question"]
        assert engine.agenda.data["actions_used"] == 0
        assert engine.agenda.data["pending"][0]["kind"] == "peer_review"
        assert engine.state.data["recovered_peer_request_posts"] == [original.id]
        assert recover_peer_requests(engine) == 0
        assert len(engine.state.agents["b"].inbox) == 1
        event = next(e for e in store.run(engine.id)["events"] if e["kind"] == "peer_message")
        assert event["recovered_from_post"] == original.id
        assert event["arrival_sequence"] == 3
