import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from swarmkit.enron.corpus import EmailCorpus
from swarmkit.enron.inquiry_model import InquiryReasoner
from swarmkit.enron.replay import ReplayCorpus
from swarmkit.types import AgentState, Message, Task, Usage


@pytest.fixture
def arrived(tmp_path):
    path = tmp_path / "corpus.sqlite"
    with EmailCorpus(path) as corpus:
        corpus.ingest_directory(Path(__file__).parent / "fixtures" / "inquiry_demo")
    with ReplayCorpus(path, tmp_path / "replay.sqlite") as view:
        view.admit_next(2)
        yield view


class Client:
    def __init__(self, output):
        self.output = output
        self.prompts = []

    async def complete(self, messages, **kwargs):
        payload = json.loads(messages[-1]["content"])
        self.prompts.append(payload)
        text = self.output(payload)
        return SimpleNamespace(text=text, finish_reason="stop", usage=Usage(calls=1, tokens=130, cost=0.01))


@pytest.mark.asyncio
async def test_open_action_has_exact_evidence_and_no_implicit_broadcast(arrived):
    def output(payload):
        ref = payload["documents"][0]["segments"][0]["span_id"]
        return json.dumps(
            {
                "update": "There is an unresolved status question.",
                "action": {
                    "kind": "open",
                    "question": "Did the correction persist?",
                    "why_matters": "The announced resolution may depend on the next refresh.",
                    "unresolved_premise": "Next refresh outcome is not available.",
                    "evidence": [ref],
                },
            }
        )

    client = Client(output)
    agent = AgentState("one", memory={"summary": "Only my local context."})
    result = await InquiryReasoner(arrived, client).act(
        agent, Task("scan", "Explore arrivals"), documents=arrived.search("correction"), arrival_sequence=2
    )
    message = result.messages[0]
    assert message.recipients == ("one",)
    assert message.metadata["action"]["kind"] == "open"
    assert all(arrived.verify_evidence(ev) for ev in message.evidence)
    assert client.prompts[0]["private_memory"] == ""  # Unscoped narrative cannot contaminate a new source.
    assert not client.prompts[0]["addressed_messages"]
    assert result.usage.cost == 0.01


@pytest.mark.asyncio
async def test_invented_reference_abstains_and_keeps_paid_usage(arrived):
    client = Client(
        lambda _: json.dumps(
            {"update": "Unsupported", "action": {"kind": "revise", "evidence": ["v-invented"]}}
        )
    )
    result = await InquiryReasoner(arrived, client).act(AgentState("one"), Task("t", "Read"))
    assert result.messages[0].metadata["reasoning_rejected"]
    assert not result.messages[0].evidence
    assert result.usage.calls == 1 and result.usage.cost == 0.01


@pytest.mark.asyncio
async def test_peer_context_is_given_only_when_host_routes_it(arrived):
    client = Client(lambda _: json.dumps({"update": "Wait for evidence.", "action": {"kind": "wait"}}))
    message = Message("two", "I saw a relevant refresh setting.", recipients=("one",))
    await InquiryReasoner(arrived, client).act(
        AgentState("one"), Task("t", "Answer request"), messages=(message,)
    )
    assert client.prompts[0]["addressed_messages"][0]["sender"] == "two"
    await InquiryReasoner(arrived, client).act(AgentState("three"), Task("u", "Explore"))
    assert client.prompts[1]["addressed_messages"] == []


@pytest.mark.asyncio
async def test_uncited_read_evidence_remains_available_for_later_peer_question(arrived):
    client = Client(lambda _: json.dumps({"update": "No current lead.", "action": {"kind": "wait"}}))
    agent = AgentState("one")
    first = await InquiryReasoner(arrived, client).act(
        agent, Task("t", "Read arrivals"), documents=arrived.search("correction")
    )
    assert not first.messages[0].evidence
    assert first.memory_updates["evidence"]
    agent.memory.update(first.memory_updates)
    await InquiryReasoner(arrived, client).act(
        agent,
        Task("u", "Answer peer"),
        messages=(Message("two", "Did anyone mark the correction resolved?", recipients=("one",)),),
    )
    assert client.prompts[1]["evidence"]
    assert all(arrived.verify_evidence(e) for e in agent.memory["evidence"].values())


