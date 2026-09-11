"""Finite bargaining, coalition diagnostics and empirical equilibrium checks."""

from __future__ import annotations

from itertools import combinations, permutations
from math import factorial

import numpy as np


def coalitions(members):
    return (frozenset(c) for k in range(len(members) + 1) for c in combinations(members, k))


class NashBargaining:
    """Maximize weighted Nash product over a supplied finite feasible set."""

    def solve(self, utilities, disagreement, weights=None):
        u, d = np.asarray(utilities, float), np.asarray(disagreement, float)
        if u.ndim != 2 or d.shape != (u.shape[1],) or not np.isfinite(u).all() or not np.isfinite(d).all():
            raise ValueError("invalid feasible utilities/disagreement")
        w = np.ones(len(d)) if weights is None else np.asarray(weights, float)
        if w.shape != d.shape or not np.isfinite(w).all() or (w <= 0).any():
            raise ValueError("positive bargaining weights required")
        gain = u - d
        feasible = np.flatnonzero((gain >= 0).all(axis=1))
        if not len(feasible):
            return None
        scores = [float(np.dot(w, np.log(gain[i]))) if (gain[i] > 0).all() else -np.inf for i in feasible]
        i = int(feasible[np.argmax(scores)])
        return {"index": i, "utilities": u[i].copy(), "log_product": scores[list(feasible).index(i)]}


class AlternatingOffers:
    """Finite-horizon divisible-pie protocol; explicit callbacks and disagreement."""

    def __init__(self, total=1.0, discounts=(1.0, 1.0), disagreement=(0.0, 0.0)):
        self.total = float(total)
        self.discounts, self.disagreement = np.asarray(discounts, float), np.asarray(disagreement, float)
        if (
            not np.isfinite(self.total)
            or total < 0
            or self.discounts.shape != (2,)
            or not np.isfinite(self.discounts).all()
            or ((self.discounts < 0) | (self.discounts > 1)).any()
            or self.disagreement.shape != (2,)
            or not np.isfinite(self.disagreement).all()
        ):
            raise ValueError("invalid bargaining parameters")

    def run(self, propose, accept, rounds=10):
        if rounds < 1 or len(propose) != 2 or len(accept) != 2:
            raise ValueError("two parties and positive horizon required")
        history = []
        for t in range(rounds):
            p, r = t % 2, 1 - t % 2
            offer = np.asarray(propose[p](t, tuple(history)), float)
            if (
                offer.shape != (2,)
                or not np.isfinite(offer).all()
                or (offer < 0).any()
                or offer.sum() > self.total + 1e-10
            ):
                raise ValueError("infeasible offer")
            utility = offer * self.discounts**t
            accepted = bool(accept[r](offer.copy(), t, tuple(history)))
            history.append((p, tuple(offer), accepted))
            if accepted:
                if (utility < self.disagreement).any():
                    raise ValueError("accepted offer violates declared participation constraints")
                return {"agreement": True, "utility": utility, "history": history}
        return {"agreement": False, "utility": self.disagreement.copy(), "history": history}


class ShapleyEstimator:
    def __init__(self, members, value):
        self.members = tuple(members)
        if len(set(self.members)) != len(self.members) or len(self.members) > 20:
            raise ValueError("unique members required; at most 20 for this small-game implementation")
        self.value = value
        if not np.isclose(value(frozenset()), 0):
            raise ValueError("characteristic value must be normalized at empty coalition")

    def estimate(self, samples=1000, seed=0, exact=False):
        n = len(self.members)
        if samples < 1 or (exact and n > 9):
            raise ValueError("positive samples; exact permutation enumeration limited to 9 players")
        rng = np.random.default_rng(seed)
        orders = permutations(range(n)) if exact else (rng.permutation(n) for _ in range(samples))
        rows = []
        for order in orders:
            row, coalition, previous = np.zeros(n), frozenset(), 0.0
            for i in order:
                coalition = coalition | {self.members[i]}
                current = float(self.value(coalition))
                if not np.isfinite(current):
                    raise ValueError("nonfinite coalition value")
                row[i], previous = current - previous, current
            rows.append(row)
        data = np.asarray(rows).reshape((-1, n)) if n else np.empty((factorial(n) if exact else samples, 0))
        stderr = (
            np.zeros(n)
            if exact
            else (data.std(axis=0, ddof=1) / np.sqrt(samples) if samples > 1 else np.full(n, np.nan))
        )
        return {
            "values": dict(zip(self.members, data.mean(axis=0), strict=True)),
            "stderr": dict(zip(self.members, stderr, strict=True)),
            "samples": len(rows),
            "exact": exact,
        }


class CoreDiagnostic:
    def evaluate(self, members, value, allocation):
        members = tuple(members)
        if len(members) > 20 or len(set(members)) != len(members) or set(members) != set(allocation):
            raise ValueError("exact small coalition domain required")
        if not all(np.isfinite(x) for x in allocation.values()):
            raise ValueError("nonfinite allocation")
        gains = [(float(value(c)) - sum(allocation[a] for a in c), c) for c in coalitions(members)]
        if not all(np.isfinite(g) for g, _ in gains):
            raise ValueError("nonfinite coalition value")
        gain, coalition = max(gains, key=lambda x: x[0])
        gap = sum(allocation.values()) - value(frozenset(members))
        return {
            "max_blocking_gain": max(0.0, gain),
            "blocking_coalition": coalition,
            "efficiency_gap": gap,
            "in_core": abs(gap) < 1e-9 and gain < 1e-9,
        }


class RestrictedCoalitionValue:
    """Sum value over connected components of fully contained hyperedges.

    A documented hypergraph extension; pairwise edges recover graph restriction.
    """

    def __init__(self, value, edges):
        self.value, self.edges = value, tuple(frozenset(e) for e in edges)

    def __call__(self, coalition):
        remaining, components = set(coalition), []
        while remaining:
            component = {min(remaining)}
            while True:
                expanded = component | set().union(
                    *(e for e in self.edges if e <= set(coalition) and e & component)
                )
                if expanded == component:
                    break
                component = expanded
            remaining -= component
            components.append(frozenset(component))
        return sum(self.value(c) for c in components)


def equilibrium_violations(game, joint):
    """Exact CE pairwise and CCE fixed-action gains under a supplied joint distribution."""
    joint = np.asarray(joint, float)
    if (
        joint.shape != game.shape
        or not np.isfinite(joint).all()
        or (joint < 0).any()
        or not np.isclose(joint.sum(), 1)
    ):
        raise ValueError("invalid joint distribution")
    ce, cce = [], []
    for i, count in enumerate(game.shape):
        swaps = np.zeros((count, count))
        for a in np.ndindex(game.shape):
            for b in range(count):
                changed = list(a)
                changed[i] = b
                swaps[a[i], b] += joint[a] * (game.payoffs[tuple(changed)][i] - game.payoffs[a][i])
        ce.append(max(0.0, float(swaps.max())))
        cce.append(max(0.0, float(swaps.sum(axis=0).max())))
    return {"ce_violation": ce, "cce_violation": cce}
