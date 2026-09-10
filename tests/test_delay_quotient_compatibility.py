import pytest

from consciousness_bridge.delay_quotient_compatibility import (
    delay_fibers,
    delay_quotient_ambiguity,
    delay_quotient_certificate,
    descended_response_table,
    quotient_geometry_selection_bound,
    representative_response_table,
    representative_selection_distance,
)

INTERVENTIONS = ("u0", "u1")
FINE_DELAYS = (0, 1, 2)
COARSE_DELAYS = ("early", "late")
QUOTIENT = {0: "early", 1: "early", 2: "late"}


def exact_responses():
    return {
        "u0": {
            0: {0: 0.8, 1: 0.2},
            1: {0: 0.8, 1: 0.2},
            2: {0: 0.3, 1: 0.7},
        },
        "u1": {
            0: {0: 0.4, 1: 0.6},
            1: {0: 0.4, 1: 0.6},
            2: {0: 0.1, 1: 0.9},
        },
    }


def inexact_responses():
    responses = exact_responses()
    responses["u0"][1] = {0: 0.7, 1: 0.3}
    responses["u1"][1] = {0: 0.35, 1: 0.65}
    return responses


def test_delay_fibers_are_exact_and_surjective():
    assert delay_fibers(FINE_DELAYS, COARSE_DELAYS, QUOTIENT) == {
        "early": (0, 1),
        "late": (2,),
    }
    with pytest.raises(ValueError):
        delay_fibers(FINE_DELAYS, ("early", "late", "unused"), QUOTIENT)


def test_exact_descent_has_zero_ambiguity():
    ambiguity = delay_quotient_ambiguity(
        exact_responses(), INTERVENTIONS, FINE_DELAYS, COARSE_DELAYS, QUOTIENT
    )
    assert ambiguity == pytest.approx(0.0)
    certificate = delay_quotient_certificate(
        exact_responses(), INTERVENTIONS, FINE_DELAYS, COARSE_DELAYS, QUOTIENT
    )
    assert certificate.exact_descent_certified
    assert certificate.within_tolerance_certified


def test_nonconstant_delay_fiber_is_detected():
    ambiguity = delay_quotient_ambiguity(
        inexact_responses(), INTERVENTIONS, FINE_DELAYS, COARSE_DELAYS, QUOTIENT
    )
    assert ambiguity == pytest.approx(0.1)
    certificate = delay_quotient_certificate(
        inexact_responses(), INTERVENTIONS, FINE_DELAYS, COARSE_DELAYS, QUOTIENT
    )
    assert not certificate.exact_descent_certified
    assert not certificate.within_tolerance_certified


def test_unique_descended_table_exists_when_fiber_constant():
    descended = descended_response_table(
        exact_responses(), INTERVENTIONS, FINE_DELAYS, COARSE_DELAYS, QUOTIENT
    )
    assert descended["u0"]["early"] == {0: 0.8, 1: 0.2}
    assert descended["u1"]["late"] == {0: 0.1, 1: 0.9}


def test_descended_table_rejects_inexact_quotient():
    with pytest.raises(ValueError, match="do not descend exactly"):
        descended_response_table(
            inexact_responses(),
            INTERVENTIONS,
            FINE_DELAYS,
            COARSE_DELAYS,
            QUOTIENT,
        )


def test_representative_selection_distance_is_bounded_by_ambiguity():
    responses = inexact_responses()
    first = representative_response_table(
        responses,
        INTERVENTIONS,
        COARSE_DELAYS,
        QUOTIENT,
        {"early": 0, "late": 2},
    )
    second = representative_response_table(
        responses,
        INTERVENTIONS,
        COARSE_DELAYS,
        QUOTIENT,
        {"early": 1, "late": 2},
    )
    distance = representative_selection_distance(first, second)
    ambiguity = delay_quotient_ambiguity(
        responses, INTERVENTIONS, FINE_DELAYS, COARSE_DELAYS, QUOTIENT
    )
    assert distance <= ambiguity + 1e-12
    assert distance == pytest.approx(0.1)


def test_geometry_selection_bound_is_two_eta():
    assert quotient_geometry_selection_bound(0.13) == pytest.approx(0.26)
    with pytest.raises(ValueError):
        quotient_geometry_selection_bound(-0.01)


def test_tolerance_certificate_does_not_claim_exact_equality():
    certificate = delay_quotient_certificate(
        inexact_responses(),
        INTERVENTIONS,
        FINE_DELAYS,
        COARSE_DELAYS,
        QUOTIENT,
        tolerance=0.11,
    )
    assert certificate.quotient_ambiguity == pytest.approx(0.1)
    assert certificate.tolerance == pytest.approx(0.11)
    assert not certificate.exact_descent_certified
    assert certificate.within_tolerance_certified
    with pytest.raises(ValueError):
        delay_quotient_certificate(
            exact_responses(),
            INTERVENTIONS,
            FINE_DELAYS,
            COARSE_DELAYS,
            QUOTIENT,
            tolerance=-1.0,
        )


def test_invalid_response_grid_and_representatives_are_rejected():
    responses = exact_responses()
    broken = {"u0": responses["u0"]}
    with pytest.raises(ValueError):
        delay_quotient_ambiguity(
            broken, INTERVENTIONS, FINE_DELAYS, COARSE_DELAYS, QUOTIENT
        )
    with pytest.raises(ValueError):
        representative_response_table(
            responses,
            INTERVENTIONS,
            COARSE_DELAYS,
            QUOTIENT,
            {"early": 2, "late": 2},
        )
