"""Email archive records. Evidence uses swarmkit.types.Evidence unchanged."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class EmailDocument:
    id: str
    subject: str
    sender: str
    recipients: tuple[str, ...]
    date_utc: str | None
    date_status: str
    raw_date: str
    body: str
    raw_sha256: str
    body_sha256: str
    authored_sha256: str
    raw_locator: str
    source_family: str
    message_id: str
    in_reply_to: tuple[str, ...]
    references: tuple[str, ...]
    raw_locators: tuple[str, ...] = ()
    parsing_notes: tuple[str, ...] = ()
    synthetic: bool = False
    thread_basis: str = ''

    @property
    def doc_id(self) -> str:
        """Alias for applications using doc_id rather than canonical id."""
        return self.id


@dataclass
class IngestStats:
    attempted: int = 0
    inserted: int = 0
    duplicates: int = 0
    skipped: int = 0
    bytes_read: int = 0
    errors: list[str] = field(default_factory=list)

    def record_error(self, text: str) -> None:
        self.skipped += 1
        if len(self.errors) < 50:
            self.errors.append(text)


@dataclass(frozen=True)
class EmailSegment:
    """Exact disjoint decoded-body span with explicitly claimed attribution."""

    document_id: str
    segment_id: str
    start: int
    end: int
    text: str
    kind: str
    claimed_sender: str | None
    claimed_date: str | None
    subject: str | None
    depth: int
    confidence: str
    ambiguities: tuple[str, ...]
    content_fingerprint: str
    source_family: str
