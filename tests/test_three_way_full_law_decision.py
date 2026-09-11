from fractions import Fraction
from pathlib import Path

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78DistanceBracket,
)
from consciousness_bridge.three_way_full_law_decision import (
    margin_resolution_is_guaranteed,
    p78_three_way_full_law_decision,
    three_way_full_law_decision,
    total_decision_uncertainty_width,
)


def _p78_bracket(lower: Fraction, upper: Fraction) -> P78DistanceBracket:
    return P78DistanceBracket(
        lower_bound=lower,
        upper_bound=upper,
        best_parameters=(Fraction(1, 2),) * 9,
        leaf_count=4,
        evaluated_boxes=7,
        iterations=3,
        maximum_active_width_sum=Fraction(1, 4),
        mesh_upper_bound=upper,
        certified_gap=upper - lower,
        conclusion="synthetic P79 integration bracket",
    )


def test_rejection_uses_distance_lower_and_radius_upper() -> None:
    certificate = three_way_full_law_decision(
        distance_lower_bound=Fraction(3, 20),
        distance_upper_bound=Fraction(9, 50),
        sampling_radius_lower_bound=Fraction(1, 10),
        sampling_radius_upper_bound=Fraction(3, 25),
    )

    assert certificate.decision == "reject"
    assert certificate.certified_rejection
    assert not certificate.certified_nonseparation
    assert not certificate.unresolved
    assert certificate.signed_margin_lower_bound == Fraction(3, 100)
    assert certificate.signed_margin_upper_bound == Fraction(2, 25)


def test_nonseparation_uses_distance_upper_and_radius_lower() -> None:
    certificate = three_way_full_law_decision(
        distance_lower_bound=Fraction(1, 50),
        distance_upper_bound=Fraction(2, 25),
        sampling_radius_lower_bound=Fraction(1, 10),
        sampling_radius_upper_bound=Fraction(3, 25),
    )

    assert certificate.decision == "nonseparation"
    assert not certificate.certified_rejection
    assert certificate.certified_nonseparation
    assert not certificate.unresolved
    assert certificate.signed_margin_upper_bound == Fraction(-1, 50)
    assert "not model acceptance" in certificate.conclusion


def test_unresolved_when_decision_boundary_is_inside_certified_interval() -> None:
    certificate = three_way_full_law_decision(
        distance_lower_bound=Fraction(2, 25),
        distance_upper_bound=Fraction(7, 50),
        sampling_radius_lower_bound=Fraction(1, 10),
        sampling_radius_upper_bound=Fraction(3, 25),
    )

    assert certificate.decision == "unresolved"
    assert not certificate.certified_rejection
    assert not certificate.certified_nonseparation
    assert certificate.unresolved
    assert certificate.signed_margin_lower_bound < 0
    assert certificate.signed_margin_upper_bound > 0


def test_touching_lower_rejection_boundary_does_not_reject() -> None:
    certificate = three_way_full_law_decision(
        distance_lower_bound=Fraction(1, 10),
        distance_upper_bound=Fraction(3, 20),
        sampling_radius_lower_bound=Fraction(9, 100),
        sampling_radius_upper_bound=Fraction(1, 10),
    )

    assert not certificate.certified_rejection
    assert certificate.unresolved


def test_candidate_on_closed_confidence_ball_certifies_nonseparation() -> None:
    certificate = three_way_full_law_decision(
        distance_lower_bound=Fraction(1, 20),
        distance_upper_bound=Fraction(1, 10),
        sampling_radius_lower_bound=Fraction(1, 10),
        sampling_radius_upper_bound=Fraction(3, 25),
    )

    assert certificate.certified_nonseparation
    assert certificate.signed_margin_upper_bound == 0


def test_p78_wrapper_preserves_exact_fraction_bounds() -> None:
    bracket = _p78_bracket(Fraction(7, 50), Fraction(3, 20))
    certificate = p78_three_way_full_law_decision(
        bracket,
        sampling_radius_lower_bound=Fraction(1, 10),
        sampling_radius_upper_bound=Fraction(3, 25),
    )

    assert certificate.certified_rejection
    assert certificate.distance_lower_bound == bracket.lower_bound
    assert certificate.distance_upper_bound == bracket.upper_bound


def test_total_decision_uncertainty_is_sum_of_two_bracket_widths() -> None:
    certificate = three_way_full_law_decision(
        distance_lower_bound=Fraction(2, 25),
        distance_upper_bound=Fraction(7, 50),
        sampling_radius_lower_bound=Fraction(1, 10),
        sampling_radius_upper_bound=Fraction(3, 25),
    )

    assert total_decision_uncertainty_width(certificate) == (
        Fraction(7, 50) - Fraction(2, 25)
        + Fraction(3, 25) - Fraction(1, 10)
    )


def test_margin_resolution_requires_total_gap_strictly_below_margin() -> None:
    assert margin_resolution_is_guaranteed(
        exact_signed_margin_magnitude=Fraction(1, 10),
        optimization_gap_upper_bound=Fraction(1, 20),
        sampling_radius_gap_upper_bound=Fraction(1, 100),
    )
    assert not margin_resolution_is_guaranteed(
        exact_signed_margin_magnitude=Fraction(3, 50),
        optimization_gap_upper_bound=Fraction(1, 20),
        sampling_radius_gap_upper_bound=Fraction(1, 100),
    )
    assert not margin_resolution_is_guaranteed(
        exact_signed_margin_magnitude=Fraction(0),
        optimization_gap_upper_bound=Fraction(0),
    )


def test_invalid_bounds_are_rejected() -> None:
    with pytest.raises(ValueError, match="distance bounds"):
        three_way_full_law_decision(
            distance_lower_bound=Fraction(1, 5),
            distance_upper_bound=Fraction(1, 10),
            sampling_radius_lower_bound=Fraction(1, 20),
            sampling_radius_upper_bound=Fraction(1, 10),
        )
    with pytest.raises(ValueError, match="sampling-radius bounds"):
        three_way_full_law_decision(
            distance_lower_bound=Fraction(1, 20),
            distance_upper_bound=Fraction(1, 10),
            sampling_radius_lower_bound=Fraction(1, 5),
            sampling_radius_upper_bound=Fraction(1, 10),
        )
    with pytest.raises(TypeError, match="fractions.Fraction"):
        three_way_full_law_decision(
            distance_lower_bound=0.1,  # type: ignore[arg-type]
            distance_upper_bound=Fraction(1, 5),
            sampling_radius_lower_bound=Fraction(1, 20),
            sampling_radius_upper_bound=Fraction(1, 10),
        )


def test_source_preserves_statistical_and_scientific_boundaries() -> None:
    source = Path(
        "src/consciousness_bridge/three_way_full_law_decision.py"
    ).read_text(encoding="utf-8")

    required = (
        "certified non-separation result",
        "It is not model acceptance",
        "two-sided radius certification",
        "does not identify the P75 latent state with consciousness",
        "does not validate the target-measurement model after non-separation",
        "does not solve the physical-to-experiential bridge",
    )
    for token in required:
        assert token in source, token
