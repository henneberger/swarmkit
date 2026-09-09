import pytest

from swarmkit.stigmergy import StigmergicPolicy
from swarmkit.types import AgentState, Artifact, Feedback, SwarmState, Task


def test_local_observation_and_verified_inheritance_after_author_removal():
    state = SwarmState({"a": AgentState("a", position=(0, 0)), "b": AgentState("b", position=(20, 0))})
    state.artifacts["x"] = Artifact(
        "x", "departed", "procedure", verified=True, metadata={"position": (1, 0)}
    )
    policy = StigmergicPolicy(radius=2, exploration=0, verify=lambda *args: Feedback(1, verified=True))
    result = policy.step(state, Task("t", ""))
    assert result.metrics["adopted"] == 1
    assert state.agents["a"].memory["adopted_artifacts"] == {"x"}
    assert "adopted_artifacts" not in state.agents["b"].memory
    assert policy.strength(state, "x") == 1
    state.step = 10
    assert policy.strength(state, "x") == 0.5
    policy.deposit(state, "x", "a")
    assert policy.strength(state, "x") == 1  # refresh, not duplicate corroboration


def test_failed_local_validation_does_not_create_success_trace():
    state = SwarmState({"a": AgentState("a")})
    state.artifacts["x"] = Artifact("x", "a", "bad", verified=True)
    policy = StigmergicPolicy(verify=lambda *args: Feedback(100, verified=False))
    result = policy.step(state, Task("t", ""))
    assert result.metrics["adopted"] == 0
    assert policy.strength(state, "x") == 0
    state.artifacts["y"] = Artifact("y", "a", "unverified")
    with pytest.raises(ValueError):
        policy.deposit(state, "y", "a")


def test_task_specific_adoption_and_mutable_artifact_isolation():
    state = SwarmState({"a": AgentState("a")})
    state.artifacts["x"] = Artifact("x", "a", {"value": 1}, verified=True)

    def verify(agent, artifact, task):
        artifact.content["value"] = 99
        return Feedback(float(task.id == "useful"), verified=True)

    policy = StigmergicPolicy(verify=verify, minimum_utility=0.5)
    assert policy.step(state, Task("wrong", "")).metrics["adopted"] == 0
    assert policy.step(state, Task("useful", "")).metrics["adopted"] == 1
    assert state.artifacts["x"].content == {"value": 1}


def test_failed_verifier_can_be_retried_without_false_seen_state():
    state = SwarmState({"a": AgentState("a")})
    state.artifacts["x"] = Artifact("x", "a", "", verified=True)
    attempts = []

    def verify(*args):
        attempts.append(1)
        if len(attempts) == 1:
            raise RuntimeError("transient")
        return Feedback(1, verified=True)

    policy = StigmergicPolicy(verify=verify)
    with pytest.raises(RuntimeError):
        policy.step(state, Task("t", ""))
    assert policy.step(state, Task("t", "")).metrics["adopted"] == 1
