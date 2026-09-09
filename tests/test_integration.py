"""Cross-domain behavior on the canonical data contracts, without provider calls."""

from __future__ import annotations

import asyncio
import runpy
from pathlib import Path

from swarmkit.deliberation import evidence_decision
from swarmkit.knowledge import EvidenceRegistry
from swarmkit.runtime import CallableAgent, MessageBus, Pipeline, SwarmRuntime, apply_result
from swarmkit.social import GossipRelay
from swarmkit.topology import RingTopology
from swarmkit.types import AgentOutput, AgentState, Budget, Evidence, Message, SwarmState, Task

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


def test_exchange_artifact_and_local_adoption_example():
    result = runpy.run_path(str(EXAMPLES / "collective_discovery.py"))["run_demo"]()
    assert result["shared_only_winner"] == result["private_independent_winner"] == "A"
    assert result["after_exchange_winner"] == "B"
    assert result["consensus"] and result["verified_artifact"]
    assert result["locally_adopted_and_retained"]
    assert result["independent_sources"] == 3
    assert result["pipeline_steps"] == 3 and result["routed_messages"] == 20


def test_feed_relay_and_collective_memory_example_is_reproducible():
    demo = runpy.run_path(str(EXAMPLES / "social_culture.py"))["run_demo"]
    first, second = demo(), demo()
    assert first == second
    assert first["feed_selected"] == "blue"
    assert first["choices_after_visibility"] == ["blue"]
    assert set(first["relay_coverage"].values()) == {1}
    assert first["independent_evidence_sources"] == 1
    assert first["maintained_records_at_step5"] == ["maintained"]


def test_graph_learning_uses_routed_task_performance_not_edge_labels():
    train = runpy.run_path(str(EXAMPLES / "learn_topology.py"))["train_demo"]
    output = train()
    probabilities = output["learned_probabilities"]
    assert probabilities["scout->solver"] > 0.9
    assert probabilities["scout->bystander"] < 0.2
    assert probabilities["bystander->solver"] < 0.2
    assert output["last_100_success_rate"] > 0.85
    assert train() == output


def test_relay_pipeline_obeys_one_hop_and_preserves_independent_source_count():
    fact = Evidence("root", "Measured fact", "measurement", "a", supports=("B",))
    state = SwarmState(
        {
            name: AgentState(name, private_evidence=(fact,) if name == "a" else ())
            for name in ("a", "b", "c", "d")
        }
    )
    task = Task("t", "", ("A", "B"))
    ring = RingTopology(bidirectional=False)
    relay = GossipRelay(ring.neighbors, cards_per_round=None)
    pipeline = Pipeline((relay,), bus=MessageBus(ring))
    first = pipeline.step(state, task)
    assert state.agents["b"].inbox
    assert not state.agents["c"].inbox  # No same-round relay cascade.
    # apply_result tolerates replaying an already committed result.
    count = len(state.messages)
    apply_result(state, first, MessageBus(ring))
    assert len(state.messages) == count
    pipeline.step(state, task)
    assert state.agents["c"].inbox and not state.agents["d"].inbox
    pipeline.step(state, task)
    assert state.agents["d"].inbox
    evidence = EvidenceRegistry(e for a in state.agents.values() for m in a.inbox for e in m.evidence)
    assert len(evidence.independent_sources()) == 1
    assert evidence.scores(("B",)) == {"B": 1}


def test_async_runtime_snapshot_delivery_feeds_deliberation_next_round():
    private = Evidence("e", "B measured feasible", "experiment", "scout", supports=("B",))
    prior = Evidence("p", "A prior", "prior", "solver", confidence=0.5, supports=("A",))
    state = SwarmState(
        {
            "scout": AgentState("scout", private_evidence=(private,)),
            "solver": AgentState("solver", private_evidence=(prior,)),
        }
    )
    task = Task("t", "", ("A", "B"))

    def act(context):
        if context.agent.id == "scout":
            return AgentOutput(
                messages=(
                    Message(
                        "scout",
                        private.claim,
                        ("solver",),
                        evidence=(private,),
                        step=context.step,
                        id=f"fact-{context.step}",
                    ),
                )
            )
        available = context.agent.private_evidence + tuple(e for m in context.messages for e in m.evidence)
        return AgentOutput(decision=evidence_decision(context.agent, context.task, available))

    runtime = SwarmRuntime(
        state,
        {agent_id: CallableAgent(act) for agent_id in state.agents},
        budget=Budget(max_calls=4),
        fail_fast=True,
    )

    async def run():
        before = await runtime.round(task)
        after = await runtime.round(task)
        stopped = await runtime.round(task)
        return before, after, stopped

    before, after, stopped = asyncio.run(run())
    assert before.decisions[0].answer == "A"
    assert after.decisions[0].answer == "B"
    assert set(after.decisions[0].evidence_ids) == {"p", "e"}
    assert stopped.metadata["stopped"] == "budget"
    assert state.step == 2 and runtime.budget.used_calls == 4


