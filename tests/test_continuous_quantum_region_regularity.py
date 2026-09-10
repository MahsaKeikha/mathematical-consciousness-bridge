import pytest

from consciousness_bridge.continuous_quantum_region_regularity import (
    continuous_region_regularity_certificate,
    injective_descriptor_allows_unrestricted_factorization,
    lipschitz_modulus_values,
    regularity_obstruction_margin,
)

PREPARATIONS = ("x0", "x1", "x2")
QUANTUM_UPPER = {
    ("x0", "x1"): 0.10,
    ("x0", "x2"): 0.25,
    ("x1", "x2"): 0.20,
}
TARGET_LOWER = {
    ("x0", "x1"): 0.35,
    ("x0", "x2"): 0.20,
    ("x1", "x2"): 0.12,
}


def test_injective_descriptor_allows_unrestricted_factorization():
    distances = {
        ("x0", "x1"): 0.01,
        ("x0", "x2"): 0.02,
        ("x1", "x2"): 0.03,
    }
    assert injective_descriptor_allows_unrestricted_factorization(
        PREPARATIONS, distances
    )


def test_zero_distance_breaks_injective_descriptor():
    distances = {
        ("x0", "x1"): 0.0,
        ("x0", "x2"): 0.02,
        ("x1", "x2"): 0.03,
    }
    assert not injective_descriptor_allows_unrestricted_factorization(
        PREPARATIONS, distances
    )


def test_regularity_obstruction_margin_is_target_minus_allowed_variation():
    assert regularity_obstruction_margin(0.35, 0.10, 0.20) == pytest.approx(0.15)


def test_lipschitz_bridge_can_be_ruled_out_by_one_pair():
    modulus = lipschitz_modulus_values(PREPARATIONS, QUANTUM_UPPER, 2.0)
    certificate = continuous_region_regularity_certificate(
        PREPARATIONS,
        TARGET_LOWER,
        QUANTUM_UPPER,
        modulus,
    )
    assert certificate.certified
    assert certificate.maximum_obstruction_margin == pytest.approx(0.15)
    assert certificate.witness_pair_count == 1


def test_larger_lipschitz_class_can_remove_obstruction():
    modulus = lipschitz_modulus_values(PREPARATIONS, QUANTUM_UPPER, 4.0)
    certificate = continuous_region_regularity_certificate(
        PREPARATIONS,
        TARGET_LOWER,
        QUANTUM_UPPER,
        modulus,
    )
    assert not certificate.certified
    assert certificate.maximum_obstruction_margin <= 0.0


def test_reversed_pair_keys_are_accepted():
    reversed_quantum = {
        ("x1", "x0"): 0.10,
        ("x2", "x0"): 0.25,
        ("x2", "x1"): 0.20,
    }
    modulus = lipschitz_modulus_values(PREPARATIONS, reversed_quantum, 2.0)
    certificate = continuous_region_regularity_certificate(
        PREPARATIONS,
        TARGET_LOWER,
        reversed_quantum,
        modulus,
    )
    assert certificate.certified


def test_tolerance_can_suppress_numerical_boundary_only():
    target = {
        ("x0", "x1"): 0.2000000000001,
        ("x0", "x2"): 0.10,
        ("x1", "x2"): 0.10,
    }
    quantum = {
        ("x0", "x1"): 0.10,
        ("x0", "x2"): 0.10,
        ("x1", "x2"): 0.10,
    }
    modulus = lipschitz_modulus_values(PREPARATIONS, quantum, 2.0)
    certificate = continuous_region_regularity_certificate(
        PREPARATIONS, target, quantum, modulus, tolerance=1e-12
    )
    assert not certificate.certified


def test_missing_pair_and_invalid_values_are_rejected():
    with pytest.raises(ValueError):
        continuous_region_regularity_certificate(
            PREPARATIONS,
            {( "x0", "x1"): 0.2},
            QUANTUM_UPPER,
            lipschitz_modulus_values(PREPARATIONS, QUANTUM_UPPER, 1.0),
        )
    with pytest.raises(ValueError):
        lipschitz_modulus_values(PREPARATIONS, QUANTUM_UPPER, -1.0)
    with pytest.raises(ValueError):
        regularity_obstruction_margin(1.1, 0.1, 0.1)
