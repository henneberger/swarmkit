# Algorithm and method catalog

This table is generated from `swarmkit.catalog.methods()`. All listed targets are importable implementations. Runtime protocols and shared records are described in [API.md](API.md).

Fidelity labels: **primitive** is general infrastructure; **mechanism** implements the stated local operation; **component** supplies one part of a larger method; **adaptation** changes the published method for a common API; **baseline** is a deliberately simpler comparator; **design** is an explicit synthesis; **metric** measures a limited property. **implemented_core** is a self-contained economic component; **numpy_adaptation** is a small numerical research adaptation; **callback_training** executes caller-supplied learning; **optional_adapter** invokes an external solver. None claims to reproduce a paper’s full experimental results.

There are **77 registered entries**. Some entries expose several operations (for example graph sampling, learning and pruning).

## Topology

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `full` · [swarmkit.topology.FullTopology](../src/swarmkit/topology.py#L24) | All active peers. | **primitive**.  | General primitive |
| `ring` · [swarmkit.topology.RingTopology](../src/swarmkit/topology.py#L30) | Bounded ring communication. | **primitive**.  | General primitive |
| `star` · [swarmkit.topology.StarTopology](../src/swarmkit/topology.py#L43) | Hub-and-spoke communication. | **primitive**.  | General primitive |
| `random` · [swarmkit.topology.RandomTopology](../src/swarmkit/topology.py#L52) | Seeded directed random topology. | **primitive**.  | General primitive |
| `spatial` · [swarmkit.topology.LocalRadiusTopology](../src/swarmkit/topology.py#L76) | Radius-bounded local observation/communication. | **component**. Not the complete SwarmBench or robot simulator. | [source 1](https://arxiv.org/abs/2505.04364) |
| `hypergraph` · [swarmkit.topology.HypergraphTopology](../src/swarmkit/topology.py#L103) | Groups create multilateral communication neighborhoods. | **component**.  | [source 1](https://arxiv.org/abs/2608.15519) |
| `agent_dropout` · [swarmkit.topology.RoundDropoutTopology](../src/swarmkit/topology.py#L240) | Round-specific arbitrary-size node and edge masks. | **adaptation**. Caller supplies importance estimates. | [source 1](https://arxiv.org/abs/2503.18891) |

## Optimization

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `gptswarm` · [swarmkit.topology.BernoulliDAGPolicy](../src/swarmkit/topology.py#L114) | REINFORCE edge learning, optional nuclear regularization, permanent pruning. | **adaptation**. Fixed topological order; no node prompt optimizer or full spatial-temporal AgentPrune training recipe. | [source 1](https://arxiv.org/abs/2402.16823) · [source 2](https://arxiv.org/abs/2410.02506) |
| `swarmagentic` · [swarmkit.optimization.ParticleSwarmSearch](../src/swarmkit/optimization.py#L22) | Personal/global-best population search with failure memory and artifact ancestry. | **adaptation**. Injected mutation/evaluation implement task-specific design search. | [source 1](https://arxiv.org/abs/2506.15672) |

## Selection

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `dylan` · [swarmkit.topology.DyLANSelection](../src/swarmkit/topology.py#L291) | Contributor selection, backward importance and consensus stopping. | **adaptation**. Caller supplies ranker scores; consensus is not proof of correctness. | [source 1](https://arxiv.org/abs/2310.02170) |

## Routing

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `agentnet` · [swarmkit.topology.CapabilitySuccessRouter](../src/swarmkit/topology.py#L347) | Capability overlap and success feedback route peer work. | **adaptation**. No learned language router or automatic agent creation. | [source 1](https://arxiv.org/abs/2504.00587) |

## Deliberation

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `independent_vote` · [swarmkit.deliberation.IndependentVoting](../src/swarmkit/deliberation.py#L60) | Independent decisions form a no-exchange baseline. | **mechanism**.  | [source 1](https://arxiv.org/abs/2508.17536) |
| `consensus` · [swarmkit.deliberation.WeightedConsensus](../src/swarmkit/deliberation.py#L86) | Weighted aggregation with stability stopping. | **adaptation**. Voting does not establish evidence independence. | [source 1](https://arxiv.org/abs/2502.19130) |
| `exchange_then_decide` · [swarmkit.deliberation.ExchangeThenDecide](../src/swarmkit/deliberation.py#L180) | Budgeted evidence disclosure and objections before commitment. | **adaptation**. Symbolic evidence scorer by default; all-peer and topology-constrained inbox modes are explicit. | [source 1](https://arxiv.org/abs/2505.11556) |
| `critique_revise` · [swarmkit.deliberation.CritiqueReviseDebate](../src/swarmkit/deliberation.py#L464) | Independent candidates followed by bounded critique/revision callbacks. | **component**. Prescribed discussion component, not a complete decentralized swarm. | [source 1](https://arxiv.org/abs/2305.14325) |

## Knowledge

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `evidence_registry` · [swarmkit.knowledge.EvidenceRegistry](../src/swarmkit/knowledge.py#L40) | Validate ancestry and count independent root sources. | **design**. Source identifiers are assertions; no external source-authenticity service. | [source 1](https://arxiv.org/abs/2505.11556) |
| `artifact_store` · [swarmkit.knowledge.ArtifactStore](../src/swarmkit/knowledge.py#L114) | Verifier-controlled immutable artifact admission, lineage and retirement. | **component**. Verifiers are trusted caller code; this is not a sandbox. | [source 1](https://arxiv.org/abs/2608.26081) |
| `peer_adoption` · [swarmkit.knowledge.PeerAdoption](../src/swarmkit/knowledge.py#L174) | Locally test candidate utility before adoption and roll back regressions. | **adaptation**. Local evaluation quality determines validity. | [source 1](https://github.com/gensyn-ai/collaborative-autoresearch-demo) |
| `decaying_memory` · [swarmkit.knowledge.DecayingMemory](../src/swarmkit/knowledge.py#L238) | Exponential forgetting plus explicit collective refresh. | **adaptation**. A deterministic retention model, not exact character-corruption simulation. | [source 1](https://arxiv.org/abs/2606.30668) |
| `cultural_transfer` · [swarmkit.knowledge.CulturalTransfer](../src/swarmkit/knowledge.py#L291) | Retain verified artifacts across generations and test fresh recipients. | **adaptation**. No RL policy training or TerraLingua ecology reproduced. | [source 1](https://arxiv.org/abs/2406.00392) · [source 2](https://arxiv.org/abs/2603.16910) |
| `abstraction` · [swarmkit.knowledge.ProcedureAbstraction](../src/swarmkit/knowledge.py#L331) | Generate procedures from artifacts and admit only held-out verified candidates. | **design**. Caller supplies abstraction generator and independent cases. | [source 1](https://arxiv.org/abs/2608.26081) |
| `stigmergy` · [swarmkit.stigmergy.StigmergicPolicy](../src/swarmkit/stigmergy.py#L19) | Local artifact discovery, decaying success traces and tested reuse. | **adaptation**. Numeric pheromone policy is a design adaptation, not SwarmSys reproduction. | [source 1](https://arxiv.org/abs/2510.10047) · [source 2](https://arxiv.org/abs/2608.26081) |

## Social

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `naming_game` · [swarmkit.social.NamingGame](../src/swarmkit/social.py#L45) | Pairwise reward/memory convention formation and committed minorities. | **adaptation**. Symbolic choice policy; arbitrary conventions are not true propositions. | [source 1](https://arxiv.org/abs/2410.08948) |
| `proportional_copying` · [swarmkit.social.ProportionalCopying](../src/swarmkit/social.py#L101) | Copy proportional to locally visible frequencies. | **mechanism**.  | [source 1](https://arxiv.org/abs/2609.09150) |
| `feed` · [swarmkit.social.FeedPolicy](../src/swarmkit/social.py#L137) | Score and diversify visible messages using recency, engagement and reputation. | **adaptation**. Popularity ranking is not knowledge verification. | [source 1](https://arxiv.org/abs/2411.11581) · [source 2](https://github.com/swarmclawai/swarmfeed) |
| `trust` · [swarmkit.social.TrustNetwork](../src/swarmkit/social.py#L208) | Directional domain trust with bounded transitive paths and admission checks. | **design**. Explicit local trust formula; MoltHub server internals were unavailable. | [source 1](https://molt-hub.org/about/) |
| `gossip` · [swarmkit.social.GossipRelay](../src/swarmkit/social.py#L277) | Synchronous, bounded-bandwidth evidence relay with lifetime constraints. | **mechanism**. Use topology.neighbors as the callback; messages require bus commit. | [source 1](https://arxiv.org/abs/2608.22884) |

## Communication

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `information_gate` · [swarmkit.communication.InformationGate](../src/swarmkit/communication.py#L60) | Entropy or JS change, novelty, and silence interval trigger messages. | **adaptation**. Entropy-only mode misses equal-entropy hypothesis switches. | [source 1](https://arxiv.org/abs/2605.06988) |
| `evidence_compression` · [swarmkit.communication.EvidenceCompressor](../src/swarmkit/communication.py#L129) | Bound evidence-card count while preserving provenance and counterevidence. | **design**. Card count is not a token or byte budget. | [source 1](https://arxiv.org/abs/2505.11556) |

## Latent

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `latent_memory` · [swarmkit.communication.LatentMemory](../src/swarmkit/communication.py#L169) | FIFO model/layer-compatible hidden-state memory. | **component**. Caller must supply real hidden states; no model internals are fabricated. | [source 1](https://arxiv.org/abs/2511.20639) |
| `geometric_alignment` · [swarmkit.communication.GeometricAlignment](../src/swarmkit/communication.py#L199) | Centered/whitened Procrustes alignment of paired hidden states. | **component**. Not the full model-specific StateBridge implementation. | [source 1](https://arxiv.org/abs/2608.13317) |
| `vocabulary_anchor` · [swarmkit.communication.VocabularyAnchor](../src/swarmkit/communication.py#L265) | Blend mapped states with target-vocabulary neighbors. | **component**.  | [source 1](https://arxiv.org/abs/2608.13317) |
| `linear_latent` · [swarmkit.communication.LinearLatentCodec](../src/swarmkit/communication.py#L307) | Fit a ridge reconstruction adapter from paired states. | **baseline**. Linear baseline, not the published neural/generative trainer. | [source 1](https://arxiv.org/abs/2606.13594) |
| `kv_translation` · [swarmkit.communication.KVCacheTranslator](../src/swarmkit/communication.py#L349) | Learn separate feature maps for cache keys and values. | **baseline**. Leading axes must align; no arbitrary head/layer conversion. | [source 1](https://arxiv.org/abs/2606.13594) |
| `contrastive_latent` · [swarmkit.latent_training.ContrastiveLatentCodec](../src/swarmkit/latent_training.py#L34) | Train paired InfoNCE communication against mismatched negatives. | **component**. Linear interface, not full Interlat or its pretrained weights. | [source 1](https://arxiv.org/abs/2511.09149) |
| `latent_bottleneck` · [swarmkit.latent_training.LatentBottleneck](../src/swarmkit/latent_training.py#L104) | PCA compression/decompression with measurable reconstruction error. | **baseline**.  | [source 1](https://arxiv.org/abs/2511.09149) |

## Learning

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `policy_gradient` · [swarmkit.learning.SoftmaxPolicy](../src/swarmkit/learning.py#L23) | Train categorical coordination choices using REINFORCE or clipped PPO. | **primitive**. Small NumPy policy; not transformer weight training. | [source 1](https://arxiv.org/abs/2502.18439) |
| `collaborative_reward` · [swarmkit.learning.CollaborativeReward](../src/swarmkit/learning.py#L103) | Reward correctness and measured peer improvement minus cost. | **adaptation**.  | [source 1](https://arxiv.org/abs/2502.18439) |
| `parallel_reward` · [swarmkit.learning.ParallelReward](../src/swarmkit/learning.py#L166) | Anneal useful-parallelism/completion shaping with separate critical-path cost. | **adaptation**.  | [source 1](https://arxiv.org/abs/2602.02276) |
| `counterfactual_credit` · [swarmkit.learning.counterfactual_message_credit](../src/swarmkit/learning.py#L146) | Leave-one-message-out evaluator credit. | **design**. Requires deterministic controlled evaluation; not exact Shapley values. | [source 1](https://arxiv.org/abs/2502.18439) |

## Scheduling

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `dag_executor` · [swarmkit.scheduling.DAGExecutor](../src/swarmkit/scheduling.py#L43) | Parallel dependency scheduling with compact direct-dependency handoffs. | **component**. Caller supplies decomposition/worker; not a trained orchestrator. | [source 1](https://arxiv.org/abs/2602.02276) · [source 2](https://arxiv.org/abs/2606.09730) |
| `critical_path` · [swarmkit.scheduling.critical_path](../src/swarmkit/scheduling.py#L20) | Compute the longest weighted dependency path separately from total work. | **mechanism**.  | [source 1](https://arxiv.org/abs/2602.02276) |

## Evaluation

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `private_recovery` · [swarmkit.evaluation.private_evidence_recovery](../src/swarmkit/evaluation.py#L53) | Measure disclosed private evidence coverage. | **metric**.  | [source 1](https://arxiv.org/abs/2505.11556) |
| `ancestry_agreement` · [swarmkit.evaluation.ancestry_adjusted_agreement](../src/swarmkit/evaluation.py#L71) | Discount shared-root evidence when measuring agreement. | **metric**.  | [source 1](https://arxiv.org/abs/2609.09150) |
| `diversity` · [swarmkit.evaluation.population_diversity](../src/swarmkit/evaluation.py#L21) | Entropy of population labels. | **metric**.  | [source 1](https://arxiv.org/abs/2602.14299) |
| `reciprocity` · [swarmkit.evaluation.interaction_reciprocity](../src/swarmkit/evaluation.py#L36) | Reciprocated directed interaction edges. | **metric**.  | [source 1](https://arxiv.org/abs/2604.13052) |
| `hyperedge_irreducibility` · [swarmkit.evaluation.hyperedge_irreducibility](../src/swarmkit/evaluation.py#L115) | Published normalized higher-order degree-inequality score. | **metric**. A structural score, not a measure of problem-solving intelligence. | [source 1](https://arxiv.org/abs/2608.15519) |
| `transfer_gain` · [swarmkit.evaluation.transfer_gain](../src/swarmkit/evaluation.py#L141) | Paired fresh-recipient capability differences. | **metric**.  | [source 1](https://arxiv.org/abs/2406.00392) |
| `matched_controls` · [swarmkit.evaluation.matched_independent_control](../src/swarmkit/evaluation.py#L169) | Compare shared interaction with matched independent agent budgets. | **design**. Callbacks are responsible for honoring supplied work budgets. | [source 1](https://arxiv.org/abs/2608.26081) |
| `communication_evaluation` · [swarmkit.benchmarks.CommunicationEvaluator](../src/swarmkit/benchmarks/communication.py#L119) | Private-channel experiments, actual receipts and checkpoint interventions. | **design**. Original diagnostic tasks; external model/tool determinism is caller-owned. | [source 1](https://arxiv.org/abs/1903.05168) |

## Economics

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `economic_normal_form` · [swarmkit.economics.NormalFormGame](../src/swarmkit/economics/games.py#L12) | Small local strategic interactions | **implemented_core**. Known payoff tensors; finite legal actions | [source 1](https://timroughgarden.org/f13/f13.html) |
| `economic_repeated_games` · [swarmkit.economics.RepeatedGame](../src/swarmkit/economics/games.py#L66) | Repeated evidence sharing | **implemented_core**. Continuation and observation noise explicitly modeled | [source 1](https://arxiv.org/abs/1908.09453) |
| `economic_public_goods` · [swarmkit.economics.HypergraphPublicGoods](../src/swarmkit/economics/games.py#L103) | Shared evidence and costly verification | **implemented_core**. State contribution budget per agent versus per edge | [source 1](https://arxiv.org/abs/2001.10313) |
| `economic_threshold_coalitions` · [swarmkit.economics.ThresholdTeamGame](../src/swarmkit/economics/games.py#L132) | Complementary specialist teams | **numpy_adaptation**. Our nonlinear task adaptation; no generic stability theorem | [source 1](https://arxiv.org/abs/2001.10313) |
| `economic_contract_net` · [swarmkit.economics.ContractNet](../src/swarmkit/economics/mechanisms.py#L155) | Distributed task procurement | **implemented_core**. Task-sharing protocol; not inherently truthful | [source 1](https://doi.org/10.1109/TC.1980.1675516) |
| `economic_single_item_auctions` · [swarmkit.economics.FirstPriceAuction](../src/swarmkit/economics/mechanisms.py#L14) | Allocate tools or procure work | **implemented_core**. State private-value utility, budgets, reserves and tie rules | [source 1](https://timroughgarden.org/f13/f13.html) |
| `economic_combinatorial_vcg` · [swarmkit.economics.CombinatorialAuction](../src/swarmkit/economics/mechanisms.py#L52) | Allocate complementary resource bundles | **implemented_core**. Truthfulness requires suitable exact allocation and utility assumptions | [source 1](https://arxiv.org/abs/1607.07684) |
| `economic_double_auction` · [swarmkit.economics.DoubleAuction](../src/swarmkit/economics/mechanisms.py#L110) | Exchange resource allocations | **implemented_core**. Explicit clearing and inventories; no automatic truthfulness | [source 1](https://arxiv.org/abs/2609.02580) |
| `economic_congestion` · [swarmkit.economics.CongestionGame](../src/swarmkit/economics/games.py#L154) | Route work across shared tools | **implemented_core**. Exact-potential guarantees require the corresponding game assumptions | [source 1](https://timroughgarden.org/f13/f13.html) |
| `economic_stable_matching` · [swarmkit.economics.DeferredAcceptance](../src/swarmkit/economics/mechanisms.py#L130) | Match agents and projects | **implemented_core**. Classical preference domain; arbitrary complementary teams excluded | [source 1](https://doi.org/10.2307/2312726) |
| `economic_bargaining` · [swarmkit.economics.AlternatingOffers](../src/swarmkit/economics/solutions.py#L34) | Negotiate deadline quality and price | **implemented_core**. Nash solution separate from dialogue; disagreement utility explicit | [source 1](https://doi.org/10.2307/1907266) |
| `economic_coalition_value` · [swarmkit.economics.ShapleyEstimator](../src/swarmkit/economics/solutions.py#L75) | Share rewards for joint artifacts | **implemented_core**. Normalized characteristic value; exact permutation limit 9; sampled estimates include standard errors; graph restriction extends to fully contained hyperedges | [source 1](https://doi.org/10.1007/BF01787031) |
| `economic_prediction_market` · [swarmkit.economics.LMSRMarket](../src/swarmkit/economics/mechanisms.py#L234) | Forecast independent verification outcomes | **implemented_core**. Outcome oracle, liquidity and subsidy required; strategic traders can influence prices | [source 1](https://mason.gmu.edu/~rhanson/mktscore.pdf) |
| `economic_external_regret` · [swarmkit.economics.ExternalRegretPolicy](../src/swarmkit/economics/strategies.py#L46) | Adaptive bidding and routing | **implemented_core**. Bounded payoff feedback; empirical CCE connection, not generic Nash | [source 1](https://timroughgarden.org/f13/f13.html) |
| `economic_internal_regret` · [swarmkit.economics.InternalRegretPolicy](../src/swarmkit/economics/strategies.py#L81) | Coordinated local recommendations | **implemented_core**. Distinguish internal deviations from fixed action deviations | [source 1](https://ma.huji.ac.il/~hart/abs/adapt.html) |
| `economic_cfr` · [swarmkit.economics.OpenSpielCFR](../src/swarmkit/economics/adapters.py#L4) | Small imperfect-information economic games | **optional_adapter**. Classical Nash guarantee for appropriate two-player zero-sum perfect-recall games | [source 1](https://arxiv.org/abs/1908.09453) |
| `economic_psro` · [swarmkit.economics.PolicySpaceResponseOracles](../src/swarmkit/economics/population.py#L11) | Maintain diverse strategic agents | **numpy_adaptation**. Approximate LLM response oracle; restricted population equilibria | [source 1](https://arxiv.org/abs/1711.00832) |
| `economic_alpharank` · [swarmkit.economics.AlphaRankEvaluator](../src/swarmkit/economics/population.py#L61) | Evaluate cyclic strategy populations | **implemented_core**. Ranking is neither Nash certificate nor welfare optimization | [source 1](https://arxiv.org/abs/1903.01373) |
| `economic_opponent_shaping` · [swarmkit.economics.LOLAAdapter](../src/swarmkit/economics/learning.py#L29) | Learn reciprocal behavior | **numpy_adaptation**. Requires learning model and gradient access for fidelity | [source 1](https://arxiv.org/abs/1709.04326) |
| `economic_mean_field` · [swarmkit.economics.MultiTypeMeanField](../src/swarmkit/economics/population.py#L109) | Scale populations with roles | **numpy_adaptation**. Averages may erase sparse complementarities | [source 1](https://arxiv.org/abs/1802.05438) |
| `economic_learned_auctions` · [swarmkit.economics.LearnedAuction](../src/swarmkit/economics/learning.py#L94) | Optimize allocation and payment | **numpy_adaptation**. Empirical deviation search is not exact DSIC | [source 1](https://arxiv.org/abs/1706.03459) |
| `economic_learned_institutions` · [swarmkit.economics.TwoLevelInstitution](../src/swarmkit/economics/learning.py#L171) | Learn incentives while workers adapt | **callback_training**. Simulation-specific; changing rules changes the game | [source 1](https://arxiv.org/abs/2108.02755) |
| `economic_other_regarding_q` · [swarmkit.economics.GroupHistoryQPolicy](../src/swarmkit/economics/strategies.py#L119) | Condition cooperation on group history | **numpy_adaptation**. Other-regarding state is not necessarily altruistic utility | [source 1](https://arxiv.org/abs/2410.10921) |
| `economic_language_self_play` · [swarmkit.economics.NegotiationSelfPlay](../src/swarmkit/economics/learning.py#L201) | Improve structured language offers | **callback_training**. Validate structured outcomes and hold out partners | [source 1](https://arxiv.org/abs/1706.05125) |
| `economic_information_design` · [swarmkit.economics.FramingAndDisclosurePolicy](../src/swarmkit/economics/learning.py#L251) | Study evidence framing and disclosure | **numpy_adaptation**. Belief oracle is a modeling assumption; no general behavior guarantee | [source 1](https://arxiv.org/abs/2509.25565) |
| `economic_leader_follower` · [swarmkit.economics.StackelbergContractGame](../src/swarmkit/economics/games.py#L179) | Model scheduler incentives and worker effort | **numpy_adaptation**. Tentative extension; full principal-agent literature not covered | [source 1](https://arxiv.org/abs/2108.02755) |

## Experiments

| Registry name / API | Implemented operation | Fidelity and limits | Sources |
|---|---|---|---|
| `research_foundry` · [swarmkit.foundry.FoundryExperiment](../src/swarmkit/foundry/experiment.py#L170) | Private discovery, team procurement, resource scheduling and independently verified production. | **design**. Synthetic physics and scripted controls; provider-backed agents require explicit adapters and usage accounting. | [source 1](https://arxiv.org/abs/2505.11556) · [source 2](https://arxiv.org/abs/2601.13295) |

## What the package does not bundle

Provider credentials, proprietary orchestration checkpoints, full transformer training stacks, model-specific hidden-state extraction, complete robot/world simulators, large benchmark datasets and upstream services are not bundled. Callbacks provide task-specific model inference, evaluation, decomposition, mutation and abstraction generation. These are explicit extension points, not silently successful placeholders.

For arbitrary transformer training, use the reward and policy primitives as components of an external trainer. For latent channels, supply actual aligned model states and evaluate downstream behavior. For scientific discovery, provide independent artifact validators and held-out tasks.

The research-to-code mapping emphasizes mechanisms relevant to swarms. Platform observation studies inform metrics and controls; their results are not represented as algorithms that reproduce an entire social network.
