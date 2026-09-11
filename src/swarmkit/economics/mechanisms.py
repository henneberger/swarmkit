"""Exact small allocation mechanisms; ties use sorted participant IDs."""

from __future__ import annotations

import copy
from itertools import product

import numpy as np

from .ledger import amount
from .types import Settlement


class FirstPriceAuction:
    def __init__(self, reserve=0.0, budgets=None):
        self.reserve = amount(reserve)
        self.budgets = {a: amount(v) for a, v in (budgets or {}).items()}

    def clear(self, bids):
        bids = {a: amount(v) for a, v in bids.items()}
        if any(a in self.budgets and v > self.budgets[a] for a, v in bids.items()):
            raise ValueError("bid exceeds budget")
        ranked = sorted(bids, key=lambda a: (-bids[a], a))
        if not ranked or bids[ranked[0]] < self.reserve:
            return {"winner": None, "payment": 0.0}
        return {"winner": ranked[0], "payment": bids[ranked[0]]}


class SecondPriceAuction(FirstPriceAuction):
    def clear(self, bids):
        result = super().clear(bids)
        if result["winner"] is not None:
            others = [v for a, v in bids.items() if a != result["winner"]]
            result["payment"] = max(self.reserve, max(others, default=0))
        return result


class ReverseAuction:
    """First-price procurement: lowest ask wins and is paid its ask."""

    def __init__(self, budget):
        self.budget = amount(budget)

    def clear(self, asks):
        asks = {a: amount(v) for a, v in asks.items()}
        ranked = sorted(asks, key=lambda a: (asks[a], a))
        if not ranked or asks[ranked[0]] > self.budget:
            return {"winner": None, "payment": 0.0}
        return {"winner": ranked[0], "payment": asks[ranked[0]]}


class CombinatorialAuction:
    """Exact XOR bundle bids: at most one bundle per bidder, unit supply per item.

    Enumeration deliberately bounded; raises instead of silently approximating.
    Quasilinear, nonnegative values; no budgets or cross-bidder externalities.
    """

    def __init__(self, items, max_allocations=1_000_000):
        self.items = frozenset(items)
        self.max_allocations = max_allocations

    def clear(self, bids):
        names = sorted(bids)
        choices = []
        count = 1
        for a in names:
            options = [(frozenset(), 0.0)]
            for bundle, value in bids[a].items():
                bundle = frozenset(bundle)
                if not bundle or not bundle <= self.items:
                    raise ValueError("invalid bundle")
                options.append((bundle, amount(value)))
            options[1:] = sorted(options[1:], key=lambda x: tuple(sorted(x[0])))
            choices.append(options)
            count *= len(options)
            if count > self.max_allocations:
                raise ValueError("exact allocation enumeration limit exceeded")
        best = {"allocation": {}, "values": {}, "welfare": 0.0}
        for joint in product(*choices):
            occupied = set()
            for bundle, _ in joint:
                if occupied & bundle:
                    break
                occupied.update(bundle)
            else:
                welfare = sum(v for _, v in joint)
                if welfare > best["welfare"]:
                    best = {
                        "allocation": {a: b for a, (b, _) in zip(names, joint, strict=True) if b},
                        "values": {a: v for a, (b, v) in zip(names, joint, strict=True) if b},
                        "welfare": welfare,
                    }
        return best


class VCGPayments:
    def __init__(self, auction):
        self.auction = auction

    def clear(self, bids):
        result = self.auction.clear(bids)
        result["payments"] = {}
        for a in bids:
            without = self.auction.clear({b: v for b, v in bids.items() if b != a})["welfare"]
            result["payments"][a] = max(0.0, without - (result["welfare"] - result["values"].get(a, 0)))
        return result


class DoubleAuction:
    """Single-unit call market, sorted matching and pairwise midpoint payments.

    This rule is budget balanced and bid/ask individually rational, not truthful.
    Each ID may submit one unit on one side; callers settle actual inventory.
    """

    def clear(self, buyers, sellers):
        if set(buyers) & set(sellers):
            raise ValueError("an account cannot appear on both sides")
        bids = sorted(((amount(v), a) for a, v in buyers.items()), key=lambda x: (-x[0], x[1]))
        asks = sorted((amount(v), a) for a, v in sellers.items())
        trades = []
        for (bid, buyer), (ask, seller) in zip(bids, asks, strict=False):
            if bid < ask:
                break
            trades.append({"buyer": buyer, "seller": seller, "price": (bid + ask) / 2, "surplus": bid - ask})
        return trades


class DeferredAcceptance:
    """One-to-one strict incomplete preferences; missing partners unacceptable."""

    def clear(self, proposers, receivers):
        for prefs, other in ((proposers, receivers), (receivers, proposers)):
            if any(len(set(p)) != len(p) or not set(p) <= other.keys() for p in prefs.values()):
                raise ValueError("preferences must be strict lists of known partners")
        ranks = {r: {p: i for i, p in enumerate(ps)} for r, ps in receivers.items()}
        next_index = dict.fromkeys(proposers, 0)
        free, held = sorted(proposers), {}
        while free:
            p = free.pop(0)
            if next_index[p] == len(proposers[p]):
                continue
            r = proposers[p][next_index[p]]
            next_index[p] += 1
            if p in ranks[r] and (r not in held or ranks[r][p] < ranks[r][held[r]]):
                if r in held:
                    free.append(held[r])
                held[r] = p
            else:
                free.append(p)
        return {p: r for r, p in held.items()}


