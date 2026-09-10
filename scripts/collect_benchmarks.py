"""Archive benchmark research using the shared public-source collector."""

from pathlib import Path

import collect_economic_games as collector

if __name__ == "__main__":
    collector.BASE = Path(__file__).resolve().parents[1] / "sources/benchmarks"
    collector.main()
