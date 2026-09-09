"""Shared exact, attributed, paged source context for email swarm applications."""

from __future__ import annotations

import hashlib
import json
from dataclasses import replace


def stable_ref(metadata):
    identity = (metadata.get("document_id"), metadata.get("start"), metadata.get("end"))
    return "v" + hashlib.sha256(json.dumps(identity).encode()).hexdigest()[:16]


class SourceContext:
    def __init__(self, corpus):
        self.replay = corpus

    def build(self, docs, offsets=None):
        spans, views, seen = {}, [], set()
        offsets = offsets or {}
        for doc in docs:
            segments = []
            remaining_chars = 1600
            offset = offsets.get(doc.id, 0)
            if type(offset) is not int or not 0 <= offset < len(doc.body):
                continue
            next_offset = None
            for segment in self.replay.segments(doc.id):
                if segment.end <= offset or segment.kind == "header" or segment.source_family in seen:
                    continue
                seen.add(segment.source_family)
                start = max(segment.start, offset)
                text = doc.body[start : min(segment.end, start + min(700, remaining_chars))]
                end = start + len(text)
                truncated = end < segment.end
                if truncated:
                    next_offset = end if next_offset is None else min(next_offset, end)
                if len(text.strip()) < 15:
                    continue
                evidence = self.replay.evidence(doc.id, start, end, owner="source-resolver")
                scope = {
                    "document_id": doc.id,
                    "outer_subject": doc.subject,
                    "outer_sender": doc.sender,
                    "outer_date": doc.date_utc,
                    "outer_recipients": tuple(doc.recipients),
                    "claimed_subject": segment.subject,
                    "claimed_sender": segment.claimed_sender,
                    "claimed_date": segment.claimed_date,
                    "kind": segment.kind,
                    "segment_id": segment.segment_id,
                    "segment_start": segment.start,
                    "segment_end": segment.end,
                    "depth": segment.depth,
                    "attribution_confidence": segment.confidence,
                    "ambiguities": tuple(segment.ambiguities),
                }
                if evidence.metadata["quote"] != text:
                    raise ValueError("provided document text differs from canonical source span")
                evidence = replace(
                    evidence,
                    metadata={
                        **evidence.metadata,
                        **scope,
                        "excerpt_truncated": truncated,
                        "next_read": f"read: {doc.id} {end}" if truncated else None,
                    },
                )
                if not self.replay.verify_evidence(evidence):
                    raise ValueError("source membership/span verification failed")
                alias = stable_ref(evidence.metadata)
                spans[alias] = evidence
                segments.append(
                    {
                        **scope,
                        "span_id": alias,
                        "text": text,
                        "start": start,
                        "end": end,
                        "truncated": truncated,
                        "starts_mid_segment": start > segment.start,
                        "next_read": f"read: {doc.id} {end}" if truncated else None,
                        "kind": segment.kind,
                        "claimed_sender": segment.claimed_sender,
                        "claimed_date": segment.claimed_date,
                        "ambiguities": list(segment.ambiguities),
                    }
                )
                remaining_chars -= len(text)
                if len(segments) >= 4 or remaining_chars < 15:
                    if end < len(doc.body):
                        next_offset = end if next_offset is None else min(next_offset, end)
                    break
            views.append(
                {
                    "document_id": doc.id,
                    "subject": doc.subject,
                    "outer_subject": doc.subject,
                    "outer_sender": doc.sender,
                    "outer_date": doc.date_utc,
                    "in_reply_to": list(doc.in_reply_to),
                    "segments": segments,
                    "read_offset": offset,
                    "truncated": next_offset is not None,
                    "next_read": f"read: {doc.id} {next_offset}" if next_offset is not None else None,
                }
            )
        return views, spans
