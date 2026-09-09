"""Evidence and artifact mechanisms for collective knowledge.

Fresh, bounded adaptations of HiddenBench (https://arxiv.org/abs/2505.11556),
SwarmWorld (https://arxiv.org/abs/2608.26081), peer verification
(https://github.com/gensyn-ai/collaborative-autoresearch-demo), minimal culture
(https://arxiv.org/abs/2606.30668), and generational accumulation
(https://arxiv.org/abs/2406.00392). These are mechanisms, not reproductions.
Verifier callbacks are trusted application code, not a security sandbox.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Iterable, Sequence
from copy import deepcopy
from dataclasses import replace

from .types import (
    AgentState,
    AlgorithmResult,
    Artifact,
    ArtifactVerifier,
    Evidence,
    Feedback,
    SwarmState,
    Task,
    probability,
)


def _feedback_ok(feedback: Feedback, minimum: float) -> bool:
    return (
        feedback.verified
        and math.isfinite(feedback.utility)
        and math.isfinite(feedback.costs)
        and feedback.utility >= minimum
    )


class EvidenceRegistry:
    """Immutable evidence DAG; source ancestry, never agent votes, defines independence.

    Parents must already exist. Descendants inherit root source identities, so
    copying a claim to ten agents does not create ten independent observations.
    ``scores`` distributes each claim's confidence over its roots and takes the
    maximum positive/negative contribution per root, preventing copy inflation.
    Source identifiers must be supplied honestly; this is not source authentication.
    """

    def __init__(self, evidence: Iterable[Evidence] = ()) -> None:
        self._items: dict[str, Evidence] = {}
        self.add_many(evidence)

    def add(self, evidence: Evidence) -> None:
        if evidence.id in evidence.parents:
            raise ValueError("evidence cannot be its own parent")
        if evidence.id in self._items:
            if self._items[evidence.id] != evidence:
                raise ValueError("evidence id cannot be overwritten")
            return
        if any(parent not in self._items for parent in evidence.parents):
            raise ValueError("unknown evidence parent")
        self._items[evidence.id] = deepcopy(evidence)

    def add_many(self, evidence: Iterable[Evidence]) -> None:
        """Accept unordered DAGs transactionally; reject missing parents and cycles."""
        pending = list(evidence)
        backup = deepcopy(self._items)
        try:
            while pending:
                ready = [e for e in pending if all(p in self._items for p in e.parents)]
                if not ready:
                    raise ValueError("missing evidence parents or ancestry cycle")
                for item in ready:
                    self.add(item)
                    pending.remove(item)
        except Exception:
            self._items = backup
            raise

    def get(self, evidence_id: str) -> Evidence:
        return deepcopy(self._items[evidence_id])

    @property
    def evidence(self) -> tuple[Evidence, ...]:
        return tuple(deepcopy(list(self._items.values())))

    def roots(self, evidence_id: str) -> frozenset[str]:
        item = self._items[evidence_id]
        if not item.parents:
            return frozenset((item.source,))
        return frozenset(root for p in item.parents for root in self.roots(p))

    def scores(self, candidates: Sequence[str]) -> dict[str, float]:
        result = {}
        for candidate in candidates:
            positive: dict[str, float] = {}
            negative: dict[str, float] = {}
            for item in self._items.values():
                roots = self.roots(item.id)
                contribution = item.confidence / len(roots)
                for root in roots:
                    if candidate in item.supports:
                        positive[root] = max(positive.get(root, 0.0), contribution)
                    if candidate in item.contradicts:
                        negative[root] = max(negative.get(root, 0.0), contribution)
            result[candidate] = sum(positive.values()) - sum(negative.values())
        return result

    def independent_sources(self) -> frozenset[str]:
        return frozenset(r for key in self._items for r in self.roots(key))


class ArtifactStore:
    """Verified admission, immutable snapshots, explicit ancestry and retirement.

    A parent must be admitted before its child: cycles and dangling ancestry are
    impossible. Retirement excludes future adoption but preserves history. Caller
    supplied ``verified=True`` is ignored; every admission calls the verifier.
    """

    def __init__(self, verifier: ArtifactVerifier, minimum_score: float = 0.0) -> None:
        if not math.isfinite(minimum_score):
            raise ValueError("minimum_score must be finite")
        self.verifier = verifier
        self.minimum_score = minimum_score
        self._items: dict[str, Artifact] = {}
        self._retired: dict[str, str] = {}

    def admit(self, artifact: Artifact) -> Artifact:
        if not artifact.id or artifact.id in self._items:
            raise ValueError("artifact id must be new and nonempty")
        if artifact.id in artifact.parents or any(p not in self._items for p in artifact.parents):
            raise ValueError("invalid artifact ancestry")
        candidate = deepcopy(artifact)
        feedback = self.verifier(deepcopy(candidate))
        if not _feedback_ok(feedback, self.minimum_score):
            raise ValueError("artifact failed admission verification")
        admitted = replace(candidate, verified=True, score=feedback.utility)
        self._items[admitted.id] = deepcopy(admitted)
        return deepcopy(admitted)

    def get(self, artifact_id: str, *, active_only: bool = False) -> Artifact:
        if active_only and artifact_id in self._retired:
            raise ValueError("artifact is retired")
        return deepcopy(self._items[artifact_id])

    def retire(self, artifact_id: str, reason: str) -> None:
        if artifact_id not in self._items:
            raise KeyError(artifact_id)
        if not reason:
            raise ValueError("retirement requires a reason")
        self._retired[artifact_id] = reason

    @property
    def active(self) -> tuple[Artifact, ...]:
        return tuple(self.get(key) for key in self._items if key not in self._retired)

    def lineage(self, artifact_id: str) -> tuple[str, ...]:
        seen: set[str] = set()
        ordered: list[str] = []

        def visit(key: str) -> None:
            if key not in seen:
                seen.add(key)
                for parent in self._items[key].parents:
                    visit(parent)
                ordered.append(key)

        visit(artifact_id)
        return tuple(ordered)


class PeerAdoption:
    """Adopt only after local evaluation, then roll back if later fitness fails.

    Evaluator(agent, artifact, task) -> Feedback. ``None`` artifact means current
    baseline behavior. No artifact content is executed by this class. An adoption
    is just a memory reference; the application chooses how to use that reference.
    """

    def __init__(
        self,
        store: ArtifactStore,
        evaluator: Callable[[AgentState, Artifact | None, Task], Feedback],
        minimum_gain: float = 0.0,
        memory_key: str = "adopted_artifact",
    ) -> None:
        if not math.isfinite(minimum_gain) or minimum_gain < 0:
            raise ValueError("minimum_gain must be finite and nonnegative")
        self.store, self.evaluator = store, evaluator
        self.minimum_gain, self.memory_key = minimum_gain, memory_key
        self._history: dict[str, tuple[bool, object, float]] = {}

    def adopt(self, agent: AgentState, artifact_id: str, task: Task) -> bool:
        if agent.id in self._history:
            raise ValueError("audit or rollback existing trial before adopting again")
        artifact = self.store.get(artifact_id, active_only=True)
        baseline = self.evaluator(deepcopy(agent), None, task)
        candidate = self.evaluator(deepcopy(agent), artifact, task)
        if not (
            _feedback_ok(baseline, -math.inf)
            and _feedback_ok(candidate, baseline.utility + self.minimum_gain)
        ):
            return False
        self._history[agent.id] = (
            self.memory_key in agent.memory,
            deepcopy(agent.memory.get(self.memory_key)),
            baseline.utility,
        )
        agent.memory[self.memory_key] = artifact_id
        return True

    def rollback(self, agent: AgentState) -> None:
        present, previous, _ = self._history.pop(agent.id)
        if present:
            agent.memory[self.memory_key] = previous
        else:
            agent.memory.pop(self.memory_key, None)

    def audit(self, agent: AgentState, task: Task) -> bool:
        """Commit a locally successful trial; restore previous reference on failure."""
        _, _, baseline = self._history[agent.id]
        try:
            artifact = self.store.get(agent.memory[self.memory_key], active_only=True)
            feedback = self.evaluator(deepcopy(agent), artifact, task)
            passed = _feedback_ok(feedback, baseline + self.minimum_gain)
        except Exception:
            self.rollback(agent)
            raise
        if passed:
            self._history.pop(agent.id)
        else:
            self.rollback(agent)
        return passed


class DecayingMemory:
    """Stigmergic shared memory with exponential decay and explicit peer refresh.

    Inspired by https://arxiv.org/abs/2606.30668; numeric expiry approximates the
    paper's text corruption. Refresh records maintenance, not independent evidence.
    """

    def __init__(self, half_life: float = 4.0, threshold: float = 0.05) -> None:
        if not math.isfinite(half_life) or half_life <= 0:
            raise ValueError("half_life must be positive and finite")
        probability(threshold, "threshold")
        if threshold == 0:
            raise ValueError("threshold must be positive")
        self.half_life, self.threshold = half_life, threshold
        self._records: dict[str, tuple[Artifact, float, int]] = {}
        self.refreshers: dict[str, set[str]] = {}
        self._step = 0

    def _advance(self, step: int) -> None:
        if step < self._step:
            raise ValueError("memory time must not move backwards")
        self._step = step
        expired = [
            key
            for key, (_, strength, updated) in self._records.items()
            if strength * 2 ** (-(step - updated) / self.half_life) < self.threshold
        ]
        for key in expired:
            del self._records[key]
            self.refreshers.pop(key, None)

    def write(self, artifact: Artifact, step: int) -> None:
        self._advance(step)
        if artifact.id in self._records:
            raise ValueError("use refresh for existing artifact, or a new id for revisions")
        self._records[artifact.id] = (deepcopy(artifact), 1.0, step)
        self.refreshers[artifact.id] = {artifact.author}

    def read(self, artifact_id: str, step: int) -> Artifact:
        self._advance(step)
        return deepcopy(self._records[artifact_id][0])

    def refresh(self, artifact_id: str, agent_id: str, step: int) -> None:
        self._advance(step)
        artifact, _, _ = self._records[artifact_id]
        self._records[artifact_id] = (artifact, 1.0, step)
        self.refreshers[artifact_id].add(agent_id)

    def available(self, step: int) -> tuple[Artifact, ...]:
        self._advance(step)
        return tuple(deepcopy(record[0]) for record in self._records.values())


class CulturalTransfer:
    """Locally test inherited artifacts in a new generation, recording lineage.

    This implements observable artifact transfer, not policy-weight inheritance.
    Each active receiver evaluates every active artifact against a task, then
    adopts the highest verified score meeting the threshold. Independent local
    evaluation is retained even if the sender's artifact was already admitted.
    """

    def __init__(
        self,
        store: ArtifactStore,
        evaluator: Callable[[AgentState, Artifact, Task], Feedback],
        minimum_score: float = 0.0,
    ) -> None:
        if not math.isfinite(minimum_score):
            raise ValueError("minimum_score must be finite")
        self.store, self.evaluator, self.minimum_score = store, evaluator, minimum_score

    def step(self, state: SwarmState, task: Task) -> AlgorithmResult:
        adopted = 0
        transfers: dict[str, str] = {}
        for agent_id in state.active_ids:
            agent = state.agents[agent_id]
            viable = []
            for artifact in self.store.active:
                feedback = self.evaluator(deepcopy(agent), artifact, task)
                if _feedback_ok(feedback, self.minimum_score):
                    viable.append((feedback.utility, artifact.id))
            if viable:
                _, artifact_id = max(viable, key=lambda pair: (pair[0], pair[1]))
                artifact = self.store.get(artifact_id)
                agent.memory["cultural_artifact"] = artifact_id
                agent.memory["cultural_lineage"] = self.store.lineage(artifact_id)
                state.artifacts[artifact_id] = artifact
                transfers[agent_id] = artifact_id
                adopted += 1
        return AlgorithmResult(metrics={"adoptions": float(adopted)}, metadata={"transfers": transfers})


class ProcedureAbstraction:
    """Propose a reusable procedure from artifacts, admit on held-out tasks only.

    proposer(artifacts) -> Artifact; evaluator(artifact, task) -> Feedback.
    Callables are supplied by the application. Text is never evaluated as code.
    Explicit disjoint task IDs prevent accidental train/test reuse; they cannot
    detect semantic overlap or hidden leakage within user callbacks.
    """

    def __init__(
        self,
        store: ArtifactStore,
        proposer: Callable[[tuple[Artifact, ...]], Artifact],
        evaluator: Callable[[Artifact, Task], Feedback],
        minimum_score: float = 0.0,
    ) -> None:
        if not math.isfinite(minimum_score):
            raise ValueError("minimum_score must be finite")
        self.store, self.proposer, self.evaluator = store, proposer, evaluator
        self.minimum_score = minimum_score

    def discover(
        self, parents: Sequence[str], held_out: Sequence[Task], training_task_ids: Iterable[str] = ()
    ) -> Artifact:
        if not parents or not held_out:
            raise ValueError("parents and held-out tasks are required")
        ids = [task.id for task in held_out]
        if len(ids) != len(set(ids)) or set(ids) & set(training_task_ids):
            raise ValueError("held-out tasks must be distinct and disjoint from training")
        artifacts = tuple(self.store.get(key, active_only=True) for key in parents)
        candidate = self.proposer(artifacts)
        candidate = replace(candidate, parents=tuple(parents))
        feedbacks = [self.evaluator(deepcopy(candidate), task) for task in held_out]
        if not all(_feedback_ok(f, self.minimum_score) for f in feedbacks):
            raise ValueError("procedure failed held-out validation")
        metadata = dict(candidate.metadata)
        metadata["held_out_scores"] = dict(zip(ids, (f.utility for f in feedbacks), strict=True))
        return self.store.admit(replace(candidate, metadata=metadata))
