"""Frozen, resumable integrated model-agent experiment; real API calls are opt-in via this CLI."""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import itertools
import json
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np

from ..benchmarks import ChannelConfig
from ..economics import AlphaRankEvaluator, PolicySpaceResponseOracles
from ..providers.deepseek import DeepSeekClient, GateLimits, SQLiteCallGate
from .experiment import FoundryConfig, FoundryExperiment
from .model_agents import PROTOCOLS, SYSTEM, ModelScientist, encode
from .world import FoundryWorld


def cases(seeds=(1101, 1102, 1103)):
    result = []
    for seed, incentive, pressure, protocol in itertools.product(
        seeds, ("shared", "private"), ("stable", "disrupted"), (*PROTOCOLS, "silent")
    ):
        result.append(
            dict(
                id=f"primary-{seed}-{incentive}-{pressure}-{protocol}",
                kind="primary",
                seed=seed,
                incentive=incentive,
                pressure=pressure,
                protocol=protocol,
            )
        )
    for seed, incentive in itertools.product(seeds, ("shared", "private")):
        parent = f"primary-{seed}-{incentive}-disrupted-targeted"
        for kind in ("artifacts_off", "message_removed"):
            result.append(
                dict(
                    id=f"{kind}-{seed}-{incentive}",
                    kind=kind,
                    seed=seed,
                    incentive=incentive,
                    pressure="disrupted",
                    protocol="targeted",
                    parent=parent,
                )
            )
    for seed, pair in itertools.product(seeds, (("broadcast", "targeted"), ("targeted", "broadcast"))):
        result.append(
            dict(
                id=f"crossplay-{seed}-{pair[0]}-{pair[1]}",
                kind="crossplay",
                seed=seed,
                incentive="private",
                pressure="disrupted",
                protocol=pair[0],
                partners=list(pair),
            )
        )
    return result


def settings(case):
    disrupted = case["pressure"] == "disrupted"
    world = FoundryWorld(
        seed=case["seed"],
        split=case.get("split", "test"),
        firms=2,
        components=2,
        generations=4,
        change_every=2 if disrupted else 99,
    )
    cfg = FoundryConfig(
        rounds=4,
        incentives=case["incentive"],
        agent_teams=True,
        agent_publication=True,
        agent_concurrency=6,
        artifact_visibility="public",
        forecast_market=True,
        channel=ChannelConfig(
            max_messages=24,
            max_bytes=40000,
            loss=0.1 if disrupted else 0,
            disabled=case["protocol"] == "silent",
        ),
        equipment_slots=1 if disrupted else 2,
        turnover=0.5 if disrupted else 0,
        research_budget=12,
        production_budget=8,
        trust_reported_usage=True,
        artifacts=case["kind"] != "artifacts_off",
        pooled=case.get("pooled", False),
    )
    return world, cfg


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(".tmp")
    temp.write_text(json.dumps(obj, indent=2, allow_nan=False, default=sorted) + "\n")
    temp.replace(path)


def freeze(directory, plan, phase):
    root = Path(__file__).resolve().parents[1]
    hashes = {
        str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(root.rglob("*.py"))
    }
    current = {
        "protocol": "foundry-model-v1",
        "cases": plan,
        "source_hashes": hashes,
        "prompt_hash": hashlib.sha256(
            encode({"system": SYSTEM, "protocols": PROTOCOLS}).encode()
        ).hexdigest(),
        "model": "deepseek-flash",
        "max_output_tokens": 1024,
        "temperature": 0,
        "thinking": False,
        "phase": phase,
    }
    path = directory / "manifest.json"
    if path.exists():
        old = json.loads(path.read_text())
        if old != current:
            raise ValueError(
                "manifest differs; use a new output directory, never resume changed treatment code"
            )
    else:
        save(path, current)
    return current


