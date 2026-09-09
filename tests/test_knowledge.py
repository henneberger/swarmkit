from dataclasses import replace

import pytest

from swarmkit.knowledge import (
    ArtifactStore,
    CulturalTransfer,
    DecayingMemory,
    EvidenceRegistry,
    PeerAdoption,
    ProcedureAbstraction,
)
from swarmkit.types import AgentState, Artifact, Evidence, Feedback, SwarmState, Task


def fact(key, source, *, parents=(), confidence=1, supports=("yes",)):
    return Evidence(key, key, source, "agent", confidence, supports, parents=parents)


def verified(artifact):
    return Feedback(float(artifact.content["score"]), verified=artifact.content.get("valid", True))


def test_evidence_ancestry_and_same_source_do_not_multiply_support():
    root = fact("root", "experiment")
    copies = [fact(f"copy{i}", f"blog{i}", parents=("root",)) for i in range(15)]
    registry = EvidenceRegistry([*copies, root, fact("same", "experiment")])
    assert registry.scores(("yes", "no")) == {"yes": 1, "no": 0}
    registry.add(fact("independent", "experiment2"))
    assert registry.scores(("yes",))["yes"] == 2
    assert registry.roots("copy1") == frozenset({"experiment"})


def test_derived_multisource_confidence_is_not_duplicated():
    registry = EvidenceRegistry(
        [fact("a", "a", supports=()), fact("b", "b", supports=()), fact("c", "new", parents=("a", "b"))]
    )
    assert registry.scores(("yes",))["yes"] == 1


def test_cycles_missing_parents_and_conflicting_ids_are_transactional():
    registry = EvidenceRegistry([fact("root", "r")])
    with pytest.raises(ValueError):
        registry.add_many([fact("good", "g"), fact("a", "a", parents=("b",)), fact("b", "b", parents=("a",))])
    assert len(registry.evidence) == 1
    with pytest.raises(ValueError):
        registry.add(fact("root", "different"))
    with pytest.raises(ValueError):
        registry.add(fact("self", "self", parents=("self",)))


def test_store_verifies_copies_and_keeps_retired_lineage():
    store = ArtifactStore(verified)
    content = {"score": 1, "payload": []}
    store.admit(Artifact("p", "alice", content))
    content["payload"].append("outside mutation")
    view = store.get("p")
    view.content["payload"].append("read mutation")
    assert store.get("p").content["payload"] == []
    child = store.admit(Artifact("c", "bob", {"score": 2}, parents=("p",)))
    assert child.verified and store.lineage("c") == ("p", "c")
    store.retire("p", "superseded")
    assert [a.id for a in store.active] == ["c"]
    assert store.get("p").id == "p"
    with pytest.raises(ValueError):
        store.get("p", active_only=True)
    with pytest.raises(ValueError):
        store.admit(Artifact("bad", "a", {"score": 1, "valid": False}, verified=True))
    with pytest.raises(ValueError):
        store.admit(Artifact("cycle", "a", {"score": 1}, parents=("cycle",)))
    with pytest.raises(ValueError):
        store.admit(replace(child, parents=()))


def test_peer_adoption_requires_local_gain_and_rolls_back_bad_fit():
    store = ArtifactStore(verified)
    store.admit(Artifact("skill", "teacher", {"score": 8}))
    agent = AgentState("student", memory={"adopted_artifact": "old"})

    def evaluate(agent, artifact, task):
        return Feedback(5 if artifact is None else task.metadata["local_score"], verified=True)

    adoption = PeerAdoption(store, evaluate, minimum_gain=1)
    assert not adoption.adopt(agent, "skill", Task("t", "", metadata={"local_score": 5.5}))
    assert adoption.adopt(agent, "skill", Task("t", "", metadata={"local_score": 7}))
    assert agent.memory["adopted_artifact"] == "skill"
    assert not adoption.audit(agent, Task("ood", "", metadata={"local_score": 2}))
    assert agent.memory["adopted_artifact"] == "old"
    assert adoption.adopt(agent, "skill", Task("t", "", metadata={"local_score": 7}))
    assert adoption.audit(agent, Task("ood", "", metadata={"local_score": 6}))
    assert agent.memory["adopted_artifact"] == "skill"


def test_adoption_audit_exception_restores_missing_reference():
    store = ArtifactStore(verified)
    store.admit(Artifact("skill", "teacher", {"score": 1}))
    adoption = PeerAdoption(store, lambda a, art, t: Feedback(1, verified=True))
    agent = AgentState("student")
    assert adoption.adopt(agent, "skill", Task("t", ""))
    store.retire("skill", "invalidated")
    with pytest.raises(ValueError):
        adoption.audit(agent, Task("t", ""))
    assert "adopted_artifact" not in agent.memory


def test_collective_refresh_survives_unmaintained_memory_and_cannot_resurrect():
    memory = DecayingMemory(half_life=2, threshold=0.2)
    memory.write(Artifact("kept", "a", "knowledge"), 0)
    memory.write(Artifact("lost", "a", "knowledge"), 0)
    memory.refresh("kept", "b", 3)
    assert {a.id for a in memory.available(5)} == {"kept"}
    assert memory.refreshers["kept"] == {"a", "b"}
    with pytest.raises(KeyError):
        memory.refresh("lost", "c", 5)
    with pytest.raises(ValueError):
        memory.available(4)


def test_cultural_transfer_checks_each_receiver_without_sender_score_copying():
    store = ArtifactStore(verified)
    store.admit(Artifact("root", "old", {"score": 99}))
    store.admit(Artifact("child", "old2", {"score": 100}, parents=("root",)))
    state = SwarmState({"a": AgentState("a"), "b": AgentState("b")})

    def evaluate(agent, artifact, task):
        return Feedback(2 if agent.id == "a" and artifact.id == "child" else -1, verified=True)

    result = CulturalTransfer(store, evaluate).step(state, Task("new", ""))
    assert result.metrics["adoptions"] == 1
    assert state.agents["a"].memory["cultural_lineage"] == ("root", "child")
    assert state.agents["b"].memory == {}
    assert state.step == 0


def test_procedure_abstraction_runs_callable_on_heldout_and_preserves_parents():
    store = ArtifactStore(lambda a: Feedback(1, verified=True))
    store.admit(Artifact("example", "a", lambda x: x * 2))
    abstraction = ProcedureAbstraction(
        store,
        lambda artifacts: Artifact("general", "synth", lambda x: x + x),
        lambda artifact, task: Feedback(
            1, verified=artifact.content(task.metadata["input"]) == task.metadata["expected"]
        ),
    )
    tests = [Task("held", "", metadata={"input": 12, "expected": 24})]
    result = abstraction.discover(["example"], tests, ["train"])
    assert result.parents == ("example",)
    assert result.metadata["held_out_scores"] == {"held": 1}
    with pytest.raises(ValueError, match="disjoint"):
        abstraction.discover(["example"], tests, ["held"])
    with pytest.raises(ValueError, match="held-out validation"):
        abstraction.discover(["example"], [Task("bad", "", metadata={"input": 2, "expected": 5})])
