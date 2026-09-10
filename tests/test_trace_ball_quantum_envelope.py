import pytest

from consciousness_bridge.trace_ball_quantum_envelope import (
    lipschitz_trace_ball_pair_certificate,
    target_pairwise_lower_bound,
    trace_ball_global_lipschitz_certificate,
    trace_ball_pairwise_upper_bound,
)

PREPARATIONS = ("x0", "x1", "x2")
QDIST = {
    ("x0", "x1"): 0.08,
    ("x0", "x2"): 0.30,
    ("x1", "x2"): 0.25,
}
QRAD = {"x0": 0.01, "x1": 0.02, "x2": 0.03}
YDIST = {
    ("x0", "x1"): 0.42,
    ("x0", "x2"): 0.20,
    ("x1", "x2"): 0.18,
}
YRAD = {"x0": 0.03, "x1": 0.04, "x2": 0.03}


def test_trace_ball_upper_bound_adds_both_radii():
    assert trace_ball_pairwise_upper_bound(0.08, 0.01, 0.02) == pytest.approx(0.11)


def test_trace_ball_upper_bound_clips_at_one():
    assert trace_ball_pairwise_upper_bound(0.9, 0.2, 0.1) == 1.0


def test_target_lower_bound_subtracts_both_radii():
    assert target_pairwise_lower_bound(0.42, 0.03, 0.04) == pytest.approx(0.35)


def test_target_lower_bound_clips_at_zero():
    assert target_pairwise_lower_bound(0.04, 0.03, 0.03) == 0.0


def test_pairwise_lipschitz_obstruction_is_end_to_end():
    certificate = lipschitz_trace_ball_pair_certificate(
        0.08,
        0.01,
        0.02,
        0.42,
        0.03,
        0.04,
        2.0,
    )
    assert certificate.quantum_distance_upper_bound == pytest.approx(0.11)
    assert certificate.target_separation_lower_bound == pytest.approx(0.35)
    assert certificate.allowed_target_variation == pytest.approx(0.22)
    assert certificate.obstruction_margin == pytest.approx(0.13)
    assert certificate.certified


def test_larger_bridge_lipschitz_constant_can_remove_obstruction():
    certificate = lipschitz_trace_ball_pair_certificate(
        0.08,
        0.01,
        0.02,
        0.42,
        0.03,
        0.04,
        4.0,
    )
    assert not certificate.certified


def test_global_certificate_finds_best_witness_pair_and_union_bound():
    certificate = trace_ball_global_lipschitz_certificate(
        PREPARATIONS,
        QDIST,
        QRAD,
        YDIST,
        YRAD,
        2.0,
        alpha_quantum=0.02,
        alpha_target=0.03,
    )
    assert certificate.certified
    assert certificate.maximum_obstruction_margin == pytest.approx(0.13)
    assert certificate.witness_pair_count == 1
    assert certificate.confidence_lower_bound == pytest.approx(0.95)


def test_reversed_pair_keys_are_accepted():
    reversed_q = {("x1", "x0"): 0.08, ("x2", "x0"): 0.30, ("x2", "x1"): 0.25}
    certificate = trace_ball_global_lipschitz_certificate(
        PREPARATIONS,
        reversed_q,
        QRAD,
        YDIST,
        YRAD,
        2.0,
        alpha_quantum=0.01,
        alpha_target=0.01,
    )
    assert certificate.certified


def test_invalid_distances_radii_domains_and_lipschitz_constant_are_rejected():
    with pytest.raises(ValueError):
        trace_ball_pairwise_upper_bound(1.1, 0.01, 0.01)
    with pytest.raises(ValueError):
        lipschitz_trace_ball_pair_certificate(0.1, 0.1, 0.1, 0.2, 0.1, 0.1, -1.0)
    with pytest.raises(ValueError):
        trace_ball_global_lipschitz_certificate(
            PREPARATIONS,
            {("x0", "x1"): 0.1},
            QRAD,
            YDIST,
            YRAD,
            1.0,
            alpha_quantum=0.01,
            alpha_target=0.01,
        )
