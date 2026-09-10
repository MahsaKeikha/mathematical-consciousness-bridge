import pytest

from consciousness_bridge.joint_p11_operational_scale import (
    exact_component_bounds,
    full_geometry_upper_bound,
    joint_p11_operational_scale_certificate,
    p30_uniform_budget,
    separate_audit_geometry_upper_bound,
)


def test_p30_uniform_budget_matches_component_maximum():
    assert p30_uniform_budget(0.02, 0.03, 0.01, 0.04) == pytest.approx(0.06)


def test_exact_joint_descent_preserves_full_p11_certificate():
    certificate = joint_p11_operational_scale_certificate(
        rho_geometry=0.02,
        rho_directed=0.03,
        rho_response=0.01,
        rho_partition_reference=0.04,
        joint_ambiguity=0.0,
        p30_conditions_hold=True,
        directed_semantics_descend=True,
        partition_domain_descends=True,
    )
    assert certificate.joint_response_descent_holds
    assert certificate.exact_full_p11_descent_certified
    assert certificate.p30_uniform_budget == pytest.approx(0.06)
    assert certificate.geometry_full_upper_bound == pytest.approx(0.04)


def test_nonzero_joint_ambiguity_blocks_exact_full_signature_descent():
    certificate = joint_p11_operational_scale_certificate(
        rho_geometry=0.02,
        rho_directed=0.03,
        rho_response=0.01,
        rho_partition_reference=0.04,
        joint_ambiguity=0.05,
        p30_conditions_hold=True,
        directed_semantics_descend=True,
        partition_domain_descends=True,
    )
    assert not certificate.joint_response_descent_holds
    assert not certificate.exact_full_p11_descent_certified
    assert certificate.geometry_full_upper_bound == pytest.approx(0.14)


def test_semantic_failure_blocks_exact_descent_even_with_zero_ambiguity():
    certificate = joint_p11_operational_scale_certificate(
        rho_geometry=0.0,
        rho_directed=0.0,
        rho_response=0.0,
        rho_partition_reference=0.0,
        joint_ambiguity=0.0,
        p30_conditions_hold=True,
        directed_semantics_descend=False,
        partition_domain_descends=True,
    )
    assert not certificate.exact_full_p11_descent_certified


def test_geometry_bound_adds_node_state_and_operational_ambiguity():
    assert full_geometry_upper_bound(0.03, 0.04) == pytest.approx(0.14)
    assert separate_audit_geometry_upper_bound(0.03, 0.01, 0.03) == pytest.approx(0.14)


def test_exact_component_bounds_require_exact_full_certificate():
    with pytest.raises(ValueError, match="requires exact operational descent"):
        exact_component_bounds(
            0.02,
            0.03,
            0.01,
            0.04,
            exact_full_p11_descent_certified=False,
        )

    bounds = exact_component_bounds(
        0.02,
        0.03,
        0.01,
        0.04,
        exact_full_p11_descent_certified=True,
    )
    assert bounds["geometry"] == pytest.approx(0.04)
    assert bounds["directed_influence"] == pytest.approx(0.06)
    assert bounds["partition_irreducibility"] == pytest.approx(0.05)


def test_negative_budget_is_rejected():
    with pytest.raises(ValueError, match="nonnegative"):
        full_geometry_upper_bound(-0.01, 0.0)
