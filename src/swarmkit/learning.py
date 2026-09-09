"""Small trainable coordination policies and explicit swarm reward components.

MAPoRL: https://arxiv.org/abs/2502.18439
PARL: https://arxiv.org/abs/2602.02276

These NumPy policies train communication/allocation choices, not transformer
weights. They provide executable reward/optimization primitives for plugging in
larger trainers; they do not reproduce either paper's proprietary model training.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike

from .types import Feedback, Message, SwarmState


class SoftmaxPolicy:
    """Linear categorical policy with REINFORCE and clipped PPO updates."""

    def __init__(self, features: int, actions: int, *, learning_rate: float = 0.01):
        if (
            not isinstance(features, (int, np.integer))
            or not isinstance(actions, (int, np.integer))
            or features < 1
            or actions < 2
            or not math.isfinite(learning_rate)
            or learning_rate <= 0
        ):
            raise ValueError("positive feature count/rate and at least two actions required")
        self.weights = np.zeros((features, actions), dtype=float)
        self.learning_rate = learning_rate

    def probabilities(self, features: ArrayLike) -> np.ndarray:
        x = np.asarray(features, dtype=float)
        if x.shape != (self.weights.shape[0],) or not np.isfinite(x).all():
            raise ValueError("invalid policy feature vector")
        with np.errstate(over="ignore", invalid="ignore"):
            logits = x @ self.weights
        if not np.isfinite(logits).all():
            raise ValueError("policy logits must be finite")
        with np.errstate(over="ignore", under="ignore"):
            exp = np.exp(logits - logits.max())
        return exp / exp.sum()

    def sample(self, features: ArrayLike, state: SwarmState) -> tuple[int, float]:
        p = self.probabilities(features)
        action = state.rng.choices(range(len(p)), weights=p, k=1)[0]
        return action, float(np.log(max(p[action], 1e-300)))

    def update(
        self,
        features: ArrayLike,
        action: int,
        advantage: float,
        *,
        old_log_probability: float | None = None,
        clip: float = 0.2,
        entropy_weight: float = 0.0,
    ) -> Mapping[str, float]:
        p = self.probabilities(features)
        if (
            not isinstance(action, (int, np.integer))
            or not 0 <= action < len(p)
            or not all(math.isfinite(v) for v in (advantage, clip, entropy_weight))
        ):
            raise ValueError("invalid action or update values")
        if not 0 < clip < 1 or entropy_weight < 0:
            raise ValueError("clip must be in (0,1), entropy weight nonnegative")
        logp = float(np.log(max(p[action], 1e-300)))
        ratio = 1.0
        coefficient = advantage
        if old_log_probability is not None:
            if not math.isfinite(old_log_probability) or old_log_probability > 0:
                raise ValueError("old log probability must be finite and nonpositive")
            try:
                ratio = math.exp(logp - old_log_probability)
            except OverflowError as error:
                raise ValueError("importance ratio exceeds numerical range") from error
            # Gradient of min(r*A, clip(r)*A) vanishes on the clipped branch.
            saturated = (advantage >= 0 and ratio > 1 + clip) or (advantage < 0 and ratio < 1 - clip)
            coefficient = 0.0 if saturated else ratio * advantage
        score = -p.copy()
        score[action] += 1
        log_probs = np.log(np.maximum(p, 1e-300))
        entropy = float(-np.sum(p * log_probs))
        entropy_gradient = -p * (log_probs + entropy)
        with np.errstate(over="ignore", invalid="ignore"):
            updated = self.weights + self.learning_rate * np.outer(
                np.asarray(features), coefficient * score + entropy_weight * entropy_gradient
            )
        if not np.isfinite(updated).all():
            raise ValueError("policy update exceeds numerical range")
        self.weights = updated
        return {"ratio": ratio, "entropy": entropy, "coefficient": coefficient}


@dataclass(frozen=True)
class CollaborativeReward:
    """Correctness plus measured peer improvement minus communication cost.

    Peer changes must come from a caller-controlled evaluator. Improvement is
    not inferred from confidence or persuasiveness. MAPoRL-inspired adaptation.
    """

    influence_weight: float = 1.0
    cost_weight: float = 0.0

    def __post_init__(self):
        if any(not math.isfinite(v) or v < 0 for v in (self.influence_weight, self.cost_weight)):
            raise ValueError("reward weights must be finite and nonnegative")

    def __call__(
        self,
        correctness: float,
        before: Mapping[str, float],
        after: Mapping[str, float],
        *,
        cost: float = 0.0,
    ) -> Feedback:
        if set(before) != set(after):
            raise ValueError("before and after must cover the same peers")
        numbers = [
            correctness,
            cost,
            self.influence_weight,
            self.cost_weight,
            *before.values(),
            *after.values(),
        ]
        if not all(math.isfinite(x) for x in numbers) or cost < 0:
            raise ValueError("reward inputs must be finite and cost nonnegative")
        improvements = {agent: after[agent] - before[agent] for agent in before}
        mean = sum(improvements.values()) / len(improvements) if improvements else 0.0
        utility = correctness + self.influence_weight * mean - self.cost_weight * cost
        if not math.isfinite(utility) or not all(math.isfinite(v) for v in improvements.values()):
            raise ValueError("reward exceeds numerical range")
        return Feedback(utility, costs=cost, per_agent=improvements)


def counterfactual_message_credit(
    messages: Sequence[Message], evaluate: Callable[[Sequence[Message]], float]
) -> Mapping[str, float]:
    """Leave-one-message-out utility differences; deterministic evaluation required."""
    if len({m.id for m in messages}) != len(messages):
        raise ValueError("message ids must be unique")
    full = evaluate(tuple(messages))
    if not math.isfinite(full):
        raise ValueError("evaluator returned non-finite utility")
    credits = {}
    for index, message in enumerate(messages):
        ablated = evaluate(tuple(messages[:index]) + tuple(messages[index + 1 :]))
        if not math.isfinite(ablated):
            raise ValueError("evaluator returned non-finite utility")
        credits[message.id] = full - ablated
        if not math.isfinite(credits[message.id]):
            raise ValueError("credit exceeds numerical range")
    return credits


@dataclass(frozen=True)
class ParallelReward:
    """PARL-inspired useful-parallelism shaping with annealed auxiliary terms.

    Workload performance remains after annealing. Critical-path cost is explicit
    and separate from total compute; spawning unsuccessful tasks gives no credit.
    """

    parallel_weight: float = 0.1
    completion_weight: float = 0.1
    critical_path_weight: float = 0.0
    anneal_steps: int = 100

    def __post_init__(self):
        if (
            not isinstance(self.anneal_steps, int)
            or self.anneal_steps < 1
            or any(
                not math.isfinite(v) or v < 0
                for v in (self.parallel_weight, self.completion_weight, self.critical_path_weight)
            )
        ):
            raise ValueError("invalid reward configuration")

    def __call__(
        self,
        performance: float,
        *,
        spawned: int,
        completed: int,
        critical_path_steps: float,
        training_step: int,
    ) -> Feedback:
        if (
            any(not isinstance(v, (int, np.integer)) for v in (spawned, completed, training_step))
            or spawned < 0
            or not 0 <= completed <= spawned
            or training_step < 0
        ):
            raise ValueError("invalid task counts or training step")
        if (
            not math.isfinite(performance)
            or not math.isfinite(critical_path_steps)
            or critical_path_steps < 0
        ):
            raise ValueError("invalid performance or critical path")
        anneal = max(0.0, 1 - training_step / self.anneal_steps)
        useful_parallelism = max(0, completed - 1) / max(1, spawned)
        fraction = completed / max(1, spawned)
        auxiliary = self.parallel_weight * useful_parallelism + self.completion_weight * fraction
        utility = performance + anneal * auxiliary - self.critical_path_weight * critical_path_steps
        if not math.isfinite(utility) or not math.isfinite(auxiliary):
            raise ValueError("parallel reward exceeds numerical range")
        return Feedback(
            utility, costs=critical_path_steps, metadata={"anneal": anneal, "auxiliary": auxiliary}
        )
