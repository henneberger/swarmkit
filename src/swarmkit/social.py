"""Local social mechanisms for interacting populations; no provider calls.

Naming/copying adapt https://arxiv.org/abs/2410.08948v2 and
https://arxiv.org/abs/2609.09150v1. Feed/trust policies are explicit engineering
choices, not claimed reproductions of Moltbook ranking formulas.
Relay adapts the deterministic evidence-exchange experimental design in
Darwin-Agent/topological-collapse-agent-societies/llm_relay_benchmark.
Algorithms own local state only: callers record/route returned messages and
advance ``state.step``. Relay delivery is additionally maintained internally so
its synchronous evidence propagation is independent of inbox routing.
"""

from __future__ import annotations

import math
import random
from collections import Counter
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field

from .types import AgentState, AlgorithmResult, Decision, Evidence, Message, SwarmState, Task, probability

Choice = Callable[[AgentState, Task, random.Random], str]
Neighbors = Callable[[SwarmState, str], Sequence[str]]


def _message(
    state: SwarmState,
    sender: str,
    content: str,
    recipients: tuple[str, ...],
    evidence: tuple[Evidence, ...] = (),
) -> Message:
    # Use the population RNG rather than UUIDs for reproducible trajectories.
    return Message(
        sender,
        content,
        recipients,
        evidence=evidence,
        step=state.step,
        id=f"social-{state.rng.getrandbits(128):032x}",
    )


@dataclass
class NamingGame:
    """Random pair, local history, matching payoff; fixed committed minorities.

    Default choice copies a random remembered partner label (uniform initially).
    This is a runnable classical null, NOT the paper's LLM reasoning policy.
    Supply ``choose`` to implement a language-model or other decision policy.
    ``committed`` maps agent IDs to labels; memory contains (own, peer, payoff).
    """

    memory_size: int = 5
    committed: Mapping[str, str] = field(default_factory=dict)
    choose: Choice | None = None
    namespace: str = "naming_game"

    def __post_init__(self) -> None:
        if not isinstance(self.memory_size, int) or self.memory_size < 0:
            raise ValueError("memory_size must be a nonnegative integer")

    def step(self, state: SwarmState, task: Task) -> AlgorithmResult:
        if not task.candidates or len(set(task.candidates)) != len(task.candidates):
            raise ValueError("naming game requires distinct candidate labels")
        if any(label not in task.candidates for label in self.committed.values()):
            raise ValueError("committed labels must be candidates")
        if len(state.active_ids) < 2:
            return AlgorithmResult(metrics={"interactions": 0.0})
        pair = state.rng.sample(list(state.active_ids), 2)
        labels = []
        for agent_id in pair:
            agent = state.agents[agent_id]
            history = agent.memory.get(self.namespace, [])
            if agent_id in self.committed:
                label = self.committed[agent_id]
            elif self.choose is not None:
                label = self.choose(agent, task, state.rng)
            else:
                label = state.rng.choice([entry[1] for entry in history] or list(task.candidates))
            if label not in task.candidates:
                raise ValueError("choice callback returned an invalid label")
            labels.append(label)
        payoff = 1.0 if labels[0] == labels[1] else -1.0
        decisions, messages = [], []
        for index, agent_id in enumerate(pair):
            agent = state.agents[agent_id]
            history = list(agent.memory.get(self.namespace, []))
            history.append((labels[index], labels[1 - index], payoff))
            agent.memory[self.namespace] = history[-self.memory_size :] if self.memory_size else []
            agent.beliefs = {label: float(label == labels[index]) for label in task.candidates}
            agent.score += payoff
            decisions.append(Decision(agent_id, labels[index]))
            messages.append(_message(state, agent_id, labels[index], (pair[1 - index],)))
        return AlgorithmResult(
            tuple(messages), tuple(decisions), metrics={"interactions": 1.0, "matched": float(payoff > 0)}
        )


@dataclass
class ProportionalCopying:
    """Copy visible option frequencies with probability 1-innovation.

    Visibility is supplied explicitly; absent a callback, each agent sees its
    inbox contents. Empty views fall back to uniform innovation. The synchronous
    update never exposes decisions from the current round to later agents.
    """

    innovation: float = 0.07
    visible: Callable[[SwarmState, str], Sequence[str]] | None = None

    def __post_init__(self) -> None:
        probability(self.innovation, "innovation")

    def step(self, state: SwarmState, task: Task) -> AlgorithmResult:
        if not task.candidates or len(set(task.candidates)) != len(task.candidates):
            raise ValueError("copying requires distinct candidate labels")
        views = {
            i: list(self.visible(state, i) if self.visible else (m.content for m in state.agents[i].inbox))
            for i in state.active_ids
        }
        decisions, messages = [], []
        for agent_id, view in views.items():
            options = [x for x in view if x in task.candidates]
            use_copy = bool(options) and state.rng.random() >= self.innovation
            label = state.rng.choice(options if use_copy else list(task.candidates))
            decisions.append(Decision(agent_id, label, metadata={"copied": use_copy}))
            messages.append(_message(state, agent_id, label, ()))
        for decision in decisions:
            state.agents[decision.agent_id].beliefs = {
                label: float(label == decision.answer) for label in task.candidates
            }
        return AlgorithmResult(tuple(messages), tuple(decisions))


