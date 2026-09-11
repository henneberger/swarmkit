"""Private-channel communication experiments with delivery interventions and replay.

This harness runs canonical Agent/AgentContext/AgentOutput callbacks. No shared
artifacts are exposed; callbacks may still have external side effects, which must
be isolated by the caller. Scripted fixtures are diagnostics, not SOTA benchmarks.
"""

from __future__ import annotations

import copy
import hashlib
import inspect
import json
import time
from collections import Counter
from dataclasses import asdict, dataclass, field, replace
from typing import Callable, Mapping

import numpy as np

from ..types import (
    AgentContext,
    AgentOutput,
    AgentState,
    Decision,
    Evidence,
    Message,
    SwarmState,
    Task,
)


def wire_bytes(message):
    """UTF-8 serialized canonical message, including evidence and metadata."""
    return len(json.dumps(asdict(message), sort_keys=True, ensure_ascii=False, default=str).encode("utf-8"))


@dataclass
class CommunicationCase:
    id: str
    task: Task
    private: Mapping[str, tuple[Evidence, ...]]
    required: Mapping[str, tuple[str, ...]]
    evaluate: Callable[[Mapping[str, Decision]], Mapping[str, float]]
    split: str = "test"


@dataclass(frozen=True)
class ChannelConfig:
    max_messages: int | None = None
    max_bytes: int | None = None
    delay: int = 0
    loss: float = 0.0
    duplicate: float = 0.0
    reorder: bool = False
    disabled: bool = False

    def __post_init__(self):
        if (
            any(
                x is not None and (not isinstance(x, int) or x < 0)
                for x in (self.max_messages, self.max_bytes)
            )
            or not isinstance(self.delay, int)
            or self.delay < 0
            or not all(0 <= x <= 1 for x in (self.loss, self.duplicate))
        ):
            raise ValueError("invalid channel configuration")


@dataclass(frozen=True)
class Delivery:
    message_id: str
    sender: str
    recipient: str
    sent_round: int
    due_round: int
    status: str
    bytes: int
    evidence_ids: tuple[str, ...]


@dataclass
class Checkpoint:
    case_id: str
    seed: int
    pooled: bool
    round: int
    state: SwarmState
    agents: dict
    pending: list
    decisions: dict
    deliveries: list
    metrics: dict
    first_arrival: dict


@dataclass
class EvaluationRun:
    case_id: str
    seed: int
    decisions: dict
    metrics: dict
    deliveries: list[Delivery]
    checkpoints: dict[int, Checkpoint] = field(repr=False)
    config: dict = field(default_factory=dict)

    def report(self):
        return {
            "case_id": self.case_id,
            "seed": self.seed,
            "decisions": {a: asdict(d) for a, d in self.decisions.items()},
            "metrics": self.metrics,
            "deliveries": [asdict(d) for d in self.deliveries],
            "config": self.config,
        }


