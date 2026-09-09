import asyncio
import copy
import json

import pytest

from swarmkit.runtime import CallableAgent, CompletionAgent, MessageBus, SwarmRuntime, apply_result
from swarmkit.topology import RandomTopology, RingTopology
from swarmkit.types import (
    AgentOutput,
    AgentState,
    AlgorithmResult,
    Artifact,
    Budget,
    Decision,
    Evidence,
    Message,
    SwarmState,
    Task,
    Usage,
)


def make_state(n=3):
    return SwarmState({str(i): AgentState(str(i)) for i in range(n)}, seed=14)


def run(coro):
    return asyncio.run(coro)


def test_concurrency_snapshot_isolation_and_inbox_delivery_next_round():
    async def scenario():
        state = make_state(4)
        secret = Evidence("secret", "private fact", "private source", "0")
        state.agents["0"].private_evidence = (secret,)
        live = peak = 0
        contexts = []

        async def act(ctx):
            nonlocal live, peak
            live += 1
            peak = max(peak, live)
            contexts.append(ctx)
            ctx.agent.memory["not_committed"] = True
            assert not ctx.messages
            assert (secret in ctx.agent.private_evidence) == (ctx.agent.id == "0")
            await asyncio.sleep(0.005)
            live -= 1
            return AgentOutput(
                messages=(Message(ctx.agent.id, "public"),), memory_updates={"committed": True}
            )

        runtime = SwarmRuntime(state, {a: CallableAgent(act) for a in state.agents}, concurrency=2)
        result = await runtime.round(Task("t", "public task"))
        assert peak == 2
        assert result.metrics["calls"] == 4
        assert all(len(a.inbox) == 3 for a in state.agents.values())
        assert all(a.memory == {"committed": True} for a in state.agents.values())
        assert all(not m.evidence for m in state.messages)  # no automatic private-fact broadcast
        assert all("secret" not in repr(ctx) for ctx in contexts if ctx.agent.id != "0")

    run(scenario())


def test_direct_messages_respect_topology_and_are_copied():
    state = make_state(4)
    bus = MessageBus(RingTopology(bidirectional=False))
    metadata = {"nested": [1]}
    message = Message("0", "hello", recipients=("1", "2", "1"), metadata=metadata, id="m")
    assert bus.publish(state, message) == ("1",)
    metadata["nested"].append(2)
    assert state.agents["1"].inbox[0].metadata["nested"] == [1]
    assert not state.agents["2"].inbox
    original = copy.deepcopy(state.messages[0])
    assert bus.publish(state, original) == ()
    with pytest.raises(ValueError):
        bus.publish(state, message)
    assert len(state.messages) == 1


def test_publish_and_batch_routing_failures_rollback_topology_rng_and_artifacts():
    state = make_state()
    before = state.rng.getstate()

    def bad_filter(message, recipient):
        if recipient == "2":
            raise ValueError("bad filter")
        return True

    bus = MessageBus(RandomTopology(1), recipient_filter=bad_filter)
    with pytest.raises(ValueError):
        bus.publish(state, Message("0", "public"))
    assert state.rng.getstate() == before
    assert not state.data and not state.messages
    assert all(not a.inbox for a in state.agents.values())
    result = AlgorithmResult(
        messages=(Message("0", "ok"), Message("0", "bad", recipients=("unknown",))),
        artifacts=(Artifact("a", "0", "value"),),
    )
    with pytest.raises(ValueError):
        apply_result(state, result)
    assert not state.artifacts and not state.messages


def test_malformed_agent_batch_does_not_commit_any_part_and_peer_survives():
    state = make_state(2)
    incoming = Message("1", "existing", recipients=("0",), id="old")
    MessageBus().publish(state, incoming)
    state.messages.append(Message("1", "original", id="collision"))

    async def bad(ctx):
        return AgentOutput(
            messages=(Message("0", "first"), Message("0", "conflict", id="collision")),
            artifacts=(Artifact("x", "0", "should rollback"),),
            memory_updates={"bad": True},
        )

    async def good(ctx):
        return AgentOutput(messages=(Message("1", "survives"),))

    result = run(
        SwarmRuntime(state, {"0": CallableAgent(bad), "1": CallableAgent(good)}).round(Task("t", "test"))
    )
    assert "0" in result.metadata["errors"]
    assert not state.artifacts and not state.agents["0"].memory
    assert [m.content for m in state.messages] == ["existing", "original", "survives"]
    assert incoming.id in [m.id for m in state.agents["0"].inbox]


@pytest.mark.parametrize(
    "output",
    [
        AgentOutput(messages=(Message("1", "spoof"),)),
        AgentOutput(artifacts=(Artifact("x", "1", "spoof"),)),
        AgentOutput(decision=Decision("1", "spoof")),
        AgentOutput(memory_updates=None),
        AgentOutput(artifacts=(Artifact("x", "0", "a"), Artifact("x", "0", "b"))),
        None,
    ],
)
def test_spoofing_and_malformed_outputs_are_isolated(output):
    class Agent:
        async def act(self, ctx):
            return output

    state = make_state(2)
    result = run(SwarmRuntime(state, {"0": Agent()}).round(Task("t", "test")))
    assert "0" in result.metadata["errors"]
    assert not state.messages and not state.artifacts and not state.agents["0"].memory


