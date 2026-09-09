"""Experimental chronological inquiry swarm, not validated emergent discovery.

Private sender partitions seed different observations; agents select inquiry work,
address peers, retrieve arrived context, and register later-arrival watches. The
agenda controls dispatch, not a fixed round of reviewers. A small public question
directory is intentional disclosure; private source text reaches only its owner,
explicit recipients, subscribers, or an agent that retrieves it. Runtime isolation
is logical: trusted adapters deliberately ignore its globally available artifacts.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass

from ..runtime import CallableAgent, MessageBus, SwarmRuntime, apply_result
from ..serialization import to_data
from ..types import AgentState, Budget, Message, SwarmState, Task, new_id
from .inquiries import AgendaConfig, InquiryAgenda
from .inquiry_model import InquiryReasoner
from .investigate import evidence_view


@dataclass(frozen=True)
class InquiryExperimentConfig:
    batch_size: int = 20
    max_batches: int = 4
    actions_per_batch: int = 4
    max_actions: int = 16
    max_actions_per_inquiry: int = 8
    docs_per_agent: int = 3
    max_output_tokens: int = 1800
    peer_exchange: bool = True

    def __post_init__(self):
        if any(type(v) is not int or v < 1 for k, v in vars(self).items() if k != "peer_exchange"):
            raise ValueError("experiment limits must be positive integers")
        if type(self.peer_exchange) is not bool:
            raise ValueError("peer_exchange must be boolean")
        if self.batch_size > 10000 or self.docs_per_agent > 16:
            raise ValueError("batch/source context limit exceeded")


class InquiryExperiment:
    def __init__(self, replay, store, client, config=None, agents=None):
        self.replay, self.store, self.client = replay, store, client
        self.config = config or InquiryExperimentConfig()
        if replay.stats()["arrived"]:
            raise ValueError("fresh experiment requires an empty replay membership")
        peers = agents or [AgentState(f"investigator-{i + 1}") for i in range(4)]
        if not peers or len({a.id for a in peers}) != len(peers):
            raise ValueError("distinct investigators required")
        self.state = SwarmState(agents={a.id: a for a in peers})
        self.id = new_id("inquiry-run")
        self.agenda = InquiryAgenda(
            self.state,
            replay.verify_evidence,
            AgendaConfig(
                max_actions=self.config.max_actions,
                max_actions_per_inquiry=self.config.max_actions_per_inquiry,
                max_pending=max(32, self.config.max_actions * 2),
            ),
        )
        self.reasoner = InquiryReasoner(
            replay, client, max_output_tokens=self.config.max_output_tokens, on_exposure=self._on_exposure
        )
        self.bus = MessageBus()
        self.runtime = SwarmRuntime(
            self.state,
            {a.id: CallableAgent(self._act) for a in peers},
            bus=self.bus,
            budget=Budget(max_calls=self.config.max_actions),
            timeout=None,
        )
        self.current = None
        self.record = dict(
            id=self.id,
            mode="inquiry_swarm",
            model=getattr(client, "model", "offline-test-client"),
            status="created",
            config=asdict(self.config),
            algorithm_version="inquiry-agenda-v1",
            peers=[{"id": a.id, "capabilities": sorted(a.capabilities)} for a in peers],
            metrics=dict(
                arrived=0,
                allocated=0,
                exposed=0,
                scheduled_calls=0,
                model_calls=0,
                tokens=0,
                cost=0.0,
                action_rejections=0,
                reasoning_rejections=0,
            ),
            coverage_limitations="Bounded sender-partition samples and agent-selected arrived-history retrieval; no exhaustive reading or validated discovery.",
            inquiries=[],
            history=[],
            errors=[],
            event_sequence=0,
        )
        self.exposed = set()
        self.coverage = {a.id: [] for a in peers}
        self.seen_bodies = set()

    def owner_for(self, sender):
        ids = sorted(self.state.agents)
        index = int(hashlib.sha256(sender.casefold().strip().encode()).hexdigest()[:16], 16) % len(ids)
        return ids[index]

    def _sequence(self):
        self.record["event_sequence"] += 1
        return self.record["event_sequence"]

    def _event(self, kind, **fields):
        self.store.event(self.id, kind, event_sequence=self._sequence(), **fields)

    def _on_exposure(self, fields):
        self.exposed.update(fields["document_ids"])
        for docid in fields["document_ids"]:
            doc = self.replay.get(docid)
            if doc:
                item = {"sender": doc.sender, "subject": doc.subject[:120]}
                actor = fields["agent"]
                if item not in self.coverage[actor]:
                    self.coverage[actor] = (self.coverage[actor] + [item])[-8:]
        self._event("prompt_exposure", **fields)

    def _watermark(self):
        stats = self.replay.stats()
        return dict(virtual_time=stats["virtual_time"], arrival_sequence=stats["arrived"])

    def _persist(self):
        snapshot = self.agenda.snapshot()
        self.record.update(
            inquiries=snapshot["inquiries"],
            history=snapshot["history"],
            virtual_time=self.replay.stats()["virtual_time"],
            agenda=to_data(snapshot),
        )
        self.record["metrics"]["arrived"] = self.replay.stats()["arrived"]
        self.record["metrics"]["scheduled_calls"] = self.agenda.data["actions_used"]
        self.record["metrics"]["exposed"] = len(self.exposed)
        self.record["state_snapshot"] = to_data(self.state)
        self.store.save_run(self.record)

    async def _act(self, context):
        work = self.current
        actor = context.agent.id
        payload = work["payload"]
        docs, offsets = [], {}
        access_result = None
        if work["kind"] == "search":
            query = str(payload["query"])
            match = "all" if query.startswith("all:") else "any"
            query = query[4:] if match == "all" else query
            query = " ".join(re.findall(r"[\w@.-]+", query)[:32])[:300]
            if query:
                docs = self.replay.search(query, limit=self.config.docs_per_agent, match=match)
            self._event(
                "historical_retrieval",
                agent=actor,
                query=query,
                match=match,
                document_ids=[d.id for d in docs],
                **self._watermark(),
            )
        elif work["kind"] == "read":
            doc = self.replay.get(payload["document_id"])
            if doc is not None and 0 <= payload["offset"] < len(doc.body):
                docs, offsets = [doc], {doc.id: payload["offset"]}
            prior_reads = self.state.agents[actor].memory.setdefault("source_reads", [])
            read_key = [payload["document_id"], payload["offset"]]
            access_result = {
                "document_id": payload["document_id"],
                "offset": payload["offset"],
                "already_requested": read_key in prior_reads,
                "arrived": doc is not None,
                "body_length": len(doc.body) if doc is not None else None,
                "outcome": "page_supplied" if docs else "no_readable_characters_at_requested_offset",
            }
            if read_key not in prior_reads:
                prior_reads.append(read_key)
            self._event(
                "historical_read",
                agent=actor,
                document_ids=[d.id for d in docs],
                offset=payload["offset"],
                **self._watermark(),
            )
        elif work["kind"] == "watch":
            doc = self.replay.get(payload["evidence"].metadata["document_id"])
            docs = [doc] if doc else []
            if doc:
                offsets = {doc.id: payload["evidence"].metadata["start"]}
        elif work["kind"] == "explore":
            docs = [d for docid in payload.get("document_ids", []) if (d := self.replay.get(docid))]
        messages = list(context.messages) if self.config.peer_exchange else []
        directory = []
        for row in self.agenda.data["inquiries"].values():
            if actor in row["participants"] and (
                self.config.peer_exchange or len(row["participants"]) == 1 and actor == row["owner"]
            ):
                directory.append(row)
                artifact = self.state.artifacts[row["artifact_id"]]
                messages.append(
                    Message(
                        artifact.author,
                        "Subscribed inquiry context.",
                        recipients=(actor,),
                        evidence=artifact.evidence,
                        artifact_ids=(artifact.id,),
                    )
                )
            else:
                directory.append({k: row[k] for k in ("inquiry_id", "question", "owner", "status")})
        # Agent IDs/capabilities are public; partition contents and private summaries are not.
        task = Task(
            work["id"],
            "Choose a useful next inquiry action from your available context.",
            metadata={
                "assignment": {k: work[k] for k in ("inquiry_id", "kind")},
                "peers": self.record["peers"],
                "source_access_result": access_result,
            },
        )
        assigned = work["inquiry_id"]
        directory.sort(key=lambda row: row["inquiry_id"] != assigned)
        peers = [{**p, "coverage": self.coverage[p["id"]]} for p in self.record["peers"]]
        output = await self.reasoner.act(
            context.agent,
            task,
            documents=docs,
            offsets=offsets,
            peers=peers,
            messages=messages,
            inquiries=directory,
            **self._watermark(),
        )
        self.record["metrics"]["model_calls"] += output.usage.calls
        self.record["metrics"]["tokens"] += output.usage.tokens
        self.record["metrics"]["cost"] += output.usage.cost
        return output

    async def _dispatch(self):
        assignments = self.agenda.schedule(1)
        if not assignments:
            return False
        work = assignments[0]
        self.current = work
        self._persist()
        result = await self.runtime.round(
            Task(work["id"], "Inquiry agenda dispatch"), phase=work["kind"], participants=(work["agent_id"],)
        )
        self.agenda.finish(work["id"])
        if result.metadata.get("errors"):
            self.record["errors"].append(result.metadata["errors"])
            self.record["status"] = "incomplete"
            return False
        for message in result.messages:
            action = dict(message.metadata.get("action", {"kind": "wait"}))
            rejected = message.metadata.get("reasoning_rejected", False)
            self.record["metrics"]["reasoning_rejections"] += int(rejected)
            try:
                if action["kind"] != "wait":
                    action["evidence"] = message.evidence
                    action.update(self._watermark(), event_sequence=self._sequence())
                    applied = self.agenda.apply(message.sender, action)
                    self.state.agents[message.sender].memory.pop("host_feedback", None)
                    action["inquiry_id"] = applied.metadata["inquiry_id"]
                    apply_result(self.state, applied, self.bus)
                    for routed in applied.messages:
                        self._event(
                            "peer_message",
                            sender=routed.sender,
                            recipients=list(routed.recipients),
                            message_id=routed.id,
                            text=routed.content,
                            evidence=[evidence_view(e) for e in routed.evidence],
                            visibility="addressed" if self.config.peer_exchange else "withheld_at_reasoner",
                            artifact_ids=list(routed.artifact_ids),
                            inquiry_id=routed.metadata["inquiry_id"],
                            action=routed.metadata["action"],
                            **self._watermark(),
                        )
            except (ValueError, TypeError, KeyError) as exc:
                rejected = True
                self.record["metrics"]["action_rejections"] += 1
                self.state.agents[message.sender].memory["host_feedback"] = (
                    f"Your {action.get('kind')} action was not executed: {str(exc)[:500]}. "
                    "Correct the request or choose a different action."
                )
                self._event(
                    "action_rejected", agent=message.sender, reason=str(exc)[:500], **self._watermark()
                )
            self.store.post(
                self.id,
                dict(
                    id=message.id,
                    agent=message.sender,
                    agent_id=message.sender,
                    phase=work["kind"],
                    event_sequence=self._sequence(),
                    text=message.content,
                    action={k: v for k, v in action.items() if k != "evidence"},
                    inquiry_id=action.get("inquiry_id"),
                    reasoning_rejected=rejected,
                    reasoning_rejection_reason=message.metadata.get("reasoning_rejection_reason"),
                    finish_reason=message.metadata.get("finish_reason"),
                    evidence=[evidence_view(e) for e in message.evidence],
                    **self._watermark(),
                ),
            )
        self._persist()
        return True

    async def run(self):
        gate = getattr(self.client, "gate", None)
        initial_gate = gate.status() if gate else None
        self.record["status"] = "running"
        self._persist()
        try:
            for _ in range(self.config.max_batches):
                arrivals = self.replay.admit_next_metadata(self.config.batch_size)
                if not arrivals:
                    break
                groups = {a: [] for a in self.state.agents}
                for row in arrivals:
                    # Watch all newly arrived substantial segments, not just samples.
                    for segment in self.replay.segments(row["id"]):
                        if segment.kind != "header" and len(segment.text.strip()) >= 15:
                            e = self.replay.evidence(
                                row["id"], segment.start, segment.end, owner="arrival-watcher"
                            )
                            woke = self.agenda.notify_arrival(e, segment.text)
                            for iid in woke:
                                self._event(
                                    "watch_wake", inquiry_id=iid, document_id=row["id"], **self._watermark()
                                )
                    if row["body_sha256"] not in self.seen_bodies:
                        self.seen_bodies.add(row["body_sha256"])
                        groups[self.owner_for(row["sender"])].append(row["id"])
                for agent, docids in groups.items():
                    if docids:
                        selected = docids[: self.config.docs_per_agent]
                        self.agenda.enqueue_exploration(agent, {"document_ids": selected})
                        self.record["metrics"]["allocated"] += len(selected)
                self._persist()
                for _ in range(self.config.actions_per_batch):
                    if not await self._dispatch():
                        break
                if (
                    self.record["status"] == "incomplete"
                    or self.agenda.data["actions_used"] >= self.config.max_actions
                ):
                    break
            if self.record["status"] != "incomplete":
                self.record["status"] = (
                    "completed"
                    if self.replay.stats()["complete"] and not self.agenda.data["pending"]
                    else "partial"
                )
                self.record["completion_scope"] = (
                    "Configured arrival prefix and work budget; open inquiries are not resolved by run completion."
                )
        except Exception as exc:
            self.record["status"] = "incomplete"
            # Exceptions from providers must already be sanitized by their client.
            self.record["errors"].append({"type": type(exc).__name__})
        finally:
            if gate:
                final_gate = gate.status()
                self.record["shared_ledger_delta"] = {
                    key: final_gate[key] - initial_gate[key] for key in ("calls", "tokens", "cost_usd")
                }
                self.record["shared_ledger_delta_scope"] = (
                    "All shared-ledger activity during run, including concurrent callers and charged failures."
                )
            self._persist()
        return self.store.run(self.id)
