#!/usr/bin/env python3
"""Read-only exact-quote and arrival-time audit of a replay run JSON export.

Requires each evidence-bearing post to record virtual_time and arrival_sequence
(or arrived_count). A date alone cannot certify equal-timestamp arrival isolation.
This checks provenance/visibility only, never historical truth or inference quality.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


def _utc(value):
    if not isinstance(value, str):
        raise ValueError("missing UTC timestamp")
    date = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if date.tzinfo is None or date.utcoffset() is None:
        raise ValueError("timezone required")
    return date.astimezone(timezone.utc)


def audit(run, corpus_path, replay_path):
    corpus = sqlite3.connect(Path(corpus_path).resolve().as_uri() + "?mode=ro", uri=True)
    corpus.row_factory = sqlite3.Row
    replay = sqlite3.connect(Path(replay_path).resolve().as_uri() + "?mode=ro", uri=True)
    failures = []
    checked = 0
    documents = {}
    evidence_posts = 0
    checked_exposure_events = checked_exposure_documents = 0
    event_types = {}
    exposed_documents = {}
    try:
        for index, post in enumerate(run.get("posts", [])):
            citations = post.get("evidence", [])
            if not citations:
                continue
            evidence_posts += 1
            try:
                cutoff = _utc(post.get("virtual_time"))
            except ValueError:
                failures.append({"post": index, "reason": "missing_or_invalid_virtual_time"})
                continue
            sequence = post.get("arrival_sequence", post.get("arrived_count"))
            if isinstance(sequence, bool) or not isinstance(sequence, int) or sequence < 0:
                failures.append({"post": index, "reason": "missing_or_invalid_arrival_sequence"})
                continue
            for number, evidence in enumerate(citations):
                checked += 1
                meta = evidence.get("metadata", {})
                doc_id = evidence.get("document_id", meta.get("document_id"))
                reason = None
                if doc_id not in documents:
                    documents[doc_id] = corpus.execute(
                        "SELECT body,date_utc,body_sha256,raw_sha256,raw FROM documents WHERE id=?", (doc_id,)
                    ).fetchone()
                doc = documents[doc_id]
                arrival = replay.execute(
                    "SELECT sequence,date_utc FROM arrived WHERE doc_id=?", (doc_id,)
                ).fetchone()
                if doc is None:
                    reason = "unknown_document"
                elif arrival is None or arrival[0] > sequence:
                    reason = "not_arrived_at_post_sequence"
                else:
                    try:
                        if _utc(doc["date_utc"]) > cutoff or _utc(arrival[1]) > cutoff:
                            reason = "future_outer_date"
                    except ValueError:
                        reason = "unknown_outer_date"
                if reason is None:
                    start, end = meta.get("start"), meta.get("end")
                    quote = evidence.get("quote", meta.get("quote"))
                    if (
                        isinstance(start, bool)
                        or isinstance(end, bool)
                        or not isinstance(start, int)
                        or not isinstance(end, int)
                        or not 0 <= start < end <= len(doc["body"])
                    ):
                        reason = "invalid_offsets"
                    elif doc["body"][start:end] != quote:
                        reason = "quote_mismatch"
                    elif hashlib.sha256(doc["body"].encode()).hexdigest() != doc["body_sha256"]:
                        reason = "body_hash_mismatch"
                    elif hashlib.sha256(doc["raw"]).hexdigest() != doc["raw_sha256"]:
                        reason = "raw_hash_mismatch"
                    elif (
                        meta.get("body_sha256") != doc["body_sha256"]
                        or meta.get("raw_sha256") != doc["raw_sha256"]
                    ):
                        reason = "evidence_hash_mismatch"
                if reason:
                    failures.append(
                        {"post": index, "evidence": number, "document_id": doc_id, "reason": reason}
                    )
        for index, event in enumerate(run.get("events", [])):
            kind = event.get("kind")
            if kind not in ("prompt_exposure", "historical_retrieval", "historical_read"):
                continue
            checked_exposure_events += 1
            event_types[kind] = event_types.get(kind, 0) + 1
            try:
                cutoff = _utc(event.get("virtual_time"))
            except (ValueError, TypeError):
                failures.append({"event": index, "kind": kind, "reason": "missing_or_invalid_virtual_time"})
                continue
            sequence = event.get("arrival_sequence")
            if type(sequence) is not int or sequence < 0:
                failures.append(
                    {"event": index, "kind": kind, "reason": "missing_or_invalid_arrival_sequence"}
                )
                continue
            ids = [event.get("document_id")] if kind == "historical_read" else event.get("document_ids")
            if not isinstance(ids, list):
                failures.append({"event": index, "kind": kind, "reason": "missing_document_ids"})
                continue
            for doc_id in ids:
                checked_exposure_documents += 1
                reason = None
                if not isinstance(doc_id, str) or not doc_id:
                    failures.append({"event": index, "kind": kind, "reason": "invalid_document_id"})
                    continue
                if doc_id not in exposed_documents:
                    exposed_documents[doc_id] = corpus.execute(
                        "SELECT date_utc,length(body) FROM documents WHERE id=?", (doc_id,)
                    ).fetchone()
                doc = exposed_documents[doc_id]
                arrival = replay.execute(
                    "SELECT sequence,date_utc FROM arrived WHERE doc_id=?", (doc_id,)
                ).fetchone()
                if doc is None:
                    reason = "unknown_document"
                elif arrival is None or arrival[0] > sequence:
                    reason = "not_arrived_at_event_sequence"
                else:
                    try:
                        if _utc(doc[0]) > cutoff or _utc(arrival[1]) > cutoff:
                            reason = "future_outer_date"
                    except (ValueError, TypeError):
                        reason = "unknown_outer_date"
                if reason is None and kind == "historical_read":
                    offset = event.get("offset")
                    if type(offset) is not int or not 0 <= offset < doc[1]:
                        reason = "invalid_read_offset"
                if reason:
                    failures.append({"event": index, "kind": kind, "document_id": doc_id, "reason": reason})
        if not evidence_posts:
            failures.append({"reason": "no_evidence_bearing_posts_to_audit"})
    finally:
        corpus.close()
        replay.close()
    return {
        "passed": not failures,
        "evidence_posts": evidence_posts,
        "checked_citations": checked,
        "unique_documents": len(documents),
        "failures": failures,
        "checked_exposure_events": checked_exposure_events,
        "checked_exposure_documents": checked_exposure_documents,
        "unique_exposure_documents": len(exposed_documents),
        "exposure_event_types": event_types,
        "exposure_audit_available": bool(checked_exposure_events),
        "scope": "post quotes/hashes and recorded prompt/search/read document visibility by outer date and exact arrival sequence",
        "limitations": "Checks recorded audit events, not unrecorded access, uncited prose, model prior knowledge, truth, or inference quality.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--replay", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit(json.loads(args.run.read_text()), args.corpus, args.replay)
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
