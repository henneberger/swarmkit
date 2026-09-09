"""Evidence-first deliberation and independent-vote controls.

Adaptations of HiddenBench https://arxiv.org/abs/2505.11556 and the
vote/debate control https://arxiv.org/abs/2508.17536. Default scoring is a
transparent symbolic rule, not an LLM or reproduction of paper benchmarks.
Messages are returned un-routed; methods never increment ``state.step``.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Mapping, Sequence
from copy import deepcopy
from dataclasses import dataclass

from .knowledge import EvidenceRegistry
from .types import (
    AgentState,
    AlgorithmResult,
    Decision,
    Evidence,
    Message,
    MessageKind,
    SwarmState,
    Task,
    probability,
)

DecisionRule = Callable[[AgentState, Task, tuple[Evidence, ...]], Decision]


def _validate(decision: Decision, agent_id: str, task: Task) -> Decision:
    if decision.agent_id != agent_id:
        raise ValueError("decision agent id does not match participant")
    if decision.answer not in task.candidates:
        raise ValueError("decision answer must be a task candidate")
    return decision


def evidence_decision(agent: AgentState, task: Task, evidence: tuple[Evidence, ...]) -> Decision:
    """Deterministic source-deduplicated evidence rule, with zero-confidence ties."""
    if not task.candidates:
        raise ValueError("deliberation requires task candidates")
    registry = EvidenceRegistry(evidence)
    scores = registry.scores(task.candidates)
    ranked = sorted(task.candidates, key=lambda c: (-scores[c], task.candidates.index(c)))
    best = ranked[0]
    margin = scores[best] - scores[ranked[1]] if len(ranked) > 1 else max(scores[best], 0)
    confidence = min(1.0, max(0.0, margin) / max(1.0, sum(abs(v) for v in scores.values())))
    return Decision(
        agent.id,
        best,
        confidence,
        tuple(e.id for e in evidence),
        rationale=f"Provenance-weighted evidence scores: {scores}",
        metadata={"source_scores": scores},
    )


class IndependentVoting:
    """Each voter sees only its private evidence, before any peer responses.

    The callback receives a copied agent with inbox, beliefs and memory cleared:
    independence means isolation from this deliberation, not statistically
    independent training data or independent evidence sources.
    """

    def __init__(self, decide: DecisionRule = evidence_decision) -> None:
        self.decide = decide

    def step(self, state: SwarmState, task: Task) -> AlgorithmResult:
        if not task.candidates:
            raise ValueError("voting requires candidates")
        decisions = []
        for agent_id in state.active_ids:
            agent = deepcopy(state.agents[agent_id])
            agent.inbox, agent.memory, agent.beliefs = [], {}, {}
            decisions.append(_validate(self.decide(agent, task, agent.private_evidence), agent_id, task))
        return AlgorithmResult(
            decisions=tuple(decisions),
            metrics={"voters": float(len(decisions))},
            metadata={"phase": "independent"},
        )


class WeightedConsensus:
    """Weighted ballots with quorum, margin and stable-round stopping.

    Agent weights count ballots, not independent evidence. Confidence weighting
    is optional and must not be interpreted as calibration. Use EvidenceRegistry
    to assess shared provenance separately. Repeated calls can track stability;
    one ballot per agent per call is enforced.
    """

    def __init__(
        self,
        weights: Mapping[str, float] | None = None,
        *,
        threshold: float = 2 / 3,
        margin: float = 0.0,
        stable_rounds: int = 1,
        confidence_weighted: bool = False,
        minimum_voters: int = 1,
    ) -> None:
        probability(threshold, "threshold")
        probability(margin, "margin")
        if stable_rounds < 1 or minimum_voters < 1:
            raise ValueError("rounds and minimum_voters must be positive")
        self.weights = dict(weights or {})
        if any(not math.isfinite(w) or w < 0 for w in self.weights.values()):
            raise ValueError("weights must be finite and nonnegative")
        self.threshold, self.margin = threshold, margin
        self.stable_rounds, self.confidence_weighted = stable_rounds, confidence_weighted
        self.minimum_voters = minimum_voters
        self._history: dict[str, tuple[str | None, int]] = {}

    def aggregate(self, decisions: Sequence[Decision], task: Task) -> AlgorithmResult:
        if not task.candidates:
            raise ValueError("consensus requires candidates")
        if len({d.agent_id for d in decisions}) != len(decisions):
            raise ValueError("duplicate voter")
        totals = {candidate: 0.0 for candidate in task.candidates}
        eligible = 0
        for decision in decisions:
            _validate(decision, decision.agent_id, task)
            weight = self.weights.get(decision.agent_id, 1.0)
            if self.confidence_weighted:
                weight *= decision.confidence
            eligible += int(weight > 0)
            totals[decision.answer] += weight
        total = sum(totals.values())
        ranking = sorted(totals, key=lambda key: (-totals[key], task.candidates.index(key)))
        winner = ranking[0]
        lead = totals[winner]
        second = totals[ranking[1]] if len(ranking) > 1 else 0.0
        share = lead / total if total else 0.0
        gap = (lead - second) / total if total else 0.0
        passed = (
            eligible >= self.minimum_voters
            and total > 0
            and lead > second
            and share >= self.threshold
            and gap >= self.margin
        )
        previous, count = self._history.get(task.id, (None, 0))
        count = count + 1 if passed and previous == winner else int(passed)
        self._history[task.id] = (winner if passed else None, count)
        return AlgorithmResult(
            decisions=tuple(decisions),
            metrics={"share": share, "margin": gap, "total_weight": total, "stable_rounds": float(count)},
            metadata={
                "winner": winner if total else None,
                "totals": totals,
                "converged": passed and count >= self.stable_rounds,
            },
        )

    def step(self, state: SwarmState, task: Task) -> AlgorithmResult:
        """Aggregate fresh isolated ballots; use aggregate() for supplied decisions."""
        ballots = IndependentVoting().step(state, task)
        return self.aggregate(ballots.decisions, task)

    def reset(self, task_id: str) -> None:
        self._history.pop(task_id, None)


@dataclass(frozen=True)
class ExchangeConfig:
    exchange_rounds: int = 2
    facts_per_round: int = 2
    delivery: str = "all_peer"

    def __post_init__(self) -> None:
        if self.exchange_rounds < 1 or self.facts_per_round < 1:
            raise ValueError("exchange rounds and facts per round must be positive")
        if self.delivery not in ("all_peer", "inbox"):
            raise ValueError("delivery must be 'all_peer' or 'inbox'")


class ExchangeThenDecide:
    """Exchange decision-relevant facts and objections before permitting a vote.

    Each step is one phase: configured exchange rounds followed by one decision
    pass. In all_peer mode, peers receive the same completed round next step. Ancestry
    is included with disclosures, without counting copies as independent facts.
    This is a symbolic adaptation of HiddenBench §6.4, not forced Reveal-All.
    Default all_peer uses a public board regardless of output routing. Set
    delivery="inbox" to use only actually delivered evidence and local retained
    observations, respecting sparse topology and message filters. Inbox mode
    forwards received facts within the same disclosure budget; missing ancestry
    stays pending until delivered, never fetched from other agents.
    State is scoped by task id and optional ``namespace``; reset explicitly to
    start another episode with the same task. The active roster is fixed per run.
    """

    def __init__(
        self,
        config: ExchangeConfig | None = None,
        decide: DecisionRule = evidence_decision,
        *,
        namespace: str = "exchange",
    ) -> None:
        self.config = config or ExchangeConfig()
        self.decide, self.namespace = decide, namespace

    def reset(self, state: SwarmState, task_id: str) -> None:
        state.data.pop(f"{self.namespace}:{task_id}", None)

    def step(self, state: SwarmState, task: Task) -> AlgorithmResult:
        if not task.candidates:
            raise ValueError("exchange requires candidates")
        key = f"{self.namespace}:{task.id}"
        if self.config.delivery == "inbox":
            return self._inbox_step(state, task, key)
        if key not in state.data:
            registry = EvidenceRegistry(e for a in state.agents.values() for e in a.private_evidence)
            state.data[key] = {
                "round": 0,
                "roster": state.active_ids,
                "shared": (),
                "disclosed": set(),
                "registry": registry.evidence,
                "done": False,
            }
        run = state.data[key]
        if run.get("delivery", "all_peer") != "all_peer":
            raise ValueError("delivery mode changed during deliberation; reset episode")
        if run["roster"] != state.active_ids:
            raise ValueError("active roster changed during deliberation; reset episode")
        if run["done"]:
            return AlgorithmResult(metadata={"phase": "complete", "done": True})
        archive = EvidenceRegistry(run["registry"])
        if run["round"] >= self.config.exchange_rounds:
            shared = EvidenceRegistry(run["shared"])
            decisions = []
            for agent_id in state.active_ids:
                agent = deepcopy(state.agents[agent_id])
                local = EvidenceRegistry(shared.evidence)
                self._include_with_ancestry(local, agent.private_evidence, archive)
                decisions.append(_validate(self.decide(agent, task, local.evidence), agent_id, task))
            messages = tuple(
                Message(
                    d.agent_id,
                    d.rationale,
                    kind=MessageKind.DECISION,
                    step=state.step,
                    metadata={"answer": d.answer, "confidence": d.confidence},
                )
                for d in decisions
            )
            run["done"] = True
            return AlgorithmResult(
                messages,
                tuple(decisions),
                metrics={"shared_sources": float(len(shared.independent_sources()))},
                metadata={"phase": "decide", "done": True},
            )
        shared = EvidenceRegistry(run["shared"])
        public_scores = shared.scores(task.candidates)
        front = max(task.candidates, key=lambda candidate: public_scores[candidate])
        messages = []
        newly_shared = EvidenceRegistry(shared.evidence)
        for agent_id in state.active_ids:
            agent = state.agents[agent_id]
            candidates = [
                e
                for e in agent.private_evidence
                if e.id not in run["disclosed"]
                and (set(e.supports) | set(e.contradicts)) & set(task.candidates)
            ]
            selected = candidates[: self.config.facts_per_round]
            disclosure = EvidenceRegistry()
            self._include_with_ancestry(disclosure, selected, archive)
            self._include_with_ancestry(newly_shared, selected, archive)
            run["disclosed"].update(e.id for e in selected)
            messages.append(
                Message(
                    agent_id,
                    "; ".join(e.claim for e in selected) or "No new fact to disclose.",
                    kind=MessageKind.OBSERVATION,
                    evidence=disclosure.evidence,
                    step=state.step,
                )
            )
            objections = [
                e
                for e in agent.private_evidence
                if front in e.contradicts or any(c != front for c in e.supports)
            ]
            objection = (
                f"{front} may be wrong: {objections[0].claim}"
                if objections
                else f"{front} may be wrong because other peers may hold undisclosed evidence; "
                "request disconfirming observations before deciding."
            )
            messages.append(
                Message(
                    agent_id,
                    objection,
                    kind=MessageKind.CRITIQUE,
                    step=state.step,
                    metadata={"front_runner": front},
                )
            )
        run["shared"] = newly_shared.evidence
        run["round"] += 1
        return AlgorithmResult(
            messages=tuple(messages),
            metrics={
                "exchange_round": float(run["round"]),
                "shared_sources": float(len(newly_shared.independent_sources())),
            },
            metadata={"phase": "exchange", "done": False},
        )

    def _inbox_step(self, state: SwarmState, task: Task, key: str) -> AlgorithmResult:
        run = state.data.setdefault(
            key,
            {
                "round": 0,
                "roster": state.active_ids,
                "delivery": "inbox",
                "done": False,
                "local": {},
                "pending": {},
                "sent": {},
            },
        )
        if run.get("delivery") != "inbox":
            raise ValueError("delivery mode changed during deliberation; reset episode")
        if run["roster"] != state.active_ids:
            raise ValueError("active roster changed during deliberation; reset episode")
        if run["done"]:
            return AlgorithmResult(metadata={"phase": "complete", "done": True, "delivery": "inbox"})
        # Snapshot and resolve every local inventory before producing any output.
        # Unknown ancestry remains pending locally; no population-wide lookup exists.
        for agent_id in state.active_ids:
            agent = state.agents[agent_id]
            local = EvidenceRegistry(run["local"].get(agent_id, ()))
            pending = run["pending"].setdefault(agent_id, {})
            run["sent"].setdefault(agent_id, set())
            available = list(agent.private_evidence)
            available.extend(e for message in agent.inbox for e in message.evidence)
            known = {e.id: e for e in local.evidence}
            for evidence in available:
                previous = known.get(evidence.id, pending.get(evidence.id))
                if previous is not None and previous != evidence:
                    raise ValueError("conflicting local evidence id")
                if evidence.id not in known:
                    pending[evidence.id] = deepcopy(evidence)
            while True:
                ready = [e for e in pending.values() if all(p in known for p in e.parents)]
                if not ready:
                    break
                for evidence in ready:
                    local.add(evidence)
                    known[evidence.id] = evidence
                    del pending[evidence.id]
            run["local"][agent_id] = local.evidence
        local_sources = {
            agent: len(EvidenceRegistry(evidence).independent_sources())
            for agent, evidence in run["local"].items()
        }
        metrics = {
            "mean_local_sources": sum(local_sources.values()) / max(1, len(local_sources)),
            "pending_evidence": float(sum(len(items) for items in run["pending"].values())),
        }
        if run["round"] >= self.config.exchange_rounds:
            decisions = tuple(
                _validate(
                    self.decide(deepcopy(state.agents[agent_id]), task, run["local"][agent_id]),
                    agent_id,
                    task,
                )
                for agent_id in state.active_ids
            )
            messages = tuple(
                Message(
                    d.agent_id,
                    d.rationale,
                    kind=MessageKind.DECISION,
                    step=state.step,
                    metadata={"answer": d.answer, "confidence": d.confidence},
                )
                for d in decisions
            )
            run["done"] = True
            return AlgorithmResult(
                messages=messages,
                decisions=decisions,
                metrics=metrics,
                metadata={
                    "phase": "decide",
                    "done": True,
                    "delivery": "inbox",
                    "local_sources": local_sources,
                },
            )
        messages = []
        for agent_id in state.active_ids:
            local = EvidenceRegistry(run["local"][agent_id])
            scores = local.scores(task.candidates)
            front = max(task.candidates, key=lambda candidate: scores[candidate])
            relevant = [
                e for e in local.evidence if (set(e.supports) | set(e.contradicts)) & set(task.candidates)
            ]
            selected = [e for e in relevant if e.id not in run["sent"][agent_id]][
                : self.config.facts_per_round
            ]
            disclosure = EvidenceRegistry()
            self._include_with_ancestry(disclosure, selected, local)
            run["sent"][agent_id].update(e.id for e in selected)
            messages.append(
                Message(
                    agent_id,
                    "; ".join(e.claim for e in selected) or "No new fact to disclose.",
                    kind=MessageKind.OBSERVATION,
                    evidence=disclosure.evidence,
                    step=state.step,
                )
            )
            objections = [
                e for e in relevant if front in e.contradicts or any(c != front for c in e.supports)
            ]
            objection = (
                f"{front} may be wrong: {objections[0].claim}"
                if objections
                else f"{front} may be wrong: request disconfirming observations from reachable peers."
            )
            messages.append(
                Message(
                    agent_id,
                    objection,
                    kind=MessageKind.CRITIQUE,
                    step=state.step,
                    metadata={"front_runner": front},
                )
            )
        run["round"] += 1
        return AlgorithmResult(
            messages=tuple(messages),
            metrics={**metrics, "exchange_round": float(run["round"])},
            metadata={
                "phase": "exchange",
                "done": False,
                "delivery": "inbox",
                "local_sources": local_sources,
            },
        )

    @staticmethod
    def _include_with_ancestry(
        target: EvidenceRegistry, evidence: Sequence[Evidence], archive: EvidenceRegistry
    ) -> None:
        def include(item: Evidence) -> None:
            for parent in item.parents:
                include(archive.get(parent))
            target.add(item)

        for item in evidence:
            include(item)


class CritiqueReviseDebate:
    """Synchronous independent proposals, peer critique, then callback revisions.

    critique(agent, previous_decisions, task) -> str;
    revise(agent, own_decision, critiques, task) -> Decision.
    All critics see the same preceding snapshot, all revisers see the completed
    critique round. Early stopping uses WeightedConsensus; reaching the round cap
    sets ``done`` without implying convergence or truth.
    """

    def __init__(
        self,
        critique: Callable[[AgentState, tuple[Decision, ...], Task], str],
        revise: Callable[[AgentState, Decision, tuple[Message, ...], Task], Decision],
        *,
        decide: DecisionRule = evidence_decision,
        max_rounds: int = 3,
        consensus: WeightedConsensus | None = None,
        namespace: str = "debate",
    ) -> None:
        if max_rounds < 1:
            raise ValueError("max_rounds must be positive")
        self.critique, self.revise, self.decide = critique, revise, decide
        self.max_rounds, self.consensus = max_rounds, consensus or WeightedConsensus()
        self.namespace = namespace

    def reset(self, state: SwarmState, task_id: str) -> None:
        state.data.pop(f"{self.namespace}:{task_id}", None)
        self.consensus.reset(task_id)

    def step(self, state: SwarmState, task: Task) -> AlgorithmResult:
        key = f"{self.namespace}:{task.id}"
        if key not in state.data:
            output = IndependentVoting(self.decide).step(state, task)
            state.data[key] = {
                "decisions": output.decisions,
                "round": 0,
                "roster": state.active_ids,
                "done": False,
            }
            return AlgorithmResult(
                decisions=output.decisions, metadata={"phase": "independent", "done": False}
            )
        run = state.data[key]
        if run["roster"] != state.active_ids:
            raise ValueError("active roster changed during debate")
        if run["done"]:
            return AlgorithmResult(metadata={"phase": "complete", "done": True})
        previous = run["decisions"]
        critiques = tuple(
            Message(
                agent_id,
                self.critique(deepcopy(state.agents[agent_id]), deepcopy(previous), task),
                kind=MessageKind.CRITIQUE,
                step=state.step,
            )
            for agent_id in state.active_ids
        )
        decisions = tuple(
            _validate(
                self.revise(deepcopy(state.agents[d.agent_id]), deepcopy(d), deepcopy(critiques), task),
                d.agent_id,
                task,
            )
            for d in previous
        )
        run["decisions"], run["round"] = decisions, run["round"] + 1
        result = self.consensus.aggregate(decisions, task)
        done = bool(result.metadata["converged"]) or run["round"] >= self.max_rounds
        run["done"] = done
        return AlgorithmResult(
            messages=critiques,
            decisions=decisions,
            metrics={**result.metrics, "debate_round": float(run["round"])},
            metadata={**result.metadata, "phase": "revise", "done": done},
        )
