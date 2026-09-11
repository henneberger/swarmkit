import json
from dataclasses import replace

import numpy as np
import pytest

from swarmkit.benchmarks import ChannelConfig
from swarmkit.foundry import FoundryConfig, FoundryExperiment, FoundryScientist, FoundryWorld
from swarmkit.foundry.study import CommunicationPortfolio, cross_play, paired_difference, run_study
from swarmkit.types import AgentOutput, Artifact, Decision, Evidence, Message


@pytest.fixture
def world():
    return FoundryWorld(firms=2, components=2, generations=2)


def stable_metrics(run):
    return {k: v for k, v in run.metrics.items() if k not in ("elapsed_seconds", "suffix_only_timing")}


def test_world_has_genuine_three_way_interactions_and_disjoint_splits(world):
    dev = replace(world, split="dev")
    assert dev.id != world.id
    assert any(dev.value(0, t) != world.value(0, t) for t in world.topics())
    values = np.array([world.quality(0, r) for r in world.recipes]).reshape(2, 2, 2)
    # Third mixed discrete difference would be zero for a purely pairwise additive model.
    assert np.diff(np.diff(np.diff(values, axis=0), axis=1), axis=2).item() != 0
    all_facts = [e.id for a in world.agents for e in world.private(a, 0)]
    assert len(all_facts) == len(set(all_facts)) == len(world.topics())
    for generation in range(world.generations):
        assert all(
            any(world.quality(world.version(generation), r) >= o["threshold"] for r in world.recipes)
            for o in world.orders(generation)
        )


@pytest.mark.parametrize(
    "kwargs", [{"components": 1}, {"firms": 1}, {"rounds": 0}, {"turnover": float("nan")}]
)
def test_invalid_world_or_config_rejected(kwargs):
    with pytest.raises(ValueError):
        (FoundryWorld if "components" in kwargs or "firms" in kwargs else FoundryConfig)(**kwargs)


async def test_reproducible_verified_production_and_conserved_cash(world):
    exp = FoundryExperiment(world, FoundryConfig(turnover=0, pooled=True))
    a, b = await exp.run(), await exp.run()
    assert a.outcomes == b.outcomes and a.events == b.events and a.deliveries == b.deliveries
    assert stable_metrics(a) == stable_metrics(b)
    assert a.metrics["accepted_value"] > 0
    assert a.metrics["ledger_conservation_error"] == pytest.approx(0)
    assert a.metrics["outstanding_reservations"] == 0
    assert a.metrics["agent_calls"] == len(world.agents) * world.generations * exp.config.rounds
    assert a.metrics["tokens"] is None and a.metrics["model_cost"] is None
    for outcome in a.outcomes:
        order = next(o for o in world.orders(outcome["generation"]) if o["id"] == outcome["order"])
        truth = world.verify(outcome["generation"], outcome["assembled_recipe"], outcome["completion"], order)
        assert outcome["success"] == truth["success"]
        assert sum(outcome["modeled_shapley_value"].values()) == pytest.approx(outcome["accepted_value"])
    json.dumps(a.report(), allow_nan=False)


async def test_no_messages_and_no_artifacts_leave_only_explicit_environment_channels(world):
    cfg = FoundryConfig(channel=ChannelConfig(disabled=True), artifacts=False, research_budget=0, turnover=0)
    run = await FoundryExperiment(world, cfg).run()
    assert not any(d.status == "delivered" for d in run.deliveries)
    assert run.metrics["artifact_reads"] == 0 and run.metrics["research_calls"] == 0
    assert run.metrics["generated_messages"] > 0
    assert any(e["channel"] == "procurement" for e in run.events)
    assert all(not e["adoptions"] for e in run.events if e.get("kind") == "transfer")


