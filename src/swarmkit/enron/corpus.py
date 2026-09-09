"""Read-only-source MIME ingestion, immutable raw snapshots and bounded literal FTS search.

No email, HTML, attachment or archive member is executed. Archives are streamed
without extraction; links and unsafe paths are skipped. Quote offsets reference
Python characters in the stored decoded body, never byte offsets in MIME source.
Authored-content families are conservative deduplication hints, not proof of
shared authorship or independently corroborated events. All facts remain claims
attributed to documents; this module does not detect or label fraud.
"""
from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import tarfile
import threading
from dataclasses import replace
from datetime import datetime, timedelta, timezone
from email import policy
from email.message import Message as MIMEMessage
from email.parser import BytesParser
from email.utils import getaddresses, parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath

from ..types import Evidence
from .schemas import EmailDocument, IngestStats

EXTRACTION_VERSION = 'decoded-body-v1'
MAX_QUERY_CHARS = 2048
MAX_QUERY_TERMS = 32
MAX_RESULTS = 200


def _sha(value: bytes | str) -> str:
    return hashlib.sha256(value.encode('utf-8') if isinstance(value, str) else value).hexdigest()


def _limit(value: int, maximum: int = MAX_RESULTS) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= maximum:
        raise ValueError(f'limit must be an integer in [0, {maximum}]')
    return value


def _ingest_limit(value: int | None) -> None:
    if value is not None and (isinstance(value, bool) or not isinstance(value, int) or value < 0):
        raise ValueError('ingest limit must be a nonnegative integer or None')


def _cutoff(value: str | datetime | None) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
            value = datetime.fromisoformat(value).replace(hour=23, minute=59, second=59,
                                                         tzinfo=timezone.utc)
        else:
            value = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if not isinstance(value, datetime) or value.tzinfo is None or value.utcoffset() is None:
        raise ValueError('cutoff requires an ISO date or timezone-aware datetime')
    return value.astimezone(timezone.utc).isoformat(timespec='seconds')


def _date(header: str) -> tuple[str | None, str]:
    if not header:
        return None, 'missing'
    try:
        date = parsedate_to_datetime(header)
        if date.tzinfo is None or date.utcoffset() is None:
            return None, 'timezone_ambiguous'
        return date.astimezone(timezone.utc).isoformat(timespec='seconds'), 'explicit_timezone'
    except (TypeError, ValueError, OverflowError):
        return None, 'invalid'


