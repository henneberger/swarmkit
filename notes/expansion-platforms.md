# Expansion: social-agent networks and persistent swarm collaboration

New relative to `sources/catalog.json` when scanned on 2026-09-09. Four bounded additions below, prioritized by relevance. Code was read remotely, not cloned or executed. No platform accounts or posts were created.

## 1. Gensyn collaborative autoresearch: reproducible findings circulate among peers

[Repository](https://github.com/gensyn-ai/collaborative-autoresearch-demo); [communication implementation](https://github.com/gensyn-ai/collaborative-autoresearch-demo/blob/main/skills/autoresearch-network/research_network.py); [agent experiment protocol](https://github.com/gensyn-ai/collaborative-autoresearch-demo/blob/main/program.md).

This is actual swarm research infrastructure: independent GPU-equipped agents experiment, communicate results over an AXL/Yggdrasil mesh, and incorporate peers' improvements. Static audit: `all_peer_ids` at line 214 combines direct peers and spanning-tree entries; `broadcast_finding` at 238 sends status/metric/description/commit and includes source only for retained improvements. Receiving at 311 deduplicates sender-round pairs and prefers the transport sender identity. `should_adopt` at 391 requires retained source and improvement ≥0.002 validation bits/byte. The experiment protocol requires rerunning adopted code locally and reverting regressions.

Important limitation: verification is an instruction to the agent, not enforced inside the network helper. Its peer-best registry is in memory. The README's “super-linear” search language is not supported there by a controlled comparison. Strong acquisition candidate for studying transmission of methods and negative results; no linked swarm-specific paper located.

## 2. SwarmFeed: inspect the algorithms governing agents' attention

[Repository](https://github.com/swarmclawai/swarmfeed); [audited feed implementation](https://github.com/swarmclawai/swarmfeed/blob/main/packages/api/src/lib/feed-algorithm.ts).

A complete agent social-network codebase rather than a landing page: posts, replies, follows, topic channels, moderation, API/SDK/MCP access. Hosted service is explicitly discontinued; it is self-host-only. The code supplies a valuable experimental substrate for social swarms.

`scorePost` at line 155 mixes normalized engagement, velocity, quality, exponential recency, author reputation, and social proof, with follow/freshness/conversation bonuses and ±15% randomness. `diversify` at 183 caps posts per author; topic spreading at 209 defers repeated hashtags. Reputation at 245 combines capped follower counts and average engagement equally. Trending at 439 prioritizes engagement/hour and freshness.

These are explicit attention-allocation and popularity mechanisms, not verified-knowledge ranking. Researchers could intervene on them to measure repetition, minority-evidence suppression, and discovery. Code caution: the reputation comment says recent 50 posts per author, but its SQL actually limits a jointly ordered candidate pool to 500 rows. No linked research paper located.

## 3. Failure-First's vocabulary-diffusion field experiment

[First-party experiment report, March 10, 2026](https://failurefirst.ai/blog/moltbook-social-experiment/); [research programme](https://failurefirst.ai/research/moltbook/).

Researchers describe a two-week intervention: nine posts in six Moltbook communities, including a novel term intended to propagate. They report zero upvotes and twenty comments, eighteen classified as automated spam; vocabulary uptake reached only one commenter. This is directly relevant to whether social-agent interaction transmits concepts, including a useful negative result rather than an assumption that exposure becomes collective learning.

The sample is tiny, and the authors explicitly cannot distinguish weak agent engagement capacity from suppressive platform incentives. Their inference that karma incentives explain the behavior is not a randomized platform intervention. The footer links the verified [public repository](https://github.com/failurefirst/failure-first), whose README says full datasets, traces, and runner infrastructure remain private; it is not a public reproduction package. Use as a bounded firsthand observation; do not generalize the rates to Moltbook overall.

## 4. Agent Swarm's organizational postmortem: shared files are insufficient

[First-party post, June 24, 2026](https://www.agent-swarm.dev/blog/deep-dive-agent-coordination-anti-patterns); [site-linked repository](https://github.com/desplega-ai/agent-swarm).

An operating swarm's maintainers describe redundant research documents, information silos, and stale shared material. Their proposed discovery-before-writing hook searches for related work and updates an existing document when coverage exceeds 80%; they report roughly 60% fewer duplicates while acknowledging added latency and unresolved staleness. The concrete lesson is to distinguish shared storage from successful uptake by peers.

Evidence is an uncontrolled engineering report; displayed hook configuration is illustrative and was not verified against repository enforcement. Include this specific swarm communication postmortem, not the broader generic runtime as a core swarm algorithm. Its lead-worker architecture is orchestrated, not decentralized.

## Rejected after inspection

`joelhooks/atproto-agent-network` advertises federation, but audited `apps/network/src/relay.ts:798` leaves peer listing as a TODO. Useful messaging infrastructure exists, yet treating the README federation protocol as implemented would overclaim. It is weaker than the four additions above for this report.
