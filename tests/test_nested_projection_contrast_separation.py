from fractions import Fraction
from itertools import product
from pathlib import Path

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    p75_four_view_law_exact,
)
from consciousness_bridge.nested_projection_contrast_separation import (
    certified_p75_linf_branch_and_bound_contrast,
    empirical_nested_projection_contrast_exact,
    p75_box_nested_projection_contrast_linf_lower_bound_exact,
    p75_box_nested_projection_contrast_witness_exact,
    p75_box_p82_linf_lower_bound_exact,
    p75_nested_projection_contrast_enclosure_exact,
    p75_nested_projection_contrast_interval_exact,
    p75_nested_projection_contrast_subtraction_enclosure_exact,
    p82_dominates_p81_on_box,
    p82_standard_contrast_count,
)
from consciousness_bridge.projection_event_model_separation import (
    p75_box_p81_linf_lower_bound_exact,
)
from consciousness_bridge.simplex_coupled_model_separation import (
    p75_box_simplex_linf_lower_bound_exact,
)


def _strict_witness_box() -> P78ParameterBox:
    lower = [Fraction(0)] * 9
    upper = [Fraction(1)] * 9
    for index in (5, 6, 7, 8):
        lower[index] = Fraction(1, 2)
        upper[index] = Fraction(1, 2)
    return P78ParameterBox(tuple(lower), tuple(upper))


def _strict_witness_empirical_law() -> tuple[Fraction, ...]:
    law = []
    for pattern in product((0, 1), repeat=4):
        if pattern[2:] == (1, 1):
            if pattern == (0, 0, 1, 1):
                law.append(Fraction(0))
            else:
                law.append(Fraction(1, 6))
        else:
            law.append(Fraction(1, 24))
    return tuple(law)


def _all_box_vertices(box: P78ParameterBox) -> tuple[tuple[Fraction, ...], ...]:
    coordinates = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    return tuple(product(*coordinates))


def test_p82_standard_family_contains_256_genuinely_new_contrasts() -> None:
    assert p82_standard_contrast_count() == 256


def test_exact_residual_interval_matches_exhaustive_parameter_box_vertices() -> None:
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
    parent_views = (0, 3)
    parent_assignment = (1, 0)
    child_views = (0, 1, 2, 3)
    child_assignment = (1, 0, 1, 0)

    exact_interval = p75_nested_projection_contrast_interval_exact(
        box,
        parent_views,
        parent_assignment,
        child_views,
        child_assignment,
    )
    vertex_values = tuple(
        empirical_nested_projection_contrast_exact(
            p75_four_view_law_exact(vertex),
            parent_views,
            parent_assignment,
            child_views,
            child_assignment,
        )
        for vertex in _all_box_vertices(box)
    )

    assert exact_interval == (min(vertex_values), max(vertex_values))
    assert p75_nested_projection_contrast_enclosure_exact(
        box,
        parent_views,
        parent_assignment,
        child_views,
        child_assignment,
    ) == exact_interval


def test_exact_residual_interval_can_be_strictly_tighter_than_interval_subtraction() -> None:
    lower = [Fraction(0)] * 9
    upper = [Fraction(1)] * 9
    for index in (3, 4, 5, 6):
        lower[index] = Fraction(1)
        upper[index] = Fraction(1)
    box = P78ParameterBox(tuple(lower), tuple(upper))

    parent_views = (0,)
    parent_assignment = (1,)
    child_views = (0, 1, 2)
    child_assignment = (1, 1, 1)

    exact_interval = p75_nested_projection_contrast_interval_exact(
        box,
        parent_views,
        parent_assignment,
        child_views,
        child_assignment,
    )
    subtraction = p75_nested_projection_contrast_subtraction_enclosure_exact(
        box,
        parent_views,
        parent_assignment,
        child_views,
        child_assignment,
    )

    assert exact_interval == (Fraction(0), Fraction(0))
    assert subtraction == (Fraction(0), Fraction(1))


