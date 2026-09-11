"""Atomic, conserved credits/inventories with explicit escrow and retry identity."""

from __future__ import annotations

import copy
import json
import math
from dataclasses import asdict

from .types import Settlement


def amount(value):
    value = float(value)
    if not math.isfinite(value) or value < 0:
        raise ValueError("amount must be finite and nonnegative")
    return value


class Ledger:
    """All accounts, including subsidy/treasury accounts, must be funded explicitly.

    Reservations impose an ordered-clearing policy across overlapping edges.
    No overdrafts, implicit minting, or partially committed settlements.
    """

    def __init__(self, balances, inventories=None):
        self.balances = {a: amount(v) for a, v in balances.items()}
        self.inventories = {a: {r: amount(v) for r, v in rs.items()} for a, rs in (inventories or {}).items()}
        if not set(self.inventories) <= set(self.balances):
            raise ValueError("inventory owner needs an account")
        self.reservations = {}
        self.settlements = {}

    def available(self, account):
        return self.balances[account] - sum(v for a, v in self.reservations.values() if a == account)

    def reserve(self, key, account, value):
        value = amount(value)
        if key in self.reservations:
            if self.reservations[key] != (account, value):
                raise ValueError("reservation key reused")
            return
        if value > self.available(account) + 1e-10:
            raise ValueError("insufficient unreserved credit")
        self.reservations[key] = (account, value)

    def settle(self, settlement: Settlement):
        record = json.loads(json.dumps(asdict(settlement), allow_nan=False))
        if settlement.id in self.settlements:
            if self.settlements[settlement.id] != record:
                raise ValueError("settlement id reused with different content")
            return False
        if not settlement.id or len(set(settlement.releases)) != len(settlement.releases):
            raise ValueError("invalid settlement identity or duplicate releases")
        staged = copy.deepcopy(self)
        for key in settlement.releases:
            if key not in staged.reservations:
                raise ValueError("unknown reservation")
            del staged.reservations[key]
        if any(not math.isfinite(v) for v in settlement.transfers.values()):
            raise ValueError("nonfinite transfer")
        if abs(sum(settlement.transfers.values())) > 1e-8:
            raise ValueError("transfers must conserve credit")
        for a, delta in settlement.transfers.items():
            if a not in staged.balances:
                raise ValueError("unknown account")
            staged.balances[a] += delta
        for a in staged.balances:
            if not math.isfinite(staged.balances[a]) or staged.available(a) < -1e-8:
                raise ValueError("settlement overspends available credit")
        resources = set()
        for a, deltas in settlement.inventory.items():
            if a not in staged.balances:
                raise ValueError("unknown inventory account")
            for r, delta in deltas.items():
                if not math.isfinite(delta):
                    raise ValueError("nonfinite inventory change")
                resources.add(r)
                stock = staged.inventories.setdefault(a, {})
                stock[r] = stock.get(r, 0) + delta
                if not math.isfinite(stock[r]) or stock[r] < -1e-8:
                    raise ValueError("negative inventory")
        for r in resources:
            if abs(sum(ds.get(r, 0) for ds in settlement.inventory.values())) > 1e-8:
                raise ValueError("inventory must be conserved")
        staged.settlements[settlement.id] = copy.deepcopy(record)
        self.__dict__.update(staged.__dict__)
        return True

    def snapshot(self):
        return copy.deepcopy(self.__dict__)

    @classmethod
    def restore(cls, snapshot):
        result = cls(snapshot["balances"], snapshot["inventories"])
        result.reservations = {k: tuple(v) for k, v in snapshot["reservations"].items()}
        result.settlements = copy.deepcopy(snapshot["settlements"])
        for a in result.balances:
            if result.available(a) < -1e-8:
                raise ValueError("checkpoint reservations exceed balances")
        return result
