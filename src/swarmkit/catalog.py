"""Executable method registry with explicit source and fidelity boundaries."""

from __future__ import annotations

from importlib import import_module

from .economics.catalog import ECONOMIC_METHODS
from .types import MethodInfo


def _entry(name, family, target, source, fidelity, description, limitations=""):
    sources = (source,) if isinstance(source, str) else tuple(source)
    return MethodInfo(name, family, "swarmkit." + target, sources, fidelity, description, limitations)


_ENTRIES = (
    _entry("full", "topology", "topology.FullTopology", (), "primitive", "All active peers."),
    _entry("ring", "topology", "topology.RingTopology", (), "primitive", "Bounded ring communication."),
    _entry("star", "topology", "topology.StarTopology", (), "primitive", "Hub-and-spoke communication."),
    _entry(
        "random", "topology", "topology.RandomTopology", (), "primitive", "Seeded directed random topology."
    ),
    _entry(
        "spatial",
        "topology",
        "topology.LocalRadiusTopology",
        "https://arxiv.org/abs/2505.04364",
        "component",
        "Radius-bounded local observation/communication.",
        "Not the complete SwarmBench or robot simulator.",
    ),
    _entry(
        "hypergraph",
        "topology",
        "topology.HypergraphTopology",
        "https://arxiv.org/abs/2608.15519",
        "component",
        "Groups create multilateral communication neighborhoods.",
    ),
    _entry(
        "gptswarm",
        "optimization",
        "topology.BernoulliDAGPolicy",
        ("https://arxiv.org/abs/2402.16823", "https://arxiv.org/abs/2410.02506"),
        "adaptation",
        "REINFORCE edge learning, optional nuclear regularization, permanent pruning.",
        "Fixed topological order; no node prompt optimizer or full spatial-temporal AgentPrune training recipe.",
    ),
    _entry(
        "agent_dropout",
        "topology",
        "topology.RoundDropoutTopology",
        "https://arxiv.org/abs/2503.18891",
        "adaptation",
        "Round-specific arbitrary-size node and edge masks.",
        "Caller supplies importance estimates.",
    ),
    _entry(
        "dylan",
        "selection",
        "topology.DyLANSelection",
        "https://arxiv.org/abs/2310.02170",
        "adaptation",
        "Contributor selection, backward importance and consensus stopping.",
        "Caller supplies ranker scores; consensus is not proof of correctness.",
    ),
    _entry(
        "agentnet",
        "routing",
        "topology.CapabilitySuccessRouter",
        "https://arxiv.org/abs/2504.00587",
        "adaptation",
        "Capability overlap and success feedback route peer work.",
        "No learned language router or automatic agent creation.",
    ),
    _entry(
        "swarmagentic",
        "optimization",
        "optimization.ParticleSwarmSearch",
        "https://arxiv.org/abs/2506.15672",
        "adaptation",
        "Personal/global-best population search with failure memory and artifact ancestry.",
        "Injected mutation/evaluation implement task-specific design search.",
    ),
    _entry(
        "independent_vote",
        "deliberation",
        "deliberation.IndependentVoting",
        "https://arxiv.org/abs/2508.17536",
        "mechanism",
        "Independent decisions form a no-exchange baseline.",
    ),
    _entry(
        "consensus",
        "deliberation",
        "deliberation.WeightedConsensus",
        "https://arxiv.org/abs/2502.19130",
        "adaptation",
        "Weighted aggregation with stability stopping.",
        "Voting does not establish evidence independence.",
    ),
    _entry(
        "exchange_then_decide",
        "deliberation",
        "deliberation.ExchangeThenDecide",
        "https://arxiv.org/abs/2505.11556",
        "adaptation",
        "Budgeted evidence disclosure and objections before commitment.",
        "Symbolic evidence scorer by default; all-peer and topology-constrained inbox modes are explicit.",
    ),
    _entry(
        "critique_revise",
        "deliberation",
        "deliberation.CritiqueReviseDebate",
        "https://arxiv.org/abs/2305.14325",
        "component",
        "Independent candidates followed by bounded critique/revision callbacks.",
        "Prescribed discussion component, not a complete decentralized swarm.",
    ),
    _entry(
        "evidence_registry",
        "knowledge",
        "knowledge.EvidenceRegistry",
        "https://arxiv.org/abs/2505.11556",
        "design",
        "Validate ancestry and count independent root sources.",
        "Source identifiers are assertions; no external source-authenticity service.",
    ),
    _entry(
        "artifact_store",
        "knowledge",
        "knowledge.ArtifactStore",
        "https://arxiv.org/abs/2608.26081",
        "component",
        "Verifier-controlled immutable artifact admission, lineage and retirement.",
        "Verifiers are trusted caller code; this is not a sandbox.",
    ),
    _entry(
        "peer_adoption",
        "knowledge",
        "knowledge.PeerAdoption",
        "https://github.com/gensyn-ai/collaborative-autoresearch-demo",
        "adaptation",
        "Locally test candidate utility before adoption and roll back regressions.",
        "Local evaluation quality determines validity.",
    ),
    _entry(
        "decaying_memory",
        "knowledge",
        "knowledge.DecayingMemory",
        "https://arxiv.org/abs/2606.30668",
        "adaptation",
        "Exponential forgetting plus explicit collective refresh.",
        "A deterministic retention model, not exact character-corruption simulation.",
    ),
    _entry(
        "cultural_transfer",
        "knowledge",
        "knowledge.CulturalTransfer",
        ("https://arxiv.org/abs/2406.00392", "https://arxiv.org/abs/2603.16910"),
        "adaptation",
        "Retain verified artifacts across generations and test fresh recipients.",
        "No RL policy training or TerraLingua ecology reproduced.",
    ),
    _entry(
        "abstraction",
        "knowledge",
        "knowledge.ProcedureAbstraction",
        "https://arxiv.org/abs/2608.26081",
        "design",
        "Generate procedures from artifacts and admit only held-out verified candidates.",
        "Caller supplies abstraction generator and independent cases.",
    ),
    _entry(
        "stigmergy",
        "knowledge",
        "stigmergy.StigmergicPolicy",
        ("https://arxiv.org/abs/2510.10047", "https://arxiv.org/abs/2608.26081"),
        "adaptation",
        "Local artifact discovery, decaying success traces and tested reuse.",
        "Numeric pheromone policy is a design adaptation, not SwarmSys reproduction.",
    ),
    _entry(
        "naming_game",
        "social",
        "social.NamingGame",
        "https://arxiv.org/abs/2410.08948",
        "adaptation",
        "Pairwise reward/memory convention formation and committed minorities.",
        "Symbolic choice policy; arbitrary conventions are not true propositions.",
    ),
    _entry(
        "proportional_copying",
        "social",
        "social.ProportionalCopying",
        "https://arxiv.org/abs/2609.09150",
        "mechanism",
        "Copy proportional to locally visible frequencies.",
    ),
    _entry(
        "feed",
        "social",
        "social.FeedPolicy",
        ("https://arxiv.org/abs/2411.11581", "https://github.com/swarmclawai/swarmfeed"),
        "adaptation",
        "Score and diversify visible messages using recency, engagement and reputation.",
        "Popularity ranking is not knowledge verification.",
    ),
    _entry(
        "trust",
        "social",
        "social.TrustNetwork",
        "https://molt-hub.org/about/",
        "design",
        "Directional domain trust with bounded transitive paths and admission checks.",
        "Explicit local trust formula; MoltHub server internals were unavailable.",
    ),
    _entry(
        "gossip",
        "social",
        "social.GossipRelay",
        "https://arxiv.org/abs/2608.22884",
        "mechanism",
        "Synchronous, bounded-bandwidth evidence relay with lifetime constraints.",
        "Use topology.neighbors as the callback; messages require bus commit.",
    ),
    _entry(
        "information_gate",
        "communication",
        "communication.InformationGate",
        "https://arxiv.org/abs/2605.06988",
        "adaptation",
        "Entropy or JS change, novelty, and silence interval trigger messages.",
        "Entropy-only mode misses equal-entropy hypothesis switches.",
    ),
    _entry(
        "evidence_compression",
        "communication",
        "communication.EvidenceCompressor",
        "https://arxiv.org/abs/2505.11556",
        "design",
        "Bound evidence-card count while preserving provenance and counterevidence.",
        "Card count is not a token or byte budget.",
    ),
    _entry(
        "latent_memory",
        "latent",
        "communication.LatentMemory",
        "https://arxiv.org/abs/2511.20639",
        "component",
        "FIFO model/layer-compatible hidden-state memory.",
        "Caller must supply real hidden states; no model internals are fabricated.",
    ),
    _entry(
        "geometric_alignment",
        "latent",
        "communication.GeometricAlignment",
        "https://arxiv.org/abs/2608.13317",
        "component",
        "Centered/whitened Procrustes alignment of paired hidden states.",
        "Not the full model-specific StateBridge implementation.",
    ),
    _entry(
        "vocabulary_anchor",
        "latent",
        "communication.VocabularyAnchor",
        "https://arxiv.org/abs/2608.13317",
        "component",
        "Blend mapped states with target-vocabulary neighbors.",
    ),
    _entry(
        "linear_latent",
        "latent",
        "communication.LinearLatentCodec",
        "https://arxiv.org/abs/2606.13594",
        "baseline",
        "Fit a ridge reconstruction adapter from paired states.",
        "Linear baseline, not the published neural/generative trainer.",
    ),
    _entry(
        "kv_translation",
        "latent",
        "communication.KVCacheTranslator",
        "https://arxiv.org/abs/2606.13594",
        "baseline",
        "Learn separate feature maps for cache keys and values.",
        "Leading axes must align; no arbitrary head/layer conversion.",
    ),
    _entry(
        "contrastive_latent",
        "latent",
        "latent_training.ContrastiveLatentCodec",
        "https://arxiv.org/abs/2511.09149",
        "component",
        "Train paired InfoNCE communication against mismatched negatives.",
        "Linear interface, not full Interlat or its pretrained weights.",
    ),
    _entry(
        "latent_bottleneck",
        "latent",
        "latent_training.LatentBottleneck",
        "https://arxiv.org/abs/2511.09149",
        "baseline",
        "PCA compression/decompression with measurable reconstruction error.",
    ),
    _entry(
        "policy_gradient",
        "learning",
        "learning.SoftmaxPolicy",
        "https://arxiv.org/abs/2502.18439",
        "primitive",
        "Train categorical coordination choices using REINFORCE or clipped PPO.",
        "Small NumPy policy; not transformer weight training.",
    ),
    _entry(
        "collaborative_reward",
        "learning",
        "learning.CollaborativeReward",
        "https://arxiv.org/abs/2502.18439",
        "adaptation",
        "Reward correctness and measured peer improvement minus cost.",
    ),
    _entry(
        "parallel_reward",
        "learning",
        "learning.ParallelReward",
        "https://arxiv.org/abs/2602.02276",
        "adaptation",
        "Anneal useful-parallelism/completion shaping with separate critical-path cost.",
    ),
    _entry(
        "counterfactual_credit",
        "learning",
        "learning.counterfactual_message_credit",
        "https://arxiv.org/abs/2502.18439",
        "design",
        "Leave-one-message-out evaluator credit.",
        "Requires deterministic controlled evaluation; not exact Shapley values.",
    ),
    _entry(
        "dag_executor",
        "scheduling",
        "scheduling.DAGExecutor",
        ("https://arxiv.org/abs/2602.02276", "https://arxiv.org/abs/2606.09730"),
        "component",
        "Parallel dependency scheduling with compact direct-dependency handoffs.",
        "Caller supplies decomposition/worker; not a trained orchestrator.",
    ),
    _entry(
        "critical_path",
        "scheduling",
        "scheduling.critical_path",
        "https://arxiv.org/abs/2602.02276",
        "mechanism",
        "Compute the longest weighted dependency path separately from total work.",
    ),
    _entry(
        "private_recovery",
        "evaluation",
        "evaluation.private_evidence_recovery",
        "https://arxiv.org/abs/2505.11556",
        "metric",
        "Measure disclosed private evidence coverage.",
    ),
    _entry(
        "ancestry_agreement",
        "evaluation",
        "evaluation.ancestry_adjusted_agreement",
        "https://arxiv.org/abs/2609.09150",
        "metric",
        "Discount shared-root evidence when measuring agreement.",
    ),
    _entry(
        "diversity",
        "evaluation",
        "evaluation.population_diversity",
        "https://arxiv.org/abs/2602.14299",
        "metric",
        "Entropy of population labels.",
    ),
    _entry(
        "reciprocity",
        "evaluation",
        "evaluation.interaction_reciprocity",
        "https://arxiv.org/abs/2604.13052",
        "metric",
        "Reciprocated directed interaction edges.",
    ),
    _entry(
        "hyperedge_irreducibility",
        "evaluation",
        "evaluation.hyperedge_irreducibility",
        "https://arxiv.org/abs/2608.15519",
        "metric",
        "Published normalized higher-order degree-inequality score.",
        "A structural score, not a measure of problem-solving intelligence.",
    ),
    _entry(
        "transfer_gain",
        "evaluation",
        "evaluation.transfer_gain",
        "https://arxiv.org/abs/2406.00392",
        "metric",
        "Paired fresh-recipient capability differences.",
    ),
    _entry(
        "matched_controls",
        "evaluation",
        "evaluation.matched_independent_control",
        "https://arxiv.org/abs/2608.26081",
        "design",
        "Compare shared interaction with matched independent agent budgets.",
        "Callbacks are responsible for honoring supplied work budgets.",
    ),
)



