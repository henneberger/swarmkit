"""Model-owned Foundry actions with auditable prompts, strict parsing and exact-context replay."""

from __future__ import annotations

import hashlib
import json
import math
import time
from dataclasses import asdict, replace
from pathlib import Path

from ..types import AgentOutput, Decision, Message, Usage

PROTOCOLS = {
    "broadcast": "You may send one message to all other agents per round. recipients must be [].",
    "targeted": "You may send one message per round to a chosen nonempty subset of other agents. Use requests, evidence, proposals or acknowledgments as you judge useful.",
    "coordinator": "You may send one message per round through hub firm0.sensor. Other agents may address only the hub; the hub may address any nonempty subset of other agents. The hub has no privileged observations or extra calls.",
}

SYSTEM = """You are one autonomous specialist in a repeated research-production economy. Optimize the objective in your observation over the entire episode. Other agents are independent decision makers; their messages can be mistaken or self-serving. No agent has the complete initial evidence. Choose your own research, disclosure, negotiation, partners, design and publication strategy.

Mechanics:
- A device recipe is [sensor_index,power_index,firmware_index]. Quality equals the three component measurements PLUS the whole-recipe interaction measurement; missing values are UNKNOWN, not zero. Evidence cards are authenticated measurements. Artifacts give measured recipe quality; use only current-version facts for current physics.
- Each generation has several synchronous rounds. Round 0 submits a sealed bid (your requested per-build payment). Round 1 ranks acceptable partners after bid reveal and one round of messages. Sensor specialists rank power and firmware partners; others rank sensor coordinators. Empty preference lists refuse participation. Matching uses both sides' rankings, one partner per specialty. Affordable matched teams get customer-funded contracts at 3*largest ask, split equally on successful delivery. Partners may work across firms. Rankings do not guarantee a team.
- Each order belongs to its sensor coordinator. Assignments become visible after round 1. At commit, each team member independently chooses the index for its OWN specialty from its recipe. Different choices can assemble a different recipe than the coordinator intended. Agree on a complete design before committing. Messages at commit arrive too late to help.
- A legal query buys one measurement for cost 1, delivered next round subject to the generation research budget. You may query only your permitted specialty topics. Duplicate queries still cost 1. No query runs at commit. Execution consumes materials, specialty costs, and shared equipment time; all order thresholds and deadlines must be met. Failure pays nothing. Full effort does not guarantee success.
- Optional forecast prices concern each firm's order. A non-null forecast takes a small funded long position in success if >=0.5, failure otherwise. This changes your balance. Null means no trade.
- Shared objective: total accepted order value minus real research, execution and verification costs. Private objective: your own cash change minus your own execution/research costs. Neither objective instructs you to cooperate or conceal. Choose your strategy.
- Successful builds are independently verified. The sensor coordinator's publish decision determines whether the recipe enters the shared archive for future generations. Withholding does not prevent customer payment or your team's own outcome feedback. Publication has no fee. Retained artifacts can survive turnover, with version labels. Replacements lose predecessor observations and notes. Physics changes invalidate old measurements. Your memory is a short note you explicitly write; use it to remember commitments and lessons.

Return ONLY a JSON object with these fields, no markdown:
{"bid":3,"query":null,"preferences":{"power":["firm0.power"],"firmware":["firm0.firmware"]},"recipe":[0,0,0],"publish":true,"forecast":null,"memory":"brief private notes","messages":[{"recipients":[],"content":"brief public message","evidence_ids":[]}]}
For power/firmware roles preferences instead has only "sensor": [...]. Use actual member IDs and legal indices from your observation. Evidence IDs may cite observed measurement cards or visible artifact IDs; an artifact citation is not a new component measurement. You can send zero messages. At most one message, 800 content characters, 12 evidence IDs, and 800 memory characters. Always provide all fields. Bid must be finite and nonnegative, forecast null or [0,1]. Do not embed hidden chain-of-thought; return decisions and concise operational notes.
"""


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def observed_cards(context):
    return {
        e.id: e for e in (*context.agent.private_evidence, *(e for m in context.messages for e in m.evidence))
    }


