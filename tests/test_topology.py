import math

import pytest

from swarmkit.topology import (
    BernoulliDAGPolicy,
    CapabilitySuccessRouter,
    DyLANSelection,
    FullTopology,
    HypergraphTopology,
    LocalRadiusTopology,
    RandomTopology,
    RingTopology,
    RoundDropoutTopology,
    StarTopology,
)
from swarmkit.types import AgentState, Decision, Feedback, SwarmState


def state(n=6, seed=12):
    return SwarmState({str(i): AgentState(str(i), position=(float(i), 0.0)) for i in range(n)}, seed=seed)


def test_static_topologies_filter_inactive_and_no_duplicates():
    s = state(3)
    assert FullTopology().neighbors(s, "0") == ("1", "2")
    assert RingTopology().neighbors(s, "0") == ("1", "2")
    assert StarTopology("0").neighbors(s, "1") == ("0",)
    s.agents["2"].active = False
    assert RingTopology().neighbors(s, "0") == ("1",)
    assert StarTopology("2").neighbors(s, "1") == ()
    assert HypergraphTopology((frozenset(("0", "1")), frozenset(("0", "1", "2")))).neighbors(s, "0") == ("1",)
    assert FullTopology().neighbors(s, "unknown") == ()


def test_spatial_boundaries_and_dimensions():
    s = state(3)
    assert LocalRadiusTopology(1).neighbors(s, "0") == ("1",)
    s.agents["1"].position = (0.0,)
    with pytest.raises(ValueError):
        LocalRadiusTopology(1).neighbors(s, "0")
    with pytest.raises(ValueError):
        LocalRadiusTopology(float("nan"))


def test_random_graph_is_reproducible_and_cached():
    a, b = state(), state()
    p = RandomTopology(0.4)
    graph = {x: p.neighbors(a, x) for x in a.active_ids}
    assert graph == {x: p.neighbors(b, x) for x in b.active_ids}
    assert graph == {x: p.neighbors(a, x) for x in a.active_ids}
    assert RandomTopology(0, "empty").neighbors(a, "0") == ()
    assert RandomTopology(1, "full").neighbors(a, "0") == FullTopology().neighbors(a, "0")


def test_reinforce_gradient_uses_absent_edges_and_single_update():
    s = state(4)
    p = BernoulliDAGPolicy(learning_rate=1, baseline_decay=1)
    before = p.probabilities(s)
    edges = p.sample(s)
    assert all(int(a) < int(b) for a, b in edges)
    p.update(s, Feedback(2))
    after = p.probabilities(s)
    for edge in before:
        assert (after[edge] > before[edge]) == (edge in edges)
    with pytest.raises(ValueError):
        p.update(s, Feedback(2))
    assert p.sample(s) == edges  # routing is stable after the learning update
    s.step += 1
    p.sample(s)
    p.update(s, Feedback(0))


def test_pruning_is_monotone_and_nuclear_regularizer_finite():
    s = state(7)
    p = BernoulliDAGPolicy(nuclear_penalty=0.2)
    p.sample(s)
    with pytest.raises(ValueError):
        p.prune(s, 0.5)
    assert math.isfinite(p.update(s, Feedback(1))["nuclear_norm"])
    assert len(p.prune(s, 0.5)) == 10
    assert len(p.prune(s, 1)) == 11
    assert p.sample(s) == ()
    p.update(s, Feedback(1))
    assert all(v == 0 for v in p.probabilities(s).values())


def test_dropout_arbitrary_size_and_round_local():
    s = state(9)
    p = RoundDropoutTopology(FullTopology())
    keep = p.configure(s, 0, {a: float(a) for a in s.agents}, 1 / 3)
    assert len(keep) == 6
    assert p.neighbors(s, "0") == ()
    assert len(p.neighbors(s, "8")) == 5
    assert len(s.active_ids) == 9  # does not permanently deactivate members
    s.step = 1
    assert len(p.neighbors(s, "0")) == 8
    p.configure(s, 1, {}, 1)
    assert p.neighbors(s, "0") == ()


def test_dylan_consensus_missing_and_duplicate_voters():
    p = DyLANSelection(keep=2)
    s = state(3)
    assert p.select(s, {"2": 9})[0] == "2"
    assert p.consensus([Decision("0", "A"), Decision("1", "A")], s.active_ids) is None
    assert p.consensus([Decision(a, "A") for a in s.active_ids], s.active_ids) == "A"
    with pytest.raises(ValueError):
        p.consensus([Decision("0", "A")] * 3, s.active_ids)
    assert p.backward_importance({"c": 1}, [{("a", "b"): 0.5}, {("b", "c"): 0.8}])["a"] == pytest.approx(0.4)


def test_router_capability_success_and_no_cycles():
    s = state(3)
    s.agents["1"].capabilities = frozenset(["math"])
    p = CapabilitySuccessRouter(exploration=0, success_weight=0.75, decay=0)
    assert p.route(s, "0", frozenset(["math"])) == "1"
    p.record(s, "0", "1", 0)
    p.record(s, "0", "2", 1)
    assert p.route(s, "0", frozenset(["math"])) == "2"
    assert p.route(s, "0", frozenset(), visited=("1", "2")) is None


def test_reinforce_learns_rewarded_communication_edge():
    s = state(2, seed=17)
    p = BernoulliDAGPolicy(learning_rate=0.3, baseline_decay=0.9)
    for step in range(200):
        s.step = step
        present = bool(p.sample(s))
        p.update(s, Feedback(float(present)))
    assert p.probabilities(s)[("0", "1")] > 0.95


def test_empty_population_and_invalid_learning_feedback():
    s = state(0)
    p = BernoulliDAGPolicy(nuclear_penalty=1)
    assert p.sample(s) == ()
    assert p.update(s, Feedback(0))["nuclear_norm"] == 0
    p = BernoulliDAGPolicy(key="overflow")
    p.sample(s)
    with pytest.raises(ValueError):
        p.update(s, Feedback(1e308, costs=-1e308))
