import json
from dataclasses import replace

import numpy as np
import pytest

from swarmkit.economics import (
    AlphaRankEvaluator,
    AlternatingOffers,
    CombinatorialAuction,
    CongestionGame,
    ContractNet,
    CoreDiagnostic,
    DeferredAcceptance,
    DoubleAuction,
    EconomicAction,
    EconomicArena,
    EconomicHyperedge,
    ExternalRegretPolicy,
    FictitiousPlay,
    FirstPriceAuction,
    FramingAndDisclosurePolicy,
    GroupHistoryQPolicy,
    HypergraphPublicGoods,
    InternalRegretPolicy,
    LearnedAuction,
    Ledger,
    LMSRMarket,
    LOLAAdapter,
    MultiTypeMeanField,
    NashBargaining,
    NegotiationSelfPlay,
    NormalFormGame,
    OpenSpielCFR,
    POLAAdapter,
    PolicySpaceResponseOracles,
    PrivateType,
    RepeatedGame,
    RestrictedCoalitionValue,
    ReverseAuction,
    SecondPriceAuction,
    Settlement,
    ShapleyEstimator,
    ThresholdTeamGame,
    TwoLevelInstitution,
    VCGPayments,
    equilibrium_violations,
    fixed,
    generous_reciprocity,
    tit_for_tat,
    win_stay_lose_shift,
)
from swarmkit.types import Artifact, Evidence, Feedback

PD = [[[3, 3], [0, 5]], [[5, 0], [1, 1]]]


def test_normal_form_known_equilibrium_and_matching_pennies():
    game = NormalFormGame(PD)
    assert game.pure_equilibria() == [(1, 1)]
    np.testing.assert_allclose(game.expected([[1, 0], [1, 0]]), [3, 3])
    np.testing.assert_allclose(game.deviation_gains([[1, 0], [1, 0]]), [2, 2])
    pennies = NormalFormGame([[[1, -1], [-1, 1]], [[-1, 1], [1, -1]]])
    np.testing.assert_allclose(pennies.deviation_gains([[0.5, 0.5], [0.5, 0.5]]), 0)
    assert equilibrium_violations(pennies, np.full((2, 2), 0.25)) == {
        "ce_violation": [0, 0],
        "cce_violation": [0, 0],
    }
    for actions in ((-1, 0), (2, 0), (0,)):
        with pytest.raises(ValueError):
            game.utilities(actions)


def test_repeated_reciprocity_and_noise_are_reproducible():
    game = RepeatedGame(NormalFormGame(PD))
    result = game.run([tit_for_tat, fixed(1)], rounds=3)
    assert result["actions"] == [(0, 1), (1, 1), (1, 1)]
    np.testing.assert_allclose(result["utility"], [2, 7])
    assert generous_reciprocity(1)([(1, 1, 1)], np.random.default_rng()) == 0
    assert win_stay_lose_shift()([(0, 1, 0)], None) == 1
    noisy = RepeatedGame(NormalFormGame(PD), observation_noise=1)
    assert noisy.run([tit_for_tat, fixed(0)], rounds=2)["actions"] == [(0, 0), (1, 0)]


def test_public_goods_degree_budget_and_threshold_complementarity():
    contributions = {"a": 1, "b": 1, "c": 1}
    edges = [("a", "b"), ("b", "c")]
    agent = HypergraphPublicGoods(edges, 2, "agent").utilities(contributions)
    edge = HypergraphPublicGoods(edges, 2, "edge").utilities(contributions)
    assert sum(agent.values()) == 3
    assert sum(edge.values()) == 4
    team = ThresholdTeamGame({"a": ["scout"], "b": ["review"]}, ["scout", "review"], 10, {"a": 1, "b": 2})
    assert team.utilities(["a"]) == {"a": -1, "b": 0}
    assert team.utilities(["a", "b"]) == {"a": 4, "b": 3}


def test_congestion_potential_change_equals_unilateral_cost_change():
    game = CongestionGame({"x": lambda n: n, "y": lambda n: 2 * n})
    before, after = {"a": ["x"], "b": ["x"]}, {"a": ["y"], "b": ["x"]}
    assert (
        game.potential(after) - game.potential(before)
        == game.utilities(before)["a"] - game.utilities(after)["a"]
    )


@pytest.mark.parametrize("bad", [float("nan"), float("inf"), -1])
def test_ledger_rejects_invalid_funding(bad):
    with pytest.raises(ValueError):
        Ledger({"a": bad})


