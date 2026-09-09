"""Composable, provider-neutral agentic swarm algorithms."""

from .types import (
    Agent,
    AgentContext,
    AgentOutput,
    AgentState,
    AlgorithmResult,
    Artifact,
    ArtifactVerifier,
    Decision,
    Evidence,
    Feedback,
    Message,
    MessageKind,
    SwarmAlgorithm,
    SwarmState,
    Task,
    TopologyPolicy,
    Usage,
)

__version__ = "0.2.0"
__all__ = [
    "Agent",
    "AgentContext",
    "AgentOutput",
    "AgentState",
    "AlgorithmResult",
    "Artifact",
    "ArtifactVerifier",
    "Decision",
    "Evidence",
    "Feedback",
    "Message",
    "MessageKind",
    "SwarmAlgorithm",
    "SwarmState",
    "Task",
    "TopologyPolicy",
    "Usage",
]

from .catalog import methods, resolve
from .runtime import CallableAgent, CompletionAgent, MessageBus, Pipeline, SwarmRuntime, apply_result
from .types import Budget, KVCache, LatentPayload, MethodInfo

__all__ += [
    "Budget",
    "KVCache",
    "LatentPayload",
    "MethodInfo",
    "CallableAgent",
    "CompletionAgent",
    "MessageBus",
    "Pipeline",
    "SwarmRuntime",
    "apply_result",
    "methods",
    "resolve",
]
