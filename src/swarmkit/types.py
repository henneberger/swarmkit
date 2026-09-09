"""Canonical data contracts used by every swarmkit subsystem.

Payloads are JSON-shaped by convention; local numerical adapters may carry arrays
in metadata. No provider or algorithm defines an alternative agent/message type.
"""

from __future__ import annotations

import math
import random
import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Protocol, Sequence, runtime_checkable


def new_id(prefix: str = "item") -> str:
    return f"{prefix}-{uuid.uuid4().hex}"


def probability(value: float, name: str = "probability") -> float:
    if not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError(f"{name} must be finite and in [0, 1]")
    return value


class MessageKind(str, Enum):
    OBSERVATION = "observation"
    QUESTION = "question"
    PROPOSAL = "proposal"
    CRITIQUE = "critique"
    DECISION = "decision"
    RESULT = "result"
    NOTIFICATION = "notification"


@dataclass(frozen=True)
class Evidence:
    id: str
    claim: str
    source: str
    owner: str
    confidence: float = 1.0
    supports: tuple[str, ...] = ()
    contradicts: tuple[str, ...] = ()
    parents: tuple[str, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        probability(self.confidence, "confidence")
        if not self.id or not self.source:
            raise ValueError("evidence requires an id and a source")


@dataclass(frozen=True)
class Message:
    sender: str
    content: str
    recipients: tuple[str, ...] = ()  # empty means broadcast to active peers
    kind: MessageKind = MessageKind.OBSERVATION
    evidence: tuple[Evidence, ...] = ()
    artifact_ids: tuple[str, ...] = ()
    parents: tuple[str, ...] = ()
    step: int = 0
    id: str = field(default_factory=lambda: new_id("msg"))
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Artifact:
    id: str
    author: str
    content: Any
    parents: tuple[str, ...] = ()
    evidence: tuple[Evidence, ...] = ()
    score: float | None = None
    verified: bool = False
    tags: frozenset[str] = frozenset()
    created_step: int = 0
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.score is not None and not math.isfinite(self.score):
            raise ValueError("artifact score must be finite")


@dataclass(frozen=True)
class Decision:
    agent_id: str
    answer: str
    confidence: float = 1.0
    evidence_ids: tuple[str, ...] = ()
    rationale: str = ""
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        probability(self.confidence, "confidence")


@dataclass(frozen=True)
class Task:
    id: str
    description: str
    candidates: tuple[str, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass
class AgentState:
    id: str
    capabilities: frozenset[str] = frozenset()
    private_evidence: tuple[Evidence, ...] = ()
    inbox: list[Message] = field(default_factory=list)
    memory: dict[str, Any] = field(default_factory=dict)
    beliefs: dict[str, float] = field(default_factory=dict)
    score: float = 0.0
    active: bool = True
    position: tuple[float, ...] | None = None


@dataclass
class SwarmState:
    agents: dict[str, AgentState] = field(default_factory=dict)
    messages: list[Message] = field(default_factory=list)
    artifacts: dict[str, Artifact] = field(default_factory=dict)
    step: int = 0
    seed: int = 0
    data: dict[str, Any] = field(default_factory=dict)
    rng: random.Random = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.rng = random.Random(self.seed)
        if any(key != agent.id for key, agent in self.agents.items()):
            raise ValueError("agent dictionary keys must match agent ids")

    @property
    def active_ids(self) -> tuple[str, ...]:
        return tuple(key for key, agent in self.agents.items() if agent.active)


@dataclass(frozen=True)
class Feedback:
    utility: float
    costs: float = 0.0
    per_agent: Mapping[str, float] = field(default_factory=dict)
    verified: bool = False
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Usage:
    calls: int = 1
    tokens: int = 0
    cost: float = 0.0

    def __post_init__(self) -> None:
        if self.calls < 0 or self.tokens < 0 or self.cost < 0 or not math.isfinite(self.cost):
            raise ValueError("usage cannot be negative or non-finite")


@dataclass(frozen=True)
class AgentContext:
    task: Task
    agent: AgentState
    messages: tuple[Message, ...] = ()
    artifacts: tuple[Artifact, ...] = ()
    phase: str = "explore"
    step: int = 0


@dataclass(frozen=True)
class AgentOutput:
    messages: tuple[Message, ...] = ()
    decision: Decision | None = None
    artifacts: tuple[Artifact, ...] = ()
    usage: Usage = field(default_factory=Usage)
    memory_updates: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AlgorithmResult:
    messages: tuple[Message, ...] = ()
    decisions: tuple[Decision, ...] = ()
    artifacts: tuple[Artifact, ...] = ()
    metrics: Mapping[str, float] = field(default_factory=dict)
    metadata: Mapping[str, Any] = field(default_factory=dict)


@runtime_checkable
class Agent(Protocol):
    async def act(self, context: AgentContext) -> AgentOutput: ...


@runtime_checkable
class TopologyPolicy(Protocol):
    def neighbors(self, state: SwarmState, sender: str) -> Sequence[str]: ...


@runtime_checkable
class SwarmAlgorithm(Protocol):
    def step(self, state: SwarmState, task: Task) -> AlgorithmResult: ...


@runtime_checkable
class ArtifactVerifier(Protocol):
    def __call__(self, artifact: Artifact) -> Feedback: ...


@dataclass
class Budget:
    """Dispatch limits and observed usage; token/cost totals are known after calls."""

    max_calls: int | None = None
    max_tokens: int | None = None
    max_cost: float | None = None
    max_steps: int | None = None
    used_calls: int = 0
    used_tokens: int = 0
    used_cost: float = 0.0
    used_steps: int = 0

    def __post_init__(self) -> None:
        for name in ("max_calls", "max_tokens", "max_steps", "used_calls", "used_tokens", "used_steps"):
            value = getattr(self, name)
            if value is not None and (not isinstance(value, int) or value < 0):
                raise ValueError(f"{name} must be a nonnegative integer or None")
        for name in ("max_cost", "used_cost"):
            value = getattr(self, name)
            if value is not None and (not math.isfinite(value) or value < 0):
                raise ValueError(f"{name} must be finite and nonnegative")

    @property
    def exhausted(self) -> bool:
        return any(
            limit is not None and used >= limit
            for limit, used in (
                (self.max_calls, self.used_calls),
                (self.max_tokens, self.used_tokens),
                (self.max_cost, self.used_cost),
                (self.max_steps, self.used_steps),
            )
        )


@dataclass(frozen=True)
class LatentPayload:
    """Numeric channel packet. The codec validates shape/model compatibility."""

    values: Any
    model_id: str
    layer: int | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class KVCache:
    """Paired key/value arrays; feature dimension is always the final axis."""

    keys: Any
    values: Any
    model_id: str
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class MethodInfo:
    """Discoverable implementation/provenance contract for a method family."""

    name: str
    family: str
    target: str
    sources: tuple[str, ...]
    fidelity: str
    description: str
    limitations: str