def test_exchange_inbox_mode_cannot_bypass_sparse_topology():
    from swarmkit.deliberation import ExchangeConfig, ExchangeThenDecide

    root = Evidence("decisive", "B passes the measurement.", "experiment", "a", supports=("B",))
    prior = Evidence("weak-prior", "Weak preference for A.", "prior", "all", confidence=0.4, supports=("A",))
    task = Task("topology-exchange", "", ("A", "B"))

    def run(delivery):
        state = SwarmState(
            {
                name: AgentState(name, private_evidence=(root,) if name == "a" else (prior,))
                for name in ("a", "b", "c", "d")
            }
        )
        method = ExchangeThenDecide(ExchangeConfig(exchange_rounds=2, delivery=delivery))
        ring = RingTopology(bidirectional=False)
        pipeline = Pipeline((method,), bus=MessageBus(ring))
        pipeline.step(state, task)
        assert not any(root.id == e.id for m in state.agents["d"].inbox for e in m.evidence)
        pipeline.step(state, task)
        # Consumption by another component does not erase retained local evidence.
        for agent in state.agents.values():
            if agent.id == "b":
                agent.inbox.clear()
        result = pipeline.step(state, task)
        return {d.agent_id: d for d in result.decisions}

    sparse = run("inbox")
    assert {agent: decision.answer for agent, decision in sparse.items()} == {
        "a": "B",
        "b": "B",
        "c": "B",
        "d": "A",
    }
    assert "decisive" not in sparse["d"].evidence_ids
    assert "decisive" in sparse["b"].evidence_ids
    assert {d.answer for d in run("all_peer").values()} == {"B"}


def test_exchange_inbox_mode_does_not_fetch_undelivered_ancestors():
    from swarmkit.deliberation import ExchangeConfig, ExchangeThenDecide

    root = Evidence("secret-root", "Private B observation", "private-experiment", "a", supports=("B",))
    derived = Evidence(
        "derived",
        "A retelling without its ancestor",
        "retelling",
        "b",
        supports=("B",),
        parents=("secret-root",),
    )
    prior = Evidence("prior", "A remains the only supported option here", "local", "c", supports=("A",))
    state = SwarmState(
        {
            "a": AgentState("a", private_evidence=(root,)),
            "b": AgentState("b"),
            "c": AgentState(
                "c",
                private_evidence=(prior,),
                inbox=[Message("b", derived.claim, ("c",), evidence=(derived,))],
            ),
        }
    )
    task = Task("ancestry", "", ("A", "B"))
    method = ExchangeThenDecide(ExchangeConfig(exchange_rounds=1, delivery="inbox"))
    method.step(state, task)  # Deliberately do not deliver outputs.
    result = method.step(state, task)
    receiver = next(d for d in result.decisions if d.agent_id == "c")
    assert receiver.answer == "A"
    assert receiver.evidence_ids == ("prior",)
    assert result.metrics["pending_evidence"] == 1


def test_exchange_inbox_mode_honors_transport_filter():
    from swarmkit.deliberation import ExchangeConfig, ExchangeThenDecide

    root = Evidence("blocked", "B", "s", "a", supports=("B",))
    prior = Evidence("prior", "A", "p", "b", confidence=0.2, supports=("A",))
    state = SwarmState(
        {"a": AgentState("a", private_evidence=(root,)), "b": AgentState("b", private_evidence=(prior,))}
    )
    task = Task("filter", "", ("A", "B"))
    method = ExchangeThenDecide(ExchangeConfig(exchange_rounds=1, delivery="inbox"))
    output = Pipeline((method, method), bus=MessageBus(gate=lambda message: not message.evidence)).step(
        state, task
    )
    assert {d.agent_id: d.answer for d in output.decisions} == {"a": "B", "b": "A"}


def test_exchange_mid_episode_snapshot_restores_both_delivery_modes():
    from swarmkit.deliberation import ExchangeConfig, ExchangeThenDecide
    from swarmkit.serialization import dumps, loads

    root = Evidence("root", "Independent B observation", "measurement", "a", supports=("B",))
    prior = Evidence("prior", "A prior", "prior-source", "all", confidence=0.3, supports=("A",))
    task = Task("checkpoint", "", ("A", "B"))
    for delivery in ("all_peer", "inbox"):
        config = ExchangeConfig(delivery=delivery)
        state = SwarmState(
            {
                name: AgentState(name, private_evidence=(root,) if name == "a" else (prior,))
                for name in ("a", "b", "c", "d")
            },
            seed=13,
        )
        ring = RingTopology(bidirectional=False)
        original = Pipeline((ExchangeThenDecide(config),), bus=MessageBus(ring))
        original.step(state, task)
        restored = loads(dumps(state))
        resumed = Pipeline((ExchangeThenDecide(config),), bus=MessageBus(ring))
        original.step(state, task)
        resumed.step(restored, task)
        expected = original.step(state, task)
        actual = resumed.step(restored, task)
        assert actual.decisions == expected.decisions
        assert actual.metrics == expected.metrics
        assert restored.step == state.step == 3
        # Even completed state remains in the canonical serialization whitelist.
        assert loads(dumps(restored)).data["decisions"] == list(actual.decisions)