async def test_private_context_has_no_oracle_or_other_private_types_and_is_immutable(world):
    class Inspector:
        def act(self, context):
            meta = context.task.metadata
            assert context.task.id == "foundry"
            assert "seed" not in meta and "physics" not in meta
            assert meta["own_cost"] == world.cost(context.agent.id)
            assert set(meta["queries"]) == {
                q for q in world.topics() if world.topic_role(q) == context.agent.id.split(".")[1]
            }
            assert set(e.id for e in context.agent.private_evidence) == set(
                e.id for e in world.private(context.agent.id, 0)
            )
            context.agent.private_evidence = ()
            context.agent.memory["mutation"] = True
            context.task.metadata["orders"] = []
            return AgentOutput(
                decision=Decision(context.agent.id, "[0,0,0]", metadata={"bid": 1, "query": None})
            )

    exp = FoundryExperiment(replace(world, generations=1), FoundryConfig(checkpoint=True))
    run = await exp.run({a: Inspector() for a in world.agents})
    assert not run.checkpoints[1].data["state"].agents[world.agents[0]].memory


async def test_forged_evidence_and_context_mutation_cannot_authorize_a_query(world):
    class Forger:
        def act(self, context):
            fake = Evidence("fake", "{}", "fake-source", context.agent.id)
            context.agent.private_evidence += (fake,)
            return AgentOutput(
                messages=(Message(context.agent.id, "fake", evidence=(fake,)),),
                decision=Decision(context.agent.id, "[0,0,0]", metadata={"bid": 1}),
            )

    with pytest.raises(ValueError, match="unobserved"):
        await FoundryExperiment(world).run({a: Forger() for a in world.agents})


async def test_output_artifacts_cannot_bypass_verification(world):
    class Fabricator:
        def act(self, context):
            return AgentOutput(artifacts=(Artifact("fake", context.agent.id, {}, verified=True),))

    with pytest.raises(ValueError, match="verified builds"):
        await FoundryExperiment(world).run({a: Fabricator() for a in world.agents})


@pytest.mark.parametrize("config", [FoundryConfig(production_budget=0), FoundryConfig(equipment_failure=1)])
async def test_failed_work_never_pays_contracts_and_releases_escrow(world, config):
    run = await FoundryExperiment(world, config).run()
    assert run.metrics["accepted_value"] == 0
    assert run.metrics["balances"]["customer"] == 10000
    assert run.metrics["outstanding_reservations"] == 0
    assert all(o["reason"] == "execution_failed" for o in run.outcomes)
    assert not run.artifacts


async def test_oversized_bids_produce_unawarded_orders_without_mutation(world):
    class Expensive(FoundryScientist):
        def act(self, context):
            output = super().act(context)
            return replace(
                output, decision=replace(output.decision, metadata={**output.decision.metadata, "bid": 100})
            )

    run = await FoundryExperiment(world).run({a: Expensive() for a in world.agents})
    assert run.metrics["accepted_value"] == run.metrics["production_calls"] == 0
    assert run.metrics["outstanding_reservations"] == 0
    assert all(o["reason"] == "no_affordable_team" for o in run.outcomes)


@pytest.mark.parametrize("institution", ["first_price", "second_price", "vcg"])
async def test_priority_auctions_are_real_balanced_transfers(world, institution):
    run = await FoundryExperiment(world, FoundryConfig(institution=institution)).run()
    assert run.metrics["equipment_payments"] > 0
    assert run.metrics["balances"]["equipment"] == run.metrics["equipment_payments"]
    assert run.metrics["ledger_conservation_error"] == pytest.approx(0)


@pytest.mark.parametrize("rule", ["cost", "matching", "routing"])
async def test_team_selection_requires_specialties_and_matching_avoids_shared_workers(world, rule):
    run = await FoundryExperiment(world, FoundryConfig(team_selection=rule)).run()
    awards = [e for e in run.events if e.get("kind") == "award" and e["generation"] == 0]
    for award in awards:
        assert {a.split(".")[1] for a in award["members"]} == {"sensor", "power", "firmware"}
    if rule == "matching":
        assert len({a for e in awards for a in e["members"]}) == 6


