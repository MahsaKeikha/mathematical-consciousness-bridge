import pytest

from consciousness_bridge.finite_data_quantum_nonfactorization import (
    model_set_nonfactorization_certificate,
    quantum_model_violation_margin,
    target_separation_lower_bound,
)

PREPARATIONS = ("x0", "x1", "x2")
TARGETS = {
    "x0": {0: 0.90, 1: 0.10},
    "x1": {0: 0.20, 1: 0.80},
    "x2": {0: 0.35, 1: 0.65},
}
RADII = {"x0": 0.05, "x1": 0.05, "x2": 0.05}


def test_target_separation_subtracts_both_confidence_radii():
    lower = target_separation_lower_bound(
        TARGETS["x0"], TARGETS["x1"], 0.05, 0.05
    )
    assert lower == pytest.approx(0.60)


def test_target_separation_lower_bound_clips_at_zero():
    lower = target_separation_lower_bound(
        {0: 0.52, 1: 0.48}, {0: 0.50, 1: 0.50}, 0.03, 0.03
    )
    assert lower == 0.0


def test_same_quantum_state_pair_yields_positive_violation_margin():
    state_labels = {"x0": "q0", "x1": "q0", "x2": "q1"}
    margin = quantum_model_violation_margin(
        PREPARATIONS, state_labels, TARGETS, RADII
    )
    assert margin == pytest.approx(0.60)


def test_injective_quantum_model_has_no_collision_certificate():
    state_labels = {"x0": "q0", "x1": "q1", "x2": "q2"}
    margin = quantum_model_violation_margin(
        PREPARATIONS, state_labels, TARGETS, RADII
    )
    assert margin == 0.0


def test_every_confidence_model_must_be_violated_for_robust_certificate():
    models = {
        "h01": {"x0": "q0", "x1": "q0", "x2": "q1"},
        "h02": {"x0": "q0", "x1": "q1", "x2": "q0"},
    }
    certificate = model_set_nonfactorization_certificate(
        PREPARATIONS,
        models,
        ("h01", "h02"),
        TARGETS,
        RADII,
        alpha_quantum=0.02,
        alpha_target=0.03,
    )
    assert certificate.certified
    assert certificate.model_count == 2
    assert certificate.violating_model_count == 2
    assert certificate.robust_violation_margin == pytest.approx(0.45)
    assert certificate.confidence_lower_bound == pytest.approx(0.95)


def test_one_injective_confidence_model_blocks_nonfactorization_certificate():
    models = {
        "collision": {"x0": "q0", "x1": "q0", "x2": "q1"},
        "injective": {"x0": "a", "x1": "b", "x2": "c"},
    }
    certificate = model_set_nonfactorization_certificate(
        PREPARATIONS,
        models,
        ("collision", "injective"),
        TARGETS,
        RADII,
        alpha_quantum=0.01,
        alpha_target=0.04,
    )
    assert not certificate.certified
    assert certificate.violating_model_count == 1
    assert certificate.robust_violation_margin == 0.0


def test_large_target_uncertainty_can_remove_a_nominal_collision_signal():
    state_labels = {"x0": "q0", "x1": "q0", "x2": "q1"}
    radii = {"x0": 0.40, "x1": 0.40, "x2": 0.05}
    margin = quantum_model_violation_margin(
        PREPARATIONS, state_labels, TARGETS, radii
    )
    assert margin == 0.0


def test_union_bound_confidence_is_never_negative():
    models = {"h": {"x0": "q0", "x1": "q0", "x2": "q1"}}
    certificate = model_set_nonfactorization_certificate(
        PREPARATIONS,
        models,
        ("h",),
        TARGETS,
        RADII,
        alpha_quantum=0.70,
        alpha_target=0.60,
    )
    assert certificate.confidence_lower_bound == 0.0


def test_invalid_domains_radii_and_confidence_models_are_rejected():
    model = {"x0": "q0", "x1": "q0", "x2": "q1"}
    with pytest.raises(ValueError):
        quantum_model_violation_margin(
            PREPARATIONS,
            model,
            TARGETS,
            {"x0": -0.1, "x1": 0.05, "x2": 0.05},
        )
    with pytest.raises(ValueError):
        model_set_nonfactorization_certificate(
            PREPARATIONS,
            {"h": model},
            ("missing",),
            TARGETS,
            RADII,
            alpha_quantum=0.01,
            alpha_target=0.01,
        )
    with pytest.raises(ValueError):
        model_set_nonfactorization_certificate(
            PREPARATIONS,
            {"h": model},
            (),
            TARGETS,
            RADII,
            alpha_quantum=0.01,
            alpha_target=0.01,
        )
