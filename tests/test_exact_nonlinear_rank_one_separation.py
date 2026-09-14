from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.exact_nonlinear_rank_one_separation import (
    certify_p90_exact_nonlinear_distance_exact,
    p90_canonical_rank_one_slice_exact,
    p90_rank_one_linf_lower_certificate_exact,
    rank_one_slice_determinant_exact,
    verify_p90_rank_one_upper_certificate_exact,
)


def _strict_box() -> P78ParameterBox:
    return P78ParameterBox(
        lower=(
            Fraction(0),
            Fraction(1, 4),
            Fraction(1, 2),
            Fraction(1, 4),
            Fraction(3, 4),
            Fraction(1, 2),
            Fraction(1, 2),
            Fraction(1, 4),
            Fraction(3, 4),
        ),
        upper=(
            Fraction(0),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(3, 4),
            Fraction(1),
            Fraction(3, 4),
            Fraction(1),
            Fraction(1),
        ),
    )


def _strict_empirical_law() -> tuple[Fraction, ...]:
    counts = (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    return tuple(Fraction(count, 24) for count in counts)


def _matching_parameters() -> tuple[Fraction, ...]:
    return (
        Fraction(0),
        Fraction(3, 5),
        Fraction(1, 2),
        Fraction(3, 8),
        Fraction(3, 4),
        Fraction(5, 9),
        Fraction(1, 2),
        Fraction(2, 3),
        Fraction(3, 4),
    )


def test_p90_empirical_slice_has_exact_nonlinear_rank_one_residual():
    empirical = _strict_empirical_law()
    slice_entries = p90_canonical_rank_one_slice_exact(empirical)
    assert slice_entries == (
        Fraction(1, 8),
        Fraction(1, 24),
        Fraction(0),
        Fraction(5, 24),
    )
    assert rank_one_slice_determinant_exact(slice_entries) == Fraction(5, 192)


def test_p90_rank_one_interval_argument_gives_exact_5_over_72_lower_bound():
    certificate = p90_rank_one_linf_lower_certificate_exact(
        _strict_empirical_law(), _strict_box()
    )
    assert certificate.determinant_residual == Fraction(5, 192)
    assert certificate.slice_mass == Fraction(3, 8)
    assert certificate.orientation == "ad>bc"
    assert certificate.lower_bound == Fraction(5, 72)


def test_p90_explicit_rational_model_point_attains_5_over_72():
    certificate = verify_p90_rank_one_upper_certificate_exact(
        _strict_empirical_law(), _strict_box(), _matching_parameters()
    )
    assert certificate.model_determinant == 0
    assert certificate.model_slice == (
        Fraction(1, 18),
        Fraction(1, 9),
        Fraction(5, 72),
        Fraction(5, 36),
    )
    assert certificate.radius == Fraction(5, 72)


def test_p90_matching_certificates_prove_exact_nonlinear_distance():
    certificate = certify_p90_exact_nonlinear_distance_exact(
        _strict_empirical_law(), _strict_box(), _matching_parameters()
    )
    assert certificate.optimum == Fraction(5, 72)
    assert certificate.lower.lower_bound == certificate.upper.radius
    assert certificate.optimum > Fraction(5, 168)
    assert certificate.optimum / Fraction(5, 168) == Fraction(7, 3)


def test_p90_rejects_box_with_unfixed_prevalence():
    box = _strict_box()
    relaxed = P78ParameterBox(
        lower=box.lower,
        upper=(Fraction(1, 10),) + box.upper[1:],
    )
    with pytest.raises(ValueError, match="prevalence coordinate to be fixed"):
        p90_rank_one_linf_lower_certificate_exact(_strict_empirical_law(), relaxed)


def test_p90_rejects_box_with_nonextreme_fixed_prevalence():
    box = _strict_box()
    lower = (Fraction(1, 2),) + box.lower[1:]
    upper = (Fraction(1, 2),) + box.upper[1:]
    with pytest.raises(ValueError, match="exactly zero or one"):
        p90_rank_one_linf_lower_certificate_exact(
            _strict_empirical_law(), P78ParameterBox(lower=lower, upper=upper)
        )


def test_p90_rejects_upper_certificate_outside_box():
    parameters = list(_matching_parameters())
    parameters[5] = Fraction(1, 4)
    with pytest.raises(ValueError, match="outside the declared P75 box"):
        verify_p90_rank_one_upper_certificate_exact(
            _strict_empirical_law(), _strict_box(), tuple(parameters)
        )


def test_p90_source_keeps_scientific_interpretation_boundary():
    source = (
        __import__(
            "consciousness_bridge.exact_nonlinear_rank_one_separation",
            fromlist=["dummy"],
        ).__doc__
        or ""
    ).lower()
    assert "conditional" in source
    assert "does not identify" in source
    assert "consciousness" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
