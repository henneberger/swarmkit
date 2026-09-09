"""Offline graph learning from actual routed evidence and edge cost.

Run: python examples/learn_topology.py
This trains three Bernoulli edges, not transformer weights. The synthetic task
rewards a useful scout->solver edge and penalizes unnecessary communication.
"""

from __future__ import annotations

import json

from swarmkit.deliberation import evidence_decision
from swarmkit.runtime import MessageBus
from swarmkit.topology import BernoulliDAGPolicy
from swarmkit.types import AgentState, Evidence, Feedback, Message, SwarmState, Task


def train_demo(iterations: int = 500, seed: int = 17) -> dict:
    if iterations < 1:
        raise ValueError("iterations must be positive")
    observation = Evidence(
        "measurement", "B satisfies the measured constraint.", "sensor", "scout", supports=("B",)
    )
    prior = Evidence(
        "prior",
        "A appears preferable before measurement.",
        "prior",
        "solver",
        confidence=0.5,
        supports=("A",),
    )
    state = SwarmState(
        {
            "scout": AgentState("scout", private_evidence=(observation,)),
            "bystander": AgentState("bystander"),
            "solver": AgentState("solver", private_evidence=(prior,)),
        },
        seed=seed,
    )
    task = Task("measurement-task", "Choose the measured feasible option.", ("A", "B"))
    policy = BernoulliDAGPolicy(learning_rate=0.25, edge_penalty=0.2)
    initial = policy.probabilities(state)
    bus = MessageBus(policy)
    success = []
    for iteration in range(iterations):
        for agent in state.agents.values():
            agent.inbox.clear()
        policy.sample(state)
        bus.publish(
            state,
            Message(
                "scout",
                observation.claim,
                evidence=(observation,),
                step=state.step,
                id=f"measurement-{iteration}",
            ),
        )
        bus.publish(
            state, Message("bystander", "No relevant observation.", step=state.step, id=f"noise-{iteration}")
        )
        solver = state.agents["solver"]
        received = solver.private_evidence + tuple(e for message in solver.inbox for e in message.evidence)
        decision = evidence_decision(solver, task, received)
        correct = float(decision.answer == "B")
        success.append(correct)
        policy.update(state, Feedback(correct, verified=True))
        state.step += 1  # A new sample is required before the next policy update.
    return {
        "iterations": iterations,
        "initial_probabilities": {f"{a}->{b}": p for (a, b), p in initial.items()},
        "learned_probabilities": {
            f"{a}->{b}": round(p, 4) for (a, b), p in policy.probabilities(state).items()
        },
        "last_100_success_rate": sum(success[-100:]) / len(success[-100:]),
        "training_feedback": "Measured answer correctness minus sampled-edge cost",
    }


if __name__ == "__main__":
    print(json.dumps(train_demo(), indent=2))
