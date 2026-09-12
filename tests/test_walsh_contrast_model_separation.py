from fractions import Fraction
from itertools import product
from pathlib import Path

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    p75_four_view_law_exact,
)
from consciousness_bridge.nested_projection_contrast_separation import (
    p75_box_p82_linf_lower_bound_exact,
)
from consciousness_bridge.projection_parity_model_separation import (
    p75_box_p83_linf_lower_bound_exact,
)
from consciousness_bridge.walsh_contrast_model_separation import (
    certified_p75_linf_branch_and_bound_walsh,
    empirical_walsh_contrast_expectation_exact,
    p75_box_p84_linf_lower_bound_exact,
    p75_box_walsh_contrast_linf_lower_bound_exact,
    p75_box_walsh_contrast_witness_exact,
    p75_walsh_contrast_interval_exact,
    p84_dominates_p83_on_box,
    p84_standard_contrast_count,
    p84_standard_walsh_character_count,
    walsh_contrast_l1_norm,
)


def _chi(outcome: tuple[int, ...], views: tuple[int, ...]) -> int:
    return 1 if sum(outcome[view] for view in views) % 2 == 0 else -1


def _strict_witness_box() -> P78ParameterBox:
    return P78ParameterBox(
        lower=(
            Fraction(0),
            Fraction(3, 8),
            Fraction(3, 8),
            Fraction(1, 4),
            Fraction(1, 4),
            Fraction(1, 4),
            Fraction(1, 4),
            Fraction(1, 2),
            Fraction(1, 2),
        ),
        upper=(
            Fraction(1),
            Fraction(5, 8),
            Fraction(5, 8),
            Fraction(1, 4),
            Fraction(1, 4),
            Fraction(1, 4),
            Fraction(1, 4),
            Fraction(1, 2),
            Fraction(1, 2),
        ),
    )


def _strict_witness_empirical_law() -> tuple[Fraction, ...]:
    d = Fraction(3, 32)
    masses: list[Fraction] = []
    for outcome in product((0, 1), repeat=4):
        expansion = (
            Fraction(1)
            + Fraction(1, 2) * _chi(outcome, (1,))
            + Fraction(1, 2) * _chi(outcome, (2,))
            + Fraction(1, 4) * _chi(outcome, (1, 2))
            + d * _chi(outcome, (0, 1))
            - d * _chi(outcome, (0, 2))
        )
        masses.append(expansion / 16)
    return tuple(masses)


def _all_box_vertices(box: P78ParameterBox) -> tuple[tuple[Fraction, ...], ...]:
    coordinates = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    return tuple(product(*coordinates))


def test_p84_standard_family_contains_15_characters_and_210_contrasts() -> None:
    assert p84_standard_walsh_character_count() == 15
    assert p84_standard_contrast_count() == 210


def test_pairwise_walsh_contrast_has_exact_discrete_l1_norm() -> None:
    assert walsh_contrast_l1_norm((0, 1), (0, 2), -1) == 16
    assert walsh_contrast_l1_norm((0,), (1, 2, 3), 1) == 16


def test_walsh_contrast_interval_matches_exhaustive_parameter_box_vertices() -> None:
    box = P78ParameterBox(
        lower=(
            Fraction(1, 5),
            Fraction(1, 7),
            Fraction(1, 6),
            Fraction(1, 4),
            Fraction(1, 3),
            Fraction(2, 7),
            Fraction(1, 5),
            Fraction(1, 8),
            Fraction(2, 5),
        ),
        upper=(
            Fraction(4, 5),
            Fraction(3, 7),
            Fraction(2, 3),
            Fraction(3, 5),
            Fraction(3, 4),
            Fraction(5, 7),
            Fraction(4, 5),
            Fraction(5, 8),
            Fraction(7, 8),
        ),
    )
    left_views = (0, 1, 3)
    right_views = (0, 2)
    right_sign = -1

    exact_interval = p75_walsh_contrast_interval_exact(
        box,
        left_views,
        right_views,
        right_sign,
    )
    vertex_values = tuple(
        empirical_walsh_contrast_expectation_exact(
            p75_four_view_law_exact(vertex),
            left_views,
            right_views,
            right_sign,
        )
        for vertex in _all_box_vertices(box)
    )

    assert exact_interval == (min(vertex_values), max(vertex_values))


def test_strict_witness_empirical_law_is_an_exact_probability_law() -> None:
    empirical = _strict_witness_empirical_law()

    assert len(empirical) == 16
    assert sum(empirical) == 1
    assert min(empirical) == Fraction(1, 64)
    assert max(empirical) == Fraction(9, 64)


def test_p84_strictly_improves_p83_on_exact_shared_parameter_witness() -> None:
    box = _strict_witness_box()
    empirical = _strict_witness_empirical_law()

    p82 = p75_box_p82_linf_lower_bound_exact(empirical, box)
    p83 = p75_box_p83_linf_lower_bound_exact(empirical, box)
    walsh = p75_box_walsh_contrast_linf_lower_bound_exact(empirical, box)
    p84 = p75_box_p84_linf_lower_bound_exact(empirical, box)
    witness = p75_box_walsh_contrast_witness_exact(empirical, box)

    assert p82 == Fraction(0)
    assert p83 == Fraction(0)
    assert walsh == Fraction(3, 256)
    assert p84 == Fraction(3, 256)
    assert p84 > p83
    assert witness.lower_bound == Fraction(3, 256)
    assert witness.left_views == (0, 1)
    assert witness.right_views == (0, 2)
    assert witness.right_sign == -1
    assert witness.l1_norm == 16
    assert witness.empirical_expectation == Fraction(3, 16)
    assert witness.interval_lower == Fraction(0)
    assert witness.interval_upper == Fraction(0)


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


def test_p84_validation_rejects_degenerate_or_invalid_contrasts() -> None:
    box = P78ParameterBox.unit_cube()

    with pytest.raises(ValueError, match="distinct"):
        p75_walsh_contrast_interval_exact(box, (0, 1), (0, 1), -1)

    with pytest.raises(ValueError, match="strictly increasing"):
        p75_walsh_contrast_interval_exact(box, (1, 0), (0, 2), -1)

    with pytest.raises(ValueError, match="-1 or \\+1"):
        p75_walsh_contrast_interval_exact(box, (0,), (1,), 0)


def test_p84_branch_and_bound_returns_valid_exact_rational_bracket() -> None:
    empirical = _strict_witness_empirical_law()
    counts = tuple(int(mass * 256) for mass in empirical)
    assert sum(counts) == 256

    certificate = certified_p75_linf_branch_and_bound_walsh(
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
    assert certificate.root_walsh_contrast_bound <= certificate.root_p84_bound
    assert certificate.root_tightening_over_p83 >= 0
    assert certificate.leaf_count == 4
    assert certificate.evaluated_boxes == 2 * certificate.iterations + 1
    assert certificate.certified_gap == certificate.upper_bound - certificate.lower_bound


def test_p84_source_states_exactness_scope_and_scientific_boundary() -> None:
    source = Path(
        "src/consciousness_bridge/walsh_contrast_model_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "210",
        "exact, not merely an enclosure",
        "never weaker than P83",
        "strict exact-rational witness",
        "every P83 parity",
        "certificate at zero",
        "3/256",
        "does not validate",
        "identify a latent state with consciousness",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
