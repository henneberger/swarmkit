"""Normalize equivalent inquiry response envelopes without inferring evidence.

This is syntax normalization only. Callers must validate action permissions,
parameters, and each returned alias against the exact model-visible references.
ValueError messages are fixed categories and never echo model/source content.
"""

from __future__ import annotations

import json
import math
import re
from typing import Any

_KINDS = frozenset(
    {"open", "join", "request_peer", "reply", "search", "read", "watch", "revise", "close", "wait"}
)
_MAX_RESPONSE_CHARS = 1_000_000


def _object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate_json_key")
        result[key] = value
    return result


def _constant(_: str) -> None:
    raise ValueError("nonfinite_json_number")


def _float(value: str) -> float:
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("nonfinite_json_number")
    return number


def _aliases(value: Any) -> list[str]:
    if not isinstance(value, list):
        raise ValueError("invalid_evidence_shape")
    aliases = []
    for item in value:
        if isinstance(item, dict):
            if set(item) != {"span_id"}:
                raise ValueError("ambiguous_evidence_reference")
            item = item["span_id"]
        if not isinstance(item, str) or not item.strip():
            raise ValueError("invalid_evidence_reference")
        aliases.append(item)
    return aliases


def parse_response(text: str, finish_reason: str) -> tuple[str, dict[str, Any]]:
    """Return normalized ``(update, action)`` or a bounded ValueError category.

    Accept one action in an ``action`` envelope, a singleton ``actions`` list,
    or a direct object with ``kind``. An optional entire-response JSON code fence
    is allowed. Missing update becomes a neutral requested-action description;
    narrative and evidence content are never filled in or extracted from prose.
    """
    if finish_reason != "stop":
        raise ValueError("incomplete_response")
    if not isinstance(text, str) or not text.strip():
        raise ValueError("invalid_response_text")
    if len(text) > _MAX_RESPONSE_CHARS:
        raise ValueError("response_too_large")
    payload = text.strip()
    if payload.startswith("```"):
        fence = re.fullmatch(
            r"```(?:json)?[ \t]*\r?\n(.*?)\r?\n```[ \t]*", payload, re.DOTALL | re.IGNORECASE
        )
        if fence is None:
            raise ValueError("invalid_json_fence")
        payload = fence[1]
    try:
        data = json.loads(payload, object_pairs_hook=_object, parse_constant=_constant, parse_float=_float)
    except (json.JSONDecodeError, RecursionError) as exc:
        raise ValueError("invalid_json") from exc
    except ValueError as exc:
        if str(exc) in {"duplicate_json_key", "nonfinite_json_number"}:
            raise
        raise ValueError("invalid_json") from exc
    if not isinstance(data, dict):
        raise ValueError("invalid_response_shape")
    data = {key: value for key, value in data.items() if value is not None}
    shapes = [key for key in ("action", "actions", "kind") if key in data]
    if not shapes:
        raise ValueError("missing_action")
    if len(shapes) != 1:
        raise ValueError("ambiguous_action_shape")
    shape = shapes[0]
    if shape != "kind" and set(data) - {"update", shape}:
        raise ValueError("unknown_response_field")
    if shape == "action":
        action = data["action"]
    elif shape == "actions":
        if not isinstance(data["actions"], list) or len(data["actions"]) != 1:
            raise ValueError("action_count")
        action = data["actions"][0]
    else:
        action = {key: value for key, value in data.items() if key != "update"}
    if not isinstance(action, dict):
        raise ValueError("invalid_action_shape")
    action = {key: value for key, value in action.items() if value is not None}
    kind = action.get("kind")
    if not isinstance(kind, str) or kind not in _KINDS:
        raise ValueError("unknown_action")
    if "action" in action or "actions" in action:
        raise ValueError("nested_action_shape")

    update = data.get("update")
    if isinstance(update, dict):
        if set(update) != {"text"} or not isinstance(update["text"], str):
            raise ValueError("invalid_update_shape")
        update = update["text"]
    elif isinstance(update, list):
        if any(not isinstance(item, str) for item in update):
            raise ValueError("invalid_update_shape")
        update = "\n".join(update)
    elif update is not None and not isinstance(update, str):
        raise ValueError("invalid_update_shape")
    if update is None:
        update = f"Requested {kind}."

    if kind == "search" and "terms" in action:
        terms = action["terms"]
        if (
            not isinstance(terms, list)
            or not terms
            or any(not isinstance(term, str) or not term.strip() for term in terms)
        ):
            raise ValueError("invalid_search_terms")
        query = " ".join(terms)
        if "query" in action and action["query"] != query:
            raise ValueError("ambiguous_search_query")
        action["query"] = query
        del action["terms"]

    evidence = _aliases(action["evidence"]) if "evidence" in action else None
    alternate = _aliases(action["evidence_ids"]) if "evidence_ids" in action else None
    if evidence is not None and alternate is not None and evidence != alternate:
        raise ValueError("conflicting_evidence_aliases")
    action["evidence"] = evidence if evidence is not None else alternate if alternate is not None else []
    action.pop("evidence_ids", None)
    return update, action
