"""Swarm measurements and paired controls, expressed with shared contracts.

Metrics deliberately separate agreement, evidence access and held-out utility.
Controls are motivated by https://arxiv.org/abs/2508.17536v2 and
https://arxiv.org/abs/2512.08296v3; they are evaluation utilities, not replications.
"""

from __future__ import annotations

import math
import random
from collections import Counter
from collections.abc import Callable, Iterable, Mapping, Sequence
from copy import deepcopy
from dataclasses import dataclass
from typing import TypeVar

from .types import AgentState, Decision, Evidence, Message, SwarmState, Task


def population_diversity(labels: Iterable[str], normalized: bool = True) -> float:
    """Shannon entropy of observed categories; normalized by observed richness.

    Empty or uniform populations score zero. This is diversity, not correctness;
    normalization uses observed categories, so report richness separately when
    comparing populations with different possible label vocabularies.
    """
    counts = Counter(labels)
    size = sum(counts.values())
    if len(counts) < 2:
        return 0.0
    entropy = -sum((n / size) * math.log(n / size) for n in counts.values())
    return entropy / math.log(len(counts)) if normalized else entropy


def interaction_reciprocity(messages: Iterable[Message], population: Iterable[str] = ()) -> float:
    """Fraction of unique directed edges whose reverse edge exists.

    Empty-recipient broadcasts expand only against an explicitly supplied
    population; without one, they do not invent unknown recipients. Repeated
    messages and self-edges never increase reciprocity.
    """
    members = tuple(population)
    edges = {
        (m.sender, recipient)
        for m in messages
        for recipient in (m.recipients or members)
        if recipient != m.sender
    }
    return sum((b, a) in edges for a, b in edges) / len(edges) if edges else 0.0


def private_evidence_recovery(
    required: Iterable[str | Evidence], observed: Iterable[str | Evidence | Message]
) -> float:
    """Fraction of unique required evidence IDs surfaced (empty target is 1).

    Repetition does not improve coverage. This measures exposure, not whether a
    recipient understands or correctly uses the evidence.
    """
    target = {x.id if isinstance(x, Evidence) else x for x in required}
    found = set()
    for item in observed:
        if isinstance(item, Message):
            found.update(card.id for card in item.evidence)
        else:
            found.add(item.id if isinstance(item, Evidence) else item)
    return len(target & found) / len(target) if target else 1.0


def ancestry_adjusted_agreement(
    decisions: Sequence[Decision], evidence: Mapping[str, Evidence], answer: str | None = None
) -> float:
    """Agreement after assigning unit mass to each distinct evidential root.

    A root's vote is split equally over grounded decisions citing descendants of
    it. Decisions lacking evidence contribute no mass. Roots with the same source
    string are collapsed (conservative source independence convention). Unknown
    evidence or cyclic ancestry raises ValueError rather than fabricating support.
    This is a defined ancestry-aware diagnostic, not a published formula.
    """
    cache: dict[str, frozenset[str]] = {}

    def roots(card_id: str, path: frozenset[str]) -> frozenset[str]:
        if card_id in path:
            raise ValueError("cyclic evidence ancestry")
        if card_id in cache:
            return cache[card_id]
        if card_id not in evidence:
            raise ValueError(f"unknown evidence: {card_id}")
        card = evidence[card_id]
        result = (
            frozenset().union(*(roots(p, path | {card_id}) for p in card.parents))
            if card.parents
            else frozenset({card.source})
        )
        cache[card_id] = result
        return result

    root_answers: dict[str, list[str]] = {}
    for decision in decisions:
        origins = frozenset().union(*(roots(i, frozenset()) for i in decision.evidence_ids))
        for origin in origins:
            root_answers.setdefault(origin, []).append(decision.answer)
    if not root_answers:
        return 0.0
    masses: Counter[str] = Counter()
    for answers in root_answers.values():
        for label in answers:
            masses[label] += 1 / len(answers)
    numerator = masses[answer] if answer is not None else max(masses.values())
    return numerator / len(root_answers)


