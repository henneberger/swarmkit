"""Offline private-evidence exchange -> verified artifact -> peer adoption.

Run after installing the package: python examples/collective_discovery.py
This is a deterministic fixture, not an empirical claim about model performance.
"""

from __future__ import annotations

import json

from swarmkit.deliberation import ExchangeThenDecide, IndependentVoting, WeightedConsensus
from swarmkit.knowledge import ArtifactStore, EvidenceRegistry, PeerAdoption
from swarmkit.runtime import Pipeline, apply_result
from swarmkit.types import AgentState, AlgorithmResult, Artifact, Evidence, Feedback, SwarmState, Task


def run_demo() -> dict:
    common = Evidence("shared", "The advertised route A appears shorter.", "map", "all", supports=("A",))
    hidden = (
        Evidence("inspection", "A is blocked by construction.", "site-inspection", "scout", supports=("B",)),
        Evidence("measurement", "B is passable today.", "field-measurement", "scout", supports=("B",)),
    )
    task = Task("route", "Choose a usable route.", ("A", "B"))
    state = SwarmState(
        {
            name: AgentState(name, private_evidence=(common,))
            for name in ("planner1", "planner2", "planner3", "scout")
        },
        seed=7,
    )
    shared_votes = IndependentVoting().step(state, task)
    shared_winner = WeightedConsensus().aggregate(shared_votes.decisions, task).metadata["winner"]
    state.agents["scout"].private_evidence += hidden
    private_votes = IndependentVoting().step(state, task)
    private_winner = WeightedConsensus().aggregate(private_votes.decisions, task).metadata["winner"]

    exchange = ExchangeThenDecide()
    result = Pipeline((exchange, exchange, exchange)).step(state, task)
    consensus = WeightedConsensus().aggregate(result.decisions, task)
    winner = consensus.metadata["winner"]
    evidence = EvidenceRegistry(e for agent in state.agents.values() for e in agent.private_evidence)

    # Verification uses the fixture's measured passability, never ballot confidence.
    passable = {"A": False, "B": True}
    store = ArtifactStore(
        lambda artifact: Feedback(
            float(passable[artifact.content["route"]]), verified=passable[artifact.content["route"]]
        )
    )
    artifact = store.admit(Artifact("verified-route", "scout", {"route": winner}, evidence=evidence.evidence))
    apply_result(state, AlgorithmResult(artifacts=(artifact,)))

    def local_test(agent: AgentState, candidate: Artifact | None, local_task: Task) -> Feedback:
        utility = 0.2 if candidate is None else local_task.metadata["measured_utility"]
        return Feedback(utility, verified=True)

    adopter = PeerAdoption(store, local_test, minimum_gain=0.1)
    receiver = state.agents["planner1"]
    accepted = adopter.adopt(receiver, artifact.id, Task("local", "", metadata={"measured_utility": 0.9}))
    retained = adopter.audit(receiver, Task("holdout", "", metadata={"measured_utility": 0.8}))
    return {
        "shared_only_winner": shared_winner,
        "private_independent_winner": private_winner,
        "after_exchange_winner": winner,
        "consensus": consensus.metadata["converged"],
        "independent_sources": len(evidence.independent_sources()),
        "verified_artifact": state.artifacts[artifact.id].verified,
        "locally_adopted_and_retained": accepted and retained,
        "routed_messages": len(state.messages),
        "pipeline_steps": state.step,
    }


if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
