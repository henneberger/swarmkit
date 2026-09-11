"""Communication experiments and original diagnostic task generators."""

from .communication import (
    ChannelConfig,
    CommunicationCase,
    CommunicationEvaluator,
    EvaluationRun,
    paired_summary,
    quality_cost_summary,
)
from .tasks import EvidenceAgent, distributed_evidence, interdependent_schedule

__all__ = [
    "ChannelConfig",
    "CommunicationCase",
    "CommunicationEvaluator",
    "EvaluationRun",
    "paired_summary",
    "quality_cost_summary",
    "EvidenceAgent",
    "distributed_evidence",
    "interdependent_schedule",
]
