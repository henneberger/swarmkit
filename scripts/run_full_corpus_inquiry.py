#!/usr/bin/env python3
"""Run the entire dated corpus with bounded, distributed swarm work.

Credentials remain in memory. All calls share the existing ledger. This command
requires --live and never resets spending or reservations. Progress is both in
the forum and a compact JSON file, so a long run is visibly distinguishable
from an idle server. Resume preserves the original run and arrival membership.
"""
from __future__ import annotations

import argparse
import asyncio
import gzip
import json
import shutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from swarmkit.enron.cli import load_credentials  # noqa: E402
from swarmkit.enron.inquiry_experiment import InquiryExperiment, InquiryExperimentConfig  # noqa: E402
from swarmkit.enron.inquiry_report import export_inquiries  # noqa: E402
from swarmkit.enron.replay import ReplayCorpus  # noqa: E402
from swarmkit.enron.store import InvestigationStore  # noqa: E402
from swarmkit.providers.deepseek import DeepSeekClient, SQLiteCallGate  # noqa: E402


class VisibleExperiment(InquiryExperiment):
    async def _dispatch(self):
        if (ROOT / "var/enron/full-corpus-stop").exists():
            self.record["status"] = "incomplete"
            self.record["stop_reason"] = "operator_checkpoint_requested"
            self._persist()
            return False
        return await super()._dispatch()

    def _persist(self):
        self.record["metrics"]["eligible"] = self.replay.stats()["eligible"]
        super()._persist()
        stats = self.replay.stats()
        progress = {
            "id": self.id, "status": self.record["status"],
            "arrived": stats["arrived"], "total": stats["eligible"],
            "virtual_time": stats["virtual_time"],
            "metrics": self.record["metrics"],
            "updated_unix": time.time(),
        }
        path = ROOT / "var/enron/full-corpus-progress.json"
        temporary = path.with_suffix(".tmp")
        temporary.write_text(json.dumps(progress, indent=2) + "\n")
        temporary.replace(path)
        print(json.dumps(progress), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", required=True)
    parser.add_argument("--resume-run")
    args = parser.parse_args()
    load_credentials(ROOT / ".env")
    gate = SQLiteCallGate(ROOT / "var/api-ledger.sqlite")
    client = DeepSeekClient(gate=gate, max_retries=0)
    store = InvestigationStore(ROOT / "var/enron/forum.sqlite")
    config = InquiryExperimentConfig(
        batch_size=4000, max_batches=130, actions_per_batch=10,
        max_actions=1500, max_actions_per_inquiry=32,
        docs_per_agent=16, max_output_tokens=3000,
    )
    with ReplayCorpus(
        ROOT / "var/enron/corpus.sqlite",
        ROOT / "var/enron/replays/inquiry-full-corpus-v1.sqlite",
        start="1980-01-01", end="2044-12-31",
    ) as replay:
        engine = VisibleExperiment(
            replay, store, client, None if args.resume_run else config,
            resume_run_id=args.resume_run,
            peer_fact_probes=True,
        )
        try:
            result = asyncio.run(engine.run())
            export_inquiries(result, ROOT / "reports/INQUIRY_FULL_CORPUS_V1.md")
            source = ROOT / "reports/INQUIRY_FULL_CORPUS_V1.json"
            destination = source.with_suffix(".json.gz")
            temporary = destination.with_suffix(".gz.tmp")
            with source.open("rb") as incoming, temporary.open("wb") as outgoing:
                with gzip.GzipFile(filename="", mode="wb", fileobj=outgoing, mtime=0) as compressed:
                    shutil.copyfileobj(incoming, compressed)
            temporary.replace(destination)
            report = ROOT / "reports/INQUIRY_FULL_CORPUS_V1.md"
            with report.open("a") as handle:
                handle.write("\nComplete canonical records: [compressed JSON](INQUIRY_FULL_CORPUS_V1.json.gz).\n")
            print(json.dumps({k: result.get(k) for k in ("id", "status", "metrics", "errors")}))
        finally:
            gate.set_paused(True)
    return 0 if result["status"] == "completed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
