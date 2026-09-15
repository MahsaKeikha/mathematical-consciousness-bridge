"""P93 localized finite-sample rejection from the P92 sign-coherence witness.

P92 proves that every law in the complete P75 model family satisfies a
nonnegative product constraint across three selected 2 by 2 determinants on
the X1 = 1 observable subtensor. The established empirical witness has signs
(-,+,+), so its determinant product is negative.

P93 converts that exact population obstruction into a finite-sample rejection
rule without constructing a confidence box for all sixteen observable cells.
Only seven distinct cell probabilities enter the three P92 minors. A union
bound over those seven Bernoulli cell indicators gives the simultaneous radius

    eps_n,7(alpha) = sqrt(log(14 / alpha) / (2 n)).

If the empirical determinant product is negative and a certified upper bound
on this seven-cell radius is strictly smaller than every empirical determinant
sign-stability radius, then the unknown population determinants retain the
same signs on the simultaneous confidence event. Their product is therefore
negative, which is impossible for every P75 law. The P75 family is rejected at
confidence at least 1-alpha.

For the established P92 profile, the smallest determinant sign-stability
radius is exactly 1/24. At alpha = 1/20, exact P79 rational envelopes prove
that the seven-cell radius is still above 1/24 at n = 1622 and is below 1/24
at n = 1623. The first exact integer replication of the original 24-count
profile that can trigger the P93 certificate is therefore n = 1632 = 68*24.

This is a conditional statistical theorem for the declared P75 family and IID
sampling model. It does not identify the latent state with consciousness,
establish nonphysicality, validate an alternative ontology, or solve the
physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.certified_sampling_radius import (
    P79SamplingRadiusCertificate,
    certified_finite_alphabet_sampling_radius,
)
from consciousness_bridge.exact_global_mixed_prevalence_distance import (
    determinant_2_by_2_exact,
    determinant_sign_stability_radius_exact,
    p92_selected_minor_matrices_exact,
)

_SELECTED_CELL_COUNT = 7
_P92_WITNESS_RADIUS = Fraction(1, 24)
_P93_ALPHA_95 = Fraction(1, 20)


@dataclass(frozen=True)
class P93LocalizedRejectionCertificate:
    """Finite-sample rejection certificate for the localized P92 witness."""

    sample_size: int
    alpha: Fraction
    confidence_lower: Fraction
    selected_cell_count: int
    determinants: tuple[Fraction, Fraction, Fraction]
    determinant_product: Fraction
    sign_stability_radii: tuple[Fraction, Fraction, Fraction]
    minimum_sign_stability_radius: Fraction
    sampling_radius: P79SamplingRadiusCertificate
    rejects_p75: bool
    conclusion: str


@dataclass(frozen=True)
class P93WitnessThresholdCertificate:
    """Exact 95 percent sample-size crossing for the established P92 profile."""

    alpha: Fraction
    witness_radius: Fraction
    last_noncertifying_sample_size: int
    first_certifying_sample_size: int
    last_radius: P79SamplingRadiusCertificate
    first_radius: P79SamplingRadiusCertificate
    base_profile_sample_size: int
    first_exact_replication_sample_size: int
    generic_p77_last_noncertifying_sample_size: int
    generic_p77_first_certifying_sample_size: int
    generic_p77_last_radius: P79SamplingRadiusCertificate
    generic_p77_first_radius: P79SamplingRadiusCertificate


def _validate_sample_size(sample_size: int) -> int:
    if isinstance(sample_size, bool) or not isinstance(sample_size, int) or sample_size <= 0:
        raise ValueError("sample_size must be a positive integer")
    return sample_size


def _validate_alpha(alpha: Fraction) -> Fraction:
    if not isinstance(alpha, Fraction):
        raise TypeError("alpha must be a fractions.Fraction")
    if alpha <= 0 or alpha >= 1:
        raise ValueError("alpha must lie strictly between zero and one")
    return alpha


def _validate_empirical_law_sample_compatibility(
    empirical_law: tuple[Fraction, ...],
    sample_size: int,
) -> None:
    for probability in empirical_law:
        scaled = probability * sample_size
        if scaled.denominator != 1:
            raise ValueError(
                "empirical_law is not compatible with the declared sample_size"
            )


def _safe_sign_stability_radius(
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> Fraction:
    determinant = determinant_2_by_2_exact(matrix)
    if determinant == 0:
        return Fraction(0)
    try:
        return determinant_sign_stability_radius_exact(matrix)
    except ValueError:
        return Fraction(0)


def certify_p93_localized_rejection_exact(
    empirical_law: tuple[Fraction, ...],
    *,
    sample_size: int,
    alpha: Fraction,
    series_terms: int = 20,
    sqrt_bits: int = 80,
) -> P93LocalizedRejectionCertificate:
    """Return the exact localized finite-sample P92 rejection certificate.

    The function checks that the supplied rational empirical law is compatible
    with ``sample_size``. It then builds the three P92 minors, computes their
    exact determinant signs and sign-stability radii, and combines them with a
    P79-certified upper bound on the seven-cell Hoeffding radius.

    Rejection is certified only when all three conditions hold:

    1. the empirical determinant product is negative;
    2. every selected determinant has a valid positive sign-stability radius;
    3. the certified sampling-radius upper bound is strictly smaller than the
       smallest of those three radii.
    """

    sample_size = _validate_sample_size(sample_size)
    alpha = _validate_alpha(alpha)
    matrices = p92_selected_minor_matrices_exact(empirical_law)
    _validate_empirical_law_sample_compatibility(empirical_law, sample_size)

    determinants = tuple(determinant_2_by_2_exact(matrix) for matrix in matrices)
    product = determinants[0] * determinants[1] * determinants[2]
    radii = tuple(_safe_sign_stability_radius(matrix) for matrix in matrices)
    minimum_radius = min(radii)

    sampling_radius = certified_finite_alphabet_sampling_radius(
        sample_size=sample_size,
        alphabet_size=_SELECTED_CELL_COUNT,
        alpha=alpha,
        series_terms=series_terms,
        sqrt_bits=sqrt_bits,
    )

    rejects = (
        product < 0
        and minimum_radius > 0
        and sampling_radius.cell_linf_radius_upper < minimum_radius
    )
    conclusion = (
        "P75 rejected by localized P92 sign coherence at confidence at least 1-alpha"
        if rejects
        else "P75 not rejected by the localized P93 certificate"
    )
    return P93LocalizedRejectionCertificate(
        sample_size=sample_size,
        alpha=alpha,
        confidence_lower=1 - alpha,
        selected_cell_count=_SELECTED_CELL_COUNT,
        determinants=determinants,
        determinant_product=product,
        sign_stability_radii=radii,
        minimum_sign_stability_radius=minimum_radius,
        sampling_radius=sampling_radius,
        rejects_p75=rejects,
        conclusion=conclusion,
    )


def certify_p93_witness_95_threshold_exact(
    *,
    series_terms: int = 20,
    sqrt_bits: int = 80,
) -> P93WitnessThresholdCertificate:
    """Certify the exact 1622/1623 crossing for the P92 witness radius.

    The P93 localized seven-cell condition is ``eps_n,7(0.05) < 1/24``.
    P79 lower and upper rational envelopes prove that n=1622 is still above
    the boundary while n=1623 is below it. Monotonicity in n then proves that
    1623 is the first integer sample size satisfying the exact mathematical
    inequality.

    For comparison, the generic P77 fixed-margin design theorem at population
    margin tau=1/24 requires ``eps_n,16(0.05) < 1/48``. The corresponding exact
    P79 crossing is 7443/7444. These are different sufficient conditions: P93
    exploits the observed P92 sign witness, whereas the P77 bound is a generic
    fixed-population-margin guarantee.
    """

    last = certified_finite_alphabet_sampling_radius(
        sample_size=1622,
        alphabet_size=_SELECTED_CELL_COUNT,
        alpha=_P93_ALPHA_95,
        series_terms=series_terms,
        sqrt_bits=sqrt_bits,
    )
    first = certified_finite_alphabet_sampling_radius(
        sample_size=1623,
        alphabet_size=_SELECTED_CELL_COUNT,
        alpha=_P93_ALPHA_95,
        series_terms=series_terms,
        sqrt_bits=sqrt_bits,
    )
    if last.cell_linf_radius_lower <= _P92_WITNESS_RADIUS:
        raise RuntimeError("P79 lower envelope does not certify n=1622 as insufficient")
    if first.cell_linf_radius_upper >= _P92_WITNESS_RADIUS:
        raise RuntimeError("P79 upper envelope does not certify n=1623 as sufficient")

    generic_last = certified_finite_alphabet_sampling_radius(
        sample_size=7443,
        alphabet_size=16,
        alpha=_P93_ALPHA_95,
        series_terms=series_terms,
        sqrt_bits=sqrt_bits,
    )
    generic_first = certified_finite_alphabet_sampling_radius(
        sample_size=7444,
        alphabet_size=16,
        alpha=_P93_ALPHA_95,
        series_terms=series_terms,
        sqrt_bits=sqrt_bits,
    )
    generic_threshold = Fraction(1, 48)
    if generic_last.cell_linf_radius_lower <= generic_threshold:
        raise RuntimeError("P79 lower envelope does not certify n=7443 as insufficient")
    if generic_first.cell_linf_radius_upper >= generic_threshold:
        raise RuntimeError("P79 upper envelope does not certify n=7444 as sufficient")

    base_sample_size = 24
    first_replication = (
        (1623 + base_sample_size - 1) // base_sample_size
    ) * base_sample_size
    return P93WitnessThresholdCertificate(
        alpha=_P93_ALPHA_95,
        witness_radius=_P92_WITNESS_RADIUS,
        last_noncertifying_sample_size=1622,
        first_certifying_sample_size=1623,
        last_radius=last,
        first_radius=first,
        base_profile_sample_size=base_sample_size,
        first_exact_replication_sample_size=first_replication,
        generic_p77_last_noncertifying_sample_size=7443,
        generic_p77_first_certifying_sample_size=7444,
        generic_p77_last_radius=generic_last,
        generic_p77_first_radius=generic_first,
    )
