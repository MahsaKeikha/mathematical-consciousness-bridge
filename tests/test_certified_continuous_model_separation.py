from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np
import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    certified_p75_linf_branch_and_bound,
    empirical_law_from_counts,
    linf_distance_exact,
    p75_box_cell_intervals_exact,
    p75_box_linf_lower_bound_exact,
    p75_four_view_law_exact,
    p77_rejection_from_certified_radius,
)
from consciousness_bridge.target_model_adequacy import (
    four_view_joint_distribution_from_model,
)


def test_exact_p78_parameterization_matches_p75_model() -> None:
    parameters = (
        Fraction(2, 5),
        Fraction(1, 5),
        Fraction(4, 5),
        Fraction(1, 4),
        Fraction(3, 4),
        Fraction(1, 3),
        Fraction(2, 3),
        Fraction(2, 7),
        Fraction(5, 7),
    )
    exact = p75_four_view_law_exact(parameters)
    p75 = four_view_joint_distribution_from_model(
        float(parameters[0]),
        tuple(
            (float(parameters[1 + 2 * view]), float(parameters[2 + 2 * view]))
            for view in range(4)
        ),
    ).reshape(-1)

    assert sum(exact) == 1
    assert np.allclose(np.array([float(value) for value in exact]), p75)


def test_box_intervals_are_exact_on_a_singleton_box() -> None:
    parameters = (
        Fraction(1, 3),
        Fraction(1, 5),
        Fraction(4, 5),
        Fraction(1, 4),
        Fraction(3, 4),
        Fraction(2, 5),
        Fraction(3, 5),
        Fraction(1, 6),
        Fraction(5, 6),
    )
    box = P78ParameterBox(parameters, parameters)
    lower, upper = p75_box_cell_intervals_exact(box)
    law = p75_four_view_law_exact(parameters)

    assert lower == law
    assert upper == law


def test_box_intervals_contain_all_corner_and_center_laws() -> None:
    lower = (
        Fraction(1, 4),
        Fraction(1, 10),
        Fraction(6, 10),
        Fraction(2, 10),
        Fraction(7, 10),
        Fraction(3, 10),
        Fraction(6, 10),
        Fraction(2, 10),
        Fraction(8, 10),
    )
    upper = (
        Fraction(3, 4),
        Fraction(3, 10),
        Fraction(9, 10),
        Fraction(4, 10),
        Fraction(9, 10),
        Fraction(5, 10),
        Fraction(8, 10),
        Fraction(4, 10),
        Fraction(9, 10),
    )
    box = P78ParameterBox(lower, upper)
    cell_lower, cell_upper = p75_box_cell_intervals_exact(box)

    points = [box.center]
    for bits in product((0, 1), repeat=9):
        points.append(
            tuple(upper[index] if bit else lower[index] for index, bit in enumerate(bits))
        )

    for parameters in points:
        law = p75_four_view_law_exact(parameters)
        for value, minimum, maximum in zip(
            law,
            cell_lower,
            cell_upper,
            strict=True,
        ):
            assert minimum <= value <= maximum


def test_singleton_box_lower_bound_equals_exact_distance() -> None:
    counts = (6, 2, 1, 1, 2, 3, 1, 0, 1, 1, 2, 2, 0, 1, 2, 7)
    empirical = empirical_law_from_counts(counts)
    parameters = (
        Fraction(1, 2),
        Fraction(1, 4),
        Fraction(3, 4),
        Fraction(1, 3),
        Fraction(2, 3),
        Fraction(2, 5),
        Fraction(4, 5),
        Fraction(1, 5),
        Fraction(3, 5),
    )
    box = P78ParameterBox(parameters, parameters)
    model = p75_four_view_law_exact(parameters)

    assert p75_box_linf_lower_bound_exact(empirical, box) == linf_distance_exact(
        empirical,
        model,
    )


def test_branch_and_bound_returns_nested_certified_brackets() -> None:
    counts = tuple(
        10 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )

    coarse = certified_p75_linf_branch_and_bound(counts, max_leaves=64)
    refined = certified_p75_linf_branch_and_bound(counts, max_leaves=256)

    assert Fraction(0) <= coarse.lower_bound <= coarse.upper_bound <= 1
    assert Fraction(0) <= refined.lower_bound <= refined.upper_bound <= 1
    assert refined.lower_bound >= coarse.lower_bound
    assert refined.upper_bound <= coarse.upper_bound
    assert refined.certified_gap <= coarse.certified_gap
    assert refined.leaf_count == 256
    assert refined.evaluated_boxes == 2 * refined.iterations + 1


def test_even_parity_example_gets_positive_global_lower_bound() -> None:
    counts = tuple(
        8 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
    certificate = certified_p75_linf_branch_and_bound(counts, max_leaves=2048)

    assert certificate.lower_bound >= Fraction(1, 64)
    assert certificate.upper_bound <= Fraction(1, 16)
    assert certificate.lower_bound <= certificate.upper_bound
    assert "valid global distance bracket" in certificate.conclusion


def test_p77_interface_uses_strict_certified_lower_bound() -> None:
    counts = tuple(
        8 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
    certificate = certified_p75_linf_branch_and_bound(counts, max_leaves=2048)

    assert p77_rejection_from_certified_radius(
        certificate,
        sampling_radius_upper=Fraction(1, 100),
    )
    assert not p77_rejection_from_certified_radius(
        certificate,
        sampling_radius_upper=certificate.lower_bound,
    )


def test_p78_validation_rejects_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        empirical_law_from_counts((1,) * 15)
    with pytest.raises(TypeError):
        empirical_law_from_counts((1,) * 15 + (1.5,))
    with pytest.raises(ValueError):
        empirical_law_from_counts((0,) * 16)
    with pytest.raises(ValueError):
        P78ParameterBox(
            (Fraction(0),) * 9,
            (Fraction(2),) + (Fraction(1),) * 8,
        )
    with pytest.raises(ValueError):
        p75_four_view_law_exact((Fraction(1, 2),) * 8)
    with pytest.raises(TypeError):
        certified_p75_linf_branch_and_bound((1,) * 16, max_leaves=True)
    with pytest.raises(ValueError):
        certified_p75_linf_branch_and_bound((1,) * 16, max_leaves=0)
    with pytest.raises(TypeError):
        certified_p75_linf_branch_and_bound((1,) * 16, gap_tolerance=0.0)


def test_p78_source_keeps_certification_and_scientific_boundaries_explicit() -> None:
    source = Path(
        "src/consciousness_bridge/certified_continuous_model_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "lower* bound on distance",
        "local numerical best fit is an upper bound",
        "exact ``Fraction`` arithmetic",
        "does not identify the latent state with consciousness",
        "does not solve the physical-to-experiential bridge",
        "Passing an ordinary floating approximation",
    )
    for token in required:
        assert token in source
