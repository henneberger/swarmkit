"""Research Foundry: private discovery, communication, procurement and verified work."""

from __future__ import annotations

import asyncio
import copy
import inspect
import itertools
import json
import math
import time
from dataclasses import asdict, dataclass, field, replace

from ..benchmarks.communication import ChannelConfig, Delivery, wire_bytes
from ..economics import (
    CombinatorialAuction,
    ContractNet,
    CoreDiagnostic,
    DeferredAcceptance,
    EconomicHyperedge,
    FirstPriceAuction,
    Ledger,
    LMSRMarket,
    SecondPriceAuction,
    Settlement,
    ShapleyEstimator,
    ThresholdTeamGame,
    VCGPayments,
)
from ..evaluation import hyperedge_irreducibility, interaction_reciprocity, population_diversity
from ..knowledge import ArtifactStore, CulturalTransfer, DecayingMemory
from ..runtime import MessageBus
from ..scheduling import DAGExecutor, critical_path
from ..social import TrustNetwork
from ..topology import CapabilitySuccessRouter, FullTopology, HypergraphTopology, RingTopology, StarTopology
from ..types import (
    AgentContext,
    AgentOutput,
    AgentState,
    AlgorithmResult,
    Artifact,
    Budget,
    Feedback,
    SwarmState,
    Task,
)
from .policies import FoundryScientist
from .world import ROLES, FoundryWorld, keyed


@dataclass(frozen=True)
class FoundryConfig:
    communication: str = "targeted"
    incentives: str = "shared"
    rounds: int = 5
    channel: ChannelConfig = field(default_factory=lambda: ChannelConfig(max_messages=48))
    topology: str = "full"
    artifacts: bool = True
    team_selection: str = "cost"
    forecast_market: bool = False
    pooled: bool = False
    research_budget: int = 24  # per generation
    production_budget: int = 16  # stage dispatches per generation
    equipment_slots: int = 2
    material_units: int | None = None  # episode supply per component specialty
    equipment_failure: float = 0.0
    turnover: float = 0.25
    memory_half_life: float = 2.0  # generations
    memory_threshold: float = 0.2
    max_cards: int = 12
    institution: str = "contract"  # contract, first_price, second_price, vcg priority slots
    checkpoint: bool = False
    trust_reported_usage: bool = False
    agent_concurrency: int = 1
    agent_teams: bool = False
    agent_publication: bool = False
    artifact_visibility: str = "incentives"

    def __post_init__(self):
        if type(self.agent_concurrency) is not int or self.agent_concurrency < 1:
            raise ValueError("agent_concurrency must be a positive integer")
        if self.agent_teams and self.rounds < 3:
            raise ValueError("agent-selected teams need bid, contract and commit rounds")
        if self.artifact_visibility not in ("incentives", "public", "firm"):
            raise ValueError("invalid artifact visibility")
        if self.communication not in ("none", "broadcast", "request", "targeted", "gated"):
            raise ValueError("unknown communication strategy")
        if self.incentives not in ("shared", "private") or self.topology not in (
            "full",
            "ring",
            "star",
            "hypergraph",
        ):
            raise ValueError("unknown incentives/topology")
        if self.team_selection not in ("cost", "matching", "routing"):
            raise ValueError("unknown team selection rule")
        if self.institution not in ("contract", "first_price", "second_price", "vcg"):
            raise ValueError("unknown allocation institution")
        if self.material_units is not None and (
            type(self.material_units) is not int or self.material_units < 0
        ):
            raise ValueError("material_units must be a nonnegative integer or None")
        for name in ("rounds", "research_budget", "production_budget", "equipment_slots", "max_cards"):
            v = getattr(self, name)
            if type(v) is not int or v < (1 if name in ("rounds", "equipment_slots", "max_cards") else 0):
                raise ValueError(f"invalid {name}")
        if not all(math.isfinite(p) and 0 <= p <= 1 for p in (self.turnover, self.equipment_failure)):
            raise ValueError("turnover and failure rates must be probabilities")
        if (
            not math.isfinite(self.memory_half_life)
            or self.memory_half_life <= 0
            or not 0 < self.memory_threshold <= 1
        ):
            raise ValueError("invalid memory retention")


@dataclass(frozen=True)
class DeviceVerifier:
    world: FoundryWorld

    def __call__(self, artifact):
        try:
            generation = artifact.metadata["generation"]
            orders = {o["id"]: o for o in self.world.orders(generation)}
            order = orders[artifact.metadata["task_id"]]
            recipe = artifact.content["recipe"]
            result = self.world.verify(generation, recipe, artifact.metadata["completion"], order)
            valid = result["success"] and result["quality"] == artifact.content["quality"]
            valid &= artifact.metadata["version"] == self.world.version(generation)
            return Feedback(float(result["quality"]), verified=valid)
        except (KeyError, TypeError, ValueError):
            return Feedback(0, verified=False)


@dataclass
class FoundryCheckpoint:
    world_id: str
    seed: int
    config: FoundryConfig
    tick: int
    data: dict = field(repr=False)


