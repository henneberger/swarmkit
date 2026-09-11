"""Run the Research Foundry offline, including its paired factorial study."""

import argparse
import asyncio
import json
from dataclasses import asdict
from pathlib import Path

from ..benchmarks import ChannelConfig
from . import FoundryConfig, FoundryExperiment, FoundryWorld
from .study import cross_play, run_study


async def execute(args):
    world = FoundryWorld(
        seed=args.seed,
        split=args.split,
        firms=args.firms,
        components=args.components,
        generations=args.generations,
        change_every=args.change_every,
    )
    cfg = FoundryConfig(
        communication=args.policy,
        incentives=args.incentives,
        rounds=args.rounds,
        channel=ChannelConfig(
            max_messages=args.budget,
            max_bytes=args.bytes,
            delay=args.delay,
            loss=args.loss,
            disabled=args.disable_messages,
        ),
        topology=args.topology,
        artifacts=not args.no_artifacts,
        pooled=args.pooled,
        research_budget=args.research_budget,
        production_budget=args.production_budget,
        equipment_slots=args.equipment_slots,
        material_units=args.material_units,
        equipment_failure=args.failure,
        turnover=args.turnover,
        institution=args.institution,
        team_selection=args.team_selection,
        forecast_market=args.forecast_market,
        checkpoint=args.remove_message is not None,
        trust_reported_usage=True,
    )
    if args.mode == "study":
        result = await run_study(
            tuple(range(args.seed, args.seed + args.worlds)),
            template=world,
            config=cfg,
            budgets=tuple(args.budgets),
            run_seeds=(args.run_seed,),
            extra_controls=args.extra_controls,
            traces=args.traces,
        )
    elif args.mode == "cross-play":
        result = await cross_play(
            tuple(args.policies), tuple(range(args.seed, args.seed + args.worlds)), template=world, config=cfg
        )
    else:
        experiment = FoundryExperiment(world, cfg)
        run = await experiment.run(seed=args.run_seed)
        result = run.report(traces=args.traces)
        result["world"] = asdict(world)
        if args.remove_message:
            effect = await experiment.replay_without(run, args.remove_message)
            result["intervention"] = {k: v for k, v in effect.items() if k != "intervened"}
            result["intervened"] = effect["intervened"].report(traces=args.traces)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result.get("summaries", result.get("metrics", result)), indent=2, allow_nan=False))
    print(f"Report: {args.output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["run", "study", "cross-play"], nargs="?", default="run")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--run-seed", type=int, default=0)
    parser.add_argument("--split", choices=["dev", "test"], default="test")
    parser.add_argument("--worlds", type=int, default=3)
    parser.add_argument("--firms", type=int, default=4)
    parser.add_argument("--components", type=int, default=3)
    parser.add_argument("--generations", type=int, default=4)
    parser.add_argument("--change-every", type=int, default=2)
    parser.add_argument("--rounds", type=int, default=5)
    parser.add_argument(
        "--policy", choices=["none", "broadcast", "request", "targeted", "gated"], default="targeted"
    )
    parser.add_argument("--incentives", choices=["shared", "private"], default="shared")
    parser.add_argument("--topology", choices=["full", "ring", "star", "hypergraph"], default="full")
    parser.add_argument("--budget", type=int, default=48)
    parser.add_argument("--budgets", type=int, nargs="+", default=[12, 48])
    parser.add_argument("--bytes", type=int)
    parser.add_argument("--research-budget", type=int, default=24)
    parser.add_argument("--production-budget", type=int, default=16)
    parser.add_argument("--material-units", type=int)
    parser.add_argument("--equipment-slots", type=int, default=2)
    parser.add_argument("--delay", type=int, default=0)
    parser.add_argument("--loss", type=float, default=0)
    parser.add_argument("--failure", type=float, default=0)
    parser.add_argument("--turnover", type=float, default=0.25)
    parser.add_argument(
        "--institution", choices=["contract", "first_price", "second_price", "vcg"], default="contract"
    )
    parser.add_argument("--team-selection", choices=["cost", "matching", "routing"], default="cost")
    parser.add_argument("--forecast-market", action="store_true")
    parser.add_argument("--no-artifacts", action="store_true")
    parser.add_argument("--disable-messages", action="store_true")
    parser.add_argument("--pooled", action="store_true")
    parser.add_argument("--extra-controls", action="store_true")
    parser.add_argument("--policies", nargs="+", default=["broadcast", "targeted"])
    parser.add_argument("--remove-message")
    parser.add_argument("--traces", action="store_true")
    parser.add_argument("--output", type=Path, default=Path("foundry-results.json"))
    args = parser.parse_args()
    if args.worlds < 1:
        parser.error("--worlds must be positive")
    asyncio.run(execute(args))


if __name__ == "__main__":
    main()
