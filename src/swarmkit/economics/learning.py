"""Executable small numerical research adaptations and explicit training callbacks.

Finite differences are for low-dimensional controlled experiments, not efficient
transformer training. No pretrained models or paper-scale reproductions implied.
"""

from __future__ import annotations

import copy

import numpy as np


def gradient(function, parameters, epsilon=1e-4):
    x = np.asarray(parameters, float)
    if not np.isfinite(x).all() or epsilon <= 0:
        raise ValueError("finite parameters and positive difference step required")
    result = np.zeros_like(x)
    for index in np.ndindex(x.shape):
        plus, minus = x.copy(), x.copy()
        plus[index] += epsilon
        minus[index] -= epsilon
        result[index] = (function(plus) - function(minus)) / (2 * epsilon)
    if not np.isfinite(result).all():
        raise ValueError("nonfinite objective gradient")
    return result


class LOLAAdapter:
    """First-order LOLA objective: V1 + eta2 * grad_2(V1) dot grad_2(V2).

    Hold grad_2(V1) fixed in the correction, as in the original backward pass. Requires pure
    differentiable expected-value callbacks; numerical derivatives, no rollout
    gradient estimator. Update player 2 by invoking with reversed arguments.
    """

    def __init__(self, rate=0.1, opponent_rate=0.1):
        if not all(np.isfinite(x) and x > 0 for x in (rate, opponent_rate)):
            raise ValueError("positive finite learning rates required")
        self.rate, self.opponent_rate = rate, opponent_rate

    def step(self, own, opponent, own_value, opponent_value):
        own, opponent = np.asarray(own, float), np.asarray(opponent, float)

        influence = gradient(lambda y: own_value(own, y), opponent)

        def shaped(x):
            learning = gradient(lambda y: opponent_value(x, y), opponent)
            return own_value(x, opponent) + self.opponent_rate * float(np.sum(influence * learning))

        return own + self.rate * gradient(shaped, own)


class POLAAdapter:
    """Finite-step numerical nested proximal opponent-aware update.

    KL(old || new) callbacks act on policy distributions, not parameter distance.
    Recomputes inner proximal response for outer perturbations. Approximate POLA;
    finite steps/finite differences do not provide ideal invariance guarantees.
    """

    def __init__(self, rate=0.05, penalty=1.0, inner_steps=10, outer_steps=5):
        if (
            not np.isfinite(rate)
            or rate <= 0
            or not np.isfinite(penalty)
            or penalty <= 0
            or inner_steps < 1
            or outer_steps < 1
        ):
            raise ValueError("invalid proximal configuration")
        self.rate, self.penalty, self.inner_steps, self.outer_steps = rate, penalty, inner_steps, outer_steps

    def step(self, own, opponent, own_value, opponent_value, own_kl, opponent_kl):
        own, opponent = np.asarray(own, float), np.asarray(opponent, float)

        def response(x):
            y = opponent.copy()
            for _ in range(self.inner_steps):
                y += self.rate * gradient(
                    lambda z: opponent_value(x, z) - self.penalty * opponent_kl(opponent, z), y
                )
            return y

        def objective(x):
            return own_value(x, response(x)) - self.penalty * own_kl(own, x)

        result = own.copy()
        for _ in range(self.outer_steps):
            result += self.rate * gradient(objective, result)
        return result


class LearnedAuction:
    """Small differentiable single-item mechanism with feasible fractional allocation.

    Softmax includes an unsold option. Payment = reported value * allocation *
    sigmoid. Truthful-report ex-post IR for nonnegative values, but not DSIC.
    Train revenue minus sampled unilateral regret penalty by finite differences.
    """

    def __init__(self, bidders, seed=0):
        if bidders < 1:
            raise ValueError("positive bidder count required")
        self.n = bidders
        self.parameters = np.random.default_rng(seed).normal(0, 0.1, (bidders + 1, bidders + 1))
        self.payment_logits = np.zeros(bidders)

    def _forward(self, bids, theta):
        bids = np.asarray(bids, float)
        if bids.shape != (self.n,) or not np.isfinite(bids).all() or (bids < 0).any():
            raise ValueError("nonnegative finite bid vector required")
        weights = theta[: (self.n + 1) ** 2].reshape(self.n + 1, self.n + 1)
        logits = weights @ np.append(bids, 1)
        p = np.exp(logits - logits.max())
        allocation = (p / p.sum())[: self.n]
        fraction = 1 / (1 + np.exp(-np.clip(theta[(self.n + 1) ** 2 :], -40, 40)))
        return allocation, allocation * bids * fraction

    def _theta(self):
        return np.concatenate((self.parameters.ravel(), self.payment_logits))

    def clear(self, bids):
        allocation, payments = self._forward(bids, self._theta())
        return {"allocation": allocation, "payments": payments}

    def _metrics(self, values, deviations, theta):
        revenues, regrets = [], []
        for value in values:
            x, p = self._forward(value, theta)
            truthful = np.asarray(value) * x - p
            gain = np.zeros(self.n)
            for i in range(self.n):
                for report in deviations:
                    bids = np.array(value, float)
                    bids[i] = report
                    dx, dp = self._forward(bids, theta)
                    gain[i] = max(gain[i], value[i] * dx[i] - dp[i] - truthful[i])
            revenues.append(p.sum())
            regrets.append(gain)
        return {
            "revenue": float(np.mean(revenues)),
            "mean_regret": float(np.mean(regrets)),
            "max_tested_regret": float(np.max(regrets)),
        }

    def evaluate(self, values, deviations):
        if len(values) == 0 or len(deviations) == 0:
            raise ValueError("nonempty values and explicit deviation grid required")
        return self._metrics(values, deviations, self._theta())

    def fit(self, values, deviations, steps=20, rate=0.01, penalty=10.0):
        self.evaluate(values, deviations)
        if steps < 1 or not all(np.isfinite(x) and x > 0 for x in (rate, penalty)):
            raise ValueError("invalid training configuration")
        theta = self._theta()

        def objective(t):
            m = self._metrics(values, deviations, t)
            return m["revenue"] - penalty * m["mean_regret"]

        history = []
        for _ in range(steps):
            theta += rate * gradient(objective, theta)
            history.append(self._metrics(values, deviations, theta))
        split = (self.n + 1) ** 2
        self.parameters, self.payment_logits = theta[:split].reshape(self.n + 1, self.n + 1), theta[split:]
        return history


