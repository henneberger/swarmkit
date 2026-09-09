"""Equivalent envelopes normalize; ambiguity never silently becomes a chosen action."""

import json

import pytest

from swarmkit.enron.inquiry_response import parse_response


@pytest.mark.parametrize("response", [
    {"update": "Read the next span.", "action": {"kind": "read", "document_id": "d1", "offset": 700}},
    {"update": "Read the next span.", "actions": [{"kind": "read", "document_id": "d1", "offset": 700}]},
    {"update": "Read the next span.", "kind": "read", "document_id": "d1", "offset": 700},
])
def test_equivalent_action_envelopes_preserve_parameters(response):
    update, action = parse_response(json.dumps(response), "stop")
    assert update == "Read the next span."
    assert action == {"kind": "read", "document_id": "d1", "offset": 700, "evidence": []}


@pytest.mark.parametrize("fence", ["json", "JSON", ""])
def test_whole_json_fence_and_explicit_update_forms(fence):
    payload = {"update": ["First observation.", "A second line."], "action": {"kind": "wait"}}
    update, action = parse_response(f"  ```{fence}\n{json.dumps(payload)}\n```  ", "stop")
    assert update == "First observation.\nA second line."
    assert action == {"kind": "wait", "evidence": []}
    assert parse_response('{"update":{"text":"Literal ``` inside update"},"kind":"wait"}', "stop")[0] == "Literal ``` inside update"


def test_null_optional_fields_and_missing_update_are_neutral():
    update, action = parse_response(json.dumps({
        "update": None, "unused": None, "action": {"kind": "search", "query": None,
                                                    "terms": ["all:", "meter", "refresh"],
                                                    "inquiry_id": None, "evidence": None},
    }), "stop")
    assert update == "Requested search."
    assert action == {"kind": "search", "query": "all: meter refresh", "evidence": []}


def test_equivalent_evidence_aliases_preserve_exact_order_and_ids():
    update, action = parse_response(json.dumps({"update": {"text": "Source comparison"}, "action": {
        "kind": "revise", "inquiry_id": "q1", "evidence": [{"span_id": "v1"}, "v2", "v1"],
        "evidence_ids": ["v1", {"span_id": "v2"}, "v1"],
    }}), "stop")
    assert update == "Source comparison"
    assert action["evidence"] == ["v1", "v2", "v1"]
    assert "evidence_ids" not in action
    assert action["inquiry_id"] == "q1"
    assert parse_response('{"kind":"wait","evidence_ids":[" untrimmed "]}', "stop")[1]["evidence"] == [" untrimmed "]


@pytest.mark.parametrize("response,category", [
    ({"actions": [{"kind": "wait"}, {"kind": "read"}]}, "action_count"),
    ({"actions": []}, "action_count"),
    ({"action": {"kind": "wait"}, "kind": "wait"}, "ambiguous_action_shape"),
    ({"action": {"kind": "wait"}, "actions": [{"kind": "wait"}]}, "ambiguous_action_shape"),
    ({"action": {"kind": "wait"}, "second_action": {"kind": "read"}}, "unknown_response_field"),
    ({"action": [{"kind": "wait"}]}, "invalid_action_shape"),
    ({"actions": [None]}, "invalid_action_shape"),
    ({"kind": "wait", "action": {"kind": "read"}}, "ambiguous_action_shape"),
    ({"action": {"kind": "wait", "actions": [{"kind": "read"}]}}, "nested_action_shape"),
    ({"kind": "shell"}, "unknown_action"),
    ({"kind": ["wait"]}, "unknown_action"),
    ({"update": "I did something"}, "missing_action"),
    ([{"kind": "wait"}], "invalid_response_shape"),
    ({"kind": "wait", "update": ["one", 2]}, "invalid_update_shape"),
    ({"kind": "wait", "update": {"text": "one", "claim": "two"}}, "invalid_update_shape"),
    ({"kind": "wait", "update": False}, "invalid_update_shape"),
    ({"kind": "read", "evidence": "v1"}, "invalid_evidence_shape"),
    ({"kind": "read", "evidence": [None]}, "invalid_evidence_reference"),
    ({"kind": "read", "evidence": [""]}, "invalid_evidence_reference"),
    ({"kind": "read", "evidence": [{"span_id": "v1", "quote": "invented"}]}, "ambiguous_evidence_reference"),
    ({"kind": "read", "evidence": [{"id": "v1"}]}, "ambiguous_evidence_reference"),
    ({"kind": "read", "evidence": ["v1"], "evidence_ids": ["v2"]}, "conflicting_evidence_aliases"),
    ({"kind": "read", "evidence": ["v1", "v2"], "evidence_ids": ["v2", "v1"]}, "conflicting_evidence_aliases"),
    ({"kind": "search", "terms": ["a", 2]}, "invalid_search_terms"),
    ({"kind": "search", "terms": []}, "invalid_search_terms"),
    ({"kind": "search", "terms": ["a"], "query": "b"}, "ambiguous_search_query"),
])
def test_ambiguous_or_unknown_forms_fail_with_bounded_categories(response, category):
    with pytest.raises(ValueError, match=f"^{category}$"):
        parse_response(json.dumps(response), "stop")


@pytest.mark.parametrize("text,category", [
    ('{"kind":"wait"', "invalid_json"),
    ('Some prose {"kind":"wait"}', "invalid_json"),
    ('{"kind":"wait"} trailing prose', "invalid_json"),
    ('{"kind":"wait"}{"kind":"read"}', "invalid_json"),
    ('```json\n{"kind":"wait"}\n```\nextra', "invalid_json_fence"),
    ('```python\n{"kind":"wait"}\n```', "invalid_json_fence"),
    ('{"kind":"wait","kind":"read"}', "duplicate_json_key"),
    ('{"kind":"read","offset":NaN}', "nonfinite_json_number"),
    ('{"kind":"read","offset":1e999}', "nonfinite_json_number"),
    ('', "invalid_response_text"),
    (' ' * 1_000_001 + '{}', "response_too_large"),
])
def test_adversarial_json_is_not_extracted_or_repaired(text, category):
    with pytest.raises(ValueError, match=f"^{category}$"):
        parse_response(text, "stop")


@pytest.mark.parametrize("finish_reason", ["length", "max_tokens", "tool_calls", None, "unknown"])
def test_nonstop_finish_rejects_even_valid_complete_json(finish_reason):
    with pytest.raises(ValueError, match="^incomplete_response$"):
        parse_response('{"kind":"wait"}', finish_reason)


def test_search_query_equivalence_and_content_are_not_invented():
    text = json.dumps({"kind": "search", "terms": ["a", "b"], "query": "a b", "update": ""})
    update, action = parse_response(text, "stop")
    assert update == ""
    assert action == {"kind": "search", "query": "a b", "evidence": []}
    # Parameters remain for the host to validate; parsing does not approve a read.
    assert parse_response('{"kind":"read","offset":-1}', "stop")[1]["offset"] == -1