async def episode(case, client, directory):
    destination = directory / "episodes" / (case["id"] + ".json")
    if destination.exists():
        return json.loads(destination.read_text())
    world, cfg = settings(case)
    namespace = case.get("parent", case["id"])
    suppression = []
    if case["kind"] == "message_removed":
        parent = json.loads((directory / "episodes" / (case["parent"] + ".json")).read_text())
        delivered = [d for d in parent["deliveries"] if d["status"] == "delivered" and d["evidence_ids"]]
        if not delivered:
            report = {"case": case, "status": "unavailable", "reason": "no delivered evidence message"}
            save(destination, report)
            return report
        chosen = min(delivered, key=lambda d: (d["sent_round"], d["message_id"]))
        suppression = [chosen["message_id"]]
    experiment = FoundryExperiment(world, cfg)
    population = {}
    for a in world.agents:
        protocol = case["partners"][int(a[4])] if "partners" in case else case["protocol"]
        population[a] = ModelScientist(
            client,
            protocol="broadcast" if protocol == "silent" else protocol,
            directory=directory / "responses",
            namespace=namespace,
        )
    started = time.time()
    run = await experiment.run(population, suppress=suppression)
    report = run.report()
    report.update(
        case=case,
        status="complete",
        world=asdict(world),
        suppressed=suppression,
        started_at=started,
        finished_at=time.time(),
    )
    metrics = report["metrics"]
    if metrics["ledger_conservation_error"] != 0 or metrics["outstanding_reservations"]:
        # Floating-point LMSR transfers allow tiny roundoff, never real deficits.
        if abs(metrics["ledger_conservation_error"]) > 1e-7 or metrics["outstanding_reservations"]:
            raise ValueError("settlement invariant failed")
    metrics["coordination_mismatches"] = sum(o.get("commitment_match") is False for o in run.outcomes)
    metrics["publication_count"] = sum(e.get("kind") == "publication" and e["published"] for e in run.events)
    metrics["artifact_adoptions"] = sum(
        len(e["adoptions"]) for e in run.events if e.get("kind") == "transfer"
    )
    metrics["cached_callbacks"] = sum(e.get("cached", False) for e in run.events if e["channel"] == "model")
    metrics["generation_values"] = [
        sum(o["accepted_value"] for o in run.outcomes if o["generation"] == g)
        for g in range(world.generations)
    ]
    save(destination, report)
    print(
        encode(
            {
                "episode": case["id"],
                "value": metrics["accepted_value"],
                "success": metrics["success_rate"],
                "protocol_errors": metrics["protocol_errors"],
                "gate_cost_bound": client.gate.status()["cost_usd"],
            }
        ),
        flush=True,
    )
    return report


def interval(values):
    values = np.array(values, float)
    return {
        "mean": float(values.mean()),
        "worlds": len(values),
        "interval_95": np.quantile(
            np.random.default_rng(0).choice(values, (2000, len(values)), replace=True).mean(axis=1),
            [0.025, 0.975],
        ).tolist()
        if len(values) > 1
        else None,
    }


