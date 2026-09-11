"""Opt-in DeepSeek V4.1 Flash access through a durable, process-shared budget gate.

Official contracts checked 2026-09-09:
https://api-docs.deepseek.com/api/create-chat-completion/
https://api-docs.deepseek.com/guides/thinking_mode/
https://api-docs.deepseek.com/guides/json_mode/
https://api-docs.deepseek.com/quick_start/pricing/

Reservations use peak cache-miss prices ($0.44/$1.32 per million input/output
 tokens). UTF-8 bytes plus framing headroom conservatively estimate text input;
this is not an official tokenizer. Unexpected usage exceeding a reservation
pauses the gate. Unknown outcomes retain their entire reservation. Process death
leaves active slots blocked: recover only after confirming the request ended.
The ledger contains counters, never prompts, responses, or credentials.
"""

from __future__ import annotations

import asyncio
import json
import math
import os
import sqlite3
import threading
import time
import urllib.error
import urllib.request
import uuid
from contextlib import contextmanager
from dataclasses import asdict, dataclass, replace
from decimal import Decimal
from pathlib import Path
from typing import Any, Mapping, Sequence

from swarmkit.types import Usage

ENDPOINT = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-flash"
# Retain the historical, higher price bound so reopening an existing ledger
# never reprices its previous charges downward. V4.1 peak prices checked
# 2026-09-10 are $0.30/$1.20; reported cost is a conservative bound, not a bill.
# Integer nanodollars per token avoids floating point admission errors.
INPUT_NANODOLLARS = 440
OUTPUT_NANODOLLARS = 1320


class GateDenied(RuntimeError):
    """Disabled, paused, or exhausted gate; no network request was made."""


class GateBusy(GateDenied):
    def __init__(self, retry_after: float):
        super().__init__("API gate concurrency or rate limit reached")
        self.retry_after = retry_after


class ProviderError(RuntimeError):
    """Sanitized provider failure, without response bodies or request headers."""

    def __init__(self, message: str, *, status: int | None = None, retryable: bool = False):
        super().__init__(message)
        self.status = status
        self.retryable = retryable


@dataclass(frozen=True)
class GateLimits:
    max_calls: int = 24
    max_tokens: int = 150_000
    max_usd: float = 1.0
    max_concurrency: int = 4
    requests_per_minute: int = 60

    def __post_init__(self) -> None:
        for name in ("max_calls", "max_tokens", "max_concurrency", "requests_per_minute"):
            value = getattr(self, name)
            if type(value) is not int or value <= 0:
                raise ValueError(f"{name} must be a positive integer")
        if not math.isfinite(self.max_usd) or self.max_usd <= 0:
            raise ValueError("max_usd must be positive and finite")


