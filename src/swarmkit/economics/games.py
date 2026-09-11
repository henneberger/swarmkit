"""Finite and hypergraph games with explicit payoff conventions."""

from __future__ import annotations

from itertools import product

import numpy as np

from .ledger import amount


class NormalFormGame:
    """Payoffs have shape (actions_player_0, ..., actions_player_n, n)."""

    def __init__(self, payoffs):
        self.payoffs = np.asarray(payoffs, dtype=float).copy()
        self.n = self.payoffs.ndim - 1
        if self.n < 1 or self.payoffs.shape[-1] != self.n or not np.isfinite(self.payoffs).all():
            raise ValueError("invalid finite payoff tensor")
        self.shape = self.payoffs.shape[:-1]
        if min(self.shape) < 1:
            raise ValueError("players require actions")

    def utilities(self, actions):
        if len(actions) != self.n or any(
            not isinstance(a, (int, np.integer)) or not 0 <= a < k
            for a, k in zip(actions, self.shape, strict=True)
        ):
            raise ValueError("illegal joint action")
        return self.payoffs[tuple(actions)].copy()

    def expected(self, profile):
        if len(profile) != self.n:
            raise ValueError("one distribution per player required")
        ps = [np.asarray(p, float) for p in profile]
        for p, k in zip(ps, self.shape, strict=True):
            if p.shape != (k,) or not np.isfinite(p).all() or (p < 0).any() or not np.isclose(p.sum(), 1):
                raise ValueError("invalid mixed strategy")
        joint = ps[0]
        for p in ps[1:]:
            joint = np.multiply.outer(joint, p)
        return np.sum(self.payoffs * joint[..., None], axis=tuple(range(self.n)))

    def action_values(self, player, profile):
        self.expected(profile)
        result = []
        for action in range(self.shape[player]):
            replaced = list(profile)
            replaced[player] = np.eye(self.shape[player])[action]
            result.append(self.expected(replaced)[player])
        return np.array(result)

    def deviation_gains(self, profile):
        base = self.expected(profile)
        return np.array([max(0, self.action_values(i, profile).max() - base[i]) for i in range(self.n)])

    def pure_equilibria(self):
        return [
            a
            for a in product(*(range(k) for k in self.shape))
            if np.max(self.deviation_gains([np.eye(k)[x] for k, x in zip(self.shape, a, strict=True)]))
            < 1e-10
        ]


class RepeatedGame:
    """Two-player binary repeated game; policies receive only their noisy histories."""

    def __init__(self, game, discount=1.0, observation_noise=0.0, continuation=1.0):
        if game.shape != (2, 2) or not all(0 <= x <= 1 for x in (discount, observation_noise, continuation)):
            raise ValueError("requires binary two-player game and probabilities")
        self.game, self.discount, self.noise, self.continuation = (
            game,
            discount,
            observation_noise,
            continuation,
        )

    def run(self, policies, rounds=100, seed=0):
        if len(policies) != 2 or rounds < 1:
            raise ValueError("two policies and positive rounds required")
        rng = np.random.default_rng(seed)
        histories = [[], []]
        trajectory = []
        utility = np.zeros(2)
        for t in range(rounds):
            a = tuple(p(tuple(h), rng) for p, h in zip(policies, histories, strict=True))
            reward = self.game.utilities(a)
            utility += self.discount**t * reward
            trajectory.append(a)
            for i in range(2):
                observed = a[1 - i] ^ int(rng.random() < self.noise)
                histories[i].append((a[i], observed, float(reward[i])))
            if rng.random() >= self.continuation:
                break
        return {
            "utility": utility,
            "actions": trajectory,
            "cooperation": float(np.mean(np.array(trajectory) == 0)),
        }


