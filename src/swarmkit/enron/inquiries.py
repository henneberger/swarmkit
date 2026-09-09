"""Budgeted, agent-directed inquiry agenda, independent of model/provider calls.

AgentNet-inspired addressed capability routing (https://arxiv.org/abs/2504.00587),
not a reproduction or a learned discovery policy. Agents propose questions and
next tests; this controller enforces provenance, queues, and fair dispatch. Source
validation authenticates supplied spans, not their semantic interpretation.

Artifacts/data are committed locally; returned messages must be routed by the
caller. No inbox, runtime clock, router success, or API ledger is changed. Persist
with swarmkit.serialization.save/load; reattach the trusted evidence validator.
"""

from __future__ import annotations

import re
from copy import deepcopy
from dataclasses import dataclass
from typing import Callable

from ..topology import CapabilitySuccessRouter
from ..types import AlgorithmResult, Artifact, Evidence, Message, MessageKind, SwarmState


@dataclass(frozen=True)
class AgendaConfig:
    max_actions: int = 64
    max_actions_per_inquiry: int = 12
    max_pending: int = 64
    exploration_every: int = 5

    def __post_init__(self):
        if any(type(v) is not int or v < 1 for v in vars(self).values()):
            raise ValueError("agenda limits must be positive integers")


class InquiryAgenda:
    KEY = "inquiry_agenda_v1"

    def __init__(
        self,
        state: SwarmState,
        validate_evidence: Callable[[Evidence], bool],
        config: AgendaConfig | None = None,
        router: CapabilitySuccessRouter | None = None,
        evidence_available: Callable[[str, Evidence], bool] | None = None,
    ):
        self.state, self.validate_evidence = state, validate_evidence
        self.evidence_available = evidence_available
        saved = state.data.get(self.KEY)
        self.config = config or (AgendaConfig(**saved["config"]) if saved else AgendaConfig())
        if saved and saved["config"] != vars(self.config):
            raise ValueError("resume must preserve agenda limits")
        self.router = router or CapabilitySuccessRouter(exploration=0)
        state.data.setdefault(
            self.KEY,
            dict(
                config=vars(self.config).copy(),
                inquiries={},
                history=[],
                pending=[],
                running=[],
                actions_used=0,
                per_inquiry={},
                sequence=0,
                dispatch_sequence=0,
                last_dispatched={},
                watch_seen={},
                arrivals_seen=[],
            ),
        )

    @property
    def data(self):
        return self.state.data[self.KEY]

    def _agent(self, agent_id):
        if agent_id not in self.state.agents or not self.state.agents[agent_id].active:
            raise ValueError("unknown or inactive agent")

    @staticmethod
    def _text(value, field):
        if not isinstance(value, str) or not value.strip() or len(value) > 8000:
            raise ValueError(f"{field} requires a nonempty bounded string")
        return value.strip()

    @staticmethod
    def _family(e):
        return str(e.metadata.get("segment_source_family") or e.source)

    @staticmethod
    def _span(e):
        m = e.metadata
        return (m.get("document_id", e.source), m.get("start"), m.get("end"), m.get("quote", e.claim))

    def _queue(self, data, inquiry_id, agent_id, kind, payload):
        item = dict(inquiry_id=inquiry_id, agent_id=agent_id, kind=kind, payload=deepcopy(payload))
        if any(all(q[k] == item[k] for k in item) for q in data["pending"] + data["running"]):
            return
        if len(data["pending"]) + len(data["running"]) >= self.config.max_pending:
            raise ValueError("agenda queue full")
        data["sequence"] += 1
        item["id"] = f"work-{data['sequence']}"
        data["pending"].append(item)

    def _retrieval_payload(self, action):
        if action["kind"] == "search":
            return {"query": self._text(action.get("query"), "query")}
        document_id = self._text(action.get("document_id"), "document_id")
        if not re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_.:-]{0,255}", document_id):
            raise ValueError("read document_id must be an opaque source ID, not a path")
        offset = action.get("offset", 0)
        if type(offset) is not int or offset < 0:
            raise ValueError("read offset must be a nonnegative integer")
        return {"document_id": document_id, "offset": offset}

    def apply(self, agent_id: str, action: dict) -> AlgorithmResult:
        """Apply one authenticated proposal atomically; rejected proposals mutate nothing.

        Interpretive changes require Evidence or an unresolved premise. Search/read
        acquire context and can stand alone without an inquiry or asserted premise.
        They create bounded assignments, never unrestricted corpus access; the
        executor must enforce arrived membership and document offset boundaries.
        """
        self._agent(agent_id)
        kind = action.get("kind")
        if kind not in {"open", "join", "request_peer", "search", "read", "watch", "revise", "close"}:
            raise ValueError("unknown inquiry action")
        evidence = tuple(action.get("evidence", ()))
        if any(
            not isinstance(e, Evidence)
            or not self.validate_evidence(e)
            or (self.evidence_available is not None and not self.evidence_available(agent_id, e))
            for e in evidence
        ):
            raise ValueError("invalid or unarrived evidence")
        premise = action.get("unresolved_premise", "")
        if premise:
            premise = self._text(premise, "unresolved_premise")
        iid = action.get("inquiry_id")
        if not premise and kind in {"search", "read", "watch"} and iid in self.data["inquiries"]:
            premise = self.data["inquiries"][iid].get("unresolved_premise", "")
        if kind in {"search", "read"} and iid is None:
            payload = self._retrieval_payload(action)
            data = deepcopy(self.data)
            self._queue(data, None, agent_id, kind, payload)
            self.state.data[self.KEY] = data
            return AlgorithmResult(metadata={"inquiry_id": None, "standalone_retrieval": True})
        if not evidence and not premise and kind not in {"search", "read"}:
            raise ValueError("change needs source evidence or a specific unresolved premise")
        data = deepcopy(self.data)
        messages = []
        if kind == "open":
            question = self._text(action.get("question"), "question")
            key = " ".join(question.casefold().split())
            if any(
                " ".join(q["question"].casefold().split()) == key and q["status"] != "closed"
                for q in data["inquiries"].values()
            ):
                raise ValueError("question already open; join its inquiry")
            data["sequence"] += 1
            iid = f"inquiry-{data['sequence']}"
            row = dict(
                inquiry_id=iid,
                version=0,
                question=question,
                why_matters=self._text(action.get("why_matters"), "why_matters"),
                rivals=[],
                next_actions=[],
                watches=[],
                owner=agent_id,
                participants=[agent_id],
                status="open",
                evidence_ids=[],
            )
        else:
            iid = action.get("inquiry_id")
            if iid not in data["inquiries"]:
                raise ValueError("unknown inquiry")
            row = deepcopy(data["inquiries"][iid])
            if row["status"] == "closed":
                raise ValueError("inquiry closed; open a new linked inquiry")
            if kind != "join" and agent_id not in row["participants"]:
                raise ValueError("join inquiry before changing it")
        if kind == "revise":
            for field in ("question", "why_matters"):
                if field in action:
                    row[field] = self._text(action[field], field)
        for field in ("rivals", "next_actions"):
            if field in action:
                if not isinstance(action[field], (list, tuple)) or len(action[field]) > 12:
                    raise ValueError(f"{field} requires at most 12 strings")
                row[field] = [self._text(x, field) for x in action[field]]
        if kind == "join" and agent_id not in row["participants"]:
            row["participants"].append(agent_id)
        if kind == "request_peer":
            if len(data["pending"]) + len(data["running"]) >= self.config.max_pending:
                raise ValueError("agenda queue full")
            recipient = action.get("recipient")
            if recipient is None:
                recipient = self.router.route(
                    deepcopy(self.state),
                    agent_id,
                    frozenset(action.get("capabilities", ())),
                    visited=row["participants"],
                )
            if recipient is None or recipient == agent_id:
                raise ValueError("no eligible peer")
            self._agent(recipient)
            if recipient not in row["participants"]:
                row["participants"].append(recipient)
            self._queue(
                data,
                iid,
                recipient,
                "peer_review",
                {"request": premise or action.get("request", row["question"])},
            )
            messages.append(
                Message(
                    sender=agent_id,
                    recipients=(recipient,),
                    kind=MessageKind.QUESTION,
                    content=premise or action.get("request", row["question"]),
                    evidence=evidence,
                    step=self.state.step,
                    metadata={"inquiry_id": iid, "action": "request_peer"},
                )
            )
        if kind in {"open", "search", "read"}:
            payload = {}
            if kind in {"search", "read"}:
                payload = self._retrieval_payload(action)
            self._queue(data, iid, agent_id, "investigate" if kind == "open" else kind, payload)
            row["status"] = "open"
        if kind == "watch":
            terms = action.get("terms")
            if not isinstance(terms, (list, tuple)) or not 1 <= len(terms) <= 8:
                raise ValueError("watch needs 1..8 literal terms (all must match)")
            watch = {
                "terms": [self._text(t, "term").casefold() for t in terms],
                "occurrences": action.get("occurrences", False),
            }
            if type(watch["occurrences"]) is not bool:
                raise ValueError("occurrences must be boolean")
            if watch not in row["watches"]:
                row["watches"].append(watch)
            row["status"] = "watching"
        if kind == "close":
            row["status"] = "closed"
            data["pending"] = [q for q in data["pending"] if q["inquiry_id"] != iid]
        previous = self.state.artifacts.get(row.get("artifact_id"))
        all_evidence = list(previous.evidence if previous else ())
        seen = {self._span(e) for e in all_evidence}
        for e in evidence:
            if self._span(e) not in seen:
                all_evidence.append(e)
                seen.add(self._span(e))
        row.update(
            version=row["version"] + 1,
            latest_change=action.get("change", kind),
            unresolved_premise=premise,
            evidence_ids=[e.id for e in all_evidence],
            source_families=sorted({self._family(e) for e in all_evidence}),
        )
        row["artifact_id"] = f"{iid}:v{row['version']}"
        for field in ("virtual_time", "arrival_sequence", "event_sequence"):
            if field in action:
                row[field] = action[field]
        artifact = Artifact(
            id=row["artifact_id"],
            author=agent_id,
            content=deepcopy(row),
            parents=(previous.id,) if previous else (),
            evidence=tuple(all_evidence),
            tags=frozenset({"inquiry"}),
            created_step=self.state.step,
            metadata={"source_validation": "arrived_spans_only", "semantic_validation": False},
        )
        if kind == "revise":
            recipients = tuple(a for a in row["participants"] if a != agent_id)
            if recipients:
                for recipient in recipients:
                    self._queue(data, iid, recipient, "react", {"artifact_id": artifact.id})
                messages.append(
                    Message(
                        sender=agent_id,
                        recipients=recipients,
                        content=str(row["latest_change"]),
                        evidence=evidence,
                        artifact_ids=(artifact.id,),
                        kind=MessageKind.RESULT,
                        step=self.state.step,
                        metadata={"inquiry_id": iid, "action": "revise"},
                    )
                )
        data["inquiries"][iid] = row
        data["history"].append(deepcopy(row))
        self.state.data[self.KEY] = data
        self.state.artifacts[artifact.id] = artifact
        return AlgorithmResult(messages=tuple(messages), artifacts=(artifact,), metadata={"inquiry_id": iid})

    def explore(self, agent_id: str, premise: str) -> None:
        """Queue neutral scout work; every Nth eligible dispatch reserves exploration."""
        self._agent(agent_id)
        data = deepcopy(self.data)
        self._queue(data, None, agent_id, "explore", {"premise": self._text(premise, "premise")})
        self.state.data[self.KEY] = data

    def enqueue_exploration(self, agent_id: str, payload: dict) -> None:
        """Queue host-selected new-arrival context without making it globally public.

        Caller validates document membership before constructing prompt context.
        """
        self._agent(agent_id)
        if not isinstance(payload, dict):
            raise ValueError("exploration payload must be a dictionary")
        data = deepcopy(self.data)
        self._queue(data, None, agent_id, "explore", payload)
        self.state.data[self.KEY] = data

    def schedule(self, limit: int = 1) -> list[dict]:
        """Reserve bounded work; least-recently served inquiry first, FIFO ties.

        Charged dispatches are never refunded, including failures/cancellation.
        This agenda budget is work units; the provider ledger remains authoritative
        for API retries, tokens, USD, and concurrency.
        """
        if type(limit) is not int or limit < 0:
            raise ValueError("limit must be nonnegative")
        data = self.data
        result = []
        while len(result) < limit and data["actions_used"] < self.config.max_actions:
            busy = {q["agent_id"] for q in data["running"]}
            eligible = [
                q
                for q in data["pending"]
                if q["agent_id"] not in busy
                and self.state.agents[q["agent_id"]].active
                and (
                    q["inquiry_id"] is None
                    or data["per_inquiry"].get(q["inquiry_id"], 0) < self.config.max_actions_per_inquiry
                )
            ]
            if not eligible:
                break
            scouts = [q for q in eligible if q["kind"] == "explore"]
            if scouts and (data["actions_used"] + 1) % self.config.exploration_every == 0:
                chosen = scouts[0]
            else:
                chosen = min(
                    eligible,
                    key=lambda q: (
                        data["last_dispatched"].get(q["inquiry_id"], -1),
                        int(q["id"].split("-")[1]),
                    ),
                )
            data["pending"].remove(chosen)
            data["running"].append(chosen)
            data["actions_used"] += 1
            data["last_dispatched"][chosen["inquiry_id"]] = data["actions_used"]
            if chosen["inquiry_id"] is not None:
                iid = chosen["inquiry_id"]
                data["per_inquiry"][iid] = data["per_inquiry"].get(iid, 0) + 1
            result.append(deepcopy(chosen))
        return result

    def finish(self, assignment_id: str) -> None:
        matches = [q for q in self.data["running"] if q["id"] == assignment_id]
        if not matches:
            raise ValueError("unknown or already finished assignment")
        self.data["running"].remove(matches[0])

    def notify_arrival(self, evidence: Evidence, text: str) -> list[str]:
        """Wake watches on validated arrived sources, not repeated forwarded text.

        Explicit occurrences=True watches can track new receipts separately from
        corroboration; all evidence versions retain source-family dependence.
        """
        if not isinstance(evidence, Evidence) or not self.validate_evidence(evidence):
            raise ValueError("invalid or unarrived evidence")
        data = deepcopy(self.data)
        woke = []
        for iid, row in data["inquiries"].items():
            if row["status"] == "closed":
                continue
            for index, watch in enumerate(row["watches"]):
                if not all(t in text.casefold() for t in watch["terms"]):
                    continue
                origin = str(self._span(evidence)) if watch["occurrences"] else self._family(evidence)
                key = f"{iid}:{index}"
                seen = data["watch_seen"].setdefault(key, [])
                if origin in seen:
                    continue
                # Mark seen only after bounded enqueue succeeds; caller can retry.
                self._queue(data, iid, row["owner"], "watch", {"evidence": evidence, "watch": index})
                seen.append(origin)
                if iid not in woke:
                    woke.append(iid)
        self.state.data[self.KEY] = data
        return woke

    def snapshot(self) -> dict:
        result = deepcopy(self.data)
        result["inquiries"] = list(result["inquiries"].values())
        return result
