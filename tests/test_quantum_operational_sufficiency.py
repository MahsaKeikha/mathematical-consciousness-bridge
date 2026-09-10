import pytest

from consciousness_bridge.quantum_operational_sufficiency import (
    deterministic_nonfactorization_witnesses,
    deterministic_quantum_sufficiency,
    stochastic_quantum_sufficiency,
)


def test_deterministic_target_factors_when_constant_on_quantum_state_fibers():
    preparations = ("x0", "x1", "x2")
    state = {"x0": "rhoA", "x1": "rhoA", "x2": "rhoB"}
    target = {"x0": 0, "x1": 0, "x2": 1}
    certificate = deterministic_quantum_sufficiency(preparations, state, target)
    assert certificate.sufficient
    assert certificate.collision_count == 0


def test_equal_quantum_state_unequal_target_is_nonfactorization_witness():
    preparations = ("x0", "x1", "x2")
    state = {"x0": "rhoA", "x1": "rhoA", "x2": "rhoB"}
    target = {"x0": 0, "x1": 1, "x2": 1}
    certificate = deterministic_quantum_sufficiency(preparations, state, target)
    assert not certificate.sufficient
    assert certificate.collision_count == 1
    assert deterministic_nonfactorization_witnesses(preparations, state, target) == [("x0", "x1")]


def test_stochastic_target_sufficiency_requires_equal_target_laws_within_state_fiber():
    preparations = ("x0", "x1", "x2")
    state = {"x0": "rhoA", "x1": "rhoA", "x2": "rhoB"}
    target_laws = {
        "x0": {0: 0.8, 1: 0.2},
        "x1": {0: 0.8, 1: 0.2},
        "x2": {0: 0.2, 1: 0.8},
    }
    certificate = stochastic_quantum_sufficiency(preparations, state, target_laws)
    assert certificate.sufficient
    assert certificate.maximum_within_state_target_tv < 1e-12


def test_stochastic_residual_detects_within_state_target_difference():
    preparations = ("x0", "x1")
    state = {"x0": "rhoA", "x1": "rhoA"}
    target_laws = {
        "x0": {0: 0.8, 1: 0.2},
        "x1": {0: 0.6, 1: 0.4},
    }
    certificate = stochastic_quantum_sufficiency(preparations, state, target_laws)
    assert not certificate.sufficient
    assert certificate.maximum_within_state_target_tv == pytest.approx(0.2)


def test_invalid_distribution_is_rejected():
    with pytest.raises(ValueError, match="sum to one"):
        stochastic_quantum_sufficiency(
            ("x0", "x1"),
            {"x0": "rhoA", "x1": "rhoA"},
            {"x0": {0: 0.8}, "x1": {0: 0.5, 1: 0.5}},
        )
