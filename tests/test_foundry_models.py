"""Offline model-contract checks: fake transport, real Foundry settlement and treatments."""

import json
from dataclasses import replace
from types import SimpleNamespace

import pytest

from swarmkit.foundry import FoundryConfig, FoundryExperiment, FoundryWorld
from swarmkit.foundry.model_agents import ModelScientist, observation
from swarmkit.foundry.model_study import analyze, cases, episode, freeze, settings
from swarmkit.providers.deepseek import CompletionResult
from swarmkit.types import Usage


def fixture():
    world = FoundryWorld(seed=901, split="dev", firms=2, components=2, generations=2)
    config = FoundryConfig(rounds=4, agent_teams=True, agent_publication=True, artifact_visibility="public")
    exp = FoundryExperiment(world, config)
    data = exp._initial(exp.population(), 0)
    exp._begin(data, 0, 0)
    return exp, data, exp._contexts(data, 0, 1)["firm0.sensor"]


def action(context):
    role = context.agent.id.split(".")[1]
    return dict(
        bid=3,
        query=None,
        preferences={
            r: [a for a in context.task.metadata["members"] if a.endswith("." + r)]
            for r in (("power", "firmware") if role == "sensor" else ("sensor",))
        },
        recipe=[0, 0, 0],
        publish=True,
        forecast=None,
        memory="remember the agreed design",
        messages=[],
    )


class FakeClient:
    model = "deepseek-flash"

    def __init__(self, respond):
        self.respond = respond
        self.calls = 0
        self.gate = SimpleNamespace(status=lambda: {"cost_usd": 0})

    async def complete(self, prompt, **kwargs):
        self.calls += 1
        text = self.respond(json.loads(prompt[-1]["content"]))
        return CompletionResult(
            text, Usage(calls=1, tokens=15, cost=0.001), "fake-request", 10, 5, "stop", "deepseek-flash"
        )


async def test_model_cache_accounts_usage_and_no_oracle(tmp_path):
    exp, data, ctx = fixture()
    client = FakeClient(lambda obs: json.dumps(action(ctx)))
    agent = ModelScientist(client, directory=tmp_path, namespace="test")
    first = await agent.act(ctx)
    second = await agent.act(ctx)
    assert client.calls == 1 and first.usage.tokens == second.usage.tokens == 15
    assert second.decision.metadata["model_audit"]["cached"]
    assert exp.world.id not in json.dumps(agent.prompt(ctx))
    assert "seed" not in observation(ctx)["environment"]
    assert "physics" not in observation(ctx)["environment"]
    exp._validate(ctx.agent.id, first, ctx)


async def test_invalid_output_abstains_with_usage_not_solver(tmp_path):
    _, _, ctx = fixture()
    client = FakeClient(lambda obs: "not JSON")
    output = await ModelScientist(client, directory=tmp_path, namespace="bad").act(ctx)
    assert output.usage.calls == 1
    assert (
        output.decision.metadata["protocol_error"]
        if "protocol_error" in output.decision.metadata
        else output.decision.metadata["model_audit"]["protocol_error"]
    )
    assert output.messages == () and output.decision.metadata["preferences"] == {"power": [], "firmware": []}
    assert output.decision.metadata["query"] is None and not output.decision.metadata["publish"]


@pytest.mark.parametrize(
    "mutation",
    [
        lambda o, c: o.update(query="unknown/0"),
        lambda o, c: o.update(recipe=[True, 0, 0]),
        lambda o, c: o.update(forecast=float("nan")),
        lambda o, c: o.update(
            messages=[dict(recipients=["firm0.power"], content="x", evidence_ids=["forged"])]
        ),
        lambda o, c: o.update(
            messages=[dict(recipients=["firm0.power"], content="x", evidence_ids=[], sender="firm1.sensor")]
        ),
        lambda o, c: o.update(preferences={"power": ["firm0.sensor"], "firmware": []}),
    ],
)
def test_model_rejects_forgery_and_invalid_actions(tmp_path, mutation):
    _, _, ctx = fixture()
    obj = action(ctx)
    mutation(obj, ctx)
    agent = ModelScientist(None, directory=tmp_path, namespace="bad")
    with pytest.raises((ValueError, TypeError)):
        agent.parse(json.dumps(obj), ctx)


