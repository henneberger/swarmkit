"""Coordination through persistent artifacts and decaying environmental traces.

SwarmSys/SwarmWorld-inspired mechanisms, not their complete simulators:
https://arxiv.org/abs/2510.10047 ; https://arxiv.org/abs/2608.26081
The numeric pheromone policy is an explicit adaptation, not a claim that the
SwarmSys implementation uses this formula.
"""

from __future__ import annotations

import math
from copy import deepcopy
from dataclasses import dataclass
from typing import Callable

from .types import AlgorithmResult, Artifact, Feedback, Message, MessageKind, SwarmState, Task


@dataclass(frozen=True)
class StigmergicPolicy:
    """Select locally visible artifacts by decayed verified contribution traces.

    Selection is epsilon-greedy. ``verify`` is an optional recipient-specific
    evaluator; a failed local check cannot become a successful adoption. With no
    evaluator, previously verified artifacts are exposed as observations only.
    A shared artifact remains valid after its author disappears; traces decay,
    while immutable artifacts and ancestry remain in the common store.
    """

    half_life: float = 10.0
    exploration: float = 0.1
    radius: float | None = None
    verify: Callable[[str, Artifact, Task], Feedback] | None = None
    minimum_utility: float = 0.0
    namespace: str = "stigmergy"

    def __post_init__(self):
        if not math.isfinite(self.half_life) or self.half_life <= 0:
            raise ValueError("half_life must be positive")
        if not 0 <= self.exploration <= 1 or not math.isfinite(self.minimum_utility):
            raise ValueError("invalid exploration or minimum utility")
        if self.radius is not None and (not math.isfinite(self.radius) or self.radius < 0):
            raise ValueError("radius must be nonnegative and finite")

    def deposit(self, state: SwarmState, artifact_id: str, contributor: str, strength: float = 1.0) -> None:
        if artifact_id not in state.artifacts or contributor not in state.agents:
            raise ValueError("unknown artifact or contributor")
        if not state.artifacts[artifact_id].verified:
            raise ValueError("only verified artifacts may receive success traces")
        if not math.isfinite(strength) or strength < 0:
            raise ValueError("trace strength must be finite and nonnegative")
        records = state.data.setdefault(self.namespace, {})
        traces = records.setdefault(artifact_id, {})
        # One trace per contributor; repeats refresh rather than counterfeit independent support.
        traces[contributor] = {"strength": strength, "step": state.step}

    def strength(self, state: SwarmState, artifact_id: str) -> float:
        traces = state.data.get(self.namespace, {}).get(artifact_id, {})
        total = 0.0
        for trace in traces.values():
            age = state.step - trace["step"]
            if age < 0:
                raise ValueError("state step precedes stored trace")
            strength = trace["strength"]
            if not math.isfinite(strength) or strength < 0:
                raise ValueError("stored trace strength must be finite and nonnegative")
            total += strength * 2 ** (-age / self.half_life)
        if not math.isfinite(total):
            raise ValueError("aggregate trace strength exceeds numerical range")
        return total

    def _visible(self, state: SwarmState, agent_id: str, artifact: Artifact) -> bool:
        if self.radius is None:
            return True
        position = state.agents[agent_id].position
        location = artifact.metadata.get("position")
        if position is None or location is None:
            return False
        if len(position) != len(location) or not all(math.isfinite(x) for x in (*position, *location)):
            raise ValueError("invalid artifact/agent coordinates")
        return math.dist(position, location) <= self.radius

    def step(self, state: SwarmState, task: Task) -> AlgorithmResult:
        messages, adopted, observed = [], 0, 0
        # Freeze current traces to prevent the first mover biasing this same round.
        weights = {key: self.strength(state, key) for key in state.artifacts}
        deposits = []
        for agent_id in state.active_ids:
            # Recipient-specific usefulness can change with the task.
            memory = state.agents[agent_id].memory.setdefault(self.namespace + ":seen:" + task.id, set())
            candidates = [
                a
                for a in state.artifacts.values()
                if a.verified and a.id not in memory and self._visible(state, agent_id, a)
            ]
            if not candidates:
                continue
            if state.rng.random() < self.exploration:
                artifact = state.rng.choice(candidates)
            else:
                artifact = max(candidates, key=lambda a: (weights[a.id], a.score or 0, a.id))
            accepted = False
            if self.verify:
                feedback = self.verify(agent_id, deepcopy(artifact), deepcopy(task))
                if (
                    not isinstance(feedback, Feedback)
                    or not math.isfinite(feedback.utility)
                    or not math.isfinite(feedback.costs)
                    or feedback.costs < 0
                ):
                    raise ValueError("local evaluator must return finite Feedback")
                accepted = feedback.verified and feedback.utility >= self.minimum_utility
                if accepted:
                    state.agents[agent_id].memory.setdefault("adopted_artifacts", set()).add(artifact.id)
                    deposits.append((artifact.id, agent_id, max(0.0, feedback.utility)))
                    adopted += 1
            memory.add(artifact.id)
            observed += 1
            messages.append(
                Message(
                    agent_id,
                    f"{'Adopted' if accepted else 'Observed'} artifact {artifact.id}",
                    kind=MessageKind.RESULT if accepted else MessageKind.OBSERVATION,
                    artifact_ids=(artifact.id,),
                    step=state.step,
                    id=f"{self.namespace}:{task.id}:{state.step}:{agent_id}:{artifact.id}",
                    metadata={"verified_local_adoption": accepted},
                )
            )
        for artifact_id, agent_id, strength in deposits:
            self.deposit(state, artifact_id, agent_id, strength)
        return AlgorithmResult(
            messages=tuple(messages), metrics={"observed": float(observed), "adopted": float(adopted)}
        )
