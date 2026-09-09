"""Executable swarm communication policies; all learned state lives in SwarmState.data.

These are mechanism-level adaptations, not reproductions of benchmark pipelines.
"""

from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass
from typing import Mapping, Sequence

import numpy as np

from .types import Decision, Feedback, SwarmState, TopologyPolicy, probability


def _peers(state: SwarmState, sender: str) -> tuple[str, ...]:
    if sender not in state.agents or not state.agents[sender].active:
        return ()
    return tuple(x for x in state.active_ids if x != sender)


@dataclass(frozen=True)
class FullTopology:
    def neighbors(self, state: SwarmState, sender: str) -> tuple[str, ...]:
        return _peers(state, sender)


@dataclass(frozen=True)
class RingTopology:
    bidirectional: bool = True

    def neighbors(self, state: SwarmState, sender: str) -> tuple[str, ...]:
        if not _peers(state, sender):
            return ()
        ids = state.active_ids
        i = ids.index(sender)
        offsets = (1, -1) if self.bidirectional else (1,)
        return tuple(dict.fromkeys(ids[(i + d) % len(ids)] for d in offsets))


@dataclass(frozen=True)
class StarTopology:
    center: str

    def neighbors(self, state: SwarmState, sender: str) -> tuple[str, ...]:
        peers = _peers(state, sender)
        return peers if sender == self.center else ((self.center,) if self.center in peers else ())


@dataclass(frozen=True)
class RandomTopology:
    """Independent directed edges sampled once per simulation step."""

    edge_probability: float = 0.5
    key: str = "random_topology"

    def __post_init__(self) -> None:
        probability(self.edge_probability)

    def neighbors(self, state: SwarmState, sender: str) -> tuple[str, ...]:
        if sender not in state.active_ids:
            return ()
        signature = (state.step, state.active_ids, self.edge_probability)
        record = state.data.get(self.key)
        if record is None or record["signature"] != signature:
            graph = {
                a: tuple(b for b in state.active_ids if a != b and state.rng.random() < self.edge_probability)
                for a in state.active_ids
            }
            record = state.data[self.key] = {"signature": signature, "graph": graph}
        return record["graph"][sender]


@dataclass(frozen=True)
class LocalRadiusTopology:
    radius: float

    def __post_init__(self) -> None:
        if not math.isfinite(self.radius) or self.radius < 0:
            raise ValueError("radius must be finite and nonnegative")

    def neighbors(self, state: SwarmState, sender: str) -> tuple[str, ...]:
        peers = _peers(state, sender)
        if sender not in state.agents or state.agents[sender].position is None:
            return ()
        origin = state.agents[sender].position
        found = []
        for target in peers:
            position = state.agents[target].position
            if position is None:
                continue
            if len(position) != len(origin):
                raise ValueError("positions must share a dimension")
            if not all(math.isfinite(v) for v in (*origin, *position)):
                raise ValueError("positions must be finite")
            if math.dist(origin, position) <= self.radius:
                found.append(target)
        return tuple(found)


@dataclass(frozen=True)
class HypergraphTopology:
    """Broadcast within incident hyperedges; union removes duplicate recipients."""

    groups: tuple[frozenset[str], ...]

    def neighbors(self, state: SwarmState, sender: str) -> tuple[str, ...]:
        targets = set().union(*(g for g in self.groups if sender in g)) if self.groups else set()
        return tuple(x for x in _peers(state, sender) if x in targets)