def hyperedge_irreducibility(hyperedges: Iterable[Iterable[str]]) -> float | None:
    """Exact Eq.3 diagnostic from arXiv:2608.15519v1, not an intelligence score.

    Compute global hyperdegree over all events (including dyads/singletons), then
    average 1 - sum_{i<j}|d_i-d_j| / (choose(k,2)*mean_degree*2) over k>=3.
    Repeated events count separately; repeated membership within one event does
    not. No qualifying event returns None, matching the paper's undefined case.
    Equal global degree yields 1 even for semantically unproductive exchanges.
    """
    events = [frozenset(edge) for edge in hyperedges]
    degree = Counter(node for edge in events for node in edge)
    scores = []
    for edge in events:
        if len(edge) < 3:
            continue
        values = [degree[node] for node in sorted(edge)]
        k = len(values)
        difference = sum(abs(values[i] - values[j]) for i in range(k) for j in range(i + 1, k))
        denominator = (k * (k - 1) / 2) * (sum(values) / k) * 2
        scores.append(1 - difference / denominator)
    return sum(scores) / len(scores) if scores else None


T = TypeVar("T")


def transfer_gain(cases: Iterable[T], before: Callable[[T], float], after: Callable[[T], float]) -> float:
    """Mean paired utility gain on caller-provided held-out cases.

    Each evaluator receives its own deep copy. Callers are responsible for
    holding discoveries fixed and preventing training/test contamination.
    """
    gains = []
    for case in cases:
        baseline, treatment = float(before(deepcopy(case))), float(after(deepcopy(case)))
        if not math.isfinite(baseline) or not math.isfinite(treatment):
            raise ValueError("transfer scores must be finite")
        gains.append(treatment - baseline)
    if not gains:
        raise ValueError("at least one held-out case is required")
    return sum(gains) / len(gains)


@dataclass(frozen=True)
class MatchedComparison:
    swarm_score: float
    independent_score: float
    gain: float
    total_budget: int
    independent_budgets: Mapping[str, int]
    swarm_decisions: tuple[Decision, ...]
    independent_decisions: tuple[Decision, ...]


def matched_independent_control(
    state: SwarmState,
    task: Task,
    total_budget: int,
    swarm_runner: Callable[[SwarmState, Task, int], Sequence[Decision]],
    independent_runner: Callable[[AgentState, Task, int, random.Random], Decision],
    score: Callable[[Sequence[Decision], Task], float],
) -> MatchedComparison:
    """Compare an interacting run with isolated runners on identical initial inputs.

    Allocate the same TOTAL declared budget across independent agents, preserving
    their initial private evidence and inboxes; no shared mutable state is passed
    to isolated callbacks. Task inputs and state are copied. This wrapper cannot
    meter opaque callback internals: callers must enforce the declared budget
    unit (tokens, calls, or steps), identical tools, and external data access.
    """
    agents = state.active_ids
    if not isinstance(total_budget, int) or total_budget < len(agents) or not agents:
        raise ValueError("budget must be an integer with at least one unit per active agent")
    initial = deepcopy(state)
    # Snapshot baseline before invoking external callbacks.
    independent_agents = [deepcopy(initial.agents[i]) for i in agents]
    swarm_decisions = tuple(swarm_runner(deepcopy(initial), deepcopy(task), total_budget))
    base, remainder = divmod(total_budget, len(agents))
    budgets = {agent: base + (i < remainder) for i, agent in enumerate(agents)}
    independent = []
    for index, agent in enumerate(independent_agents):
        decision = independent_runner(
            agent, deepcopy(task), budgets[agent.id], random.Random(state.seed + index)
        )
        if decision.agent_id != agent.id:
            raise ValueError("independent callback returned a different agent ID")
        independent.append(decision)
    if any(d.agent_id not in agents for d in swarm_decisions):
        raise ValueError("swarm callback returned an inactive or unknown agent")
    a = float(score(swarm_decisions, deepcopy(task)))
    b = float(score(tuple(independent), deepcopy(task)))
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("comparison scores must be finite")
    return MatchedComparison(a, b, a - b, total_budget, budgets, swarm_decisions, tuple(independent))
