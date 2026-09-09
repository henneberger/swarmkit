"""Deterministic, provider-free exports of recorded inquiry activity.

Replay cursor fields order records; embedded email dates never do. The exporter
does not infer successful discoveries, causal communication effects, or outcomes.
"""

from __future__ import annotations

import html
import json
import re
from collections import Counter, defaultdict
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_SUMMARY_FIELDS = (
    "id", "mode", "model", "status", "algorithm_version", "created_at", "finished_at",
    "config", "metrics", "limits", "runtime_usage", "shared_ledger_delta", "shared_ledger_delta_scope",
    "coverage_limitations", "reasoning_rejections", "validation_rejections", "errors", "agent_errors",
)
_SUBSTANTIVE_EVENTS = {
    "peer_message", "watch_wake", "action_rejected", "inquiry_opened", "inquiry_revised",
    "inquiry_closed", "inquiry_joined", "recruitment", "private_read",
}


def _text(value: Any) -> str:
    """Render untrusted content literally, including Markdown/HTML delimiters."""
    raw = json.dumps(value, ensure_ascii=False) if isinstance(value, (dict, list)) else str(value)
    return re.sub(r"([\\`*_{}\[\]()#+.!|>~-])", r"\\\1", html.escape(raw, quote=False))


def _json_block(value: Any) -> list[str]:
    payload = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)
    longest = max((len(match[0]) for match in re.finditer(r"`+", payload)), default=0)
    fence = "`" * max(3, longest + 1)
    return [fence + "json", payload, fence, ""]


def _records(run: Mapping[str, Any], key: str) -> list[dict[str, Any]]:
    value = run.get(key, [])
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise ValueError(f"{key} must be a list of objects")
    return value


def _number(value: Any) -> int | None:
    return value if type(value) is int and value >= 0 else None


