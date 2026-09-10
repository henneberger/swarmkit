"""Loopback-only, dependency-free monitor for an Enron research run.

Callbacks return JSON-serializable snapshots; the browser never receives provider
credentials. This server is for a single user's local machine, not deployment.
"""

from __future__ import annotations

import ipaddress
import json
from collections.abc import Callable
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, unquote, urlsplit

_STATIC = Path(__file__).with_name("static")
_FILES = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/style.css": ("style.css", "text/css; charset=utf-8"),
    "/app.js": ("app.js", "text/javascript; charset=utf-8"),
}


def monitor_view(value: dict[str, Any] | None, *, summary: bool = False) -> dict[str, Any] | None:
    """Project browser snapshots without copying resumable agent state.

    Histories are recent windows, not complete audit exports. Counts retain any
    upstream truncation so a SQL-limited callback cannot masquerade as complete.
    """
    if value is None:
        return None
    if summary:
        return {key: value[key] for key in ("id", "status", "mode", "created_at", "updated_at") if key in value}
    result = {key: item for key, item in value.items()
              if key not in {"state_snapshot", "resume_state", "agenda"}}
    agenda = value.get("agenda") or {}
    if isinstance(agenda, dict):
        for key in ("pending", "running"):
            if isinstance(agenda.get(key), list):
                result.setdefault(key + "_count", len(agenda[key]))
    counts = {key: dict(item) for key, item in (value.get("monitor_truncation") or {}).items()}
    for key, limit in (("posts", 200), ("events", 300), ("history", 300),
                       ("inquiries", 100), ("wiki", 200), ("cases", 200),
                       ("windows", 100), ("errors", 50), ("agent_errors", 50),
                       ("pending", 100), ("running", 100)):
        items = result.get(key)
        if isinstance(items, list):
            total = max(len(items), counts.get(key, {}).get("total", 0))
            if key == "inquiries":
                result["active_inquiry_count"] = value.get("active_inquiry_count", sum(
                    row.get("status") not in {"closed", "resolved", "abandoned", "retired"}
                    for row in items))
            result[key] = items[-limit:]
            counts[key] = {"total": total, "shown": len(result[key])}
    if counts:
        result["monitor_truncation"] = counts
    return result


