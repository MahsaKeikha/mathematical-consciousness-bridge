from math import log

import pytest

from consciousness_bridge.descriptor_refinement_residual import (
    descriptor_refinement_violations,
    is_descriptor_refinement,
    refinement_chain_residuals,
    refinement_collision_sets,
    refinement_residual_decomposition,
    unresolved_target_collision_pairs,
)


def test_refinement_requires_coarse_to_be_function_of_fine():
    coarse = ["left", "left", "right", "right"]
    fine = ["a", "b", "c", "d"]

    assert is_descriptor_refinement(coarse, fine)
    assert descriptor_refinement_violations(coarse, fine) == []


def test_refinement_violation_returns_explicit_witness():
    coarse = ["left", "right", "right"]
    fine = ["same", "same", "other"]

    assert descriptor_refinement_violations(coarse, fine) == [(0, 1)]
    assert not is_descriptor_refinement(coarse, fine)


def test_target_collision_set_shrinks_under_refinement():
    coarse = ["c", "c", "c", "c"]
    fine = ["a", "a", "b", "b"]
    target = [0, 1, 0, 0]

    coarse_collisions, fine_collisions = refinement_collision_sets(
        coarse, fine, target
    )

    assert fine_collisions == {(0, 1)}
    assert fine_collisions < coarse_collisions
    assert unresolved_target_collision_pairs(fine, target) == fine_collisions


def test_invalid_refinement_is_rejected_before_collision_comparison():
    with pytest.raises(ValueError, match="do not refine"):
        refinement_collision_sets(
            coarse_labels=["a", "b"],
            fine_labels=["same", "same"],
            target_labels=[0, 1],
        )


def test_refinement_residual_decomposition_closes_exactly():
    records = [
        (0, "coarse", "a", 0),
        (1, "coarse", "a", 1),
        (2, "coarse", "b", 0),
        (3, "coarse", "b", 0),
    ]

    certificate = refinement_residual_decomposition(records)

    assert certificate.coarse_residual > certificate.fine_residual > 0.0
    assert certificate.captured_by_refinement > 0.0
    assert certificate.coarse_residual == pytest.approx(
        certificate.fine_residual + certificate.captured_by_refinement
    )
    assert certificate.decomposition_error < 1e-12
    assert certificate.residual_persists


def test_fine_descriptor_can_remove_the_entire_coarse_residual():
    records = [
        (0, "coarse", "e0", 0),
        (1, "coarse", "e1", 1),
        (2, "coarse", "e0", 0),
        (3, "coarse", "e1", 1),
    ]

    certificate = refinement_residual_decomposition(records)

    assert certificate.coarse_residual == pytest.approx(log(2.0))
    assert certificate.fine_residual == pytest.approx(0.0, abs=1e-12)
    assert certificate.captured_by_refinement == pytest.approx(log(2.0))
    assert not certificate.residual_persists


def test_target_irrelevant_refinement_leaves_residual_unchanged():
    records = [
        (0, "coarse", "a", 0),
        (1, "coarse", "a", 1),
        (2, "coarse", "b", 0),
        (3, "coarse", "b", 1),
    ]

    certificate = refinement_residual_decomposition(records)

    assert certificate.coarse_residual == pytest.approx(log(2.0))
    assert certificate.fine_residual == pytest.approx(log(2.0))
    assert certificate.captured_by_refinement == pytest.approx(0.0, abs=1e-12)
    assert certificate.residual_persists


def test_nested_refinement_chain_has_monotone_residual_and_telescoping_gain():
    records = [
        (0, ("all", "a", ("a", 0)), 0),
        (1, ("all", "a", ("a", 1)), 1),
        (2, ("all", "b", ("b", 0)), 0),
        (3, ("all", "b", ("b", 0)), 0),
    ]

    certificate = refinement_chain_residuals(records)

    assert len(certificate.residuals) == 3
    assert len(certificate.captured_increments) == 2
    assert certificate.residuals[0] > certificate.residuals[1] > 0.0
    assert certificate.residuals[2] == pytest.approx(0.0, abs=1e-12)
    assert certificate.monotone
    assert certificate.telescoping_error < 1e-12
    assert certificate.residuals[0] == pytest.approx(
        sum(certificate.captured_increments)
    )


def test_pairwise_decomposition_rejects_nonphysical_labeling_of_same_state():
    records = [
        ("omega", "c", "fine-a", 0),
        ("omega", "c", "fine-b", 1),
    ]

    with pytest.raises(ValueError, match="deterministic function of omega"):
        refinement_residual_decomposition(records)


def test_pairwise_decomposition_rejects_non_nested_descriptors():
    records = [
        (0, "coarse-a", "same", 0),
        (1, "coarse-b", "same", 1),
    ]

    with pytest.raises(ValueError, match="coarse must be"):
        refinement_residual_decomposition(records)


def test_chain_validation_rejects_empty_and_inconsistent_paths():
    with pytest.raises(ValueError, match="at least one sample"):
        refinement_chain_residuals([])

    with pytest.raises(ValueError, match="same length"):
        refinement_chain_residuals(
            [
                (0, ("a", "b"), 0),
                (1, ("a",), 1),
            ]
        )


def test_negative_tolerance_is_rejected():
    with pytest.raises(ValueError, match="non-negative"):
        refinement_residual_decomposition(
            [(0, "c", "f", 0)], tolerance=-1.0
        )

    with pytest.raises(ValueError, match="non-negative"):
        refinement_chain_residuals(
            [(0, ("c",), 0)], tolerance=-1.0
        )