def analyze(reports):
    primary = {
        r["case"]["id"]: r for r in reports if r["status"] == "complete" and r["case"]["kind"] == "primary"
    }
    groups = {}
    metrics = (
        "accepted_value",
        "shared_payoff",
        "real_execution_cost",
        "tokens",
        "model_cost",
        "protocol_errors",
        "coordination_mismatches",
        "publication_count",
        "artifact_adoptions",
        "duplicate_experiments",
        "delivered_bytes",
    )
    for r in primary.values():
        c = r["case"]
        key = "/".join(c[k] for k in ("incentive", "pressure", "protocol"))
        groups.setdefault(key, []).append(r)
    summaries = {k: {m: interval([r["metrics"][m] for r in rs]) for m in metrics} for k, rs in groups.items()}
    effects = {}
    for key, rs in groups.items():
        inc, pressure, protocol = key.split("/")
        pairs = [(r, primary.get(f"primary-{r['case']['seed']}-{inc}-{pressure}-silent")) for r in rs]
        if all(b is not None for _, b in pairs):
            effects[key] = interval(
                [a["metrics"]["accepted_value"] - b["metrics"]["accepted_value"] for a, b in pairs]
            )
    interactions = {}
    seeds = sorted({r["case"]["seed"] for r in primary.values()})
    for protocol in PROTOCOLS:
        for moderator, levels, other, fixed_values in (
            ("incentive", ("private", "shared"), "pressure", ("stable", "disrupted")),
            ("pressure", ("disrupted", "stable"), "incentive", ("shared", "private")),
        ):
            for fixed in fixed_values:
                values = []
                for seed in seeds:
                    ds = []
                    for level in levels:
                        opts = {moderator: level, other: fixed}
                        prefix = f"primary-{seed}-{opts['incentive']}-{opts['pressure']}-"
                        a, b = primary.get(prefix + protocol), primary.get(prefix + "silent")
                        if a and b:
                            ds.append(a["metrics"]["accepted_value"] - b["metrics"]["accepted_value"])
                    if len(ds) == 2:
                        values.append(ds[0] - ds[1])
                if values:
                    interactions[f"{protocol}/{moderator}/{fixed}"] = interval(values)
    interventions = {}
    for kind in ("artifacts_off", "message_removed"):
        for inc in ("shared", "private"):
            rows = [
                r
                for r in reports
                if r["status"] == "complete" and r["case"]["kind"] == kind and r["case"]["incentive"] == inc
            ]
            values = [
                primary[r["case"]["parent"]]["metrics"]["accepted_value"] - r["metrics"]["accepted_value"]
                for r in rows
                if r["case"]["parent"] in primary
            ]
            if values:
                interventions[f"{kind}/{inc}/baseline_minus_intervened"] = interval(values)
    cross = []
    for seed in seeds:
        cube = np.zeros((2, 2, 2))
        complete = True
        for i, a in enumerate(("broadcast", "targeted")):
            for j, b in enumerate(("broadcast", "targeted")):
                r = (
                    primary.get(f"primary-{seed}-private-disrupted-{a}")
                    if i == j
                    else next(
                        (
                            r
                            for r in reports
                            if r["status"] == "complete" and r["case"]["id"] == f"crossplay-{seed}-{a}-{b}"
                        ),
                        None,
                    )
                )
                if r is None:
                    complete = False
                    continue
                for firm in (0, 1):
                    cube[i, j, firm] = np.mean(
                        [
                            v
                            for agent, v in r["metrics"]["private_surplus"].items()
                            if agent.startswith(f"firm{firm}.")
                        ]
                    )
        if complete:
            cross.append(cube)
    population = None
    if cross:
        payoff = np.mean(cross, axis=0)
        scale = max(float(np.ptp(payoff)), 1.0)
        rank = AlphaRankEvaluator(alpha=0.1).evaluate(payoff / scale)
        meta = PolicySpaceResponseOracles([[0, 1], [0, 1]], lambda a, b: payoff[a, b]).meta_strategy(500)
        population = {
            "policies": ["broadcast", "targeted"],
            "worlds": len(cross),
            "payoffs": payoff.tolist(),
            "alpharank": {"profiles": rank["profiles"], "mass": rank["mass"].tolist(), "scale": scale},
            "meta_mixtures": [p.tolist() for p in meta["mixtures"]],
            "restricted_deviation": meta["restricted_product_deviation"].tolist(),
        }
    return {
        "summaries": summaries,
        "paired_communication_effects": effects,
        "difference_in_differences": interactions,
        "interventions": interventions,
        "cross_play": population,
        "completed_episodes": sum(r["status"] == "complete" for r in reports),
        "unavailable": [r["case"]["id"] for r in reports if r["status"] == "unavailable"],
    }