def create_server(
    *,
    status: Callable[[], dict[str, Any]],
    runs: Callable[[], list[dict[str, Any]]],
    run: Callable[[str], dict[str, Any] | None],
    document: Callable[[str], dict[str, Any] | None],
    search: Callable[[str], list[dict[str, Any]]],
    set_paused: Callable[[bool], dict[str, Any]],
    host: str = "127.0.0.1",
    port: int = 8765,
) -> ThreadingHTTPServer:
    """Create a server; caller owns ``serve_forever()``, shutdown, and close.

    GET endpoints expose callback snapshots. POST /api/pause accepts exactly
    ``{"paused": bool}`` and requires the browser's same-origin Origin header.
    Callbacks may execute concurrently and must synchronize their own state.
    IPv4 loopback binding only; port=0 chooses a free port for tests/embedding.
    """
    if host == "localhost":
        host = "127.0.0.1"
    try:
        address = ipaddress.ip_address(host)
    except ValueError as exc:
        raise ValueError("monitor must bind to an IPv4 loopback address") from exc
    if address.version != 4 or not address.is_loopback:
        raise ValueError("monitor must bind to an IPv4 loopback address")
    if isinstance(port, bool) or not isinstance(port, int) or not 0 <= port <= 65535:
        raise ValueError("port must be an integer from 0 to 65535")

    class Handler(BaseHTTPRequestHandler):
        server_version = "SwarmMonitor/1"

        def log_message(self, format: str, *args: Any) -> None:
            # Corpus queries and identifiers should not enter access logs.
            pass

        def _send(self, code: int, body: bytes, content_type: str) -> None:
            self.send_response(code)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Referrer-Policy", "no-referrer")
            self.send_header("X-Frame-Options", "DENY")
            self.send_header(
                "Content-Security-Policy",
                "default-src 'self'; script-src 'self'; style-src 'self'; "
                "connect-src 'self'; img-src 'self'; object-src 'none'; "
                "base-uri 'none'; frame-ancestors 'none'; form-action 'self'",
            )
            self.end_headers()
            self.wfile.write(body)

        def _json(self, code: int, payload: Any) -> None:
            body = json.dumps(payload, allow_nan=False, ensure_ascii=False).encode("utf-8")
            self._send(code, body, "application/json; charset=utf-8")

        def _host_ok(self) -> bool:
            # Reject DNS rebinding and duplicate Host headers, including on reads.
            hosts = self.headers.get_all("Host", [])
            bound_host, bound_port = self.server.server_address[:2]
            allowed = {f"{bound_host}:{bound_port}", f"localhost:{bound_port}"}
            if bound_port == 80:
                allowed.update({bound_host, "localhost"})
            return len(hosts) == 1 and hosts[0] in allowed

        def do_GET(self) -> None:
            if not self._host_ok():
                self._json(403, {"error": "invalid local Host"})
                return
            try:
                parsed = urlsplit(self.path)
                if parsed.scheme or parsed.netloc:
                    self._json(400, {"error": "relative request target required"})
                    return
                path = parsed.path
                if path in _FILES:
                    filename, content_type = _FILES[path]
                    self._send(200, (_STATIC / filename).read_bytes(), content_type)
                    return
                query = parse_qs(parsed.query)
                if path == "/api/status":
                    value = monitor_view(status())
                elif path == "/api/runs":
                    value = [monitor_view(item, summary=True) for item in runs()[:100]]
                elif path.startswith("/api/runs/"):
                    identifier = unquote(path[len("/api/runs/"):])
                    if not identifier or len(identifier) > 512 or "/" in identifier:
                        self._json(400, {"error": "invalid run identifier"})
                        return
                    value = monitor_view(run(identifier))
                elif path == "/api/document":
                    identifier = query.get("id", [""])[0]
                    if not identifier or len(identifier) > 1024:
                        self._json(400, {"error": "document id required (maximum 1024 characters)"})
                        return
                    value = document(identifier)
                elif path == "/api/search":
                    term = query.get("q", [""])[0].strip()
                    if not term or len(term) > 512:
                        self._json(400, {"error": "search query required (maximum 512 characters)"})
                        return
                    value = search(term)
                else:
                    self._json(404, {"error": "not found"})
                    return
                self._json(404 if value is None else 200, {"error": "not found"} if value is None else value)
            except Exception:
                self._json(500, {"error": "monitor data unavailable"})

        def do_POST(self) -> None:
            if not self._host_ok():
                self._json(403, {"error": "invalid local Host"})
                return
            origins = self.headers.get_all("Origin", [])
            if origins != [f"http://{self.headers['Host']}"]:
                self._json(403, {"error": "same-origin request required"})
                return
            if self.headers.get("Sec-Fetch-Site") not in (None, "same-origin"):
                self._json(403, {"error": "same-origin request required"})
                return
            if self.path != "/api/pause":
                self._json(404, {"error": "not found"})
                return
            if self.headers.get_content_type() != "application/json":
                self._json(415, {"error": "application/json required"})
                return
            lengths = self.headers.get_all("Content-Length", [])
            try:
                if len(lengths) != 1 or self.headers.get("Transfer-Encoding"):
                    raise ValueError
                length = int(lengths[0])
                if not 0 < length <= 4096:
                    raise ValueError
                data = json.loads(self.rfile.read(length))
                if not isinstance(data, dict) or set(data) != {"paused"} or type(data["paused"]) is not bool:
                    raise ValueError
            except (ValueError, UnicodeError):
                self._json(400, {"error": "expected a JSON object with one boolean paused field"})
                return
            try:
                self._json(200, set_paused(data["paused"]))
            except Exception:
                self._json(500, {"error": "pause state unavailable"})

    server = ThreadingHTTPServer((host, port), Handler)
    server.daemon_threads = True
    return server


def serve_monitor(**kwargs: Any) -> None:
    """Create and serve until interrupted; see :func:`create_server` for options."""
    with create_server(**kwargs) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