@dataclass
class FeedPolicy:
    """Transparent ranking design: position, age, endorsement, reputation/diversity.

    ``social_proof`` metadata is a nonnegative count, ``topic`` a category.
    A greedy topic-repeat penalty diversifies the resulting list. Weights are
    configurable design parameters, not an inferred platform algorithm.
    """

    position_weight: float = 1.0
    recency_weight: float = 1.0
    proof_weight: float = 0.25
    reputation_weight: float = 0.5
    diversity_penalty: float = 0.5
    half_life: float = 10.0

    def __post_init__(self) -> None:
        for name in (
            "position_weight",
            "recency_weight",
            "proof_weight",
            "reputation_weight",
            "diversity_penalty",
        ):
            value = getattr(self, name)
            if not math.isfinite(value) or value < 0:
                raise ValueError(f"{name} must be finite and nonnegative")
        if not math.isfinite(self.half_life) or self.half_life <= 0:
            raise ValueError("half_life must be positive and finite")

    def rank(
        self,
        messages: Sequence[Message],
        now: int,
        limit: int | None = None,
        reputation: Callable[[str], float] | None = None,
    ) -> tuple[Message, ...]:
        if limit is not None and (not isinstance(limit, int) or limit < 0):
            raise ValueError("limit must be a nonnegative integer")
        if len({m.id for m in messages}) != len(messages):
            raise ValueError("feed message IDs must be unique")
        candidates = []
        for index, message in enumerate(messages):
            proof = float(message.metadata.get("social_proof", 0))
            if not math.isfinite(proof) or proof < 0:
                raise ValueError("social proof must be finite and nonnegative")
            rep = probability(float(reputation(message.sender))) if reputation else 0.0
            age = max(0, now - message.step)
            score = (
                self.position_weight / (index + 1)
                + self.recency_weight * 2 ** (-age / self.half_life)
                + self.proof_weight * math.log1p(proof)
                + self.reputation_weight * rep
            )
            candidates.append((message, score, index))
        counts: Counter[str] = Counter()
        selected = []
        while candidates and (limit is None or len(selected) < limit):

            def key(item: tuple[Message, float, int]) -> tuple[float, int]:
                topic = str(item[0].metadata.get("topic", item[0].id))
                return item[1] - self.diversity_penalty * counts[topic], -item[2]

            best = max(candidates, key=key)
            candidates.remove(best)
            message = best[0]
            selected.append(message)
            counts[str(message.metadata.get("topic", message.id))] += 1
        return tuple(selected)


