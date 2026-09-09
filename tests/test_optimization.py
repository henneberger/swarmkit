import pytest

from swarmkit.optimization import ParticleSwarmSearch
from swarmkit.types import AgentState, Artifact, Feedback, SwarmState, Task


def test_population_best_failure_memory_and_shared_artifacts():
    s = SwarmState({"a": AgentState("a"), "b": AgentState("b")}, seed=7)
    task = Task("t", "maximize")
    counter = iter(range(100))
    observed = []

    def mutate(current, personal, best, failures, rng):
        observed.append((current.author, best.score, len(failures)))
        delta = 1 if current.author == "a" else -1
        return Artifact(f"new-{next(counter)}", current.author, current.content + delta)

    algo = ParticleSwarmSearch(
        [Artifact("a0", "a", 1), Artifact("b0", "b", 3)],
        lambda a: Feedback(a.content, verified=True),
        mutate,
        failure_limit=2,
    )
    result = algo.step(s, task)
    assert result.metrics["best_score"] == 3
    assert s.step == 0
    assert not s.artifacts  # runtime commits outputs
    for _ in range(4):
        result = algo.step(s, task)
    assert result.metrics["best_score"] == 5
    assert result.metrics["failure_memory_size"] == 2
    assert all(a.verified and a.parents for a in result.artifacts)
    # Both candidates receive the same frozen global best for their generation.
    assert observed[0][1] == observed[1][1]
    assert observed[-1][2] == 2
    with pytest.raises(ValueError):
        algo.step(s, Task("different", "other"))


def test_minimize_costs_and_invalid_candidates():
    s = SwarmState({"a": AgentState("a")})
    task = Task("t", "minimize")
    algo = ParticleSwarmSearch(
        [Artifact("first", "a", 2)],
        lambda a: Feedback(a.content, costs=3),
        lambda c, p, g, f, r: Artifact("first", "a", 0),
        maximize=False,
    )
    assert algo.step(s, task).metrics["best_score"] == 5
    with pytest.raises(ValueError):
        algo.step(s, task)
    bad = ParticleSwarmSearch(
        [Artifact("x", "a", 1)],
        lambda a: Feedback(float("nan")),
        lambda *args: Artifact("z", "a", 0),
        key="bad",
    )
    with pytest.raises(ValueError):
        bad.step(s, task)
    assert "bad" not in s.data
