"""Export aggregate evidence from a completed live Foundry study (no API calls)."""

import argparse
import json
from collections import Counter
from pathlib import Path


def audit(episodes):
    from swarmkit.foundry import FoundryWorld

    checked = 0
    for r in episodes:
        world = FoundryWorld(**r["world"])
        metrics = r["metrics"]
        assert metrics["agent_calls"] == world.generations * r["config"]["rounds"] * len(world.agents)
        assert abs(metrics["ledger_conservation_error"]) < 1e-7
        assert metrics["outstanding_reservations"] == 0
        for role in ("sensor", "power", "firmware"):
            assert (
                metrics["remaining_materials"].get(role, 0) + metrics["consumed_materials"].get(role, 0)
                == world.firms * world.generations
            )
        invalid = {
            (e["agent"], e["tick"]) for e in r["events"] if e["channel"] == "model" and e["protocol_error"]
        }
        for o in r["outcomes"]:
            if "assembled_recipe" not in o:
                assert o["accepted_value"] == 0
                continue
            order = next(x for x in world.orders(o["generation"]) if x["id"] == o["order"])
            expected = world.verify(o["generation"], o["assembled_recipe"], o["completion"], order)
            bad = any((a, (o["generation"] + 1) * r["config"]["rounds"] - 1) in invalid for a in o["team"])
            assert o["quality"] == expected["quality"]
            assert o["success"] == (expected["success"] and o["tested"] and not bad)
            assert o["accepted_value"] == (order["value"] if o["success"] else 0)
            checked += 1
        assert metrics["accepted_value"] == sum(o["accepted_value"] for o in r["outcomes"])
        if r["case"]["protocol"] == "silent":
            assert not any(d["status"] == "delivered" for d in r["deliveries"])
    return {
        "episodes_checked": len(episodes),
        "assembled_devices_checked": checked,
        "cash_materials_escrow_calls_and_silent_controls": "passed",
        "invalid_commitments_cannot_earn_value": "passed",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("study", type=Path)
    parser.add_argument("--output", type=Path, default=Path("docs/experiments"))
    args = parser.parse_args()
    summary = json.loads((args.study / "summary.json").read_text())
    if not summary["complete"]:
        raise SystemExit("Refusing to label an incomplete study as complete")
    manifest = json.loads((args.study / "manifest.json").read_text())
    episodes = [json.loads(p.read_text()) for p in sorted((args.study / "episodes").glob("*.json"))]
    complete = [r for r in episodes if r["status"] == "complete"]
    models = Counter(e["response_model"] for r in complete for e in r["events"] if e["channel"] == "model")
    errors = Counter(
        e["protocol_error"]
        for r in complete
        for e in r["events"]
        if e["channel"] == "model" and e["protocol_error"]
    )
    activity = Counter()
    bids = Counter()
    # Characterize primary runs only; intervention reuse must not inflate behavior counts.
    for r in complete:
        if r["case"]["kind"] != "primary":
            continue
        invalid = {
            (e["agent"], e["tick"]) for e in r["events"] if e["channel"] == "model" and e["protocol_error"]
        }
        for e in r["events"]:
            if e.get("kind") == "forecast_trade":
                activity["forecast_trades"] += 1
            if e.get("kind") == "publication":
                activity["published" if e["published"] else "withheld"] += 1
            if e.get("kind") == "bid_reveal":
                bids.update(
                    str(v)
                    for a, v in e["bids"].items()
                    if (a, e["generation"] * r["config"]["rounds"]) not in invalid
                )
        for o in r["outcomes"]:
            activity[o["reason"]] += 1
            if o.get("team"):
                activity[
                    "cross_firm_teams" if len({a.split(".")[0] for a in o["team"]}) > 1 else "same_firm_teams"
                ] += 1
    artifact = {
        "interpretation": "Exploratory, three held-out worlds; not a powered strategy ranking. "
        "Logical callback usage includes cached replay. Gate usage includes development and calibration. "
        "Costs are conservative bounds, not the provider invoice.",
        "manifest": manifest,
        "summary": summary,
        "response_model_counts": dict(models),
        "protocol_error_counts": dict(errors),
        "independent_audit": audit(complete),
        "primary_behavior_counts": dict(activity),
        "primary_valid_bid_histogram": dict(bids),
        "episodes": [
            {
                k: r[k]
                for k in (
                    "case",
                    "status",
                    "world",
                    "config",
                    "metrics",
                    "outcomes",
                    "suppressed",
                    "started_at",
                    "finished_at",
                )
            }
            for r in complete
        ],
    }
    args.output.mkdir(parents=True, exist_ok=True)
    stem = args.output / "foundry-deepseek-v41"
    stem.with_suffix(".json").write_text(json.dumps(artifact, indent=2, allow_nan=False) + "\n")

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    protocols = ("silent", "broadcast", "targeted", "coordinator")
    colors = ("#9ca3af", "#2563eb", "#059669", "#d97706")
    fig, axes = plt.subplots(2, 2, figsize=(11, 7), sharey=True)
    for i, inc in enumerate(("shared", "private")):
        for j, pressure in enumerate(("stable", "disrupted")):
            ax = axes[i, j]
            for x, (protocol, color) in enumerate(zip(protocols, colors, strict=True)):
                rows = [
                    r
                    for r in complete
                    if r["case"]["kind"] == "primary"
                    and (r["case"]["incentive"], r["case"]["pressure"], r["case"]["protocol"])
                    == (inc, pressure, protocol)
                ]
                values = [r["metrics"]["accepted_value"] for r in rows]
                ax.bar(x, np.mean(values), color=color, alpha=0.75, width=0.65)
                ax.scatter(x + np.linspace(-0.12, 0.12, len(values)), values, color="#111827", s=22, zorder=3)
            ax.set_title(f"{inc.title()} objective · {pressure}")
            ax.set_xticks(range(4), protocols)
            ax.set_ylim(0, 440)
            ax.spines[["top", "right"]].set_visible(False)
            ax.grid(axis="y", alpha=0.15)
            if j == 0:
                ax.set_ylabel("Accepted order value (maximum 420)")
    fig.suptitle("DeepSeek V4.1 Flash — integrated communication experiment", fontsize=15)
    fig.text(
        0.5,
        0.015,
        "Bars: mean; dots: three held-out worlds. Same model-call allowances; actual token use differs.",
        ha="center",
        fontsize=9,
    )
    fig.tight_layout(rect=(0, 0.045, 1, 0.95))
    fig.savefig(stem.with_suffix(".png"), dpi=160)
    fig.savefig(stem.with_suffix(".svg"))
    plt.close(fig)

    text = [
        "# DeepSeek V4.1 Flash: integrated Foundry results",
        "",
        "This is a live API experiment with model-chosen research, messages, bids, partners, commitments, forecasts and publication. "
        "The environment and verification are synthetic; results apply to this task and model configuration.",
        "",
        f"Completed {len(complete)} held-out episodes; {len(summary['unavailable'])} conditional interventions were unavailable. "
        "Three independent world seeds are too few to establish a reliable strategy ranking.",
        "",
        "![Accepted value across conditions](foundry-deepseek-v41.png)",
        "",
        "| Objective | Environment | Silent | Broadcast | Targeted | Coordinator |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for inc in ("shared", "private"):
        for pressure in ("stable", "disrupted"):
            vals = [
                summary["summaries"][f"{inc}/{pressure}/{p}"]["accepted_value"]["mean"] for p in protocols
            ]
            text.append(f"| {inc} | {pressure} | " + " | ".join(f"{v:.2f}" for v in vals) + " |")
    gate = summary["gate"]
    text.extend(
        [
            "",
            "## What the agents actually exercised",
            "",
            f"Primary runs made {activity['forecast_trades']} forecast trades, published {activity['published']} successful recipes "
            f"and withheld {activity['withheld']}. Valid first-round bids: `{json.dumps(dict(bids), sort_keys=True)}`. "
            f"There were {activity['cross_firm_teams']} cross-firm teams and {activity['same_firm_teams']} same-firm teams.",
            "",
            f"Late outcomes: {activity['late']}; execution failures: {activity['execution_failed']}. "
            "Available mechanisms are not necessarily exercised. If bids remain at the JSON example value, that is compatible "
            "with example anchoring and is not evidence of strategic bidding. No trading or withholding provides no support "
            "for claims about emergent markets or strategic disclosure. Nonbinding resource constraints cannot establish "
            "a congestion effect.",
            "",
            "Hub-condition scores include failures to follow its routing instruction. They do not isolate the intrinsic "
            "value of a hub topology from the model’s ability to follow that protocol. The development gate tested pooled "
            "broadcast and targeted interaction, not hub comprehension. These limitations are preserved rather than repaired on test data.",
        ]
    )
    text.extend(
        [
            "",
            f"The shared gate recorded **{gate['calls']:,} API attempts**, **{gate['tokens']:,} charged/reserved tokens**, "
            f"and **${gate['cost_usd']:.4f} conservative cost** across calibration, development and testing. "
            "Exact-context replay reuses responses; episode logical token totals therefore differ from newly billed usage.",
            "",
            f"Protocol failures across completed held-out logical callbacks: {sum(errors.values())}. "
            "They count as failed turns, with no scripted solver or extra repair call. Distribution: `"
            + json.dumps(dict(errors), sort_keys=True)
            + "`.",
            "",
            "See the [experimental contract](../FOUNDRY_MODEL_EXPERIMENT.md) for development repairs, controls, "
            "confounds and spending definitions. The [machine-readable artifact](foundry-deepseek-v41.json) includes "
            "the frozen manifest, per-world outcomes, paired effects, interaction estimates, interventions and population payoffs.",
            "",
            "Full prompts and responses are retained in the local study directory; credentials are excluded. "
            "No test-time prompt tuning was performed. Message interventions reuse matching contexts but cannot eliminate "
            "provider randomness on changed contexts. Confidence intervals resample worlds, not individual orders.",
            "",
        ]
    )
    stem.with_suffix(".md").write_text("\n".join(text))
    print(stem.with_suffix(".md"))


if __name__ == "__main__":
    main()