@dataclass
class TrustNetwork:
    """Directional contextual trust with Bayesian observations and bounded paths.

    This is an ORIGINAL design. Direct reliability uses a Beta prior; indirect
    trust takes the maximum discounted product along a simple path. Parallel
    paths are not summed, preventing trust inflation from copied endorsements.
    Admission also requires an explicit verifier and evidence confidence.
    """

    prior_success: float = 1.0
    prior_failure: float = 1.0
    edges: dict[tuple[str, str, str], tuple[float, float]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if any(not math.isfinite(x) or x <= 0 for x in (self.prior_success, self.prior_failure)):
            raise ValueError("Beta prior values must be positive and finite")
        for values in self.edges.values():
            if len(values) != 2 or any(not math.isfinite(x) or x < 0 for x in values):
                raise ValueError("trust observations must be finite and nonnegative")

    def observe(self, observer: str, subject: str, topic: str, success: bool, weight: float = 1.0) -> None:
        if not math.isfinite(weight) or weight < 0:
            raise ValueError("weight must be finite and nonnegative")
        key = observer, subject, topic
        good, bad = self.edges.get(key, (0.0, 0.0))
        self.edges[key] = good + weight * bool(success), bad + weight * (not success)

    def direct(self, observer: str, subject: str, topic: str) -> float:
        good, bad = self.edges.get((observer, subject, topic), (0.0, 0.0))
        return (good + self.prior_success) / (good + bad + self.prior_success + self.prior_failure)

    def trust(self, observer: str, subject: str, topic: str, max_hops: int = 2, decay: float = 0.9) -> float:
        if not isinstance(max_hops, int) or max_hops < 0:
            raise ValueError("max_hops must be a nonnegative integer")
        probability(decay, "decay")
        if observer == subject:
            return 1.0
        best = 0.0
        stack = [(observer, frozenset({observer}), 1.0, 0)]
        while stack:
            node, visited, value, depth = stack.pop()
            if depth >= max_hops:
                continue
            for source, target, edge_topic in self.edges:
                if source != node or edge_topic != topic or target in visited:
                    continue
                propagated = value * self.direct(source, target, topic) * (decay if depth else 1.0)
                if target == subject:
                    best = max(best, propagated)
                elif propagated > best:
                    stack.append((target, visited | {target}, propagated, depth + 1))
        return best

    def admit(
        self,
        observer: str,
        evidence: Evidence,
        topic: str,
        verify: Callable[[Evidence], bool],
        threshold: float = 0.5,
        max_hops: int = 2,
        decay: float = 0.9,
    ) -> bool:
        probability(threshold, "threshold")
        trust = self.trust(observer, evidence.owner, topic, max_hops, decay)
        return trust * evidence.confidence >= threshold and bool(verify(evidence))


@dataclass
class GossipRelay:
    """Synchronous evidence relay with bounded fanout, bandwidth and lifetime.

    ``cards_per_round=None`` sends all known cards losslessly. Otherwise select
    unsent cards first, repeating oldest known cards after exhaustion. Selection
    is deterministic; fanout sampling uses state.rng. No prose is interpreted.
    Lifetime is measured from evidence's first appearance in this relay state,
    never refreshed by copying. ``ttl=0`` prevents any relay transmission.
    """

    neighbors: Neighbors
    fanout: int | None = None
    cards_per_round: int | None = 1
    ttl: int | None = None
    namespace: str = "gossip_relay"
    admit: Callable[[str, Evidence], bool] | None = None

    def __post_init__(self) -> None:
        for name in ("fanout", "cards_per_round", "ttl"):
            value = getattr(self, name)
            if value is not None and (not isinstance(value, int) or value < 0):
                raise ValueError(f"{name} must be a nonnegative integer or None")

    def step(self, state: SwarmState, task: Task) -> AlgorithmResult:
        data = state.data.setdefault(self.namespace, {"known": {}, "sent": {}, "birth": {}})
        known, sent, birth = data["known"], data["sent"], data["birth"]
        registry = data.setdefault("registry", {})
        active = state.active_ids
        for agent_id in active:
            inventory = known.setdefault(agent_id, {})
            sent.setdefault(agent_id, set())
            evidence = list(state.agents[agent_id].private_evidence)
            for message in state.agents[agent_id].inbox:
                evidence.extend(message.evidence)
            for card in evidence:
                if card.id in registry and registry[card.id] != card:
                    raise ValueError(f"conflicting evidence ID: {card.id}")
                registry[card.id] = card
                birth.setdefault(card.id, state.step)
                if self.admit is None or self.admit(agent_id, card):
                    inventory.setdefault(card.id, card)
            if self.ttl is not None:
                for card_id in list(inventory):
                    if state.step - birth[card_id] >= self.ttl:
                        del inventory[card_id]
        snapshot = {agent: dict(known[agent]) for agent in active}
        messages = []
        deliveries = []
        for agent in active:
            recipients = sorted({i for i in self.neighbors(state, agent) if i in active and i != agent})
            if self.fanout is not None and len(recipients) > self.fanout:
                recipients = sorted(state.rng.sample(recipients, self.fanout))
            if not recipients:
                continue
            cards = list(snapshot[agent])
            cards.sort(key=lambda i: (i in sent[agent], birth[i], i))
            if self.cards_per_round is not None:
                cards = cards[: self.cards_per_round]
            if not cards:
                continue
            selected = tuple(snapshot[agent][i] for i in cards)
            messages.append(_message(state, agent, "Evidence relay", tuple(recipients), selected))
            sent[agent].update(cards)
            for recipient in recipients:
                deliveries.extend((recipient, card) for card in selected)
        admitted = 0
        for recipient, card in deliveries:
            if card.id not in known[recipient] and (self.admit is None or self.admit(recipient, card)):
                known[recipient][card.id] = card
                admitted += 1
        total = sum(len(known[i]) for i in active)
        return AlgorithmResult(
            tuple(messages),
            metrics={
                "new_deliveries": float(admitted),
                "evidence_copies": float(total),
                "messages": float(len(messages)),
            },
            metadata={"knowledge": {i: tuple(known[i].values()) for i in active}},
        )
