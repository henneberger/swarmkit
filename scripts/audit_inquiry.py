#!/usr/bin/env python3
"""Read-only inquiry provenance audit; never a semantic/discovery certification.

Checks exact quotes/hashes and date+sequence visibility using actual replay
membership. Audits posts, addressed-message events, every historical artifact
version, and recorded prompt/search/read exposure. Does not infer unlogged access.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from swarmkit.enron.investigate import evidence_view  # noqa: E402
from swarmkit.serialization import from_data  # noqa: E402
from swarmkit.types import SwarmState  # noqa: E402

spec = importlib.util.spec_from_file_location("_inquiry_base_audit", ROOT / "scripts" / "audit_replay.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def audit(run, corpus_path, replay_path):
    failures, rows, labels = [], [], []
    counts = {"posts": 0, "peer_messages": 0, "artifact_versions": 0}

    def add(row, category, index):
        counts[category] += 1
        rows.append(row)
        labels.append({"category": category, "index": index})

    for i, post in enumerate(run.get("posts", [])):
        add(post, "posts", i)
    snapshot = None
    try:
        snapshot = from_data(run["state_snapshot"])
        if not isinstance(snapshot, SwarmState):
            raise ValueError("snapshot is not SwarmState")
    except (KeyError, ValueError, TypeError):
        failures.append({"reason": "missing_or_invalid_canonical_state_snapshot"})
    messages = {m.id: m for m in snapshot.messages} if snapshot else {}
    for i, event in enumerate(run.get("events", [])):
        if event.get("kind") != "peer_message":
            continue
        if not isinstance(event.get("evidence"), list):
            failures.append({"category": "peer_messages", "index": i, "reason": "missing_peer_evidence_list"})
            continue
        add(event, "peer_messages", i)
        actual = messages.get(event.get("message_id"))
        if actual is None:
            failures.append(
                {"category": "peer_messages", "index": i, "reason": "message_missing_from_snapshot"}
            )
        elif (
            actual.sender != event.get("sender")
            or list(actual.recipients) != event.get("recipients")
            or json.loads(json.dumps([evidence_view(e) for e in actual.evidence], allow_nan=False)) != event["evidence"]
        ):
            failures.append({"category": "peer_messages", "index": i, "reason": "message_snapshot_mismatch"})
    seen_artifacts = set()
    for i, row in enumerate(run.get("history", [])):
        aid = row.get("artifact_id")
        artifact = snapshot.artifacts.get(aid) if snapshot else None
        if artifact is None:
            failures.append(
                {"category": "artifact_versions", "index": i, "reason": "missing_historical_artifact"}
            )
            continue
        if aid in seen_artifacts:
            failures.append(
                {"category": "artifact_versions", "index": i, "reason": "duplicate_artifact_history"}
            )
        seen_artifacts.add(aid)
        if artifact.content != row or list(row.get("evidence_ids", [])) != [e.id for e in artifact.evidence]:
            failures.append(
                {"category": "artifact_versions", "index": i, "reason": "artifact_history_mismatch"}
            )
        add({**row, "evidence": [evidence_view(e) for e in artifact.evidence]}, "artifact_versions", i)
    if snapshot:
        missing = {a.id for a in snapshot.artifacts.values() if "inquiry" in a.tags} - seen_artifacts
        if missing:
            failures.append(
                {"reason": "artifact_versions_missing_from_history", "artifact_ids": sorted(missing)}
            )
    # Normalize the runner's list-shaped historical_read record to legacy auditor.
    events = []
    for event in run.get("events", []):
        if event.get("kind") == "historical_read" and "document_ids" in event:
            ids = event["document_ids"]
            if not isinstance(ids, list):
                failures.append({"reason": "malformed_read_document_ids"})
                continue
            for doc_id in ids:
                events.append({**event, "document_id": doc_id})
        else:
            events.append(event)
    result = base.audit({"posts": rows, "events": events}, corpus_path, replay_path)
    for failure in result["failures"]:
        if failure["reason"] == "no_evidence_bearing_posts_to_audit":
            continue  # Abstention can be valid; report absence explicitly below.
        failure = dict(failure)
        if "post" in failure:
            failure.update(labels[failure.pop("post")])
        failures.append(failure)
    sequence_rows = [*run.get("posts", []), *run.get("events", []), *run.get("history", [])]
    sequence_values = [r.get("event_sequence") for r in sequence_rows]
    if any(type(s) is not int or s < 1 for s in sequence_values):
        failures.append({"reason": "missing_or_invalid_event_sequence"})
    elif len(sequence_values) != len(set(sequence_values)):
        failures.append({"reason": "duplicate_global_event_sequence"})
    else:
        last = 0
        for row in sorted(sequence_rows, key=lambda r: r["event_sequence"]):
            seq = row.get("arrival_sequence")
            if type(seq) is not int or seq < last:
                failures.append(
                    {"reason": "nonmonotonic_arrival_watermark", "event_sequence": row["event_sequence"]}
                )
                break
            last = seq
    result.update(
        passed=not failures,
        failures=failures,
        checked_records=counts,
        citation_audit_available=result["checked_citations"] > 0,
        scope="Recorded posts, addressed-message evidence, historical artifact quotes/hashes; prompt/search/read visibility by outer date and exact arrival sequence; snapshot/history linkage.",
        limitations="No semantic entailment, interestingness, independent corroboration, successful discovery, unrecorded access, model-prior contamination, or complete private-context isolation certification.",
    )
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("run", "corpus", "replay"):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    result = audit(json.loads(a.run.read_text()), a.corpus, a.replay)
    text = json.dumps(result, indent=2) + "\n"
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text)
    print(text, end="")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