class ContractNet:
    """Capability/cost team procurement with escrow, verification and idempotent payout.

    Offers map team IDs to {members, capabilities, cost}. Completion verification
    is trusted application code. Award and verified delivery are separate events.
    """

    def __init__(self, ledger):
        self.ledger = ledger
        self.contracts = {}

    def award(self, contract_id, task_id, buyer, required, offers):
        request = copy.deepcopy((task_id, buyer, sorted(required), offers))
        if contract_id in self.contracts:
            if self.contracts[contract_id]["request"] != request:
                raise ValueError("contract identity reused")
            return copy.deepcopy(self.contracts[contract_id])
        legal = []
        for team, offer in offers.items():
            members = tuple(offer["members"])
            if not members or len(set(members)) != len(members) or buyer in members:
                raise ValueError("invalid team members")
            if not set(members) <= self.ledger.balances.keys():
                raise ValueError("team requires ledger accounts")
            cost = amount(offer["cost"])
            if set(required) <= set(offer["capabilities"]) and cost <= self.ledger.available(buyer):
                legal.append((cost, team, members))
        if not legal:
            return None
        cost, team, members = min(legal)
        key = "contract:" + contract_id
        self.ledger.reserve(key, buyer, cost)
        record = {
            "request": request,
            "task_id": task_id,
            "buyer": buyer,
            "team": team,
            "members": members,
            "cost": cost,
            "reservation": key,
            "status": "awarded",
        }
        self.contracts[contract_id] = record
        return copy.deepcopy(record)

    def complete(self, contract_id, artifact, verifier):
        c = self.contracts[contract_id]
        if c["status"] != "awarded":
            return c["status"] == "paid"
        if (
            artifact.author not in c["members"]
            or artifact.metadata.get("task_id") != c["task_id"]
            or artifact.metadata.get("contract_id") != contract_id
        ):
            raise ValueError("artifact not bound to this task, contract and team")
        feedback = verifier(artifact)
        success = bool(feedback.verified)
        transfers = {c["buyer"]: -c["cost"]} if success else {}
        if success:
            for member in c["members"]:
                transfers[member] = c["cost"] / len(c["members"])
        self.ledger.settle(
            Settlement(
                "contract-result:" + contract_id,
                transfers,
                releases=(c["reservation"],),
                metadata={"artifact_id": artifact.id},
            )
        )
        c["status"] = "paid" if success else "failed"
        return success

    def cancel(self, contract_id):
        c = self.contracts[contract_id]
        if c["status"] == "awarded":
            self.ledger.settle(Settlement("contract-cancel:" + contract_id, {}, releases=(c["reservation"],)))
            c["status"] = "cancelled"


class LMSRMarket:
    """Logarithmic scoring-rule market. Positive shares are bought from the maker.

    Long-only funded trades settle through Ledger. The maker needs initial subsidy
    b*log(outcomes); no uncollateralized shorts or implicit minting.
    """

    def __init__(self, outcomes, liquidity=10.0, maker="market"):
        if outcomes < 2 or liquidity <= 0 or not np.isfinite(liquidity):
            raise ValueError("at least two outcomes and positive finite liquidity")
        self.q = np.zeros(outcomes)
        self.b, self.maker = float(liquidity), maker
        self.positions, self.trades = {}, {}
        self.resolved = None

    def cost(self, q):
        q = np.asarray(q, float) / self.b
        return float(self.b * (np.max(q) + np.log(np.exp(q - np.max(q)).sum())))

    def prices(self):
        x = np.exp((self.q - self.q.max()) / self.b)
        return x / x.sum()

    def trade(self, ledger, trade_id, trader, delta):
        delta = np.asarray(delta, float)
        if self.resolved is not None or trader == self.maker:
            raise ValueError("market closed or invalid trader")
        if delta.shape != self.q.shape or not np.isfinite(delta).all():
            raise ValueError("invalid trade")
        signature = (trader, tuple(delta))
        if trade_id in self.trades:
            if self.trades[trade_id][0] != signature:
                raise ValueError("trade identity reused")
            return self.trades[trade_id][1]
        position = self.positions.get(trader, np.zeros_like(self.q)) + delta
        if (position < -1e-10).any():
            raise ValueError("short selling unsupported")
        payment = self.cost(self.q + delta) - self.cost(self.q)
        staged = copy.deepcopy(ledger)
        collateral = "market-collateral:" + self.maker
        releases = (collateral,) if collateral in staged.reservations else ()
        staged.settle(
            Settlement("market-trade:" + trade_id, {trader: -payment, self.maker: payment}, releases=releases)
        )
        staged.reserve(collateral, self.maker, float(np.max(self.q + delta)))
        ledger.__dict__.update(staged.__dict__)
        self.q += delta
        self.positions[trader] = position
        self.trades[trade_id] = (signature, payment)
        return payment

    def resolve(self, ledger, outcome):
        if not isinstance(outcome, int) or not 0 <= outcome < len(self.q):
            raise ValueError("invalid outcome")
        if self.resolved is not None:
            if self.resolved != outcome:
                raise ValueError("outcome already resolved")
            return False
        transfers = {a: float(p[outcome]) for a, p in self.positions.items()}
        transfers[self.maker] = -sum(transfers.values())
        collateral = "market-collateral:" + self.maker
        releases = (collateral,) if collateral in ledger.reservations else ()
        ledger.settle(Settlement("market-resolution:" + self.maker, transfers, releases=releases))
        self.resolved = outcome
        return True
