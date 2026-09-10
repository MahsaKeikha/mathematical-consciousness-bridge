import pytest

from consciousness_bridge.joint_operational_quotient import (
    additive_geometry_bound,
    descended_joint_response_table,
    joint_geometry_selection_bound,
    joint_operational_quotient_certificate,
    joint_quotient_ambiguity,
)

FINE_U = ("u0", "u1", "u2")
COARSE_U = ("A", "B")
B = {"u0": "A", "u1": "A", "u2": "B"}
FINE_T = ("t0", "t1", "t2")
COARSE_T = ("early", "late")
A = {"t0": "early", "t1": "early", "t2": "late"}


def _exact_responses():
    return {
        "u0": {
            "t0": {0: 0.8, 1: 0.2},
            "t1": {0: 0.8, 1: 0.2},
            "t2": {0: 0.6, 1: 0.4},
        },
        "u1": {
            "t0": {0: 0.8, 1: 0.2},
            "t1": {0: 0.8, 1: 0.2},
            "t2": {0: 0.6, 1: 0.4},
        },
        "u2": {
            "t0": {0: 0.3, 1: 0.7},
            "t1": {0: 0.3, 1: 0.7},
            "t2": {0: 0.2, 1: 0.8},
        },
    }


def _approximate_responses():
    responses = _exact_responses()
    responses["u1"]["t0"] = {0: 0.75, 1: 0.25}
    responses["u1"]["t1"] = {0: 0.70, 1: 0.30}
    return responses


def test_exact_separate_quotients_give_exact_joint_descent():
    certificate = joint_operational_quotient_certificate(
        _exact_responses(), FINE_U, COARSE_U, B, FINE_T, COARSE_T, A
    )
    assert certificate.intervention_ambiguity < 1e-12
    assert certificate.delay_ambiguity < 1e-12
    assert certificate.joint_ambiguity < 1e-12
    assert certificate.exact_joint_descent_certified


def test_exact_joint_table_is_unique():
    table = descended_joint_response_table(
        _exact_responses(), FINE_U, COARSE_U, B, FINE_T, COARSE_T, A
    )
    assert table["A"]["early"] == {0: 0.8, 1: 0.2}
    assert table["B"]["late"] == {0: 0.2, 1: 0.8}


def test_joint_ambiguity_is_bounded_by_sum_of_separate_ambiguities():
    certificate = joint_operational_quotient_certificate(
        _approximate_responses(), FINE_U, COARSE_U, B, FINE_T, COARSE_T, A
    )
    assert certificate.joint_ambiguity <= certificate.additive_upper_bound + 1e-12
    assert certificate.additive_upper_bound == pytest.approx(
        certificate.intervention_ambiguity + certificate.delay_ambiguity
    )


def test_joint_ambiguity_detects_product_fiber_variation():
    eta = joint_quotient_ambiguity(_approximate_responses(), FINE_U, B, FINE_T, A)
    assert eta > 0.0


def test_nonzero_joint_ambiguity_blocks_unique_joint_table():
    with pytest.raises(ValueError, match="do not descend exactly"):
        descended_joint_response_table(
            _approximate_responses(), FINE_U, COARSE_U, B, FINE_T, COARSE_T, A
        )


def test_geometry_bounds_are_correct():
    assert joint_geometry_selection_bound(0.08) == pytest.approx(0.16)
    assert additive_geometry_bound(0.03, 0.05) == pytest.approx(0.16)