@dataclass(frozen=True)
class BernoulliDAGPolicy:
    """GPTSwarm-inspired REINFORCE on fixed-order DAG edges.

    https://arxiv.org/abs/2402.16823 ; sparsity inspired by
    https://arxiv.org/abs/2410.02506 . Fixed topological order is an
    explicit restriction. Optional nuclear-norm gradient is a surrogate,
    not AgentPrune's complete constrained optimization algorithm.
    """

    learning_rate: float = 0.1
    initial_probability: float = 0.5
    baseline_decay: float = 0.9
    edge_penalty: float = 0.0
    nuclear_penalty: float = 0.0
    key: str = "bernoulli_dag"

    def __post_init__(self) -> None:
        if not 0 < self.initial_probability < 1:
            raise ValueError("initial_probability must be strictly between zero and one")
        probability(self.baseline_decay)
        for value in (self.learning_rate, self.edge_penalty, self.nuclear_penalty):
            if not math.isfinite(value) or value < 0:
                raise ValueError("learning rate and penalties must be finite and nonnegative")

    def _record(self, state: SwarmState) -> dict:
        ids = tuple(state.agents)
        rec = state.data.get(self.key)
        if rec is None:
            rec = state.data[self.key] = {
                "ids": ids,
                "logits": {},
                "pruned": set(),
                "baseline": 0.0,
                "sample": None,
            }
        if rec["ids"] != ids:
            raise ValueError("DAG population changed; use a fresh policy state key")
        initial = math.log(self.initial_probability / (1 - self.initial_probability))
        for i, a in enumerate(ids):
            for b in ids[i + 1 :]:
                rec["logits"].setdefault((a, b), initial)
        return rec

    def probabilities(self, state: SwarmState) -> dict[tuple[str, str], float]:
        rec = self._record(state)
        return {
            edge: (0.0 if edge in rec["pruned"] else 1 / (1 + math.exp(-value)))
            for edge, value in rec["logits"].items()
        }

    def sample(self, state: SwarmState) -> tuple[tuple[str, str], ...]:
        rec = self._record(state)
        signature = (state.step, state.active_ids)
        old = rec["sample"]
        if old is not None and old["signature"] == signature:
            return old["edges"]
        probs = {
            e: p
            for e, p in self.probabilities(state).items()
            if e not in rec["pruned"] and all(a in state.active_ids for a in e)
        }
        outcomes = {e: int(state.rng.random() < p) for e, p in probs.items()}
        edges = tuple(e for e, on in outcomes.items() if on)
        rec["sample"] = {
            "signature": signature,
            "probabilities": probs,
            "outcomes": outcomes,
            "edges": edges,
            "updated": False,
        }
        return edges

    def neighbors(self, state: SwarmState, sender: str) -> tuple[str, ...]:
        if sender not in state.active_ids:
            return ()
        return tuple(b for a, b in self.sample(state) if a == sender)

    def update(self, state: SwarmState, feedback: Feedback) -> Mapping[str, float]:
        """Apply once to the last sampled graph, using its sampling probabilities."""
        if not math.isfinite(feedback.utility) or not math.isfinite(feedback.costs):
            raise ValueError("feedback must be finite")
        rec = self._record(state)
        sample = rec["sample"]
        if sample is None or sample["updated"]:
            raise ValueError("sample a new graph before updating")
        reward = feedback.utility - feedback.costs - self.edge_penalty * len(sample["edges"])
        if not math.isfinite(reward):
            raise ValueError("effective reward must be finite")
        advantage = reward - rec["baseline"]
        if not math.isfinite(advantage):
            raise ValueError("advantage must be finite")
        ids = rec["ids"]
        matrix = np.zeros((len(ids), len(ids)))
        index = {a: i for i, a in enumerate(ids)}
        for (a, b), p in sample["probabilities"].items():
            matrix[index[a], index[b]] = p
        nuclear = 0.0
        grad = np.zeros_like(matrix)
        if self.nuclear_penalty and len(ids):
            u, singular, vt = np.linalg.svd(matrix, full_matrices=False)
            nuclear = float(singular.sum())
            grad = (u * (singular > 1e-12)) @ vt
        for edge, p in sample["probabilities"].items():
            a, b = edge
            delta = advantage * (sample["outcomes"][edge] - p)
            delta -= self.nuclear_penalty * grad[index[a], index[b]] * p * (1 - p)
            rec["logits"][edge] = float(np.clip(rec["logits"][edge] + self.learning_rate * delta, -20, 20))
        rec["baseline"] = self.baseline_decay * rec["baseline"] + (1 - self.baseline_decay) * reward
        sample["updated"] = True
        return {"reward": reward, "advantage": advantage, "nuclear_norm": nuclear}

    def prune(self, state: SwarmState, fraction: float) -> tuple[tuple[str, str], ...]:
        """Permanently prune the lowest-probability fraction of surviving edges."""
        probability(fraction, "fraction")
        rec = self._record(state)
        sample = rec["sample"]
        if sample is not None and not sample["updated"]:
            raise ValueError("update sampled graph before pruning")
        candidates = [(p, e) for e, p in self.probabilities(state).items() if e not in rec["pruned"]]
        removed = tuple(e for _, e in sorted(candidates)[: math.floor(len(candidates) * fraction)])
        rec["pruned"].update(removed)
        rec["sample"] = None
        return removed


@dataclass(frozen=True)
class RoundDropoutTopology:
    """AgentDropout-inspired round-specific node/edge masks, arbitrary population size.

    https://arxiv.org/abs/2503.18891 . Importance is supplied by the caller;
    fitting that importance and temporal-edge policies remains caller-controlled.
    """

    base: TopologyPolicy
    key: str = "round_dropout"

    def configure(
        self,
        state: SwarmState,
        round_index: int,
        importance: Mapping[str, float],
        drop_fraction: float = 0.2,
        edge_scores: Mapping[tuple[str, str], float] | None = None,
        edge_drop_fraction: float = 0.0,
    ) -> tuple[str, ...]:
        probability(drop_fraction)
        probability(edge_drop_fraction)
        if round_index < 0 or any(not math.isfinite(v) for v in importance.values()):
            raise ValueError("round and importance must be valid")
        ids = state.active_ids
        ranked = sorted(ids, key=lambda a: (-importance.get(a, 0.0), a))
        keep = set(ranked[: len(ids) - math.floor(len(ids) * drop_fraction)])
        excluded: set[tuple[str, str]] = set()
        if edge_scores:
            if any(not math.isfinite(v) for v in edge_scores.values()):
                raise ValueError("edge scores must be finite")
            candidates = sorted(
                (score, edge) for edge, score in edge_scores.items() if all(a in keep for a in edge)
            )
            excluded.update(e for _, e in candidates[: math.floor(len(candidates) * edge_drop_fraction)])
        state.data.setdefault(self.key, {})[round_index] = {"keep": keep, "excluded": excluded}
        return tuple(a for a in ids if a in keep)

    def neighbors(self, state: SwarmState, sender: str) -> tuple[str, ...]:
        rec = state.data.get(self.key, {}).get(state.step)
        if rec is None:
            return tuple(self.base.neighbors(state, sender))
        if sender not in rec["keep"]:
            return ()
        return tuple(
            a
            for a in self.base.neighbors(state, sender)
            if a in rec["keep"] and (sender, a) not in rec["excluded"]
        )