class TwoLevelInstitution:
    """Alternating planner/worker training, with injected actual learning backends.

    adapt_workers(rule, workers, seed) returns updated workers;
    evaluate(rule, workers, seed) returns finite planner utility;
    update_planner(rule, workers, score, seed) proposes the next rule.
    """

    def __init__(self, rule, workers, adapt_workers, evaluate, update_planner):
        self.rule, self.workers = copy.deepcopy(rule), copy.deepcopy(workers)
        self.adapt_workers, self.evaluate, self.update_planner = adapt_workers, evaluate, update_planner
        self.history = []

    def fit(self, rounds=10, seed=0):
        if rounds < 1:
            raise ValueError("positive training horizon required")
        for t in range(rounds):
            workers = self.adapt_workers(copy.deepcopy(self.rule), copy.deepcopy(self.workers), seed + t)
            score = float(self.evaluate(copy.deepcopy(self.rule), copy.deepcopy(workers), seed + t))
            if not np.isfinite(score):
                raise ValueError("nonfinite planner score")
            next_rule = self.update_planner(copy.deepcopy(self.rule), copy.deepcopy(workers), score, seed + t)
            self.history.append({"rule": copy.deepcopy(self.rule), "score": score, "seed": seed + t})
            self.workers, self.rule = workers, next_rule
        return copy.deepcopy(self.history)

    def held_out(self, workers, seeds):
        return [self.evaluate(copy.deepcopy(self.rule), copy.deepcopy(workers), seed) for seed in seeds]


class NegotiationSelfPlay:
    """Structured negotiation rollout/training coordinator; caller owns language model.

    rollout(p1,p2,seed) must return {valid, utilities, transcript}. Invalid outcomes
    abort the update. update(policy, role, episodes) performs actual policy training.
    Hold-out partners are evaluated without applying updates.
    """

    def __init__(self, policies, rollout, update):
        if len(policies) != 2:
            raise ValueError("two negotiating roles required")
        self.policies, self.rollout, self.update = list(policies), rollout, update

    def _episode(self, policies, seed):
        episode = self.rollout(*copy.deepcopy(policies), seed)
        u = np.asarray(episode["utilities"], float)
        if episode.get("valid") is not True or u.shape != (2,) or not np.isfinite(u).all():
            raise ValueError("rollout must have independently validated structured outcome")
        return episode

    def fit(self, rounds=10, episodes_per_round=4, seed=0):
        if rounds < 1 or episodes_per_round < 1:
            raise ValueError("positive training sizes required")
        history = []
        for t in range(rounds):
            episodes = [
                self._episode(self.policies, seed + t * episodes_per_round + k)
                for k in range(episodes_per_round)
            ]
            updated = [
                self.update(copy.deepcopy(p), i, copy.deepcopy(episodes)) for i, p in enumerate(self.policies)
            ]
            self.policies = updated
            history.extend(episodes)
        return history

    def cross_play(self, partners, seeds):
        return [
            {
                "role": i,
                "partner": j,
                "seed": seed,
                "episode": self._episode([policy, partner] if i == 0 else [partner, policy], seed),
            }
            for i, policy in enumerate(self.policies)
            for j, partner in enumerate(partners)
            for seed in seeds
        ]


class FramingAndDisclosurePolicy:
    """Search fact-preserving subsets/orderings and explicit framing labels.

    Facts remain immutable Evidence records. Evaluator receives the framing label
    separately; scores report sender benefit and recipient accuracy independently.
    """

    def select(self, evidence, candidates, evaluate, objective="sender_utility"):
        cards = {e.id: e for e in evidence}
        if len(cards) != len(evidence):
            raise ValueError("duplicate fact ids")
        results = []
        for ids, frame in candidates:
            if len(set(ids)) != len(ids) or not set(ids) <= cards.keys():
                raise ValueError("framing candidate must reference unique original facts")
            selected = tuple(copy.deepcopy(cards[i]) for i in ids)
            metrics = evaluate(selected, frame)
            if not np.isfinite(metrics[objective]):
                raise ValueError("nonfinite framing score")
            results.append({"evidence": selected, "frame": frame, "metrics": metrics})
        if not results:
            raise ValueError("candidate set empty")
        return max(results, key=lambda r: r["metrics"][objective])
