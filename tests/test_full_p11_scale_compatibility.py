import pytest

from consciousness_bridge.full_p11_scale_compatibility import (
    p11_scale_compatibility_certificate,
    uniform_p11_bound,
)


BASE = {
    "fine_nodes": (0, 1, 2),
    "coarse_nodes": ("A", "B"),
    "aggregation": {0: "A", 1: "A", 2: "B"},
    "intervention_labels": ("u0", "u1", "u2"),
    "delay_labels": ("t1", "t2"),
    "partition_semantics_compatible": True,
    "source_pair_semantics_compatible": True,
    "response_grid_compatible": True,
    "common_state_map_declared": True,
    "common_reconstruction_family_declared": True,
    "geometry_distortion": 0.08,
    "geometry_bound": 0.10,
    "influence_distortion": 0.05,
    "influence_bound": 0.06,
    "partition_distortion": 0.07,
    "partition_bound": 0.09,
}


def test_complete_semantic_and_quantitative_alignment_certifies_transport():
    certificate = p11_scale_compatibility_certificate(**BASE)
    assert certificate.semantic_compatibility_certified
    assert certificate.quantitative_bounds_certified
    assert certificate.full_declared_p11_transport_certified
    assert certificate.p11_distortion == pytest.approx(0.08)
    assert certificate.p11_reconstruction_bound == pytest.approx(0.10)


def test_one_semantic_failure_blocks_full_transport_even_when_bounds_hold():
    values = dict(BASE)
    values["source_pair_semantics_compatible"] = False
    certificate = p11_scale_compatibility_certificate(**values)
    assert certificate.quantitative_bounds_certified
    assert not certificate.semantic_compatibility_certified
    assert not certificate.full_declared_p11_transport_certified


def test_one_exceeded_component_bound_blocks_quantitative_certificate():
    values = dict(BASE)
    values["partition_distortion"] = 0.11
    certificate = p11_scale_compatibility_certificate(**values)
    assert certificate.semantic_compatibility_certified
    assert not certificate.quantitative_bounds_certified
    assert not certificate.full_declared_p11_transport_certified


def test_exact_preservation_requires_all_three_observed_distortions_to_vanish():
    values = dict(BASE)
    for key in ("geometry_distortion", "influence_distortion", "partition_distortion"):
        values[key] = 0.0
    certificate = p11_scale_compatibility_certificate(**values)
    assert certificate.exact_declared_p11_preservation_certified


def test_exact_preservation_is_not_claimed_for_nonzero_distortion():
    certificate = p11_scale_compatibility_certificate(**BASE)
    assert not certificate.exact_declared_p11_preservation_certified


def test_uniform_bound_is_maximum_of_three_existing_theorem_budgets():
    bound = uniform_p11_bound(
        geometry_reconstruction_defect=0.04,
        influence_reconstruction_defect=0.03,
        response_reconstruction_defect=0.02,
        product_reconstruction_defect=0.07,
    )
    assert bound == pytest.approx(0.09)


def test_uniform_bound_rejects_negative_defects():
    with pytest.raises(ValueError, match="nonnegative"):
        uniform_p11_bound(
            geometry_reconstruction_defect=-0.01,
            influence_reconstruction_defect=0.0,
            response_reconstruction_defect=0.0,
            product_reconstruction_defect=0.0,
        )


def test_aggregation_must_be_surjective():
    values = dict(BASE)
    values["aggregation"] = {0: "A", 1: "A", 2: "A"}
    with pytest.raises(ValueError, match="surjective"):
        p11_scale_compatibility_certificate(**values)


def test_declared_intervention_and_delay_grids_must_be_nonempty_and_unique():
    values = dict(BASE)
    values["intervention_labels"] = ("u0", "u0")
    with pytest.raises(ValueError, match="unique"):
        p11_scale_compatibility_certificate(**values)

    values = dict(BASE)
    values["delay_labels"] = ()
    with pytest.raises(ValueError, match="nonempty"):
        p11_scale_compatibility_certificate(**values)
