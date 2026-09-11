# Economic games: implementation and usage

All **26 candidate entries** from [the research catalog](../sources/economic-games/method-candidates.json) have public implementations in `swarmkit.economics`. These include exact small-game components, numerical research adaptations, training coordinators with explicit callbacks, and an optional OpenSpiel solver adapter. The table below distinguishes them. None is a claim to reproduce every experiment in the cited papers.

The core still requires only NumPy. Discover methods with `python -m swarmkit list --family economics`. Run `python examples/economic_games.py` for verified team procurement, exact complementary bundle allocation, and repeated reciprocity.

## Start with a mechanism

```python
from swarmkit.economics import CombinatorialAuction, VCGPayments

auction = VCGPayments(CombinatorialAuction(["gpu", "dataset"]))
result = auction.clear({
    "team": {("gpu", "dataset"): 10},
    "gpu-only": {("gpu",): 4},
    "data-only": {("dataset",): 5},
})
assert result["payments"]["team"] == 9
```

This exact XOR auction allocates at most one bundle per bidder and each item once. It enumerates feasible combinations and raises at a configured enumeration limit. VCG uses exact leave-one-bidder-out welfare. The usual truthfulness interpretation assumes quasilinear private values and this exact allocation domain; adding hard budgets or approximate clearing changes the claim.

## What to use and when

| Catalog entry | Public API | Implemented behavior and boundary |
|---|---|---|
| Normal form | `NormalFormGame` | Finite payoff tensors, mixed expected utilities, action values, pure equilibria and unilateral deviation gains |
| Repeated games | `RepeatedGame` | Two-player binary actions, discount, continuation and observation noise; fixed, tit-for-tat, generous and win-stay/lose-shift controls |
| Public goods | `HypergraphPublicGoods` | Linear returns over overlapping groups; explicit per-agent versus per-edge contribution cost |
| Threshold coalitions | `ThresholdTeamGame` | Capability complements, joining costs and equal gross reward; original task adaptation |
| Contract Net | `ContractNet` | Capability/cost team award, escrow, independently verified completion, equal team payout, cancellation and retry identity |
| Single-item auctions | `FirstPriceAuction`, `SecondPriceAuction`, `ReverseAuction` | Nonnegative bids/asks, deterministic ID ties, reserves/budgets; reverse auction is first-price procurement |
| Bundle auctions | `CombinatorialAuction`, `VCGPayments` | Exact finite XOR allocation and externality payments; exponential enumeration bounded explicitly |
| Double auction | `DoubleAuction` | One unit per participant, sorted call-market matching and pairwise midpoint payments; budget balanced, not truthful |
| Congestion | `CongestionGame` | Unweighted resource routes and Rosenthal potential; caller supplies pure load-latency functions |
| Stable matching | `DeferredAcceptance` | One-to-one strict incomplete preferences, mutual acceptability, proposer-oriented deferred acceptance |
| Bargaining | `AlternatingOffers`, `NashBargaining` | Finite divisible-pie dialogue with disagreement/discounts; separately, weighted Nash product on finite feasible utility vectors |
| Coalition value | `ShapleyEstimator`, `CoreDiagnostic`, `RestrictedCoalitionValue` | Exact or sampled permutation contributions with standard errors, exhaustive blocking tests, connected-component restriction |
| Prediction market | `LMSRMarket` | Stable log-sum-exp prices, long-only positions, reserved worst-outcome collateral, atomic trades and oracle settlement |
| External regret | `ExternalRegretPolicy` | Full-information Hedge or external regret matching with [0,1] utilities; accumulated external regret |
| Internal regret | `InternalRegretPolicy` | Pairwise conditional regret transitions with bounded full feedback; measured swap regret |
| CFR | `OpenSpielCFR` | Real CFR, CFR+, external-sampling and outcome-sampling implementations; optional dependency |
| PSRO | `PolicySpaceResponseOracles` | Two-role cross-play, external-regret empirical meta-solver and caller response oracle; restricted product deviations reported |
| AlphaRank | `AlphaRankEvaluator` | Finite-selection multi-population Moran chain and dense stationary solve; extreme numerical regimes rejected |
| Opponent shaping | `LOLAAdapter`, `POLAAdapter` | Small numerical expected-value updates. LOLA freezes the influence factor in the original backward-pass correction. POLA uses finite nested policy-KL proximal steps |
| Mean field | `MultiTypeMeanField` | Role-specific binned-neighbor tabular Q learning; no neural actor-critic implementation |
| Learned auctions | `LearnedAuction` | Small single-item fractional allocation/payment network, finite-difference revenue-minus-tested-regret training; not full RegretNet |
| Learned institutions | `TwoLevelInstitution` | Actual alternating worker/planner callback updates, history and held-out evaluation; application supplies environment and learning backend |
| Group-history Q | `GroupHistoryQPolicy` | Own action plus other-action histogram states and tabular Q updates; own reward, not implicit altruism |
| Language self-play | `NegotiationSelfPlay` | Validated structured rollout batches, policy-training callbacks, held-out partner cross-play; application supplies model and verifier |
| Information design | `FramingAndDisclosurePolicy` | Search original fact subsets/orderings and separate framing labels against caller metrics; no fabricated fact rewriting |
| Leader–follower | `StackelbergContractGame` | Exact finite pure commitments and follower responses, strong/weak tie rule and optional participation threshold; not mixed commitment optimization |

All proposed API names are importable. Variants outside these stated domains—such as continuous double auctions, arbitrary many-to-many matching, full neural training recipes, and unrestricted language response optimization—are not silently substituted for the implemented models.

