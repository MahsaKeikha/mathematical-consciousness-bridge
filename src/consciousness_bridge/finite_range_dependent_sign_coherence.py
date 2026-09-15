"""P94 finite-range dependent extension of the P93 rejection gate.

Assume Z_1,...,Z_n are m-dependent and share one common marginal four-view
law P. With q=m+1, residue classes modulo q are independent. Holder plus
Hoeffding gives, for each selected cell x,

    Pr(|P_hat(x)-P(x)| > eps) <= 2 exp(-2 n eps^2 / q).

Union over the seven P92 cells gives radius
sqrt(q log(14/alpha)/(2n)). The P92 determinant geometry is unchanged.

The common-marginal assumption is essential rather than cosmetic. P94 also
provides an exact interior counterexample in which two time-specific P75 laws
each obey P92 sign coherence while their 50/50 temporal average violates it.
Thus an apparent rejection can be manufactured by drift if one silently pools
different marginal laws.

This theorem is conditional on the declared common-marginal finite-range
dependence model. It does not establish drift robustness, identify the latent
state with consciousness, establish nonphysicality, or solve the
physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.certified_continuous_model_separation import (
    p75_four_view_law_exact,
)
from consciousness_bridge.certified_sampling_radius import (
    P79LogBracket,
    natural_log_rational_bracket,
)
from consciousness_bridge.exact_global_mixed_prevalence_distance import (
    determinant_2_by_2_exact,
    determinant_sign_stability_radius_exact,
    p92_selected_determinants_exact,
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


@dataclass(frozen=True)
class P94TemporalDriftNoGoCertificate:
    """Exact counterexample showing why a common marginal law is required."""

    regime_one_parameters: tuple[Fraction, ...]
    regime_two_parameters: tuple[Fraction, ...]
    regime_one_determinants: tuple[Fraction, Fraction, Fraction]
    regime_two_determinants: tuple[Fraction, Fraction, Fraction]
    average_determinants: tuple[Fraction, Fraction, Fraction]
    regime_one_product: Fraction
    regime_two_product: Fraction
    average_product: Fraction
    all_parameters_interior: bool
    each_regime_sign_coherent: bool
    average_violates_sign_coherence: bool


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
    if any(
        (probability * sample_size).denominator != 1
        for probability in empirical_law
    ):
        raise ValueError("empirical_law is not compatible with the declared sample_size")


def _safe_radius(
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> Fraction:
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
    if (
        isinstance(series_terms, bool)
        or not isinstance(series_terms, int)
        or series_terms <= 0
    ):
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


def certify_p94_temporal_drift_no_go_exact() -> P94TemporalDriftNoGoCertificate:
    """Return two exact interior P75 regimes whose average violates P92 coherence.

    Each parameter vector lies strictly inside the nine-dimensional P75 cube.
    The two individual laws have strictly positive products of the three P92
    determinants. Their equally weighted average has determinant signs
    (-,+,+), hence a strictly negative product. Pooling nonstationary regimes
    can therefore mimic the same qualitative obstruction used for rejection.
    """

    regime_one_parameters = (
        Fraction(1, 2),
        Fraction(1, 2),
        Fraction(1, 4),
        Fraction(3, 4),
        Fraction(1, 4),
        Fraction(1, 4),
        Fraction(3, 4),
        Fraction(1, 4),
        Fraction(1, 2),
    )
    regime_two_parameters = (
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(1, 2),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(3, 4),
        Fraction(1, 4),
    )
    law_one = p75_four_view_law_exact(regime_one_parameters)
    law_two = p75_four_view_law_exact(regime_two_parameters)
    average_law = tuple(
        (left + right) / 2
        for left, right in zip(law_one, law_two, strict=True)
    )
    determinants_one = p92_selected_determinants_exact(law_one)
    determinants_two = p92_selected_determinants_exact(law_two)
    determinants_average = p92_selected_determinants_exact(average_law)
    product_one = determinants_one[0] * determinants_one[1] * determinants_one[2]
    product_two = determinants_two[0] * determinants_two[1] * determinants_two[2]
    product_average = (
        determinants_average[0]
        * determinants_average[1]
        * determinants_average[2]
    )
    interior = all(
        0 < value < 1
        for value in regime_one_parameters + regime_two_parameters
    )
    if not interior or product_one <= 0 or product_two <= 0 or product_average >= 0:
        raise RuntimeError("P94 temporal-drift counterexample failed exact validation")
    return P94TemporalDriftNoGoCertificate(
        regime_one_parameters=regime_one_parameters,
        regime_two_parameters=regime_two_parameters,
        regime_one_determinants=determinants_one,
        regime_two_determinants=determinants_two,
        average_determinants=determinants_average,
        regime_one_product=product_one,
        regime_two_product=product_two,
        average_product=product_average,
        all_parameters_interior=interior,
        each_regime_sign_coherent=product_one > 0 and product_two > 0,
        average_violates_sign_coherence=product_average < 0,
    )
