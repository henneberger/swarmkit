"""Dependency-aware parallel work and compact handoffs.

Engineering mechanisms inspired by PARL/SearchSwarm, without claiming their
learned orchestrator checkpoints or training pipelines:
https://arxiv.org/abs/2602.02276 ; https://arxiv.org/abs/2606.09730
"""

from __future__ import annotations

import asyncio
import copy
import math
import time
from dataclasses import replace
from typing import Awaitable, Callable, Mapping, Sequence

from .types import AlgorithmResult, Budget, Task


def critical_path(durations: Mapping[str, float], dependencies: Mapping[str, Sequence[str]]) -> float:
    """Longest weighted path in a DAG (not total work). Reject cycles/missing jobs."""
    if set(dependencies) - set(durations) or any(not math.isfinite(v) or v < 0 for v in durations.values()):
        raise ValueError("invalid durations or dependency nodes")
    done, visiting = {}, set()

    def finish(node: str) -> float:
        if node not in durations:
            raise ValueError(f"unknown dependency: {node}")
        if node in visiting:
            raise ValueError("dependency cycle")
        if node in done:
            return done[node]
        visiting.add(node)
        done[node] = durations[node] + max((finish(dep) for dep in dependencies.get(node, ())), default=0.0)
        if not math.isfinite(done[node]):
            raise ValueError("critical path exceeds numerical range")
        visiting.remove(node)
        return done[node]

    return max((finish(node) for node in durations), default=0.0)


class DAGExecutor:
    """Run independent task frontiers concurrently, supplying completed handoffs.

    Each Task declares metadata['depends_on'] = sequence of task ids. Workers
    receive only their direct dependency results in metadata['dependency_results'].
    A failed task blocks descendants, while independent branches continue. A
    call budget bounds dispatches; token/cost soft limits use returned metrics.
    """

    def __init__(
        self,
        worker: Callable[[Task], Awaitable[AlgorithmResult]],
        *,
        concurrency: int = 8,
        timeout: float | None = 60,
        budget: Budget | None = None,
    ):
        if (
            not isinstance(concurrency, int)
            or concurrency < 1
            or (timeout is not None and (not math.isfinite(timeout) or timeout <= 0))
        ):
            raise ValueError("concurrency and timeout must be positive")
        self.worker, self.concurrency, self.timeout = worker, concurrency, timeout
        self.budget = budget or Budget()

    async def run(self, tasks: Sequence[Task]) -> AlgorithmResult:
        jobs = {task.id: task for task in tasks}
        if len(jobs) != len(tasks):
            raise ValueError("duplicate task ids")
        dependencies = {}
        for task in tasks:
            declared = task.metadata.get("depends_on", ())
            if isinstance(declared, (str, bytes)):
                raise ValueError("depends_on must be a sequence of task IDs, not a string")
            dependencies[task.id] = tuple(declared)
        critical_path({key: 1 for key in jobs}, dependencies)  # validate before any side effect
        pending, results, errors, durations = set(jobs), {}, {}, {}
        while pending:
            blocked = {key for key in pending if any(dep in errors for dep in dependencies[key])}
            for key in blocked:
                errors[key] = "dependency failed"
            pending -= blocked
            if not pending or self.budget.exhausted:
                break
            ready = [
                key for key in jobs if key in pending and all(dep in results for dep in dependencies[key])
            ]
            if not ready:
                continue  # blocked status propagates to the next generation
            # Dispatch only one concurrency-sized batch so soft limits are checked between batches.
            ready = ready[: self.concurrency]
            if self.budget.max_calls is not None:
                ready = ready[: max(0, self.budget.max_calls - self.budget.used_calls)]
            if not ready:
                break
            self.budget.used_calls += len(ready)

            async def invoke(key: str):
                start = time.monotonic()
                try:
                    task = replace(
                        jobs[key],
                        metadata={
                            **copy.deepcopy(jobs[key].metadata),
                            "dependency_results": copy.deepcopy(
                                {dep: results[dep] for dep in dependencies[key]}
                            ),
                        },
                    )
                    call = self.worker(task)
                    result = await asyncio.wait_for(call, self.timeout) if self.timeout else await call
                    if not isinstance(result, AlgorithmResult):
                        raise TypeError("worker must return AlgorithmResult")
                    tokens = result.metrics.get("tokens", 0)
                    cost = result.metrics.get("cost", 0.0)
                    if (
                        tokens < 0
                        or cost < 0
                        or not math.isfinite(tokens)
                        or not math.isfinite(cost)
                        or tokens != int(tokens)
                    ):
                        raise ValueError("invalid worker usage metrics")
                    if not math.isfinite(self.budget.used_cost + cost):
                        raise ValueError("accumulated worker cost exceeds numerical range")
                    self.budget.used_tokens += int(tokens)
                    self.budget.used_cost += float(cost)
                    results[key] = result
                except Exception as exc:
                    errors[key] = f"{type(exc).__name__}: {exc}"
                finally:
                    durations[key] = time.monotonic() - start

            await asyncio.gather(*(invoke(key) for key in ready))
            pending -= set(ready)
            self.budget.used_steps += 1
        for key in pending:
            errors[key] = "budget exhausted"
        successful = [results[key] for key in jobs if key in results]
        observed = {key: durations.get(key, 0.0) for key in jobs}
        return AlgorithmResult(
            tuple(m for result in successful for m in result.messages),
            tuple(d for result in successful for d in result.decisions),
            tuple(a for result in successful for a in result.artifacts),
            {
                "completed": float(len(results)),
                "failed": float(len(errors)),
                "critical_path_seconds": critical_path(observed, dependencies),
                "total_work_seconds": sum(observed.values()),
            },
            {"results": results, "errors": errors},
        )