class CommunicationEvaluator:
    """Synchronous rounds, private contexts, explicit topology and delayed receipts.

    Agents are deep-copied for every run and checkpoint. Models needing an external
    session should implement __deepcopy__ or use an isolated wrapper. Model RNG and
    external tools are not reset by Python copies; supply deterministic wrappers
    for causal replay. Budgets here constrain the channel, not opaque model calls.
    """

    def __init__(
        self,
        rounds=3,
        channel=None,
        topology=None,
        gate=None,
        transform=None,
        trust_reported_usage=False,
        aggregation="designated",
        decision_maker=None,
    ):
        if rounds < 1 or aggregation not in ("designated", "vote", "joint"):
            raise ValueError("invalid rounds or aggregation")
        self.rounds, self.channel, self.topology = rounds, channel or ChannelConfig(), topology
        self.gate, self.transform, self.trust_usage = gate, transform, trust_reported_usage
        self.aggregation, self.decision_maker = aggregation, decision_maker

    @staticmethod
    def _random(seed, *parts):
        digest = hashlib.sha256(repr((seed, parts)).encode()).digest()
        return int.from_bytes(digest[:8], "big") / 2**64

    async def run(
        self, case, agents, seed=0, *, checkpoint=None, suppress=(), replace_messages=None, pooled=False
    ):
        if set(agents) != set(case.private) or not agents or "__channel__" in agents:
            raise ValueError("one agent per private view required")
        if not set(case.required) <= set(agents):
            raise ValueError("required evidence names unknown recipients")
        if checkpoint is None:
            private = copy.deepcopy(case.private)
            if pooled:
                merged = {e.id: e for cards in private.values() for e in cards}
                private = {a: tuple(merged.values()) for a in private}
            state = SwarmState(
                {a: AgentState(a, private_evidence=cards) for a, cards in private.items()}, seed=seed
            )
            local = copy.deepcopy(dict(agents))
            pending, decisions, deliveries, first = [], {}, [], {}
            metrics = {
                "calls": 0,
                "generated_messages": 0,
                "generated_bytes": 0,
                "admitted_messages": 0,
                "admitted_bytes": 0,
                "receiver_input_bytes": 0,
                "decision_rounds": {},
                "decision_exposure": {},
                "tokens": 0 if self.trust_usage else None,
                "cost": 0.0 if self.trust_usage else None,
            }
            start = 0
        else:
            if checkpoint.case_id != case.id or checkpoint.seed != seed:
                raise ValueError("checkpoint case or random seed mismatch")
            pooled = checkpoint.pooled
            saved = copy.deepcopy(checkpoint)
            state, local, pending, decisions = saved.state, saved.agents, saved.pending, saved.decisions
            deliveries, metrics, first, start = (
                saved.deliveries,
                saved.metrics,
                saved.first_arrival,
                saved.round,
            )
        # State of mutable channel policies is snapshotted alongside agents.
        if checkpoint is None:
            local["__channel__"] = copy.deepcopy((self.topology, self.gate, self.transform))
        topology, gate, transform = local["__channel__"]
        snapshots = {}
        suppressed = set(suppress)
        replacements = replace_messages or {}
        started = time.perf_counter()
        for t in range(start, self.rounds):
            state.step = t
            snapshots[t] = Checkpoint(
                case.id,
                seed,
                pooled,
                t,
                copy.deepcopy(state),
                copy.deepcopy(local),
                copy.deepcopy(pending),
                copy.deepcopy(decisions),
                copy.deepcopy(deliveries),
                copy.deepcopy(metrics),
                copy.deepcopy(first),
            )
            due, pending = [p for p in pending if p[0] <= t], [p for p in pending if p[0] > t]
            if self.channel.reorder:
                due.sort(key=lambda p: self._random(seed, "order", t, p[1].id, p[2], p[3]))
            for due_round, message, recipient, _duplicate in due:
                receipt = Delivery(
                    message.id,
                    message.sender,
                    recipient,
                    message.step,
                    due_round,
                    "suppressed" if message.id in suppressed else "delivered",
                    wire_bytes(message),
                    tuple(e.id for e in message.evidence),
                )
                if message.id not in suppressed:
                    if message.id in replacements:
                        message = replace(message, content=replacements[message.id], evidence=(), metadata={})
                        receipt = replace(receipt, bytes=wire_bytes(message), evidence_ids=())
                    state.agents[recipient].inbox.append(copy.deepcopy(message))
                    for e in message.evidence:
                        first.setdefault((recipient, e.id), t)
                deliveries.append(receipt)
            outputs = {}
            # All contexts constructed before any output is incorporated.
            contexts = {
                a: AgentContext(
                    copy.deepcopy(case.task),
                    copy.deepcopy(s),
                    tuple(copy.deepcopy(s.inbox)),
                    (),
                    "decide" if t == self.rounds - 1 else "exchange",
                    t,
                )
                for a, s in state.agents.items()
            }
            for a in agents:
                context = contexts[a]
                metrics["receiver_input_bytes"] += sum(wire_bytes(m) for m in context.messages)
                result = local[a].act(context)
                output = await result if inspect.isawaitable(result) else result
                if not isinstance(output, AgentOutput):
                    raise TypeError("agent must return AgentOutput")
                if output.artifacts:
                    raise ValueError("shared artifacts disabled in communication-only experiments")
                metrics["calls"] += 1
                if self.trust_usage:
                    metrics["tokens"] += output.usage.tokens
                    metrics["cost"] += output.usage.cost
                if output.decision is not None and output.decision.agent_id != a:
                    raise ValueError("decision identity mismatch")
                outputs[a] = copy.deepcopy(output)
            for a, output in outputs.items():
                state.agents[a].memory.update(copy.deepcopy(output.memory_updates))
                if output.decision is not None:
                    decisions[a] = output.decision
                    metrics["decision_rounds"][a] = t
                    metrics["decision_exposure"][a] = sorted(
                        {e.id for e in contexts[a].agent.private_evidence}
                        | {e.id for m in contexts[a].messages for e in m.evidence}
                    )
                for index, original in enumerate(output.messages):
                    if original.sender != a or any(r not in agents for r in original.recipients):
                        raise ValueError("message identity or recipient invalid")
                    message = replace(original, id=f"{t}:{a}:{index}", step=t)
                    metrics["generated_messages"] += 1
                    metrics["generated_bytes"] += wire_bytes(message)
                    if transform:
                        message = transform(copy.deepcopy(message))
                        if not isinstance(message, Message) or message.sender != a:
                            raise ValueError("transform must preserve sender and message type")
                        message = replace(message, id=f"{t}:{a}:{index}", step=t)
                    size = wire_bytes(message)
                    allowed = set(topology.neighbors(copy.deepcopy(state), a)) if topology else set(agents)
                    recipients = tuple(
                        dict.fromkeys(
                            r for r in (message.recipients or tuple(agents)) if r != a and r in allowed
                        )
                    )
                    reason = None
                    if self.channel.disabled:
                        reason = "disabled"
                    elif gate and not gate(message):
                        reason = "gated"
                    elif (
                        self.channel.max_messages is not None
                        and metrics["admitted_messages"] >= self.channel.max_messages
                    ):
                        reason = "budget"
                    elif (
                        self.channel.max_bytes is not None
                        and metrics["admitted_bytes"] + size > self.channel.max_bytes
                    ):
                        reason = "budget"
                    if reason is None:
                        metrics["admitted_messages"] += 1
                        metrics["admitted_bytes"] += size
                        state.messages.append(copy.deepcopy(message))
                    for r in recipients:
                        status = reason or (
                            "lost" if self._random(seed, "loss", message.id, r) < self.channel.loss else None
                        )
                        due_round = t + 1 + self.channel.delay
                        if status:
                            deliveries.append(
                                Delivery(
                                    message.id,
                                    a,
                                    r,
                                    t,
                                    due_round,
                                    status,
                                    size,
                                    tuple(e.id for e in message.evidence),
                                )
                            )
                        else:
                            pending.append((due_round, copy.deepcopy(message), r, 0))
                            if self._random(seed, "duplicate", message.id, r) < self.channel.duplicate:
                                pending.append((due_round, copy.deepcopy(message), r, 1))
        for due_round, message, r, _ in pending:
            deliveries.append(
                Delivery(
                    message.id,
                    message.sender,
                    r,
                    message.step,
                    due_round,
                    "late",
                    wire_bytes(message),
                    tuple(e.id for e in message.evidence),
                )
            )
        judged = dict(decisions)
        maker = self.decision_maker or next(iter(agents))
        if maker not in agents:
            raise ValueError("unknown designated decision maker")
        if self.aggregation == "vote" and decisions:
            counts = Counter(d.answer for d in decisions.values())
            winner = min(counts, key=lambda a: (-counts[a], a))
            judged = {maker: Decision(maker, winner)}
        if self.aggregation == "designated":
            judged = {maker: decisions[maker]} if maker in decisions else {}
        evaluation_started = time.perf_counter()
        verified = dict(case.evaluate(copy.deepcopy(judged)))
        evaluation_seconds = time.perf_counter() - evaluation_started
        if not all(np.isfinite(v) for v in verified.values()):
            raise ValueError("nonfinite evaluator metric")
        required_count, recovered = 0, 0
        for a, ids in case.required.items():
            seen = {e.id for e in state.agents[a].private_evidence} | {
                e.id for m in state.agents[a].inbox for e in m.evidence
            }
            required_count += len(set(ids))
            recovered += len(set(ids) & set(metrics["decision_exposure"].get(a, seen)))
        delivered = [d for d in deliveries if d.status == "delivered"]
        metrics.update(
            {
                "outcome": verified,
                "evaluator_seconds": evaluation_seconds,
                "evidence_first_arrival": {
                    a: {e: t for (r, e), t in first.items() if r == a} for a in agents
                },
                "evidence_delivery": recovered / required_count if required_count else 1.0,
                "delivered_copies": len(delivered),
                "delivered_bytes": sum(d.bytes for d in delivered),
                "mean_delivery_rounds": float(np.mean([d.due_round - d.sent_round for d in delivered]))
                if delivered
                else None,
                "elapsed_seconds": time.perf_counter() - started,
                "replay_suffix_only_timing": checkpoint is not None,
            }
        )
        return EvaluationRun(
            case.id,
            seed,
            decisions,
            metrics,
            deliveries,
            snapshots,
            {
                "channel": asdict(self.channel),
                "rounds": self.rounds,
                "aggregation": self.aggregation,
                "pooled": pooled,
                "split": case.split,
                "agents": {
                    a: {
                        "class": type(agent).__name__,
                        "policy": getattr(agent, "policy", None)
                        if isinstance(getattr(agent, "policy", None), str)
                        else None,
                    }
                    for a, agent in agents.items()
                },
                "topology": type(topology).__name__ if topology else "full",
                "suppressed": sorted(suppressed),
                "replaced": sorted(replacements),
            },
        )

    async def replay_without(self, case, agents, run, message_id):
        if not any(d.message_id == message_id for d in run.deliveries):
            raise ValueError("unknown attempted message")
        t = int(message_id.split(":", 1)[0])
        if t not in run.checkpoints:
            raise ValueError("message creation checkpoint unavailable")
        altered = await self.run(
            case, agents, run.seed, checkpoint=run.checkpoints[t], suppress=(message_id,)
        )
        changed = {
            a: getattr(run.decisions.get(a), "answer", None)
            != getattr(altered.decisions.get(a), "answer", None)
            for a in agents
        }
        return {
            "original": run,
            "intervened": altered,
            "decision_changed": changed,
            "success_effect": run.metrics["outcome"]["success"] - altered.metrics["outcome"]["success"],
        }


