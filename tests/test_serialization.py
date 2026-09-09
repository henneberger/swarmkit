import json

import numpy as np
import pytest

from swarmkit.serialization import dumps, loads
from swarmkit.types import AgentState, Artifact, Evidence, Message, MessageKind, SwarmState


def test_checkpoint_preserves_common_types_numpy_and_rng():
    evidence = Evidence("e", "fact", "source", "a")
    state = SwarmState({"a": AgentState("a", private_evidence=(evidence,))}, seed=4)
    state.messages.append(Message("a", "fact", kind=MessageKind.CRITIQUE, evidence=(evidence,)))
    state.artifacts["x"] = Artifact("x", "a", {"array": np.ones((2, 3))})
    state.data["weights"] = {("a", "b"): np.array([1.0, 2.0])}
    state.data["set"] = {"x", "y"}
    state.rng.random()
    restored = loads(dumps(state))
    assert restored.rng.random() == state.rng.random()
    assert restored.messages[0].kind is MessageKind.CRITIQUE
    assert restored.agents["a"].private_evidence == (evidence,)
    np.testing.assert_equal(restored.data["weights"][("a", "b")], [1, 2])
    assert restored.data["set"] == {"x", "y"}


def test_never_deserialize_arbitrary_code_or_unsupported_values():
    state = SwarmState()
    state.data["callable"] = lambda: 1
    with pytest.raises(TypeError):
        dumps(state)
    with pytest.raises(ValueError):
        loads(json.dumps({"format": "swarmkit", "version": 1, "state": {"$type": "os.system", "fields": {}}}))
    with pytest.raises(ValueError):
        loads('{"format":"swarmkit","version":999}')


def test_empty_array_axes_roundtrip_and_invalid_envelopes():
    state = SwarmState()
    state.data["empty"] = np.empty((2, 0, 3))
    assert loads(dumps(state)).data["empty"].shape == (2, 0, 3)
    for text in ("[]", "null", '{"format":"swarmkit","version":true}'):
        with pytest.raises(ValueError):
            loads(text)


def test_unique_temporary_snapshot_preserves_unrelated_tmp_file(tmp_path):
    from swarmkit.serialization import load, save

    path = tmp_path / "snapshot.json"
    sibling = tmp_path / "snapshot.json.tmp"
    sibling.write_text("other writer")
    save(SwarmState(seed=9), path)
    assert load(path).seed == 9
    assert sibling.read_text() == "other writer"
