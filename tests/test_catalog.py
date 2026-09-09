import pytest

from swarmkit.catalog import methods, resolve


def test_every_registered_implementation_resolves_and_names_are_unique():
    records = methods()
    assert len(records) >= 45
    assert len({record.name for record in records}) == len(records)
    for record in records:
        assert callable(resolve(record.name))
        assert record.description and record.fidelity
        assert all(source.startswith("https://") for source in record.sources)
    assert all(record.family == "latent" for record in methods("latent"))
    with pytest.raises(KeyError):
        resolve("os.system")