## Attach a game to a persistent group

```python
from swarmkit.economics import (
    EconomicAction, EconomicArena, EconomicHyperedge, Ledger, PrivateType, Settlement,
)

edge = EconomicHyperedge("market", ("buyer", "seller"), "posted_price")
ledger = Ledger({"buyer": 10, "seller": 0})

def strategy(observation):
    # Only this participant's PrivateType is supplied.
    return EconomicAction(observation.edge_id, observation.round,
                          observation.agent_id, "accept", True)

def clear(edge, actions, staged_ledger):
    agreed = all(action.kind == "accept" and action.payload is True for action in actions.values())
    transfers = {"buyer": -3, "seller": 3} if agreed else {}
    return Settlement(f"{edge.id}:{actions['buyer'].round}", transfers)

arena = EconomicArena([edge], {
    "buyer": PrivateType(values={"work": 5}),
    "seller": PrivateType(costs={"work": 2}),
}, ledger, {"posted_price": clear})
arena.run_round("market", {"buyer": strategy, "seller": strategy})
assert ledger.balances == {"buyer": 7, "seller": 3}
```

`EconomicArena` collects all actions before clearing. It checks edge/round/participant identities and settles on a copy before committing. No sealed actions enter the ordinary message bus. Public feedback is empty unless a trusted `disclose(settlement)` callback explicitly supplies it. Mechanism functions and private types remain caller configuration; `arena.snapshot()` contains balances, reservations, public state, rounds and settlement history. Restore into an arena configured with the same edges, types and mechanism registry. A snapshot can be kept in `SwarmState.data`; it is authoritative state and must not be broadcast to agents.

Overlapping groups share one `Ledger`. Reservations impose an **ordered clearing policy**, so order is part of the experiment. All transfer and inventory accounts must exist; funded treasury/subsidy accounts are explicit participants. Credits and stock are conserved; invalid settlements leave ledger state unchanged. This is a local floating-point research ledger, not a financial production service. Trusted callbacks and application state must be isolated separately.

For delayed work, use `ContractNet.award()` then `complete()`. Artifacts must carry matching `task_id` and `contract_id` metadata and a team author. A caller verifier returns `Feedback(verified=True)` only after checking the work. Rejected delivery releases escrow without paying; repeated completion cannot pay twice. Capability claims remain submitted declarations; validate them in the application. `cancel()` releases an outstanding award.

## Learn and evaluate strategies

```python
from swarmkit.economics import ExternalRegretPolicy

policy = ExternalRegretPolicy(3, method="hedge")
for _ in range(100):
    probabilities = policy.probabilities()
    policy.update([0.2, 0.8, 0.4])  # requires counterfactual utility for EVERY action
assert policy.probabilities()[1] > 0.9
```

Use `FictitiousPlay` for empirical-opponent best responses. Use `equilibrium_violations(game, joint)` for exact CE/CCE deviations in a small empirical joint distribution. PSRO's averaged joint play and product of its marginals are different objects; the latter need not be an equilibrium in general-sum games. Keep training partners and evaluation partners separate. AlphaRank ranks a supplied payoff population; it does not certify Nash or optimize task welfare.

`LearnedAuction.fit()` accepts explicit training valuations and a misreport grid. Evaluate on new valuations and a larger/stronger grid. `max_tested_regret` is a lower bound on unrestricted worst-case gain, not DSIC. Fractional allocations are expected allocations; a realized auction must sample a feasible winner before transferring a physical item.

LOLA/POLA callbacks must return deterministic differentiable expected utilities. POLA additionally requires policy-distribution KL callbacks. Finite differences scale poorly with parameter dimension; these are for small controlled experiments. `TwoLevelInstitution` and `NegotiationSelfPlay` execute supplied learning callbacks; they do not provide pretrained language policies or train a provider API by themselves.

## Optional upstream integrations

```sh
pip install -e '.[economics-solvers,hypergraphs]'
```

```python
from swarmkit.economics import OpenSpielCFR
solver = OpenSpielCFR("kuhn_poker", variant="cfr")
solver.train(100)
print(solver.exploitability())
```

`NegMASNegotiation.run()` takes finite utility maps over outcome tuples, reservation utilities and optional negotiator factories. `HyperNetXAdapter.convert(edges)` and `XGIAdapter.convert(edges)` export group incidence with stable edge IDs for structural analysis. Exports do not copy private economic state. Optional libraries are imported only when those adapters are used; core imports work without them.

These adapters were exercised against OpenSpiel 2.0.2, NegMAS 0.16.0, HyperNetX 2.4.3 and XGI 0.10.2. Their reference interfaces are documented in [OpenSpiel](https://openspiel.readthedocs.io/en/latest/), [NegMAS](https://negmas.readthedocs.io/en/v0.11.1/tutorials/01.running_simple_negotiation.html), [HyperNetX](https://hypernetx.readthedocs.io/en/latest/hypconstructors.html), and [XGI](https://xgi.readthedocs.io/en/stable/api/core/xgi.core.hypergraph.Hypergraph.html).

## Validation and limits

`tests/test_economics.py` exercises hand-solvable games, VCG misreports, matching stability, coalition axioms, market funding, transaction rollback, retry consistency, private observations, training updates and real optional integrations when installed. The [research guide](ECONOMIC_GAMES_RESEARCH.md) supplies sources and assumptions; [communication experiments](COMMUNICATION_EVAL_USAGE.md) provide a way to test whether communication changes independently verified task outcomes. Economic payoffs alone are not evidence that a swarm performs useful work better.
