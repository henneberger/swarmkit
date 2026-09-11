# Research Foundry

A runnable, synthetic research-and-production economy for experiments on **how private discoveries become useful collective work**. Agents investigate components, communicate, bid for team membership, commit to designs, execute resource-constrained jobs and receive independently verified outcomes. Successful devices become persistent artifacts. Physics changes and staff turnover test recovery.

For the live DeepSeek V4.1 Flash program, see the [integrated model experiment](FOUNDRY_MODEL_EXPERIMENT.md). It uses model-chosen partner rankings and publication instead of the offline defaults below, and independently controls artifact visibility and incentives.

## Run it

```sh
# One complete 12-agent, four-generation world, with transcripts and delivery logs.
python -m swarmkit.foundry run --traces --output foundry-run.json

# Four communication policies × two incentives × two allowances, plus silent controls.
python -m swarmkit.foundry study --worlds 3 --output foundry-study.json

# Add message/artifact factorial endpoints and a pooled-information diagnostic.
python -m swarmkit.foundry study --worlds 3 --extra-controls --output foundry-controls.json

# Partner cross-play using actual production payoffs.
python -m swarmkit.foundry cross-play --firms 2 --incentives private --worlds 3 --output foundry-crossplay.json

# Paired ablation and message-removal example.
python examples/research_foundry.py
```

These commands use deterministic Python scientists. They make no provider calls. CLI runs explicitly record zero model tokens/cost; custom-agent runs leave usage unknown by default. Three worlds are a smoke experiment, not a sample-size or generalization claim.

The checked-in [78-run smoke summary](experiments/foundry-smoke.json) records seeds, conditions, measurements and paired comparisons. At the 48-message allowance, mean accepted value was 766.67 for shared-objective broadcast and 460 for its silent control; removing artifacts reduced broadcast to 745. Private-objective targeted messaging scored 400 against its silent control's 460. These scripted examples demonstrate that communication can help or hurt under different strategies; three worlds do not establish a reliable strategy ranking.

## What agents actually do

A world starts with four firms, each containing a sensor, power and firmware specialist. An order specifies minimum device quality, a deadline, value and procurement budget. A recipe chooses one component for each specialty.

Quality is the sum of three hidden component qualities and a hidden whole-recipe interaction. Individual component measurements cannot determine the interaction table. Measurements initially belong to different specialists; later investigations expose one specialty-permitted fact at a cost. The simulator knows the complete generated rules, but agents receive only private measurements, delivered messages, authorized artifacts and explicitly described environment/procurement feedback. Public contexts omit world seeds and physics tables.

A generation contains five synchronous rounds by default. The first round collects sealed cost bids and awards teams; later contexts include the resulting assignments and bids. All agents have the same number of callback opportunities under communication ablations. At the final round, **each specialist commits to its own component choice**. The coordinator's intended recipe is recorded separately from the recipe actually assembled from the team's commitments. Complete evidence at the coordinator is therefore insufficient if the team fails to coordinate its actions.

Each awarded order has a DAG: sensor calibration and power preparation precede firmware assembly, followed by independent verification. Shared workers and equipment impose additional scheduling dependencies. Production uses a bounded dispatch budget and conserved material inventory. A budget shortage, equipment failure, exhausted material, poor device or missed deadline can prevent payment. The simulator records these causes separately.

Contract Net reserves customer credits. Only independently accepted work releases payment to the team; failure releases escrow without payment. Equal team payout is supported by quoting three times the largest team ask, so an accepted quote covers each submitted ask. Actual execution costs remain distinct from internal credit transfers. Awarding a team does not guarantee profitable execution or deadline feasibility.

## Communication and incentives

| Reference policy | Behavior |
|---|---|
| `broadcast` | Repeatedly broadcasts known measurements, bounded by evidence-card selection |
| `request` | Requests missing design constraints, then responds with relevant measurements |
| `targeted` | Sends new evidence toward order coordinators; topology still restricts delivery |
| `gated` | Targeted novelty selection plus the library's belief-change/silence gate |
| `none` | Generates no direct messages |

The study's **silent control uses broadcast agents with transport disabled**, preserving message-generation activity and decision opportunities. It is different from the `none` policy.

In `shared` mode the objective feedback is generation-wide accepted value minus actual execution cost. In `private` mode it is the agent's change in ledger balance minus its own execution costs. The scripted private policy shades its bid and shares favorable measurements only inside its firm, while disclosing negative warnings more widely. This is an explicit baseline behavior, not an empirical finding that competition necessarily produces secrecy. Model or learning agents can respond differently to the supplied objectives.

