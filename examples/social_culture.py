"""Offline conventions, ranked visibility, bounded evidence relay and maintenance.

Run: python examples/social_culture.py
Copying changes displayed choices; it does not demonstrate acquired expertise.
"""

from __future__ import annotations

import json

from swarmkit.evaluation import private_evidence_recovery
from swarmkit.knowledge import DecayingMemory, EvidenceRegistry
from swarmkit.runtime import MessageBus, Pipeline
from swarmkit.social import FeedPolicy, GossipRelay, NamingGame, ProportionalCopying
from swarmkit.topology import RingTopology
from swarmkit.types import AgentState, Artifact, Evidence, Message, SwarmState, Task


def run_demo(seed: int = 11) -> dict:
    names = tuple(f"agent{i}" for i in range(6))
    state = SwarmState({name: AgentState(name) for name in names}, seed=seed)
    task = Task("labels", "Coordinate a shared label.", ("amber", "blue"))
    naming = NamingGame(committed={"agent0": "blue"})
    for _ in range(100):
        Pipeline((naming,)).step(state, task)
    matched = sum(
        bool(a.memory.get("naming_game")) and a.memory["naming_game"][-1][2] > 0
        for a in state.agents.values()
    )

    # A visibility intervention makes the exact same population see one recent item.
    posts = (
        Message("agent1", "amber", step=0, id="old", metadata={"topic": "label", "social_proof": 10}),
        Message("agent0", "blue", step=state.step, id="fresh", metadata={"topic": "label"}),
    )
    feed = FeedPolicy(position_weight=0, recency_weight=1, proof_weight=0, reputation_weight=0)
    copying = ProportionalCopying(
        innovation=0, visible=lambda s, a: [message.content for message in feed.rank(posts, s.step, limit=1)]
    )
    copied = Pipeline((copying,)).step(state, task)

    fact = Evidence("observation", "The sensor was calibrated.", "calibration-log", "agent0")
    state.agents["agent0"].private_evidence = (fact,)
    ring = RingTopology()
    relay = GossipRelay(ring.neighbors, cards_per_round=1, ttl=10)
    routed = Pipeline((relay,), bus=MessageBus(ring))
    # Enough synchronous rounds for the ring diameter; no all-to-all shortcut.
    for _ in range(3):
        relayed = routed.step(state, task)
    inventories = state.data[relay.namespace]["known"]
    coverage = {name: private_evidence_recovery((fact,), inventories[name].values()) for name in names}
    registry = EvidenceRegistry(card for inventory in inventories.values() for card in inventory.values())

    memory = DecayingMemory(half_life=2, threshold=0.2)
    memory.write(Artifact("maintained", "agent0", "calibration procedure"), 0)
    memory.write(Artifact("forgotten", "agent0", "unmaintained record"), 0)
    memory.refresh("maintained", "agent1", 3)
    return {
        "naming_agents_last_matching": matched,
        "feed_selected": feed.rank(posts, state.step, limit=1)[0].content,
        "choices_after_visibility": sorted({d.answer for d in copied.decisions}),
        "relay_coverage": coverage,
        "relay_last_round_copies": relayed.metrics["0.evidence_copies"],
        "independent_evidence_sources": len(registry.independent_sources()),
        "maintained_records_at_step5": [artifact.id for artifact in memory.available(5)],
    }


if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