def test_fail_fast_rolls_back_whole_round_but_accounts_dispatch():
    state = make_state(2)

    async def good(ctx):
        return AgentOutput(messages=(Message("0", "valid"),), usage=Usage(tokens=3))

    async def bad(ctx):
        raise ValueError("broken")

    runtime = SwarmRuntime(state, {"0": CallableAgent(good), "1": CallableAgent(bad)}, fail_fast=True)
    with pytest.raises(ValueError):
        run(runtime.round(Task("t", "test")))
    assert not state.messages and state.step == 0
    assert runtime.budget.used_calls == 2 and runtime.budget.used_tokens == 3


def test_budget_stops_queued_work_after_usage_is_known():
    state = make_state(4)
    called = []

    async def act(ctx):
        called.append(ctx.agent.id)
        return AgentOutput(usage=Usage(tokens=6))

    runtime = SwarmRuntime(
        state, {a: CallableAgent(act) for a in state.agents}, concurrency=1, budget=Budget(max_tokens=5)
    )
    result = run(runtime.round(Task("t", "test")))
    assert called == ["0"] and result.metrics["calls"] == 1
    assert runtime.budget.used_calls == 1 and runtime.budget.used_tokens == 6
    assert run(runtime.round(Task("t", "test"))).metadata["stopped"] == "budget"


def test_max_call_budget_and_timeout_failure_are_accounted():
    state = make_state(3)

    async def slow(ctx):
        await asyncio.sleep(1)
        return AgentOutput()

    runtime = SwarmRuntime(
        state, {a: CallableAgent(slow) for a in state.agents}, budget=Budget(max_calls=2), timeout=0.005
    )
    result = run(runtime.round(Task("t", "test")))
    assert result.metrics == {"calls": 2.0, "errors": 2.0}
    assert runtime.budget.used_calls == 2
    assert all("TimeoutError" in error for error in result.metadata["errors"].values())


def test_external_cancellation_cancels_children_no_commit_and_counts_only_started():
    async def scenario():
        state = make_state(3)
        started, cancelled = asyncio.Event(), asyncio.Event()

        async def act(ctx):
            started.set()
            try:
                await asyncio.sleep(100)
            finally:
                cancelled.set()
            return AgentOutput(messages=(Message(ctx.agent.id, "never"),))

        runtime = SwarmRuntime(state, {a: CallableAgent(act) for a in state.agents}, concurrency=1)
        job = asyncio.create_task(runtime.round(Task("t", "test")))
        await started.wait()
        job.cancel()
        with pytest.raises(asyncio.CancelledError):
            await job
        assert cancelled.is_set()
        assert runtime.budget.used_calls == 1
        assert not state.messages and state.step == 0 and runtime.budget.used_steps == 0

    run(scenario())


def test_child_self_cancellation_is_isolated():
    async def bad(ctx):
        raise asyncio.CancelledError()

    async def good(ctx):
        return AgentOutput(messages=(Message("1", "ok"),))

    state = make_state(2)
    result = run(
        SwarmRuntime(state, {"0": CallableAgent(bad), "1": CallableAgent(good)}).round(Task("t", "test"))
    )
    assert "0" in result.metadata["errors"] and state.messages[0].content == "ok"


def test_completion_agent_retains_received_evidence_without_cross_task_leakage():
    state = make_state(2)
    evidence = Evidence("known", "important observation", "measurement", "1")
    MessageBus().publish(state, Message("1", "observation", recipients=("0",), evidence=(evidence,)))
    prompts = []

    async def completion(prompt):
        data = json.loads(prompt)
        prompts.append(data)
        if data["phase"] == "decide":
            return json.dumps({"answer": "A", "evidence_ids": [e["id"] for e in data["evidence"]]})
        return "acknowledged"

    runtime = SwarmRuntime(state, {"0": CompletionAgent(completion)})
    run(runtime.round(Task("t", "test", ("A", "B")), phase="explore"))
    assert not state.agents["0"].inbox
    result = run(runtime.round(Task("t", "test", ("A", "B")), phase="decide"))
    assert result.decisions[0].evidence_ids == ("known",)
    run(runtime.round(Task("new", "other", ("A", "B")), phase="decide"))
    assert prompts[-1]["evidence"] == []
    assert state.agents["0"].memory["completion_received_evidence"]["t"] == (evidence,)


def test_output_return_values_do_not_alias_state():
    state = make_state(2)

    async def act(ctx):
        return AgentOutput(messages=(Message("0", "x", metadata={"x": []}),))

    result = run(SwarmRuntime(state, {"0": CallableAgent(act)}).round(Task("t", "test")))
    result.messages[0].metadata["x"].append("mutation")
    assert state.messages[0].metadata["x"] == []
    assert state.agents["1"].inbox[0].metadata["x"] == []


def test_idempotence_supports_numpy_channel_payloads():
    import numpy as np

    from swarmkit.types import LatentPayload

    state = make_state(2)
    message = Message(
        "0", "latent", id="latent", metadata={"payload": LatentPayload(np.ones((2, 3)), "model")}
    )
    bus = MessageBus()
    assert bus.publish(state, message) == ("1",)
    assert bus.publish(state, copy.deepcopy(message)) == ()
    artifact = Artifact("numeric", "0", np.arange(4))
    apply_result(state, AlgorithmResult(artifacts=(artifact,)))
    apply_result(state, AlgorithmResult(artifacts=(copy.deepcopy(artifact),)))
    assert len(state.artifacts) == 1


def test_recipient_string_is_rejected_without_partial_delivery():
    state = make_state(3)
    with pytest.raises(ValueError):
        MessageBus().publish(state, Message("0", "x", recipients="12"))
    assert not state.messages