def test_atomic_ledger_reservations_inventory_and_json_retry():
    ledger = Ledger({"a": 10, "b": 0}, {"a": {"tool": 1}})
    ledger.reserve("edge1", "a", 7)
    with pytest.raises(ValueError):
        ledger.reserve("edge2", "a", 4)
    before = ledger.snapshot()
    with pytest.raises(ValueError):
        ledger.settle(Settlement("bad", {"a": -5, "b": 5}, {"a": {"tool": -2}, "b": {"tool": 2}}, ("edge1",)))
    assert ledger.snapshot() == before
    transaction = Settlement("good", {"a": -7, "b": 7}, {"a": {"tool": -1}, "b": {"tool": 1}}, ("edge1",))
    assert ledger.settle(transaction)
    restored = Ledger.restore(json.loads(json.dumps(ledger.snapshot())))
    assert not restored.settle(transaction)
    assert restored.balances == {"a": 3, "b": 7}
    assert restored.inventories["b"]["tool"] == 1
    with pytest.raises(ValueError):
        restored.settle(replace(transaction, transfers={"a": -1, "b": 1}))


def test_auctions_payments_reserves_ties_and_budget():
    bids = {"b": 9, "a": 9, "c": 4}
    assert FirstPriceAuction().clear(bids) == {"winner": "a", "payment": 9}
    assert SecondPriceAuction().clear({"a": 9, "b": 4})["payment"] == 4
    assert SecondPriceAuction(reserve=3).clear({"a": 9})["payment"] == 3
    assert FirstPriceAuction(reserve=10).clear(bids)["winner"] is None
    assert ReverseAuction(10).clear({"a": 5, "b": 3}) == {"winner": "b", "payment": 3}
    with pytest.raises(ValueError):
        FirstPriceAuction(budgets={"a": 5}).clear(bids)


def test_exact_bundle_vcg_complementarity_and_truthful_small_grid():
    auction = VCGPayments(CombinatorialAuction(["x", "y"]))
    bids = {"team": {("x", "y"): 10}, "a": {("x",): 4}, "b": {("y",): 5}}
    result = auction.clear(bids)
    assert result["allocation"] == {"team": frozenset(("x", "y"))}
    assert result["payments"] == {"team": 9, "a": 0, "b": 0}
    for reported in range(15):
        changed = bids | {"team": {("x", "y"): reported}}
        r = auction.clear(changed)
        utility = (10 if "team" in r["allocation"] else 0) - r["payments"]["team"]
        assert utility <= 1 + 1e-9
    with pytest.raises(ValueError):
        CombinatorialAuction(["x"], max_allocations=1).clear({"a": {("x",): 1}})


def test_double_auction_balanced_surplus():
    trades = DoubleAuction().clear({"a": 10, "b": 2}, {"c": 4, "d": 8})
    assert trades == [{"buyer": "a", "seller": "c", "price": 7, "surplus": 6}]


def test_matching_has_no_blocking_pair():
    proposers = {"a": ["x", "y"], "b": ["x", "y"], "c": ["y"]}
    receivers = {"x": ["b", "a"], "y": ["a", "b", "c"]}
    match = DeferredAcceptance().clear(proposers, receivers)
    assert match == {"b": "x", "a": "y"}
    reverse = {r: p for p, r in match.items()}
    for p, prefs in proposers.items():
        for r in prefs:
            wants = p not in match or prefs.index(r) < prefs.index(match[p])
            accepts = p in receivers[r] and (
                r not in reverse or receivers[r].index(p) < receivers[r].index(reverse[r])
            )
            assert not (wants and accepts)


def test_contract_verified_only_and_retry_payment():
    ledger = Ledger({"buyer": 10, "scout": 0, "review": 0})
    net = ContractNet(ledger)
    offers = {"team": {"members": ["scout", "review"], "capabilities": ["s", "r"], "cost": 6}}
    net.award("c1", "t1", "buyer", ["s", "r"], offers)
    assert ledger.available("buyer") == 4
    artifact = Artifact("out", "scout", "work", metadata={"task_id": "t1", "contract_id": "c1"})
    with pytest.raises(ValueError):
        net.complete("c1", replace(artifact, author="stranger"), lambda a: Feedback(1, verified=True))
    assert net.complete("c1", artifact, lambda a: Feedback(1, verified=True))
    assert net.complete("c1", artifact, lambda a: pytest.fail("must not verify/pay twice"))
    assert ledger.balances == {"buyer": 4, "scout": 3, "review": 3}
    net.award("c2", "t2", "buyer", [], {"s": {"members": ["scout"], "capabilities": [], "cost": 2}})
    failed = replace(artifact, metadata={"task_id": "t2", "contract_id": "c2"})
    assert not net.complete("c2", failed, lambda a: Feedback(0, verified=False))
    assert ledger.available("buyer") == 4


