from fractions import Fraction
from itertools import product
from pathlib import Path

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    p75_four_view_law_exact,
)
from consciousness_bridge.projection_parity_contrast_separation import (
    certified_p75_linf_branch_and_bound_parity_contrast,
    empirical_projection_parity_contrast_exact,
    empirical_projection_parity_expectation_exact,
    p75_box_p84_linf_lower_bound_exact,
    p75_box_projection_parity_contrast_linf_lower_bound_exact,
    p75_box_projection_parity_contrast_witness_exact,
    p75_projection_parity_expectation_contrast_interval_exact,
    p84_dominates_p83_on_box,
    p84_standard_contrast_count,
)
from consciousness_bridge.projection_parity_model_separation import (
    p75_box_p83_linf_lower_bound_exact,
)


def _strict_witness_box() -> P78ParameterBox:
    lower = [Fraction(0)] * 9
    upper = [Fraction(1)] * 9
    fixed = {
        3: Fraction(1, 4),
        4: Fraction(3, 4),
        5: Fraction(1, 4),
        6: Fraction(3, 4),
    }
    for index, value in fixed.items():
        lower[index] = value
        upper[index] = value
    return P78ParameterBox(tuple(lower), tuple(upper))


def _strict_witness_empirical_law() -> tuple[Fraction, ...]:
    masses = [Fraction(0)] * 16
    masses[3] = Fraction(3, 16)
    masses[7] = Fraction(3, 16)
    masses[9] = Fraction(1, 16)
    masses[12] = Fraction(3, 16)
    masses[14] = Fraction(5, 16)
    masses[15] = Fraction(1, 16)
    return tuple(masses)


def _all_box_vertices(box: P78ParameterBox) -> tuple[tuple[Fraction, ...], ...]:
    coordinates = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    return tuple(product(*coordinates))


def test_p84_standard_family_contains_55_pairwise_parity_contrasts() -> None:
    assert p84_standard_contrast_count() == 55


def test_p84_contrast_interval_matches_exhaustive_parameter_box_vertices() -> None:
    box = P78ParameterBox(
        lower=(
            Fraction(1, 4),
            Fraction(1, 5),
            Fraction(1, 3),
            Fraction(1, 7),
            Fraction(1, 2),
            Fraction(1, 4),
            Fraction(2, 5),
            Fraction(1, 6),
            Fraction(3, 8),
        ),
        upper=(
            Fraction(3, 4),
            Fraction(2, 5),
            Fraction(2, 3),
            Fraction(3, 7),
            Fraction(4, 5),
            Fraction(3, 5),
            Fraction(3, 4),
            Fraction(1, 2),
            Fraction(7, 8),
        ),
    )
    first_views = (0, 1)
    second_views = (0, 2, 3)

    exact_interval = p75_projection_parity_expectation_contrast_interval_exact(
        box,
        first_views,
        second_views,
    )
    vertex_values = tuple(
        empirical_projection_parity_contrast_exact(
            p75_four_view_law_exact(vertex),
            first_views,
            second_views,
        )
        for vertex in _all_box_vertices(box)
    )

    assert exact_interval == (min(vertex_values), max(vertex_values))


def test_p84_strictly_improves_complete_p83_certificate() -> None:
    box = _strict_witness_box()
    empirical = _strict_witness_empirical_law()

    p83 = p75_box_p83_linf_lower_bound_exact(empirical, box)
    contrast = p75_box_projection_parity_contrast_linf_lower_bound_exact(
        empirical,
        box,
    )
    p84 = p75_box_p84_linf_lower_bound_exact(empirical, box)
    witness = p75_box_projection_parity_contrast_witness_exact(empirical, box)

    assert p83 == Fraction(0)
    assert contrast == Fraction(3, 64)
    assert p84 == Fraction(3, 64)
    assert p84 > p83
    assert witness.lower_bound == Fraction(3, 64)
    assert witness.first_views == (0, 1)
    assert witness.second_views == (0, 2)
    assert witness.coefficient_l1_norm == 16
    assert witness.empirical_first_expectation == Fraction(1, 2)
    assert witness.empirical_second_expectation == Fraction(-1, 4)
    assert witness.empirical_contrast == Fraction(3, 4)
    assert witness.interval_lower == Fraction(0)
    assert witness.interval_upper == Fraction(0)