def observation(context):
    public = dict(context.task.metadata)
    public["last_results"] = [
        {
            k: o[k]
            for k in ("order", "generation", "version", "assembled_recipe", "quality", "success", "reason")
            if k in o
        }
        for o in public.get("last_results", ())
    ]
    return {
        "agent": context.agent.id,
        "phase": context.phase,
        "step": context.step,
        "environment": public,
        "memory": context.agent.memory,
        "evidence": [{"id": e.id, "claim": e.claim} for e in observed_cards(context).values()],
        "messages": [
            {"id": m.id, "sender": m.sender, "content": m.content, "evidence_ids": [e.id for e in m.evidence]}
            for m in context.messages
        ],
        "artifacts": [
            {"id": a.id, "author": a.author, "content": a.content, "version": a.metadata["version"]}
            for a in context.artifacts
        ],
    }


class ModelScientist:
    """One provider call per turn; invalid actions abstain, never invoke a solving policy.

    The shared client/cache/audit are infrastructure, not private agent memory.
    Exact prompt matches reuse recorded responses in intervention replay. New
    contexts query the model and therefore do not eliminate provider randomness.
    """

    def __init__(self, client, *, protocol="targeted", directory, namespace, max_output_tokens=1024):
        if protocol not in PROTOCOLS:
            raise ValueError("unknown model protocol")
        self.client, self.protocol = client, protocol
        self.directory, self.namespace = Path(directory), namespace
        self.max_output_tokens = max_output_tokens
        self.directory.mkdir(parents=True, exist_ok=True)

    def __deepcopy__(self, memo):
        # All behavioral memory lives in AgentState. Never copy API gates or trace sinks.
        return self

    def prompt(self, context):
        visible = observation(context)
        visible["omitted"] = {"messages": 0, "artifacts": 0}
        prompt = [
            {"role": "system", "content": SYSTEM + "\nCommunication rule: " + PROTOCOLS[self.protocol]},
            {"role": "user", "content": encode(visible)},
        ]
        while len(encode(prompt).encode()) > 24000:
            field = "messages" if visible["messages"] else "artifacts"
            if not visible[field]:
                raise ValueError("private observation exceeds fixed context allowance")
            visible[field].pop(0)
            visible["omitted"][field] += 1
            prompt[1]["content"] = encode(visible)
        return prompt

    def parse(self, text, context):
        obj = json.loads(text)
        required = {"bid", "query", "preferences", "recipe", "publish", "forecast", "memory", "messages"}
        if not isinstance(obj, dict) or set(obj) != required:
            raise ValueError("expected exact action fields")
        encode(obj)
        if type(obj["bid"]) not in (int, float) or not math.isfinite(obj["bid"]) or obj["bid"] < 0:
            raise ValueError("invalid bid")
        if obj["query"] is not None and obj["query"] not in context.task.metadata["queries"]:
            raise ValueError("invalid research query")
        if (
            not isinstance(obj["recipe"], list)
            or len(obj["recipe"]) != 3
            or any(
                type(i) is not int or not 0 <= i < context.task.metadata["components"] for i in obj["recipe"]
            )
        ):
            raise ValueError("invalid recipe")
        if type(obj["publish"]) is not bool:
            raise ValueError("invalid publication")
        f = obj["forecast"]
        if f is not None and (type(f) not in (int, float) or not math.isfinite(f) or not 0 <= f <= 1):
            raise ValueError("invalid forecast")
        if not isinstance(obj["memory"], str) or len(obj["memory"]) > 800:
            raise ValueError("invalid memory")
        members = context.task.metadata["members"]
        role = context.agent.id.split(".")[1]
        targets = ("power", "firmware") if role == "sensor" else ("sensor",)
        prefs = obj["preferences"]
        if not isinstance(prefs, dict) or set(prefs) != set(targets):
            raise ValueError("invalid preference roles")
        for target, names in prefs.items():
            if not isinstance(names, list) or any(not isinstance(n, str) for n in names):
                raise ValueError("invalid partner IDs")
            if len(set(names)) != len(names) or any(
                n not in members or not n.endswith("." + target) for n in names
            ):
                raise ValueError("invalid partners")
        cards = observed_cards(context)
        artifacts = {a.id for a in context.artifacts}
        raw = obj["messages"]
        if not isinstance(raw, list) or len(raw) > 1:
            raise ValueError("at most one message allowed")
        messages = []
        for m in raw:
            if (
                not isinstance(m, dict)
                or not {"recipients", "content", "evidence_ids"} <= set(m)
                or not set(m) <= {"recipients", "content", "evidence_ids", "id", "sender"}
            ):
                raise ValueError("invalid message fields")
            if "sender" in m and m["sender"] != context.agent.id:
                raise ValueError("spoofed sender")
            recipients, ids = m["recipients"], m["evidence_ids"]
            if not isinstance(recipients, list) or any(
                not isinstance(r, str) or r not in members or r == context.agent.id for r in recipients
            ):
                raise ValueError("invalid recipients")
            if self.protocol == "broadcast" and recipients:
                raise ValueError("broadcast requires empty recipient list")
            if self.protocol != "broadcast" and not recipients:
                raise ValueError("direct message requires recipients")
            if (
                self.protocol == "coordinator"
                and context.agent.id != "firm0.sensor"
                and recipients != ["firm0.sensor"]
            ):
                raise ValueError("message must go through hub")
            if not isinstance(m["content"], str) or len(m["content"]) > 800:
                raise ValueError("invalid message text")
            if (
                not isinstance(ids, list)
                or len(ids) > 12
                or any(not isinstance(i, str) or (i not in cards and i not in artifacts) for i in ids)
            ):
                raise ValueError("unobserved evidence citation")
            messages.append(
                Message(
                    context.agent.id,
                    m["content"],
                    tuple(recipients),
                    evidence=tuple(cards[i] for i in ids if i in cards),
                    metadata={"artifact_ids": [i for i in ids if i in artifacts]},
                )
            )
        return AgentOutput(
            messages=tuple(messages),
            decision=Decision(
                context.agent.id,
                encode(obj["recipe"]),
                metadata={k: obj[k] for k in ("bid", "query", "preferences", "publish", "forecast")},
            ),
            memory_updates={"notes": obj["memory"]},
        )

    async def act(self, context):
        prompt = self.prompt(context)
        fingerprint = hashlib.sha256(
            encode(
                {"prompt": prompt, "model": self.client.model, "max_output_tokens": self.max_output_tokens}
            ).encode()
        ).hexdigest()
        path = self.directory / (
            hashlib.sha256(self.namespace.encode()).hexdigest()[:16] + "-" + fingerprint + ".json"
        )
        cached = path.exists()
        if cached:
            record = json.loads(path.read_text())
        else:
            result = await self.client.complete(
                prompt,
                max_output_tokens=self.max_output_tokens,
                temperature=0,
                thinking=False,
                json_mode=True,
            )
            record = {
                "fingerprint": fingerprint,
                "namespace": self.namespace,
                "agent": context.agent.id,
                "step": context.step,
                "protocol": self.protocol,
                "prompt": prompt,
                "response": result.text,
                "response_model": result.response_model,
                "request_id": result.request_id,
                "usage": asdict(result.usage),
                "input_tokens": result.input_tokens,
                "output_tokens": result.output_tokens,
                "finish_reason": result.finish_reason,
                "recorded_at": time.time(),
            }
        error = None
        try:
            if record["finish_reason"] != "stop":
                raise ValueError("nonterminal or truncated response")
            output = self.parse(record["response"], context)
        except (ValueError, TypeError, KeyError) as exc:
            error = str(exc)
            role = context.agent.id.split(".")[1]
            prefs = {r: [] for r in (("power", "firmware") if role == "sensor" else ("sensor",))}
            output = AgentOutput(
                decision=Decision(
                    context.agent.id,
                    "[0,0,0]",
                    metadata={
                        "bid": 1e6,
                        "query": None,
                        "preferences": prefs,
                        "publish": False,
                        "forecast": None,
                    },
                ),
                memory_updates={"protocol_error": "Previous action rejected: " + error},
            )
        record["protocol_error"] = error
        if not cached:
            temp = path.with_suffix(".tmp")
            temp.write_text(encode(record) + "\n")
            temp.replace(path)
        output = replace(output, usage=Usage(**record["usage"]))
        output.decision.metadata.update(
            {
                "model_audit": {
                    "fingerprint": fingerprint,
                    "cached": cached,
                    "protocol_error": error,
                    "input_tokens": record["input_tokens"],
                    "output_tokens": record["output_tokens"],
                    "response_model": record["response_model"],
                    "request_id": record["request_id"],
                }
            }
        )
        return output
