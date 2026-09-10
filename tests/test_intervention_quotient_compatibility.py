import pytest

from consciousness_bridge.intervention_quotient_compatibility import (
    descended_response_table,
    intervention_fibers,
    intervention_quotient_ambiguity,
    intervention_quotient_certificate,
    quotient_geometry_selection_bound,
    representative_response_table,
    representative_selection_distance,
)

FINE = ("u0", "u1", "u2")
COARSE = ("A", "B")
QUOTIENT = {"u0": "A", "u1": "A", "u2": "B"}
DELAYS = ("t1", "t2")


def _exact_responses():
    return {
        "u0": {"t1": {0: 0.8, 1: 0.2}, "t2": {0: 0.6, 1: 0.4}},
        "u1": {"t1": {0: 0.8, 1: 0.2}, "t2": {0: 0.6, 1: 0.4}},
        "u2": {"t1": {0: 0.2, 1: 0.8}, "t2": {0: 0.3, 1: 0.7}},
    }


def _approximate_responses():
    responses = _exact_responses()
    responses["u1"] = {
        "t1": {0: 0.7, 1: 0.3},
        "t2": {0: 0.55, 1: 0.45},
    }
    return responses


def test_intervention_fibers_form_declared_surjective_quotient():
    fibers = intervention_fibers(FINE, COARSE, QUOTIENT)
    assert fibers == {"A": ("u0", "u1"), "B": ("u2",)}


def test_exact_response_equality_inside_fibers_certifies_descent():
    certificate = intervention_quotient_certificate(
        _exact_responses(), FINE, COARSE, QUOTIENT, DELAYS
    )
    assert certificate.quotient_ambiguity < 1e-12
    assert certificate.exact_descent_certified


def test_exact_descended_response_is_representative_independent():
    descended = descended_response_table(
        _exact_responses(), FINE, COARSE, QUOTIENT, DELAYS
    )
    assert descended["A"]["t1"] == {0: 0.8, 1: 0.2}
    assert descended["B"]["t2"] == {0: 0.3, 1: 0.7}


def test_positive_within_fiber_discrepancy_blocks_exact_descent():
    certificate = intervention_quotient_certificate(
        _approximate_responses(), FINE, COARSE, QUOTIENT, DELAYS
    )
    assert certificate.quotient_ambiguity == pytest.approx(0.1)
    assert not certificate.exact_descent_certified
    with pytest.raises(ValueError, match="do not descend exactly"):
        descended_response_table(
            _approximate_responses(), FINE, COARSE, QUOTIENT, DELAYS
        )


def test_quotient_ambiguity_is_maximum_over_fiber_pairs_and_delays():
    ambiguity = intervention_quotient_ambiguity(
        _approximate_responses(), FINE, COARSE, QUOTIENT, DELAYS
    )
    assert ambiguity == pytest.approx(0.1)


def test_two_representative_choices_differ_by_at_most_quotient_ambiguity():
    responses = _approximate_responses()
    first = representative_response_table(
        responses,
        COARSE,
        QUOTIENT,
        {"A": "u0", "B": "u2"},
        DELAYS,
    )
    second = representative_response_table(
        responses,
        COARSE,
        QUOTIENT,
        {"A": "u1", "B": "u2"},
        DELAYS,
    )
    ambiguity = intervention_quotient_ambiguity(
        responses, FINE, COARSE, QUOTIENT, DELAYS
    )
    assert representative_selection_distance(first, second) <= ambiguity + 1e-12


def test_pairwise_geometry_representation_uncertainty_has_two_eta_bound():
    assert quotient_geometry_selection_bound(0.07) == pytest.approx(0.14)


def test_non_surjective_intervention_map_is_rejected():
    with pytest.raises(ValueError, match="surjective"):
        intervention_fibers(
            FINE,
            COARSE,
            {"u0": "A", "u1": "A", "u2": "A"},
        )


def test_representative_must_lie_inside_its_quotient_fiber():
    with pytest.raises(ValueError, match="quotient fiber"):
        representative_response_table(
            _exact_responses(),
            COARSE,
            QUOTIENT,
            {"A": "u2", "B": "u2"},
            DELAYS,
        )
