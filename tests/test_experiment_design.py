import pytest

from consciousness_bridge.experiment_design import (
    best_single_protocol,
    distinguishable_pairs,
    minimal_discriminating_protocol_sets,
    protocol_pair_separations,
    protocol_set_utility,
)


def _family_requiring_two_protocols():
    return {
        "T1": {
            "recurrence": {"yes": 0.9, "no": 0.1},
            "broadcast": {"yes": 0.5, "no": 0.5},
        },
        "T2": {
            "recurrence": {"yes": 0.1, "no": 0.9},
            "broadcast": {"yes": 0.5, "no": 0.5},
        },
        "T3": {
            "recurrence": {"yes": 0.9, "no": 0.1},
            "broadcast": {"yes": 0.1, "no": 0.9},
        },
    }


def test_protocol_pair_separation_has_direct_tv_meaning():
    family = _family_requiring_two_protocols()
    separations = protocol_pair_separations(family, "recurrence")

    assert separations[("T1", "T2")] == pytest.approx(0.8)
    assert separations[("T1", "T3")] == pytest.approx(0.0)


def test_no_single_protocol_separates_all_pairs():
    family = _family_requiring_two_protocols()

    protocol, utility = best_single_protocol(family)
    assert protocol in {"recurrence", "broadcast"}
    assert utility == pytest.approx(0.0)


def test_two_protocol_set_has_positive_worst_pair_utility():
    family = _family_requiring_two_protocols()

    utility = protocol_set_utility(family, {"recurrence", "broadcast"})
    assert utility == pytest.approx(0.4)


def test_minimal_discriminating_set_is_exact_cover():
    family = _family_requiring_two_protocols()

    assert distinguishable_pairs(family) == frozenset(
        {("T1", "T2"), ("T1", "T3"), ("T2", "T3")}
    )
    assert minimal_discriminating_protocol_sets(family) == (
        frozenset({"recurrence", "broadcast"}),
    )


def test_added_universal_protocol_can_be_best_single_design():
    family = _family_requiring_two_protocols()
    family = {
        name: {
            **predictions,
            "hybrid": hybrid,
        }
        for (name, predictions), hybrid in zip(
            family.items(),
            (
                {"yes": 0.8, "no": 0.2},
                {"yes": 0.5, "no": 0.5},
                {"yes": 0.2, "no": 0.8},
            ),
            strict=True,
        )
    }

    protocol, utility = best_single_protocol(family)
    assert protocol == "hybrid"
    assert utility == pytest.approx(0.3)