def test_nested_contrast_interval_for_strict_witness_is_exactly_as_expected() -> None:
    box = _strict_witness_box()
    empirical = _strict_witness_empirical_law()
    parent_views = (2, 3)
    parent_assignment = (1, 1)
    child_views = (0, 1, 2, 3)
    child_assignment = (0, 0, 1, 1)

    exact_interval = p75_nested_projection_contrast_interval_exact(
        box,
        parent_views,
        parent_assignment,
        child_views,
        child_assignment,
    )
    empirical_residual = empirical_nested_projection_contrast_exact(
        empirical,
        parent_views,
        parent_assignment,
        child_views,
        child_assignment,
    )

    assert exact_interval == (Fraction(0), Fraction(1, 4))
    assert empirical_residual == Fraction(1, 2)


def test_p82_strictly_improves_p81_on_clean_exact_rational_witness() -> None:
    box = _strict_witness_box()
    empirical = _strict_witness_empirical_law()

    p80 = p75_box_simplex_linf_lower_bound_exact(empirical, box)
    p81 = p75_box_p81_linf_lower_bound_exact(empirical, box)
    contrast = p75_box_nested_projection_contrast_linf_lower_bound_exact(
        empirical,
        box,
    )
    p82 = p75_box_p82_linf_lower_bound_exact(empirical, box)
    witness = p75_box_nested_projection_contrast_witness_exact(empirical, box)

    assert p80 == 0
    assert p81 == Fraction(1, 16)
    assert contrast == Fraction(1, 12)
    assert p82 == Fraction(1, 12)
    assert p82 > p81
    assert witness.lower_bound == Fraction(1, 12)
    assert witness.parent_views == (2, 3)
    assert witness.parent_assignment == (1, 1)
    assert witness.child_views == (0, 1, 2, 3)
    assert witness.child_assignment == (0, 0, 1, 1)
    assert witness.support_size == 3
    assert witness.empirical_residual_probability == Fraction(1, 2)
    assert witness.interval_lower == 0
    assert witness.interval_upper == Fraction(1, 4)
    assert witness.subtraction_interval_lower <= witness.interval_lower
    assert witness.interval_upper <= witness.subtraction_interval_upper


def test_p82_always_dominates_p81_on_same_box() -> None:
    empirical = tuple(Fraction(1, 16) for _ in range(16))
    box = P78ParameterBox(
        lower=(Fraction(1, 8),) * 9,
        upper=(Fraction(7, 8),) * 9,
    )

    p81 = p75_box_p81_linf_lower_bound_exact(empirical, box)
    p82 = p75_box_p82_linf_lower_bound_exact(empirical, box)

    assert p82 >= p81
    assert p82_dominates_p81_on_box(empirical, box)


def test_nested_projection_validation_rejects_non_nested_pairs() -> None:
    box = P78ParameterBox.unit_cube()

    with pytest.raises(ValueError, match="strict subset"):
        p75_nested_projection_contrast_interval_exact(
            box,
            (0,),
            (0,),
            (1,),
            (0,),
        )

    with pytest.raises(ValueError, match="strict subset"):
        p75_nested_projection_contrast_interval_exact(
            box,
            (0,),
            (0,),
            (0,),
            (0,),
        )


def test_p82_branch_and_bound_returns_valid_exact_rational_bracket() -> None:
    counts = tuple(
        4 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
    certificate = certified_p75_linf_branch_and_bound_contrast(
        counts,
        max_leaves=8,
    )

    assert Fraction(0) <= certificate.lower_bound <= certificate.upper_bound <= 1
    assert certificate.p78_active_lower_bound <= certificate.p80_active_lower_bound
    assert certificate.p80_active_lower_bound <= certificate.p81_active_lower_bound
    assert certificate.p81_active_lower_bound <= certificate.lower_bound
    assert certificate.root_p78_bound <= certificate.root_p80_bound
    assert certificate.root_p80_bound <= certificate.root_p81_bound
    assert certificate.root_p81_bound <= certificate.root_p82_bound
    assert certificate.root_contrast_bound <= certificate.root_p82_bound
    assert certificate.root_tightening_over_p81 >= 0
    assert certificate.leaf_count == 8
    assert certificate.evaluated_boxes == 2 * certificate.iterations + 1
    assert certificate.certified_gap == certificate.upper_bound - certificate.lower_bound


def test_p82_source_states_exactness_scope_and_scientific_boundary() -> None:
    source = Path(
        "src/consciousness_bridge/nested_projection_contrast_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "exact branchwise residual range",
        "256",
        "never weaker than P81",
        "strictly stronger",
        "exact global residual interval",
        "does not validate",
        "identify any latent state with consciousness",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
