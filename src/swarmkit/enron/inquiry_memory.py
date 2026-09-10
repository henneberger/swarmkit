"""Private source retrieval: lexical relevance, never synthesized memory facts.

Only caller-supplied canonical Evidence is ranked. The caller must enforce private
exposure and arrived-source validity; this helper has no corpus or peer access.
Input order is oldest to newest. Scores use exact quotes and factual source scope,
not model-written claims. This is a deterministic retrieval baseline, not learned
expertise or calibrated information gain.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from typing import Iterable

from ..types import Evidence

_STOP = frozenset('a an and are as at be been by did do does for from has have how i '
                  'in is it me of on or that the their there this to was were what '
                  'when whether which who will with you your re fw fwd cc subject '
                  'sent enron com'.split())


def _tokens(text: str) -> list[str]:
    return [term for term in re.findall(r'\w+', text.casefold()) if term not in _STOP]


def rank_evidence(evidence_iterable: Iterable[Evidence], query: str, limit: int = 16,
                  *, matching_only: bool = False) -> list[Evidence]:
    """Return original Evidence objects, relevance first with newest-first ties.

    IDF is calculated exclusively over the supplied private collection. Matching
    uses saturated term frequency with document-length normalization (BM25-style).
    Empty/noninformative queries and zero-score ties use reverse input order,
    unless matching_only is enabled to omit unrelated fallback material.
    No claim, source identity, quotation, or provenance metadata is rewritten.
    """
    if type(limit) is not int or limit < 0:
        raise ValueError('limit must be a nonnegative integer')
    if not isinstance(query, str):
        raise TypeError('query must be text')
    evidence = list(evidence_iterable)
    if any(not isinstance(item, Evidence) for item in evidence):
        raise TypeError('memory requires canonical Evidence')
    if not limit or not evidence:
        return []
    query_terms = set(_tokens(query))
    if not query_terms:
        return [] if matching_only else list(reversed(evidence))[:limit]
    documents = []
    frequency: Counter[str] = Counter()
    for item in evidence:
        fields = ('quote', 'outer_subject', 'claimed_subject', 'outer_sender', 'claimed_sender')
        text = ' '.join(value for key in fields if isinstance(value := item.metadata.get(key), str))
        counts = Counter(_tokens(text))
        documents.append(counts)
        frequency.update(counts.keys() & query_terms)
    average = sum(sum(counts.values()) for counts in documents) / len(documents) or 1.0
    ranked = []
    for index, counts in enumerate(documents):
        normalization = 1.2 * (0.25 + 0.75 * sum(counts.values()) / average)
        score = sum(
            math.log(1 + (len(documents) - frequency[term] + 0.5) / (frequency[term] + 0.5))
            * counts[term] * 2.2 / (counts[term] + normalization)
            for term in query_terms if counts[term]
        )
        if not matching_only or score > 0:
            ranked.append((score, index))
    ranked.sort(reverse=True)
    return [evidence[index] for _, index in ranked[:limit]]