@dataclass(frozen=True)
class DyLANSelection:
    """Ranker-score selection, backward attribution, and strict >2/3 agreement.

    https://arxiv.org/abs/2310.02170 . Agreement is a heuristic, not proof.
    """

    keep: int = 2
    consensus_threshold: float = 2 / 3
    key: str = "dylan_selection"

    def __post_init__(self) -> None:
        if self.keep < 1:
            raise ValueError("keep must be positive")
        probability(self.consensus_threshold)

    def select(self, state: SwarmState, scores: Mapping[str, float]) -> tuple[str, ...]:
        if any(not math.isfinite(v) for v in scores.values()):
            raise ValueError("scores must be finite")
        selected = tuple(sorted(state.active_ids, key=lambda a: (-scores.get(a, 0.0), a))[: self.keep])
        state.data[self.key] = {"selected": selected, "scores": dict(scores)}
        return selected

    def consensus(self, decisions: Sequence[Decision], participants: Sequence[str]) -> str | None:
        ids = set(participants)
        answers: dict[str, str] = {}
        for d in decisions:
            if d.agent_id not in ids or d.agent_id in answers:
                raise ValueError("one decision per participating agent required")
            answers[d.agent_id] = d.answer
        if not ids or not answers:
            return None
        answer, count = Counter(answers.values()).most_common(1)[0]
        return answer if count / len(ids) > self.consensus_threshold else None

    @staticmethod
    def backward_importance(
        final_scores: Mapping[str, float], layers: Sequence[Mapping[tuple[str, str], float]]
    ) -> dict[str, float]:
        """Each layer maps (predecessor, successor) to a nonnegative peer rating."""
        current = dict(final_scores)
        if any(not math.isfinite(v) or v < 0 for v in current.values()):
            raise ValueError("importance must be finite and nonnegative")
        total = dict(current)
        for layer in reversed(layers):
            previous: dict[str, float] = {}
            for (a, b), weight in layer.items():
                if not math.isfinite(weight) or weight < 0:
                    raise ValueError("peer weights must be finite and nonnegative")
                previous[a] = previous.get(a, 0.0) + weight * current.get(b, 0.0)
            for a, value in previous.items():
                total[a] = total.get(a, 0.0) + value
            current = previous
        return total


@dataclass(frozen=True)
class CapabilitySuccessRouter:
    """AgentNet-inspired local capability/success routing with exploration.

    https://arxiv.org/abs/2504.00587 . Set overlap replaces learned embeddings;
    empirical success EMA replaces an LLM router. Caller supplies task capabilities.
    """

    exploration: float = 0.1
    success_weight: float = 0.5
    decay: float = 0.9
    key: str = "capability_router"

    def __post_init__(self) -> None:
        for v in (self.exploration, self.success_weight, self.decay):
            probability(v)

    def route(
        self, state: SwarmState, sender: str, required: frozenset[str], visited: Sequence[str] = ()
    ) -> str | None:
        peers = tuple(a for a in _peers(state, sender) if a not in visited)
        if not peers:
            return None
        history = state.data.setdefault(self.key, {})
        if state.rng.random() < self.exploration:
            return state.rng.choice(peers)

        def score(a: str) -> float:
            match = len(required & state.agents[a].capabilities) / len(required) if required else 1.0
            success = history.get((sender, a), 0.5)
            return (1 - self.success_weight) * match + self.success_weight * success

        return max(peers, key=score)

    def record(self, state: SwarmState, sender: str, recipient: str, success: float) -> None:
        probability(success, "success")
        if sender == recipient or sender not in state.agents or recipient not in state.agents:
            raise ValueError("routing feedback requires distinct known agents")
        history = state.data.setdefault(self.key, {})
        old = history.get((sender, recipient), 0.5)
        history[(sender, recipient)] = self.decay * old + (1 - self.decay) * success

    def neighbors(self, state: SwarmState, sender: str) -> tuple[str, ...]:
        required = frozenset(state.data.get(self.key + ":required", ()))
        target = self.route(state, sender, required)
        return (target,) if target is not None else ()
