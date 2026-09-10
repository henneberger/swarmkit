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
import json
import math
import re
from dataclasses import asdict, dataclass, replace

from ..runtime import CallableAgent, MessageBus, SwarmRuntime, apply_result
from ..serialization import from_data, to_data
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
    def __init__(self, replay, store, client, config=None, agents=None, resume_run_id=None, peer_fact_probes=False):
        self.replay, self.store, self.client = replay, store, client
        saved = store.run(resume_run_id) if resume_run_id else None
        if resume_run_id and (not saved or saved.get("mode") != "inquiry_swarm"):
            raise ValueError("unknown inquiry run to resume")
        self.config = config or (
            InquiryExperimentConfig(**saved["config"]) if saved else InquiryExperimentConfig()
        )
        if saved and asdict(self.config) != saved["config"]:
            raise ValueError("resume configuration must match stored limits")
        if replay.stats()["arrived"] and not saved:
            raise ValueError("fresh experiment requires an empty replay membership")
        peers = agents or [AgentState(f"investigator-{i + 1}") for i in range(4)]
        if not peers or len({a.id for a in peers}) != len(peers):
            raise ValueError("distinct investigators required")
        self.state = (
            from_data(saved["state_snapshot"]) if saved else SwarmState(agents={a.id: a for a in peers})
        )
        if saved:
            if not isinstance(self.state, SwarmState) or agents is not None:
                raise ValueError("resume restores canonical agents; do not replace them")
            if replay.stats()["arrived"] != saved["metrics"]["arrived"] or replay.stats()[
                "virtual_time"
            ] != saved.get("virtual_time"):
                raise ValueError("replay membership differs from saved checkpoint")
            if saved.get("replay_bounds") and replay.stats()["bounds"] != saved["replay_bounds"]:
                raise ValueError("replay bounds differ from saved checkpoint")
            peers = list(self.state.agents.values())
        self.id = resume_run_id or new_id("inquiry-run")
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
            coverage_limitations="Stable-hash samples within sender partitions plus agent-selected arrived-history retrieval; watch candidates coalesced per inquiry/batch. Archive admission is not exhaustive model reading or validated discovery.",
            sampling_version="sender-partition-stable-hash-v2",
            inquiries=[],
            history=[],
            errors=[],
            event_sequence=0,
        )
        self.exposed = set()
        self.coverage = {a.id: [] for a in peers}
        self.coverage_archive = {a.id:{} for a in peers}
        self.seen_bodies = set()
        self.batches_processed = 0
        self.resuming = bool(saved)
        if saved:
            self.record = {k: v for k, v in saved.items() if k not in ("posts", "events")}
            self.runtime.budget.used_calls = self.agenda.data["actions_used"]
            self.runtime.budget.used_tokens = self.record["metrics"]["tokens"]
            self.runtime.budget.used_cost = self.record["metrics"]["cost"]
            extra = saved.get("resume_state", {})
            self.batches_processed = extra.get(
                "batches_processed",
                (replay.stats()["arrived"] + self.config.batch_size - 1) // self.config.batch_size,
            )
            self.exposed = set(extra.get("exposed", []))
            self.coverage = extra.get("coverage", self.coverage)
            self.coverage_archive = extra.get('coverage_archive', self.coverage_archive)
            if 'coverage_archive' not in extra:
                # Recover only sources recorded as exposed to this actor, never all arrivals.
                for event in saved.get('events', []):
                    if event.get('kind') == 'prompt_exposure':
                        actor = event.get('agent')
                        if actor in self.coverage_archive:
                            for docid in event.get('document_ids', []):
                                self._record_coverage(actor, docid)
                for actor, agent in self.state.agents.items():
                    for evidence in agent.memory.get('evidence_archive', {}).values():
                        if not replay.verify_evidence(evidence):
                            raise ValueError('coverage backfill source outside arrived history')
                        self._record_coverage(actor, evidence.metadata['document_id'])
            else:
                for actor, entries in self.coverage_archive.items():
                    if actor not in self.state.agents:
                        raise ValueError('unknown coverage owner')
                    for docid in list(entries):
                        self._record_coverage(actor, docid)
            if not extra:
                for event in saved.get("events", []):
                    if event.get("kind") == "prompt_exposure":
                        self.exposed.update(event.get("document_ids", []))
                for actor in self.coverage:
                    ids = [
                        d
                        for event in saved.get("events", [])
                        if event.get("agent") == actor and event.get("kind") == "prompt_exposure"
                        for d in event.get("document_ids", [])
                    ]
                    for docid in ids:
                        doc = replay.get(docid)
                        if doc:
                            item = {"sender": doc.sender, "subject": doc.subject[:120]}
                            if item not in self.coverage[actor]:
                                self.coverage[actor] = (self.coverage[actor] + [item])[-8:]
            # Read existing membership only; never re-admit the prefix or search future mail.
            with replay._lock:
                self.seen_bodies = {
                    r[0]
                    for r in replay._db.execute(
                        "SELECT d.body_sha256 FROM arrived a JOIN archive.documents d ON d.id=a.doc_id"
                    )
                }
            if any(replay.get(docid) is None for docid in self.exposed):
                raise ValueError("saved exposure outside replay membership")
            for actor in self.state.agents.values():
                evidence = [
                    *actor.private_evidence,
                    *actor.memory.get("evidence", {}).values(),
                    *actor.memory.get("evidence_archive", {}).values(),
                    *(e for m in actor.inbox for e in m.evidence),
                ]
                if any(not replay.verify_evidence(e) for e in evidence):
                    raise ValueError("saved private evidence outside replay membership")
            for artifact in self.state.artifacts.values():
                if any(not replay.verify_evidence(e) for e in artifact.evidence):
                    raise ValueError("saved evidence does not match replay membership")
            self.record.setdefault("resume_history", []).append(
                {
                    "prior_status": saved["status"],
                    "prior_errors": saved.get("errors", []),
                    "prior_shared_ledger_delta": dict(saved.get("shared_ledger_delta", {})),
                    **self._watermark(),
                }
            )
            self.record["errors"] = []
            if saved.get("errors") and not self.agenda.data["running"]:
                self._event(
                    "lost_assignment",
                    reason="prior failed dispatch already retired; no automatic repetition or budget refund",
                    **self._watermark(),
                )
            for work in list(self.agenda.data["running"]):
                self._event(
                    "lost_assignment",
                    assignment_id=work["id"],
                    reason="unknown interrupted outcome; reservation retained, not automatically repeated",
                    **self._watermark(),
                )
                self.agenda.finish(work["id"])
            self._event("resume", batches_processed=self.batches_processed, **self._watermark())

        if type(peer_fact_probes) is not bool:
            raise ValueError('peer_fact_probes must be boolean')
        flags = self.record.setdefault('protocol_flags', {})
        if peer_fact_probes and not flags.get('peer_fact_probes', False):
            flags['peer_fact_probes'] = True
            self._event('protocol_intervention', intervention='host_assisted_fact_probe_v1',
                scope='Only future agent-opened inquiries; one relevant addressed probe, no implicit join.', **self._watermark())
        self.peer_fact_probes = flags.get('peer_fact_probes', False)
        if self.peer_fact_probes and flags.get('probe_matching_version') != 'named_anchor_v2':
            flags['probe_matching_version'] = 'named_anchor_v2'
            self._event('protocol_intervention', intervention='probe_named_anchor_v2',
                scope='Future host probes require an observed named matter/person anchor from the original question.', **self._watermark())

    def owner_for(self, sender):
        ids = sorted(self.state.agents)
        index = int(hashlib.sha256(sender.casefold().strip().encode()).hexdigest()[:16], 16) % len(ids)
        return ids[index]

    def _sequence(self):
        self.record["event_sequence"] += 1
        return self.record["event_sequence"]

    def _event(self, kind, **fields):
        self.store.event(self.id, kind, event_sequence=self._sequence(), **fields)

    def _record_coverage(self, actor, docid):
        document = self.replay.get(docid)
        if actor not in self.state.agents or document is None:
            raise ValueError('coverage requires a known actor and arrived document')
        item = {'sender':document.sender,'subject':document.subject[:120]}
        self.coverage_archive.setdefault(actor,{})[docid] = item
        if item not in self.coverage[actor]:
            self.coverage[actor] = (self.coverage[actor]+[item])[-8:]

    def _peer_directory(self, query, limit=8):
        """Rank observed public descriptors; no private quote/claim is disclosed."""
        stop = {'the','and','for','with','from','this','that','have','was','are','not','re','fw','fwd','com','enron'}
        def tokens(text):
            return {t for t in re.findall(r'[a-z0-9]+',text.casefold()) if len(t)>2 and t not in stop}
        desired = tokens(query)
        all_entries = [item for entries in self.coverage_archive.values() for item in entries.values()]
        token_cache = {(item['sender'],item['subject']):tokens(item['sender']+' '+item['subject']) for item in all_entries}
        frequency = {term:sum(term in token_cache[(item['sender'],item['subject'])] for item in all_entries) for term in desired}
        directory=[]
        for peer in self.record['peers']:
            unique = {}
            for item in self.coverage_archive.get(peer['id'],{}).values():
                unique[(item['sender'],item['subject'])] = item
            entries=list(unique.values())
            def score(pair):
                index,item=pair
                overlap=desired & token_cache[(item['sender'],item['subject'])]
                return (sum(math.log(1+len(all_entries)/(1+frequency[t])) for t in overlap), index)
            selected=[item for _,item in sorted(enumerate(entries),key=score,reverse=True)[:limit]]
            directory.append({**peer,'coverage':selected,'coverage_descriptor_count':len(entries)})
        return directory

    def _on_exposure(self, fields):
        self.exposed.update(fields['document_ids'])
        for docid in fields['document_ids']:
            self._record_coverage(fields['agent'],docid)
        self._event('prompt_exposure', **fields)

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
        self.record["replay_bounds"] = self.replay.stats()["bounds"]
        self.record["metrics"]["arrived"] = self.replay.stats()["arrived"]
        self.record["metrics"]["scheduled_calls"] = self.agenda.data["actions_used"]
        self.record["metrics"]["exposed"] = len(self.exposed)
        self.record["resume_state"] = {
            "batches_processed": self.batches_processed,
            "exposed": sorted(self.exposed),
            "coverage": self.coverage,
            "coverage_archive": self.coverage_archive,
        }
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
        # Preserve access to previously recorded private work after short prompt caches expire.
        archive = dict(context.agent.memory.get("evidence_archive", {}))
        archive.update(context.agent.memory.get("evidence", {}))
        for prior in self.state.messages:
            if prior.sender == actor or (self.config.peer_exchange and actor in prior.recipients):
                archive.update({e.id: e for e in prior.evidence})
        for artifact in self.state.artifacts.values():
            if artifact.author == actor:
                archive.update({e.id: e for e in artifact.evidence})
        context.agent.memory["evidence_archive"] = archive
        messages = list(context.messages) if self.config.peer_exchange else []
        request_id = payload.get("request_id")
        if self.config.peer_exchange and request_id and work["kind"] in ("peer_review", "react"):
            # The inbox may have been consumed by an earlier exploration task.
            # Bind this assignment to its original addressed request/reply.
            candidates = [
                message
                for message in self.state.messages
                if actor in message.recipients
                and (
                    (work["kind"] == "peer_review" and message.id == request_id)
                    or (
                        work["kind"] == "react"
                        and message.metadata.get("request_id") == request_id
                        and message.sender == payload.get("sender")
                        and message.metadata.get("action") == "reply"
                    )
                )
            ]
            if not candidates:
                raise ValueError("assigned peer message is missing from the canonical conversation")
            assigned_message = candidates[-1]
            if all(message.id != assigned_message.id for message in messages):
                messages.append(assigned_message)
        directory = []
        for row in self.agenda.data["inquiries"].values():
            if row['inquiry_id'] == work['inquiry_id'] and actor in row["participants"] and (
                self.config.peer_exchange or len(row["participants"]) == 1 and actor == row["owner"]
            ):
                directory.append(dict(row))
                artifact = self.state.artifacts[row["artifact_id"]]
                # Artifacts are knowledge context, not correspondence. A synthetic
                # message here creates a reply target with no underlying request.
                context.agent.memory['evidence_archive'].update({e.id:e for e in artifact.evidence})
            else:
                directory.append({k: row[k] for k in ("inquiry_id", "question", "owner", "status")})
        for entry in directory:
            joined = actor in self.agenda.data['inquiries'][entry['inquiry_id']]['participants']
            entry['joined'] = joined
            entry['allowed_inquiry_actions'] = (['search','read','watch','revise','close','request_peer'] if joined else ['join','request_peer']) if entry['status'] != 'closed' else []
        # Agent IDs/capabilities are public; partition contents and private summaries are not.
        task = Task(
            work["id"],
            ("Scout NEW developments in the currently supplied arrival batch. Prioritize these sources; an unrelated older open inquiry or watch is not a reason to ignore them. Open a question only for a concrete useful gap, otherwise choose a targeted action or wait."
             if work['kind'] == 'explore' else "Choose a useful next inquiry action for the assigned question from your available context."),
            metadata={
                "assignment": {**{k: work[k] for k in ("inquiry_id", "kind")}, "request_id": request_id},
                "peers": self.record["peers"],
                "source_access_result": access_result,
            },
        )
        assigned = work["inquiry_id"]
        current_terms = set(re.findall(r'[a-z0-9]+',' '.join(d.subject+' '+d.sender for d in docs).casefold())) - {'the','and','for','from','with','enron','com','re','fw'}
        directory.sort(key=lambda row:(row['inquiry_id'] == assigned,
            len(current_terms & set(re.findall(r'[a-z0-9]+',row['question'].casefold()))),
            self.agenda.data['inquiries'][row['inquiry_id']].get('event_sequence',0)), reverse=True)
        routing_query = ' '.join([*(doc.subject+' '+doc.sender for doc in docs),
            *(row['question'] for row in directory if row['inquiry_id']==assigned),
            str(payload.get('request','')),str(payload.get('query','')),
            *(m.content for m in messages if m.id==request_id)])
        peers = self._peer_directory(routing_query)
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

    def _maybe_fact_probe(self, inquiry_id):
        """Host-assisted active elicitation, not spontaneous agent recruitment.

        HiddenBench motivates eliciting missing information before decisions
        (https://arxiv.org/abs/2505.11556); this lexical notice heuristic is an
        experimental adaptation, not that benchmark's algorithm or a truth test.
        """
        if not self.peer_fact_probes or inquiry_id in self.record.setdefault('fact_probe_considered', []):
            return
        self.record['fact_probe_considered'].append(inquiry_id)
        row = self.agenda.data['inquiries'][inquiry_id]
        if self.agenda.data['actions_used'] >= self.config.max_actions:
            return
        stop = {'the','and','for','from','with','this','that','which','what','why','did','does','was','were','have','has','how','are','not','enron','com','agreement','master','legal','meeting','please','request','update','office','status','matter','contract','message','current','review','approval'}
        stop.update({'about','could','would','should','can','will','when','where','who','whom','whether','any','there','their','these','those','document','documents','email','emails','executed','execution','letter','needed','needs','project','confirmation','authorization','signing','signed','form','forms','legal','credit','board','committee','department','agreement','notice','update','application','report','reports','final','draft'})
        def terms(text):
            return {t for t in re.findall(r'[a-z0-9]+',text.casefold()) if len(t)>2 and t not in stop}
        # Conservative surface-name heuristic: no inferred entities or topic aliases.
        anchors = {token.casefold() for token in re.findall(r'\b[A-Z][A-Za-z0-9]+\b',row['question'])
                   if len(token)>2 and token.casefold() not in stop}
        if not anchors:
            self._event('fact_probe_skipped',inquiry_id=inquiry_id,reason='no named matter/person anchor in original question',**self._watermark())
            return
        target = terms(row['question']+' '+row.get('unresolved_premise',''))
        peer_terms = {actor:set().union(*(terms(x['sender']+' '+x['subject']) for x in entries.values())) if entries else set() for actor,entries in self.coverage_archive.items()}
        candidates=[]
        for actor,observed in peer_terms.items():
            if actor == row['owner'] or not self.state.agents[actor].active:
                continue
            overlap=target & observed
            rare={term for term in overlap if sum(term in ts for ts in peer_terms.values()) <= max(1,len(peer_terms)//2)}
            if anchors & observed and rare and (len(overlap)>=2 or any(len(term)>=6 for term in rare)):
                candidates.append((len(rare),len(overlap),actor,sorted(overlap)))
        if not candidates:
            self._event('fact_probe_skipped',inquiry_id=inquiry_id,reason='no distinctive observed peer-coverage overlap',**self._watermark())
            return
        _,_,recipient,matched=max(candidates,key=lambda x:(x[0],x[1],x[2]))
        question = ('Host-assisted factual probe of a new inquiry. Question: '+row['question']+
            '\nUnresolved premise: '+row.get('unresolved_premise','')+
            '\nReport any relevant observed fact, including contrary or partial evidence. If your context has none, say so. Do not join, endorse, or infer a conclusion merely because you were asked.')
        try:
            result = self.agenda.apply(row['owner'],{'kind':'request_peer','inquiry_id':inquiry_id,
                'recipient':recipient,'question':question})
        except ValueError as exc:
            self._event('fact_probe_skipped',inquiry_id=inquiry_id,reason=str(exc)[:200],**self._watermark())
            return
        messages=tuple(replace(m,metadata={**m.metadata,'initiation':'host_assisted_fact_probe_v1','matched_coverage_terms':matched,'matched_named_anchors':sorted(anchors & set(matched)),'probe_matching_version':'named_anchor_v2'}) for m in result.messages)
        apply_result(self.state,replace(result,messages=messages),self.bus)
        self.record['metrics']['host_assisted_fact_probes'] = self.record['metrics'].get('host_assisted_fact_probes',0)+len(messages)
        for message in messages:
            self._event('peer_message',sender=message.sender,recipients=list(message.recipients),message_id=message.id,
                text=message.content,evidence=[evidence_view(e) for e in message.evidence],
                visibility='addressed' if self.config.peer_exchange else 'withheld_at_reasoner',
                artifact_ids=list(message.artifact_ids),inquiry_id=inquiry_id,action='request_peer',
                initiation='host_assisted_fact_probe_v1',matched_coverage_terms=matched,matched_named_anchors=sorted(anchors & set(matched)),probe_matching_version='named_anchor_v2',**self._watermark())

    async def _dispatch(self):
        assignments = self.agenda.schedule(1)
        if not assignments:
            return False
        work = assignments[0]
        self.current = work
        if work["kind"] == "read" and [
            work["payload"]["document_id"],
            work["payload"]["offset"],
        ] in self.state.agents[work["agent_id"]].memory.get("source_reads", []):
            self.agenda.finish(work["id"])
            self.state.agents[work["agent_id"]].memory["host_feedback"] = (
                "Duplicate read retired locally: this source offset was already requested. Choose another source, continuation offset, or action."
            )
            self.record["metrics"]["duplicate_reads_prevented"] = (
                self.record["metrics"].get("duplicate_reads_prevented", 0) + 1
            )
            self._event(
                "duplicate_read_retired",
                agent=work["agent_id"],
                assignment_id=work["id"],
                **self._watermark(),
            )
            self._persist()
            return True
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
                    if action["kind"] == "read":
                        key = [action.get("document_id"), action.get("offset", 0)]
                        prior = self.state.agents[message.sender].memory.get("source_reads", [])
                        queued = [
                            q
                            for q in self.agenda.data["pending"]
                            if q["agent_id"] == message.sender and q["kind"] == "read"
                        ]
                        if key in prior or any(
                            [q["payload"]["document_id"], q["payload"]["offset"]] == key for q in queued
                        ):
                            raise ValueError(
                                "duplicate read: this source offset was already requested; choose a different source, continuation, or action"
                            )
                    action["evidence"] = message.evidence
                    action.update(self._watermark(), event_sequence=self._sequence())
                    applied = self.agenda.apply(message.sender, action)
                    self.state.agents[message.sender].memory.pop("host_feedback", None)
                    action["inquiry_id"] = applied.metadata["inquiry_id"]
                    apply_result(self.state, applied, self.bus)
                    if action['kind'] == 'open':
                        self._maybe_fact_probe(action['inquiry_id'])
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
                if str(exc).startswith("duplicate read:"):
                    self.record["metrics"]["duplicate_reads_prevented"] = (
                        self.record["metrics"].get("duplicate_reads_prevented", 0) + 1
                    )
                feedback = f"Your {action.get('kind')} action was not executed: {str(exc)[:500]}. "
                if str(exc) == 'join inquiry before changing it':
                    feedback += 'First choose an explicit join action for inquiry_id ' + json.dumps(action.get('inquiry_id')) + '; cite your reason/evidence or a specific unresolved_premise. Joining does not execute the rejected watch/revision: request it again on a later turn.'
                elif str(exc).startswith('reply needs one known unanswered request'):
                    feedback += 'Reply only to an actually supplied addressed QUESTION and copy its request_id. If none is supplied, choose wait or request_peer; do not send an unsolicited reply.'
                else:
                    feedback += 'Correct the request or choose a different action.'
                self.state.agents[message.sender].memory['host_feedback'] = feedback
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

    def _process_arrivals(self, arrivals, groups):
        """Cheap body prefilter before exact segment parsing and provenance checks.

        All queried IDs are in this newly committed arrival batch. A
        fresh candidate is needed to wake an inquiry again within a batch;
        candidates matching only already-woken inquiries are coalesced and counted,
        not claimed read or resolved. Detailed retrieval
        remains available through the arrived-only corpus.
        """
        watches = [(iid,index,watch) for iid,row in self.agenda.data['inquiries'].items()
                   if row['status'] != 'closed' for index,watch in enumerate(row['watches'])]
        bodies = {}
        if watches:
            for start in range(0,len(arrivals),400):
                ids = [row['id'] for row in arrivals[start:start+400]]
                with self.replay._lock:
                    rows = self.replay._db.execute(
                        'SELECT d.id,d.body FROM arrived a JOIN archive.documents d ON d.id=a.doc_id WHERE a.doc_id IN ('+','.join('?' for _ in ids)+')', ids).fetchall()
                bodies.update({row[0]:row[1] for row in rows})
        awakened = set()
        metrics = self.record['metrics']
        for row in arrivals:
            if row['body_sha256'] not in self.seen_bodies:
                self.seen_bodies.add(row['body_sha256'])
                groups[self.owner_for(row['sender'])].append(row['id'])
            if not watches:
                continue
            text = bodies[row['id']].casefold()
            matches = {(iid,index) for iid,index,watch in watches if all(term in text for term in watch['terms'])}
            if not matches:
                continue
            metrics['watch_candidate_documents'] = metrics.get('watch_candidate_documents',0)+1
            if matches <= awakened:
                metrics['watch_coalesced_documents'] = metrics.get('watch_coalesced_documents',0)+1
                continue
            for segment in self.replay.segments(row['id']):
                if segment.kind == 'header' or len(segment.text.strip()) < 15:
                    continue
                segment_text = segment.text.casefold()
                if not any((iid,index) not in awakened and all(term in segment_text for term in watch['terms']) for iid,index,watch in watches):
                    continue
                evidence = self.replay.evidence(row['id'],segment.start,segment.end,owner='arrival-watcher')
                try:
                    woke = self.agenda.notify_arrival(evidence,segment.text)
                except ValueError as exc:
                    if str(exc) != 'agenda queue full':
                        raise
                    metrics['watch_queue_deferrals'] = metrics.get('watch_queue_deferrals',0)+1
                    continue
                # Only coalesce the concrete subscriptions now represented in work.
                awakened.update((q['inquiry_id'],q['payload']['watch'])
                    for q in self.agenda.data['pending'] + self.agenda.data['running']
                    if q['kind'] == 'watch' and q['inquiry_id'] in woke)
                for iid in woke:
                    self._event('watch_wake',inquiry_id=iid,document_id=row['id'],**self._watermark())
        metrics['watch_scanned_documents'] = metrics.get('watch_scanned_documents',0)+(len(arrivals) if watches else 0)

    async def run(self):
        gate = getattr(self.client, "gate", None)
        initial_gate = gate.status() if gate else None
        ledger_segment = None
        if gate:
            segments = self.record.setdefault("ledger_segments", [])
            if not segments and self.record.get("shared_ledger_delta"):
                segments.append(
                    {
                        "id": "legacy-aggregate",
                        "kind": "imported_prior_aggregate",
                        "delta": dict(self.record["shared_ledger_delta"]),
                        "scope": "Prior recorded aggregate; individual historical boundaries unavailable.",
                    }
                )
            ledger_segment = {
                "id": new_id("ledger-segment"),
                "kind": "execution",
                "start": {k: initial_gate[k] for k in ("calls", "tokens", "cost_usd")},
                "start_arrival_sequence": self.replay.stats()["arrived"],
                "delta": None,
            }
            segments.append(ledger_segment)
        self.record["status"] = "running"
        self._persist()
        try:
            if self.resuming:
                for _ in range(self.config.actions_per_batch):
                    if not await self._dispatch():
                        break
                self.resuming = False
            for _ in range(self.batches_processed, self.config.max_batches):
                if (
                    self.record["status"] == "incomplete"
                    or self.agenda.data["actions_used"] >= self.config.max_actions
                ):
                    break
                arrivals = self.replay.admit_next_metadata(self.config.batch_size)
                if not arrivals:
                    break
                self.batches_processed += 1
                groups = {a: [] for a in self.state.agents}
                self._process_arrivals(arrivals, groups)
                for agent, docids in groups.items():
                    if docids:
                        # Deterministic content-neutral reservoir per sender partition.
                        selected = sorted(docids, key=lambda d:hashlib.sha256(d.encode()).digest())[:self.config.docs_per_agent]
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
            if self.record["status"] != "incomplete" and self.replay.stats()["complete"]:
                # Finish already scheduled conversations after the final arrival,
                # still subject to the same per-inquiry and total action limits.
                while await self._dispatch():
                    pass
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
                ledger_segment["end"] = {key: final_gate[key] for key in ("calls", "tokens", "cost_usd")}
                ledger_segment["end_arrival_sequence"] = self.replay.stats()["arrived"]
                ledger_segment["delta"] = {
                    key: final_gate[key] - initial_gate[key] for key in ("calls", "tokens", "cost_usd")
                }
                self.record["shared_ledger_delta"] = {
                    key: sum(
                        segment["delta"][key]
                        for segment in self.record["ledger_segments"]
                        if segment.get("delta") is not None
                    )
                    for key in ("calls", "tokens", "cost_usd")
                }
                self.record["ledger_accounting_complete"] = all(
                    segment.get("delta") is not None for segment in self.record["ledger_segments"]
                )
                self.record["shared_ledger_delta_scope"] = (
                    "Sum of recorded execution-interval shared-ledger deltas plus any labeled legacy aggregate; "
                    "includes concurrent callers and charged failures during those intervals, excludes between-session activity. "
                    "Segments missing a terminal checkpoint are explicitly incomplete and are not silently estimated."
                )
            self._persist()
        return self.store.run(self.id)
