"""Offline checks only: provider requests are replaced, never sent."""

import asyncio
import json
import multiprocessing
import threading
import urllib.error
from concurrent.futures import ThreadPoolExecutor

import pytest

from swarmkit.providers.deepseek import (
    DeepSeekClient,
    GateBusy,
    GateDenied,
    GateLimits,
    ProviderError,
    SQLiteCallGate,
    _NoRedirect,
)


def gate(tmp_path, **kwargs):
    options = dict(
        max_calls=20, max_tokens=100_000, max_usd=1, max_concurrency=4, requests_per_minute=1_000_000_000
    )
    options.update(kwargs)
    return SQLiteCallGate(tmp_path / "calls.sqlite", limits=GateLimits(**options), enabled=True)


def response(inputs=10, outputs=5):
    return {
        "id": "test-request",
        "usage": {"prompt_tokens": inputs, "completion_tokens": outputs},
        "choices": [{"message": {"content": '{"ok":true}'}, "finish_reason": "stop"}],
    }


def test_persistent_opt_in_and_pause(tmp_path):
    path = tmp_path / "gate.sqlite"
    first = SQLiteCallGate(path)
    with pytest.raises(GateDenied):
        first.reserve(1, 1)
    first.set_enabled(True)
    reopened = SQLiteCallGate(path)
    first.reserve(1, 1)
    reopened.set_paused(True)
    with pytest.raises(GateDenied):
        first.reserve(1, 1)
    assert reopened.status()["calls"] == 1
    assert reopened.status()["paused"]
    with pytest.raises(ValueError, match="limits differ"):
        SQLiteCallGate(path, limits=GateLimits(max_calls=3))


def _process_reserve(path):
    try:
        SQLiteCallGate(path).reserve(10, 10)
        return True
    except GateDenied:
        return False


def test_atomic_budget_across_processes(tmp_path):
    limiter = gate(tmp_path, max_calls=3, max_concurrency=10)
    with multiprocessing.get_context("spawn").Pool(4) as pool:
        outcomes = pool.map(_process_reserve, [str(limiter.path)] * 12)
    assert sum(outcomes) == 3
    assert limiter.status()["calls"] == 3


def test_atomic_concurrency_threads_and_unknown(tmp_path):
    limiter = gate(tmp_path, max_concurrency=2)

    def reserve():
        try:
            return limiter.reserve(10, 20)
        except GateBusy:
            return None

    with ThreadPoolExecutor(max_workers=8) as pool:
        ids = [i for i in pool.map(lambda _: reserve(), range(8)) if i]
    assert len(ids) == 2
    limiter.mark_unknown(ids[0])
    limiter.release_slot(ids[0])
    limiter.reconcile(ids[0], 0, 0)
    assert limiter.status()["tokens"] == 60
    assert limiter.status()["active"] == 1
    assert limiter.status()["unknown_calls"] == 1


@pytest.mark.parametrize(
    "limits,inputs,outputs",
    [
        ({"max_tokens": 9}, 5, 5),
        ({"max_usd": 0.000001}, 0, 1),
    ],
)
def test_reject_before_reservation(tmp_path, limits, inputs, outputs):
    limiter = gate(tmp_path, **limits)
    with pytest.raises(GateDenied):
        limiter.reserve(inputs, outputs)
    assert limiter.status()["calls"] == 0


def test_reconcile_and_overrun_pauses(tmp_path):
    limiter = gate(tmp_path)
    one = limiter.reserve(100, 50)
    limiter.reconcile(one, 10, 5)
    limiter.reconcile(one, 0, 0)
    assert limiter.status()["tokens"] == 15
    two = limiter.reserve(10, 5)
    limiter.reconcile(two, 11, 5)
    assert limiter.status()["paused"]
    assert limiter.status()["tokens"] == 31


def test_rate_limits(tmp_path):
    limiter = gate(tmp_path, requests_per_minute=1)
    one = limiter.reserve(1, 1)
    limiter.release_slot(one)
    with pytest.raises(GateBusy) as failure:
        limiter.reserve(1, 1)
    assert 0 < failure.value.retry_after <= 60


