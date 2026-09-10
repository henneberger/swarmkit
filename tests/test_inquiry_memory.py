from copy import deepcopy

import pytest

from swarmkit.enron.inquiry_memory import rank_evidence
from swarmkit.types import Evidence


def source(identifier, quote, subject, speaker='Mark Brook'):
    return Evidence(identifier, 'Model-written claim is not a ranking source.',
                    'family-' + identifier, 'private-owner', metadata={
                        'document_id': 'mail-' + identifier, 'start': 0, 'end': len(quote),
                        'quote': quote, 'outer_subject': subject, 'claimed_subject': subject,
                        'claimed_sender': speaker})


def test_old_relevant_source_beats_more_than_32_unrelated_recent_items():
    old = source('old', 'I faxed the signed OMnet Agreement this afternoon.', 'OMnet execution')
    recent = [source(str(i), f'The office picnic has {i} lunches.', 'Office picnic') for i in range(40)]
    items = [old, *recent]
    before = deepcopy(items)
    ranked = rank_evidence(iter(items), 'Was the signed OMnet agreement faxed?', limit=4)
    assert ranked[0] is old
    assert len(ranked) == 4
    assert items == before
    assert all(any(item is original for original in items) for item in ranked)


def test_shared_first_name_does_not_erase_matter_or_source_identity():
    copper = source('copper', 'Use the standard guaranty form.', 'Copper guaranty', 'Mark Finch')
    silver = source('silver', 'The swap draft needs a bank response.', 'Silver swap', 'Mark Brook')
    ranked = rank_evidence([silver, copper], 'Mark Silver swap bank', limit=1)
    assert ranked == [silver]
    assert ranked[0].metadata['document_id'] == 'mail-silver'
    assert ranked[0].metadata['claimed_sender'] == 'Mark Brook'
    assert ranked[0].source == 'family-silver'
    # A model claim matching the query cannot substitute for an exact source match.
    invented = Evidence('invented', 'Silver swap bank', 'family-other', 'private-owner',
                        metadata={'quote': 'Lunch is ready.', 'outer_subject': 'Catering'})
    assert rank_evidence([silver, invented], 'Silver swap bank', 1) == [silver]


def test_empty_or_unmatched_query_uses_stable_recent_fallback_without_expansion():
    items = [source(str(i), 'Routine update.', 'Office') for i in range(5)]
    for query in ('', 'the and was', 'unmatched-token'):
        assert rank_evidence(items, query, 2) == items[-2:][::-1]
    assert rank_evidence([], 'anything') == []
    assert rank_evidence(items, 'Office', 0) == []
    with pytest.raises(ValueError):
        rank_evidence(items, '', True)
    with pytest.raises(TypeError):
        rank_evidence(['untrusted text'], 'query')


def test_exploration_can_omit_unrelated_recent_memory_without_deleting_it():
    old = source('old', 'The turbine shipment was delayed.', 'Re: Turbine shipment')
    other = source('other', 'Picnic tickets are available.', 'Fwd: Office picnic')
    archive = [old, other]
    assert rank_evidence(archive, 'Re: Enron turbine', matching_only=True) == [old]
    assert rank_evidence(archive, 'Fwd: Enron com', matching_only=True) == []
    assert rank_evidence(archive, 'Bananas', matching_only=True) == []
    assert archive == [old, other]
