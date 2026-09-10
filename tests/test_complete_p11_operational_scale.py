import pytest

from consciousness_bridge.complete_p11_operational_scale import (
    complete_component_bounds,
    complete_p11_scale_certificate,
    complete_uniform_bound,
    separate_audit_uniform_bound,
)


def test_complete_component_bounds():
    geometry, directed, partition = complete_component_bounds(
        rho_geometry=0.02,
        rho_directed=0.03,
        rho_response=0.01,
        rho_partition_reference=0.02,
        max_block_count=3,
        joint_ambiguity=0.01,
    )
    assert geometry == pytest.approx(0.06)
    assert directed == pytest.approx(0.08)
    assert partition == pytest.approx(0.07)


def test_uniform_bound_is_component_maximum():
    bound = complete_uniform_bound(
        rho_geometry=0.02,
        rho_directed=0.03,
        rho_response=0.01,
        rho_partition_reference=0.02,
        max_block_count=3,
        joint_ambiguity=0.01,
    )
    assert bound == pytest.approx(0.08)


def test_separate_audit_bound_uses_eta_b_plus_eta_a():
    bound = separate_audit_uniform_bound(
        rho_geometry=0.02,
        rho_directed=0.03,
        rho_response=0.01,
        rho_partition_reference=0.02,
        max_block_count=3,
        intervention_ambiguity=0.004,
        delay_ambiguity=0.006,
    )
    assert bound == pytest.approx(0.08)


def test_delta_stability_requires_semantics_and_numeric_margin():
    certificate = complete_p11_scale_certificate(
        rho_geometry=0.02,
        rho_directed=0.03,
        rho_response=0.01,
        rho_partition_reference=0.02,
        max_block_count=3,
        joint_ambiguity=0.01,
        semantic_validity=True,
        tolerance_delta=0.10,
    )
    assert certificate.delta_stable

    invalid = complete_p11_scale_certificate(
        rho_geometry=0.02,
        rho_directed=0.03,
        rho_response=0.01,
        rho_partition_reference=0.02,
        max_block_count=3,
        joint_ambiguity=0.01,
        semantic_validity=False,
        tolerance_delta=0.10,
    )
    assert not invalid.delta_stable


def test_exact_limit_recovers_p30_budget_structure():
    certificate = complete_p11_scale_certificate(
        rho_geometry=0.02,
        rho_directed=0.03,
        rho_response=0.01,
        rho_partition_reference=0.02,
        max_block_count=5,
        joint_ambiguity=0.0,
        semantic_validity=True,
    )
    assert certificate.geometry_bound == pytest.approx(0.04)
    assert certificate.directed_influence_bound == pytest.approx(0.06)
    assert certificate.partition_bound == pytest.approx(0.03)
    assert certificate.uniform_bound == pytest.approx(0.06)


def test_invalid_block_count_rejected():
    with pytest.raises(ValueError, match="at least 1"):
        complete_uniform_bound(
            rho_geometry=0.0,
            rho_directed=0.0,
            rho_response=0.0,
            rho_partition_reference=0.0,
            max_block_count=0,
            joint_ambiguity=0.0,
        )