async def test_production_schedules_do_not_overlap_shared_workers(world):
    run = await FoundryExperiment(world).run()
    by_worker = {}
    for event in run.events:
        if event.get("kind") == "production" and event["worker"]:
            by_worker.setdefault((event["generation"], event["worker"]), []).append(event["completion"])
    for completions in by_worker.values():
        assert all(b - a >= 2 for a, b in zip(sorted(completions), sorted(completions)[1:], strict=False))


async def test_research_and_production_budgets_are_enforced(world):
    run = await FoundryExperiment(world, FoundryConfig(research_budget=1, production_budget=3)).run()
    assert run.metrics["research_calls"] <= world.generations
    assert run.metrics["production_calls"] <= 3 * world.generations


async def test_receipts_respect_topology_loss_latency_and_duplicates(world):
    cfg = FoundryConfig(topology="ring", channel=ChannelConfig(loss=1))
    lost = await FoundryExperiment(world, cfg).run()
    assert not any(d.status == "delivered" for d in lost.deliveries)
    late = await FoundryExperiment(world, replace(cfg, channel=ChannelConfig(delay=100))).run()
    assert all(d.status != "delivered" for d in late.deliveries)
    doubled = await FoundryExperiment(world, replace(cfg, channel=ChannelConfig(duplicate=1))).run()
    assert any(d.message_id.endswith(":duplicate") and d.status == "delivered" for d in doubled.deliveries)


async def test_checkpoint_replay_and_suppression_are_exact_for_local_policies(world):
    cfg = FoundryConfig(checkpoint=True, turnover=0, channel=ChannelConfig(duplicate=1))
    exp = FoundryExperiment(replace(world, generations=1), cfg)
    run = await exp.run(seed=8)
    resumed = await exp.run(seed=8, checkpoint=run.checkpoints[2])
    assert run.outcomes == resumed.outcomes
    assert run.deliveries == resumed.deliveries
    assert stable_metrics(run) == stable_metrics(resumed)
    mid = next(
        d.message_id
        for d in run.deliveries
        if d.status == "delivered" and not d.message_id.endswith("duplicate")
    )
    effect = await exp.replay_without(run, mid)
    assert all(
        d.status != "delivered"
        for d in effect["intervened"].deliveries
        if d.message_id in (mid, mid + ":duplicate")
    )
    with pytest.raises(ValueError):
        await exp.run(seed=9, checkpoint=run.checkpoints[2])
    assert (
        run.metrics["outstanding_reservations"]
        == effect["intervened"].metrics["outstanding_reservations"]
        == 0
    )


async def test_artifact_visibility_retention_and_turnover(world):
    cfg = FoundryConfig(pooled=True, turnover=1, checkpoint=True)
    run = await FoundryExperiment(replace(world, generations=3, change_every=10), cfg).run()
    assert run.metrics["turnovers"] == 2 * len(world.agents)
    assert run.metrics["artifact_reads"] > 0
    assert any(e["adoptions"] for e in run.events if e.get("kind") == "transfer" and e["generation"] > 0)
    private = await FoundryExperiment(world, replace(cfg, incentives="private")).run()
    by_id = {a["id"]: a for a in private.artifacts}
    for event in private.events:
        if event.get("kind") == "read":
            assert all(
                by_id[i]["author"].split(".")[0] == event["agent"].split(".")[0] for i in event["artifacts"]
            )


async def test_forecast_market_is_collateralized_resolved_and_separately_logged(world):
    run = await FoundryExperiment(world, FoundryConfig(forecast_market=True)).run()
    assert any(e.get("kind") == "forecast_trade" for e in run.events)
    assert run.metrics["outstanding_reservations"] == 0
    assert run.metrics["ledger_conservation_error"] == pytest.approx(0, abs=1e-8)
    assert all(v >= -1e-8 for v in run.metrics["balances"].values())


