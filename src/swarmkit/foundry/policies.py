"""Reference scientists using the canonical Agent interface and explicit private views."""

from __future__ import annotations

import itertools
import json

import numpy as np

from ..communication import EvidenceCompressor, InformationGate
from ..knowledge import EvidenceRegistry
from ..types import AgentOutput, Decision, Message, Usage
from .world import ROLES


class FoundryScientist:
    """Deterministic baseline with evidence-based design search and costly research.

    Private-incentive policy shares favorable proprietary findings only within its
    firm, but discloses warnings. This is an explicit scripted strategic choice,
    not a claim that all profit-maximizing policies behave this way.
    """

    def __init__(self, communication="targeted", incentives="shared", max_cards=12):
        if communication not in ("none", "broadcast", "request", "targeted", "gated"):
            raise ValueError("unknown communication policy")
        if incentives not in ("shared", "private"):
            raise ValueError("unknown incentive regime")
        self.communication, self.incentives = communication, incentives
        self.compressor = EvidenceCompressor(max_cards)
        self.gate = InformationGate(0.1, max_silence=3)

    def act(self, context):
        public = context.task.metadata
        version = public["version"]
        registry = EvidenceRegistry()
        for card in (*context.agent.private_evidence, *(e for m in context.messages for e in m.evidence)):
            if card.metadata.get("version") == version:
                try:
                    registry.add(card)
                except ValueError:
                    # A conflicting claim is not allowed to overwrite an existing source.
                    continue
        known = {e.id: e for e in registry.evidence}
        facts = {e.metadata["topic"]: json.loads(e.claim)["value"] for e in known.values()}
        options = public["components"]
        estimates = {}
        for recipe in itertools.product(range(options), repeat=3):
            score = sum(facts.get(f"{role}/{c}", 8) for role, c in zip(ROLES, recipe, strict=True))
            score += facts.get("interaction/" + ",".join(map(str, recipe)), 0)
            estimates[recipe] = score
        # Verified artifacts expose a design and its measured score, not hidden evidence.
        for artifact in context.artifacts:
            if artifact.metadata.get("version") == version:
                recipe = tuple(artifact.content["recipe"])
                estimates[recipe] = artifact.content["quality"]
        for result in public.get("last_results", ()):
            if result.get("version") == version:
                estimates[tuple(result["assembled_recipe"])] = result["quality"]
        recipe = max(estimates, key=lambda r: (estimates[r], tuple(-x for x in r)))
        logits = np.array(list(estimates.values()), float)
        probs = np.exp((logits - logits.max()) / 3)
        probs /= probs.sum()
        beliefs = {",".join(map(str, r)): float(p) for r, p in zip(estimates, probs, strict=True)}
        role = context.agent.id.split(".")[1]
        wanted = [f"{r}/{c}" for r, c in zip(ROLES, recipe, strict=True)] + [
            "interaction/" + ",".join(map(str, recipe))
        ]
        legal_queries = public["queries"]
        missing = [q for q in wanted if q in legal_queries and q not in facts]
        if not missing:
            missing = [q for q in legal_queries if q not in facts]
        # Different specialists rotate the exploration order to reduce duplicated tests.
        firm = int(context.agent.id.split(".")[0][4:])
        query = (
            missing[(firm + context.step) % len(missing)] if missing and context.phase != "commit" else None
        )
        messages = []
        sent = set(context.agent.memory.get("sent", ()))
        if context.phase != "commit" and self.communication != "none":
            recipients = ()
            cards = tuple(known.values())
            content = "Measurements with provenance"
            if self.communication == "request":
                requests = [m for m in context.messages if m.metadata.get("request")]
                if public["round"] == 0:
                    messages.append(
                        Message(
                            context.agent.id,
                            "Request missing design constraints",
                            metadata={"request": wanted},
                        )
                    )
                    cards = ()
                else:
                    requested = {q for m in requests for q in m.metadata["request"]}
                    cards = tuple(e for e in cards if e.metadata["topic"] in requested)
                    recipients = tuple(
                        dict.fromkeys(m.sender for m in requests if m.sender != context.agent.id)
                    )
                    if not recipients:
                        cards = ()
            elif self.communication in ("targeted", "gated"):
                cards = tuple(e for e in cards if e.id not in sent)
                recipients = tuple(
                    o["coordinator"] for o in public["orders"] if o["coordinator"] != context.agent.id
                )
            if self.incentives == "private":
                # Own observations can be strategically valuable to competitors.
                local, warnings = [], []
                for e in cards:
                    (warnings if json.loads(e.claim)["value"] < 0 else local).append(e)
                if local:
                    own_firm = context.agent.id.split(".")[0]
                    peers = tuple(
                        a for a in public["members"] if a.split(".")[0] == own_firm and a != context.agent.id
                    )
                    messages.append(Message(context.agent.id, content, peers, evidence=tuple(local)))
                cards = tuple(warnings)
            if cards:
                message = Message(
                    context.agent.id,
                    content,
                    recipients,
                    evidence=cards,
                    metadata={"beliefs": beliefs},
                    step=context.step,
                )
                if self.communication != "gated" or self.gate(message):
                    messages.append(message)
        messages = tuple(self.compressor.compress(m) if m.evidence else m for m in messages)
        # Only actually generated cards enter the novelty cache. Transport loss remains possible.
        emitted = {e.id for m in messages for e in m.evidence}
        ask = public["own_cost"] * (1.35 if self.incentives == "private" else 1.0)
        decision = Decision(
            context.agent.id,
            json.dumps(recipe),
            evidence_ids=tuple(known),
            metadata={
                "query": query,
                "bid": ask,
                "specialty": role,
                "forecast": float(
                    1 / (1 + np.exp(-(estimates[recipe] - public["orders"][firm]["threshold"])))
                ),
            },
        )
        return AgentOutput(
            messages=messages,
            decision=decision,
            memory_updates={"sent": sorted(sent | emitted)},
            usage=Usage(calls=1, tokens=0, cost=0.0),
        )