The primary study fixes the institution while crossing policy, incentives and bandwidth. It has 16 primary conditions and four silent controls. `--extra-controls` adds six conditions: both message states with shared artifacts disabled, plus pooled information, for each incentive regime. Pooled information changes access and is a diagnostic rather than a pure communication ablation.

## Three information channels

**Direct messages:** next-round delivery plus configured delay, keyed loss, optional duplication/reordering, and topology restrictions. Limits apply per generation to admitted sender messages and serialized bytes. A broadcast's delivered copies and repeated receiver input are accounted for separately. Evidence must be an unchanged measurement already exposed to the sender. Free text is not treated as an authenticated measurement.

**Artifacts:** successful device recipes with measured quality and version labels. `ArtifactStore` admits them through an independent verifier. `DecayingMemory` controls visibility; `CulturalTransfer` admits authorized current-version recipes into a replacement agent's memory. Shared mode exposes the retained public archive; private mode restricts it to the artifact author's firm. Disabling this channel removes archive reads and cultural adoption. An agent can still remember its own work.

**Environment and procurement:** revealed bids, team assignments, own balances, objective feedback and the agent's own team's measured results. Measured-result feedback belongs to the participating agent incarnation; replacements must recover predecessor discoveries through authorized artifacts. Optional forecast-market prices also belong to this channel. These observations remain when chat is disabled. “Silent” therefore does not mean no information can pass through joint actions or prices.

No runtime-wide artifact board is handed to agents. Each context contains a copied, explicitly filtered view. All contexts are constructed before any outputs are applied. Simulator checkpoints and offline researcher reports are privileged and must not be inserted into agent prompts. This is logical isolation for trusted local callbacks, not an operating-system sandbox.

## Configure the world and institution

```sh
python -m swarmkit.foundry run --topology hypergraph --loss 0.1 --budget 24 --bytes 50000
python -m swarmkit.foundry run --team-selection matching --equipment-slots 1 --failure 0.1
python -m swarmkit.foundry run --institution second_price --forecast-market
python -m swarmkit.foundry run --turnover 1 --change-every 2 --no-artifacts
python -m swarmkit.foundry run --material-units 2 --production-budget 8
python -m swarmkit.foundry run --disable-messages --pooled
```

`--firms`, `--components`, `--generations` and `--rounds` change population and workload. Component counts are bounded at eight because reference design search is exhaustive. Research and production budgets are per generation; material units are an episode-wide supply **per specialty**. Default material supply is enough for one build per firm per generation. Used materials move to a separate ledger account, including material consumed by failed work.

`full`, `ring`, `star` and `hypergraph` select existing topology implementations. Hypergraph neighborhoods overlap by firm and specialty. Economic hyperedges record actual three-specialist teams separately.

`--team-selection cost` enumerates affordable teams; `matching` uses one-to-one deferred acceptance for each complementary specialty; `routing` uses capability/success routing. Matching reduces shared-worker contention; a cheapest-team policy can repeatedly choose the same specialist. These are different institutions and should be compared separately from the primary communication ablation.

`--institution first_price`, `second_price` or `vcg` auctions an execution-priority right using budget-limited reference valuations. Payments go to an equipment account. This is a priority-allocation experiment; the VCG option is an exact single-right special case, not a general multi-resource optimizer. Default `contract` uses order priority without this extra auction.

`--forecast-market` opens a funded LMSR market per order. Agents can report forecasts and take bounded long positions; the simulator resolves them against actual delivery. Collateral stays reserved until resolution, and all cash is conserved. Producers can affect the event they forecast, so these prices are endogenous signals rather than independent verification. Markets are off in the default experiment.

Physics changes every two generations by default. The new version is announced; old measurements and working memories are cleared, and new measurements must be acquired. Old artifacts remain labeled with their original version until they expire. Random staff replacement resets that agent's observations, memory and local policy state; it does not erase its firm's financial obligations or silently mint new funding.

## Plug in agents

```python
import asyncio
from swarmkit.foundry import FoundryConfig, FoundryExperiment, FoundryWorld

async def experiment():
    world = FoundryWorld(seed=7, firms=2, components=2, generations=2)
    exp = FoundryExperiment(world, FoundryConfig(communication="request", checkpoint=True))
    agents = exp.population()  # Replace entries with your canonical Agent objects.
    result = await exp.run(agents, seed=11)
    print(result.metrics["accepted_value"])
    return result

asyncio.run(experiment())
```

