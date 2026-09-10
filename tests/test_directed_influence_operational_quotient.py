import pytest

from consciousness_bridge.directed_influence_operational_quotient import (
    directed_influence_operational_certificate,
    directed_influence_representative_bound,
    full_directed_influence_upper_bound,
    separate_audit_directed_influence_upper_bound,
    threshold_margin_certified,
)


def test_representative_bound_is_two_eta():
    assert directed_influence_representative_bound(0.04) == pytest.approx(0.08)


def test_full_bound_adds_node_state_and_operational_terms():
    assert full_directed_influence_upper_bound(0.03, 0.04) == pytest.approx(0.14)


def test_separate_audits_recover_p33_additive_corollary():
    assert separate_audit_directed_influence_upper_bound(0.03, 0.01, 0.03) == pytest.approx(0.14)


def test_threshold_margin_certificate():
    assert threshold_margin_certified(0.8, 0.5, 0.2)
    assert not threshold_margin_certified(0.6, 0.5, 0.2)


def test_semantic_failure_blocks_threshold_certificate():
    certificate = directed_influence_operational_certificate(
        rho_directed=0.02,
        joint_ambiguity=0.01,
        source_semantics_descend=False,
        influence_value=0.9,
        threshold=0.5,
    )
    assert certificate.full_upper_bound == pytest.approx(0.06)
    assert certificate.threshold_margin == pytest.approx(0.4)
    assert not certificate.threshold_classification_certified


def test_semantically_valid_large_margin_is_certified():
    certificate = directed_influence_operational_certificate(
        rho_directed=0.02,
        joint_ambiguity=0.01,
        source_semantics_descend=True,
        influence_value=0.9,
        threshold=0.5,
    )
    assert certificate.threshold_classification_certified


def test_threshold_arguments_must_be_supplied_together():
    with pytest.raises(ValueError, match="supplied together"):
        directed_influence_operational_certificate(
            rho_directed=0.02,
            joint_ambiguity=0.01,
            source_semantics_descend=True,
            influence_value=0.9,
        )
