"""Optional solver adapter; imports OpenSpiel only on construction."""


class OpenSpielCFR:
    """OpenSpiel's CFR/CFR+ and external/outcome-sampling MCCFR implementations."""

    def __init__(self, game="kuhn_poker", variant="cfr"):
        import pyspiel
        from open_spiel.python.algorithms import cfr, external_sampling_mccfr, outcome_sampling_mccfr

        constructors = {
            "cfr": cfr.CFRSolver,
            "cfr_plus": cfr.CFRPlusSolver,
            "external_sampling": external_sampling_mccfr.ExternalSamplingSolver,
            "outcome_sampling": outcome_sampling_mccfr.OutcomeSamplingSolver,
        }
        if variant not in constructors:
            raise ValueError("unknown CFR variant")
        self.game = pyspiel.load_game(game) if isinstance(game, str) else game
        self.solver = constructors[variant](self.game)
        self.variant = variant

    def train(self, iterations=100):
        if iterations < 1:
            raise ValueError("positive iteration count required")
        for _ in range(iterations):
            if self.variant in ("cfr", "cfr_plus"):
                self.solver.evaluate_and_update_policy()
            else:
                self.solver.iteration()
        return self.solver.average_policy()

    def exploitability(self):
        from open_spiel.python.algorithms import exploitability

        return exploitability.exploitability(self.game, self.solver.average_policy())


class NegMASNegotiation:
    """Finite-outcome alternating offers using real NegMAS negotiators.

    Utilities map outcome tuples to numeric values, with one reservation value per
    party. Negotiator factories may replace the default aspiration strategy.
    """

    def run(self, utilities, disagreement, steps=100, factories=None):
        from negmas import AspirationNegotiator, MappingUtilityFunction, SAOMechanism

        if len(utilities) < 2 or len(disagreement) != len(utilities) or steps < 1:
            raise ValueError("at least two utility maps and matching disagreement values required")
        outcomes = tuple(utilities[0])
        if not outcomes or any(set(u) != set(outcomes) for u in utilities):
            raise ValueError("same finite outcome domain required")
        session = SAOMechanism(outcomes=outcomes, n_steps=steps)
        factories = factories or [AspirationNegotiator] * len(utilities)
        if len(factories) != len(utilities):
            raise ValueError("one negotiator factory per party required")
        for factory, utility, reserve in zip(factories, utilities, disagreement, strict=True):
            ufun = MappingUtilityFunction(
                utility, reserved_value=reserve, outcome_space=session.outcome_space
            )
            session.add(factory(ufun=ufun))
        state = session.run()
        return {
            "agreement": state.agreement,
            "steps": state.step,
            "utilities": [u[state.agreement] for u in utilities]
            if state.agreement is not None
            else list(disagreement),
        }


class HyperNetXAdapter:
    """Structural export preserves edge IDs; authoritative economic data stays local."""

    @staticmethod
    def convert(edges):
        import hypernetx as hnx

        edges = tuple(edges)
        if len({e.id for e in edges}) != len(edges):
            raise ValueError("duplicate edge ids")
        return hnx.Hypergraph({e.id: e.members for e in edges})


class XGIAdapter:
    @staticmethod
    def convert(edges):
        import xgi

        edges = tuple(edges)
        if len({e.id for e in edges}) != len(edges):
            raise ValueError("duplicate edge ids")
        graph = xgi.Hypergraph()
        for edge in edges:
            graph.add_edge(edge.members, idx=edge.id, mechanism_id=edge.mechanism_id)
        return graph
