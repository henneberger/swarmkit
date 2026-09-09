"""Synchronous-round, concurrent agent execution over the canonical data types.

No paid model calls, external services, or arbitrary artifact execution are built
in. A round exposes only each agent's own state and delivered messages. Tasks and
artifacts are explicitly public. This is logical isolation, not an OS sandbox.
"""

from __future__ import annotations

import asyncio
import copy
import inspect
import json
import math
from dataclasses import fields, is_dataclass, replace
from typing import Any, Awaitable, Callable, Mapping, Sequence

import numpy as np

from .types import (
    Agent,
    AgentContext,
    AgentOutput,
    AlgorithmResult,
    Artifact,
    Budget,
    Decision,
    Evidence,
    Feedback,
    Message,
    SwarmAlgorithm,
    SwarmState,
    Task,
    TopologyPolicy,
    Usage,
)


def _same_value(left: Any, right: Any) -> bool:
    """Structural identity checks also support canonical numeric channel payloads."""
    if type(left) is not type(right):
        return False
    if isinstance(left, np.ndarray):
        return bool(np.array_equal(left, right))
    if is_dataclass(left):
        return all(_same_value(getattr(left, f.name), getattr(right, f.name)) for f in fields(left))
    if isinstance(left, Mapping):
        return left.keys() == right.keys() and all(_same_value(left[k], right[k]) for k in left)
    if isinstance(left, (tuple, list)):
        return len(left) == len(right) and all(_same_value(a, b) for a, b in zip(left, right, strict=True))
    return bool(left == right)


class MessageBus:
    """Route explicit recipients through the topology, with at-most-once delivery.

    Topology restrictions apply to direct messages AND broadcasts. Filters may
    drop a message globally or independently for a recipient. Neither a message
    id nor sender identity is cryptographically authenticated by this local bus.
    """

    def __init__(
        self,
        topology: TopologyPolicy | None = None,
        gate: Callable[[Message], bool] | None = None,
        recipient_filter: Callable[[Message, str], bool] | None = None,
    ) -> None:
        self.topology = topology
        self.gate = gate
        self.recipient_filter = recipient_filter

    def publish(self, state: SwarmState, message: Message) -> tuple[str, ...]:
        """Commit delivery atomically, including stateful topology changes.

        External side effects inside user-supplied filters are not reversible.
        Filters should be pure; topology memory belongs in SwarmState.data.
        """
        staged = copy.deepcopy(state)
        recipients = self._publish(staged, message)
        _commit_state(state, staged)
        return recipients

    def _publish(self, state: SwarmState, message: Message) -> tuple[str, ...]:
        if not isinstance(message, Message):
            raise TypeError("publish requires Message")
        if not isinstance(message.id, str) or not message.id or not isinstance(message.content, str):
            raise ValueError("message requires a nonempty id and text content")
        if isinstance(message.recipients, (str, bytes)):
            raise ValueError("recipients must be a sequence of agent ids, not a string")
        if any(not isinstance(e, Evidence) for e in message.evidence):
            raise TypeError("message evidence must use Evidence instances")
        if message.sender not in state.agents:
            raise ValueError(f"unknown sender: {message.sender}")
        if any(r not in state.agents for r in message.recipients):
            raise ValueError("message addresses an unknown recipient")
        existing = next((m for m in state.messages if m.id == message.id), None)
        if existing is not None:
            if not _same_value(existing, message):
                raise ValueError("message id reused with different content")
            return ()
        if not state.agents[message.sender].active or (self.gate and not self.gate(message)):
            return ()
        allowed = (
            set(self.topology.neighbors(state, message.sender)) if self.topology else set(state.active_ids)
        )
        requested = message.recipients or state.active_ids
        recipients = tuple(
            dict.fromkeys(
                r
                for r in requested
                if r != message.sender
                and r in allowed
                and state.agents[r].active
                and (self.recipient_filter is None or self.recipient_filter(message, r))
            )
        )
        # Snapshot message metadata and evidence to prevent downstream mutation.
        stored = copy.deepcopy(message)
        state.messages.append(stored)
        for recipient in recipients:
            state.agents[recipient].inbox.append(copy.deepcopy(stored))
        return recipients


def _commit_state(state: SwarmState, staged: SwarmState) -> None:
    """Preserve the shared state's identity, replace its transaction snapshot."""
    state.agents = staged.agents
    state.messages = staged.messages
    state.artifacts = staged.artifacts
    state.data = staged.data
    state.step = staged.step
    state.rng.setstate(staged.rng.getstate())