class HypergraphPublicGoods:
    """Linear group returns. agent budget splits a contribution over incident edges;
    edge budget charges that contribution on every incident edge. No isolated cost.
    """

    def __init__(self, edges, multiplier=1.5, budget_mode="agent"):
        self.edges = tuple(tuple(e) for e in edges)
        if not self.edges or any(not e or len(set(e)) != len(e) for e in self.edges):
            raise ValueError("nonempty edges with unique members required")
        self.multiplier = amount(multiplier)
        if budget_mode not in ("agent", "edge"):
            raise ValueError("budget_mode must be agent or edge")
        self.budget_mode = budget_mode
        self.members = tuple(sorted({a for e in self.edges for a in e}))

    def utilities(self, contributions):
        if set(contributions) != set(self.members):
            raise ValueError("one contribution per member required")
        c = {a: amount(v) for a, v in contributions.items()}
        degree = {a: sum(a in e for e in self.edges) for a in self.members}
        payoff = dict.fromkeys(self.members, 0.0)
        for edge in self.edges:
            local = {a: c[a] / (degree[a] if self.budget_mode == "agent" else 1) for a in edge}
            benefit = self.multiplier * sum(local.values()) / len(edge)
            for a in edge:
                payoff[a] += benefit - local[a]
        return payoff


class ThresholdTeamGame:
    """Our complementary-capability adaptation; equal gross reward among joiners."""

    def __init__(self, capabilities, required, reward, costs):
        self.capabilities = {a: frozenset(v) for a, v in capabilities.items()}
        self.required, self.reward = frozenset(required), amount(reward)
        self.costs = {a: amount(v) for a, v in costs.items()}
        if set(self.capabilities) != set(self.costs):
            raise ValueError("costs required for all participants")

    def utilities(self, joined):
        joined = frozenset(joined)
        if not joined <= self.capabilities.keys():
            raise ValueError("unknown participant")
        covered = frozenset().union(*(self.capabilities[a] for a in joined))
        success = bool(joined) and self.required <= covered
        return {
            a: (self.reward / len(joined) if success else 0) - self.costs[a] if a in joined else 0.0
            for a in self.capabilities
        }


class CongestionGame:
    """Unweighted atomic congestion game; latency(resource load) must be pure."""

    def __init__(self, resources):
        self.resources = dict(resources)

    def loads(self, routes):
        if any(
            len(set(route)) != len(route) or not set(route) <= self.resources.keys()
            for route in routes.values()
        ):
            raise ValueError("route has duplicate or unknown resources")
        return {r: sum(r in route for route in routes.values()) for r in self.resources}

    def utilities(self, routes):
        loads = self.loads(routes)
        costs = {r: amount(f(loads[r])) for r, f in self.resources.items() if loads[r]}
        return {a: -sum(costs[r] for r in route) for a, route in routes.items()}

    def potential(self, routes):
        return sum(
            amount(self.resources[r](k)) for r, n in self.loads(routes).items() for k in range(1, n + 1)
        )


class StackelbergContractGame:
    """Exact finite leader commitment with explicit follower tie-breaking."""

    def __init__(self, leader_payoffs, follower_payoffs, tie_break="strong"):
        self.leader, self.follower = np.asarray(leader_payoffs, float), np.asarray(follower_payoffs, float)
        if self.leader.ndim != 2 or self.leader.shape != self.follower.shape or min(self.leader.shape) < 1:
            raise ValueError("matching nonempty payoff matrices required")
        if not np.isfinite(self.leader).all() or not np.isfinite(self.follower).all():
            raise ValueError("nonfinite payoffs")
        if tie_break not in ("strong", "weak"):
            raise ValueError("tie_break must be strong or weak")
        self.tie_break = tie_break

    def solve(self, outside_option=None):
        outcomes = []
        for i, row in enumerate(self.follower):
            if outside_option is not None and row.max() < outside_option:
                continue
            choices = np.flatnonzero(np.isclose(row, row.max(), rtol=0, atol=1e-12))
            scores = self.leader[i, choices]
            j = int(choices[np.argmax(scores) if self.tie_break == "strong" else np.argmin(scores)])
            outcomes.append((float(self.leader[i, j]), i, j))
        if not outcomes:
            return None
        _, i, j = max(outcomes, key=lambda x: (x[0], -x[1]))
        return {
            "leader_action": i,
            "follower_action": j,
            "leader_utility": float(self.leader[i, j]),
            "follower_utility": float(self.follower[i, j]),
        }
