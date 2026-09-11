"""Scripted reciprocity, online regret and tabular group-history learning."""

from __future__ import annotations

import numpy as np


def fixed(action):
    return lambda history, rng: action


def tit_for_tat(history, rng):
    return history[-1][1] if history else 0


def generous_reciprocity(forgiveness=0.1):
    if not 0 <= forgiveness <= 1:
        raise ValueError("forgiveness must be a probability")
    return lambda history, rng: 0 if not history or rng.random() < forgiveness else history[-1][1]


def win_stay_lose_shift(aspiration=2.0):
    return lambda history, rng: (
        0 if not history else (history[-1][0] if history[-1][2] >= aspiration else 1 - history[-1][0])
    )


class FictitiousPlay:
    def __init__(self, game, player, prior=1.0):
        if prior <= 0 or not 0 <= player < game.n:
            raise ValueError("positive prior and legal player required")
        self.game, self.player = game, player
        self.counts = [np.full(k, prior) for k in game.shape]

    def probabilities(self):
        values = self.game.action_values(self.player, [c / c.sum() for c in self.counts])
        best = np.isclose(values, values.max())
        return best / best.sum()

    def update(self, actions):
        self.game.utilities(actions)
        for c, action in zip(self.counts, actions, strict=True):
            c[action] += 1


class ExternalRegretPolicy:
    """Full-information Hedge or external regret matching, feedback in [0,1]."""

    def __init__(self, actions, method="hedge", rate=0.1):
        if actions < 1 or method not in ("hedge", "regret_matching") or not np.isfinite(rate) or rate <= 0:
            raise ValueError("invalid learner configuration")
        self.actions, self.method, self.rate = actions, method, rate
        self.cumulative = np.zeros(actions)
        self.realized = 0.0
        self.rounds = 0

    def probabilities(self):
        if self.method == "hedge":
            weights = np.exp(self.rate * (self.cumulative - self.cumulative.max()))
        else:
            weights = np.maximum(self.cumulative - self.realized, 0)
        return weights / weights.sum() if weights.sum() else np.full(self.actions, 1 / self.actions)

    def update(self, utilities, action=None):
        u = np.asarray(utilities, float)
        if u.shape != (self.actions,) or not np.isfinite(u).all() or ((u < 0) | (u > 1)).any():
            raise ValueError("one bounded counterfactual utility per action required")
        if action is not None and (
            not isinstance(action, (int, np.integer)) or not 0 <= action < self.actions
        ):
            raise ValueError("illegal selected action")
        self.realized += float(self.probabilities() @ u if action is None else u[action])
        self.cumulative += u
        self.rounds += 1

    @property
    def regret(self):
        return max(0.0, float(self.cumulative.max() - self.realized))


class InternalRegretPolicy:
    """Hart–Mas-Colell pairwise regret transition, bounded [0,1] full feedback.

    From last action i, switch to j with R_ij^+/(t*mu), retaining remaining
    probability on i. mu=number of actions bounds all outgoing probabilities.
    """

    def __init__(self, actions):
        if actions < 1:
            raise ValueError("positive action count required")
        self.actions, self.last, self.rounds = actions, None, 0
        self.regrets = np.zeros((actions, actions))

    def probabilities(self):
        if self.last is None:
            return np.full(self.actions, 1 / self.actions)
        p = np.maximum(self.regrets[self.last], 0) / (self.rounds * self.actions)
        p[self.last] = 1 - p.sum()
        return p

    def update(self, action, utilities):
        u = np.asarray(utilities, float)
        if (
            u.shape != (self.actions,)
            or not np.isfinite(u).all()
            or ((u < 0) | (u > 1)).any()
            or not isinstance(action, (int, np.integer))
            or not 0 <= action < self.actions
        ):
            raise ValueError("legal action and bounded full feedback required")
        self.regrets[action] += u - u[action]
        self.last, self.rounds = action, self.rounds + 1

    @property
    def swap_regret(self):
        return float(np.maximum(self.regrets.max(axis=1), 0).sum())


class GroupHistoryQPolicy:
    """Tabular own-action/group-histogram state, own utility (not altruistic reward)."""

    def __init__(self, actions=2, rate=0.1, discount=0.95, epsilon=0.1):
        if actions < 1 or not all(0 <= x <= 1 for x in (rate, discount, epsilon)):
            raise ValueError("invalid Q configuration")
        self.actions, self.rate, self.discount, self.epsilon = actions, rate, discount, epsilon
        self.q = {}

    def state(self, own_previous, other_actions):
        other_actions = tuple(other_actions)
        if not 0 <= own_previous < self.actions or any(not 0 <= a < self.actions for a in other_actions):
            raise ValueError("illegal previous action")
        return (own_previous, tuple(np.bincount(other_actions, minlength=self.actions)))

    def values(self, state):
        return self.q.setdefault(state, np.zeros(self.actions))

    def act(self, state, rng):
        return int(
            rng.integers(self.actions) if rng.random() < self.epsilon else np.argmax(self.values(state))
        )

    def update(self, state, action, reward, next_state, terminal=False):
        if not np.isfinite(reward) or not 0 <= action < self.actions:
            raise ValueError("invalid action/reward")
        target = reward + (0 if terminal else self.discount * self.values(next_state).max())
        self.values(state)[action] += self.rate * (target - self.values(state)[action])
