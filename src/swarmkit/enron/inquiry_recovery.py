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