def test_bargaining_disagreement_deadline_and_finite_nash():
    result = NashBargaining().solve([[1, 9], [5, 5], [9, 1]], [0, 0])
    assert result["index"] == 1
    assert NashBargaining().solve([[0, 0]], [1, 1]) is None
    protocol = AlternatingOffers(discounts=(0.9, 0.9))
    assert not protocol.run([lambda t, h: [0.5, 0.5]] * 2, [lambda o, t, h: False] * 2, 2)["agreement"]
    result = protocol.run([lambda t, h: [0.5, 0.5]] * 2, [lambda o, t, h: t == 1] * 2, 2)
    np.testing.assert_allclose(result["utility"], [0.45, 0.45])


def test_shapley_dummy_symmetry_efficiency_and_core():
    def value(c):
        return 6 if {"a", "b"} <= c else 0

    result = ShapleyEstimator(["a", "b", "dummy"], value).estimate(exact=True)
    assert result["values"] == {"a": 3, "b": 3, "dummy": 0}
    sampled = ShapleyEstimator(["a", "b"], value).estimate(samples=100, seed=1)
    assert sum(sampled["values"].values()) == 6
    assert CoreDiagnostic().evaluate(["a", "b"], value, {"a": 3, "b": 3})["in_core"]
    assert not CoreDiagnostic().evaluate(["a", "b"], value, {"a": -1, "b": 7})["in_core"]
    restricted = RestrictedCoalitionValue(lambda c: len(c) ** 2, [("a", "b")])
    assert restricted({"a", "b", "c"}) == 5


def test_lmsr_prices_budget_bound_and_retries():
    ledger = Ledger({"market": 10, "a": 20})
    market = LMSRMarket(2, liquidity=10)
    np.testing.assert_allclose(market.prices(), [0.5, 0.5])
    price = market.trade(ledger, "t1", "a", [3, 0])
    assert 1.5 < price < 3
    assert market.trade(ledger, "t1", "a", [3, 0]) == price
    assert market.prices()[0] > 0.5
    assert market.resolve(ledger, 0)
    assert not market.resolve(ledger, 0)
    assert ledger.balances["a"] == pytest.approx(20 - price + 3)
    assert 10 - ledger.balances["market"] <= 10 * np.log(2)


@pytest.mark.parametrize("method", ["hedge", "regret_matching"])
def test_external_regret_prefers_better_action(method):
    learner = ExternalRegretPolicy(2, method)
    for _ in range(500):
        learner.update([1, 0])
    assert learner.probabilities()[0] > 0.99
    assert learner.regret / 500 < 0.05
    with pytest.raises(ValueError):
        learner.update([2, 0])


def test_internal_regret_tracks_conditional_deviations():
    policy = InternalRegretPolicy(2)
    policy.update(0, [0, 1])
    assert policy.swap_regret == 1
    np.testing.assert_allclose(policy.probabilities(), [0.5, 0.5])
    policy.update(1, [0, 1])
    np.testing.assert_allclose(policy.probabilities(), [0, 1])
    fp = FictitiousPlay(NormalFormGame(PD), 0)
    fp.update((0, 0))
    np.testing.assert_allclose(fp.probabilities(), [0, 1])


def test_group_q_and_mean_field_role_separation():
    q = GroupHistoryQPolicy(rate=1, discount=0.5)
    s = q.state(0, [0, 1])
    q.update(s, 0, 2, s, terminal=True)
    assert q.values(s)[0] == 2
    mf = MultiTypeMeanField(["worker", "planner"], 2, rate=1)
    means = mf.means([("worker", 0), ("worker", 1), ("planner", 1)])
    np.testing.assert_allclose(means["worker"], [0.5, 0.5])
    mf.update("worker", "s", means, 1, 3, "s", means, terminal=True)
    assert mf.values("worker", "s", means)[1] == 3
    assert mf.values("planner", "s", means)[1] == 0


