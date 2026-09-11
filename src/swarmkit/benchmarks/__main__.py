"""Offline paired communication pilot: python -m swarmkit.benchmarks."""

import argparse
import asyncio
import json
from pathlib import Path

from . import (
    ChannelConfig,
    CommunicationEvaluator,
    EvidenceAgent,
    distributed_evidence,
    interdependent_schedule,
    paired_summary,
    quality_cost_summary,
)


async def pilot(args):
    conditions = {}
    runs = []
    for budget in args.budgets:
        for policy in ("none", "broadcast", "request", "targeted", "gated"):
            group = []
            for seed in range(args.cases):
                case = (
                    distributed_evidence(seed, args.agents)
                    if args.task == "evidence"
                    else interdependent_schedule(seed, args.agents)
                )
                evaluator = CommunicationEvaluator(
                    args.rounds,
                    ChannelConfig(max_messages=budget),
                    trust_reported_usage=True,
                    aggregation="joint" if args.task == "schedule" else "designated",
                )
                result = await evaluator.run(case, {a: EvidenceAgent(policy) for a in case.private}, seed)
                group.append(result)
                runs.append(result.report())
            conditions[(budget, policy)] = group
    comparisons = {
        f"{budget}:{policy}": paired_summary(group, conditions[(budget, "none")])
        for (budget, policy), group in conditions.items()
        if policy != "none"
    }
    return {
        "configuration": vars(args) | {"output": str(args.output)},
        "quality_cost": {
            f"{budget}:{policy}": quality_cost_summary(group)
            for (budget, policy), group in conditions.items()
        },
        "comparisons": comparisons,
        "runs": runs,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=int, default=30)
    parser.add_argument("--agents", type=int, default=4)
    parser.add_argument("--rounds", type=int, default=3)
    parser.add_argument("--budgets", type=int, nargs="+", default=[4, 16])
    parser.add_argument("--task", choices=["evidence", "schedule"], default="evidence")
    parser.add_argument("--output", type=Path, default=Path("communication-results.json"))
    args = parser.parse_args()
    if args.cases < 1 or len(set(args.budgets)) != len(args.budgets):
        parser.error("positive case count and unique budgets required")
    report = asyncio.run(pilot(args))
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["comparisons"], indent=2))


if __name__ == "__main__":
    main()
