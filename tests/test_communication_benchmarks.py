import copy
import json
from dataclasses import replace

import pytest

from swarmkit.benchmarks import (
    ChannelConfig,
    CommunicationEvaluator,
    EvidenceAgent,
    distributed_evidence,
    interdependent_schedule,
    paired_summary,
)
from swarmkit.topology import RingTopology
from swarmkit.types import AgentOutput, Artifact, Decision, Message


def agents(case, policy="broadcast"):
    return {a: EvidenceAgent(policy) for a in case.private}


@pytest.mark.parametrize("policy", ["broadcast", "request", "targeted", "gated"])
async def test_distributed_information_complete_with_three_rounds(policy):
    case = distributed_evidence(seed=5)
    result = await CommunicationEvaluator(3).run(case, agents(case, policy))
    assert result.metrics["outcome"]["success"] == 1
    assert result.metrics["evidence_delivery"] == 1
    assert result.metrics["tokens"] is None and result.metrics["cost"] is None
    assert result.metrics["calls"] == 12
    json.dumps(result.report())


async def test_disabled_and_loss_do_not_leak_facts_and_keep_calls():
    case = distributed_evidence(5)
    for channel in (ChannelConfig(disabled=True), ChannelConfig(loss=1), ChannelConfig(max_bytes=0)):
        result = await CommunicationEvaluator(3, channel).run(case, agents(case))
        assert result.metrics["evidence_delivery"] == 0.25
        assert result.metrics["delivered_copies"] == 0
        assert result.metrics["calls"] == 12
        assert result.metrics["generated_bytes"] > 0


async def test_delivery_budget_duplicates_latency_and_reordering():
    case = distributed_evidence()
    result = await CommunicationEvaluator(3, ChannelConfig(max_messages=1, duplicate=1, reorder=True)).run(
        case, agents(case)
    )
    assert result.metrics["admitted_messages"] == 1
    assert result.metrics["delivered_copies"] == 6
    assert all(d.due_round == d.sent_round + 1 for d in result.deliveries)
    late = await CommunicationEvaluator(3, ChannelConfig(delay=3)).run(case, agents(case))
    assert late.metrics["delivered_copies"] == 0
    assert any(d.status == "late" for d in late.deliveries)


async def test_topology_genuine_multihop_and_no_shared_board():
    case = distributed_evidence(1, agents=6)
    run = await CommunicationEvaluator(2, topology=RingTopology()).run(case, agents(case))
    assert run.metrics["evidence_delivery"] < 1
    full = await CommunicationEvaluator(2).run(case, agents(case))
    assert full.metrics["evidence_delivery"] == 1


async def test_private_contexts_outputs_and_original_objects_isolated():
    case = distributed_evidence()
    before = copy.deepcopy(case.private)

    class InspectAgent:
        def act(self, context):
            assert len(context.agent.private_evidence) == 1
            assert not context.artifacts
            assert "winner" not in context.task.metadata
            context.agent.memory["mutated"] = True
            context.task.metadata["mutated"] = True
            return AgentOutput(decision=Decision(context.agent.id, "0"))

    result = await CommunicationEvaluator(2).run(case, {a: InspectAgent() for a in case.private})
    assert case.private == before and "mutated" not in case.task.metadata
    assert not result.checkpoints[1].state.agents["a0"].memory


async def test_replay_removes_delivery_and_reexecutes_receiver():
    case = distributed_evidence(5)
    evaluator = CommunicationEvaluator(2)
    population = agents(case)
    run = await evaluator.run(case, population)
    effect = await evaluator.replay_without(case, population, run, "0:a1:0")
    changed = effect["intervened"]
    assert changed.metrics["evidence_delivery"] == 0.75
    assert changed.decisions["a0"].evidence_ids != run.decisions["a0"].evidence_ids
    assert any(d.status == "suppressed" for d in changed.deliveries)
    same = await evaluator.run(case, population, checkpoint=run.checkpoints[1])
    assert same.decisions == run.decisions
    assert same.deliveries == run.deliveries
    assert same.metrics["calls"] == run.metrics["calls"]


async def test_replacement_removes_evidence_and_pending_delay_replay():
    case = distributed_evidence(5)
    evaluator = CommunicationEvaluator(3, ChannelConfig(delay=1))
    population = agents(case)
    run = await evaluator.run(case, population)
    altered = await evaluator.run(
        case, population, checkpoint=run.checkpoints[1], replace_messages={"0:a1:0": "neutral"}
    )
    assert altered.metrics["evidence_delivery"] == 0.75


async def test_pooled_and_redundant_controls():
    case = distributed_evidence(5)
    evaluator = CommunicationEvaluator(2, ChannelConfig(disabled=True))
    pooled = await evaluator.run(case, agents(case), pooled=True)
    assert pooled.metrics["outcome"]["success"] == 1
    redundant = distributed_evidence(5, redundant=True)
    result = await evaluator.run(redundant, agents(redundant, "none"))
    assert result.metrics["outcome"]["success"] == 1
    assert result.metrics["evidence_delivery"] == 1


async def test_interdependent_schedule_joint_verification():
    for seed in range(5):
        case = interdependent_schedule(seed)
        result = await CommunicationEvaluator(3, aggregation="joint").run(case, agents(case))
        assert result.metrics["outcome"] == {"success": 1, "conflicts": 0}
        assert result.metrics["evidence_delivery"] == 1


async def test_paired_statistics_clusters_repeats_by_case():
    left, right = [], []
    for seed in range(3):
        case = distributed_evidence(seed)
        for repeat in range(2):
            left.append(await CommunicationEvaluator(3).run(case, agents(case), repeat))
            right.append(await CommunicationEvaluator(3).run(case, agents(case, "none"), repeat))
    summary = paired_summary(left, list(reversed(right)))
    assert summary["paired_runs"] == 6 and summary["independent_cases"] == 3
    with pytest.raises(ValueError):
        paired_summary(left, right[:-1])


async def test_forbidden_artifacts_and_sender_spoofing_rejected():
    case = distributed_evidence()

    class BadAgent:
        def act(self, context):
            return AgentOutput(artifacts=(Artifact("a", context.agent.id, "side channel"),))

    with pytest.raises(ValueError):
        await CommunicationEvaluator().run(case, {a: BadAgent() for a in case.private})

    class SpoofAgent:
        def act(self, context):
            return AgentOutput(messages=(Message("stranger", "spoof"),))

    with pytest.raises(ValueError):
        await CommunicationEvaluator().run(case, {a: SpoofAgent() for a in case.private})


async def test_gate_and_compression_are_applied_before_delivery():
    case = distributed_evidence()
    result = await CommunicationEvaluator(3, gate=lambda m: False).run(case, agents(case))
    assert result.metrics["delivered_copies"] == 0
    result = await CommunicationEvaluator(3, transform=lambda m: replace(m, evidence=())).run(
        case, agents(case)
    )
    assert result.metrics["evidence_delivery"] == 0.25


def test_generation_splits_are_distinct_and_seed_not_in_agent_task():
    dev = distributed_evidence(1, split="dev")
    test = distributed_evidence(1, split="test")
    assert dev.private != test.private
    assert dev.task.id == test.task.id == "communication-diagnostic"


async def test_replay_rejects_wrong_case_and_unknown_message():
    case = distributed_evidence(1)
    evaluator = CommunicationEvaluator(2)
    result = await evaluator.run(case, agents(case))
    with pytest.raises(ValueError):
        await evaluator.run(distributed_evidence(2), agents(case), checkpoint=result.checkpoints[0])
    with pytest.raises(ValueError):
        await evaluator.replay_without(case, agents(case), result, "0:missing:0")