def test_inbox_ids_ignored_sender_still_authenticated(tmp_path):
    _, _, ctx = fixture()
    obj = action(ctx)
    obj["messages"] = [
        dict(
            recipients=["firm0.power"], content="proposal", evidence_ids=[], sender=ctx.agent.id, id="copied"
        )
    ]
    out = ModelScientist(None, directory=tmp_path, namespace="ok").parse(json.dumps(obj), ctx)
    assert out.messages[0].sender == ctx.agent.id and out.messages[0].id != "copied"


def test_preferences_control_actual_matching_and_refusal():
    exp, data, ctx = fixture()
    data["bids"] = {a: 3 for a in exp.world.agents}
    data["preferences"] = {
        a: action(replace(ctx, agent=data["state"].agents[a]))["preferences"] for a in exp.world.agents
    }
    data["preferences"]["firm0.sensor"]["power"] = ["firm1.power"]
    data["preferences"]["firm1.power"]["sensor"] = ["firm0.sensor"]
    exp._award(data, 0)
    assert data["assignments"]["order:0:0"][1] == "firm1.power"
    exp, data, ctx = fixture()
    data["bids"] = {a: 3 for a in exp.world.agents}
    data["preferences"] = {
        a: {r: [] for r in (("power", "firmware") if a.endswith(".sensor") else ("sensor",))}
        for a in exp.world.agents
    }
    exp._award(data, 0)
    assert not data["assignments"]


def test_incentives_do_not_change_public_archive_access():
    exp, _, _ = fixture()
    art = SimpleNamespace(author="firm1.sensor")
    assert exp._authorized_artifact("firm0.power", art)
    other = FoundryExperiment(exp.world, replace(exp.config, incentives="private"))
    assert other._authorized_artifact("firm0.power", art)


def test_plan_joint_factors_and_disjoint_worlds():
    plan = cases()
    primary = [c for c in plan if c["kind"] == "primary"]
    assert len(primary) == 48 and len(plan) == 66
    assert len({c["id"] for c in plan}) == 66
    for c in primary:
        world, cfg = settings(c)
        assert world.seed != 901 and world.split == "test"
        assert cfg.agent_teams and cfg.agent_publication and cfg.forecast_market
        assert cfg.artifact_visibility == "public"
        assert world.generations * cfg.rounds * len(world.agents) == 96


def test_manifest_rejects_changed_experiment(tmp_path):
    freeze(tmp_path, cases(), "test")
    freeze(tmp_path, cases(), "test")
    with pytest.raises(ValueError, match="manifest differs"):
        freeze(tmp_path, cases((5,)), "test")


def test_analysis_pairs_worlds_and_computes_interactions():
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
    rows = []
    for c in cases((1, 2)):
        if c["kind"] != "primary":
            continue
        value = 10 if c["protocol"] == "silent" else (30 if c["incentive"] == "shared" else 15)
        rows.append(
            {
                "case": c,
                "status": "complete",
                "metrics": dict.fromkeys(metrics, value)
                | {"private_surplus": {"firm0.sensor": 1, "firm1.sensor": 2}},
            }
        )
    result = analyze(rows)
    assert result["paired_communication_effects"]["shared/stable/targeted"]["mean"] == 20
    assert result["difference_in_differences"]["targeted/incentive/stable"]["mean"] == -15


