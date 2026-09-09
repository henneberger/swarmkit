import asyncio

import pytest

from swarmkit.scheduling import DAGExecutor, critical_path
from swarmkit.types import AlgorithmResult, Budget, Task


def test_critical_path_and_cycles():
    assert critical_path({"a": 2, "b": 3, "c": 4}, {"c": ["a", "b"]}) == 7
    with pytest.raises(ValueError):
        critical_path({"a": 1}, {"a": ["a"]})
    with pytest.raises(ValueError):
        critical_path({"a": 1}, {"a": ["missing"]})


@pytest.mark.asyncio
async def test_parallel_handoff_and_budget():
    active = 0
    peak = 0

    async def worker(task):
        nonlocal active, peak
        active += 1
        peak = max(peak, active)
        await asyncio.sleep(0.01)
        if task.id == "c":
            assert set(task.metadata["dependency_results"]) == {"a", "b"}
        active -= 1
        return AlgorithmResult(metrics={"tokens": 2})

    tasks = [Task("a", "a"), Task("b", "b"), Task("c", "c", metadata={"depends_on": ["a", "b"]})]
    result = await DAGExecutor(worker, concurrency=2).run(tasks)
    assert result.metrics["completed"] == 3
    assert peak == 2
    assert result.metrics["total_work_seconds"] >= result.metrics["critical_path_seconds"]
    result = await DAGExecutor(worker, budget=Budget(max_calls=1)).run(tasks)
    assert result.metrics["completed"] == 1
    assert set(result.metadata["errors"]) == {"b", "c"}


@pytest.mark.asyncio
async def test_failed_dependency_blocks_but_unrelated_work_survives():
    executed = []

    async def worker(task):
        executed.append(task.id)
        if task.id == "a":
            raise RuntimeError("failed")
        return AlgorithmResult()

    tasks = [Task("a", ""), Task("b", "", metadata={"depends_on": ["a"]}), Task("c", "")]
    result = await DAGExecutor(worker).run(tasks)
    assert set(executed) == {"a", "c"}
    assert result.metadata["errors"]["b"] == "dependency failed"


@pytest.mark.asyncio
async def test_scheduler_copies_task_inputs_and_rejects_fractional_usage():
    metadata = {"mutable": {"x": 0}}

    async def worker(task):
        task.metadata["mutable"]["x"] = 10
        return AlgorithmResult(metrics={"tokens": 1.5})

    result = await DAGExecutor(worker).run([Task("a", "", metadata=metadata)])
    assert result.metrics["completed"] == 0
    assert "invalid worker usage" in result.metadata["errors"]["a"]
    assert metadata["mutable"]["x"] == 0


@pytest.mark.asyncio
async def test_scheduler_invalid_configuration_and_dependency_declaration():
    async def worker(task):
        return AlgorithmResult()

    for kwargs in ({"concurrency": 1.5}, {"timeout": float("nan")}, {"timeout": float("inf")}):
        with pytest.raises(ValueError):
            DAGExecutor(worker, **kwargs)
    with pytest.raises(ValueError, match="sequence"):
        await DAGExecutor(worker).run([Task("a", ""), Task("b", "", metadata={"depends_on": "a"})])
    with pytest.raises(ValueError, match="numerical range"):
        critical_path({"a": 1e308, "b": 1e308}, {"b": ["a"]})
