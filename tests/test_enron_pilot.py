"""Pilot stage-order checks with entirely fake provider/investigation backends."""

import json
import sqlite3
from dataclasses import asdict
from types import SimpleNamespace

import pytest

from scripts import run_enron_pilot as pilot
from swarmkit.providers.deepseek import GateLimits


@pytest.fixture
def fake_pipeline(tmp_path, monkeypatch):
    calls = {"network": 0, "runs": [], "bad_stage": None, "bad_smoke": False}

    class Gate:
        def __init__(self, *args, **kwargs):
            self.limits = kwargs.get("limits", GateLimits(max_calls=96, max_tokens=2_000_000, max_usd=10))

        def status(self):
            return {
                "enabled": True,
                "paused": False,
                "limits": asdict(self.limits),
                "calls": calls["network"],
                "tokens": calls["network"] * 10,
                "cost_usd": 0.01,
            }

    class Client:
        def __init__(self, **kwargs):
            pass

        async def complete(self, *args, **kwargs):
            assert kwargs["max_output_tokens"] == 64
            calls["network"] += 1
            return SimpleNamespace(text="bad" if calls["bad_smoke"] else '{"ok":true}', finish_reason="stop")

    class Corpus:
        def __init__(self, *args):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

    class Investigator:
        def __init__(self, corpus, store, client, config):
            self.config = config
            self.id = "run-" + str(len(calls["runs"]))

        async def run(self):
            calls["runs"].append(self.config)
            count = 4 * self.config.rounds
            calls["network"] += count
            bad = len(calls["runs"]) == calls["bad_stage"]
            return {
                "status": "partial" if self.config.rounds == 1 else "completed",
                "completed_invocations": count,
                "agent_errors": [],
                "events": [],
                "wiki": [],
                "quote_checks": {"accepted": 4, "rejected": int(bad)},
                "posts": [{"agent_id": agent, "evidence": [1]} for agent in pilot.PEERS],
            }

    monkeypatch.setattr(pilot, "preflight", lambda _: {"ingestion_status": "complete"})
    monkeypatch.setattr(pilot, "load_credentials", lambda _: None)
    monkeypatch.setattr(pilot, "SQLiteCallGate", Gate)
    monkeypatch.setattr(pilot, "DeepSeekClient", Client)
    monkeypatch.setattr(pilot, "EmailCorpus", Corpus)
    monkeypatch.setattr(pilot, "InvestigationStore", lambda _: None)
    monkeypatch.setattr(pilot, "Investigator", Investigator)

    def export(run, destination):
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text("test dossier")

    monkeypatch.setattr(pilot, "export_markdown", export)
    args = pilot.parser().parse_args(
        [
            "--live",
            "--report",
            str(tmp_path / "validation.json"),
            "--ledger",
            str(tmp_path / "ledger.sqlite"),
            "--output-directory",
            str(tmp_path / "reports"),
        ]
    )
    return args, calls


async def test_all_stages_order_and_optional_baseline(fake_pipeline):
    args, calls = fake_pipeline
    args.baseline = True
    report = await pilot.run_pilot(args)
    assert report["status"] == "passed"
    assert calls["network"] == 77
    assert [(c.rounds, c.synthetic, c.independent) for c in calls["runs"]] == [
        (1, True, False),
        (6, True, False),
        (6, False, False),
        (6, False, True),
    ]
    assert all(stage["status"] == "passed" for stage in report["stages"])
    assert (args.output_directory / "ENRON_PILOT.md").exists()
    assert "FICTIONAL EMAILS" in (args.output_directory / "SYNTHETIC_LIVE_PILOT.md").read_text()
    assert json.loads(args.report.read_text())["status"] == "passed"


async def test_bad_smoke_never_runs_investigators(fake_pipeline):
    args, calls = fake_pipeline
    calls["bad_smoke"] = True
    report = await pilot.run_pilot(args)
    assert report["status"] == "failed"
    assert calls["network"] == 1
    assert calls["runs"] == []


@pytest.mark.parametrize("failed_stage,expected_calls", [(1, 5), (2, 29), (3, 53)])
async def test_rejected_citation_blocks_every_larger_stage(fake_pipeline, failed_stage, expected_calls):
    args, calls = fake_pipeline
    args.baseline = True
    calls["bad_stage"] = failed_stage
    report = await pilot.run_pilot(args)
    assert report["status"] == "failed"
    assert report["failure"]["reason"] == "invalid_or_insufficient_checked_quotations"
    assert calls["network"] == expected_calls
    assert len(calls["runs"]) == failed_stage


def test_preflight_requires_complete_matching_real_and_fictional_corpora(tmp_path):
    args = pilot.parser().parse_args(
        [
            "--live",
            "--workspace",
            str(tmp_path / "actual"),
            "--demo-workspace",
            str(tmp_path / "demo"),
            "--manifest",
            str(tmp_path / "manifest.json"),
        ]
    )
    for workspace, count, synthetic in [(args.workspace, 3, 0), (args.demo_workspace, 12, 1)]:
        workspace.mkdir()
        with sqlite3.connect(workspace / "corpus.sqlite") as db:
            db.execute("CREATE TABLE documents(synthetic INTEGER)")
            db.executemany("INSERT INTO documents VALUES (?)", [(synthetic,)] * count)
    archive = tmp_path / "archive.tar.gz"
    archive.write_bytes(b"fixture")
    manifest = {
        "ingestion": {"status": "in_progress", "limit": None},
        "index": {"database": str(args.workspace / "corpus.sqlite"), "documents": 3},
        "archive": {"path": str(archive), "size_bytes": 7, "sha256": "a" * 64},
    }
    args.manifest.write_text(json.dumps(manifest))
    with pytest.raises(pilot.PilotFailure, match="not_complete"):
        pilot.preflight(args)
    manifest["ingestion"]["status"] = "complete"
    args.manifest.write_text(json.dumps(manifest))
    assert pilot.preflight(args)["actual_documents"] == 3
    manifest["index"]["documents"] = 99
    args.manifest.write_text(json.dumps(manifest))
    with pytest.raises(pilot.PilotFailure, match="manifest_mismatch"):
        pilot.preflight(args)
