import pytest

from consciousness_bridge.delay_quotient_compatibility import (
    delay_fibers,
    delay_quotient_ambiguity,
    delay_quotient_certificate,
    descended_delay_response_table,
    representative_delay_response_table,
    representative_selection_distance,
    response_geometry_selection_bound,
    temporal_path_selection_bound,
)

INTERVENTIONS = ("u0", "u1")
FINE = ("t0", "t1", "t2")
COARSE = ("early", "late")
QUOTIENT = {"t0": "early", "t1": "early", "t2": "late"}


def _exact_responses():
    return {
        "u0": {
            "t0": {0: 0.8, 1: 0.2},
            "t1": {0: 0.8, 1: 0.2},
            "t2": {0: 0.5, 1: 0.5},
        },
        "u1": {
            "t0": {0: 0.3, 1: 0.7},
            "t1": {0: 0.3, 1: 0.7},
            "t2": {0: 0.2, 1: 0.8},
        },
    }


def _approximate_responses():
    responses = _exact_responses()
    responses["u1"]["t1"] = {0: 0.4, 1: 0.6}
    return responses


def test_delay_fibers_form_declared_surjective_quotient():
    assert delay_fibers(FINE, COARSE, QUOTIENT) == {
        "early": ("t0", "t1"),
        "late": ("t2",),
    }


def test_exact_temporal_fiber_equality_certifies_descent():
    certificate = delay_quotient_certificate(
        _exact_responses(), INTERVENTIONS, FINE, COARSE, QUOTIENT
    )
    assert certificate.quotient_ambiguity < 1e-12
    assert certificate.exact_descent_certified


def test_descended_table_is_unique_under_exact_descent():
    table = descended_delay_response_table(
        _exact_responses(), INTERVENTIONS, FINE, COARSE, QUOTIENT
    )
    assert table["u0"]["early"] == {0: 0.8, 1: 0.2}
    assert table["u1"]["late"] == {0: 0.2, 1: 0.8}


def test_positive_within_temporal_fiber_discrepancy_blocks_exact_descent():
    certificate = delay_quotient_certificate(
        _approximate_responses(), INTERVENTIONS, FINE, COARSE, QUOTIENT
    )
    assert certificate.quotient_ambiguity == pytest.approx(0.1)
    assert not certificate.exact_descent_certified
    with pytest.raises(ValueError, match="do not descend exactly"):
        descended_delay_response_table(
            _approximate_responses(), INTERVENTIONS, FINE, COARSE, QUOTIENT
        )


def test_delay_ambiguity_is_uniform_over_interventions():
    ambiguity = delay_quotient_ambiguity(
        _approximate_responses(), INTERVENTIONS, FINE, COARSE, QUOTIENT
    )
    assert ambiguity == pytest.approx(0.1)


def test_representative_tables_differ_by_at_most_eta():
    responses = _approximate_responses()
    first = representative_delay_response_table(
        responses, INTERVENTIONS, COARSE, QUOTIENT, {"early": "t0", "late": "t2"}
    )
    second = representative_delay_response_table(
        responses, INTERVENTIONS, COARSE, QUOTIENT, {"early": "t1", "late": "t2"}
    )
    eta = delay_quotient_ambiguity(
        responses, INTERVENTIONS, FINE, COARSE, QUOTIENT
    )
    assert representative_selection_distance(first, second) <= eta + 1e-12


def test_response_geometry_uncertainty_has_two_eta_bound():
    assert response_geometry_selection_bound(0.07) == pytest.approx(0.14)


def test_temporal_path_uncertainty_scales_with_transition_count():
    assert temporal_path_selection_bound(0.07, 4) == pytest.approx(0.56)


def test_non_surjective_delay_map_is_rejected():
    with pytest.raises(ValueError, match="surjective"):
        delay_fibers(
            FINE,
            COARSE,
            {"t0": "early", "t1": "early", "t2": "early"},
        )


def test_representative_must_lie_in_declared_temporal_fiber():
    with pytest.raises(ValueError, match="quotient fiber"):
        representative_delay_response_table(
            _exact_responses(),
            INTERVENTIONS,
            COARSE,
            QUOTIENT,
            {"early": "t2", "late": "t2"},
        )
