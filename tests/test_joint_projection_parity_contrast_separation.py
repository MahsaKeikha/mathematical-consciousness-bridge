from fractions import Fraction
from itertools import product
from pathlib import Path

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    p75_four_view_law_exact,
)
from consciousness_bridge.joint_projection_parity_contrast_separation import (
    certified_p75_linf_branch_and_bound_parity_contrast,
    empirical_projection_parity_contrast_exact,
    p75_box_p84_linf_lower_bound_exact,
    p75_box_projection_parity_contrast_linf_lower_bound_exact,
    p75_box_projection_parity_contrast_witness_exact,
    p75_projection_parity_contrast_interval_exact,
    p84_dominates_p83_on_box,
    p84_standard_contrast_count,
    parity_contrast_coefficient_support_size,
)
from consciousness_bridge.projection_parity_model_separation import (
    p75_box_p83_linf_lower_bound_exact,
)


def _strict_witness_box() -> P78ParameterBox:
    return P78ParameterBox(
        lower=(
            Fraction(1, 2),
            Fraction(0),
            Fraction(1),
            Fraction(1),
            Fraction(1, 2),
            Fraction(0),
            Fraction(1),
            Fraction(1, 2),
            Fraction(1),
        ),
        upper=(
            Fraction(1, 2),
            Fraction(1, 2),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
        ),
    )


def _strict_witness_empirical_law() -> tuple[Fraction, ...]:
    masses = {
        (0, 1, 0, 0): Fraction(1, 8),
        (0, 1, 1, 1): Fraction(1, 4),
        (1, 0, 1, 1): Fraction(1, 4),
        (1, 1, 0, 0): Fraction(1, 8),
        (1, 1, 1, 1): Fraction(1, 4),
    }
    return tuple(masses.get(outcome, Fraction(0)) for outcome in product((0, 1), repeat=4))


def _all_box_vertices(box: P78ParameterBox) -> tuple[tuple[Fraction, ...], ...]:
    coordinates = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    return tuple(product(*coordinates))


def test_p84_standard_family_contains_220_genuinely_coupled_contrasts() -> None:
    assert p84_standard_contrast_count() == 220


def test_pairwise_parity_contrast_interval_matches_exhaustive_box_vertices() -> None:
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
    first = ((0, 2), 0)
    second = ((1, 2, 3), 1)

    exact_interval = p75_projection_parity_contrast_interval_exact(
        box,
        first[0],
        first[1],
        second[0],
        second[1],
    )
    vertex_values = tuple(
        empirical_projection_parity_contrast_exact(
            p75_four_view_law_exact(vertex),
            first[0],
            first[1],
            second[0],
            second[1],
        )
        for vertex in _all_box_vertices(box)
    )

    assert exact_interval == (min(vertex_values), max(vertex_values))


def test_p84_is_strictly_stronger_than_p83_on_exact_rational_joint_witness() -> None:
    box = _strict_witness_box()
    empirical = _strict_witness_empirical_law()

    p83 = p75_box_p83_linf_lower_bound_exact(empirical, box)
    contrast = p75_box_projection_parity_contrast_linf_lower_bound_exact(empirical, box)
    p84 = p75_box_p84_linf_lower_bound_exact(empirical, box)
    witness = p75_box_projection_parity_contrast_witness_exact(empirical, box)

    assert p83 == Fraction(0)
    assert contrast == Fraction(1, 32)
    assert p84 == Fraction(1, 32)
    assert p84 > p83
    assert witness.lower_bound == Fraction(1, 32)
    assert witness.coefficient_support_size == 8
    assert witness.empirical_contrast < witness.interval_lower or witness.empirical_contrast > witness.interval_upper


def test_named_strict_contrast_has_quarter_gap_and_eight_cell_support() -> None:
    box = _strict_witness_box()
    empirical = _strict_witness_empirical_law()
    first = ((1, 3), 0)
    second = ((1, 2, 3), 1)

    interval = p75_projection_parity_contrast_interval_exact(
        box,
        first[0],
        first[1],
        second[0],
        second[1],
    )
    observed = empirical_projection_parity_contrast_exact(
        empirical,
        first[0],
        first[1],
        second[0],
        second[1],
    )

    assert interval == (Fraction(0), Fraction(1, 2))
    assert observed == Fraction(-1, 4)
    assert interval[0] - observed == Fraction(1, 4)
    assert parity_contrast_coefficient_support_size(
        first[0],
        first[1],
        second[0],
        second[1],
    ) == 8


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


def test_p84_validation_rejects_same_view_set_and_invalid_parity() -> None:
    box = P78ParameterBox.unit_cube()

    with pytest.raises(ValueError, match="different parity view sets"):
        p75_projection_parity_contrast_interval_exact(
            box,
            (0, 1),
            0,
            (0, 1),
            1,
        )

    with pytest.raises(ValueError, match="integer 0 or 1"):
        p75_projection_parity_contrast_interval_exact(
            box,
            (0, 1),
            2,
            (1, 2),
            0,
        )


def test_p84_branch_and_bound_returns_valid_exact_rational_bracket() -> None:
    counts = tuple(
        4 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
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
    assert certificate.root_contrast_bound <= certificate.root_p84_bound
    assert certificate.root_tightening_over_p83 >= 0
    assert certificate.leaf_count == 4
    assert certificate.evaluated_boxes == 2 * certificate.iterations + 1
    assert certificate.certified_gap == certificate.upper_bound - certificate.lower_bound


def test_p84_source_states_exactness_strictness_and_scientific_boundary() -> None:
    source = Path(
        "src/consciousness_bridge/joint_projection_parity_contrast_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "220 genuinely coupled",
        "exact, not an enclosure",
        "never weaker than P83",
        "strictly stronger",
        "P83 lower bound zero",
        "1/32",
        "rejects only the declared P75 model family",
        "identify a latent state with",
        "consciousness",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
