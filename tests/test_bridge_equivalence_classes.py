from consciousness_bridge.theory_classes import (
    bridge_equivalence_classes,
    observational_fingerprint,
    observationally_equivalent,
    restrict_protocols,
)


def _theory_family():
    return {
        "T1": {
            "passive": {"yes": 0.5, "no": 0.5},
            "intervention": {"yes": 0.8, "no": 0.2},
        },
        "T2": {
            "passive": {"yes": 0.5, "no": 0.5},
            "intervention": {"yes": 0.8, "no": 0.2},
        },
        "T3": {
            "passive": {"yes": 0.5, "no": 0.5},
            "intervention": {"yes": 0.3, "no": 0.7},
        },
    }


def test_observational_fingerprint_is_order_invariant():
    first = {
        "p2": {"b": 0.7, "a": 0.3},
        "p1": {"a": 0.6, "b": 0.4},
    }
    second = {
        "p1": {"b": 0.4, "a": 0.6},
        "p2": {"a": 0.3, "b": 0.7},
    }

    assert observational_fingerprint(first) == observational_fingerprint(second)


def test_theories_with_same_fingerprint_share_equivalence_class():
    theories = _theory_family()

    assert observationally_equivalent(theories["T1"], theories["T2"])
    assert not observationally_equivalent(theories["T1"], theories["T3"])

    classes = set(bridge_equivalence_classes(theories))
    assert classes == {frozenset({"T1", "T2"}), frozenset({"T3"})}


def test_richer_experiment_class_refines_observational_partition():
    theories = _theory_family()
    passive_only = {
        name: restrict_protocols(predictions, {"passive"})
        for name, predictions in theories.items()
    }

    assert set(bridge_equivalence_classes(passive_only)) == {
        frozenset({"T1", "T2", "T3"})
    }
    assert set(bridge_equivalence_classes(theories)) == {
        frozenset({"T1", "T2"}),
        frozenset({"T3"}),
    }
