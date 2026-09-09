"""Optional provider adapters; importing this package never starts API calls."""

from .deepseek import (
    CompletionResult,
    DeepSeekClient,
    GateBusy,
    GateDenied,
    GateLimits,
    ProviderError,
    SQLiteCallGate,
)

__all__ = [
    "CompletionResult",
    "DeepSeekClient",
    "GateBusy",
    "GateDenied",
    "GateLimits",
    "ProviderError",
    "SQLiteCallGate",
]
