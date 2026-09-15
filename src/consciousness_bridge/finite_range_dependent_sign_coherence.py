"""P94 finite-range dependent extension of the P93 rejection gate.

Assume Z_1,...,Z_n are m-dependent and share one common marginal four-view
law P. With q=m+1, residue classes modulo q are independent. Holder plus
Hoeffding gives, for each selected cell x,

    Pr(|P_hat(x)-P(x)| > eps) <= 2 exp(-2 n eps^2 / q).

Union over the seven P92 cells gives radius
sqrt(q log(14/alpha)/(2n)). The P92 determinant geometry is unchanged.

This theorem is conditional on the declared common-marginal finite-range
dependence model. It does not establish drift robustness, identify the latent
state with consciousness, establish nonphysicality, or solve the
physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.certified_sampling_radius import (
    P79LogBracket,
    natural_log_rational_bracket,
)
from consciousness_bridge.exact_global_mixed_prevalence_distance import (
    determinant_2_by_2_exact,
    determinant_sign_stability_radius_exact,
    p92_selected_minor_matrices_exact,
)

_SELECTED_CELL_COUNT = 7


@dataclass(frozen=True)
class P94DependentRadiusCertificate:
    sample_size: int
    dependence_range: int
    color_count: int
    selected_cell_count: int
    alpha: Fraction
    log_bracket: P79LogBracket
    squared_radius_lower: Fraction
    squared_radius_upper: Fraction


@dataclass(frozen=True)
class P94FiniteRangeRejectionCertificate:
    sample_size: int
    dependence_range: int
    color_count: int
    alpha: Fraction
    confidence_lower: Fraction
    determinants: tuple[Fraction, Fraction, Fraction]
    determinant_product: Fraction
    sign_stability_radii: tuple[Fraction, Fraction, Fraction]
    minimum_sign_stability_radius: Fraction
    radius: P94DependentRadiusCertificate
    rejects_p75: bool
    conclusion: str


def _positive_sample_size(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("sample_size must be a positive integer")
    return value


def _dependence_range(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("dependence_range must be a nonnegative integer")
    return value


def _alpha(value: Fraction) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError("alpha must be a fractions.Fraction")
    if value <= 0 or value >= 1:
        raise ValueError("alpha must lie strictly between zero and one")
    return value


def _compatible(empirical_law: tuple[Fraction, ...], sample_size: int) -> None:
    if any((probability * sample_size).denominator != 1 for probability in empirical_law):
        raise ValueError("empirical_law is not compatible with the declared sample_size")


def _safe_radius(matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]) -> Fraction:
    if determinant_2_by_2_exact(matrix) == 0:
        return Fraction(0)
    try:
        return determinant_sign_stability_radius_exact(matrix)
    except ValueError:
        return Fraction(0)


def certified_p94_dependent_squared_radius(
    *,
    sample_size: int,
    dependence_range: int,
    alpha: Fraction,
    series_terms: int = 20,
) -> P94DependentRadiusCertificate:
    sample_size = _positive_sample_size(sample_size)
    dependence_range = _dependence_range(dependence_range)
    alpha = _alpha(alpha)
    if isinstance(series_terms, bool) or not isinstance(series_terms, int) or series_terms <= 0:
        raise ValueError("series_terms must be a positive integer")

    color_count = dependence_range + 1
    log_bracket = natural_log_rational_bracket(
        Fraction(2 * _SELECTED_CELL_COUNT, 1) / alpha,
        series_terms=series_terms,
    )
    scale = Fraction(color_count, 2 * sample_size)
    return P94DependentRadiusCertificate(
        sample_size=sample_size,
        dependence_range=dependence_range,
        color_count=color_count,
        selected_cell_count=_SELECTED_CELL_COUNT,
        alpha=alpha,
        log_bracket=log_bracket,
        squared_radius_lower=scale * log_bracket.lower,
        squared_radius_upper=scale * log_bracket.upper,
    )


def certify_p94_finite_range_rejection_exact(
    empirical_law: tuple[Fraction, ...],
    *,
    sample_size: int,
    dependence_range: int,
    alpha: Fraction,
    series_terms: int = 20,
) -> P94FiniteRangeRejectionCertificate:
    sample_size = _positive_sample_size(sample_size)
    dependence_range = _dependence_range(dependence_range)
    alpha = _alpha(alpha)
    _compatible(empirical_law, sample_size)

    matrices = p92_selected_minor_matrices_exact(empirical_law)
    determinants = tuple(determinant_2_by_2_exact(matrix) for matrix in matrices)
    product = determinants[0] * determinants[1] * determinants[2]
    radii = tuple(_safe_radius(matrix) for matrix in matrices)
    minimum_radius = min(radii)
    radius = certified_p94_dependent_squared_radius(
        sample_size=sample_size,
        dependence_range=dependence_range,
        alpha=alpha,
        series_terms=series_terms,
    )
    rejects = (
        product < 0
        and minimum_radius > 0
        and radius.squared_radius_upper < minimum_radius * minimum_radius
    )
    return P94FiniteRangeRejectionCertificate(
        sample_size=sample_size,
        dependence_range=dependence_range,
        color_count=dependence_range + 1,
        alpha=alpha,
        confidence_lower=1 - alpha,
        determinants=determinants,
        determinant_product=product,
        sign_stability_radii=radii,
        minimum_sign_stability_radius=minimum_radius,
        radius=radius,
        rejects_p75=rejects,
        conclusion=(
            "P75 rejected conditional on the common-marginal finite-range dependence model"
            if rejects
            else "P75 not rejected by the localized P94 certificate"
        ),
    )