async def test_study_pairs_worlds_and_holds_agent_calls_fixed(world):
    template = replace(world, generations=1)
    report = await run_study(
        (0,), template=template, config=FoundryConfig(rounds=2, research_budget=0), budgets=(6,)
    )
    assert len(report["summaries"]) == 10
    assert len({s["agent_calls"] for s in report["summaries"].values()}) == 1
    assert all(s["interval_95"] is None for s in report["comparisons_to_silent"].values())
    json.dumps(report, allow_nan=False)


async def test_paired_statistics_cluster_whole_worlds(world):
    exp = FoundryExperiment(replace(world, generations=1), FoundryConfig(rounds=1))
    runs = [await exp.run(seed=s) for s in (0, 1)]
    summary = paired_difference(runs, list(reversed(runs)))
    assert summary["mean_difference"] == 0 and summary["independent_worlds"] == 1
    with pytest.raises(ValueError):
        paired_difference(runs, [runs[0], runs[0]])


async def test_actual_crossplay_supplies_payoffs_to_population_solvers(world):
    report = await cross_play(
        ("none", "broadcast"),
        (0,),
        template=replace(world, generations=1),
        config=FoundryConfig(rounds=2, research_budget=0),
    )
    assert np.asarray(report["payoffs"]).shape == (2, 2, 2)
    assert sum(report["alpharank"]["mass"]) == pytest.approx(1)
    assert len(report["meta_mixtures"]) == 2


def test_communication_portfolio_separates_training_and_evaluation():
    portfolio = CommunicationPortfolio()
    rows = [
        {"split": "dev", "world_id": str(i), "normalized_utilities": {"a": 0, "b": 1}} for i in range(100)
    ]
    p = portfolio.fit(rows, ["a", "b"])
    assert p[1] > 0.99
    with pytest.raises(ValueError):
        portfolio.select("1", np.random.default_rng(0))
    with pytest.raises(ValueError):
        portfolio.fit([{"split": "test"}], ["a"])


async def test_materials_are_conserved_and_empty_inventory_prevents_delivery(world):
    run = await FoundryExperiment(world, FoundryConfig(pooled=True)).run()
    supply = world.firms * world.generations
    assert all(
        run.metrics["remaining_materials"][role] + run.metrics["consumed_materials"].get(role, 0) == supply
        for role in ("sensor", "power", "firmware")
    )
    empty = await FoundryExperiment(world, FoundryConfig(pooled=True, material_units=0)).run()
    assert empty.metrics["accepted_value"] == 0 and empty.metrics["outstanding_reservations"] == 0
    assert empty.metrics["balances"]["customer"] == 10000


async def test_replacements_do_not_inherit_predecessor_results_through_feedback(world):
    class ReplacementInspector(FoundryScientist):
        def act(self, context):
            if context.task.metadata["generation"] == 1 and context.task.metadata["round"] == 0:
                assert context.task.metadata["last_results"] == []
                assert context.agent.private_evidence == ()
                assert not context.messages
            return super().act(context)

    await FoundryExperiment(world, FoundryConfig(turnover=1)).run(
        {a: ReplacementInspector() for a in world.agents}
    )


async def test_stale_artifacts_are_labeled_and_not_adopted_as_current_measurements(world):
    changed = replace(world, generations=2, change_every=1)
    run = await FoundryExperiment(changed, FoundryConfig(pooled=True, turnover=0)).run()
    assert any(
        e["adoptions"] == {} for e in run.events if e.get("kind") == "transfer" and e["generation"] == 1
    )
    assert any(a["metadata"]["version"] == 0 for a in run.artifacts)


async def test_custom_usage_and_mutation_survive_only_explicit_outputs(world):
    from swarmkit.types import Usage

    class Metered(FoundryScientist):
        def act(self, context):
            return replace(super().act(context), usage=Usage(calls=1, tokens=7, cost=0.01))

    run = await FoundryExperiment(world, FoundryConfig(trust_reported_usage=True)).run(
        {a: Metered() for a in world.agents}
    )
    assert run.metrics["tokens"] == 7 * run.metrics["agent_calls"]
    assert run.metrics["model_cost"] == pytest.approx(0.01 * run.metrics["agent_calls"])
