"""P79 certified rational sampling-radius envelopes for the P77/P78 handoff.

P77 gives the simultaneous finite-alphabet Hoeffding radius

    eps_n,K(alpha) = sqrt(log(2 K / alpha) / (2 n)).

P78 deliberately requires a mathematically valid *upper bound* on that radius
before its exact-rational model-distance lower bound can trigger full-law
rejection. Converting an ordinary floating-point approximation to ``Fraction``
does not make the comparison rigorous.

P79 closes that numerical certification gap for rational confidence levels.
It uses exact rational arithmetic plus an explicit convergent series remainder
bound for the natural logarithm. A power-of-two argument reduction keeps the
series parameter in [0, 1/3], and a dyadic ceiling then gives a rational upper
bound on the square root. The result is a reproducible rational envelope that
can be compared directly with P78's exact ``Fraction`` lower bound.

This theorem is a numerical-certification layer for P77/P78.
It does not validate the target-measurement model when rejection fails.
It does not identify any latent state with consciousness.
It does not solve the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt

from consciousness_bridge.certified_continuous_model_separation import (
    P78DistanceBracket,
    p77_rejection_from_certified_radius,
)


@dataclass(frozen=True)
class P79LogBracket:
    """Exact rational lower/upper bracket for a natural logarithm."""

    argument: Fraction
    lower: Fraction
    upper: Fraction
    series_terms: int

    @property
    def width(self) -> Fraction:
        """Return the rigorous logarithm-bracket width."""

        return self.upper - self.lower


@dataclass(frozen=True)
class P79SamplingRadiusCertificate:
    """Certified rational envelope for the P77 finite-alphabet radius."""

    sample_size: int
    alphabet_size: int
    alpha: Fraction
    series_terms: int
    sqrt_bits: int
    log_argument: Fraction
    log_lower: Fraction
    log_upper: Fraction
    cell_linf_radius_lower: Fraction
    cell_linf_radius_upper: Fraction
    joint_l1_radius_upper: Fraction
    conclusion: str

    @property
    def cell_linf_width(self) -> Fraction:
        """Return the certified L-infinity radius bracket width."""

        return self.cell_linf_radius_upper - self.cell_linf_radius_lower


def _positive_integer(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _floor_log2_fraction(value: Fraction) -> int:
    """Return floor(log2(value)) exactly for positive rational ``value``."""

    if not isinstance(value, Fraction):
        raise TypeError("value must be a fractions.Fraction")
    if value <= 0:
        raise ValueError("value must be positive")

    exponent = value.numerator.bit_length() - value.denominator.bit_length()
    power = Fraction(2) ** exponent

    while power > value:
        exponent -= 1
        power /= 2
    while 2 * power <= value:
        exponent += 1
        power *= 2
    return exponent


def _atanh_log_bracket_unit_interval(
    value: Fraction,
    *,
    series_terms: int,
) -> tuple[Fraction, Fraction]:
    """Bracket log(value) for 1 <= value <= 2 by the atanh series.

    With y=(value-1)/(value+1), one has

        log(value) = 2 sum_{j>=0} y^(2j+1)/(2j+1).

    On [1,2], y lies in [0,1/3]. Truncating after ``series_terms`` terms gives
    a lower bound because every omitted term is nonnegative. Bounding every
    omitted denominator by the first omitted denominator gives the rational
    tail bound

        R <= 2 y^(2m+1) / ((2m+1)(1-y^2)).
    """

    if not isinstance(value, Fraction):
        raise TypeError("value must be a fractions.Fraction")
    if value < 1 or value > 2:
        raise ValueError("value must lie in [1, 2]")
    _positive_integer(series_terms, name="series_terms")

    if value == 1:
        return Fraction(0), Fraction(0)

    y = (value - 1) / (value + 1)
    partial = Fraction(0)
    for index in range(series_terms):
        degree = 2 * index + 1
        partial += 2 * y**degree / degree

    first_omitted_degree = 2 * series_terms + 1
    tail_upper = (
        2
        * y**first_omitted_degree
        / (first_omitted_degree * (1 - y * y))
    )
    return partial, partial + tail_upper


def natural_log_rational_bracket(
    value: Fraction,
    *,
    series_terms: int = 12,
) -> P79LogBracket:
    """Return a rigorous rational bracket for ``log(value)``.

    The implementation first writes ``value = 2^k r`` with ``1 <= r < 2``.
    Both ``log(2)`` and ``log(r)`` are then bounded by the same positive atanh
    series with an explicit remainder bound. P79 only needs values greater than
    one, but reciprocal handling is included for completeness.
    """

    if not isinstance(value, Fraction):
        raise TypeError("value must be a fractions.Fraction")
    if value <= 0:
        raise ValueError("value must be positive")
    _positive_integer(series_terms, name="series_terms")

    if value == 1:
        return P79LogBracket(value, Fraction(0), Fraction(0), series_terms)

    if value < 1:
        reciprocal = natural_log_rational_bracket(
            1 / value,
            series_terms=series_terms,
        )
        return P79LogBracket(
            argument=value,
            lower=-reciprocal.upper,
            upper=-reciprocal.lower,
            series_terms=series_terms,
        )

    exponent = _floor_log2_fraction(value)
    reduced = value / (Fraction(2) ** exponent)
    if reduced == 2:
        exponent += 1
        reduced = Fraction(1)

    log2_lower, log2_upper = _atanh_log_bracket_unit_interval(
        Fraction(2),
        series_terms=series_terms,
    )
    reduced_lower, reduced_upper = _atanh_log_bracket_unit_interval(
        reduced,
        series_terms=series_terms,
    )

    return P79LogBracket(
        argument=value,
        lower=exponent * log2_lower + reduced_lower,
        upper=exponent * log2_upper + reduced_upper,
        series_terms=series_terms,
    )


def _dyadic_sqrt_bracket(
    value: Fraction,
    *,
    bits: int,
) -> tuple[Fraction, Fraction]:
    """Return dyadic lower/upper bounds on sqrt(value) using integer arithmetic."""

    if not isinstance(value, Fraction):
        raise TypeError("value must be a fractions.Fraction")
    if value < 0:
        raise ValueError("value must be nonnegative")
    _positive_integer(bits, name="bits")

    if value == 0:
        return Fraction(0), Fraction(0)

    denominator = 1 << bits
    scaled_numerator = value.numerator * denominator * denominator
    source_denominator = value.denominator

    lower_integer = isqrt(scaled_numerator // source_denominator)
    while (
        (lower_integer + 1) * (lower_integer + 1) * source_denominator
        <= scaled_numerator
    ):
        lower_integer += 1
    while lower_integer * lower_integer * source_denominator > scaled_numerator:
        lower_integer -= 1

    upper_integer = lower_integer
    if lower_integer * lower_integer * source_denominator < scaled_numerator:
        upper_integer += 1

    return (
        Fraction(lower_integer, denominator),
        Fraction(upper_integer, denominator),
    )


def certified_finite_alphabet_sampling_radius(
    *,
    sample_size: int,
    alphabet_size: int,
    alpha: Fraction,
    series_terms: int = 12,
    sqrt_bits: int = 48,
) -> P79SamplingRadiusCertificate:
    """Certify rational lower/upper bounds on the P77 Hoeffding radius.

    ``alpha`` is required as an exact rational input. The returned
    ``cell_linf_radius_upper`` is mathematically guaranteed to satisfy

        eps_n,K(alpha) <= cell_linf_radius_upper.

    The lower radius is also certified, which makes the numerical envelope
    inspectable rather than returning only a one-sided decimal approximation.
    """

    sample_size = _positive_integer(sample_size, name="sample_size")
    alphabet_size = _positive_integer(alphabet_size, name="alphabet_size")
    _positive_integer(series_terms, name="series_terms")
    _positive_integer(sqrt_bits, name="sqrt_bits")

    if not isinstance(alpha, Fraction):
        raise TypeError("alpha must be a fractions.Fraction")
    if alpha <= 0 or alpha >= 1:
        raise ValueError("alpha must lie strictly between zero and one")

    log_argument = Fraction(2 * alphabet_size, 1) / alpha
    log_bracket = natural_log_rational_bracket(
        log_argument,
        series_terms=series_terms,
    )

    variance_lower = log_bracket.lower / (2 * sample_size)
    variance_upper = log_bracket.upper / (2 * sample_size)

    radius_lower, _ = _dyadic_sqrt_bracket(
        variance_lower,
        bits=sqrt_bits,
    )
    _, radius_upper = _dyadic_sqrt_bracket(
        variance_upper,
        bits=sqrt_bits,
    )

    joint_l1_upper = min(Fraction(2), alphabet_size * radius_upper)
    conclusion = (
        "certified rational upper envelope for the P77 sampling radius; "
        "safe for strict comparison with P78 exact-rational lower bounds"
    )
    return P79SamplingRadiusCertificate(
        sample_size=sample_size,
        alphabet_size=alphabet_size,
        alpha=alpha,
        series_terms=series_terms,
        sqrt_bits=sqrt_bits,
        log_argument=log_argument,
        log_lower=log_bracket.lower,
        log_upper=log_bracket.upper,
        cell_linf_radius_lower=radius_lower,
        cell_linf_radius_upper=radius_upper,
        joint_l1_radius_upper=joint_l1_upper,
        conclusion=conclusion,
    )


def p78_rejection_with_p79_radius(
    bracket: P78DistanceBracket,
    radius: P79SamplingRadiusCertificate,
) -> bool:
    """Apply the strict P77/P78 rejection gate using a P79-certified radius."""

    return p77_rejection_from_certified_radius(
        bracket,
        sampling_radius_upper=radius.cell_linf_radius_upper,
    )
