"""Enron app: ingest, investigate, inspect a local forum, and export a dossier."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import urllib.request
from dataclasses import asdict, replace
from pathlib import Path

from .corpus import EmailCorpus
from .investigate import PEERS, InvestigationConfig, Investigator, OfflineClient
from .store import InvestigationStore

CORPUS_URL = "https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz"


def load_credentials(path: Path) -> None:
    """Read only DEEPSEEK_API_KEY; never source shell code or print credentials."""
    if not os.environ.get("DEEPSEEK_API_KEY") and os.environ.get("DEEPSEEK_API"):
        os.environ["DEEPSEEK_API_KEY"] = os.environ["DEEPSEEK_API"]
    if os.environ.get("DEEPSEEK_API_KEY") or not path.exists():
        return
    for line in path.read_text().splitlines():
        name, sep, value = line.strip().partition("=")
        if sep and name.strip() == "DEEPSEEK_API_KEY":
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            if value:
                os.environ["DEEPSEEK_API_KEY"] = value
            return


def export_markdown(run: dict, destination: Path):
    if run.get('mode') == 'inquiry_swarm':
        from .inquiry_report import export_inquiries
        return export_inquiries(run, destination)
    if run.get('mode') in ('chronological', 'chronological_replay') or run.get('experiment') == 'chronological_tacit_knowledge':
        from .chronicle import export_chronicle
        return export_chronicle(run, destination)
    lines = [
        f"# Investigation: {run['query']}",
        "",
        f"Run `{run['id']}` · model `{run['model']}` · status **{run['status']}**",
        "",
        "**All interpretations are provisional and require independent review.** "
        "Citation checks confirm quoted text, not the truth of an assertion or fraud.",
        "",
        "## Scope and resource use",
        "",
        "```json",
        json.dumps(
            {
                k: run.get(k)
                for k in ("config", "quote_checks", "queries", "unique_documents", "runtime_usage")
            },
            indent=2,
        ),
        "```",
        "",
        "## Cases and knowledge cards",
        "",
    ]
    if not run.get("wiki"):
        lines += ["No supported candidate cards were published. Inspect the forum and run errors.", ""]
    for card in run.get("wiki", []):
        lines += [
            f"### {card['title']}",
            "",
            card["text"],
            "",
            f"Alternative: {card.get('alternative', '')}",
            "",
            f"Missing evidence: {card.get('missing_evidence', '')}",
            "",
            f"Next test: {card.get('next_test', '')}",
            "",
        ]
        for evidence in card.get("evidence", []):
            lines += [
                f"Source `{evidence['document_id']}`; origin `{evidence['source']}`.",
                "",
                "> " + evidence["quote"].replace("\n", "\n> "),
                "",
            ]
    lines += ["## Forum", ""]
    for post in run.get("posts", []):
        lines += [f"### {post['phase']} / {post['agent_id']}", "", post["text"], ""]
        for evidence in post.get("evidence", []):
            lines += [
                f"Source `{evidence['document_id']}` — exact quotation checked; interpretation unreviewed.",
                "",
                "> " + evidence["quote"].replace("\n", "\n> "),
                "",
            ]
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(lines))


def parser():
    p = argparse.ArgumentParser(prog="swarmkit-enron")
    p.add_argument("--workspace", type=Path, default=Path("var/enron"))
    p.add_argument(
        "--ledger",
        type=Path,
        default=Path("var/api-ledger.sqlite"),
        help="Shared API budget ledger across all corpus workspaces",
    )
    sub = p.add_subparsers(dest="command", required=True)
    fetch = sub.add_parser("fetch", help="Download the official CMU release (about 1.7 GB)")
    fetch.add_argument("--output", type=Path, default=Path("data/enron/enron_mail_20150507.tar.gz"))
    ingest = sub.add_parser("ingest")
    ingest.add_argument("source", type=Path)
    ingest.add_argument("--limit", type=int)
    run = sub.add_parser("run")
    run.add_argument("--query", required=True)
    run.add_argument("--cutoff", help="ISO date/time historical observation cutoff")
    run.add_argument(
        "--live", action="store_true", help="Explicitly authorize this run to dispatch billed API calls"
    )
    run.add_argument("--synthetic", action="store_true", help="Label a fixture-corpus run synthetic")
    run.add_argument("--independent", action="store_true", help="Disable peer messages for a baseline")
    run.add_argument("--rounds", type=int, default=6)
    run.add_argument("--credentials", type=Path, default=Path(".env"))
    run.add_argument("--max-calls", type=int, default=96)
    run.add_argument("--max-tokens", type=int, default=2_000_000)
    run.add_argument("--max-usd", type=float, default=10.0)
    run.add_argument("--export", type=Path)
    inquiry = sub.add_parser("inquire", help="Agent-directed investigations of chronological arrivals")
    inquiry.add_argument("--replay-id", required=True)
    inquiry.add_argument("--start", default="1999-01-01")
    inquiry.add_argument("--end", default="2002-12-31")
    inquiry.add_argument("--batch-size", type=int, default=20)
    inquiry.add_argument("--max-batches", type=int, default=4)
    inquiry.add_argument("--actions-per-batch", type=int, default=4)
    inquiry.add_argument("--max-actions", type=int, default=16)
    inquiry.add_argument("--docs-per-agent", type=int, default=3)
    inquiry.add_argument("--max-output-tokens", type=int, default=1800)
    inquiry.add_argument("--live", action="store_true", required=True)
    inquiry.add_argument("--withhold-peer-exchange", action="store_true",
                         help="Withhold peer messages and merged inquiry context; public questions/coverage remain visible")
    inquiry.add_argument("--credentials", type=Path, default=Path(".env"))
    inquiry.add_argument("--export", type=Path)
    replay = sub.add_parser("replay", help="Infer tacit knowledge from chronologically arriving emails")
    replay.add_argument("--replay-id", required=True, help="Unique name for persisted arrival membership")
    replay.add_argument("--start", default="1999-01-01")
    replay.add_argument("--end", default="2002-12-31")
    replay.add_argument("--batch-size", type=int, default=22000)
    replay.add_argument("--max-windows", type=int, default=24)
    replay.add_argument("--turns-per-window", type=int, default=2)
    replay.add_argument("--documents-per-window", type=int, default=32)
    replay.add_argument("--max-output-tokens", type=int, default=3000)
    replay.add_argument("--live", action="store_true")
    replay.add_argument("--synthetic", action="store_true")
    replay.add_argument("--credentials", type=Path, default=Path(".env"))
    replay.add_argument("--export", type=Path)
    serve = sub.add_parser("serve")
    serve.add_argument("--port", type=int, default=8765)
    sub.add_parser("status")
    budget = sub.add_parser(
        "budget", help="Explicitly update existing ledger caps without resetting usage or flags"
    )
    budget.add_argument("--max-calls", type=int)
    budget.add_argument("--max-tokens", type=int)
    budget.add_argument("--max-usd", type=float)
    export = sub.add_parser("export")
    export.add_argument("run_id")
    export.add_argument("output", type=Path)
    return p


def main(argv=None):
    args = parser().parse_args(argv)
    args.workspace.mkdir(parents=True, exist_ok=True)
    corpus_path = args.workspace / "corpus.sqlite"
    store = InvestigationStore(args.workspace / "forum.sqlite")
    if args.command == "fetch":
        args.output.parent.mkdir(parents=True, exist_ok=True)
        if args.output.exists():
            raise SystemExit("Output exists; ingest it or choose another path. Existing data was preserved.")
        partial = args.output.with_suffix(args.output.suffix + ".partial")
        with urllib.request.urlopen(CORPUS_URL, timeout=120) as response, partial.open("wb") as target:
            while chunk := response.read(1024 * 1024):
                target.write(chunk)
        partial.replace(args.output)
        print(str(args.output))
        return
    if args.command == "ingest":
        with EmailCorpus(corpus_path) as corpus:
            stats = (
                corpus.ingest_directory(args.source, limit=args.limit)
                if args.source.is_dir()
                else corpus.ingest_tar(args.source, limit=args.limit)
            )
            print(json.dumps(asdict(stats), indent=2))
        return
    from swarmkit.providers.deepseek import DeepSeekClient, GateLimits, SQLiteCallGate

    ledger = args.ledger
    if args.command == "inquire":
        from .inquiry_experiment import InquiryExperiment, InquiryExperimentConfig
        from .replay import ReplayCorpus
        if not args.replay_id or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_' for c in args.replay_id):
            raise SystemExit("Replay ID must contain only letters, digits, hyphens, or underscores.")
        load_credentials(args.credentials)
        if not os.environ.get("DEEPSEEK_API_KEY"):
            raise SystemExit("Set DEEPSEEK_API_KEY or DEEPSEEK_API in the environment.")
        gate = (SQLiteCallGate(ledger) if ledger.exists() else
                SQLiteCallGate(ledger, limits=GateLimits(max_calls=240, max_tokens=5_000_000,
                                                       max_usd=10), enabled=True))
        # Reusing a ledger never unpauses it or resets prior spend.
        client = DeepSeekClient(gate=gate, max_retries=0)
        config = InquiryExperimentConfig(batch_size=args.batch_size, max_batches=args.max_batches,
            actions_per_batch=args.actions_per_batch, max_actions=args.max_actions,
            docs_per_agent=args.docs_per_agent, max_output_tokens=args.max_output_tokens,
            peer_exchange=not args.withhold_peer_exchange)
        with ReplayCorpus(corpus_path, args.workspace / 'replays' / (args.replay_id + '.sqlite'),
                          start=args.start, end=args.end) as view:
            engine = InquiryExperiment(view, store, client, config)
            print(f"Inquiry swarm {engine.id}; arrival state {args.replay_id}", flush=True)
            result = asyncio.run(engine.run())
        if args.export:
            export_markdown(result, args.export)
        print(json.dumps({k: result.get(k) for k in ('id', 'status', 'metrics', 'runtime_usage')}, indent=2))
        if result['status'] in ('failed', 'incomplete', 'interrupted'):
            raise SystemExit(2)
        return
    if args.command == "replay":
        from .chronicle import export_chronicle
        from .replay import ReplayCorpus
        from .stream import ChronologicalSwarm, StreamConfig, StreamOfflineClient
        if not args.replay_id or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_' for c in args.replay_id):
            raise SystemExit("Replay ID must contain only letters, digits, hyphens, or underscores.")
        if args.live:
            load_credentials(args.credentials)
            if not os.environ.get("DEEPSEEK_API_KEY"):
                raise SystemExit("Set DEEPSEEK_API_KEY or DEEPSEEK_API in the environment.")
            gate = (SQLiteCallGate(ledger) if ledger.exists() else
                    SQLiteCallGate(ledger, limits=GateLimits(max_calls=240, max_tokens=5_000_000,
                                                           max_usd=10), enabled=True))
            client = DeepSeekClient(gate=gate)
        else:
            if not args.synthetic:
                raise SystemExit("Offline replay requires --synthetic; use --live for real inference.")
            client = StreamOfflineClient()
        config = StreamConfig(batch_size=args.batch_size, max_windows=args.max_windows,
                              turns_per_window=args.turns_per_window,
                              documents_per_window=args.documents_per_window,
                              max_output_tokens=args.max_output_tokens, synthetic=args.synthetic)
        with ReplayCorpus(corpus_path, args.workspace / 'replays' / (args.replay_id + '.sqlite'),
                          start=args.start, end=args.end) as view:
            engine = ChronologicalSwarm(view, store, client, config)
            print(f"Chronological replay {engine.id}; arrival state {args.replay_id}", flush=True)
            result = asyncio.run(engine.run())
        if args.export:
            export_chronicle(result, args.export)
        print(json.dumps({k: v for k, v in result.items() if k not in ('posts', 'events', 'wiki')}, indent=2))
        if result['status'] not in ('completed', 'completed_with_rejections', 'partial'):
            raise SystemExit(2)
        return
    if args.command == "budget":
        if not ledger.exists():
            raise SystemExit("No existing ledger; initialize it with a live run first.")
        gate = SQLiteCallGate(ledger)
        current = gate.limits
        changes = {
            key: getattr(args, key)
            for key in ("max_calls", "max_tokens", "max_usd")
            if getattr(args, key) is not None
        }
        if changes:
            gate.set_limits(replace(current, **changes), expected=current)
        print(json.dumps({"gate": gate.status(), "limits_history": gate.limits_history()}, indent=2))
        return
    if args.command == "run":
        config = InvestigationConfig(
            args.query,
            cutoff=args.cutoff,
            rounds=args.rounds,
            independent=args.independent,
            synthetic=args.synthetic,
        )
        if args.live:
            load_credentials(args.credentials)
            if not os.environ.get("DEEPSEEK_API_KEY"):
                raise SystemExit("Set DEEPSEEK_API_KEY in the environment or ignored credential file.")
            limits = GateLimits(max_calls=args.max_calls, max_tokens=args.max_tokens, max_usd=args.max_usd)
            gate = (
                SQLiteCallGate(ledger)
                if ledger.exists()
                else SQLiteCallGate(ledger, limits=limits, enabled=True)
            )
            # Run flags initialize new ledgers; use budget for explicit cap changes.
            # Existing pause/disable is deliberately preserved. --live never resumes a paused ledger.
            client = DeepSeekClient(gate=gate)
        else:
            if not args.synthetic:
                raise SystemExit("Offline runs require --synthetic; use --live for real investigation.")
            client = OfflineClient()
        with EmailCorpus(corpus_path) as corpus:
            investigator = Investigator(corpus, store, client, config)
            print(
                f"Run {investigator.id}; inspect with swarmkit-enron --workspace {args.workspace} serve",
                flush=True,
            )
            run = asyncio.run(investigator.run())
        if args.export:
            export_markdown(run, args.export)
        print(json.dumps({k: v for k, v in run.items() if k not in ("posts", "wiki", "events")}, indent=2))
        if run["status"] not in ("completed", "partial"):
            raise SystemExit(2)
        return
    if args.command == "export":
        run = store.run(args.run_id)
        if run is None:
            raise SystemExit("Unknown run ID")
        export_markdown(run, args.output)
        return
    # Opening a monitor before a live run must not create a disabled ledger with
    # different default limits. Only inspect an existing ledger here.
    gate = SQLiteCallGate(ledger) if ledger.exists() else None

    def status():
        current_gate = gate or (SQLiteCallGate(ledger) if ledger.exists() else None)
        state = current_gate.status() if current_gate else {"enabled": False, "paused": False, "calls": 0}
        runs = store.runs()
        state["budget"] = dict(state)
        state["budget"]["limit"] = state.get("limits", {}).get("max_tokens")
        state["pause_enabled"] = current_gate is not None
        state["status"] = "idle"
        state["run_id"] = runs[0]["id"] if runs else None
        state["status"] = runs[0]["status"] if runs else "idle"
        peers = runs[0].get("peers", PEERS) if runs else PEERS
        peer_ids = [peer["id"] if isinstance(peer, dict) else peer for peer in peers]
        state["peers"] = [
            {"id": key, "name": key.title(), "status": runs[0]["status"] if runs else "idle"}
            for key in peer_ids
        ]
        return state

    if args.command == "status":
        print(json.dumps({"gate": status(), "runs": store.runs()}, indent=2))
        return
    from .web import create_server

    def document(doc_id):
        with EmailCorpus(corpus_path) as corpus:
            doc = corpus.get(doc_id)
            if doc is None:
                return None
            result = asdict(doc)
            result['segments'] = [asdict(segment) for segment in corpus.segments(doc_id)]
            return result

    def search(query):
        with EmailCorpus(corpus_path) as corpus:
            # Reports expose immutable IDs; let human reviewers paste one directly.
            if query.strip().startswith('mail-'):
                exact = corpus.get(query.strip())
                if exact is not None:
                    return [asdict(exact)]
            return [asdict(doc) for doc in corpus.search(query, limit=20)]

    def set_paused(paused):
        current_gate = gate or (SQLiteCallGate(ledger) if ledger.exists() else None)
        if current_gate:
            current_gate.set_paused(paused)
        return status()

    server = create_server(
        host="127.0.0.1",
        port=args.port,
        status=status,
        runs=store.runs,
        run=store.run,
        document=document,
        search=search,
        set_paused=set_paused,
    )
    print(f"Forum: http://127.0.0.1:{server.server_address[1]}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