def test_psro_crossplay_and_response_population():
    solver = PolicySpaceResponseOracles([[0], [0]], lambda a, b: (float(a != b), float(a == b)))
    result = solver.expand(lambda i, p, m: 1, iterations=10)
    assert result["payoffs"].shape == (1, 1, 2)
    assert solver.payoff_game().shape == (2, 2)


def test_alpharank_stationarity_and_neutral_symmetry():
    game = np.zeros((2, 3, 2))
    result = AlphaRankEvaluator().evaluate(game)
    np.testing.assert_allclose(result["mass"], np.full(6, 1 / 6))
    pd = AlphaRankEvaluator(alpha=0.1).evaluate(PD)
    np.testing.assert_allclose(pd["mass"] @ pd["transition"], pd["mass"])
    assert pd["mass"][-1] > pd["mass"][0]


def test_lola_includes_opponent_shaping_derivative():
    # V1=x*y, V2=x*y: stop-gradient(x) in the shaping term gives derivative y + eta*x.
    result = LOLAAdapter(rate=0.1, opponent_rate=0.2).step(
        np.array([1.0]), np.array([2.0]), lambda x, y: (x * y).sum(), lambda x, y: (x * y).sum()
    )
    np.testing.assert_allclose(result, [1.22], atol=1e-5)


def test_pola_requires_policy_kl_and_updates_nested_response():
    adapter = POLAAdapter(rate=0.05, inner_steps=3, outer_steps=2)

    # Bernoulli policies parameterized by logits.
    def kl(a, b):
        p, q = 1 / (1 + np.exp(-a)), 1 / (1 + np.exp(-b))
        return float(np.sum(p * np.log(p / q) + (1 - p) * np.log((1 - p) / (1 - q))))

    result = adapter.step(
        np.array([0.0]),
        np.array([0.0]),
        lambda x, y: -((x[0] - 1) ** 2) + y[0],
        lambda x, y: -((y[0] - x[0]) ** 2),
        kl,
        kl,
    )
    assert 0 < result[0] < 1


def test_learned_auction_feasible_ir_training_and_deviations():
    auction = LearnedAuction(2)
    values = [[1.0, 2.0], [2.0, 1.0]]
    before = auction._theta().copy()
    history = auction.fit(values, [0.0, 1.0, 2.0], steps=2)
    assert len(history) == 2 and not np.allclose(before, auction._theta())
    for value in values:
        result = auction.clear(value)
        assert result["allocation"].sum() <= 1
        assert np.all(result["payments"] <= result["allocation"] * value)
    assert auction.evaluate([[3.0, 4.0]], [0, 1, 3, 4])["max_tested_regret"] >= 0


def test_institution_and_negotiation_invoke_actual_updates():
    institution = TwoLevelInstitution(
        1, 0, lambda r, w, s: w + r, lambda r, w, s: w, lambda r, w, score, s: r + 1
    )
    history = institution.fit(2)
    assert [h["score"] for h in history] == [1, 3]
    assert institution.rule == 3
    assert institution.held_out(7, [9]) == [7]

    def rollout(a, b, seed):
        return {"valid": True, "utilities": [a, b], "transcript": []}

    trainer = NegotiationSelfPlay([1, 2], rollout, lambda p, role, episodes: p + 1)
    trainer.fit(rounds=2, episodes_per_round=1)
    assert trainer.policies == [3, 4]
    assert len(trainer.cross_play([5], [1, 2])) == 4
    assert trainer.policies == [3, 4]


def test_disclosure_preserves_original_facts():
    cards = [Evidence("a", "actual fact", "source", "owner")]
    selected = FramingAndDisclosurePolicy().select(
        cards, [(("a",), "neutral"), ((), "omit")], lambda e, f: {"sender_utility": len(e)}
    )
    assert selected["evidence"] == tuple(cards)
    with pytest.raises(ValueError):
        FramingAndDisclosurePolicy().select(cards, [(("fake",), "")], lambda e, f: {})


