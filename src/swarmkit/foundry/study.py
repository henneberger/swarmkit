"""Paired world-level studies and empirical strategy populations."""

from __future__ import annotations

from dataclasses import asdict, replace

import numpy as np

from ..economics import AlphaRankEvaluator, ExternalRegretPolicy, PolicySpaceResponseOracles
from .experiment import FoundryConfig, FoundryExperiment
from .policies import FoundryScientist
from .world import FoundryWorld


def summarize(runs):
    if not runs:
        raise ValueError("nonempty run collection required")
    metrics = (
        "accepted_value",
        "success_rate",
        "shared_payoff",
        "real_execution_cost",
        "agent_calls",
        "research_calls",
        "production_calls",
        "duplicate_experiments",
        "generated_bytes",
        "delivered_bytes",
        "receiver_input_bytes",
        "artifact_read_bytes",
        "tokens",
        "model_cost",
    )
    result = {"runs": len(runs), "independent_worlds": len({r.world_id for r in runs})}
    for metric in metrics:
        values = [r.metrics[metric] for r in runs]
        result[metric] = None if any(v is None for v in values) else float(np.mean(values))
    result["generations"] = {
        str(g): float(
            np.mean([o["accepted_value"] for r in runs for o in r.outcomes if o["generation"] == g])
        )
        for g in sorted({o["generation"] for r in runs for o in r.outcomes})
    }
    return result


def paired_difference(treatment, control, metric="accepted_value", seed=0, bootstrap=2000):
    if not treatment or len(treatment) != len(control) or bootstrap < 1:
        raise ValueError("nonempty paired runs and positive bootstrap required")

    def indexed(runs):
        result = {(r.world_id, r.seed): r for r in runs}
        if len(result) != len(runs):
            raise ValueError("duplicate world/seed pairs")
        return result

    a, b = indexed(treatment), indexed(control)
    if set(a) != set(b):
        raise ValueError("world/seed pairs must match")
    by_world = {}
    for key in sorted(a):
        by_world.setdefault(key[0], []).append(a[key].metrics[metric] - b[key].metrics[metric])
    values = np.array([np.mean(v) for v in by_world.values()])
    if not np.isfinite(values).all():
        raise ValueError("finite paired metric required")
    interval = None
    if len(values) > 1:
        draws = (
            np.random.default_rng(seed).choice(values, (bootstrap, len(values)), replace=True).mean(axis=1)
        )
        interval = np.quantile(draws, [0.025, 0.975]).tolist()
    return {
        "mean_difference": float(values.mean()),
        "interval_95": interval,
        "independent_worlds": len(values),
        "paired_runs": len(a),
        "metric": metric,
    }


async def run_study(
    world_seeds=(0, 1, 2),
    *,
    template=None,
    config=None,
    budgets=(12, 48),
    run_seeds=(0,),
    extra_controls=False,
    progress=None,
    traces=False,
):
    """The 4 communication x 2 incentive x 2 bandwidth design plus silent controls.

    Extra controls add messages/artifacts factorial endpoints and pooled evidence.
    Entire world trajectories, never orders or messages, are statistical units.
    """
    template, base = template or FoundryWorld(), config or FoundryConfig()
    if (
        not world_seeds
        or not run_seeds
        or len(set(world_seeds)) != len(world_seeds)
        or len(set(run_seeds)) != len(run_seeds)
        or not budgets
        or len(set(budgets)) != len(budgets)
    ):
        raise ValueError("nonempty unique seeds and budgets required")
    conditions = {}
    for incentives in ("shared", "private"):
        for budget in budgets:
            for policy in ("broadcast", "request", "targeted", "gated", "silent"):
                name = f"{incentives}/{budget}/{policy}"
                channel = replace(base.channel, max_messages=budget, disabled=policy == "silent")
                conditions[name] = replace(
                    base,
                    communication="broadcast" if policy == "silent" else policy,
                    incentives=incentives,
                    channel=channel,
                    checkpoint=False,
                )
        if extra_controls:
            high = max(budgets)
            for disabled in (False, True):
                conditions[f"{incentives}/{high}/artifacts_off/{disabled}"] = replace(
                    base,
                    communication="broadcast",
                    incentives=incentives,
                    artifacts=False,
                    checkpoint=False,
                    channel=replace(base.channel, max_messages=high, disabled=disabled),
                )
            conditions[f"{incentives}/{high}/pooled"] = replace(
                base,
                communication="broadcast",
                incentives=incentives,
                pooled=True,
                checkpoint=False,
                channel=replace(base.channel, max_messages=high, disabled=True),
            )
    groups = {}
    for name, condition in conditions.items():
        group = []
        for world_seed in world_seeds:
            world = replace(template, seed=world_seed)
            for seed in run_seeds:
                run = await FoundryExperiment(world, condition).run(seed=seed)
                group.append(run)
                if progress:
                    progress(name, world_seed, seed)
        groups[name] = group
    comparisons = {}
    for name, group in groups.items():
        incentives, budget, _ = name.split("/", 2)
        reference = f"{incentives}/{budget}/silent"
        comparisons[name] = paired_difference(group, groups[reference])
    return {
        "experiment": "research-foundry",
        "world_template": asdict(template),
        "world_seeds": list(world_seeds),
        "run_seeds": list(run_seeds),
        "summaries": {n: summarize(g) for n, g in groups.items()},
        "comparisons_to_silent": comparisons,
        "runs": {name: [r.report(traces=traces) for r in group] for name, group in groups.items()},
    }


