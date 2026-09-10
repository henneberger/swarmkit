"""Durable, provider-independent forum and investigation audit trail."""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


class InvestigationStore:
    def __init__(self, path: str | Path):
        self.path = str(path)
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript("""
                PRAGMA journal_mode=WAL;
                CREATE TABLE IF NOT EXISTS runs(id TEXT PRIMARY KEY, data TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY, run_id TEXT NOT NULL,
                    data TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, run_id TEXT NOT NULL,
                    data TEXT NOT NULL);
            """)

    def connect(self):
        return sqlite3.connect(self.path, timeout=30)

    def save_run(self, data: dict[str, Any]) -> None:
        with self.connect() as db:
            db.execute("INSERT OR REPLACE INTO runs VALUES (?,?)", (data['id'], json.dumps(data)))

    def event(self, run_id: str, kind: str, **fields: Any) -> None:
        with self.connect() as db:
            db.execute('INSERT INTO events(run_id,data) VALUES (?,?)',
                       (run_id, json.dumps({'kind': kind, 'created_at': now(), **fields})))

    def post(self, run_id: str, data: dict[str, Any]) -> None:
        with self.connect() as db:
            db.execute('INSERT INTO posts(run_id,data) VALUES (?,?)', (run_id, json.dumps(data)))

    def runs(self) -> list[dict[str, Any]]:
        with self.connect() as db:
            return [json.loads(row[0]) for row in db.execute('SELECT data FROM runs ORDER BY rowid DESC')]

    def monitor_runs(self) -> list[dict[str, Any]]:
        """Small dashboard summaries; canonical snapshots stay in the database."""
        with self.connect() as db:
            return [json.loads(row[0]) for row in db.execute(
                "SELECT json_remove(data, '$.state_snapshot', '$.resume_state', "
                "'$.agenda', '$.history', '$.inquiries', '$.wiki') "
                "FROM runs ORDER BY rowid DESC LIMIT 100"
            )]

    def monitor_run(self, run_id: str) -> dict[str, Any] | None:
        """Recent activity for the UI without decoding private state archives."""
        with self.connect() as db:
            row = db.execute(
                "SELECT json_remove(data, '$.state_snapshot', '$.resume_state') "
                "FROM runs WHERE id=?", (run_id,),
            ).fetchone()
            if not row:
                return None
            data = json.loads(row[0])
            data['monitor_truncation'] = {}
            for table, limit in (('posts', 200), ('events', 300)):
                # Table names are fixed literals above; user input is parameterized.
                total = db.execute(f'SELECT count(*) FROM {table} WHERE run_id=?', (run_id,)).fetchone()[0]
                rows = db.execute(
                    f'SELECT data FROM {table} WHERE run_id=? ORDER BY id DESC LIMIT ?',
                    (run_id, limit),
                ).fetchall()
                data[table] = [json.loads(r[0]) for r in reversed(rows)]
                data['monitor_truncation'][table] = {'total': total, 'shown': len(rows)}
            return data

    def run(self, run_id: str) -> dict[str, Any] | None:
        with self.connect() as db:
            row = db.execute('SELECT data FROM runs WHERE id=?', (run_id,)).fetchone()
            if not row:
                return None
            data = json.loads(row[0])
            data['posts'] = [json.loads(r[0]) for r in db.execute(
                'SELECT data FROM posts WHERE run_id=? ORDER BY id', (run_id,))]
            data['events'] = [json.loads(r[0]) for r in db.execute(
                'SELECT data FROM events WHERE run_id=? ORDER BY id', (run_id,))]
            return data
