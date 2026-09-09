"""Population search over shared Artifact configurations.

Mechanism-level SwarmAgentic adaptation (https://arxiv.org/abs/2506.15672):
personal/population best and failure histories guide an injected mutation operator.
This module does not pretend a numeric PSO velocity is meaningful for arbitrary
language-configured agent systems; callers implement their own update semantics.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, replace
from typing import Callable, Sequence

from .types import AlgorithmResult, Artifact, Feedback, SwarmState, Task

Mutation = Callable[[Artifact, Artifact, Artifact, tuple[Artifact, ...], random.Random], Artifact]
Evaluation = Callable[[Artifact], Feedback]


@dataclass(frozen=True)
class ParticleSwarmSearch:
    """Search an artifact population with injected evaluation and mutation.

    ``mutate(current, personal_best, global_best, failures, rng)`` must return
    a fresh Artifact id and retain the particle's author. ``evaluate`` returns
    canonical Feedback. Maximizes utility minus costs by default. Every step
    evaluates one candidate per particle, using the same frozen global best.
    Initial evaluation occurs on the first step. Caller commits returned artifacts
    and advances time. Failed improvements persist as per-particle failure memory.
    """

    initial: Sequence[Artifact]
    evaluate: Evaluation
    mutate: Mutation
    maximize: bool = True
    failure_limit: int = 32
    key: str = "particle_swarm"

    def __post_init__(self) -> None:
        if not self.initial:
            raise ValueError("a nonempty initial population is required")
        if len({a.id for a in self.initial}) != len(self.initial):
            raise ValueError("initial artifact ids must be unique")
        if self.failure_limit < 1:
            raise ValueError("failure_limit must be positive")

    def _evaluate(self, candidate: Artifact, step: int) -> Artifact:
        feedback = self.evaluate(candidate)
        if not isinstance(feedback, Feedback):
            raise TypeError("evaluate must return Feedback")
        if not math.isfinite(feedback.utility) or not math.isfinite(feedback.costs):
            raise ValueError("evaluation must return finite utility and costs")
        # Cost always worsens an objective, including when minimizing.
        score = feedback.utility - feedback.costs if self.maximize else feedback.utility + feedback.costs
        return replace(
            candidate,
            score=score,
            verified=feedback.verified,
            created_step=step,
            metadata={
                **candidate.metadata,
                "evaluation": {
                    "utility": feedback.utility,
                    "costs": feedback.costs,
                    "details": dict(feedback.metadata),
                },
            },
        )

    def _better(self, a: Artifact, b: Artifact) -> bool:
        assert a.score is not None and b.score is not None
        return a.score > b.score if self.maximize else a.score < b.score

    def _best(self, population: Sequence[Artifact]) -> Artifact:
        return (max if self.maximize else min)(population, key=lambda a: a.score)

    def step(self, state: SwarmState, task: Task) -> AlgorithmResult:
        rec = state.data.get(self.key)
        if rec is None:
            for artifact in self.initial:
                if artifact.author not in state.agents:
                    raise ValueError("each particle author must be a known swarm agent")
                if artifact.id in state.artifacts:
                    raise ValueError("initial artifact id already exists in the swarm")
            evaluated = tuple(self._evaluate(a, state.step) for a in self.initial)
            rec = {
                "task_id": task.id,
                "current": evaluated,
                "personal": evaluated,
                "global": self._best(evaluated),
                "failures": [() for _ in evaluated],
                "seen_ids": {a.id for a in evaluated},
                "generation": 0,
            }
            state.data[self.key] = rec
        else:
            if rec["task_id"] != task.id:
                raise ValueError("search state belongs to a different task; use a fresh key")
            global_best = rec["global"]
            candidates = []
            seen = rec["seen_ids"] | set(state.artifacts)
            for i, current in enumerate(rec["current"]):
                candidate = self.mutate(
                    current, rec["personal"][i], global_best, rec["failures"][i], state.rng
                )
                if not isinstance(candidate, Artifact):
                    raise TypeError("mutate must return Artifact")
                if candidate.id in seen:
                    raise ValueError("mutation must produce a fresh artifact id")
                if candidate.author != current.author:
                    raise ValueError("mutation must preserve particle author")
                seen.add(candidate.id)
                parents = tuple(
                    dict.fromkeys((*candidate.parents, current.id, rec["personal"][i].id, global_best.id))
                )
                candidates.append(replace(candidate, parents=parents))
            evaluated = tuple(self._evaluate(a, state.step) for a in candidates)
            personal = list(rec["personal"])
            failures = list(rec["failures"])
            for i, candidate in enumerate(evaluated):
                if self._better(candidate, personal[i]):
                    personal[i] = candidate
                else:
                    failures[i] = (*failures[i], candidate)[-self.failure_limit :]
            rec.update(
                {
                    "current": evaluated,
                    "personal": tuple(personal),
                    "global": self._best(personal),
                    "failures": failures,
                    "seen_ids": seen,
                    "generation": rec["generation"] + 1,
                }
            )
        best = rec["global"]
        return AlgorithmResult(
            artifacts=evaluated,
            metrics={
                "best_score": float(best.score),
                "generation": float(rec["generation"]),
                "evaluations": float(len(evaluated)),
                "failure_memory_size": float(sum(map(len, rec["failures"]))),
            },
            metadata={"best_artifact_id": best.id, "personal_best_ids": tuple(a.id for a in rec["personal"])},
        )
