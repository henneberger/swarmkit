"""Scalable, exactly graded communication diagnostics (original fixtures)."""

from __future__ import annotations

import hashlib
import itertools
import json

import numpy as np

from ..types import AgentOutput, Decision, Evidence, Message, Task, Usage
from .communication import CommunicationCase


def distributed_evidence(seed=0, agents=4, options=3, redundant=False, split="test"):
    """Select lowest total resource cost from independently held cost components."""
    if agents < 2 or options < 2:
        raise ValueError("at least two agents/options required")
    values = np.random.default_rng(
        np.random.SeedSequence([seed, int.from_bytes(hashlib.sha256(split.encode()).digest()[:4], "big")])
    ).integers(1, 30, (agents, options))
    names = [f"a{i}" for i in range(agents)]
    cards = [
        Evidence(f"cost:{i}", json.dumps({"costs": row.tolist()}), f"cost-source:{i}", names[i])
        for i, row in enumerate(values)
    ]
    private = {a: tuple(cards) if redundant else (cards[i],) for i, a in enumerate(names)}
    winner = str(int(np.argmin(values.sum(axis=0))))
    case_id = f"{split}:evidence:{seed}:{agents}:{options}:{redundant}"

    def evaluate(decisions):
        decision = decisions.get(names[0])
        return {"success": float(decision is not None and decision.answer == winner)}

    return CommunicationCase(
        case_id,
        Task(
            "communication-diagnostic",
            "Choose the option with lowest total cost across all agents.",
            tuple(map(str, range(options))),
            {"family": "costs", "members": names, "options": options},
        ),
        private,
        {names[0]: tuple(e.id for e in cards)},
        evaluate,
        split,
    )


def interdependent_schedule(seed=0, agents=4, slack=1, split="test"):
    """Agents must jointly reserve distinct slots satisfying private availability.

    A planted feasible matching guarantees solvability, but is not exposed. Final
    decisions are checked jointly, allowing any feasible assignment. Exponential
    reference planner is intentionally capped; the task generator itself scales.
    """
    if agents < 2 or slack < 0:
        raise ValueError("at least two agents and nonnegative slack required")
    rng = np.random.default_rng(
        np.random.SeedSequence([seed, int.from_bytes(hashlib.sha256(split.encode()).digest()[:4], "big")])
    )
    slots = agents + slack
    planted = rng.permutation(slots)[:agents]
    names = [f"a{i}" for i in range(agents)]
    availability = {
        a: sorted(set([int(planted[i])] + [j for j in range(slots) if rng.random() < 0.4]))
        for i, a in enumerate(names)
    }
    cards = [
        Evidence(f"slots:{a}", json.dumps({"agent": a, "slots": availability[a]}), f"calendar:{a}", a)
        for a in names
    ]
    case_id = f"{split}:schedule:{seed}:{agents}:{slack}"

    def evaluate(decisions):
        selected = {}
        for a in names:
            try:
                selected[a] = int(decisions[a].answer)
            except (KeyError, ValueError):
                return {"success": 0.0, "conflicts": float(agents)}
        conflicts = agents - len(set(selected.values()))
        valid = all(selected[a] in availability[a] for a in names)
        return {"success": float(valid and conflicts == 0), "conflicts": float(conflicts)}

    return CommunicationCase(
        case_id,
        Task(
            "communication-diagnostic",
            "Each agent reserves one available slot; no two may overlap.",
            tuple(map(str, range(slots))),
            {"family": "schedule", "members": names},
        ),
        {a: (cards[i],) for i, a in enumerate(names)},
        {a: tuple(e.id for e in cards) for a in names},
        evaluate,
        split,
    )


class EvidenceAgent:
    """Deterministic reference policies, not language models or paper replicas.

    none, broadcast, request, targeted, and gated. Messages relay received cards;
    novelty gating happens before generation. Targeted cost messages go to a0;
    scheduling uses broadcast because all agents must coordinate final actions.
    """

    def __init__(self, policy="broadcast"):
        if policy not in ("none", "broadcast", "request", "targeted", "gated"):
            raise ValueError("unknown reference communication strategy")
        self.policy = policy

    def act(self, context):
        known = {e.id: e for e in context.agent.private_evidence}
        for message in context.messages:
            for e in message.evidence:
                known.setdefault(e.id, e)
        cards = tuple(known.values())
        messages = []
        if context.phase != "decide" and self.policy != "none":
            recipients = (
                ("a0",) if self.policy == "targeted" and context.task.metadata["family"] == "costs" else ()
            )
            if self.policy == "request":
                if context.step == 0:
                    messages.append(
                        Message(context.agent.id, "Please disclose your evidence", metadata={"request": True})
                    )
                else:
                    recipients = tuple(
                        dict.fromkeys(m.sender for m in context.messages if m.metadata.get("request"))
                    )
                    if recipients:
                        messages.append(
                            Message(context.agent.id, "Requested evidence", recipients, evidence=cards)
                        )
            else:
                if self.policy == "gated":
                    sent = set(context.agent.memory.get("sent", ()))
                    cards = tuple(e for e in cards if e.id not in sent)
                if cards and recipients != (context.agent.id,):
                    messages.append(Message(context.agent.id, "Evidence", recipients, evidence=cards))
        decision = None
        if context.phase == "decide":
            family = context.task.metadata["family"]
            if family == "costs":
                rows = [json.loads(e.claim)["costs"] for e in known.values()]
                answer = str(int(np.argmin(np.sum(rows, axis=0))))
            else:
                calendars = {
                    json.loads(e.claim)["agent"]: json.loads(e.claim)["slots"] for e in known.values()
                }
                members = context.task.metadata["members"]
                combinations = np.prod(
                    [len(calendars.get(a, context.task.candidates)) for a in members], dtype=float
                )
                if combinations > 1_000_000:
                    raise ValueError("reference schedule planner enumeration limit exceeded")
                assignment = None
                for candidate in itertools.product(
                    *(calendars.get(a, tuple(map(int, context.task.candidates))) for a in members)
                ):
                    if len(set(candidate)) == len(candidate):
                        assignment = dict(zip(members, candidate, strict=True))
                        break
                answer = str(assignment[context.agent.id]) if assignment else "-1"
            decision = Decision(context.agent.id, answer, evidence_ids=tuple(known))
        return AgentOutput(
            tuple(messages),
            decision,
            usage=Usage(calls=1, tokens=0, cost=0.0),
            memory_updates={"sent": list(known)},
        )