Callbacks implement `act(AgentContext) -> AgentOutput`, synchronously or asynchronously. Each turn must return a `Decision` with its own agent ID and metadata:

- `bid`: finite nonnegative specialty cost quote; only the first round's quote is used.
- `query`: a topic from the context's permitted query list, or `None`.
- `forecast`: optional probability for the firm's order when markets are enabled.

At `phase="commit"`, the decision answer must be a JSON list of three legal component indices. Persist private state through `memory_updates`. Message metadata must be finite JSON data; binary/latent transports need an explicit adapter and accurate traffic metering. Agents cannot inject verified artifacts through outputs.

Custom providers own prompt construction, model/tool determinism, side effects and usage accounting. `trust_reported_usage=True` sums explicitly reported tokens and monetary cost. `agent_calls` counts harness invocations, not hidden provider calls. The driver invokes agents sequentially within synchronous rounds; simulated production time is separate from Python/model wall time.

Set `agent_concurrency` to overlap provider requests while preserving synchronous observations and action application. `agent_teams=True` delays matching until round 1: every decision in the `contract` phase supplies `preferences`, mapping complementary specialty names to ordered acceptable agent IDs. Empty lists refuse partners. `agent_publication=True` requires a boolean `publish` at commitment; the coordinator chooses whether a successful recipe enters the archive. Payment still depends on verification. Set `artifact_visibility="public"` or `"firm"` to decouple archive access from objectives; the default `"incentives"` retains offline behavior.

## Replay and metrics

```sh
python -m swarmkit.foundry run --policy broadcast --remove-message '0:firm0.sensor:0' --traces --output intervention.json
```

Use an attempted message ID from a trace. `checkpoint=True` stores complete local pre-round state, including policy objects, outstanding contracts, markets, memory and pending deliveries. Replay restores that state and suppresses all deliveries of the chosen message, including duplicated copies. `run(..., checkpoint=..., replace_messages={id: "neutral"})` supports content replacement with evidence removed. Remote model randomness and tools require a replayable wrapper. Checkpoints stay in memory and are omitted from JSON reports.

The primary metric is **accepted order value at matched resource allowances**. Reports also expose success, realized execution cost, actual material use, private surplus, model usage, message and artifact traffic, duplication of experiments, coordinator evidence coverage, commitment mismatch, deadlines, failures, turnover and generation-by-generation performance. Coverage is fact-ID exposure before commitment, not proof of correct use. Paired interventions report changes in accepted value and assembled recipes.

Shapley/core outputs are explicitly **modeled threshold-team diagnostics**: the coalition value assumes every specialty is necessary. They are not measured causal contribution estimates from rerunning every coalition. Hyperedge structure, reciprocity and design diversity are diagnostics, not substitutes for verified production.

`paired_difference()` matches world ID and run seed, averages repeated run seeds within each world, and bootstraps independent worlds. It refuses mismatches; a single world has no confidence interval. `run_study()` records each condition, all world seeds, per-run results and comparisons against the matching silent condition. The whole multigeneration world is the statistical unit.

## Population learning and integration scope

`cross_play()` assigns two communication-policy populations to alternating firms and runs real Foundry episodes. Measured objective payoffs feed `AlphaRankEvaluator` and the `PolicySpaceResponseOracles` empirical meta-solver. Returned mixtures and deviations apply only to the evaluated policy population. No new best-response policies are automatically trained.

`CommunicationPortfolio.fit()` uses full-information external-regret learning over policy outcomes from explicitly labeled development worlds. Freeze its resulting mixture before selecting policies on disjoint test worlds. This trains a policy selector, not model weights.

The implementation directly composes existing evidence registries, compression/gating, message bus, topologies, artifact admission, memory/transfer, trust/routing, DAG execution, resource budgets, economic hyperedges, Contract Net, matching, auction/VCG payments, LMSR, ledger settlement, threshold games, coalition diagnostics, population solvers and evaluation metrics. The [full method catalog](METHODS.md) remains available for further treatments.

The initial Foundry does not automatically train neural mechanisms, extract model hidden states, synthesize general procedures, or implement every alternative game from the library. Those require additional model/environment-specific adapters or separate controlled treatments. Its built-in scientific search and secrecy policies are transparent numerical baselines. Results on these synthetic devices do not establish performance on real manufacturing or open-ended scientific discovery.