async def cross_play(policies=("broadcast", "targeted"), world_seeds=(0, 1), *, template=None, config=None):
    """Two policy populations control alternating firms; real Foundry outcomes supply payoffs.

    Fixed policy cross-play, not a learned response oracle. AlphaRank is a ranking
    of these measured policies. PSRO's meta-solver reports restricted deviations.
    """
    template, cfg = template or FoundryWorld(firms=2), config or FoundryConfig(incentives="private")
    if not policies or len(set(policies)) != len(policies) or not world_seeds or template.firms % 2:
        raise ValueError("unique policies, nonempty worlds and an even firm count required")
    cube = np.zeros((len(world_seeds), len(policies), len(policies), 2))
    for k, seed in enumerate(world_seeds):
        world = replace(template, seed=seed)
        for i, left in enumerate(policies):
            for j, right in enumerate(policies):
                agents = {
                    a: FoundryScientist(
                        left if int(a.split(".")[0][4:]) % 2 == 0 else right, cfg.incentives, cfg.max_cards
                    )
                    for a in world.agents
                }
                run = await FoundryExperiment(world, replace(cfg, checkpoint=False)).run(agents)
                for population in (0, 1):
                    members = [a for a in world.agents if int(a.split(".")[0][4:]) % 2 == population]
                    cube[k, i, j, population] = (
                        np.mean([run.metrics["private_surplus"][a] for a in members])
                        if cfg.incentives == "private"
                        else run.metrics["shared_payoff"]
                    )
    payoffs = cube.mean(axis=0)
    scale = max(float(np.ptp(payoffs)), 1.0)
    ranked = AlphaRankEvaluator(alpha=0.1).evaluate(payoffs / scale)
    meta = PolicySpaceResponseOracles(
        [list(range(len(policies)))] * 2, lambda a, b: payoffs[a, b]
    ).meta_strategy(500)
    return {
        "world_template": asdict(template),
        "config": asdict(cfg),
        "payoff_objective": cfg.incentives,
        "policies": list(policies),
        "world_seeds": list(world_seeds),
        "payoffs": payoffs.tolist(),
        "standard_error": (cube.std(axis=0, ddof=1) / np.sqrt(len(cube))).tolist() if len(cube) > 1 else None,
        "alpharank": {"profiles": ranked["profiles"], "mass": ranked["mass"].tolist(), "payoff_scale": scale},
        "meta_mixtures": [p.tolist() for p in meta["mixtures"]],
        "restricted_deviation": meta["restricted_product_deviation"].tolist(),
    }


class CommunicationPortfolio:
    """Full-information Hedge over evaluated communication policies on training worlds.

    Fit only on development runs; evaluate the frozen mixture on disjoint test
    worlds. This learns a policy selector, not language-model weights.
    """

    def fit(self, training, policies, rate=0.1):
        if not training or any(row.get("split") != "dev" for row in training):
            raise ValueError("explicit development-only world outcomes required")
        if len(set(policies)) != len(policies) or not policies:
            raise ValueError("nonempty unique policy names required")
        learner = ExternalRegretPolicy(len(policies), rate=rate)
        self.world_ids = set()
        for row in training:
            values = row["normalized_utilities"]
            learner.update([values[p] for p in policies])
            self.world_ids.add(row["world_id"])
        self.policies, self.mixture = tuple(policies), learner.probabilities().copy()
        return self.mixture.copy()

    def select(self, world_id, rng):
        if world_id in self.world_ids:
            raise ValueError("held-out world overlaps training")
        return self.policies[int(rng.choice(len(self.policies), p=self.mixture))]
