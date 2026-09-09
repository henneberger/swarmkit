import pytest

from swarmkit.social import FeedPolicy, GossipRelay, NamingGame, ProportionalCopying, TrustNetwork
from swarmkit.types import AgentState, Evidence, Message, SwarmState, Task


def population(n=3, seed=12):
    return SwarmState({str(i): AgentState(str(i)) for i in range(n)}, seed=seed)


def test_naming_committed_local_history_and_determinism():
    task = Task("t", "", ("x", "y"))
    left, right = population(), population()
    game = NamingGame(memory_size=2, committed={"0": "x"})
    for _ in range(12):
        a, b = game.step(left, task), game.step(right, task)
        assert a == b
        assert len(a.decisions) == 2
        for d in a.decisions:
            if d.agent_id == "0":
                assert d.answer == "x"
        assert all(len(agent.memory.get("naming_game", [])) <= 2 for agent in left.agents.values())
    assert left.agents == right.agents


def test_naming_empty_population_zero_memory_and_bad_callback():
    task = Task("t", "", ("x",))
    assert not NamingGame().step(population(1), task).decisions
    state = population(2)
    NamingGame(memory_size=0).step(state, task)
    assert all(a.memory["naming_game"] == [] for a in state.agents.values())
    with pytest.raises(ValueError):
        NamingGame(choose=lambda *_: "invalid").step(state, task)
    with pytest.raises(ValueError):
        NamingGame(committed={"0": "z"}).step(state, task)


def test_copying_uses_visible_multiplicity_and_does_not_share_current_answers():
    state = population(1000)
    result = ProportionalCopying(innovation=0, visible=lambda *_: ["x"] * 9 + ["y"]).step(
        state, Task("t", "", ("x", "y"))
    )
    count = sum(d.answer == "x" for d in result.decisions)
    assert 850 < count < 950
    assert all(d.metadata["copied"] for d in result.decisions)
    empty = ProportionalCopying(innovation=0).step(population(2), Task("t", "", ("x",)))
    assert all(not d.metadata["copied"] for d in empty.decisions)


def test_feed_diversifies_and_handles_reputation_age_and_limits():
    messages = [
        Message("a", "a", id="1", metadata={"topic": "A"}),
        Message("b", "b", id="2", metadata={"topic": "A"}),
        Message("c", "c", id="3", metadata={"topic": "B"}),
    ]
    policy = FeedPolicy(position_weight=0, recency_weight=0, proof_weight=0, reputation_weight=0)
    assert [m.id for m in policy.rank(messages, 0)] == ["1", "3", "2"]
    assert policy.rank(messages, 0, limit=0) == ()
    newer = Message("x", "new", id="4", step=10)
    assert FeedPolicy(position_weight=0).rank([messages[0], newer], 10)[0] == newer
    assert (
        FeedPolicy(position_weight=0, recency_weight=0)
        .rank(messages, 0, reputation=lambda i: float(i == "c"))[0]
        .sender
        == "c"
    )
    with pytest.raises(ValueError):
        policy.rank([messages[0], messages[0]], 0)
    with pytest.raises(ValueError):
        FeedPolicy(half_life=0)


def test_trust_direction_topic_hops_cycles_and_admission():
    trust = TrustNetwork()
    trust.observe("a", "b", "math", True, 8)
    trust.observe("b", "c", "math", True, 8)
    trust.observe("c", "a", "math", True, 8)
    assert trust.trust("a", "c", "math", max_hops=1) == 0
    assert trust.trust("a", "c", "math", max_hops=2) == pytest.approx(0.9 * 0.9 * 0.9)
    assert trust.trust("b", "a", "math", max_hops=1) == 0
    assert trust.trust("a", "b", "physics") == 0
    assert trust.trust("a", "c", "math", max_hops=99) == pytest.approx(0.729)
    card = Evidence("e", "a fact", "source", "c")
    assert trust.admit("a", card, "math", lambda _: True, threshold=0.7)
    assert not trust.admit("a", card, "math", lambda _: False, threshold=0.7)
    trust.observe("a", "b", "math", False, 100)
    assert not trust.admit("a", card, "math", lambda _: True, threshold=0.7)


def test_relay_synchronous_disconnected_network_and_counted_coverage():
    state = population(4)
    state.agents["0"].private_evidence = (Evidence("e", "fact", "s", "0"),)
    links = {"0": ["1"], "1": ["2"], "2": [], "3": []}
    relay = GossipRelay(lambda _, agent: links[agent])
    result = relay.step(state, Task("t", ""))
    assert len(result.metadata["knowledge"]["1"]) == 1
    assert result.metadata["knowledge"]["2"] == ()
    assert result.metrics["new_deliveries"] == 1
    state.step += 1
    result = relay.step(state, Task("t", ""))
    assert len(result.metadata["knowledge"]["2"]) == 1
    assert result.metadata["knowledge"]["3"] == ()
    assert result.metrics["evidence_copies"] == 3
    state.step += 1
    assert relay.step(state, Task("t", "")).metrics["new_deliveries"] == 0


def test_relay_lifetime_not_renewed_by_copies_and_fanout():
    state = population(5)
    state.agents["0"].private_evidence = tuple(Evidence(str(i), "fact", str(i), "0") for i in range(3))
    relay = GossipRelay(lambda s, _: s.active_ids, fanout=1, cards_per_round=2, ttl=1)
    first = relay.step(state, Task("t", ""))
    assert len(first.messages) == 1
    assert len(first.messages[0].recipients) == 1
    assert len(first.messages[0].evidence) == 2
    recipient = first.messages[0].recipients[0]
    state.agents[recipient].inbox.append(first.messages[0])
    state.step += 1
    second = relay.step(state, Task("t", ""))
    assert not second.messages
    assert second.metrics["evidence_copies"] == 0


def test_relay_admission_and_zero_bandwidth():
    state = population(2)
    state.agents["0"].private_evidence = (Evidence("e", "fact", "s", "0"),)
    relay = GossipRelay(lambda s, _: s.active_ids, admit=lambda receiver, _: receiver == "0")
    result = relay.step(state, Task("t", ""))
    assert result.metrics["new_deliveries"] == 0
    assert not GossipRelay(lambda s, _: s.active_ids, cards_per_round=0).step(state, Task("t", "")).messages
    with pytest.raises(ValueError):
        GossipRelay(lambda *_: [], ttl=-1)


def test_relay_rejects_conflicting_ids_and_never_sends_to_inactive():
    state = population(3)
    state.agents["2"].active = False
    state.agents["0"].private_evidence = (Evidence("e", "first", "s", "0"),)
    relay = GossipRelay(lambda *_: ["1", "1", "2", "unknown"])
    result = relay.step(state, Task("t", ""))
    assert result.messages[0].recipients == ("1",)
    state.agents["1"].private_evidence = (Evidence("e", "different", "s", "0"),)
    with pytest.raises(ValueError, match="conflicting"):
        relay.step(state, Task("t", ""))


def test_integer_configuration_boundaries():
    with pytest.raises(ValueError):
        NamingGame(memory_size=1.5)
    with pytest.raises(ValueError):
        GossipRelay(lambda *_: [], fanout=1.2)
    with pytest.raises(ValueError):
        FeedPolicy().rank([], now=0, limit=1.5)
