"""Persistent chronological membership view over a read-only corpus snapshot.

Arrival is a simulated observation ordered by outer UTC date and document ID,
not a claim of historical delivery time. Quoted dates never backdate admission.
The model-facing API cannot search/get unarrived documents, including timestamp
peers admitted later. This is an application boundary, not an OS sandbox.
"""
from __future__ import annotations

import json
import re
import sqlite3
import threading
from pathlib import Path

from .corpus import MAX_QUERY_CHARS, MAX_QUERY_TERMS, EmailCorpus, _cutoff, _limit


class ReplayCorpus:
    """Expose only persistently admitted records from a fixed historical window.

    ``admit_next`` returns EmailDocuments; ``admit_next_metadata`` returns metadata dictionaries without raw MIME reads.
    Admission indexes decoded bodies locally so ranking uses only arrived text. Both advance the same
    exact (date, ID) cursor atomically. Unknown/out-of-window dates are counted
    as quarantined, never silently assigned a plausible date.
    """

    def __init__(self, corpus_path, replay_db_path, *, start='1999-01-01', end='2002-12-31'):
        low = _cutoff(start + 'T00:00:00Z' if isinstance(start, str)
                      and re.fullmatch(r'\d{4}-\d{2}-\d{2}', start) else start)
        high = _cutoff(end)
        if low is None or high is None or low > high:
            raise ValueError('replay requires finite ordered UTC bounds')
        corpus_path = Path(corpus_path).resolve()
        if not corpus_path.is_file():
            raise ValueError('corpus snapshot does not exist')
        replay_path = Path(replay_db_path).resolve()
        if corpus_path == replay_path:
            raise ValueError('replay membership database must differ from corpus')
        replay_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._db = sqlite3.connect(str(replay_path), uri=True, check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._db.execute('PRAGMA journal_mode=WAL')
        self._db.execute('ATTACH DATABASE ? AS archive', (corpus_path.as_uri() + '?mode=ro',))
        self._db.executescript('''
            CREATE TABLE IF NOT EXISTS replay_meta (key TEXT PRIMARY KEY,value TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS arrived (
                doc_id TEXT PRIMARY KEY,sequence INTEGER NOT NULL UNIQUE,
                date_utc TEXT NOT NULL,source_family TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS arrived_date ON arrived(date_utc,doc_id);
            CREATE VIRTUAL TABLE IF NOT EXISTS arrived_fts USING fts5(
                doc_id UNINDEXED, subject, body, sender, recipients, tokenize='unicode61'
            );
        ''')
        config = {'corpus_path': str(corpus_path), 'start': low, 'end': high, 'ranking': 'arrived_only_fts_v1'}
        previous = self._read('config')
        if previous is not None and previous != config:
            self.close()
            raise ValueError('existing replay configuration differs; use a new replay database')
        if previous is None:
            with self._db:
                self._write('config', config)
                total = self._db.execute('SELECT count(*) FROM archive.documents').fetchone()[0]
                eligible = self._db.execute('SELECT count(*) FROM archive.documents '
                                            'WHERE date_utc BETWEEN ? AND ?', (low, high)).fetchone()[0]
                unknown = self._db.execute('SELECT count(*) FROM archive.documents '
                                           'WHERE date_utc IS NULL').fetchone()[0]
                self._write('population', {'total': total, 'eligible': eligible,
                                           'quarantined': total - eligible, 'unknown_dates': unknown})
                self._write('sequence', 0)
                self._write('cursor', None)
        self._config = config
        self._retrieval = {'search_calls': 0, 'get_calls': 0, 'raw_reads': 0}

    def _read(self, key):
        row = self._db.execute('SELECT value FROM replay_meta WHERE key=?', (key,)).fetchone()
        return json.loads(row[0]) if row else None

    def _write(self, key, value):
        self._db.execute('INSERT OR REPLACE INTO replay_meta VALUES (?,?)', (key, json.dumps(value)))

    def close(self):
        self._db.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def count(self):
        with self._lock:
            return self._read('sequence')

    def stats(self):
        with self._lock:
            sequence = self._read('sequence')
            population = self._read('population')
            return {**population, 'documents': sequence, 'arrived': sequence,
                    'remaining': population['eligible'] - sequence, 'cursor': self._read('cursor'),
                    'bounds': self._config, 'observation_basis': 'outer_header_UTC_date_then_ID',
                    'complete': sequence == population['eligible'],
                    'exhausted': sequence == population['eligible'],
                    'virtual_time': (self._read('cursor') or [None])[0],
                    'session_retrieval': dict(self._retrieval)}

    def admit_next_metadata(self, batch_size=100, *, until=None):
        """Atomically admit a bounded chronological batch, returning metadata only."""
        _limit(batch_size, 10000)
        ceiling = _cutoff(until)
        if batch_size == 0:
            return []
        with self._lock:
            self._db.execute('BEGIN IMMEDIATE')
            try:
                cursor = self._read('cursor')
                sequence = self._read('sequence')
                sql = ('SELECT id,date_utc,source_family,subject,sender,body_sha256,body,recipients '
                       'FROM archive.documents WHERE date_utc BETWEEN ? AND ?')
                params = [self._config['start'], min(self._config['end'], ceiling)
                          if ceiling is not None else self._config['end']]
                if cursor:
                    sql += ' AND (date_utc,id)>(?,?)'
                    params.extend(cursor)
                sql += ' ORDER BY date_utc,id LIMIT ?'
                rows = self._db.execute(sql, (*params, batch_size)).fetchall()
                arrivals = []
                for row in rows:
                    sequence += 1
                    self._db.execute('INSERT INTO arrived VALUES (?,?,?,?)',
                                     (row['id'], sequence, row['date_utc'], row['source_family']))
                    self._db.execute('INSERT INTO arrived_fts VALUES (?,?,?,?,?)',
                                     (row['id'], row['subject'], row['body'], row['sender'],
                                      ' '.join(json.loads(row['recipients']))))
                    arrivals.append({**{k: row[k] for k in row.keys() if k not in ('body', 'recipients')},
                                     'sequence': sequence})
                if rows:
                    self._write('sequence', sequence)
                    self._write('cursor', [rows[-1]['date_utc'], rows[-1]['id']])
                self._db.commit()
                return arrivals
            except BaseException:
                self._db.rollback()
                raise

    def admit_until(self, cutoff, *, batch_size=1000):
        """Admit at most one bounded metadata batch through cutoff; repeat until []."""
        if cutoff is None:
            raise ValueError('admit_until requires a finite cutoff')
        return self.admit_next_metadata(batch_size, until=cutoff)

    def peek_next_date(self):
        """Controller scheduling helper; reveals only the next eligible outer date."""
        with self._lock:
            cursor = self._read('cursor')
            sql = 'SELECT date_utc FROM archive.documents WHERE date_utc BETWEEN ? AND ?'
            params = [self._config['start'], self._config['end']]
            if cursor:
                sql += ' AND (date_utc,id)>(?,?)'
                params.extend(cursor)
            row = self._db.execute(sql + ' ORDER BY date_utc,id LIMIT 1', params).fetchone()
            return row[0] if row else None

    def admit_next(self, batch_size=100):
        return [self.get(row['id']) for row in self.admit_next_metadata(batch_size)]

    def get(self, doc_id):
        with self._lock:
            self._retrieval['get_calls'] += 1
            row = self._db.execute('SELECT d.* FROM archive.documents d JOIN arrived a ON a.doc_id=d.id '
                                   'WHERE d.id=?', (doc_id,)).fetchone()
            return EmailCorpus._document(self, row) if row else None

    def raw(self, doc_id):
        with self._lock:
            self._retrieval['raw_reads'] += 1
            row = self._db.execute('SELECT d.raw FROM archive.documents d JOIN arrived a ON a.doc_id=d.id '
                                   'WHERE d.id=?', (doc_id,)).fetchone()
            if row is None:
                raise KeyError(doc_id)
            return bytes(row[0])

    def search(self, query, *, limit=20, match='any', cutoff=None):
        _limit(limit)
        date = _cutoff(cutoff)
        if not isinstance(query, str) or len(query) > MAX_QUERY_CHARS:
            raise ValueError('query must be a bounded string')
        if match not in ('any', 'all'):
            raise ValueError("match must be 'any' or 'all'")
        tokens = re.findall(r'\w+', query)
        if len(tokens) > MAX_QUERY_TERMS:
            raise ValueError('query has too many terms')
        with self._lock:
            self._retrieval['search_calls'] += 1
            params = []
            if tokens:
                sql = ('SELECT d.* FROM arrived_fts f '
                       'JOIN archive.documents d ON d.id=f.doc_id JOIN arrived a ON a.doc_id=d.id '
                       'WHERE arrived_fts MATCH ?')
                params.append((' OR ' if match == 'any' else ' AND ').join('"' + t + '"' for t in tokens))
            else:
                sql = 'SELECT d.* FROM arrived a JOIN archive.documents d ON d.id=a.doc_id WHERE 1=1'
            if date:
                sql += ' AND a.date_utc<=?'
                params.append(date)
            sql += ' ORDER BY f.rank' if tokens else ' ORDER BY a.sequence DESC'
            sql += ' LIMIT ?'
            return [EmailCorpus._document(self, r) for r in
                    self._db.execute(sql, (*params, limit)).fetchall()]

    # These helpers call only this view's guarded get/raw/segments, never a master handle.
    segments = EmailCorpus.segments
    evidence = EmailCorpus.evidence
    verify_evidence = EmailCorpus.verify_evidence

    def observation(self, doc_id):
        """Arrival sequence is independent of any older inline/forwarded date."""
        with self._lock:
            row = self._db.execute('SELECT * FROM arrived WHERE doc_id=?', (doc_id,)).fetchone()
            return dict(row) if row else None