def paired_summary(left, right, metric="success", bootstrap=2000, seed=0):
    """Pair by case+seed, average repeats per case, bootstrap independent cases."""

    def index(runs):
        result = {(r.case_id, r.seed): r for r in runs}
        if len(result) != len(runs):
            raise ValueError("duplicate run identity")
        return result

    a, b = index(left), index(right)
    if not a or set(a) != set(b) or bootstrap < 1:
        raise ValueError("nonempty matched cases/seeds required")
    differences = {}
    for key in a:
        differences.setdefault(key[0], []).append(
            a[key].metrics["outcome"][metric] - b[key].metrics["outcome"][metric]
        )
    values = np.array([np.mean(v) for v in differences.values()])
    if not np.isfinite(values).all():
        raise ValueError("nonfinite paired metric")
    draws = np.random.default_rng(seed).choice(values, (bootstrap, len(values)), replace=True).mean(axis=1)
    return {
        "mean_difference": float(values.mean()),
        "interval_95": np.quantile(draws, [0.025, 0.975]).tolist(),
        "independent_cases": len(values),
        "paired_runs": len(a),
    }


def quality_cost_summary(runs):
    """One condition's observed quality and cost; unavailable usage stays unknown."""
    if not runs:
        raise ValueError("nonempty run collection required")
    result = {"runs": len(runs), "success": float(np.mean([r.metrics["outcome"]["success"] for r in runs]))}
    for metric in ("calls", "tokens", "cost", "generated_bytes", "delivered_bytes", "receiver_input_bytes"):
        values = [r.metrics[metric] for r in runs]
        result[metric] = None if any(v is None for v in values) else float(np.mean(values))
    return result
