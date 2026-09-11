"""A research-and-production economy for controlled swarm communication experiments."""

from .experiment import FoundryCheckpoint, FoundryConfig, FoundryExperiment, FoundryRun
from .policies import FoundryScientist
from .study import CommunicationPortfolio, cross_play, paired_difference, run_study, summarize
from .world import FoundryWorld

__all__ = [
    "CommunicationPortfolio",
    "cross_play",
    "paired_difference",
    "run_study",
    "summarize",
    "FoundryWorld",
    "FoundryConfig",
    "FoundryExperiment",
    "FoundryScientist",
    "FoundryRun",
    "FoundryCheckpoint",
]