async def test_request_contract_and_usage(tmp_path, monkeypatch):
    limiter = gate(tmp_path)
    client = DeepSeekClient(gate=limiter, api_key="secret-test-only")
    bodies = []

    def request(body):
        bodies.append(json.loads(body))
        return response()

    monkeypatch.setattr(client, "_request", request)
    result = await client.complete(
        [{"role": "user", "content": 'Reply JSON: {"ok":true}'}], max_output_tokens=64, json_mode=True
    )
    assert result.usage.tokens == 15
    assert result.usage.calls == 1
    assert bodies[0]["thinking"] == {"type": "disabled"}
    assert bodies[0]["response_format"] == {"type": "json_object"}
    assert bodies[0]["max_tokens"] == 64
    assert limiter.status()["tokens"] == 15
    assert limiter.status()["active"] == 0
    assert "secret-test-only" not in repr(client)
    assert b"secret-test-only" not in limiter.path.read_bytes()
    assert b"Reply JSON" not in limiter.path.read_bytes()


async def test_disabled_means_no_network(tmp_path, monkeypatch):
    limiter = gate(tmp_path)
    limiter.set_enabled(False)
    client = DeepSeekClient(gate=limiter, api_key="secret")
    monkeypatch.setattr(client, "_request", lambda _: pytest.fail("network must not run"))
    with pytest.raises(GateDenied):
        await client.complete([{"role": "user", "content": "hi"}])


async def test_auth_no_retry_and_pauses(tmp_path, monkeypatch):
    limiter = gate(tmp_path)
    client = DeepSeekClient(gate=limiter, api_key="secret", max_retries=3)

    def request(_):
        raise ProviderError("provider HTTP request failed", status=401)

    monkeypatch.setattr(client, "_request", request)
    with pytest.raises(ProviderError):
        await client.complete([{"role": "user", "content": "hi"}])
    status = limiter.status()
    assert status["calls"] == 1
    assert status["unknown_calls"] == 1
    assert status["tokens"] > 1024
    assert status["active"] == 0
    assert status["paused"]


async def test_retry_has_separate_reservation_and_usage(tmp_path, monkeypatch):
    limiter = gate(tmp_path)
    client = DeepSeekClient(gate=limiter, api_key="secret", max_retries=1)
    calls = []

    def request(_):
        calls.append(1)
        if len(calls) == 1:
            raise ProviderError("provider failed", status=503, retryable=True)
        return response()

    monkeypatch.setattr(client, "_request", request)
    result = await client.complete([{"role": "user", "content": "hi"}], max_output_tokens=32)
    status = limiter.status()
    assert status["calls"] == result.usage.calls == 2
    assert status["unknown_calls"] == 1
    assert status["tokens"] == result.usage.tokens > 15
    assert status["cost_usd"] == pytest.approx(result.usage.cost)


async def test_missing_usage_keeps_reservation(tmp_path, monkeypatch):
    limiter = gate(tmp_path)
    client = DeepSeekClient(gate=limiter, api_key="secret")
    monkeypatch.setattr(client, "_request", lambda _: {"choices": []})
    with pytest.raises(ProviderError):
        await client.complete([{"role": "user", "content": "hi"}])
    assert limiter.status()["unknown_calls"] == 1
    assert limiter.status()["tokens"] > 1024


async def test_cancellation_keeps_charge_and_live_slot(tmp_path, monkeypatch):
    limiter = gate(tmp_path, max_concurrency=1)
    client = DeepSeekClient(gate=limiter, api_key="secret")
    started, finish = threading.Event(), threading.Event()

    def request(_):
        started.set()
        finish.wait(timeout=3)
        return response()

    monkeypatch.setattr(client, "_request", request)
    task = asyncio.create_task(client.complete([{"role": "user", "content": "hi"}]))
    await asyncio.to_thread(started.wait, 2)
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    status = limiter.status()
    assert status["active"] == 1
    assert status["unknown_calls"] == 1
    charged = status["tokens"]
    with pytest.raises(GateBusy):
        limiter.reserve(1, 1)
    finish.set()
    for _ in range(100):
        if not limiter.status()["active"]:
            break
        await asyncio.sleep(0.01)
    assert limiter.status()["active"] == 0
    assert limiter.status()["tokens"] == charged


