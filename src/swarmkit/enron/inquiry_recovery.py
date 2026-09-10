"""Explicit recovery of factual peer requests rejected by an older host version.

Reuses recorded agent intent and its original canonical evidence. Delivery occurs
at the current cursor; nothing is backdated or presented as a new model decision.
"""

from dataclasses import replace

from ..runtime import apply_result
from .investigate import evidence_view


def recover_peer_requests(engine):
    run = engine.store.run(engine.id)
    recovered = set(engine.state.data.get("recovered_peer_request_posts", []))
    originals = {message.id: message for message in engine.state.messages}
    delivered = 0
    for post in run.get("posts", []):
        if (
            post.get("id") in recovered
            or not post.get("reasoning_rejected")
            or post.get("action", {}).get("kind") != "request_peer"
        ):
            continue
        original = originals.get(post.get("id"))
        if original is None or original.metadata.get("action", {}).get("kind") != "request_peer":
            continue
        action = dict(original.metadata["action"], evidence=original.evidence)
        try:
            result = engine.agenda.apply(original.sender, action)
        except (ValueError, TypeError, KeyError) as exc:
            engine._event(
                "request_recovery_rejected",
                original_post_id=post["id"],
                reason=str(exc)[:300],
                **engine._watermark(),
            )
            continue
        result = replace(
            result,
            messages=tuple(
                replace(
                    message,
                    metadata={
                        **message.metadata,
                        "recovered_from_post": post["id"],
                        "original_virtual_time": post.get("virtual_time"),
                    },
                )
                for message in result.messages
            ),
        )
        apply_result(engine.state, result, engine.bus)
        recovered.add(post["id"])
        engine.state.data["recovered_peer_request_posts"] = sorted(recovered)
        for message in result.messages:
            delivered += 1
            engine._event(
                "peer_message",
                sender=message.sender,
                recipients=list(message.recipients),
                message_id=message.id,
                text=message.content,
                evidence=[evidence_view(e) for e in message.evidence],
                inquiry_id=message.metadata.get("inquiry_id"),
                action="request_peer",
                visibility="addressed" if engine.config.peer_exchange else "withheld_at_reasoner",
                recovered_from_post=post["id"],
                original_virtual_time=post.get("virtual_time"),
                **engine._watermark(),
            )
        engine._event(
            "request_recovered",
            original_post_id=post["id"],
            delivered=bool(result.messages),
            **engine._watermark(),
        )
    engine._persist()
    return delivered


def recheck_peer_retrieval(engine):
    """Revisit recorded factual questions after repairing private-source retrieval.

    This is an explicit host maintenance intervention at the current cursor.
    Earlier requests/replies remain intact. Prior requested pages can be recovered
    from immutable arrived sources; no new question or future source is invented.
    """
    from .source_context import SourceContext

    sources = SourceContext(engine.replay)
    for actor in engine.state.agents.values():
        archive = dict(actor.memory.get("evidence_archive", actor.memory.get("evidence", {})))
        recovered_pages = 0
        for docid, offset in actor.memory.get("source_reads", []):
            doc = engine.replay.get(docid)
            if doc is not None and 0 <= offset < len(doc.body):
                _, refs = sources.build([doc], {docid: offset})
                archive.update({e.id: e for e in refs.values()})
                recovered_pages += 1
        actor.memory["evidence_archive"] = archive
        engine._event(
            "private_source_archive_recovered",
            agent=actor.id,
            requested_pages=recovered_pages,
            retained_spans=len(archive),
            **engine._watermark(),
        )
    checked = set(engine.state.data.get("retrieval_rechecked_requests", []))
    prior = list(engine.agenda.data.get("peer_requests", {}).values())
    count = 0
    for request in prior:
        if request["request_id"] in checked or request.get("retrieval_recheck"):
            continue
        original = next((m for m in engine.state.messages if m.id == request["request_id"]), None)
        if original is None:
            continue
        result = engine.agenda.apply(
            request["sender"],
            {
                "kind": "request_peer",
                "recipient": request["recipient"],
                "inquiry_id": request["inquiry_id"],
                "evidence": original.evidence,
                "question": "Recheck your retained source archive for this earlier question: "
                + request["request"]
                + " Provide the relevant exact source, or say none is available.",
            },
        )
        apply_result(engine.state, result, engine.bus)
        checked.add(request["request_id"])
        engine.state.data["retrieval_rechecked_requests"] = sorted(checked)
        engine.agenda.data["peer_requests"][result.metadata["request_id"]]["retrieval_recheck"] = True
        for message in result.messages:
            count += 1
            engine._event(
                "peer_message",
                sender=message.sender,
                recipients=list(message.recipients),
                message_id=message.id,
                text=message.content,
                evidence=[evidence_view(e) for e in message.evidence],
                inquiry_id=message.metadata.get("inquiry_id"),
                action="request_peer",
                visibility="addressed" if engine.config.peer_exchange else "withheld_at_reasoner",
                retrieval_recheck_of=request["request_id"],
                **engine._watermark(),
            )
    engine._persist()
    return count