async def test_model_episode_real_settlement_and_publication(tmp_path):
    c = dict(
        id="test",
        kind="primary",
        seed=901,
        incentive="shared",
        pressure="stable",
        protocol="targeted",
        split="dev",
        pooled=True,
    )
    world, cfg = settings(c)

    def respond(obs):
        public = obs["environment"]
        agent = obs["agent"]
        role = agent.split(".")[1]
        # The fake transport is an oracle solely to test simulator wiring, not a study policy.
        recipe = max(world.recipes, key=lambda r: world.quality(public["version"], r))
        return json.dumps(
            dict(
                bid=3,
                query=None,
                preferences={
                    r: [a for a in world.agents if a.endswith("." + r)]
                    for r in (("power", "firmware") if role == "sensor" else ("sensor",))
                },
                recipe=recipe,
                publish=False,
                forecast=None,
                memory="",
                messages=[],
            )
        )

    client = FakeClient(respond)
    run = await episode(c, client, tmp_path)
    assert run["metrics"]["success_rate"] == 1
    assert run["metrics"]["publication_count"] == 0 and run["artifacts"] == []
    assert run["metrics"]["outstanding_reservations"] == 0
    assert run["metrics"]["agent_calls"] == 96 and client.calls == 96
    assert run["metrics"]["tokens"] == 1440


def test_artifact_reference_does_not_forge_measurement(tmp_path):
    from swarmkit.types import Artifact

    _, _, ctx = fixture()
    artifact = Artifact(
        "device:order:0:0", "firm0.sensor", {"recipe": [0, 0, 0], "quality": 25}, metadata={"version": 0}
    )
    ctx = replace(ctx, artifacts=(artifact,))
    obj = action(ctx)
    obj["messages"] = [
        dict(recipients=["firm0.power"], content="Read this recipe", evidence_ids=[artifact.id])
    ]
    out = ModelScientist(None, directory=tmp_path, namespace="refs").parse(json.dumps(obj), ctx)
    assert not out.messages[0].evidence
    assert out.messages[0].metadata["artifact_ids"] == [artifact.id]


def test_prompt_cap_discloses_omitted_messages(tmp_path):
    from swarmkit.types import Message

    _, _, ctx = fixture()
    ctx = replace(
        ctx, messages=tuple(Message("firm1.sensor", str(i) + "x" * 800, id=str(i)) for i in range(50))
    )
    agent = ModelScientist(None, directory=tmp_path, namespace="cap")
    prompt = agent.prompt(ctx)
    from swarmkit.foundry.model_agents import encode

    assert len(encode(prompt).encode()) <= 24000
    obs = json.loads(prompt[-1]["content"])
    assert obs["omitted"]["messages"] > 0
    assert obs["messages"][-1]["id"] == "49"
    assert len(obs["evidence"]) == len(ctx.agent.private_evidence)


def test_hub_protocol_is_enforced(tmp_path):
    _, data, ctx = fixture()
    ctx = replace(ctx, agent=data["state"].agents["firm0.power"])
    obj = action(ctx)
    obj["messages"] = [dict(recipients=["firm1.sensor"], content="bypass hub", evidence_ids=[])]
    agent = ModelScientist(None, directory=tmp_path, namespace="hub", protocol="coordinator")
    with pytest.raises(ValueError, match="hub"):
        agent.parse(json.dumps(obj), ctx)
    obj["messages"][0]["recipients"] = ["firm0.sensor"]
    assert agent.parse(json.dumps(obj), ctx).messages[0].recipients == ("firm0.sensor",)


async def test_invalid_commit_cannot_receive_accidental_default_payment(tmp_path):
    from swarmkit.types import AgentOutput, Decision

    # Choose a world in which index-zero fallback is physically acceptable.
    world = next(
        w
        for seed in range(100)
        if (w := FoundryWorld(seed=seed, firms=2, components=2, generations=1)).verify(
            0, [0, 0, 0], 5, w.orders(0)[0]
        )["success"]
    )

    class Agent:
        def act(self, ctx):
            metadata = {"bid": 3, "query": None, "publish": True}
            if ctx.phase == "commit":
                metadata["model_audit"] = {"protocol_error": "invalid JSON"}
            return AgentOutput(decision=Decision(ctx.agent.id, "[0,0,0]", metadata=metadata))

    run = await FoundryExperiment(world, FoundryConfig(rounds=3, agent_publication=True)).run(
        {a: Agent() for a in world.agents}
    )
    assert run.metrics["accepted_value"] == 0
    assert run.metrics["outstanding_reservations"] == 0
    assert all(o["reason"] == "invalid_commitment" for o in run.outcomes)
    assert not run.artifacts
    assert all(run.metrics["balances"][a] == 100 for a in world.agents)
