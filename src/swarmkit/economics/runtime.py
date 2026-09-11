"""Sealed simultaneous rounds attached to persistent economic hyperedges."""

from __future__ import annotations

from copy import deepcopy

from .ledger import Ledger
from .types import EconomicObservation


class EconomicArena:
    """Mechanisms use registry IDs; snapshots contain no live callbacks.

    clear(edge, actions, ledger_copy) returns a Settlement. Actions are collected
    before clearing. Only declared public summaries enter later observations.
    Callbacks are trusted local code; copies provide logical, not OS isolation.
    """

    def __init__(self, edges, private_types, ledger, mechanisms):
        self.edges = {e.id: deepcopy(e) for e in edges}
        if len(self.edges) != len(edges):
            raise ValueError("duplicate edge ids")
        self.private_types = deepcopy(private_types)
        if any(not set(e.members) <= private_types.keys() or e.mechanism_id not in mechanisms for e in edges):
            raise ValueError("missing private types or registered mechanism")
        self.ledger, self.mechanisms = ledger, mechanisms
        self.rounds = dict.fromkeys(self.edges, 0)
        self.public = {e: {} for e in self.edges}
        self.history = []

    def observation(self, edge_id, agent_id):
        edge = self.edges[edge_id]
        if agent_id not in edge.members:
            raise ValueError("nonparticipant")
        return EconomicObservation(
            edge_id,
            self.rounds[edge_id],
            agent_id,
            edge.members,
            deepcopy(self.private_types[agent_id]),
            deepcopy(self.public[edge_id]),
        )

    def run_round(self, edge_id, strategies, disclose=None):
        edge = self.edges[edge_id]
        actions = {a: deepcopy(strategies[a](self.observation(edge_id, a))) for a in edge.members}
        for agent, action in actions.items():
            if (action.edge_id, action.round, action.agent_id) != (edge_id, self.rounds[edge_id], agent):
                raise ValueError("action identity mismatch")
        staged = deepcopy(self.ledger)
        settlement = self.mechanisms[edge.mechanism_id](deepcopy(edge), actions, staged)
        if settlement.id != f"{edge_id}:{self.rounds[edge_id]}":
            raise ValueError("settlement must identify edge and round")
        if not set(settlement.transfers) <= set(edge.members) or not set(settlement.inventory) <= set(
            edge.members
        ):
            raise ValueError("settlement to undeclared participant")
        staged.settle(settlement)
        public = {} if disclose is None else deepcopy(disclose(settlement))
        self.ledger.__dict__.update(staged.__dict__)
        self.public[edge_id] = public
        self.rounds[edge_id] += 1
        self.history.append(deepcopy(settlement))
        return settlement

    def snapshot(self):
        from dataclasses import asdict

        return {
            "rounds": deepcopy(self.rounds),
            "public": deepcopy(self.public),
            "ledger": self.ledger.snapshot(),
            "history": [asdict(s) for s in self.history],
        }

    def restore(self, snapshot):
        from .types import Settlement

        if set(snapshot["rounds"]) != set(self.edges):
            raise ValueError("checkpoint edge configuration mismatch")
        ledger = Ledger.restore(snapshot["ledger"])
        history = [Settlement(**s) for s in snapshot["history"]]
        self.ledger.__dict__.update(ledger.__dict__)
        self.rounds, self.public, self.history = (
            deepcopy(snapshot["rounds"]),
            deepcopy(snapshot["public"]),
            history,
        )