def apply_result(state: SwarmState, result: AlgorithmResult, bus: MessageBus | None = None) -> None:
    """Atomically commit an output batch; method-local mutations precede this call.

    Routing errors roll back this batch, including topology/RNG state. Already
    performed external side effects or algorithm.step mutations cannot roll back.
    """
    if not isinstance(result, AlgorithmResult):
        raise TypeError("result must be AlgorithmResult")
    bus = bus or MessageBus()
    staged = copy.deepcopy(state)
    for artifact in result.artifacts:
        if not isinstance(artifact, Artifact):
            raise TypeError("result artifacts must be Artifact instances")
        previous = staged.artifacts.get(artifact.id)
        if previous is not None and not _same_value(previous, artifact):
            raise ValueError(f"artifact id already exists: {artifact.id}")
        staged.artifacts[artifact.id] = copy.deepcopy(artifact)
    for message in result.messages:
        bus._publish(staged, message)
    if result.decisions:
        if any(not isinstance(d, Decision) or d.agent_id not in staged.agents for d in result.decisions):
            raise ValueError("decisions must belong to known agents")
        staged.data["decisions"] = copy.deepcopy(list(result.decisions))
    _commit_state(state, staged)


class CallableAgent:
    """Adapt a sync or async callback; sync callbacks execute in a worker thread."""

    def __init__(self, callback: Callable[[AgentContext], AgentOutput | Awaitable[AgentOutput]]) -> None:
        self.callback = callback

    async def act(self, context: AgentContext) -> AgentOutput:
        if inspect.iscoroutinefunction(self.callback):
            output = await self.callback(context)
        else:
            output = await asyncio.to_thread(self.callback, context)
            if inspect.isawaitable(output):
                output = await output
        if not isinstance(output, AgentOutput):
            raise TypeError("agent callback must return AgentOutput")
        return output


class CompletionAgent:
    """Connect any text-completion provider through an injected callable.

    The callable receives a string prompt, returning text (or an awaitable).
    For decision phases request JSON with answer/confidence/evidence_ids. Only
    supplied evidence ids are accepted; unknown candidates are rejected. Provider
    token/cost accounting needs a custom AgentOutput-producing adapter.
    """

    def __init__(self, complete: Callable[[str], str | Awaitable[str]], *, system: str = "") -> None:
        self.complete = complete
        self.system = system

    async def act(self, context: AgentContext) -> AgentOutput:
        histories = copy.deepcopy(context.agent.memory.get("completion_received_evidence", {}))
        received = {e.id: e for e in histories.get(context.task.id, ())}
        for message in context.messages:
            for evidence in message.evidence:
                if not isinstance(evidence, Evidence):
                    raise TypeError("received evidence must use the canonical Evidence type")
                previous = received.get(evidence.id)
                if previous is not None and not _same_value(previous, evidence):
                    raise ValueError("conflicting received evidence id")
                received[evidence.id] = evidence
        available = dict(received)
        for evidence in context.agent.private_evidence:
            if evidence.id in available and not _same_value(available[evidence.id], evidence):
                raise ValueError("received evidence conflicts with private evidence")
            available[evidence.id] = evidence
        histories[context.task.id] = tuple(received.values())
        memory_updates = {"completion_received_evidence": histories}
        prompt = json.dumps(
            {
                "system": self.system,
                "task": context.task.description,
                "phase": context.phase,
                "agent": context.agent.id,
                "candidates": context.task.candidates,
                "evidence": [{"id": e.id, "claim": e.claim, "source": e.source} for e in available.values()],
                "messages": [{"sender": m.sender, "content": m.content} for m in context.messages],
                "output": "JSON object with answer, confidence, evidence_ids, rationale"
                if context.phase == "decide"
                else "Share relevant evidence, uncertainties, or questions.",
            }
        )
        if inspect.iscoroutinefunction(self.complete):
            text = await self.complete(prompt)
        else:
            text = await asyncio.to_thread(self.complete, prompt)
            if inspect.isawaitable(text):
                text = await text
        if not isinstance(text, str):
            raise TypeError("completion must return text")
        if context.phase == "decide":
            data = json.loads(text)
            answer = str(data["answer"])
            if context.task.candidates and answer not in context.task.candidates:
                raise ValueError("completion chose an unknown candidate")
            evidence_ids = tuple(data.get("evidence_ids", ()))
            if any(eid not in available for eid in evidence_ids):
                raise ValueError("completion cites evidence it was not supplied")
            decision = Decision(
                context.agent.id,
                answer,
                float(data.get("confidence", 1)),
                evidence_ids,
                str(data.get("rationale", "")),
            )
            return AgentOutput(decision=decision, memory_updates=memory_updates)
        return AgentOutput(
            messages=(Message(context.agent.id, text, step=context.step),), memory_updates=memory_updates
        )