def test_fixed_host_redirect_and_sanitized_errors(tmp_path, monkeypatch):
    limiter = gate(tmp_path)
    client = DeepSeekClient(gate=limiter, api_key="secret-test-only")

    class Opener:
        def open(self, request, timeout):
            assert request.full_url == "https://api.deepseek.com/chat/completions"
            raise urllib.error.HTTPError(request.full_url, 401, "secret-test-only", {}, None)

    monkeypatch.setattr("urllib.request.build_opener", lambda *args: Opener())
    with pytest.raises(ProviderError) as failure:
        client._request(b"{}")
    assert "secret-test-only" not in str(failure.value)
    assert failure.value.__suppress_context__
    assert _NoRedirect().redirect_request(None, None, 302, "", {}, "https://evil.test") is None


def test_limit_update_preserves_counters_flags_and_audit(tmp_path):
    from dataclasses import replace

    limiter = gate(tmp_path)
    first = limiter.reserve(10, 20)
    limiter.mark_unknown(first)
    limiter.release_slot(first)
    limiter.set_enabled(False)
    limiter.set_paused(True)
    before = limiter.status()
    old = limiter.limits
    limiter.set_limits(replace(old, max_calls=160), expected=old)
    after = limiter.status()
    assert after == {**before, "limits": {**before["limits"], "max_calls": 160}}
    history = limiter.limits_history()
    assert len(history) == 1
    assert history[0]["old_limits"]["max_calls"] == old.max_calls
    assert history[0]["new_limits"]["max_calls"] == 160
    assert history[0]["calls"] == 1
    assert history[0]["tokens"] == 30
    assert not after["enabled"] and after["paused"]


@pytest.mark.parametrize("changes", [{"max_tokens": 29}, {"max_usd": 0.000001}, {"max_concurrency": 1}])
def test_limit_decrease_cannot_undercut_reserved_usage(tmp_path, changes):
    from dataclasses import replace

    limiter = gate(tmp_path)
    limiter.reserve(10, 10)
    limiter.reserve(5, 5)
    old = limiter.limits
    with pytest.raises(ValueError, match="charged/reserved"):
        limiter.set_limits(replace(old, **changes))
    assert limiter.limits == old
    assert limiter.limits_history() == []


def test_existing_gate_reads_other_instance_limit_changes(tmp_path):
    from dataclasses import replace

    limiter = gate(tmp_path, max_calls=1)
    observer = SQLiteCallGate(limiter.path)
    old = limiter.limits
    call = limiter.reserve(1, 1)
    limiter.release_slot(call)
    with pytest.raises(GateDenied):
        observer.reserve(1, 1)
    limiter.set_limits(replace(old, max_calls=2))
    assert observer.status()["limits"]["max_calls"] == observer.limits.max_calls == 2
    observer.reserve(1, 1)
    with pytest.raises(ValueError, match="concurrently"):
        observer.set_limits(replace(old, max_tokens=200_000), expected=old)
    with pytest.raises(ValueError, match="charged/reserved"):
        observer.set_limits(old)
    assert len(limiter.limits_history()) == 1


def test_budget_cli_changes_only_requested_field_and_never_resumes(tmp_path, capsys):
    from swarmkit.enron.cli import main

    limiter = gate(tmp_path)
    limiter.reserve(10, 20)
    limiter.set_paused(True)
    before = limiter.status()
    main(
        [
            "--workspace",
            str(tmp_path / "workspace"),
            "--ledger",
            str(limiter.path),
            "budget",
            "--max-calls",
            "160",
        ]
    )
    result = json.loads(capsys.readouterr().out)
    assert result["gate"] == {**before, "limits": {**before["limits"], "max_calls": 160}}
    assert len(result["limits_history"]) == 1
