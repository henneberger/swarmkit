import math

import pytest

from swarmkit.evaluation import (
    ancestry_adjusted_agreement,
    hyperedge_irreducibility,
    interaction_reciprocity,
    matched_independent_control,
    population_diversity,
    private_evidence_recovery,
    transfer_gain,
)
from swarmkit.types import AgentState, Decision, Evidence, Message, SwarmState, Task


def test_entropy_and_reciprocity_count_unique_edges():
    assert population_diversity([]) == 0
    assert population_diversity(["a"] * 10) == 0
    assert population_diversity(["a", "b"]) == pytest.approx(1)
    assert population_diversity(["a", "b"], normalized=False) == pytest.approx(math.log(2))
    messages = [
        Message("a", "", ("b",)),
        Message("a", "", ("b",)),
        Message("b", "", ("a",)),
        Message("b", "", ("c",)),
        Message("a", "", ("a",)),
    ]
    assert interaction_reciprocity(messages) == pytest.approx(2 / 3)
    assert interaction_reciprocity([Message("a", "")]) == 0
    assert interaction_reciprocity([Message("a", ""), Message("b", "")], ("a", "b")) == 1


def test_recovery_counts_evidence_not_messages():
    one = Evidence("1", "", "s", "a")
    two = Evidence("2", "", "t", "b")
    repeated = [Message("a", "", evidence=(one,))] * 100
    assert private_evidence_recovery([one, two], repeated) == 0.5
    assert private_evidence_recovery([one, one], repeated) == 1
    assert private_evidence_recovery([], []) == 1


def test_ancestry_discount_and_distinct_source_collapse():
    root = Evidence("root", "", "shared", "a")
    derived = Evidence("copy", "", "derived", "b", parents=("root",))
    other = Evidence("other", "", "independent", "c")
    registry = {e.id: e for e in (root, derived, other)}
    decisions = [Decision(str(i), "wrong", evidence_ids=("copy",)) for i in range(10)]
    decisions.append(Decision("correct", "right", evidence_ids=("other",)))
    assert ancestry_adjusted_agreement(decisions, registry, "right") == pytest.approx(0.5)
    assert ancestry_adjusted_agreement([Decision("a", "x")], registry) == 0
    registry["cycle"] = Evidence("cycle", "", "x", "a", parents=("cycle",))
    with pytest.raises(ValueError, match="cyclic"):
        ancestry_adjusted_agreement([Decision("a", "x", evidence_ids=("cycle",))], registry)
    with pytest.raises(ValueError, match="unknown"):
        ancestry_adjusted_agreement([Decision("a", "x", evidence_ids=("missing",))], registry)


def test_exact_hyperedge_formula_and_undefined_dyads():
    assert hyperedge_irreducibility([]) is None
    assert hyperedge_irreducibility([["a", "b"]]) is None
    assert hyperedge_irreducibility([["a", "b", "c"]]) == 1
    # Degrees 3,1,1: pair differences 2+2+0, denominator 3*(5/3)*2=10.
    assert hyperedge_irreducibility([["a", "b", "c"], ["a"], ["a"]]) == pytest.approx(0.6)
    assert hyperedge_irreducibility([["a", "b", "c", "c"], ["a"], ["a"]]) == pytest.approx(0.6)


def test_transfer_paired_fresh_inputs_and_invalid_scores():
    cases = [{"value": 1}, {"value": 3}]

    def before(case):
        value = case["value"]
        case["value"] = 999
        return value

    assert transfer_gain(cases, before, lambda c: c["value"] + 2) == 2
    assert cases == [{"value": 1}, {"value": 3}]
    with pytest.raises(ValueError):
        transfer_gain([], before, before)
    with pytest.raises(ValueError):
        transfer_gain([0], lambda _: 1, lambda _: float("nan"))


def test_matched_control_keeps_budget_information_and_state_isolated():
    evidence = Evidence("e", "fact", "source", "a")
    state = SwarmState({"a": AgentState("a", private_evidence=(evidence,)), "b": AgentState("b")}, seed=12)
    budgets = []

    def swarm(s, task, budget):
        assert budget == 5
        s.agents["b"].memory["leak"] = True
        return [Decision(i, "yes") for i in s.active_ids]

    def independent(agent, task, budget, rng):
        budgets.append(budget)
        assert not agent.memory
        return Decision(agent.id, "yes" if agent.private_evidence else "no")

    result = matched_independent_control(
        state,
        Task("t", ""),
        5,
        swarm,
        independent,
        lambda decisions, _: sum(d.answer == "yes" for d in decisions) / len(decisions),
    )
    assert budgets == [3, 2]
    assert result.gain == 0.5
    assert result.independent_budgets == {"a": 3, "b": 2}
    assert not state.agents["b"].memory
    with pytest.raises(ValueError):
        matched_independent_control(state, Task("t", ""), 1, swarm, independent, lambda *_: 0)
