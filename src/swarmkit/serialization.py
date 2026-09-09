"""Versioned, non-pickle JSON snapshots of shared state and random-generator state.

Only a fixed whitelist of canonical dataclasses can be constructed. Unsupported
objects (including callables) fail explicitly rather than executing/importing code.
Algorithm objects, trained codecs and external backends are configured separately.
"""

from __future__ import annotations

import json
import math
import os
import tempfile
from dataclasses import fields, is_dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Mapping

import numpy as np

from . import types

_ALLOWED = {
    name: getattr(types, name)
    for name in (
        "Evidence",
        "Message",
        "Artifact",
        "Decision",
        "Task",
        "AgentState",
        "SwarmState",
        "Feedback",
        "Usage",
        "AgentContext",
        "AgentOutput",
        "AlgorithmResult",
        "Budget",
        "LatentPayload",
        "KVCache",
    )
}


def to_data(value: Any) -> Any:
    if isinstance(value, Enum):
        if not isinstance(value, types.MessageKind):
            raise TypeError("unsupported enum")
        return {"$type": "MessageKind", "value": value.value}
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, (float, np.floating)):
        if not math.isfinite(value):
            raise ValueError("non-finite values cannot be serialized")
        return float(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.ndarray):
        if value.dtype.kind not in "biuf" or not np.isfinite(value).all():
            raise TypeError("only finite numeric arrays may be serialized")
        return {
            "$type": "array",
            "dtype": str(value.dtype),
            "shape": list(value.shape),
            "values": value.tolist(),
        }
    if isinstance(value, Mapping):
        return {"$type": "mapping", "items": [[to_data(k), to_data(v)] for k, v in value.items()]}
    if isinstance(value, (list, tuple, set, frozenset)):
        return {"$type": type(value).__name__, "items": [to_data(v) for v in value]}
    if (
        is_dataclass(value)
        and type(value).__name__ in _ALLOWED
        and type(value) is _ALLOWED[type(value).__name__]
    ):
        data = {field.name: to_data(getattr(value, field.name)) for field in fields(value) if field.init}
        if isinstance(value, types.SwarmState):
            data["_rng_state"] = to_data(value.rng.getstate())
        return {"$type": type(value).__name__, "fields": data}
    raise TypeError(f"unsupported snapshot object: {type(value).__name__}")


def from_data(value: Any) -> Any:
    if not isinstance(value, dict):
        if value is None or isinstance(value, (str, bool, int)):
            return value
        if isinstance(value, float) and math.isfinite(value):
            return value
        raise ValueError("malformed snapshot value")
    kind = value.get("$type")
    if kind == "MessageKind":
        return types.MessageKind(value["value"])
    if kind == "mapping":
        return {from_data(k): from_data(v) for k, v in value["items"]}
    if kind in ("list", "tuple", "set", "frozenset"):
        constructor = {"list": list, "tuple": tuple, "set": set, "frozenset": frozenset}[kind]
        return constructor(from_data(v) for v in value["items"])
    if kind == "array":
        dtype = np.dtype(value["dtype"])
        if dtype.kind not in "biuf":
            raise ValueError("unsupported array dtype")
        array = np.array(value["values"], dtype=dtype)
        shape = value["shape"]
        if not isinstance(shape, list) or any(type(d) is not int or d < 0 for d in shape):
            raise ValueError("array shape must contain nonnegative integer dimensions")
        # tolist loses axes after the first empty dimension; restore those axes.
        if array.size == 0 and 0 in shape:
            array = array.reshape(tuple(shape))
        if tuple(value["shape"]) != array.shape or not np.isfinite(array).all():
            raise ValueError("array shape or values invalid")
        return array
    if kind not in _ALLOWED:
        raise ValueError(f"unknown snapshot type: {kind}")
    kwargs = {k: from_data(v) for k, v in value["fields"].items()}
    rng_state = kwargs.pop("_rng_state", None)
    result = _ALLOWED[kind](**kwargs)
    if rng_state is not None:
        if not isinstance(result, types.SwarmState):
            raise ValueError("random state only belongs to SwarmState")
        result.rng.setstate(rng_state)
    return result


def dumps(state: types.SwarmState) -> str:
    if not isinstance(state, types.SwarmState):
        raise TypeError("snapshot root must be SwarmState")
    return json.dumps({"format": "swarmkit", "version": 1, "state": to_data(state)}, allow_nan=False)


def loads(text: str) -> types.SwarmState:
    envelope = json.loads(text)
    if (
        not isinstance(envelope, dict)
        or envelope.get("format") != "swarmkit"
        or type(envelope.get("version")) is not int
        or envelope.get("version") != 1
    ):
        raise ValueError("unsupported snapshot format or version")
    state = from_data(envelope["state"])
    if not isinstance(state, types.SwarmState):
        raise ValueError("snapshot root must be SwarmState")
    return state


def save(state: types.SwarmState, path: str | Path) -> None:
    path = Path(path)
    payload = dumps(state)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, prefix=path.name + ".", suffix=".tmp", delete=False
        ) as stream:
            temporary = Path(stream.name)
            stream.write(payload)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def load(path: str | Path) -> types.SwarmState:
    return loads(Path(path).read_text())