def test_economic_arena_sealed_round_atomic_failure_and_checkpoint():
    edge = EconomicHyperedge("edge", ("a", "b"), "transfer")
    ledger = Ledger({"a": 10, "b": 0})
    private = {"a": PrivateType(values={"secret": 1}), "b": PrivateType(values={"secret": 99})}
    observed = []

    def strategy(obs):
        observed.append(obs)
        return EconomicAction(obs.edge_id, obs.round, obs.agent_id, "bid", 1)

    def clearing(e, actions, staged):
        return Settlement(f"{e.id}:{actions['a'].round}", {"a": -2, "b": 2})

    arena = EconomicArena([edge], private, ledger, {"transfer": clearing})
    arena.run_round("edge", {"a": strategy, "b": strategy})
    assert observed[0].private_type.values == {"secret": 1}
    assert observed[0].public == observed[1].public == {}
    snapshot = json.loads(json.dumps(arena.snapshot()))
    arena.run_round("edge", {"a": strategy, "b": strategy})
    arena.restore(snapshot)
    assert ledger.balances == {"a": 8, "b": 2}
    assert arena.rounds == {"edge": 1}
    arena.mechanisms["transfer"] = lambda e, a, ledger: Settlement("edge:1", {"a": -100, "b": 100})
    with pytest.raises(ValueError):
        arena.run_round("edge", {"a": strategy, "b": strategy})
    assert ledger.balances == {"a": 8, "b": 2} and arena.rounds["edge"] == 1


@pytest.mark.parametrize("variant", ["cfr", "cfr_plus", "external_sampling", "outcome_sampling"])
def test_openspiel_real_kuhn_solver(variant):
    pytest.importorskip("pyspiel")
    solver = OpenSpielCFR(variant=variant)
    before = solver.exploitability()
    solver.train(100)
    assert solver.exploitability() < before


def test_all_26_research_candidates_have_public_implementations_and_registry_entries():
    from pathlib import Path

    import swarmkit.economics as economics
    from swarmkit.catalog import resolve

    candidates = json.loads(Path("sources/economic-games/method-candidates.json").read_text())["candidates"]
    assert len(candidates) == 26
    for candidate in candidates:
        assert candidate["implementation_status"] != "proposed_not_implemented"
        assert resolve("economic_" + candidate["id"]) is getattr(economics, candidate["implemented_api"][0])
        for api in candidate["proposed_api"]:
            assert callable(getattr(economics, api))


def test_optional_structure_adapters_preserve_group_identity():
    pytest.importorskip("hypernetx")
    pytest.importorskip("xgi")
    from swarmkit.economics import HyperNetXAdapter, XGIAdapter

    edges = [EconomicHyperedge("team", ("a", "b", "c"), "public_goods")]
    assert set(HyperNetXAdapter.convert(edges).edges["team"]) == {"a", "b", "c"}
    assert XGIAdapter.convert(edges).edges.members("team") == {"a", "b", "c"}


def test_optional_negmas_runs_actual_negotiation():
    pytest.importorskip("negmas")
    from swarmkit.economics import NegMASNegotiation

    result = NegMASNegotiation().run([{(0,): 1, (1,): 0}, {(0,): 1, (1,): 0}], [0, 0])
    assert result["agreement"] == (0,) and result["utilities"] == [1, 1]


def test_market_reserves_worst_outcome_and_rolls_back_unfunded_trade():
    ledger = Ledger({"market": 0, "a": 20})
    market = LMSRMarket(2)
    before = ledger.snapshot()
    with pytest.raises(ValueError):
        market.trade(ledger, "unfunded", "a", [3, 0])
    assert ledger.snapshot() == before
    np.testing.assert_allclose(market.q, [0, 0])
    funded = Ledger({"market": 10, "a": 20, "other": 0})
    market.trade(funded, "funded", "a", [3, 0])
    assert funded.reservations["market-collateral:market"] == ("market", 3)
    with pytest.raises(ValueError):
        funded.settle(Settlement("steal-collateral", {"market": -10, "other": 10}))
    market.trade(funded, "sell", "a", [-1, 0])
    assert funded.reservations["market-collateral:market"] == ("market", 2)
    market.resolve(funded, 0)
    assert "market-collateral:market" not in funded.reservations


def test_ledger_retry_normalizes_nested_json_metadata():
    ledger = Ledger({"a": 1, "b": 0})
    event = Settlement("s", {"a": -1, "b": 1}, metadata={"members": ("a", "b")})
    ledger.settle(event)
    restored = Ledger.restore(json.loads(json.dumps(ledger.snapshot())))
    assert not restored.settle(event)


def test_stackelberg_tie_rule_changes_optimal_commitment():
    from swarmkit.economics import StackelbergContractGame

    leader, follower = [[10, 0], [4, 4]], [[1, 1], [0, 2]]
    assert StackelbergContractGame(leader, follower, "strong").solve()["leader_action"] == 0
    assert StackelbergContractGame(leader, follower, "weak").solve()["leader_action"] == 1
    assert StackelbergContractGame(leader, follower).solve(outside_option=3) is None
