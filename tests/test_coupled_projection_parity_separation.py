from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    p75_four_view_law_exact,
)
from consciousness_bridge.coupled_projection_parity_separation import (
    certified_p75_linf_branch_and_bound_coupled_parity,
    empirical_projection_parity_contrast_exact,
    p75_box_p84_linf_lower_bound_exact,
    p75_box_projection_parity_contrast_linf_lower_bound_exact,
    p75_box_projection_parity_contrast_witness_exact,
    p75_projection_parity_contrast_interval_exact,
    p84_dominates_p83_on_box,
    p84_projection_parity_contrast_support_size,
    p84_standard_parity_contrast_count,
)
from consciousness_bridge.nested_projection_contrast_separation import (
    p75_box_p82_linf_lower_bound_exact,
)
from consciousness_bridge.projection_event_model_separation import (
    p75_box_p81_linf_lower_bound_exact,
)
from consciousness_bridge.projection_parity_model_separation import (
    p75_box_p83_linf_lower_bound_exact,
)


def _strict_witness_box() -> P78ParameterBox:
    return P78ParameterBox(
        lower=(
            Fraction(0),
            Fraction(1, 4),
            Fraction(0),
            Fraction(1, 4),
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(1, 4),
            Fraction(0),
        ),
        upper=(
            Fraction(0),
            Fraction(3, 4),
            Fraction(1),
            Fraction(3, 4),
            Fraction(1),
            Fraction(1, 2),
            Fraction(1),
            Fraction(3, 4),
            Fraction(1),
        ),
    )


def _strict_witness_empirical_law() -> tuple[Fraction, ...]:
    return (
        Fraction(9, 640),
        Fraction(47, 640),
        Fraction(1, 64),
        Fraction(1, 64),
        Fraction(97, 640),
        Fraction(83, 640),
        Fraction(21, 160),
        Fraction(1, 40),
        Fraction(11, 640),
        Fraction(49, 640),
        Fraction(1, 64),
        Fraction(5, 64),
        Fraction(19, 640),
        Fraction(1, 128),
        Fraction(11, 160),
        Fraction(3, 20),
    )


def _all_box_vertices(box: P78ParameterBox) -> tuple[tuple[Fraction, ...], ...]:
    coordinates = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    return tuple(product(*coordinates))


def _standard_view_sets() -> tuple[tuple[int, ...], ...]:
    return tuple(
        views
        for size in range(2, 5)
        for views in combinations(range(4), size)
    )


def test_p84_standard_family_contains_55_coupled_parity_contrasts() -> None:
    assert p84_standard_parity_contrast_count() == 55


def test_every_standard_contrast_has_signed_support_size_eight() -> None:
    view_sets = _standard_view_sets()

    for left_views, right_views in combinations(view_sets, 2):
        assert (
            p84_projection_parity_contrast_support_size(
                left_views,
                right_views,
            )
            == 8
        )


def test_coupled_parity_interval_matches_exhaustive_parameter_vertices() -> None:
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
    left_views = (0, 3)
    right_views = (0, 2, 3)

    exact_interval = p75_projection_parity_contrast_interval_exact(
        box,
        left_views,
        right_views,
    )
    vertex_values = tuple(
        empirical_projection_parity_contrast_exact(
            p75_four_view_law_exact(vertex),
            left_views,
            right_views,
        )
        for vertex in _all_box_vertices(box)
    )

    assert exact_interval == (min(vertex_values), max(vertex_values))


def test_p84_strictly_improves_p83_on_common_endpoint_witness() -> None:
    box = _strict_witness_box()
    empirical = _strict_witness_empirical_law()

    p81 = p75_box_p81_linf_lower_bound_exact(empirical, box)
    p82 = p75_box_p82_linf_lower_bound_exact(empirical, box)
    p83 = p75_box_p83_linf_lower_bound_exact(empirical, box)
    contrast = p75_box_projection_parity_contrast_linf_lower_bound_exact(
        empirical,
        box,
    )
    p84 = p75_box_p84_linf_lower_bound_exact(empirical, box)
    witness = p75_box_projection_parity_contrast_witness_exact(empirical, box)

    assert p81 == Fraction(0)
    assert p82 == Fraction(0)
    assert p83 == Fraction(0)
    assert contrast == Fraction(1, 64)
    assert p84 == Fraction(1, 64)
    assert p84 > p83
    assert witness.lower_bound == Fraction(1, 64)
    assert witness.left_views == (0, 3)
    assert witness.right_views == (0, 2, 3)
    assert witness.support_size == 8
    assert witness.empirical_contrast == Fraction(1, 4)
    assert witness.interval_lower == Fraction(-1, 8)
    assert witness.interval_upper == Fraction(1, 8)


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


def test_p84_validation_rejects_invalid_or_duplicate_view_sets() -> None:
    box = P78ParameterBox.unit_cube()

    with pytest.raises(ValueError, match="between two and four"):
        p75_projection_parity_contrast_interval_exact(box, (0,), (0, 1))

    with pytest.raises(ValueError, match="strictly increasing"):
        p75_projection_parity_contrast_interval_exact(box, (1, 0), (0, 1))

    with pytest.raises(ValueError, match="two distinct view sets"):
        p75_projection_parity_contrast_interval_exact(box, (0, 1), (0, 1))


def test_p84_branch_and_bound_returns_valid_exact_rational_bracket() -> None:
    counts = tuple(
        4 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
    certificate = certified_p75_linf_branch_and_bound_coupled_parity(
        counts,
        max_leaves=8,
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
    assert certificate.root_contrast_bound <= certificate.root_p84_bound
    assert certificate.root_tightening_over_p83 >= 0
    assert certificate.leaf_count == 8
    assert certificate.evaluated_boxes == 2 * certificate.iterations + 1
    assert certificate.certified_gap == certificate.upper_bound - certificate.lower_bound


def test_p84_source_states_exactness_scope_and_scientific_boundary() -> None:
    source = Path(
        "src/consciousness_bridge/coupled_projection_parity_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "same endpoint assignment",
        "C(11,2) = 55",
        "never weaker than P83",
        "P81 = P82 = P83 = 0 while P84 = 1/64",
        "does not validate",
        "identify a latent state with consciousness",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
