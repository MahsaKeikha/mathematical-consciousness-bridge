"""Candidate P88 held-out certification for a selected P87 parity functional.

P87 can search 39,600 exact four-event parity functionals and return a strong
shared-parameter incompatibility witness.  If the same finite sample is used
both to select a functional and to test it, however, a naive single-functional
confidence statement ignores selection.  This module closes that statistical
gap under an explicit sample-splitting assumption: the functional may be
chosen arbitrarily from an independent discovery sample, then it is frozen and
evaluated on an independent validation sample.

Conditional on the discovery data, the selected score is fixed.  Hoeffding's
inequality therefore applies directly to the validation-sample mean, with no
union bound over the 39,600 candidate functionals.  The P79 rational logarithm
and dyadic square-root machinery is reused with alphabet_size=1 to produce a
mathematically certified rational upper bound on the scalar Hoeffding radius.
The resulting population functional gap is transferred to a full-law
L-infinity distance lower bound using the exact P87 centered coefficient norm.

The implementation cannot verify that discovery and validation data were
actually independent; that is a scientific data-provenance assumption that
must be established by the caller.  This result remains conditional on the
P75 model family and does not identify a latent state with consciousness,
prove consciousness is nonphysical, validate an alternative ontology, or
solve the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product

from consciousness_bridge.bounded_primitive_quad_projection_parity_functional_separation import (
    PrimitiveQuadFunctional,
    empirical_primitive_parity_quad_exact,
    p75_primitive_parity_quad_interval_exact,
    primitive_parity_quad_centered_coefficient_norm_exact,
)
from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.certified_sampling_radius import (
    certified_finite_alphabet_sampling_radius,
)

_OUTCOME_COUNT = 16


@dataclass(frozen=True)
class P88HeldOutParityFunctionalCertificate:
    """Exact-rational held-out certificate for one discovery-selected P87 score."""

    terms: PrimitiveQuadFunctional
    validation_sample_size: int
    alpha: Fraction
    empirical_value: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    empirical_interval_gap: Fraction
    score_minimum: Fraction
    score_maximum: Fraction
    score_width: Fraction
    unit_hoeffding_radius_upper: Fraction
    functional_radius_upper: Fraction
    population_interval_gap_lower: Fraction
    centered_coefficient_norm: Fraction
    linf_distance_lower_confidence_bound: Fraction
    rejects_box: bool
    validity_statement: str


def _positive_integer(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _validate_validation_empirical_law(
    empirical_law: tuple[Fraction, ...],
    *,
    sample_size: int,
) -> None:
    if len(empirical_law) != _OUTCOME_COUNT:
        raise ValueError("validation empirical law must contain sixteen probabilities")
    total = Fraction(0)
    for probability in empirical_law:
        if not isinstance(probability, Fraction):
            raise TypeError("validation empirical probabilities must be fractions.Fraction")
        if probability < 0:
            raise ValueError("validation empirical probabilities must be nonnegative")
        count = probability * sample_size
        if count.denominator != 1:
            raise ValueError(
                "validation empirical law is incompatible with validation_sample_size"
            )
        total += probability
    if total != 1:
        raise ValueError("validation empirical probabilities must sum exactly to one")


def _distance_to_interval(value: Fraction, lower: Fraction, upper: Fraction) -> Fraction:
    if value < lower:
        return lower - value
    if value > upper:
        return value - upper
    return Fraction(0)


def _score_value(
    outcome: tuple[int, int, int, int],
    terms: PrimitiveQuadFunctional,
) -> Fraction:
    return sum(
        (
            Fraction(coefficient)
            * int(sum(outcome[view] for view in views) % 2 == 0)
            for views, coefficient in terms
        ),
        start=Fraction(0),
    )


def primitive_parity_quad_score_range_exact(
    terms: PrimitiveQuadFunctional,
) -> tuple[Fraction, Fraction]:
    """Return the exact minimum and maximum cell score for one P87 functional."""

    # The public P87 norm routine performs the complete P87 functional validation.
    primitive_parity_quad_centered_coefficient_norm_exact(terms)
    values = tuple(_score_value(outcome, terms) for outcome in product((0, 1), repeat=4))
    return min(values), max(values)


def p88_heldout_selected_p87_certificate_exact(
    validation_empirical_law: tuple[Fraction, ...],
    *,
    validation_sample_size: int,
    box: P78ParameterBox,
    terms: PrimitiveQuadFunctional,
    alpha: Fraction,
    series_terms: int = 12,
    sqrt_bits: int = 48,
) -> P88HeldOutParityFunctionalCertificate:
    """Certify one independently selected P87 functional on held-out data.

    Statistical validity requires ``terms`` to have been fixed independently of
    the validation sample, for example by selecting it using a disjoint discovery
    sample.  Conditional on that discovery sample the score is fixed, so the
    two-sided Hoeffding radius is

        R * sqrt(log(2 / alpha) / (2 n)),

    where ``R`` is the exact score range.  P79 is called with ``alphabet_size=1``
    to obtain a rigorous rational upper envelope for the unit-range square-root
    factor.  No 39,600-way union bound is needed because validation is performed
    only after the independently selected functional has been frozen.
    """

    validation_sample_size = _positive_integer(
        validation_sample_size,
        name="validation_sample_size",
    )
    _validate_validation_empirical_law(
        validation_empirical_law,
        sample_size=validation_sample_size,
    )

    empirical_value = empirical_primitive_parity_quad_exact(
        validation_empirical_law,
        terms,
    )
    interval_lower, interval_upper = p75_primitive_parity_quad_interval_exact(
        box,
        terms,
    )
    empirical_gap = _distance_to_interval(
        empirical_value,
        interval_lower,
        interval_upper,
    )

    score_minimum, score_maximum = primitive_parity_quad_score_range_exact(terms)
    score_width = score_maximum - score_minimum
    if score_width <= 0:
        raise ValueError("selected P87 functional must have a positive score range")

    unit_radius = certified_finite_alphabet_sampling_radius(
        sample_size=validation_sample_size,
        alphabet_size=1,
        alpha=alpha,
        series_terms=series_terms,
        sqrt_bits=sqrt_bits,
    ).cell_linf_radius_upper
    functional_radius_upper = score_width * unit_radius
    population_gap_lower = max(
        Fraction(0),
        empirical_gap - functional_radius_upper,
    )

    centered_norm, _ = primitive_parity_quad_centered_coefficient_norm_exact(terms)
    if centered_norm <= 0:
        raise RuntimeError("selected P87 functional unexpectedly has zero centered norm")
    linf_lower = population_gap_lower / centered_norm
    rejects_box = empirical_gap > functional_radius_upper

    return P88HeldOutParityFunctionalCertificate(
        terms=terms,
        validation_sample_size=validation_sample_size,
        alpha=alpha,
        empirical_value=empirical_value,
        interval_lower=interval_lower,
        interval_upper=interval_upper,
        empirical_interval_gap=empirical_gap,
        score_minimum=score_minimum,
        score_maximum=score_maximum,
        score_width=score_width,
        unit_hoeffding_radius_upper=unit_radius,
        functional_radius_upper=functional_radius_upper,
        population_interval_gap_lower=population_gap_lower,
        centered_coefficient_norm=centered_norm,
        linf_distance_lower_confidence_bound=linf_lower,
        rejects_box=rejects_box,
        validity_statement=(
            "valid at confidence at least 1-alpha when the selected functional is "
            "fixed using data independent of the validation sample"
        ),
    )