class SQLiteCallGate:
    """One ledger per spending scope, shared by every process using that scope.

    New ledgers are disabled unless explicitly enabled. Reopening never changes
    persisted enable/pause flags or limits. Different supplied limits are rejected;
    use ``set_limits`` for an explicit, audited budget update. No automatic stale-slot expiration
    is safe: an interrupted process may have left a billable request in flight.
    """

    def __init__(self, path: str | Path, *, limits: GateLimits | None = None, enabled: bool = False):
        if str(path) == ":memory:":
            raise ValueError("gate requires a persistent SQLite file")
        self.path = Path(path).expanduser().resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        # Restrict a newly created ledger without changing permissions on existing files.
        try:
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            pass
        else:
            os.close(fd)
        with self._connect() as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS config (id INTEGER PRIMARY KEY, limits TEXT NOT NULL, "
                "enabled INTEGER NOT NULL, paused INTEGER NOT NULL)"
            )
            db.execute(
                "CREATE TABLE IF NOT EXISTS calls (id TEXT PRIMARY KEY, started REAL NOT NULL, "
                "input_reserved INTEGER NOT NULL, output_reserved INTEGER NOT NULL, "
                "input_charged INTEGER NOT NULL, output_charged INTEGER NOT NULL, "
                "status TEXT NOT NULL, active INTEGER NOT NULL)"
            )
            db.execute(
                "CREATE TABLE IF NOT EXISTS limits_history (id INTEGER PRIMARY KEY, changed REAL NOT NULL, "
                "old_limits TEXT NOT NULL, new_limits TEXT NOT NULL, calls INTEGER NOT NULL, "
                "tokens INTEGER NOT NULL, cost_nanodollars INTEGER NOT NULL)"
            )
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT limits FROM config WHERE id=1").fetchone()
            if row is None:
                initial_limits = limits or GateLimits()
                db.execute(
                    "INSERT INTO config VALUES (1, ?, ?, 0)",
                    (json.dumps(asdict(initial_limits), sort_keys=True), int(enabled)),
                )
            else:
                persisted = GateLimits(**json.loads(row[0]))
                if limits is not None and limits != persisted:
                    raise ValueError("ledger limits differ; reopen without limits and update explicitly")

    @contextmanager
    def _connect(self):
        db = sqlite3.connect(self.path, timeout=30)
        try:
            db.execute("PRAGMA busy_timeout=30000")
            with db:
                yield db
        finally:
            db.close()

    @staticmethod
    def _totals(db: sqlite3.Connection) -> tuple[int, int, int, int]:
        row = db.execute(
            "SELECT COUNT(*), COALESCE(SUM(input_charged),0), "
            "COALESCE(SUM(output_charged),0), COALESCE(SUM(active),0) FROM calls"
        ).fetchone()
        return tuple(row)

    @property
    def limits(self) -> GateLimits:
        """Read current persisted limits, including updates by another process."""
        with self._connect() as db:
            return GateLimits(**json.loads(db.execute("SELECT limits FROM config WHERE id=1").fetchone()[0]))

    def set_limits(self, limits: GateLimits, *, expected: GateLimits | None = None) -> None:
        """Atomically update caps without resetting spending, enable, or pause.

        Lower caps must still cover all charged/reserved usage and active calls.
        ``expected`` prevents lost updates when a UI edits selected fields from a
        previously read configuration. Every successful change is audited.
        """
        if not isinstance(limits, GateLimits):
            raise TypeError("limits must use GateLimits")
        with self._connect() as db:
            db.execute("BEGIN IMMEDIATE")
            old_json = db.execute("SELECT limits FROM config WHERE id=1").fetchone()[0]
            old = GateLimits(**json.loads(old_json))
            if expected is not None and old != expected:
                raise ValueError("ledger limits changed concurrently; read and retry")
            calls, inputs, outputs, active = self._totals(db)
            cost = inputs * INPUT_NANODOLLARS + outputs * OUTPUT_NANODOLLARS
            ceiling = int(Decimal(str(limits.max_usd)) * Decimal(10**9))
            if (
                calls > limits.max_calls
                or inputs + outputs > limits.max_tokens
                or cost > ceiling
                or active > limits.max_concurrency
            ):
                raise ValueError("new limits cannot be below charged/reserved usage or active calls")
            if old == limits:
                return
            new_json = json.dumps(asdict(limits), sort_keys=True)
            db.execute("UPDATE config SET limits=? WHERE id=1", (new_json,))
            db.execute(
                "INSERT INTO limits_history(changed,old_limits,new_limits,calls,tokens,cost_nanodollars) "
                "VALUES (?,?,?,?,?,?)",
                (time.time(), old_json, new_json, calls, inputs + outputs, cost),
            )

    def limits_history(self) -> list[dict[str, Any]]:
        with self._connect() as db:
            rows = db.execute(
                "SELECT id,changed,old_limits,new_limits,calls,tokens,cost_nanodollars "
                "FROM limits_history ORDER BY id"
            ).fetchall()
            return [
                {
                    "id": row[0],
                    "changed": row[1],
                    "old_limits": json.loads(row[2]),
                    "new_limits": json.loads(row[3]),
                    "calls": row[4],
                    "tokens": row[5],
                    "cost_usd": row[6] / 1e9,
                }
                for row in rows
            ]

    def status(self) -> dict[str, Any]:
        with self._connect() as db:
            db.execute("BEGIN")
            enabled, paused, encoded_limits = db.execute(
                "SELECT enabled, paused, limits FROM config WHERE id=1"
            ).fetchone()
            calls, inputs, outputs, active = self._totals(db)
            unknown = db.execute("SELECT COUNT(*) FROM calls WHERE status='unknown'").fetchone()[0]
            return {
                "enabled": bool(enabled),
                "paused": bool(paused),
                "limits": json.loads(encoded_limits),
                "calls": calls,
                "input_tokens": inputs,
                "output_tokens": outputs,
                "tokens": inputs + outputs,
                "cost_usd": (inputs * INPUT_NANODOLLARS + outputs * OUTPUT_NANODOLLARS) / 1e9,
                "active": active,
                "unknown_calls": unknown,
            }

    def set_enabled(self, enabled: bool) -> None:
        with self._connect() as db:
            db.execute("UPDATE config SET enabled=? WHERE id=1", (int(bool(enabled)),))

    def set_paused(self, paused: bool) -> None:
        """Pause future admissions; already dispatched calls may finish and bill."""
        with self._connect() as db:
            db.execute("UPDATE config SET paused=? WHERE id=1", (int(bool(paused)),))

    def reserve(self, input_tokens: int, output_tokens: int) -> str:
        for value in (input_tokens, output_tokens):
            if type(value) is not int or value < 0:
                raise ValueError("reservation tokens must be nonnegative integers")
        with self._connect() as db:
            db.execute("BEGIN IMMEDIATE")
            enabled, paused, encoded_limits = db.execute(
                "SELECT enabled, paused, limits FROM config WHERE id=1"
            ).fetchone()
            if not enabled or paused:
                raise GateDenied("API gate is disabled or paused")
            calls, inputs, outputs, active = self._totals(db)
            limit = GateLimits(**json.loads(encoded_limits))
            cost = (inputs + input_tokens) * INPUT_NANODOLLARS + (
                outputs + output_tokens
            ) * OUTPUT_NANODOLLARS
            max_cost = int(Decimal(str(limit.max_usd)) * Decimal(10**9))
            if calls >= limit.max_calls or inputs + outputs + input_tokens + output_tokens > limit.max_tokens:
                raise GateDenied("API call or token budget exhausted")
            if cost > max_cost:
                raise GateDenied("API dollar budget exhausted")
            if active >= limit.max_concurrency:
                raise GateBusy(0.05)
            now = time.time()
            recent = db.execute("SELECT started FROM calls ORDER BY started DESC LIMIT 1").fetchone()
            if recent:
                delay = recent[0] + 60.0 / limit.requests_per_minute - now
                if delay > 0:
                    raise GateBusy(min(delay, 60.0))
            call_id = uuid.uuid4().hex
            db.execute(
                "INSERT INTO calls VALUES (?, ?, ?, ?, ?, ?, 'reserved', 1)",
                (call_id, now, input_tokens, output_tokens, input_tokens, output_tokens),
            )
            return call_id

    def reconcile(self, call_id: str, input_tokens: int, output_tokens: int) -> None:
        """Replace conservative charges only with validated terminal usage once."""
        if any(type(x) is not int or x < 0 for x in (input_tokens, output_tokens)):
            raise ValueError("usage tokens must be nonnegative integers")
        with self._connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute(
                "SELECT input_reserved, output_reserved, status FROM calls WHERE id=?", (call_id,)
            ).fetchone()
            if row is None:
                raise KeyError("unknown reservation")
            if row[2] != "reserved":
                return
            db.execute(
                "UPDATE calls SET input_charged=?, output_charged=?, status='reconciled' WHERE id=?",
                (input_tokens, output_tokens, call_id),
            )
            if input_tokens > row[0] or output_tokens > row[1]:
                db.execute("UPDATE config SET paused=1 WHERE id=1")

    def mark_unknown(self, call_id: str) -> None:
        """Cancellation/transport ambiguity never refunds the reservation."""
        with self._connect() as db:
            db.execute(
                "UPDATE calls SET input_charged=MAX(input_reserved,input_charged), "
                "output_charged=MAX(output_reserved,output_charged), status='unknown' WHERE id=?",
                (call_id,),
            )

    def release_slot(self, call_id: str) -> None:
        """Release only after network activity ended; does not refund spending."""
        with self._connect() as db:
            db.execute("UPDATE calls SET active=0 WHERE id=?", (call_id,))


