import pytest

from consciousness_bridge.equivalence import (
    bridge_is_class_invariant,
    quotient_bridge,
)


def test_invariant_bridge_descends_to_quotient():
    class_of = {
        "meters": "same_physical_system",
        "centimeters": "same_physical_system",
        "different_system": "other_system",
    }
    bridge = {
        "meters": "experience_A",
        "centimeters": "experience_A",
        "different_system": "experience_B",
    }

    assert bridge_is_class_invariant(class_of, bridge)
    assert quotient_bridge(class_of, bridge) == {
        "same_physical_system": "experience_A",
        "other_system": "experience_B",
    }


def test_noninvariant_bridge_is_rejected():
    class_of = {
        "encoding_1": "same_physical_system",
        "encoding_2": "same_physical_system",
    }
    bridge = {
        "encoding_1": "experience_A",
        "encoding_2": "experience_B",
    }

    assert not bridge_is_class_invariant(class_of, bridge)
    with pytest.raises(ValueError):
        quotient_bridge(class_of, bridge)
