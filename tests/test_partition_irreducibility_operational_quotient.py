import pytest

from consciousness_bridge.partition_irreducibility_operational_quotient import (
    fixed_partition_irreducibility_bound,
    full_partition_irreducibility_upper_bound,
    partition_operational_certificate,
    product_reference_perturbation_bound,
    separate_audit_partition_upper_bound,
)


def test_product_reference_bound_scales_with_block_count():
    assert product_reference_perturbation_bound(3, 0.02) == pytest.approx(0.06)


def test_fixed_partition_bound_is_m_plus_one_eta():
    assert fixed_partition_irreducibility_bound(3, 0.02) == pytest.approx(0.08)


def test_full_partition_bound_adds_node_and_operational_terms():
    bound = full_partition_irreducibility_upper_bound(
        rho_response=0.01,
        rho_partition_reference=0.03,
        max_block_count=3,
        joint_ambiguity=0.02,
    )
    assert bound == pytest.approx(0.12)


def test_separate_audits_use_p33_additive_bound():
    bound = separate_audit_partition_upper_bound(
        rho_response=0.01,
        rho_partition_reference=0.03,
        max_block_count=3,
        intervention_ambiguity=0.005,
        delay_ambiguity=0.015,
    )
    assert bound == pytest.approx(0.12)


def test_certificate_keeps_semantic_status_separate_from_number():
    certificate = partition_operational_certificate(
        rho_response=0.01,
        rho_partition_reference=0.03,
        block_count=2,
        joint_ambiguity=0.02,
        partition_semantics_descend=False,
    )
    assert certificate.node_state_bound == pytest.approx(0.04)
    assert certificate.operational_ambiguity_bound == pytest.approx(0.06)
    assert certificate.full_upper_bound == pytest.approx(0.10)
    assert not certificate.partition_semantics_descend


def test_invalid_block_count_is_rejected():
    with pytest.raises(ValueError, match="at least 1"):
        fixed_partition_irreducibility_bound(0, 0.01)
