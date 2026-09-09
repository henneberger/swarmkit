"""Offline method discovery and a minimal private-information swarm demo."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from .catalog import methods


def main():
    parser = argparse.ArgumentParser(prog="python -m swarmkit")
    sub = parser.add_subparsers(dest="command", required=True)
    listing = sub.add_parser("list", help="List implemented methods and source fidelity")
    listing.add_argument("--family")
    listing.add_argument("--json", action="store_true")
    sub.add_parser("demo", help="Run an offline evidence-exchange demonstration")
    args = parser.parse_args()
    if args.command == "list":
        records = methods(args.family)
        if args.json:
            print(json.dumps([asdict(record) for record in records], indent=2))
        else:
            for record in records:
                print(f"{record.name:25} {record.family:15} {record.fidelity:12} {record.description}")
        return
    from .deliberation import ExchangeThenDecide, IndependentVoting, WeightedConsensus
    from .runtime import Pipeline
    from .types import AgentState, Evidence, SwarmState, Task

    shared = Evidence("old", "Old map recommends A", "old-map", "a", supports=("A",), confidence=0.4)
    hidden = Evidence(
        "survey", "New survey closes A and confirms B", "new-survey", "b", supports=("B",), contradicts=("A",)
    )
    state = SwarmState(
        {
            key: AgentState(key, private_evidence=(shared,) + ((hidden,) if key == "b" else ()))
            for key in ("a", "b", "c")
        },
        seed=7,
    )
    task = Task("route", "Choose the currently passable route", candidates=("A", "B"))
    before = IndependentVoting().step(state, task)
    exchange = ExchangeThenDecide()
    after = Pipeline([exchange, exchange, exchange]).step(state, task)
    consensus = WeightedConsensus()
    print(
        json.dumps(
            {
                "before": consensus.aggregate(before.decisions, task).metadata["winner"],
                "after": consensus.aggregate(after.decisions, task).metadata["winner"],
                "messages": len(state.messages),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