class _HTMLText(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
        elif not self.hidden and tag in ('p', 'div', 'br', 'li', 'tr', 'h1', 'h2'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)
        elif not self.hidden and tag in ('p', 'div', 'li', 'tr'):
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def _decode(part: MIMEMessage, notes: list[str]) -> str:
    payload = part.get_payload(decode=True)
    if payload is None:
        payload = str(part.get_payload()).encode('utf-8', errors='replace')
    charset = part.get_content_charset() or 'utf-8'
    try:
        text = payload.decode(charset, errors='strict')
    except (LookupError, UnicodeDecodeError):
        notes.append('charset decoding used UTF-8 replacement fallback')
        text = payload.decode('utf-8', errors='replace')
    return text.replace('\r\n', '\n').replace('\r', '\n')


def _body(message: MIMEMessage, notes: list[str]) -> str:
    if message.get_content_disposition() == 'attachment' or message.get_filename():
        return ''
    if message.get_content_type() == 'message/rfc822':
        notes.append('attached RFC822 message excluded from body')
        return ''
    if message.is_multipart():
        children = list(message.iter_parts())
        if message.get_content_subtype() == 'alternative':
            plain = [part for part in children if part.get_content_type() == 'text/plain']
            return _body(plain[0] if plain else children[-1], notes) if children else ''
        return '\n'.join(text for part in children if (text := _body(part, notes)))
    kind = message.get_content_type()
    if kind == 'text/plain':
        return _decode(message, notes)
    if kind == 'text/html':
        parser = _HTMLText()
        parser.feed(_decode(message, notes))
        notes.append('HTML converted to inert visible text')
        return ''.join(parser.parts)
    return ''


def _message_ids(value: str) -> tuple[str, ...]:
    return tuple(dict.fromkeys(re.findall(r'<[^<>\s]{1,500}>', value)[:1000]))


def _subject(value: str) -> str:
    return re.sub(r'^(?:(?:re|fw|fwd)\s*:\s*)+', '', value.strip(), flags=re.I).casefold()


def _authored(body: str) -> str:
    """Conservative heuristic; original quoted text is retained in full body."""
    lines = []
    for line in body.splitlines():
        if re.match(r'^\s*(?:-{2,}\s*(?:original|forwarded) message|begin forwarded message:)', line, re.I):
            break
        if re.match(r'^\s*on .{1,500}wrote:\s*$', line, re.I):
            break
        if line.lstrip().startswith('>'):
            continue
        if line.strip() == '--':
            break
        lines.append(line)
    return ' '.join('\n'.join(lines).split())


class EmailCorpus:
    """SQLite FTS5 archive with raw snapshots, provenance and bounded retrieval.

    Search treats input as literal tokens, not an FTS program. Default match="any"
    connects tokens with OR for lead discovery; match="all" requires every token.
    Date-only cutoffs include that UTC day; timestamp cutoffs require a timezone.
    Unknown/ambiguous dates are excluded whenever a cutoff is specified.
    ``limit`` on ingestion counts attempted regular files, including duplicates.
    """

    def __init__(self, db_path: str | Path, *, max_message_bytes: int = 16 * 1024 * 1024) -> None:
        if not isinstance(max_message_bytes, int) or max_message_bytes < 1:
            raise ValueError('max_message_bytes must be positive')
        self.db_path = str(db_path)
        self.max_message_bytes = max_message_bytes
        if self.db_path != ':memory:':
            Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._db = sqlite3.connect(self.db_path, check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._db.execute('PRAGMA journal_mode=WAL')
        self._db.execute('PRAGMA foreign_keys=ON')
        self._db.executescript('''
            CREATE TABLE IF NOT EXISTS documents (
                id TEXT PRIMARY KEY, raw_sha256 TEXT NOT NULL UNIQUE, raw BLOB NOT NULL,
                subject TEXT NOT NULL, normalized_subject TEXT NOT NULL, sender TEXT NOT NULL,
                recipients TEXT NOT NULL, date_utc TEXT, date_status TEXT NOT NULL, raw_date TEXT NOT NULL,
                body TEXT NOT NULL, body_sha256 TEXT NOT NULL, authored_sha256 TEXT NOT NULL,
                source_family TEXT NOT NULL, raw_locator TEXT NOT NULL, message_id TEXT NOT NULL,
                in_reply_to TEXT NOT NULL, refs TEXT NOT NULL, parsing_notes TEXT NOT NULL,
                synthetic INTEGER NOT NULL, extraction_version TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS locators (
                doc_id TEXT NOT NULL REFERENCES documents(id), locator TEXT NOT NULL,
                PRIMARY KEY(doc_id, locator)
            );
            CREATE TABLE IF NOT EXISTS thread_links (
                doc_id TEXT NOT NULL REFERENCES documents(id), message_key TEXT NOT NULL,
                PRIMARY KEY(doc_id, message_key)
            );
            CREATE INDEX IF NOT EXISTS document_date ON documents(date_utc);
            CREATE INDEX IF NOT EXISTS document_subject ON documents(normalized_subject);
            CREATE INDEX IF NOT EXISTS document_family ON documents(source_family);
            CREATE INDEX IF NOT EXISTS thread_key ON thread_links(message_key);
            CREATE VIRTUAL TABLE IF NOT EXISTS document_fts USING fts5(
                doc_id UNINDEXED, subject, body, sender, recipients, tokenize='unicode61'
            );
        ''')
        self._db.commit()

    def __enter__(self) -> EmailCorpus:
        return self

    def __exit__(self, *args) -> None:
        self.close()

    def close(self) -> None:
        with self._lock:
            self._db.close()

    def count(self) -> int:
        with self._lock:
            return self._db.execute('SELECT count(*) FROM documents').fetchone()[0]

    def _commit(self) -> None:
        with self._lock:
            self._db.commit()

    def stats(self) -> dict:
        """Status metadata for the indexed snapshot, including raw-byte footprint."""
        with self._lock:
            row = self._db.execute(
                'SELECT count(*) AS documents, coalesce(sum(length(raw)),0) AS raw_bytes, '
                'count(DISTINCT source_family) AS source_families, '
                'coalesce(sum(synthetic),0) AS synthetic_documents, '
                'coalesce(sum(date_utc IS NULL),0) AS ambiguous_dates FROM documents').fetchone()
            result = dict(row)
            result['raw_copies'] = self._db.execute('SELECT count(*) FROM locators').fetchone()[0]
            result['extraction_version'] = EXTRACTION_VERSION
            result['database'] = self.db_path
            return result

    def ingest_directory(self, path: str | Path, *, limit: int | None = None) -> IngestStats:
        _ingest_limit(limit)
        root = Path(path).resolve()
        if not root.is_dir():
            raise ValueError('source directory does not exist')
        stats = IngestStats()
        for file in sorted(root.rglob('*')):
            if limit is not None and stats.attempted >= limit:
                break
            if file.is_symlink():
                stats.record_error('skipped symbolic link')
                continue
            if not file.is_file():
                continue
            stats.attempted += 1
            try:
                if file.stat().st_size > self.max_message_bytes:
                    stats.record_error('message exceeds byte limit')
                    continue
                with file.open('rb') as handle:
                    raw = handle.read(self.max_message_bytes + 1)
                self._ingest(raw, file.as_uri(), stats)
            except (OSError, ValueError, TypeError) as exc:
                stats.record_error(f'directory ingest: {type(exc).__name__}')
            if stats.attempted % 250 == 0:
                self._commit()
        self._commit()
        return stats

    def ingest_tar(self, path: str | Path, *, limit: int | None = None) -> IngestStats:
        _ingest_limit(limit)
        archive = Path(path).resolve()
        stats = IngestStats()
        with tarfile.open(archive, mode='r|*') as stream:
            for member in stream:
                if limit is not None and stats.attempted >= limit:
                    break
                if member.isdir():
                    continue
                parts = PurePosixPath(member.name).parts
                if (not member.isfile() or member.name.startswith('/') or '\\' in member.name
                        or '..' in parts or not parts or re.match(r'^[A-Za-z]:', member.name)):
                    stats.record_error('unsafe archive member skipped')
                    continue
                stats.attempted += 1
                if member.size > self.max_message_bytes:
                    stats.record_error('archive message exceeds byte limit')
                    continue
                handle = stream.extractfile(member)  # Reads member bytes; does not extract to disk.
                if handle is None:
                    stats.record_error('unreadable archive member')
                    continue
                try:
                    with handle:
                        self._ingest(handle.read(self.max_message_bytes + 1),
                                     f'{archive.as_uri()}!/{member.name}', stats)
                except (ValueError, TypeError) as exc:
                    stats.record_error(f'archive ingest: {type(exc).__name__}')
                if stats.attempted % 250 == 0:
                    self._commit()
        self._commit()
        return stats

    def _ingest(self, raw: bytes, locator: str, stats: IngestStats) -> None:
        stats.bytes_read += len(raw)
        if len(raw) > self.max_message_bytes:
            stats.record_error('message exceeds byte limit')
            return
        raw_hash = _sha(raw)
        doc_id = f'mail-{raw_hash}'
        with self._lock:
            if self._db.execute('SELECT 1 FROM documents WHERE id=?', (doc_id,)).fetchone():
                self._db.execute('INSERT OR IGNORE INTO locators VALUES (?,?)', (doc_id, locator))
                stats.duplicates += 1
                return
        message = BytesParser(policy=policy.default).parsebytes(raw)
        # Enron mail has headers even when files have no extension. Reject arbitrary text/binary files.
        if not any(message.get(name) for name in ('From', 'To', 'Subject', 'Message-ID', 'Date')):
            stats.record_error('no recognizable email headers')
            return
        notes = [type(defect).__name__ for defect in message.defects]
        body = _body(message, notes)
        sender_pairs = getaddresses([str(message.get('From', ''))])
        sender = sender_pairs[0][1].casefold() if sender_pairs else ''
        recipients = tuple(dict.fromkeys(address.casefold() for _, address in getaddresses(
            [str(message.get(name, '')) for name in ('To', 'Cc', 'Bcc')]) if address))
        subject = str(message.get('Subject', ''))
        raw_date = str(message.get('Date', ''))
        date_utc, date_status = _date(raw_date)
        authored = _authored(body)
        authored_hash = _sha(sender + '\0' + authored)
        # Tiny repeated signatures/acknowledgments do not justify a content-family merge.
        family = (f'enron-authored:{authored_hash}' if len(authored) >= 80 and len(authored.split()) >= 10
                  else f'enron-raw:{raw_hash}')
        message_ids = _message_ids(str(message.get('Message-ID', '')))
        message_id = message_ids[0] if message_ids else ''
        in_reply_to = _message_ids(str(message.get('In-Reply-To', '')))
        refs = _message_ids(str(message.get('References', '')))
        synthetic = str(message.get('X-Synthetic-Fixture', '')).strip().casefold() == 'true'
        values = (doc_id, raw_hash, raw, subject, _subject(subject), sender, json.dumps(recipients),
                  date_utc, date_status, raw_date, body, _sha(body), authored_hash, family, locator,
                  message_id, json.dumps(in_reply_to), json.dumps(refs), json.dumps(notes), int(synthetic),
                  EXTRACTION_VERSION)
        with self._lock:
            # Another ingestion thread may have inserted identical bytes while parsing.
            inserted = self._db.execute('INSERT OR IGNORE INTO documents VALUES (' + ','.join('?' * 21)
                                        + ')', values).rowcount
            self._db.execute('INSERT OR IGNORE INTO locators VALUES (?,?)', (doc_id, locator))
            if inserted:
                self._db.execute('INSERT INTO document_fts VALUES (?,?,?,?,?)',
                                 (doc_id, subject, body, sender, ' '.join(recipients)))
                self._db.executemany('INSERT OR IGNORE INTO thread_links VALUES (?,?)',
                                     [(doc_id, key) for key in dict.fromkeys((message_id, *in_reply_to, *refs))
                                      if key])
        stats.inserted += int(bool(inserted))
        stats.duplicates += int(not inserted)

    def _document(self, row: sqlite3.Row) -> EmailDocument:
        locators = tuple(record[0] for record in self._db.execute(
            'SELECT locator FROM locators WHERE doc_id=? ORDER BY locator', (row['id'],)))
        return EmailDocument(
            id=row['id'], subject=row['subject'], sender=row['sender'],
            recipients=tuple(json.loads(row['recipients'])), date_utc=row['date_utc'],
            date_status=row['date_status'], raw_date=row['raw_date'], body=row['body'],
            raw_sha256=row['raw_sha256'], body_sha256=row['body_sha256'],
            authored_sha256=row['authored_sha256'], raw_locator=row['raw_locator'],
            source_family=row['source_family'], message_id=row['message_id'],
            in_reply_to=tuple(json.loads(row['in_reply_to'])), references=tuple(json.loads(row['refs'])),
            raw_locators=locators, parsing_notes=tuple(json.loads(row['parsing_notes'])),
            synthetic=bool(row['synthetic']))

    def get(self, doc_id: str) -> EmailDocument | None:
        with self._lock:
            row = self._db.execute('SELECT * FROM documents WHERE id=?', (doc_id,)).fetchone()
            return self._document(row) if row else None

    def raw(self, doc_id: str) -> bytes:
        with self._lock:
            row = self._db.execute('SELECT raw FROM documents WHERE id=?', (doc_id,)).fetchone()
            if row is None:
                raise KeyError(doc_id)
            return bytes(row[0])

    def segments(self, doc_id: str):
        """Disjoint exact chain spans; inline authors/dates are unverified claims."""
        from .segments import parse_segments

        document = self.get(doc_id)
        if document is None:
            raise KeyError(doc_id)
        return parse_segments(document)

    def search(self, query: str, *, limit: int = 20, match: str = 'any',
               cutoff: str | datetime | None = None) -> list[EmailDocument]:
        _limit(limit)
        date = _cutoff(cutoff)
        if not isinstance(query, str) or len(query) > MAX_QUERY_CHARS:
            raise ValueError('query must be a string of at most 2048 characters')
        if match not in ('any', 'all'):
            raise ValueError("match must be 'any' or 'all'")
        tokens = re.findall(r'\w+', query, flags=re.UNICODE)
        if len(tokens) > MAX_QUERY_TERMS:
            raise ValueError('query has too many terms')
        with self._lock:
            params: list[object] = []
            if tokens:
                connector = ' OR ' if match == 'any' else ' AND '
                expression = connector.join('"' + token + '"' for token in tokens)
                sql = ('SELECT d.* FROM document_fts f JOIN documents d ON d.id=f.doc_id '
                       'WHERE document_fts MATCH ?')
                params.append(expression)
            else:
                sql = 'SELECT d.* FROM documents d WHERE 1=1'
            if date:
                sql += ' AND d.date_utc IS NOT NULL AND d.date_utc<=?'
                params.append(date)
            # FTS5's hidden rank column defaults to BM25 and streams ranked hits.
            # Adding a secondary document-ID sort defeats this optimization.
            # Keep date filtering above LIMIT: future hits must not consume slots.
            # Equal-score ordering is intentionally unspecified.
            sql += (' ORDER BY f.rank' if tokens else
                    ' ORDER BY d.date_utc DESC, d.id')
            sql += ' LIMIT ?'
            params.append(limit)
            return [self._document(row) for row in self._db.execute(sql, params).fetchall()]

    def thread(self, doc_id: str, *, limit: int = 50,
               cutoff: str | datetime | None = None) -> list[EmailDocument]:
        """Header-linked component; subject/date fallback only if no linked peers.

        Fallback is explicitly labeled subject_time_heuristic, never a claim of
        proven conversation membership. Expansion is bounded at the requested limit.
        """
        _limit(limit)
        date = _cutoff(cutoff)
        with self._lock:
            origin = self.get(doc_id)
            if origin is None or limit == 0:
                return []
            if date and (origin.date_utc is None or origin.date_utc > date):
                return []
            found = {doc_id: origin}
            frontier = [doc_id]
            while frontier and len(found) < limit:
                current = frontier.pop(0)
                sql = ('SELECT DISTINCT d.* FROM documents d JOIN thread_links t ON d.id=t.doc_id '
                       'WHERE t.message_key IN (SELECT message_key FROM thread_links WHERE doc_id=?)')
                params: list[object] = [current]
                if date:
                    sql += ' AND d.date_utc IS NOT NULL AND d.date_utc<=?'
                    params.append(date)
                sql += ' ORDER BY d.date_utc, d.id LIMIT ?'
                params.append(MAX_RESULTS)
                for row in self._db.execute(sql, params).fetchall():
                    if row['id'] not in found:
                        found[row['id']] = self._document(row)
                        frontier.append(row['id'])
                        if len(found) >= limit:
                            break
            basis = 'header_links'
            if len(found) == 1 and origin.subject and origin.date_utc:
                moment = datetime.fromisoformat(origin.date_utc)
                low = (moment - timedelta(days=30)).isoformat(timespec='seconds')
                high = (moment + timedelta(days=30)).isoformat(timespec='seconds')
                if date:
                    high = min(date, high)
                rows = self._db.execute('SELECT * FROM documents WHERE normalized_subject=? '
                                        'AND date_utc BETWEEN ? AND ? ORDER BY date_utc,id LIMIT ?',
                                        (_subject(origin.subject), low, high, limit)).fetchall()
                found = {row['id']: self._document(row) for row in rows}
                basis = 'subject_time_heuristic'
            return [replace(doc, thread_basis=basis) for doc in
                    sorted(found.values(), key=lambda d: (d.date_utc or '', d.id))[:limit]]

    def around(self, doc_id: str, *, window_days: int = 7, limit: int = 50,
               cutoff: str | datetime | None = None) -> list[EmailDocument]:
        """Chronological neighbors, not necessarily related conversation members."""
        _limit(limit)
        if not isinstance(window_days, int) or not 0 <= window_days <= 3650:
            raise ValueError('window_days must be in [0,3650]')
        date = _cutoff(cutoff)
        with self._lock:
            origin = self.get(doc_id)
            if origin is None or origin.date_utc is None or limit == 0:
                return []
            moment = datetime.fromisoformat(origin.date_utc)
            low = (moment - timedelta(days=window_days)).isoformat(timespec='seconds')
            high = (moment + timedelta(days=window_days)).isoformat(timespec='seconds')
            if date:
                if origin.date_utc > date:
                    return []
                high = min(date, high)
            rows = self._db.execute('SELECT * FROM documents WHERE date_utc BETWEEN ? AND ? '
                                    'ORDER BY abs(julianday(date_utc)-julianday(?)),id LIMIT ?',
                                    (low, high, origin.date_utc, limit)).fetchall()
            return [self._document(row) for row in rows]

    def evidence(self, doc_id: str, start: int, end: int, *, claim: str | None = None,
                 owner: str = 'corpus', supports: tuple[str, ...] = (),
                 contradicts: tuple[str, ...] = ()) -> Evidence:
        document = self.get(doc_id)
        if document is None:
            raise KeyError(doc_id)
        if (isinstance(start, bool) or isinstance(end, bool) or not isinstance(start, int)
                or not isinstance(end, int) or not 0 <= start < end <= len(document.body)):
            raise ValueError('quote offsets must select a nonempty exact body span')
        quote = document.body[start:end]
        span_id = f'{doc_id}:{start}:{end}'
        interpretation_id = _sha(json.dumps([owner, claim, supports, contradicts]))[:16]
        segments = [segment for segment in self.segments(doc_id)
                    if segment.start <= start and end <= segment.end]
        attribution = ({'segment_id': segments[0].segment_id, 'segment_kind': segments[0].kind,
                        'claimed_sender': segments[0].claimed_sender,
                        'claimed_date': segments[0].claimed_date,
                        'segment_source_family': segments[0].source_family,
                        'segment_fingerprint': segments[0].content_fingerprint,
                        'attribution_status': 'unverified_header_claim'} if len(segments) == 1 else
                       {'attribution_status': 'crosses_segments; do not assign one speaker'})
        return Evidence(f'{span_id}:{interpretation_id}', quote if claim is None else claim,
                        document.source_family, owner, supports=supports, contradicts=contradicts,
                        metadata={**attribution, 'document_id': doc_id, 'span_id': span_id, 'start': start, 'end': end, 'quote': quote,
                                  'quote_fingerprint': _sha(' '.join(quote.split())),
                                  'independence_status': 'not_established',
                                  'raw_sha256': document.raw_sha256, 'body_sha256': document.body_sha256,
                                  'offset_basis': EXTRACTION_VERSION, 'raw_locator': document.raw_locator,
                                  'source_family': document.source_family, 'synthetic': document.synthetic,
                                  'claim_status': 'attributed_statement' if claim is None else 'interpretation'})

    def verify_evidence(self, evidence: Evidence) -> bool:
        """Verify locator/hash/span integrity, not the truth of an interpretation."""
        meta = evidence.metadata
        try:
            document = self.get(meta['document_id'])
            if document is None:
                return False
            start, end = meta['start'], meta['end']
            if (isinstance(start, bool) or isinstance(end, bool) or not isinstance(start, int)
                    or not isinstance(end, int) or not 0 <= start < end <= len(document.body)):
                return False
            return (evidence.source == document.source_family
                    and meta.get('source_family') == document.source_family
                    and meta.get('offset_basis') == EXTRACTION_VERSION
                    and meta.get('raw_sha256') == document.raw_sha256 == _sha(self.raw(document.id))
                    and meta.get('body_sha256') == document.body_sha256 == _sha(document.body)
                    and meta.get('raw_locator') in document.raw_locators
                    and document.body[start:end] == meta['quote'])
        except (KeyError, TypeError, ValueError):
            return False
