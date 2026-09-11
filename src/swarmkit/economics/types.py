"""Economic records and callback contracts; observations exclude other private types."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol


@dataclass(frozen=True)
class EconomicHyperedge:
    id: str
    members: tuple[str, ...]
    mechanism_id: str
    roles: Mapping[str, str] = field(default_factory=dict)
    resource_ids: tuple[str, ...] = ()

    def __post_init__(self):
        if (
            not self.id
            or not self.mechanism_id
            or not self.members
            or len(set(self.members)) != len(self.members)
        ):
            raise ValueError("edge requires identifiers and distinct participants")
        if not set(self.roles) <= set(self.members):
            raise ValueError("roles must belong to participants")


@dataclass(frozen=True)
class PrivateType:
    values: Mapping[str, float] = field(default_factory=dict)
    costs: Mapping[str, float] = field(default_factory=dict)
    capabilities: tuple[str, ...] = ()


@dataclass(frozen=True)
class EconomicObservation:
    edge_id: str
    round: int
    agent_id: str
    members: tuple[str, ...]
    private_type: PrivateType
    public: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class EconomicAction:
    edge_id: str
    round: int
    agent_id: str
    kind: str
    payload: Any


@dataclass(frozen=True)
class Settlement:
    id: str
    transfers: Mapping[str, float]
    inventory: Mapping[str, Mapping[str, float]] = field(default_factory=dict)
    releases: tuple[str, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)


class Strategy(Protocol):
    def __call__(self, observation: EconomicObservation) -> EconomicAction: ...


class Mechanism(Protocol):
    def clear(self, submissions: Mapping[str, Any]) -> Any: ...


class GameModel(Protocol):
    def utilities(self, actions: Any) -> Any: ...