_ENTRIES += tuple(
    _entry(name, "economics", "economics."+api, source, fidelity, description, limits)
    for name, api, source, fidelity, description, limits in ECONOMIC_METHODS
)
_ENTRIES += (
    _entry("communication_evaluation", "evaluation", "benchmarks.CommunicationEvaluator",
           "https://arxiv.org/abs/1903.05168", "design",
           "Private-channel experiments, actual receipts and checkpoint interventions.",
           "Original diagnostic tasks; external model/tool determinism is caller-owned."),
)


_ENTRIES += (
    _entry("research_foundry", "experiments", "foundry.FoundryExperiment",
           ("https://arxiv.org/abs/2505.11556", "https://arxiv.org/abs/2601.13295"),
           "design", "Private discovery, team procurement, resource scheduling and independently verified production.",
           "Synthetic physics and scripted controls; provider-backed agents require explicit adapters and usage accounting."),
)


def methods(family: str | None = None) -> tuple[MethodInfo, ...]:
    return tuple(info for info in _ENTRIES if family is None or info.family == family)


def resolve(name: str):
    """Return a registered class/function without allowing arbitrary imports."""
    info = next((info for info in _ENTRIES if info.name == name), None)
    if info is None:
        raise KeyError(f"unknown method: {name}")
    module, member = info.target.rsplit(".", 1)
    return getattr(import_module(module), member)