class SwarmRuntime:
    """Bounded-concurrency coordinator for arbitrary agent implementations.

    Agents see a snapshot at the beginning of each round, never another agent's
    private facts or intermediate output from that round. max_calls bounds
    dispatched act() invocations. Token/cost limits stop FUTURE dispatch after
    reported usage arrives; concurrently in-flight calls can exceed those soft limits.
    Exceptions are recorded per agent. fail_fast=True raises after dispatch completes
    and rolls back round outputs. Timeout stops waiting
    but cannot forcibly terminate a synchronous callback's underlying thread.
    """

    def __init__(
        self,
        state: SwarmState,
        agents: Mapping[str, Agent],
        *,
        bus: MessageBus | None = None,
        budget: Budget | None = None,
        concurrency: int = 8,
        timeout: float | None = 60.0,
        verifier: Callable[[Artifact], Feedback] | None = None,
        fail_fast: bool = False,
    ) -> None:
        if (
            not isinstance(concurrency, int)
            or concurrency < 1
            or (timeout is not None and (not math.isfinite(timeout) or timeout <= 0))
        ):
            raise ValueError("concurrency and timeout must be positive")
        if set(agents) - set(state.agents):
            raise ValueError("runtime agent ids must exist in SwarmState")
        self.state, self.agents = state, dict(agents)
        self.bus, self.budget = bus or MessageBus(), budget or Budget()
        self.concurrency, self.timeout = concurrency, timeout
        self.verifier, self.fail_fast = verifier, fail_fast
        self._lock = asyncio.Lock()

    async def round(
        self, task: Task, *, phase: str = "explore", participants: Sequence[str] | None = None
    ) -> AlgorithmResult:
        async with self._lock:
            if self.budget.exhausted:
                return AlgorithmResult(metadata={"stopped": "budget"})
            selected = tuple(
                dict.fromkeys(participants if participants is not None else self.state.active_ids)
            )
            if set(selected) - set(self.state.agents):
                raise ValueError("unknown participant")
            selected = tuple(i for i in selected if self.state.agents[i].active and i in self.agents)
            if self.budget.max_calls is not None:
                selected = selected[: max(0, self.budget.max_calls - self.budget.used_calls)]
            contexts = [
                AgentContext(
                    copy.deepcopy(task),
                    copy.deepcopy(self.state.agents[i]),
                    tuple(copy.deepcopy(self.state.agents[i].inbox)),
                    tuple(copy.deepcopy(list(self.state.artifacts.values()))),
                    phase,
                    self.state.step,
                )
                for i in selected
            ]
            if not selected:
                return AlgorithmResult(metadata={"stopped": "no_participants"})
            semaphore = asyncio.Semaphore(self.concurrency)
            dispatched = 0
            skipped = object()

            async def invoke(agent_id: str, context: AgentContext) -> AgentOutput | object:
                nonlocal dispatched
                async with semaphore:
                    # Account at actual dispatch, so cancelled/over-budget queued
                    # work does not consume calls it never made.
                    if self.budget.exhausted:
                        return skipped
                    self.budget.used_calls += 1
                    dispatched += 1
                    call = self.agents[agent_id].act(context)
                    output = await asyncio.wait_for(call, self.timeout) if self.timeout else await call
                    if isinstance(output, AgentOutput):
                        usage = output.usage
                        if (
                            not isinstance(usage, Usage)
                            or not isinstance(usage.tokens, int)
                            or usage.tokens < 0
                            or not math.isfinite(usage.cost)
                            or usage.cost < 0
                        ):
                            raise ValueError("agent reported invalid usage")
                        self.budget.used_tokens += usage.tokens
                        self.budget.used_cost += usage.cost
                    return output

            # External cancellation cancels children and exits before committing
            # any output. A child cancelling itself is isolated like a failure.
            outputs = await asyncio.gather(
                *(invoke(i, c) for i, c in zip(selected, contexts, strict=True)), return_exceptions=True
            )
            messages: list[Message] = []
            artifacts: list[Artifact] = []
            decisions: list[Decision] = []
            errors: dict[str, str] = {}
            working = copy.deepcopy(self.state)
            for agent_id, context, output in zip(selected, contexts, outputs, strict=True):
                if output is skipped:
                    continue  # queued invocation skipped after budget exhaustion
                try:
                    if isinstance(output, asyncio.CancelledError):
                        raise RuntimeError("agent invocation was cancelled")
                    if isinstance(output, BaseException):
                        raise output
                    if not isinstance(output, AgentOutput):
                        raise TypeError("act() must return AgentOutput")
                    if any(not isinstance(m, Message) or m.sender != agent_id for m in output.messages):
                        raise ValueError("agent output spoofs a different sender or is malformed")
                    if any(not isinstance(a, Artifact) or a.author != agent_id for a in output.artifacts):
                        raise ValueError("agent output spoofs an artifact author or is malformed")
                    if output.decision and (
                        not isinstance(output.decision, Decision) or output.decision.agent_id != agent_id
                    ):
                        raise ValueError("agent output spoofs a decision author")
                    if any(r not in working.agents for m in output.messages for r in m.recipients):
                        raise ValueError("agent output addresses an unknown recipient")
                    # Freeze/validate every part before touching shared state.
                    memory_updates = copy.deepcopy(dict(output.memory_updates))
                    approved = []
                    ids = set(working.artifacts)
                    for artifact in output.artifacts:
                        if artifact.id in ids:
                            raise ValueError("artifact id already exists")
                        ids.add(artifact.id)
                        artifact = copy.deepcopy(artifact)
                        if self.verifier:
                            feedback = self.verifier(artifact)
                            if not isinstance(feedback, Feedback):
                                raise TypeError("verifier must return Feedback")
                            artifact = replace(artifact, verified=feedback.verified, score=feedback.utility)
                        else:
                            artifact = replace(artifact, verified=False)
                        approved.append(artifact)
                    result = AlgorithmResult(
                        output.messages, (output.decision,) if output.decision else (), tuple(approved)
                    )
                    staged = copy.deepcopy(working)
                    apply_result(staged, result, self.bus)
                    # Acknowledge only the inbox snapshot consumed by this agent.
                    consumed = {m.id for m in context.messages}
                    staged.agents[agent_id].inbox[:] = [
                        m for m in staged.agents[agent_id].inbox if m.id not in consumed
                    ]
                    staged.agents[agent_id].memory.update(memory_updates)
                    working = staged
                    messages.extend(copy.deepcopy(output.messages))
                    artifacts.extend(copy.deepcopy(approved))
                    if output.decision:
                        decisions.append(copy.deepcopy(output.decision))
                except Exception as exc:
                    errors[agent_id] = f"{type(exc).__name__}: {exc}"
                    if self.fail_fast:
                        raise
            working.step += 1
            working.data["decisions"] = copy.deepcopy(decisions)
            _commit_state(self.state, working)
            self.budget.used_steps += 1
            return AlgorithmResult(
                tuple(messages),
                tuple(decisions),
                tuple(artifacts),
                {"calls": float(dispatched), "errors": float(len(errors))},
                {"errors": errors, "budget_exhausted": self.budget.exhausted},
            )

    async def run(
        self, task: Task, phases: Sequence[str] = ("explore", "critique", "decide")
    ) -> AlgorithmResult:
        messages, decisions, artifacts, errors = [], [], [], {}
        for phase in phases:
            if self.budget.exhausted:
                break
            result = await self.round(task, phase=phase)
            messages.extend(result.messages)
            artifacts.extend(result.artifacts)
            if result.decisions:
                decisions = list(result.decisions)
            errors.update(result.metadata.get("errors", {}))
        return AlgorithmResult(
            tuple(messages),
            tuple(decisions),
            tuple(artifacts),
            {
                "calls": float(self.budget.used_calls),
                "tokens": float(self.budget.used_tokens),
                "cost": self.budget.used_cost,
            },
            {"errors": errors},
        )


class Pipeline:
    """Compose synchronous swarm algorithms; all share the same state and task."""

    def __init__(self, algorithms: Sequence[SwarmAlgorithm], *, bus: MessageBus | None = None) -> None:
        self.algorithms = tuple(algorithms)
        self.bus = bus or MessageBus()

    def step(self, state: SwarmState, task: Task) -> AlgorithmResult:
        messages, decisions, artifacts, metrics = [], [], [], {}
        for index, algorithm in enumerate(self.algorithms):
            result = algorithm.step(state, task)
            apply_result(state, result, self.bus)
            messages.extend(result.messages)
            decisions.extend(result.decisions)
            artifacts.extend(result.artifacts)
            metrics.update({f"{index}.{key}": value for key, value in result.metrics.items()})
            state.step += 1
        return AlgorithmResult(tuple(messages), tuple(decisions), tuple(artifacts), metrics)