def test_equal_branch_response_coordinates_force_zero_target_contrast() -> None:
    box = _strict_witness_box()

    assert p75_projection_parity_expectation_contrast_interval_exact(
        box,
        (0, 1),
        (0, 2),
    ) == (Fraction(0), Fraction(0))


def test_empirical_witness_has_expected_signed_parity_values() -> None:
    empirical = _strict_witness_empirical_law()

    assert empirical_projection_parity_expectation_exact(
        empirical,
        (0, 1),
    ) == Fraction(1, 2)
    assert empirical_projection_parity_expectation_exact(
        empirical,
        (0, 2),
    ) == Fraction(-1, 4)
    assert empirical_projection_parity_contrast_exact(
        empirical,
        (0, 1),
        (0, 2),
    ) == Fraction(3, 4)


def test_p84_always_dominates_p83_on_same_box() -> None:
    empirical = tuple(Fraction(1, 16) for _ in range(16))
    box = P78ParameterBox(
        lower=(Fraction(1, 8),) * 9,
        upper=(Fraction(7, 8),) * 9,
    )

    p83 = p75_box_p83_linf_lower_bound_exact(empirical, box)
    p84 = p75_box_p84_linf_lower_bound_exact(empirical, box)

    assert p84 >= p83
    assert p84_dominates_p83_on_box(empirical, box)


def test_p84_validation_rejects_equal_or_invalid_view_sets() -> None:
    box = P78ParameterBox.unit_cube()

    with pytest.raises(ValueError, match="two distinct"):
        p75_projection_parity_expectation_contrast_interval_exact(
            box,
            (0, 1),
            (0, 1),
        )

    with pytest.raises(ValueError, match="two-, three-, or four-view"):
        p75_projection_parity_expectation_contrast_interval_exact(
            box,
            (0,),
            (0, 1),
        )


def test_p84_branch_and_bound_returns_valid_exact_rational_bracket() -> None:
    counts = (0, 0, 0, 3, 0, 0, 0, 3, 0, 1, 0, 0, 3, 0, 5, 1)
    certificate = certified_p75_linf_branch_and_bound_parity_contrast(
        counts,
        max_leaves=4,
    )

    assert Fraction(0) <= certificate.lower_bound <= certificate.upper_bound <= 1
    assert certificate.p78_active_lower_bound <= certificate.p80_active_lower_bound
    assert certificate.p80_active_lower_bound <= certificate.p81_active_lower_bound
    assert certificate.p81_active_lower_bound <= certificate.p82_active_lower_bound
    assert certificate.p82_active_lower_bound <= certificate.p83_active_lower_bound
    assert certificate.p83_active_lower_bound <= certificate.lower_bound
    assert certificate.root_p78_bound <= certificate.root_p80_bound
    assert certificate.root_p80_bound <= certificate.root_p81_bound
    assert certificate.root_p81_bound <= certificate.root_p82_bound
    assert certificate.root_p82_bound <= certificate.root_p83_bound
    assert certificate.root_p83_bound <= certificate.root_p84_bound
    assert certificate.root_parity_contrast_bound <= certificate.root_p84_bound
    assert certificate.root_tightening_over_p83 >= 0
    assert certificate.leaf_count == 4
    assert certificate.evaluated_boxes == 2 * certificate.iterations + 1
    assert certificate.certified_gap == certificate.upper_bound - certificate.lower_bound


def test_p84_source_states_exactness_scope_and_scientific_boundary() -> None:
    source = Path(
        "src/consciousness_bridge/projection_parity_contrast_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "55",
        "mixture contrast interval",
        "never weaker than P83",
        "strictly stronger",
        "P83 box certificate is zero",
        "3/64",
        "does not validate",
        "identify a latent state with consciousness",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in source