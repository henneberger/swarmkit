#!/usr/bin/env python3
"""Run paid Enron validation strictly from small tests to larger investigations.

No execution on import. Pass --live explicitly. Every request uses the existing
shared SQLite ledger; no limits, pause flags, or prior charges are reset. This
script writes only sanitized counters/run IDs to its validation report. Detailed
investigation outputs live in the forum and separately labeled dossiers.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Any

from swarmkit.enron.cli import export_markdown, load_credentials
from swarmkit.enron.corpus import EmailCorpus
from swarmkit.enron.investigate import PEERS, InvestigationConfig, Investigator
from swarmkit.enron.store import InvestigationStore, now
from swarmkit.providers.deepseek import DeepSeekClient, GateLimits, SQLiteCallGate


class PilotFailure(RuntimeError):
    """A fixed diagnostic code safe to put in a machine-readable report."""

    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--live", action="store_true", help="Authorize billed, gated validation stages")
    p.add_argument("--credentials", type=Path, default=Path(".env"))
    p.add_argument("--ledger", type=Path, default=Path("var/api-ledger.sqlite"))
    p.add_argument("--workspace", type=Path, default=Path("var/enron"))
    p.add_argument("--demo-workspace", type=Path, default=Path("var/demo"))
    p.add_argument("--manifest", type=Path, default=Path("reports/CORPUS_MANIFEST.json"))
    p.add_argument("--report", type=Path, default=Path("reports/PILOT_VALIDATION.json"))
    p.add_argument("--output-directory", type=Path, default=Path("reports"))
    p.add_argument("--query", default="approval exceptions delegated authority")
    p.add_argument("--baseline", action="store_true", help="Also run the 24-call isolated control")
    return p


def _counts(path: Path) -> tuple[int, int]:
    if not path.is_file():
        raise PilotFailure("corpus_database_missing")
    db = sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)
    try:
        count, synthetic = db.execute("SELECT COUNT(*), COALESCE(SUM(synthetic),0) FROM documents").fetchone()
        return count, synthetic
    finally:
        db.close()


def preflight(args) -> dict[str, Any]:
    if not args.live:
        raise PilotFailure("explicit_live_flag_required")
    if not args.manifest.is_file():
        raise PilotFailure("completed_corpus_manifest_required")
    raw = args.manifest.read_bytes()
    manifest = json.loads(raw)
    ingestion = manifest.get("ingestion", {})
    if ingestion.get("status") != "complete" or ingestion.get("limit", "missing") is not None:
        raise PilotFailure("full_corpus_ingestion_not_complete")
    index = manifest.get("index", {})
    if Path(index.get("database", "")).resolve() != (args.workspace / "corpus.sqlite").resolve():
        raise PilotFailure("manifest_database_mismatch")
    real_count, real_synthetic = _counts(args.workspace / "corpus.sqlite")
    if real_count <= 0 or real_synthetic or index.get("documents") != real_count:
        raise PilotFailure("actual_corpus_empty_synthetic_or_manifest_mismatch")
    demo_count, demo_synthetic = _counts(args.demo_workspace / "corpus.sqlite")
    if demo_count != 12 or demo_synthetic != 12:
        raise PilotFailure("demo_requires_exactly_twelve_fictional_documents")
    archive = manifest.get("archive", {})
    digest = archive.get("sha256", "")
    if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
        raise PilotFailure("manifest_requires_archive_sha256")
    archive_path = Path(archive.get("path", ""))
    if not archive_path.is_file() or archive_path.stat().st_size != archive.get("size_bytes"):
        raise PilotFailure("manifest_archive_missing_or_size_mismatch")
    return {
        "manifest_sha256": hashlib.sha256(raw).hexdigest(),
        "actual_documents": real_count,
        "synthetic_documents": demo_count,
        "archive_sha256": digest,
        "ingestion_status": "complete",
    }


def _save(args, report) -> None:
    args.report.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.report.with_suffix(args.report.suffix + ".tmp")
    temporary.write_text(json.dumps(report, indent=2) + "\n")
    temporary.replace(args.report)


def validate_run(run: dict, *, rounds: int) -> None:
    expected = "partial" if rounds < 6 else "completed"
    if run.get("status") != expected:
        raise PilotFailure("investigation_not_complete_for_requested_stage")
    if run.get("completed_invocations") != len(PEERS) * rounds or run.get("agent_errors"):
        raise PilotFailure("missing_or_failed_peer_invocation")
    checks = run.get("quote_checks", {})
    if checks.get("rejected", 0) or checks.get("accepted", 0) < len(PEERS):
        raise PilotFailure("invalid_or_insufficient_checked_quotations")
    if any(
        event.get("kind") in ("citation_rejected", "finding_rejected", "agent_error")
        for event in run.get("events", [])
    ):
        raise PilotFailure("rejected_citation_finding_or_agent_error")
    cited_peers = {post["agent_id"] for post in run.get("posts", []) if post.get("evidence")}
    if cited_peers != set(PEERS):
        raise PilotFailure("each_peer_must_contribute_checked_evidence")


async def run_pilot(args) -> dict[str, Any]:
    report: dict[str, Any] = {
        "created_at": now(),
        "status": "running",
        "stages": [],
        "baseline_requested": args.baseline,
        "planned_calls": 77 if args.baseline else 53,
    }
    gate = None
    current = None
    _save(args, report)
    try:
        report["preflight"] = preflight(args)
        load_credentials(args.credentials)
        # Existing ledgers retain their limits and flags. New scopes use the
        # default planning allowance; passing --live never resumes a paused scope.
        gate = (
            SQLiteCallGate(args.ledger)
            if args.ledger.exists()
            else SQLiteCallGate(
                args.ledger, limits=GateLimits(max_calls=96, max_tokens=2_000_000, max_usd=10.0), enabled=True
            )
        )
        status = gate.status()
        if not status["enabled"] or status["paused"]:
            raise PilotFailure("ledger_disabled_or_paused")
        if status["limits"]["max_calls"] - status["calls"] < report["planned_calls"]:
            raise PilotFailure("insufficient_remaining_call_budget_for_stages")
        client = DeepSeekClient(gate=gate, max_retries=0)
        report["budget_before"] = status

        current = {"stage": "json_smoke", "status": "running", "budget_before": gate.status()}
        report["stages"].append(current)
        _save(args, report)
        result = await client.complete(
            [
                {"role": "system", "content": 'Return only the JSON object {"ok":true}.'},
                {"role": "user", "content": 'Confirm JSON output with {"ok":true}.'},
            ],
            max_output_tokens=64,
            json_mode=True,
            thinking=False,
        )
        data = json.loads(result.text)
        if (
            result.finish_reason != "stop"
            or not isinstance(data, dict)
            or set(data) != {"ok"}
            or data["ok"] is not True
        ):
            raise PilotFailure("smoke_json_or_finish_reason_invalid")
        current.update(status="passed", budget_after=gate.status())
        _save(args, report)

        stages = [
            ("synthetic_small", args.demo_workspace, 1, True, False, None),
            ("synthetic_full", args.demo_workspace, 6, True, False, "SYNTHETIC_LIVE_PILOT.md"),
            ("enron_full", args.workspace, 6, False, False, "ENRON_PILOT.md"),
        ]
        if args.baseline:
            stages.append(("enron_independent", args.workspace, 6, False, True, "ENRON_BASELINE.md"))
        for name, workspace, rounds, synthetic, independent, export_name in stages:
            current = {
                "stage": name,
                "status": "running",
                "synthetic": synthetic,
                "independent": independent,
                "expected_invocations": 4 * rounds,
                "budget_before": gate.status(),
            }
            report["stages"].append(current)
            _save(args, report)
            with EmailCorpus(workspace / "corpus.sqlite") as corpus:
                store = InvestigationStore(workspace / "forum.sqlite")
                config = InvestigationConfig(
                    "approval" if synthetic else args.query,
                    rounds=rounds,
                    synthetic=synthetic,
                    independent=independent,
                )
                investigator = Investigator(corpus, store, client, config)
                current["run_id"] = investigator.id
                _save(args, report)
                run = await investigator.run()
            current.update(
                run_status=run.get("status"),
                quote_checks=run.get("quote_checks"),
                completed_invocations=run.get("completed_invocations"),
                findings=len(run.get("wiki", [])),
                errors=len(run.get("agent_errors", [])),
                budget_after=gate.status(),
            )
            if export_name:
                destination = args.output_directory / export_name
                export_markdown(run, destination)
                if synthetic:
                    destination.write_text(
                        "# LIVE MODEL TEST ON FICTIONAL EMAILS — NOT ENRON FINDINGS\n\n"
                        + destination.read_text()
                    )
                current["dossier"] = str(destination)
            validate_run(run, rounds=rounds)
            current["status"] = "passed"
            _save(args, report)
        report["status"] = "passed"
    except Exception as exc:
        report["status"] = "failed"
        report["failure"] = {
            "error_type": type(exc).__name__,
            "reason": exc.code if isinstance(exc, PilotFailure) else "stage_error",
        }
        if current is not None:
            current["status"] = "failed"
    except BaseException:
        report["status"] = "interrupted"
        if current is not None:
            current["status"] = "interrupted"
        raise
    finally:
        if gate is not None:
            report["budget_after"] = gate.status()
            if current is not None:
                current["budget_after"] = gate.status()
        report["finished_at"] = now()
        _save(args, report)
    return report


def main(argv=None) -> int:
    args = parser().parse_args(argv)
    report = asyncio.run(run_pilot(args))
    print(
        json.dumps(
            {
                "status": report["status"],
                "report": str(args.report),
                "stages": [{"stage": s["stage"], "status": s["status"]} for s in report["stages"]],
            }
        )
    )
    return 0 if report["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