@dataclass(frozen=True)
class CompletionResult:
    text: str
    usage: Usage
    request_id: str
    input_tokens: int
    output_tokens: int
    finish_reason: str
    response_model: str = ""


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class DeepSeekClient:
    """Text-only Chat Completions; every attempt reserves through the same gate.

    JSON mode requires a JSON instruction/example in the caller's messages. No
    API key, raw HTTP error, response body, or authorization header is logged.
    Cancellation cannot stop urllib's thread; its slot stays occupied until that
    thread finishes. Retries count as additional calls and retain failed charges.
    """

    def __init__(
        self,
        *,
        gate: SQLiteCallGate,
        api_key: str | None = None,
        model: str = MODEL,
        timeout: float = 60.0,
        max_retries: int = 0,
    ):
        if model not in (MODEL, "deepseek-v4-flash"):
            raise ValueError("this pricing gate supports DeepSeek Flash only")
        if not math.isfinite(timeout) or timeout <= 0:
            raise ValueError("timeout must be positive and finite")
        if type(max_retries) is not int or not 0 <= max_retries <= 5:
            raise ValueError("max_retries must be between 0 and 5")
        self.gate, self.model, self.timeout, self.max_retries = gate, model, timeout, max_retries
        self._api_key = (
            api_key
            if api_key is not None
            else (os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("DEEPSEEK_API", ""))
        )
        if not self._api_key or any(c in self._api_key for c in "\r\n"):
            raise ValueError("a valid DEEPSEEK_API_KEY is required")

    def _request(self, body: bytes) -> dict[str, Any]:
        request = urllib.request.Request(
            ENDPOINT,
            data=body,
            method="POST",
            headers={"Authorization": "Bearer " + self._api_key, "Content-Type": "application/json"},
        )
        # Disable environment proxies as well as redirects: credentials only go
        # to the fixed TLS origin. No caller-supplied base URL or tools accepted.
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), _NoRedirect())
        try:
            with opener.open(request, timeout=self.timeout) as response:
                raw = response.read(16 * 1024 * 1024 + 1)
                if len(raw) > 16 * 1024 * 1024:
                    raise ProviderError("provider response exceeded size limit")
                data = json.loads(raw)
                if not isinstance(data, dict):
                    raise ProviderError("provider response must be an object")
                return data
        except urllib.error.HTTPError as exc:
            status = exc.code
            exc.close()
            raise ProviderError(
                "provider HTTP request failed", status=status, retryable=status in (429, 500, 502, 503, 504)
            ) from None
        except (urllib.error.URLError, TimeoutError, OSError):
            raise ProviderError("provider transport failed", retryable=True) from None
        except (ValueError, UnicodeError):
            raise ProviderError("provider returned invalid JSON") from None
        except ProviderError:
            raise
        except Exception:
            raise ProviderError("provider request failed") from None

    def _attempt(self, call_id: str, body: bytes, cancelled: threading.Event) -> CompletionResult:
        try:
            if cancelled.is_set():
                raise ProviderError("request cancelled before transport")
            data = self._request(body)
            try:
                usage = data["usage"]
                inputs, outputs = usage["prompt_tokens"], usage["completion_tokens"]
                if any(type(x) is not int or x < 0 for x in (inputs, outputs)):
                    raise ValueError
                choice = data["choices"][0]
                content = choice["message"]["content"]
                finish = choice["finish_reason"]
                if not isinstance(content, str) or not isinstance(finish, str):
                    raise ValueError
            except (KeyError, IndexError, TypeError, ValueError):
                raise ProviderError("provider response missing valid completion or usage") from None
            if cancelled.is_set():
                self.gate.mark_unknown(call_id)
            else:
                self.gate.reconcile(call_id, inputs, outputs)
            cost = (inputs * INPUT_NANODOLLARS + outputs * OUTPUT_NANODOLLARS) / 1e9
            return CompletionResult(
                content,
                Usage(calls=1, tokens=inputs + outputs, cost=cost),
                str(data.get("id", "")),
                inputs,
                outputs,
                finish,
                str(data.get("model", "")),
            )
        except BaseException:
            self.gate.mark_unknown(call_id)
            raise
        finally:
            self.gate.release_slot(call_id)

    async def complete(
        self,
        messages: Sequence[Mapping[str, str]],
        *,
        max_output_tokens: int = 1024,
        temperature: float = 0.0,
        thinking: bool = False,
        json_mode: bool = False,
    ) -> CompletionResult:
        if type(max_output_tokens) is not int or not 1 <= max_output_tokens <= 384_000:
            raise ValueError("max_output_tokens must be between 1 and 384000")
        if not math.isfinite(temperature) or not 0 <= temperature <= 2:
            raise ValueError("temperature must be in [0, 2]")
        clean = []
        for message in messages:
            if (
                set(message) != {"role", "content"}
                or message["role"] not in ("system", "user", "assistant")
                or not isinstance(message["content"], str)
            ):
                raise ValueError("messages require only a supported role and text content")
            clean.append(dict(message))
        if not clean:
            raise ValueError("at least one message is required")
        if json_mode and not any("json" in m["content"].lower() for m in clean if m["role"] != "assistant"):
            raise ValueError("JSON mode requires a JSON instruction and example in the prompt")
        payload = {
            "model": self.model,
            "messages": clean,
            "max_tokens": max_output_tokens,
            "temperature": temperature,
            "stream": False,
            "thinking": {"type": "enabled" if thinking else "disabled"},
        }
        if json_mode:
            payload["response_format"] = {"type": "json_object"}
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        estimated_input = len(body) + 256 * len(clean) + 1024
        if estimated_input + max_output_tokens > 1_000_000:
            raise ValueError("conservative request estimate exceeds model context")
        failed_calls = failed_tokens = 0
        failed_cost = 0.0
        for attempt in range(self.max_retries + 1):
            while True:
                try:
                    call_id = self.gate.reserve(estimated_input, max_output_tokens)
                    break
                except GateBusy as exc:
                    await asyncio.sleep(min(exc.retry_after, 0.25))
            cancelled = threading.Event()
            worker = asyncio.create_task(asyncio.to_thread(self._attempt, call_id, body, cancelled))
            # Consume eventual background exceptions when the caller cancels.
            worker.add_done_callback(lambda task: None if task.cancelled() else task.exception())
            try:
                result = await asyncio.shield(worker)
                return replace(
                    result,
                    usage=Usage(
                        calls=failed_calls + result.usage.calls,
                        tokens=failed_tokens + result.usage.tokens,
                        cost=failed_cost + result.usage.cost,
                    ),
                )
            except asyncio.CancelledError:
                cancelled.set()
                self.gate.mark_unknown(call_id)
                raise
            except ProviderError as exc:
                if exc.status in (401, 403):
                    self.gate.set_paused(True)
                failed_calls += 1
                failed_tokens += estimated_input + max_output_tokens
                failed_cost += (
                    estimated_input * INPUT_NANODOLLARS + max_output_tokens * OUTPUT_NANODOLLARS
                ) / 1e9
                if not exc.retryable or attempt >= self.max_retries:
                    raise
                await asyncio.sleep(min(2**attempt, 10))
        raise AssertionError("unreachable")