async def execute(args):
    directory = args.output
    directory.mkdir(parents=True, exist_ok=True)
    gate = SQLiteCallGate(
        args.gate,
        limits=None
        if args.gate.exists()
        else GateLimits(
            max_calls=10000, max_tokens=30_000_000, max_usd=15, max_concurrency=12, requests_per_minute=600
        ),
        enabled=True,
    )
    client = DeepSeekClient(gate=gate, timeout=90)
    plan = cases()
    dev = [
        dict(
            id="dev-pooled",
            kind="development",
            seed=901,
            split="dev",
            incentive="shared",
            pressure="stable",
            protocol="silent",
            pooled=True,
        ),
        dict(
            id="dev-private-observations",
            kind="development",
            seed=901,
            split="dev",
            incentive="shared",
            pressure="disrupted",
            protocol="targeted",
        ),
    ]
    selected = dev if args.phase == "dev" else plan
    manifest = freeze(directory, selected, args.phase)
    if args.phase == "test":
        if not args.development or not (args.development / "summary.json").exists():
            raise ValueError("test phase requires completed development directory")
        development = json.loads((args.development / "summary.json").read_text())
        if not development.get("development_passed"):
            raise ValueError("development acceptance checks did not pass")
        dev_manifest = json.loads((args.development / "manifest.json").read_text())
        for source in (
            "foundry/model_agents.py",
            "foundry/experiment.py",
            "foundry/world.py",
            "providers/deepseek.py",
        ):
            if manifest["source_hashes"][source] != dev_manifest["source_hashes"][source]:
                raise ValueError("agent/environment changed after development; repeat development validation")
        save(
            directory / "development-provenance.json",
            {
                "manifest": dev_manifest,
                "summary": development,
                "acceptance": "pooled success >= 0.5; each episode invalid-action fraction <= 0.1",
            },
        )
    reports = []
    errors = []
    semaphore = asyncio.Semaphore(2)

    async def guarded(case):
        async with semaphore:
            if errors:
                return None
            try:
                return await episode(case, client, directory)
            except Exception as exc:
                # Do not expose response bodies/credentials in exception logs.
                problem = {"episode": case["id"], "error_type": type(exc).__name__}
                errors.append(problem)
                print(encode(problem), flush=True)
                return None

    # Parent episodes must finish before conditional interventions.
    for stage in (
        selected if args.phase == "dev" else [c for c in selected if "parent" not in c],
        [] if args.phase == "dev" else [c for c in selected if "parent" in c],
    ):
        if errors:
            break
        for future in asyncio.as_completed([guarded(c) for c in stage]):
            report = await future
            if report:
                reports.append(report)
            save(
                directory / "progress.json",
                {"completed": len(reports), "errors": errors, "gate": gate.status()},
            )
    summary = analyze(reports)
    summary.update(
        errors=errors,
        gate=gate.status(),
        planned_episodes=len(selected),
        phase=args.phase,
        complete=not errors and len(reports) == len(selected),
    )
    if args.phase == "dev":
        pooled = next((r for r in reports if r["case"]["id"] == "dev-pooled"), None)
        summary["development_passed"] = (
            summary["complete"]
            and pooled["metrics"]["success_rate"] >= 0.5
            and all(r["metrics"]["protocol_errors"] / r["metrics"]["agent_calls"] <= 0.1 for r in reports)
        )
    save(directory / "summary.json", summary)
    print(
        encode(
            {
                "complete": summary["complete"],
                "completed": summary["completed_episodes"],
                "development_passed": summary.get("development_passed"),
                "gate": gate.status(),
            }
        ),
        flush=True,
    )
    if not summary["complete"]:
        raise SystemExit(1)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--phase", choices=("dev", "test"), default="dev")
    p.add_argument("--development", type=Path)
    p.add_argument("--gate", type=Path, default=Path("var/foundry/integrated-gate.sqlite"))
    asyncio.run(execute(p.parse_args()))


if __name__ == "__main__":
    main()