@pytest.mark.asyncio
async def test_model_watch_contract_is_accepted_by_agenda(arrived):
    from swarmkit.enron.inquiries import InquiryAgenda
    from swarmkit.types import SwarmState

    state = SwarmState(agents={"one": AgentState("one")})
    agenda = InquiryAgenda(state, arrived.verify_evidence)
    opened = agenda.apply(
        "one",
        {
            "kind": "open",
            "question": "Will correction survive refresh?",
            "why_matters": "A later refresh could invalidate the reported resolution.",
            "unresolved_premise": "No refresh outcome yet.",
        },
    )
    iid = opened.metadata["inquiry_id"]
    client = Client(
        lambda _: json.dumps(
            {
                "update": "Wait for the relevant observation.",
                "action": {
                    "kind": "watch",
                    "inquiry_id": iid,
                    "terms": ["refresh", "Kestrel"],
                    "unresolved_premise": "No next-refresh observation.",
                },
            }
        )
    )
    result = await InquiryReasoner(arrived, client).act(state.agents["one"], Task("t", "Choose action"))
    action = dict(result.messages[0].metadata["action"], evidence=result.messages[0].evidence)
    agenda.apply("one", action)
    assert agenda.snapshot()["inquiries"][0]["watches"][0]["terms"] == ["refresh", "kestrel"]


@pytest.mark.asyncio
async def test_exposure_is_recorded_before_provider_failure(arrived):
    exposure = []

    class FailingClient:
        async def complete(self, messages, **kwargs):
            assert exposure and exposure[0]["document_ids"]
            raise RuntimeError("provider unavailable")

    reasoner = InquiryReasoner(arrived, FailingClient(), on_exposure=exposure.append)
    with pytest.raises(RuntimeError, match="provider unavailable"):
        await reasoner.act(
            AgentState("one"), Task("t", "Read"), documents=arrived.search("correction"), arrival_sequence=2
        )
    assert exposure[0]["agent"] == "one"
    assert exposure[0]["arrival_sequence"] == 2


@pytest.mark.asyncio
async def test_wrong_recipient_is_rejected_before_model_call(arrived):
    client = Client(lambda _: json.dumps({"update": "", "action": {"kind": "wait"}}))
    private = Message("two", "Private reply for one.", recipients=("one",))
    with pytest.raises(ValueError, match="addressed to another"):
        await InquiryReasoner(arrived, client).act(
            AgentState("three"), Task("t", "Read"), messages=(private,)
        )
    assert not client.prompts


@pytest.mark.asyncio
async def test_search_terms_and_irrelevant_nulls_normalize_without_inventing_evidence(arrived):
    from swarmkit.enron.inquiries import InquiryAgenda
    from swarmkit.types import SwarmState

    client = Client(
        lambda _: json.dumps(
            {
                "update": "Locate the earlier request.",
                "action": {
                    "kind": "search",
                    "terms": ["Quartz", "refresh"],
                    "rivals": None,
                    "inquiry_id": None,
                    "evidence": None,
                },
            }
        )
    )
    agent = AgentState("one")
    result = await InquiryReasoner(arrived, client).act(agent, Task("t", "Acquire context"))
    action = result.messages[0].metadata["action"]
    assert action["query"] == "Quartz refresh"
    assert "rivals" not in action and not result.messages[0].evidence
    agenda = InquiryAgenda(SwarmState(agents={"one": agent}), arrived.verify_evidence)
    agenda.apply("one", action)
    work = agenda.schedule()[0]
    assert work["kind"] == "search" and work["inquiry_id"] is None


@pytest.mark.asyncio
async def test_source_memory_preserves_subject_and_scopes_narrative(arrived):
    docs = arrived.search("correction")
    doc = docs[0]
    client = Client(lambda _: json.dumps({"update": "A note about this source.", "action": {"kind": "wait"}}))
    agent = AgentState(
        "one",
        memory={
            "summary": "An unrelated matter with a similar name.",
            "scoped_summaries": {"source:unrelated-document": "Unrelated guaranty claim."},
        },
    )
    first = await InquiryReasoner(arrived, client).act(agent, Task("t", "Read"), documents=[doc])
    assert client.prompts[0]["private_memory"] == ""
    agent.memory.update(first.memory_updates)
    await InquiryReasoner(arrived, client).act(agent, Task("u", "Continue"), documents=[doc])
    payload = client.prompts[1]
    assert payload["private_memory"] == "A note about this source."
    assert payload["memory_scope"] == f"source:{doc.id}"
    assert all(
        e["outer_subject"] == doc.subject and e["outer_sender"] == doc.sender for e in payload["evidence"]
    )
    await InquiryReasoner(arrived, client).act(agent, Task("v", "Explore another context"))
    assert client.prompts[2]["private_memory"] == ""