def _clock(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        clock = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return clock.astimezone(timezone.utc) if clock.tzinfo is not None else None
    except ValueError:
        return None


def _order(record: dict[str, Any], source: int, index: int) -> tuple:
    clock = _clock(record.get("virtual_time"))
    sequence = _number(record.get("arrival_sequence"))
    occurrence = _number(record.get("occurrence_order", record.get("event_sequence")))
    return (
        clock is None,
        clock or datetime.max.replace(tzinfo=timezone.utc),
        sequence is None,
        sequence or 0,
        occurrence is None,
        occurrence or 0,
        source,
        index,
    )


def _field(lines: list[str], label: str, value: Any) -> None:
    if value is not None and value != "" and value != []:
        if isinstance(value, list):
            lines.extend([f"**{label}:**", "", *["- " + _text(item) for item in value], ""])
        else:
            lines.extend([f"**{label}:** {_text(value)}", ""])


def _evidence(lines: list[str], items: Any) -> None:
    if not isinstance(items, list):
        return
    for item in items:
        if not isinstance(item, dict):
            lines.extend(["Evidence reference: " + _text(item), ""])
            continue
        meta = item.get("metadata") if isinstance(item.get("metadata"), dict) else {}
        document_id = item.get("document_id", meta.get("document_id", meta.get("doc_id")))
        _field(lines, "Source document", document_id or "Not recorded")
        _field(lines, "Evidence ID", item.get("id"))
        _field(lines, "Source family", item.get("source", meta.get("source_family")))
        valid = item.get("valid", item.get("quote_valid"))
        check = "passed" if valid is True else "failed" if valid is False else "not recorded"
        review = "human review recorded" if item.get("human_reviewed") is True else "no human review recorded"
        lines.extend([f"Source-text check: {check}; {review}. This does not validate the associated explanation.", ""])
        _field(lines, "Associated claim", item.get("claim"))
        quote = item.get("quote", meta.get("quote"))
        if quote is not None:
            lines.extend(["> " + _text(quote).replace("\n", "\n> "), ""])
        provenance = {key: meta[key] for key in (
            "start", "end", "offset_basis", "segment_id", "segment_kind", "claimed_sender", "claimed_date",
            "attribution_status", "raw_sha256", "quote_fingerprint",
        ) if key in meta}
        if provenance:
            lines.extend(["Source offsets and attribution claims (complete metadata in audit JSON):", ""])
            lines.extend(_json_block(provenance))


def _inquiry(lines: list[str], item: dict[str, Any]) -> None:
    for key, label in (
        ("question", "Question"), ("inquiry_id", "Inquiry ID"), ("version", "Version"),
        ("status", "Recorded status"), ("why_matters", "Why it matters"),
        ("why_interesting", "Why it matters"), ("rivals", "Competing explanations"),
        ("latest_change", "Latest change"), ("unresolved_premise", "Unresolved premise"),
        ("next_actions", "Next actions"), ("next_action", "Next action"),
        ("owner", "Owner"), ("participants", "Participants"), ("watches", "Watches"),
        ("evidence_ids", "Recorded evidence references"),
    ):
        _field(lines, label, item.get(key))
    _evidence(lines, item.get("evidence", []))


def _exchange(lines: list[str], record: dict[str, Any]) -> None:
    metadata = record.get("metadata") if isinstance(record.get("metadata"), dict) else {}
    fields = {}
    for key in ("sender", "recipients", "visibility", "private", "message_id", "parent_message_id"):
        if key in record:
            fields[key] = record[key]
        elif key in metadata:
            fields[key] = metadata[key]
    if fields:
        lines.extend(["**Recorded exchange trace** (visibility and addressing are not inferred):", ""])
        lines.extend(_json_block(fields))


def export_inquiries(run: dict[str, Any], destination: str | Path) -> None:
    """Write Markdown plus ``destination.with_suffix('.json')`` audit companion.

    Records with aware virtual times are sorted by that time, admission sequence,
    then explicit occurrence_order/event_sequence when available. Ties retain
    posts/history/events source order. Unpositioned records are retained at the
    end, not backdated from source quotations or wall-clock logging timestamps.
    The JSON preserves all fields and original list order without mutation.
    """
    if not isinstance(run, dict) or run.get("mode") != "inquiry_swarm":
        raise ValueError("export_inquiries requires an inquiry_swarm run")
    destination = Path(destination)
    companion = destination.with_suffix(".json")
    if destination.suffix.casefold() == ".json":
        raise ValueError("Markdown destination must not have a .json extension")
    groups = [_records(run, key) for key in ("posts", "history", "events")]
    inquiries = _records(run, "inquiries")
    # Serialize before writing either output, rejecting unsupported/nonfinite data.
    audit_json = json.dumps(run, indent=2, ensure_ascii=False, allow_nan=False)
    lines = [
        "# Inquiry swarm: questions and unfolding explanations", "",
        f"Run: {_text(run.get('id', 'not recorded'))} · Model: {_text(run.get('model', 'not recorded'))} "
        f"· Status: {_text(run.get('status', 'not recorded'))}", "",
        "This is an export of recorded questions, rival explanations, actions, and changes; "
        "it assigns no discovery ranking. Exact source-text checks do not establish semantic "
        "correctness, successful outcomes, or a benefit from agent communication.", "",
        "Timeline order uses replay virtual time and arrival sequence, never dates inside "
        "quoted emails. Explicit occurrence order breaks ties when recorded; otherwise "
        "posts, history, and events retain their respective source order. Separate logs "
        "without a shared sequence do not establish exact within-cutoff interleaving. "
        "Records without an orderable replay time are listed separately.", "",
        "## Run configuration and recorded metrics", "",
    ]
    summary = {key: run[key] for key in _SUMMARY_FIELDS if key in run}
    lines.extend(_json_block(summary))
    lines.extend(["Scheduled calls, when reported, are scheduling counts rather than successful completions. "
                  "Arrived documents are not necessarily inspected documents.", "", "## Current inquiry portfolio", ""])
    for index, inquiry in enumerate(inquiries, 1):
        lines.extend([f"### Inquiry {index}", ""])
        _inquiry(lines, inquiry)
    if not inquiries:
        lines.extend(["No inquiries were recorded.", ""])
    lines.extend(["## Chronological activity and theory changes", ""])
    records = [(record, source, index) for source, group in enumerate(groups) for index, record in enumerate(group)
               if source != 2 or record.get("kind") in _SUBSTANTIVE_EVENTS]
    records.sort(key=lambda entry: _order(*entry))
    previous = None
    for record, source, _index in records:
        clock = _clock(record.get("virtual_time"))
        group = (clock, _number(record.get("arrival_sequence")))
        if group != previous:
            label = clock.isoformat() if clock else "Replay time unavailable or invalid"
            lines.extend([f"### {label} · arrival sequence {group[1] if group[1] is not None else 'not recorded'}", ""])
            previous = group
        kind = ("Post", "Inquiry revision", "Audit event")[source]
        lines.extend([f"**{kind}**", ""])
        _field(lines, "Agent", record.get("agent_id", record.get("actor", record.get("sender"))))
        action = record.get("action", record.get("kind", record.get("phase")))
        _field(lines, "Action", action.get("kind") if isinstance(action, dict) else action)
        _field(lines, "Inquiry ID", record.get("inquiry_id"))
        _field(lines, "Occurrence order", record.get("occurrence_order", record.get("event_sequence")))
        if clock is None:
            _field(lines, "Original virtual-time value", record.get("virtual_time"))
        _exchange(lines, record)
        if source == 1:
            _inquiry(lines, record)
        else:
            _field(lines, "Recorded content", record.get("text", record.get("summary", record.get("reason"))))
            rejection = record.get("reasoning_rejection", record.get("reasoning_rejected"))
            if rejection:
                _field(lines, "Reasoning rejection", rejection)
            _evidence(lines, record.get("evidence", []))
            if source == 2:
                for key in ("document_id", "question", "latest_change", "target", "participants"):
                    _field(lines, key.replace("_", " ").capitalize(), record.get(key))
    if not records:
        lines.extend(["No activity or theory changes were recorded.", ""])
    lines.extend(["## Technical audit summary", "",
                  "Telemetry stays in the complete JSON companion; these counts do not imply "
                  "successful reasoning or private knowledge unless explicitly recorded.", ""])
    counts = Counter(str(event.get("kind", "unknown")) for event in groups[2])
    if counts:
        lines.extend(_json_block(dict(sorted(counts.items()))))
    exposures: dict[str, set[str]] = defaultdict(set)
    for event in groups[2]:
        if event.get("kind") == "prompt_exposure":
            for doc in event.get("document_ids", []):
                exposures[str(event.get("agent", event.get("agent_id", "not recorded")))].add(str(doc))
    if exposures:
        lines.extend(["Unique document IDs in recorded prompt exposures, by agent:", ""])
        lines.extend(_json_block({agent: len(documents) for agent, documents in sorted(exposures.items())}))
    lines.extend(["## Complete audit companion", "",
                  f"The companion file {_text(companion.name)} preserves the complete run snapshot, "
                  "including all posts, inquiry versions, events, metadata, and their original array order.", ""])
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(lines), encoding="utf-8")
    companion.write_text(audit_json + "\n", encoding="utf-8")
