"""Empirical population games and finite evolutionary ranking."""

from __future__ import annotations

import numpy as np

from .games import NormalFormGame
from .strategies import ExternalRegretPolicy


class PolicySpaceResponseOracles:
    """Two-role empirical PSRO with caller response training and empirical CCE meta-solver.

    Policies are opaque objects. Oracle(player, opposing policies, mixture) returns
    a new policy. Evaluation is a caller-supplied pure held-out payoff function.
    The general-sum meta-solver reports restricted deviations, not a Nash guarantee.
    """

    def __init__(self, populations, evaluate):
        if len(populations) != 2 or any(not p for p in populations):
            raise ValueError("two nonempty role populations required")
        self.populations = [list(p) for p in populations]
        self.evaluate = evaluate

    def payoff_game(self):
        values = [[self.evaluate(a, b) for b in self.populations[1]] for a in self.populations[0]]
        return NormalFormGame(values)

    def meta_strategy(self, iterations=2000):
        if iterations < 1:
            raise ValueError("positive solver iterations required")
        game = self.payoff_game()
        low, high = game.payoffs.min(), game.payoffs.max()
        scale = max(high - low, 1e-12)
        learners = [ExternalRegretPolicy(k) for k in game.shape]
        joint = np.zeros(game.shape)
        for _ in range(iterations):
            ps = [p.probabilities() for p in learners]
            joint += np.outer(*ps)
            for i, learner in enumerate(learners):
                learner.update(np.clip((game.action_values(i, ps) - low) / scale, 0, 1))
        joint /= iterations
        mixtures = [joint.sum(axis=1), joint.sum(axis=0)]
        return {
            "mixtures": mixtures,
            "joint": joint,
            "payoffs": game.payoffs,
            "restricted_product_deviation": game.deviation_gains(mixtures),
        }

    def expand(self, oracle, iterations=2000):
        result = self.meta_strategy(iterations)
        candidates = [
            oracle(i, tuple(self.populations[1 - i]), result["mixtures"][1 - i].copy()) for i in range(2)
        ]
        for pop, candidate in zip(self.populations, candidates, strict=True):
            pop.append(candidate)
        return result


class AlphaRankEvaluator:
    """Multi-population finite-selection AlphaRank with Moran fixation probabilities.

    Exact dense Markov chain over joint profiles; capped for memory. Finite alpha
    ensures irreducibility mathematically; extreme numerical rates are rejected.
    """

    def __init__(self, alpha=1.0, population_size=50, max_profiles=2000):
        if not np.isfinite(alpha) or alpha < 0 or population_size < 2:
            raise ValueError("invalid selection parameters")
        self.alpha, self.m, self.max_profiles = alpha, population_size, max_profiles

    def evaluate(self, payoffs):
        game = NormalFormGame(payoffs)
        profiles = list(np.ndindex(game.shape))
        if len(profiles) > self.max_profiles:
            raise ValueError("dense ranking profile limit exceeded")
        index = {p: i for i, p in enumerate(profiles)}
        count = sum(k - 1 for k in game.shape)
        if count == 0:
            return {"profiles": profiles, "mass": np.ones(1), "transition": np.ones((1, 1))}
        matrix = np.zeros((len(profiles), len(profiles)))
        for row, profile in enumerate(profiles):
            for player, size in enumerate(game.shape):
                for action in range(size):
                    if action == profile[player]:
                        continue
                    mutant = list(profile)
                    mutant[player] = action
                    mutant = tuple(mutant)
                    delta = self.alpha * (game.payoffs[mutant][player] - game.payoffs[profile][player])
                    if abs(delta) * self.m > 500:
                        raise ValueError("selection too extreme for reliable dense stationary solve")
                    rho = 1 / self.m if abs(delta) < 1e-10 else np.expm1(-delta) / np.expm1(-self.m * delta)
                    matrix[row, index[mutant]] = rho / count
            matrix[row, row] = 1 - matrix[row].sum()
        system = matrix.T - np.eye(len(profiles))
        system[-1] = 1
        rhs = np.zeros(len(profiles))
        rhs[-1] = 1
        mass = np.linalg.solve(system, rhs)
        if (mass < -1e-8).any() or not np.allclose(mass @ matrix, mass, atol=1e-8):
            raise ValueError("stationary solve failed")
        mass = np.maximum(mass, 0)
        mass /= mass.sum()
        return {"profiles": profiles, "mass": mass, "transition": matrix}


class MultiTypeMeanField:
    """Role-conditioned tabular mean-field Q approximation with binned neighbor mix.

    Separate tables by role. This implements mean-field Q, not neural actor-critic.
    """

    def __init__(self, roles, actions, bins=10, rate=0.1, discount=0.95):
        if actions < 1 or bins < 1 or not all(0 <= x <= 1 for x in (rate, discount)):
            raise ValueError("invalid mean-field configuration")
        self.roles = tuple(roles)
        if not self.roles or len(set(self.roles)) != len(self.roles):
            raise ValueError("unique roles required")
        self.actions, self.bins, self.rate, self.discount = actions, bins, rate, discount
        self.q = {}

    def means(self, population):
        result = {}
        for role in self.roles:
            acts = [a for r, a in population if r == role]
            if any(not 0 <= a < self.actions for a in acts):
                raise ValueError("illegal population action")
            result[role] = (
                np.bincount(acts, minlength=self.actions) / len(acts) if acts else np.zeros(self.actions)
            )
        return result

    def values(self, role, state, means):
        if role not in self.roles or set(means) != set(self.roles):
            raise ValueError("unknown or missing role")
        vectors = [np.asarray(means[r], float) for r in self.roles]
        if any(
            v.shape != (self.actions,)
            or not np.isfinite(v).all()
            or (v < 0).any()
            or not (np.isclose(v.sum(), 0) or np.isclose(v.sum(), 1))
            for v in vectors
        ):
            raise ValueError("role means must be distributions or empty-population zero vectors")
        key = (role, state, tuple(np.rint(np.concatenate(vectors) * self.bins).astype(int)))
        return self.q.setdefault(key, np.zeros(self.actions))

    def update(self, role, state, means, action, reward, next_state, next_means, terminal=False):
        if not 0 <= action < self.actions or not np.isfinite(reward):
            raise ValueError("invalid feedback")
        q = self.values(role, state, means)
        target = reward + (0 if terminal else self.discount * self.values(role, next_state, next_means).max())
        q[action] += self.rate * (target - q[action])