@dataclass
class FoundryRun:
    world_id: str
    seed: int
    config: FoundryConfig
    metrics: dict
    outcomes: list
    deliveries: list
    events: list
    artifacts: list
    checkpoints: dict = field(repr=False)

    def report(self, traces=True):
        result = {
            "world_id": self.world_id,
            "seed": self.seed,
            "config": asdict(self.config),
            "metrics": self.metrics,
            "outcomes": self.outcomes,
            "artifacts": self.artifacts,
        }
        if traces:
            result.update(deliveries=[asdict(d) for d in self.deliveries], events=self.events)
        return result


class FoundryExperiment:
    """An isolated local simulator using canonical agent callbacks.

    External tools/model state remain caller-owned. Checkpoints copy local agent
    objects and simulator state; custom callbacks must be replayable for causal use.
    Sealed bids, direct messages, artifact reads and physical actions are distinct.
    """

    def __init__(self, world=None, config=None):
        self.world, self.config = world or FoundryWorld(), config or FoundryConfig()

    def population(self):
        return {
            a: FoundryScientist(self.config.communication, self.config.incentives, self.config.max_cards)
            for a in self.world.agents
        }

    def _authorized_artifact(self, agent, artifact):
        public = self.config.artifact_visibility == "public" or (
            self.config.artifact_visibility == "incentives" and self.config.incentives == "shared"
        )
        return public or agent.split(".")[0] == artifact.author.split(".")[0]

    def _initial(self, agents, seed):
        material_supply = (
            self.world.firms * self.world.generations
            if self.config.material_units is None
            else self.config.material_units
        )
        ledger = Ledger(
            {a: 100.0 for a in self.world.agents}
            | {"customer": 10000.0, "equipment": 0.0, "warehouse": 0.0, "used_material": 0.0},
            {"warehouse": {role: material_supply for role in ROLES}},
        )
        return {
            "state": SwarmState(
                {a: AgentState(a, capabilities=frozenset([a.split(".")[1]])) for a in self.world.agents},
                seed=seed,
            ),
            "agents": copy.deepcopy(agents),
            "prototypes": copy.deepcopy(agents),
            "ledger": ledger,
            "contracts": ContractNet(ledger),
            "store": ArtifactStore(DeviceVerifier(self.world)),
            "memory": DecayingMemory(self.config.memory_half_life, self.config.memory_threshold),
            "trust": TrustNetwork(),
            "pending": [],
            "deliveries": [],
            "events": [],
            "outcomes": [],
            "decisions": {},
            "exposure": {},
            "bids": {},
            "research_counts": {},
            "started": -1,
            "stats": {
                "agent_calls": 0,
                "tokens": 0 if self.config.trust_reported_usage else None,
                "model_cost": 0.0 if self.config.trust_reported_usage else None,
                "research_calls": 0,
                "verification_cost": 0,
                "duplicate_experiments": 0,
                "production_calls": 0,
                "generated_bytes": 0,
                "generated_messages": 0,
                "delivered_bytes": 0,
                "receiver_input_bytes": 0,
                "artifact_read_bytes": 0,
                "artifact_reads": 0,
                "equipment_payments": 0.0,
                "turnovers": 0,
                "protocol_errors": 0,
            },
            "real_costs": dict.fromkeys(self.world.agents, 0.0),
            "memberships": [],
            "markets": {},
            "router": CapabilitySuccessRouter(exploration=0),
            "incarnations": dict.fromkeys(self.world.agents, 0),
        }

    def _begin(self, data, generation, seed):
        world, cfg, state = self.world, self.config, data["state"]
        version = world.version(generation)
        data["generation_balances"] = {a: data["ledger"].balances[a] for a in world.agents}
        data["generation_costs"] = dict(data["real_costs"])
        data["generation_verification_cost"] = data["stats"]["verification_cost"]
        replacements = []
        for a in world.agents:
            if generation and keyed(seed, world.id, "turnover", generation, a) < cfg.turnover:
                data["agents"][a] = copy.deepcopy(data["prototypes"][a])
                data["incarnations"][a] += 1
                state.agents[a] = AgentState(a, capabilities=frozenset([a.split(".")[1]]))
                replacements.append(a)
            if generation == 0:
                state.agents[a].private_evidence = world.private(a, version)
            elif world.version(generation - 1) != version:
                # Changed physics requires new investigation; announce version, never new values.
                state.agents[a].private_evidence = ()
                state.agents[a].inbox = []
                state.agents[a].memory = {}
            if cfg.pooled:
                state.agents[a].private_evidence = tuple(world.card(version, q) for q in world.topics())
        data["stats"]["turnovers"] += len(replacements)
        data["events"].append(
            {
                "channel": "environment",
                "kind": "generation",
                "generation": generation,
                "version": version,
                "replacements": replacements,
            }
        )
        data["started"], data["bids"], data["decisions"], data["exposure"] = generation, {}, {}, {}
        data["preferences"], data["assignments"] = {}, {}
        data["message_count"], data["message_bytes"], data["research_used"] = 0, 0, 0
        data["memory"]._advance(generation)
        visible_ids = {a.id for a in data["memory"].available(generation)} if cfg.artifacts else set()

        def transfer_evaluator(agent, artifact, task):
            authorized = self._authorized_artifact(agent.id, artifact)
            valid = authorized and artifact.id in visible_ids and artifact.metadata["version"] == version
            return Feedback(float(artifact.score or 0), verified=valid)

        transfer = CulturalTransfer(data["store"], transfer_evaluator).step(
            state, Task(f"transfer:{generation}", "inherit recipes")
        )
        data["events"].append(
            {
                "channel": "artifact",
                "kind": "transfer",
                "generation": generation,
                "adoptions": transfer.metadata["transfers"],
            }
        )
        if cfg.forecast_market:
            for order in world.orders(generation):
                maker = "market:" + order["id"]
                data["ledger"].balances[maker] = 0.0
                data["ledger"].settle(Settlement("fund:" + maker, {"customer": -2.0, maker: 2.0}))
                data["markets"][order["id"]] = LMSRMarket(2, liquidity=2, maker=maker)

    def _topology(self):
        cfg, world = self.config, self.world
        if cfg.topology == "full":
            return FullTopology()
        if cfg.topology == "ring":
            return RingTopology()
        if cfg.topology == "star":
            return StarTopology(world.agents[0])
        groups = tuple(
            frozenset(a for a in world.agents if a.split(".")[0] == f"firm{f}") for f in range(world.firms)
        )
        groups += tuple(frozenset(a for a in world.agents if a.endswith("." + role)) for role in ROLES)
        return HypergraphTopology(groups)

    def _deliver(self, data, tick, suppressed, replacements):
        pending, data["pending"] = (
            [p for p in data["pending"] if p[0] <= tick],
            [p for p in data["pending"] if p[0] > tick],
        )
        for due, original in pending:
            message = original
            if message.id in replacements:
                message = replace(message, content=replacements[message.id], evidence=(), metadata={})
            recipients = () if message.id in suppressed else MessageBus().publish(data["state"], message)
            for recipient in original.recipients:
                delivered = recipient in recipients
                data["deliveries"].append(
                    Delivery(
                        original.id,
                        original.sender,
                        recipient,
                        original.step,
                        due,
                        "delivered" if delivered else "suppressed",
                        wire_bytes(message),
                        tuple(e.id for e in message.evidence),
                    )
                )
                if delivered:
                    data["stats"]["delivered_bytes"] += wire_bytes(message)

    def _contexts(self, data, generation, round_index):
        world, cfg, state = self.world, self.config, data["state"]
        version = world.version(generation)
        available = data["memory"].available(generation) if cfg.artifacts else ()
        # Archive visibility is explicit. Old-version recipes remain visible but are labeled stale.
        contexts = {}
        for a in world.agents:
            visible = tuple(art for art in available if self._authorized_artifact(a, art))
            data["stats"]["artifact_reads"] += len(visible)
            data["stats"]["artifact_read_bytes"] += sum(
                len(json.dumps(asdict(art), sort_keys=True, default=sorted).encode()) for art in visible
            )
            if visible:
                data["events"].append(
                    {
                        "channel": "artifact",
                        "kind": "read",
                        "tick": state.step,
                        "agent": a,
                        "artifacts": [art.id for art in visible],
                    }
                )
            public = {
                "generation": generation,
                "total_generations": world.generations,
                "rounds": cfg.rounds,
                "agent_teams": cfg.agent_teams,
                "agent_publication": cfg.agent_publication,
                "artifact_visibility": cfg.artifact_visibility,
                "round": round_index,
                "version": version,
                "members": world.agents,
                "components": world.components,
                "orders": world.orders(generation),
                "own_cost": world.cost(a),
                "feedback": copy.deepcopy(data.get("last_feedback", {}).get(a)),
                "last_results": [
                    copy.deepcopy(o)
                    for o in data["outcomes"]
                    if o["generation"] == generation - 1
                    and a in o.get("team", ())
                    and o.get("tested", False)
                    and o.get("team_incarnations", {}).get(a) == data["incarnations"][a]
                ],
                "own_balance": data["ledger"].available(a),
                "queries": tuple(q for q in world.topics() if world.topic_role(q) == a.split(".")[1]),
                "procurement": copy.deepcopy(data["bids"]),
                "assignments": copy.deepcopy(data.get("assignments", {})),
                "incentives": cfg.incentives,
                "forecast_prices": {
                    o["id"]: data["markets"][o["id"]].prices().tolist()
                    for o in world.orders(generation)
                    if o["id"] in data["markets"]
                },
                "trust": {b: data["trust"].direct(a, b, "delivery") for b in world.agents if b != a},
            }
            contexts[a] = AgentContext(
                Task("foundry", "Discover, contract and build a device meeting its order.", metadata=public),
                copy.deepcopy(state.agents[a]),
                tuple(copy.deepcopy(state.agents[a].inbox)),
                copy.deepcopy(visible),
                "commit"
                if round_index == cfg.rounds - 1
                else ("contract" if cfg.agent_teams and round_index == 1 else "research"),
                state.step,
            )
            data["stats"]["receiver_input_bytes"] += sum(wire_bytes(m) for m in contexts[a].messages)
        return contexts

    def _validate(self, agent, output, context):
        if not isinstance(output, AgentOutput) or output.artifacts:
            raise ValueError("Foundry requires AgentOutput; artifacts are created only by verified builds")
        if output.decision is None or output.decision.agent_id != agent:
            raise ValueError("each turn requires an identified decision with bid/query metadata")
        bid = output.decision.metadata.get("bid")
        if isinstance(bid, bool) or not isinstance(bid, (int, float)) or not math.isfinite(bid) or bid < 0:
            raise ValueError("bid must be finite and nonnegative")
        query = output.decision.metadata.get("query")
        if query is not None and query not in context.task.metadata["queries"]:
            raise ValueError("experiment requires a legal specialty-specific topic")
        probability = output.decision.metadata.get("forecast")
        if probability is not None and (
            not isinstance(probability, (int, float))
            or not math.isfinite(probability)
            or not 0 <= probability <= 1
        ):
            raise ValueError("forecast must be a probability")
        if context.phase == "commit":
            self.world.validate_recipe(json.loads(output.decision.answer))
            if self.config.agent_publication and type(output.decision.metadata.get("publish")) is not bool:
                raise ValueError("commit requires a boolean publication decision")
        if self.config.agent_teams and context.phase == "contract":
            prefs = output.decision.metadata.get("preferences")
            if not isinstance(prefs, dict):
                raise ValueError("contract requires partner preferences")
            role = agent.split(".")[1]
            targets = ("power", "firmware") if role == "sensor" else ("sensor",)
            if set(prefs) != set(targets):
                raise ValueError("preferences must name complementary roles")
            for target, members in prefs.items():
                if not isinstance(members, list) or any(not isinstance(m, str) for m in members):
                    raise ValueError("preferences must contain agent identifiers")
                if len(set(members)) != len(members) or any(
                    m not in self.world.agents or not m.endswith("." + target) for m in members
                ):
                    raise ValueError("invalid partner preferences")
        for message in output.messages:
            if message.sender != agent or any(r not in self.world.agents for r in message.recipients):
                raise ValueError("spoofed message sender or unknown recipient")
            if not isinstance(message.content, str):
                raise ValueError("message content must be text")
            try:
                json.dumps(asdict(message), allow_nan=False)
            except (TypeError, ValueError) as exc:
                raise ValueError("Foundry messages must have finite JSON-serializable payloads") from exc
            # Structured simulator measurements cannot be forged or read from an unseen oracle.
            exposed = {
                e.id: e
                for e in (*context.agent.private_evidence, *(e for m in context.messages for e in m.evidence))
            }
            if any(e.id not in exposed or exposed[e.id] != e for e in message.evidence):
                raise ValueError("message cites an unobserved or altered measurement")

    def _send(self, data, message, tick, seed):
        cfg, world = self.config, self.world
        size = wire_bytes(message)
        data["events"].append(
            {"channel": "message", "kind": "send", "tick": tick, "message": asdict(message)}
        )
        data["stats"]["generated_messages"] += 1
        data["stats"]["generated_bytes"] += size
        masked = SwarmState(
            {a: AgentState(a, capabilities=data["state"].agents[a].capabilities) for a in world.agents},
            seed=seed,
        )
        allowed = set(self._topology().neighbors(masked, message.sender))
        requested = tuple(
            dict.fromkeys(r for r in (message.recipients or world.agents) if r != message.sender)
        )
        reason = None
        if cfg.channel.disabled:
            reason = "disabled"
        elif cfg.channel.max_messages is not None and data["message_count"] >= cfg.channel.max_messages:
            reason = "budget"
        elif cfg.channel.max_bytes is not None and data["message_bytes"] + size > cfg.channel.max_bytes:
            reason = "budget"
        if reason is None:
            data["message_count"] += 1
            data["message_bytes"] += size
        due = tick + 1 + cfg.channel.delay
        recipients = []
        for recipient in requested:
            status = reason or ("topology" if recipient not in allowed else None)
            if not status and keyed(seed, world.id, "loss", message.id, recipient) < cfg.channel.loss:
                status = "lost"
            if status:
                data["deliveries"].append(
                    Delivery(
                        message.id,
                        message.sender,
                        recipient,
                        tick,
                        due,
                        status,
                        size,
                        tuple(e.id for e in message.evidence),
                    )
                )
            else:
                recipients.append(recipient)
        if recipients:
            data["pending"].append((due, replace(message, recipients=tuple(recipients))))
            duplicate_recipients = tuple(
                r for r in recipients if keyed(seed, world.id, "dup", message.id, r) < cfg.channel.duplicate
            )
            if duplicate_recipients:
                data["pending"].append(
                    (due, replace(message, id=message.id + ":duplicate", recipients=duplicate_recipients))
                )

    def _apply(self, data, contexts, outputs, tick, seed):
        cfg, world, state = self.config, self.world, data["state"]
        generation, round_index = divmod(tick, cfg.rounds)
        for a, output in outputs.items():
            audit = output.decision.metadata.get("model_audit")
            if audit:
                data["events"].append(
                    {"channel": "model", "kind": "decision", "tick": tick, "agent": a, **copy.deepcopy(audit)}
                )
                data["stats"]["protocol_errors"] += int(audit.get("protocol_error") is not None)
            state.agents[a].memory.update(copy.deepcopy(output.memory_updates))
            if round_index == 0:
                data["bids"][a] = float(output.decision.metadata["bid"])
            if cfg.agent_teams and round_index == 1:
                data["preferences"][a] = copy.deepcopy(output.decision.metadata["preferences"])
            if round_index == cfg.rounds - 1:
                data["decisions"][a] = output.decision
                data["events"].append(
                    {
                        "channel": "environment",
                        "kind": "commit",
                        "tick": tick,
                        "agent": a,
                        "recipe": json.loads(output.decision.answer),
                        "cited_evidence": list(output.decision.evidence_ids),
                    }
                )
                data["exposure"][a] = tuple(
                    {e.id for e in contexts[a].agent.private_evidence}
                    | {e.id for m in contexts[a].messages for e in m.evidence}
                )
            for index, message in enumerate(output.messages):
                self._send(data, replace(message, step=tick, id=f"{tick}:{a}:{index}"), tick, seed)
        if cfg.forecast_market and round_index < cfg.rounds - 1:
            for a, output in outputs.items():
                forecast = output.decision.metadata.get("forecast")
                if forecast is None:
                    continue
                oid = f"order:{generation}:{int(a.split('.')[0][4:])}"
                delta = [0.0, 0.0]
                delta[int(forecast >= 0.5)] = 0.25
                try:
                    data["markets"][oid].trade(data["ledger"], f"{tick}:{a}", a, delta)
                except ValueError:
                    continue  # An unfunded forecast cannot create a position.
                data["events"].append(
                    {
                        "channel": "procurement",
                        "kind": "forecast_trade",
                        "tick": tick,
                        "agent": a,
                        "order": oid,
                        "prices": data["markets"][oid].prices().tolist(),
                    }
                )
        if round_index == 0:
            data["events"].append(
                {
                    "channel": "procurement",
                    "kind": "bid_reveal",
                    "generation": generation,
                    "bids": copy.deepcopy(data["bids"]),
                }
            )
        # Paired, keyed dispatch ordering prevents a fixed agent-ID priority advantage.
        for a in sorted(outputs, key=lambda a: keyed(seed, world.id, "dispatch", tick, a)):
            query = outputs[a].decision.metadata.get("query")
            if query is None or round_index == cfg.rounds - 1:
                continue
            if data["research_used"] >= cfg.research_budget:
                continue
            data["research_used"] += 1
            key = (world.version(generation), query)
            count = data["research_counts"].get(key, 0)
            data["stats"]["duplicate_experiments"] += int(count > 0)
            data["research_counts"][key] = count + 1
            data["stats"]["research_calls"] += 1
            data["real_costs"][a] += 1
            evidence = world.card(world.version(generation), query)
            current = {e.id: e for e in state.agents[a].private_evidence}
            current[evidence.id] = evidence
            state.agents[a].private_evidence = tuple(current.values())
            data["events"].append(
                {
                    "channel": "environment",
                    "kind": "experiment",
                    "tick": tick,
                    "agent": a,
                    "topic": query,
                    "duplicate": count > 0,
                }
            )

    def _award(self, data, generation):
        world = self.world
        data["assignments"] = {}
        matches = {}
        coordinators = [o["coordinator"] for o in world.orders(generation)]
        if self.config.team_selection == "matching" or self.config.agent_teams:
            for role in ("power", "firmware"):
                candidates = [a for a in world.agents if a.endswith("." + role)]
                matches[role] = DeferredAcceptance().clear(
                    {
                        c: data["preferences"][c][role]
                        if self.config.agent_teams
                        else sorted(candidates, key=lambda a: (data["bids"][a], a))
                        for c in coordinators
                    },
                    {
                        a: data["preferences"][a]["sensor"]
                        if self.config.agent_teams
                        else sorted(coordinators)
                        for a in candidates
                    },
                )
        for order in world.orders(generation):
            coordinator = order["coordinator"]
            offers = {}
            chosen = {}
            if self.config.team_selection == "routing":
                for role in ("power", "firmware"):
                    chosen[role] = data["router"].route(data["state"], coordinator, frozenset([role]))
            for power, firmware in itertools.product(
                [a for a in world.agents if a.endswith(".power")],
                [a for a in world.agents if a.endswith(".firmware")],
            ):
                if (self.config.team_selection == "matching" or self.config.agent_teams) and (
                    power != matches["power"].get(coordinator)
                    or firmware != matches["firmware"].get(coordinator)
                ):
                    continue
                if chosen and (power != chosen["power"] or firmware != chosen["firmware"]):
                    continue
                team = (coordinator, power, firmware)
                cost = 3 * max(data["bids"][a] for a in team)  # equal payout covers every reported ask
                if cost <= order["budget"]:
                    offers["|".join(team)] = {"members": team, "capabilities": ROLES, "cost": cost}
            award = data["contracts"].award(order["id"], order["id"], "customer", ROLES, offers)
            if award:
                data["assignments"][order["id"]] = award["members"]
                edge = EconomicHyperedge(
                    order["id"],
                    award["members"],
                    "contract_net",
                    {a: a.split(".")[1] for a in award["members"]},
                )
                data["memberships"].append(edge)
                data["events"].append(
                    {
                        "channel": "procurement",
                        "kind": "award",
                        "generation": generation,
                        "order": order["id"],
                        "members": award["members"],
                        "cost": award["cost"],
                    }
                )

    def _priority(self, data, orders):
        from ..economics import Settlement

        cfg = self.config
        ready = [o for o in orders if o["id"] in data["assignments"]]
        if cfg.institution == "contract" or not ready:
            return ready
        bids = {
            o["coordinator"]: min(o["value"] / 5, data["ledger"].available(o["coordinator"])) for o in ready
        }
        if cfg.institution == "vcg":
            result = VCGPayments(CombinatorialAuction(["priority"])).clear(
                {a: {("priority",): v} for a, v in bids.items()}
            )
            winners = set(result["allocation"])
            payments = {a: p for a, p in result["payments"].items() if a in winners}
        else:
            mechanism = FirstPriceAuction() if cfg.institution == "first_price" else SecondPriceAuction()
            result = mechanism.clear(bids)
            winners, payments = {result["winner"]}, {result["winner"]: result["payment"]}
        for a, price in payments.items():
            data["ledger"].settle(
                Settlement("priority:" + ready[0]["id"] + ":" + a, {a: -price, "equipment": price})
            )
            data["stats"]["equipment_payments"] += price
        data["events"].append({"channel": "procurement", "kind": "priority_auction", "payments": payments})
        return sorted(ready, key=lambda o: (o["coordinator"] not in winners, o["id"]))

    async def _produce(self, data, generation, seed):
        world, cfg = self.world, self.config
        orders = world.orders(generation)
        ranked = self._priority(data, orders)
        durations, dependencies, finishes, resources, benches = {}, {}, {}, {}, [None] * cfg.equipment_slots
        jobs, actual, planned, task_owners = [], {}, {}, {}
        for order in ranked:
            oid, team = order["id"], data["assignments"][order["id"]]
            planned[oid] = json.loads(data["decisions"][order["coordinator"]].answer)
            actual[oid] = [json.loads(data["decisions"][a].answer)[i] for i, a in enumerate(team)]
            for stage, worker, duration, deps in (
                ("sensor", team[0], 2, ()),
                ("power", team[1], 2, ()),
                ("assemble", team[2], 2, (oid + ":sensor", oid + ":power")),
                ("verify", None, 1, (oid + ":assemble",)),
            ):
                tid = oid + ":" + stage
                prerequisites = list(deps)
                if worker in resources:
                    prerequisites.append(resources[worker])
                bench = None
                if stage in ("assemble", "verify"):
                    bench = min(range(len(benches)), key=lambda i: finishes.get(benches[i], 0))
                    if benches[bench]:
                        prerequisites.append(benches[bench])
                dependencies[tid] = tuple(dict.fromkeys(prerequisites))
                durations[tid] = duration
                finishes[tid] = duration + max((finishes[d] for d in dependencies[tid]), default=0)
                if worker:
                    resources[worker] = tid
                if bench is not None:
                    benches[bench] = tid
                task_owners[tid] = worker
                jobs.append(
                    Task(tid, f"{stage} device", metadata={"depends_on": dependencies[tid], "stage": stage})
                )
        # Resource-order edges constrain start times; they do not require another order to succeed.
        # Worker failures are represented as outcomes, so resource edges remain releasable.
        physical_success = {}

        async def worker(task):
            owner = task_owners[task.id]
            data["stats"]["production_calls"] += 1
            if owner:
                data["real_costs"][owner] += world.cost(owner)
            else:
                data["stats"]["verification_cost"] += 1
            stage = task.metadata["stage"]
            oid = task.id.rsplit(":", 1)[0]
            own_dependencies = [d for d in dependencies[task.id] if d.startswith(oid + ":")]
            passed = all(physical_success.get(d, False) for d in own_dependencies)
            failed = keyed(seed, world.id, "equipment_failure", generation, task.id) < cfg.equipment_failure
            material_available = True
            if owner and passed:
                role = owner.split(".")[1]
                try:
                    data["ledger"].settle(
                        Settlement(
                            "material:" + task.id,
                            {},
                            inventory={"warehouse": {role: -1}, "used_material": {role: 1}},
                        )
                    )
                except ValueError:
                    material_available = False
            physical_success[task.id] = passed and not failed and material_available
            data["events"].append(
                {
                    "channel": "environment",
                    "kind": "production",
                    "generation": generation,
                    "task": task.id,
                    "worker": owner,
                    "stage": stage,
                    "completion": finishes[task.id],
                    "passed": physical_success[task.id],
                }
            )
            return AlgorithmResult(metadata={"passed": physical_success[task.id]})

        execution = await DAGExecutor(
            worker, concurrency=cfg.equipment_slots, budget=Budget(max_calls=cfg.production_budget)
        ).run(jobs)
        for order in orders:
            oid, coordinator = order["id"], order["coordinator"]
            team = data["assignments"].get(oid, ())
            if not team:
                data["outcomes"].append(
                    {
                        "order": oid,
                        "generation": generation,
                        "success": False,
                        "reason": "no_affordable_team",
                        "accepted_value": 0.0,
                    }
                )
                continue
            last = oid + ":verify"
            ran = physical_success.get(last, False)
            invalid_commitment = any(
                data["decisions"][a].metadata.get("model_audit", {}).get("protocol_error") for a in team
            )
            result = world.verify(generation, actual[oid], finishes[last], order)
            # A parser fallback is not a valid commitment, even if index zero
            # accidentally assembles a physically acceptable device.
            result["success"] &= ran and not invalid_commitment
            card_ids = world.required(world.version(generation), planned[oid])
            exposed = set(data["exposure"][coordinator])
            coverage = len(exposed & set(card_ids)) / len(card_ids)
            taskgame = ThresholdTeamGame(
                {a: [a.split(".")[1]] for a in team}, ROLES, order["value"], {a: world.cost(a) for a in team}
            )
            artifact = Artifact(
                "device:" + oid,
                coordinator if cfg.agent_publication else team[2],
                {"recipe": actual[oid], "quality": result["quality"]},
                metadata={
                    "generation": generation,
                    "version": world.version(generation),
                    "task_id": oid,
                    "contract_id": oid,
                    "completion": finishes[last],
                },
            )
            if result["success"]:
                publish = not cfg.agent_publication or data["decisions"][coordinator].metadata["publish"]
                if publish:
                    admitted = data["store"].admit(artifact)
                    data["memory"].write(admitted, generation)
                data["events"].append(
                    {
                        "channel": "artifact",
                        "kind": "publication",
                        "order": oid,
                        "generation": generation,
                        "published": publish,
                    }
                )
                data["contracts"].complete(oid, artifact, DeviceVerifier(world))
            else:
                data["contracts"].complete(oid, artifact, lambda a: Feedback(0, verified=False))
            for member in team:
                if member != coordinator:
                    data["trust"].observe(coordinator, member, "delivery", result["success"])
                    data["router"].record(data["state"], coordinator, member, float(result["success"]))
            reward = float(order["value"]) if result["success"] else 0.0

            def coalition_value(coalition, team=frozenset(team), reward=reward):
                return reward if team <= coalition else 0.0

            shares = ShapleyEstimator(team, coalition_value).estimate(exact=True)["values"]
            core = CoreDiagnostic().evaluate(team, coalition_value, shares)
            data["outcomes"].append(
                {
                    "order": oid,
                    "generation": generation,
                    **result,
                    "accepted_value": reward,
                    "tested": ran,
                    "invalid_commitment": invalid_commitment,
                    "version": world.version(generation),
                    "planned_recipe": planned[oid],
                    "assembled_recipe": actual[oid],
                    "commitment_match": actual[oid] == planned[oid],
                    "team": team,
                    "team_incarnations": {a: data["incarnations"][a] for a in team},
                    "completion": finishes[last],
                    "evidence_coverage": coverage,
                    "modeled_team_utilities": taskgame.utilities(team),
                    "modeled_shapley_value": shares,
                    "modeled_core_gap": core["max_blocking_gain"],
                    "reason": "accepted"
                    if result["success"]
                    else (
                        "invalid_commitment"
                        if invalid_commitment
                        else "execution_failed"
                        if not ran
                        else "late"
                        if not result["on_time"]
                        else "invalid_device"
                    ),
                }
            )
        period_value = sum(o["accepted_value"] for o in data["outcomes"] if o["generation"] == generation)
        period_cost = sum(data["real_costs"][a] - data["generation_costs"][a] for a in world.agents)
        period_cost += data["stats"]["verification_cost"] - data["generation_verification_cost"]
        if cfg.forecast_market:
            results = {o["order"]: o["success"] for o in data["outcomes"] if o["generation"] == generation}
            for order in orders:
                data["markets"][order["id"]].resolve(data["ledger"], int(results[order["id"]]))
        data["last_feedback"] = {
            a: {
                "utility": period_value - period_cost
                if cfg.incentives == "shared"
                else data["ledger"].balances[a]
                - data["generation_balances"][a]
                - (data["real_costs"][a] - data["generation_costs"][a]),
                "objective": cfg.incentives,
            }
            for a in world.agents
        }
        data["events"].append(
            {
                "channel": "environment",
                "kind": "schedule_summary",
                "generation": generation,
                "critical_path": critical_path(durations, dependencies),
                "total_planned_work": sum(durations.values()),
                "failed_jobs": execution.metrics["failed"],
            }
        )
        # No delayed information is allowed to cross generation/turnover boundaries implicitly.
        for due, message in data["pending"]:
            for recipient in message.recipients:
                data["deliveries"].append(
                    Delivery(
                        message.id,
                        message.sender,
                        recipient,
                        message.step,
                        due,
                        "late",
                        wire_bytes(message),
                        tuple(e.id for e in message.evidence),
                    )
                )
        data["pending"] = []

    async def run(self, agents=None, seed=0, *, checkpoint=None, suppress=(), replace_messages=None):
        population = self.population() if agents is None else agents
        if set(population) != set(self.world.agents):
            raise ValueError("one agent per world participant required")
        if type(seed) is not int or seed < 0:
            raise ValueError("nonnegative run seed required")
        if checkpoint is not None:
            if (
                checkpoint.world_id != self.world.id
                or checkpoint.seed != seed
                or checkpoint.config != self.config
            ):
                raise ValueError("checkpoint world, seed or configuration mismatch")
            data, start = copy.deepcopy(checkpoint.data), checkpoint.tick
        else:
            data, start = self._initial(population, seed), 0
        captured, started = {}, time.perf_counter()
        suppressed = set(suppress) | {s + ":duplicate" for s in suppress}
        replacements = replace_messages or {}
        replacements = dict(replacements) | {s + ":duplicate": v for s, v in replacements.items()}
        for tick in range(start, self.world.generations * self.config.rounds):
            generation, round_index = divmod(tick, self.config.rounds)
            data["state"].step = tick
            if data["started"] != generation:
                self._begin(data, generation, seed)
            if self.config.checkpoint:
                captured[tick] = FoundryCheckpoint(
                    self.world.id, seed, self.config, tick, copy.deepcopy(data)
                )
            if self.config.channel.reorder:
                data["pending"].sort(key=lambda p: keyed(seed, self.world.id, "order", tick, p[1].id))
            self._deliver(data, tick, suppressed, replacements)
            contexts = self._contexts(data, generation, round_index)
            # Concurrency changes wall time, never synchronous observation/action ordering.
            semaphore = asyncio.Semaphore(self.config.agent_concurrency)

            async def invoke(a, semaphore=semaphore, contexts=contexts):
                async with semaphore:
                    call = data["agents"][a].act(copy.deepcopy(contexts[a]))
                    output = await call if inspect.isawaitable(call) else call
                    self._validate(a, output, contexts[a])
                    return copy.deepcopy(output)

            results = await asyncio.gather(*(invoke(a) for a in self.world.agents), return_exceptions=True)
            failures = [r for r in results if isinstance(r, BaseException)]
            if failures:
                raise failures[0]
            outputs = dict(zip(self.world.agents, results, strict=True))
            for output in outputs.values():
                data["stats"]["agent_calls"] += 1
                if self.config.trust_reported_usage:
                    data["stats"]["tokens"] += output.usage.tokens
                    data["stats"]["model_cost"] += output.usage.cost
            self._apply(data, contexts, outputs, tick, seed)
            if round_index == (1 if self.config.agent_teams else 0):
                self._award(data, generation)
            if round_index == self.config.rounds - 1:
                await self._produce(data, generation, seed)
        stats = copy.deepcopy(data["stats"])
        stats.update(
            {
                "accepted_value": sum(o["accepted_value"] for o in data["outcomes"]),
                "success_rate": sum(o["success"] for o in data["outcomes"]) / len(data["outcomes"]),
                "real_execution_cost": sum(data["real_costs"].values()) + data["stats"]["verification_cost"],
                "balances": copy.deepcopy(data["ledger"].balances),
                "private_surplus": {
                    a: data["ledger"].balances[a] - 100 - data["real_costs"][a] for a in self.world.agents
                },
                "ledger_conservation_error": sum(data["ledger"].balances.values())
                - (10000 + 100 * len(self.world.agents)),
                "outstanding_reservations": len(data["ledger"].reservations),
                "remaining_materials": copy.deepcopy(data["ledger"].inventories["warehouse"]),
                "consumed_materials": copy.deepcopy(data["ledger"].inventories.get("used_material", {})),
                "reciprocity": interaction_reciprocity(data["state"].messages, self.world.agents),
                "hyperedge_structure_score": hyperedge_irreducibility(e.members for e in data["memberships"]),
                "design_diversity": population_diversity(
                    json.dumps(o.get("assembled_recipe")) for o in data["outcomes"]
                ),
                "elapsed_seconds": time.perf_counter() - started,
                "suffix_only_timing": checkpoint is not None,
            }
        )
        stats["shared_payoff"] = stats["accepted_value"] - stats["real_execution_cost"]
        return FoundryRun(
            self.world.id,
            seed,
            self.config,
            stats,
            data["outcomes"],
            data["deliveries"],
            data["events"],
            [json.loads(json.dumps(asdict(a), default=sorted)) for a in data["store"].active],
            captured,
        )

    async def replay_without(self, run, message_id):
        if not any(d.message_id == message_id for d in run.deliveries):
            raise ValueError("unknown attempted message")
        tick = int(message_id.split(":")[0])
        if tick not in run.checkpoints:
            raise ValueError("enable checkpoint=True before running the baseline")
        changed = await self.run(seed=run.seed, checkpoint=run.checkpoints[tick], suppress=(message_id,))
        return {
            "intervened": changed,
            "accepted_value_effect": run.metrics["accepted_value"] - changed.metrics["accepted_value"],
            "changed_orders": [
                old["order"]
                for old, new in zip(run.outcomes, changed.outcomes, strict=True)
                if old.get("assembled_recipe") != new.get("assembled_recipe")
            ],
        }
