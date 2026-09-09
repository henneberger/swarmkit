import pytest

from swarmkit.deliberation import (
    CritiqueReviseDebate,
    ExchangeConfig,
    ExchangeThenDecide,
    IndependentVoting,
    WeightedConsensus,
)
from swarmkit.types import AgentState, Decision, Evidence, Message, MessageKind, SwarmState, Task


def hidden_state():
    common = Evidence("common", "Shared appearance favors A", "common-source", "all", supports=("A",))
    hidden1 = Evidence("h1", "A bridge is closed", "inspection1", "minority", supports=("B",))
    hidden2 = Evidence("h2", "B route is clear", "inspection2", "minority", supports=("B",))
    agents = {f"a{i}": AgentState(f"a{i}", private_evidence=(common,)) for i in range(3)}
    agents["minority"] = AgentState("minority", private_evidence=(common, hidden1, hidden2))
    return SwarmState(agents), Task("route", "", ("A", "B"))


def test_minority_private_facts_reverse_majority_after_required_exchange():
    state, task = hidden_state()
    independent = IndependentVoting().step(state, task)
    assert [d.answer for d in independent.decisions].count("A") == 3
    protocol = ExchangeThenDecide()
    for _ in range(2):
        output = protocol.step(state, task)
        assert output.decisions == ()
        assert sum(m.kind == MessageKind.CRITIQUE for m in output.messages) == 4
    output = protocol.step(state, task)
    assert {d.answer for d in output.decisions} == {"B"}
    assert output.metrics["shared_sources"] == 3
    assert output.metadata["done"]
    assert state.messages == [] and state.step == 0
    assert protocol.step(state, task).metadata["phase"] == "complete"


def test_independent_votes_isolate_inbox_memory_and_callback_side_effects():
    state, task = hidden_state()
    state.agents["a0"].memory["answer"] = "B"
    state.agents["a0"].inbox.append(Message("other", "B"))

    def decide(agent, task, evidence):
        assert not agent.memory and not agent.inbox and not agent.beliefs
        agent.memory["side_effect"] = True
        return Decision(agent.id, "A")

    IndependentVoting(decide).step(state, task)
    assert state.agents["a0"].memory == {"answer": "B"}


def test_exchange_includes_provenance_ancestors_without_extra_source_vote():
    root = Evidence("root", "fact", "s", "a", supports=("B",))
    copy = Evidence("copy", "retelling", "blog", "b", supports=("B",), parents=("root",))
    state = SwarmState(
        {"a": AgentState("a", private_evidence=(root,)), "b": AgentState("b", private_evidence=(copy,))}
    )
    task = Task("t", "", ("A", "B"))
    method = ExchangeThenDecide(ExchangeConfig(exchange_rounds=1))
    method.step(state, task)
    result = method.step(state, task)
    assert result.metrics["shared_sources"] == 1
    assert {d.answer for d in result.decisions} == {"B"}


def test_consensus_weighted_quorum_stability_ties_and_duplicate_voters():
    task = Task("t", "", ("A", "B"))
    consensus = WeightedConsensus({"a": 3, "b": 1}, threshold=0.7, stable_rounds=2)
    ballots = [Decision("a", "B"), Decision("b", "A")]
    assert not consensus.aggregate(ballots, task).metadata["converged"]
    assert consensus.aggregate(ballots, task).metadata["converged"]
    tie = WeightedConsensus(threshold=0.5)
    assert not tie.aggregate(ballots, task).metadata["converged"]
    with pytest.raises(ValueError, match="duplicate"):
        tie.aggregate([ballots[0], ballots[0]], task)
    assert (
        WeightedConsensus(confidence_weighted=True)
        .aggregate([Decision("a", "B", confidence=0)], task)
        .metadata["winner"]
        is None
    )
    assert not WeightedConsensus(minimum_voters=2).aggregate([ballots[0]], task).metadata["converged"]


def test_debate_critics_share_snapshot_then_revise_from_all_critiques():
    state, task = hidden_state()
    seen = []

    def critique(agent, previous, task):
        seen.append(tuple(d.answer for d in previous))
        return "Inspect both hidden observations before choosing."

    def revise(agent, own, critiques, task):
        assert len(critiques) == 4
        assert all(c.kind == MessageKind.CRITIQUE for c in critiques)
        return Decision(agent.id, "B")

    debate = CritiqueReviseDebate(critique, revise)
    first = debate.step(state, task)
    assert first.metadata["phase"] == "independent"
    result = debate.step(state, task)
    assert len(set(seen)) == 1
    assert result.metadata["converged"] and result.metadata["done"]
    assert {d.answer for d in result.decisions} == {"B"}


def test_debate_round_cap_does_not_assert_convergence():
    state, task = hidden_state()
    debate = CritiqueReviseDebate(
        lambda a, d, t: "Keep disagreement visible",
        lambda a, d, c, t: d,
        max_rounds=1,
        consensus=WeightedConsensus(threshold=1),
    )
    debate.step(state, task)
    result = debate.step(state, task)
    assert result.metadata["done"] and not result.metadata["converged"]


def test_protocol_rejects_roster_changes_and_invalid_callback_answers():
    state, task = hidden_state()
    method = ExchangeThenDecide()
    method.step(state, task)
    state.agents["a0"].active = False
    with pytest.raises(ValueError, match="roster"):
        method.step(state, task)
    method.reset(state, task.id)
    assert method.step(state, task).metadata["phase"] == "exchange"
    with pytest.raises(ValueError, match="candidate"):
        IndependentVoting(lambda a, t, e: Decision(a.id, "unknown")).step(state, task)
