from fractions import Fraction
from itertools import product
from pathlib import Path

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    empirical_law_from_counts,
    p75_box_linf_lower_bound_exact,
)
from consciousness_bridge.simplex_coupled_model_separation import (
    certified_p75_linf_branch_and_bound_simplex,
    interval_simplex_linf_distance_exact,
    p75_box_simplex_linf_lower_bound_exact,
    p80_dominates_p78_on_box,
    uncoupled_interval_linf_distance_exact,
)


def test_interval_simplex_distance_is_zero_when_empirical_law_is_feasible() -> None:
    empirical = (Fraction(1, 5), Fraction(3, 10), Fraction(1, 2))
    lower = (Fraction(1, 10), Fraction(1, 5), Fraction(2, 5))
    upper = (Fraction(3, 10), Fraction(2, 5), Fraction(3, 5))

    assert interval_simplex_linf_distance_exact(empirical, lower, upper) == 0


def test_simplex_coupling_can_strictly_improve_uncoupled_interval_bound() -> None:
    empirical = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
    lower = (Fraction(0), Fraction(0), Fraction(0))
    upper = (Fraction(3, 10), Fraction(3, 10), Fraction(1))

    uncoupled = uncoupled_interval_linf_distance_exact(empirical, lower, upper)
    simplex = interval_simplex_linf_distance_exact(empirical, lower, upper)

    assert uncoupled == Fraction(1, 30)
    assert simplex == Fraction(1, 15)
    assert simplex > uncoupled


def test_interval_simplex_distance_handles_lower_mass_and_upper_mass_obstructions() -> None:
    empirical = (Fraction(1, 2), Fraction(1, 4), Fraction(1, 4))

    lower_heavy = (Fraction(3, 5), Fraction(1, 5), Fraction(1, 5))
    upper_heavy = (Fraction(4, 5), Fraction(1, 2), Fraction(1, 2))
    assert interval_simplex_linf_distance_exact(
        empirical,
        lower_heavy,
        upper_heavy,
    ) == Fraction(1, 10)

    lower_light = (Fraction(0), Fraction(0), Fraction(0))
    upper_light = (Fraction(2, 5), Fraction(3, 10), Fraction(3, 10))
    assert interval_simplex_linf_distance_exact(
        empirical,
        lower_light,
        upper_light,
    ) == Fraction(1, 10)


def test_interval_simplex_rejects_infeasible_or_nonprobability_inputs() -> None:
    empirical = (Fraction(1, 2), Fraction(1, 2))

    with pytest.raises(ValueError, match="empty intersection"):
        interval_simplex_linf_distance_exact(
            empirical,
            (Fraction(3, 5), Fraction(3, 5)),
            (Fraction(4, 5), Fraction(4, 5)),
        )

    with pytest.raises(ValueError, match="sum exactly to one"):
        interval_simplex_linf_distance_exact(
            (Fraction(1, 3), Fraction(1, 3)),
            (Fraction(0), Fraction(0)),
            (Fraction(1), Fraction(1)),
        )

    with pytest.raises(TypeError):
        interval_simplex_linf_distance_exact(
            (Fraction(1, 2), Fraction(1, 2)),
            (0.0, Fraction(0)),  # type: ignore[arg-type]
            (Fraction(1), Fraction(1)),
        )


def test_p80_box_bound_always_dominates_p78_on_same_parameter_box() -> None:
    counts = (6, 2, 1, 1, 2, 3, 1, 0, 1, 1, 2, 2, 0, 1, 2, 7)
    empirical = empirical_law_from_counts(counts)
    box = P78ParameterBox(
        lower=(
            Fraction(1, 4),
            Fraction(1, 10),
            Fraction(6, 10),
            Fraction(2, 10),
            Fraction(7, 10),
            Fraction(3, 10),
            Fraction(6, 10),
            Fraction(2, 10),
            Fraction(8, 10),
        ),
        upper=(
            Fraction(3, 4),
            Fraction(3, 10),
            Fraction(9, 10),
            Fraction(4, 10),
            Fraction(9, 10),
            Fraction(5, 10),
            Fraction(8, 10),
            Fraction(4, 10),
            Fraction(9, 10),
        ),
    )

    p78 = p75_box_linf_lower_bound_exact(empirical, box)
    p80 = p75_box_simplex_linf_lower_bound_exact(empirical, box)

    assert p80 >= p78
    assert p80_dominates_p78_on_box(empirical, box)


def test_p80_branch_and_bound_returns_a_valid_exact_rational_bracket() -> None:
    counts = tuple(
        8 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
    certificate = certified_p75_linf_branch_and_bound_simplex(
        counts,
        max_leaves=128,
    )

    assert Fraction(0) <= certificate.lower_bound <= certificate.upper_bound <= 1
    assert certificate.p78_active_lower_bound <= certificate.lower_bound
    assert certificate.root_p78_bound <= certificate.root_p80_bound
    assert certificate.root_tightening >= 0
    assert certificate.leaf_count == 128
    assert certificate.evaluated_boxes == 2 * certificate.iterations + 1
    assert certificate.certified_gap == certificate.upper_bound - certificate.lower_bound


def test_p80_refinement_does_not_weaken_its_global_lower_bound() -> None:
    counts = tuple(
        8 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
    coarse = certified_p75_linf_branch_and_bound_simplex(counts, max_leaves=32)
    refined = certified_p75_linf_branch_and_bound_simplex(counts, max_leaves=128)

    assert refined.lower_bound >= coarse.lower_bound
    assert refined.upper_bound <= coarse.upper_bound


def test_p80_source_states_scope_and_scientific_boundary() -> None:
    source = Path(
        "src/consciousness_bridge/simplex_coupled_model_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "sum to one",
        "always dominates the P78",
        "can be strictly stronger",
        "``fractions.Fraction`` arithmetic",
        "does not validate the latent target model",
        "identify a latent state with consciousness",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
