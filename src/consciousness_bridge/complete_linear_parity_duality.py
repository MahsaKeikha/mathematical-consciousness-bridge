"""P89 complete linear parity-functional duality certificates.

P88 exhausts a finite radius-three integer family supported on four of the
canonical P83 parity coordinates. P89 closes a different gap: it considers
*every real linear functional* of all eleven canonical even-parity coordinates
at once.

For a rational P75 parameter box, every linear parity functional is
multi-affine in the nine model parameters, so its exact range is attained at
parameter-box vertices. The resulting complete linear-functional problem has a
finite convex dual. A lower certificate is one explicit linear functional. A
matching upper certificate is a convex combination of box-vertex parity vectors
plus a zero-mass signed outcome perturbation whose L-infinity radius reproduces
the empirical parity vector. Equality of the two exact rational certificates
proves the unrestricted linear-parity optimum without bounding coefficient
magnitudes or support size.

This is a conditional model-separation result for the declared P75
measurement family. It does not identify the latent state with consciousness,
establish nonphysicality, validate a replacement model, or solve the
physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
)
from consciousness_bridge.projection_parity_model_separation import (
    empirical_projection_parity_probability_exact,
)

_VIEW_COUNT = 4
_OUTCOME_COUNT = 16
_PARAMETER_COUNT = 9
_OUTCOMES = tuple(product((0, 1), repeat=_VIEW_COUNT))
_CANONICAL_VIEW_SETS = tuple(
    views
    for size in range(2, _VIEW_COUNT + 1)
    for views in combinations(range(_VIEW_COUNT), size)
)

RationalCoefficient = int | Fraction
ParityVector = tuple[Fraction, ...]


@dataclass(frozen=True)
class P89LinearParityFunctionalWitness:
    """Exact lower certificate from one unrestricted linear parity functional."""

    lower_bound: Fraction
    coefficients: tuple[Fraction, ...]
    empirical_value: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    interval_gap: Fraction
    centered_coefficient_norm: Fraction
    centering_constant: Fraction


@dataclass(frozen=True)
class P89LinearParityUpperCertificate:
    """Exact universal upper certificate for the complete linear parity family."""

    radius: Fraction
    vertex_weights: tuple[Fraction, ...]
    perturbation: tuple[Fraction, ...]
    empirical_parity_vector: ParityVector
    model_parity_vector: ParityVector
    residual_parity_vector: ParityVector


@dataclass(frozen=True)
class P89CompleteLinearParityCertificate:
    """Matching lower/upper certificate proving the exact P89 linear optimum."""

    optimum: Fraction
    functional: P89LinearParityFunctionalWitness
    upper: P89LinearParityUpperCertificate


def p89_canonical_parity_view_sets() -> tuple[tuple[int, ...], ...]:
    """Return the eleven canonical P83 even-parity view sets."""

    return _CANONICAL_VIEW_SETS


def _coerce_coefficients(
    coefficients: tuple[RationalCoefficient, ...],
) -> tuple[Fraction, ...]:
    if len(coefficients) != len(_CANONICAL_VIEW_SETS):
        raise ValueError("P89 requires exactly eleven parity coefficients")
    coerced: list[Fraction] = []
    for coefficient in coefficients:
        if isinstance(coefficient, bool) or not isinstance(
            coefficient, (int, Fraction)
        ):
            raise TypeError("P89 coefficients must be exact integers or Fractions")
        coerced.append(Fraction(coefficient))
    result = tuple(coerced)
    if all(coefficient == 0 for coefficient in result):
        raise ValueError("P89 coefficient vector must be nonzero")
    return result


def _coerce_exact_vector(
    values: tuple[RationalCoefficient, ...],
    *,
    length: int,
    name: str,
) -> tuple[Fraction, ...]:
    if len(values) != length:
        raise ValueError(f"{name} must contain exactly {length} entries")
    result: list[Fraction] = []
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
            raise TypeError(f"{name} entries must be exact integers or Fractions")
        result.append(Fraction(value))
    return tuple(result)


def _validate_empirical_law(
    empirical_law: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    if len(empirical_law) != _OUTCOME_COUNT:
        raise ValueError("empirical_law must contain sixteen probabilities")
    for value in empirical_law:
        if not isinstance(value, Fraction):
            raise TypeError("empirical_law entries must be fractions.Fraction")
        if value < 0 or value > 1:
            raise ValueError("empirical_law entries must lie in [0, 1]")
    if sum(empirical_law, start=Fraction(0)) != 1:
        raise ValueError("empirical_law must have total mass one")
    return empirical_law


def empirical_p89_parity_vector_exact(
    empirical_law: tuple[Fraction, ...],
) -> ParityVector:
    """Return all eleven canonical even-parity probabilities exactly."""

    empirical_law = _validate_empirical_law(empirical_law)
    return tuple(
        empirical_projection_parity_probability_exact(empirical_law, views, 0)
        for views in _CANONICAL_VIEW_SETS
    )


def p75_parity_vector_from_parameters_exact(
    parameters: tuple[Fraction, ...],
) -> ParityVector:
    """Return the eleven canonical P83 parity probabilities for one P75 point."""

    if len(parameters) != _PARAMETER_COUNT:
        raise ValueError("exactly nine P75 model parameters are required")
    for value in parameters:
        if not isinstance(value, Fraction):
            raise TypeError("P75 parameters must be fractions.Fraction")
        if value < 0 or value > 1:
            raise ValueError("P75 parameters must lie in [0, 1]")

    prevalence_plus = parameters[0]
    vector: list[Fraction] = []
    for views in _CANONICAL_VIEW_SETS:
        minus_product = Fraction(1)
        plus_product = Fraction(1)
        for view in views:
            minus_product *= 1 - 2 * parameters[1 + 2 * view]
            plus_product *= 1 - 2 * parameters[2 + 2 * view]
        minus_probability = (1 + minus_product) / 2
        plus_probability = (1 + plus_product) / 2
        vector.append(
            (1 - prevalence_plus) * minus_probability
            + prevalence_plus * plus_probability
        )
    return tuple(vector)


def p75_box_parity_vertex_vectors_exact(
    box: P78ParameterBox,
) -> tuple[ParityVector, ...]:
    """Return distinct P75 parity vectors at the rational box vertices.

    Endpoint order is lower then upper in every parameter coordinate. Duplicate
    parity vectors are removed while preserving first occurrence. The convex
    hull of these vectors has the same support function as the full P75 box
    image for every linear parity functional.
    """

    endpoint_sets = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    vertices: list[ParityVector] = []
    seen: set[ParityVector] = set()
    for parameters in product(*endpoint_sets):
        vector = p75_parity_vector_from_parameters_exact(tuple(parameters))
        if vector not in seen:
            seen.add(vector)
            vertices.append(vector)
    return tuple(vertices)


def p89_parity_incidence_matrix() -> tuple[tuple[int, ...], ...]:
    """Return the 16 by 11 outcome-to-even-parity incidence matrix."""

    return tuple(
        tuple(
            int(sum(outcome[view] for view in views) % 2 == 0)
            for views in _CANONICAL_VIEW_SETS
        )
        for outcome in _OUTCOMES
    )


def empirical_complete_linear_parity_functional_exact(
    empirical_law: tuple[Fraction, ...],
    coefficients: tuple[RationalCoefficient, ...],
) -> Fraction:
    """Return one complete linear-parity functional on the empirical law."""

    coefficient_vector = _coerce_coefficients(coefficients)
    parity_vector = empirical_p89_parity_vector_exact(empirical_law)
    return sum(
        (
            coefficient * probability
            for coefficient, probability in zip(
                coefficient_vector, parity_vector, strict=True
            )
        ),
        start=Fraction(0),
    )


def p75_box_complete_linear_parity_functional_interval_exact(
    box: P78ParameterBox,
    coefficients: tuple[RationalCoefficient, ...],
) -> tuple[Fraction, Fraction]:
    """Return the exact P75-box interval for one P89 linear functional."""

    coefficient_vector = _coerce_coefficients(coefficients)
    values = tuple(
        sum(
            (
                coefficient * probability
                for coefficient, probability in zip(
                    coefficient_vector, vertex, strict=True
                )
            ),
            start=Fraction(0),
        )
        for vertex in p75_box_parity_vertex_vectors_exact(box)
    )
    return min(values), max(values)


def complete_linear_parity_centered_coefficient_norm_exact(
    coefficients: tuple[RationalCoefficient, ...],
) -> tuple[Fraction, Fraction]:
    """Return D(c)=min_a sum_x |g_c(x)-a| and one minimizing center."""

    coefficient_vector = _coerce_coefficients(coefficients)
    incidence = p89_parity_incidence_matrix()
    outcome_coefficients = tuple(
        sum(
            (
                coefficient * indicator
                for coefficient, indicator in zip(
                    coefficient_vector, row, strict=True
                )
            ),
            start=Fraction(0),
        )
        for row in incidence
    )
    candidates = tuple(sorted(set(outcome_coefficients)))
    norm, center = min(
        (
            sum(
                (abs(value - candidate) for value in outcome_coefficients),
                start=Fraction(0),
            ),
            candidate,
        )
        for candidate in candidates
    )
    if norm <= 0:
        raise RuntimeError("nonzero P89 functional unexpectedly has zero norm")
    return norm, center


def _distance_to_interval(
    value: Fraction,
    lower: Fraction,
    upper: Fraction,
) -> Fraction:
    if value < lower:
        return lower - value
    if value > upper:
        return value - upper
    return Fraction(0)


def p75_box_complete_linear_parity_functional_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    coefficients: tuple[RationalCoefficient, ...],
) -> P89LinearParityFunctionalWitness:
    """Return the exact lower certificate from one unrestricted P89 direction."""

    coefficient_vector = _coerce_coefficients(coefficients)
    empirical_value = empirical_complete_linear_parity_functional_exact(
        empirical_law, coefficient_vector
    )
    interval_lower, interval_upper = (
        p75_box_complete_linear_parity_functional_interval_exact(
            box, coefficient_vector
        )
    )
    interval_gap = _distance_to_interval(
        empirical_value, interval_lower, interval_upper
    )
    centered_norm, center = complete_linear_parity_centered_coefficient_norm_exact(
        coefficient_vector
    )
    return P89LinearParityFunctionalWitness(
        lower_bound=interval_gap / centered_norm,
        coefficients=coefficient_vector,
        empirical_value=empirical_value,
        interval_lower=interval_lower,
        interval_upper=interval_upper,
        interval_gap=interval_gap,
        centered_coefficient_norm=centered_norm,
        centering_constant=center,
    )


def verify_complete_linear_parity_upper_certificate_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    vertex_weights: tuple[RationalCoefficient, ...],
    perturbation: tuple[RationalCoefficient, ...],
) -> P89LinearParityUpperCertificate:
    """Verify one exact universal upper certificate for every linear direction.

    The weights form a convex combination of distinct box-vertex parity
    vectors. The signed perturbation has zero total mass and must reproduce the
    difference between the empirical parity vector and that convex combination.
    Its L-infinity radius then upper-bounds every normalized linear-parity
    mismatch, regardless of coefficient magnitudes or support size.
    """

    empirical_parity = empirical_p89_parity_vector_exact(empirical_law)
    vertices = p75_box_parity_vertex_vectors_exact(box)
    weights = _coerce_exact_vector(
        vertex_weights,
        length=len(vertices),
        name="vertex_weights",
    )
    if any(weight < 0 for weight in weights):
        raise ValueError("vertex_weights must be nonnegative")
    if sum(weights, start=Fraction(0)) != 1:
        raise ValueError("vertex_weights must sum exactly to one")

    delta = _coerce_exact_vector(
        perturbation,
        length=_OUTCOME_COUNT,
        name="perturbation",
    )
    if sum(delta, start=Fraction(0)) != 0:
        raise ValueError("perturbation must have exact zero total mass")

    model_parity = tuple(
        sum(
            (weight * vertex[index] for weight, vertex in zip(weights, vertices)),
            start=Fraction(0),
        )
        for index in range(len(_CANONICAL_VIEW_SETS))
    )
    incidence = p89_parity_incidence_matrix()
    residual_parity = tuple(
        sum(
            (
                delta[outcome_index] * incidence[outcome_index][parity_index]
                for outcome_index in range(_OUTCOME_COUNT)
            ),
            start=Fraction(0),
        )
        for parity_index in range(len(_CANONICAL_VIEW_SETS))
    )
    reconstructed = tuple(
        model + residual
        for model, residual in zip(model_parity, residual_parity, strict=True)
    )
    if reconstructed != empirical_parity:
        raise ValueError(
            "upper certificate does not reconstruct the empirical parity vector"
        )

    radius = max(abs(value) for value in delta)
    return P89LinearParityUpperCertificate(
        radius=radius,
        vertex_weights=weights,
        perturbation=delta,
        empirical_parity_vector=empirical_parity,
        model_parity_vector=model_parity,
        residual_parity_vector=residual_parity,
    )


def certify_complete_linear_parity_optimum_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    coefficients: tuple[RationalCoefficient, ...],
    vertex_weights: tuple[RationalCoefficient, ...],
    perturbation: tuple[RationalCoefficient, ...],
) -> P89CompleteLinearParityCertificate:
    """Certify the exact unrestricted P89 linear optimum by matching bounds.

    A functional witness gives a lower bound on the supremum over all real
    eleven-coordinate parity coefficients. A valid primal perturbation
    certificate gives a universal upper bound. Exact equality proves the
    optimum over the complete linear family.
    """

    functional = p75_box_complete_linear_parity_functional_witness_exact(
        empirical_law, box, coefficients
    )
    upper = verify_complete_linear_parity_upper_certificate_exact(
        empirical_law, box, vertex_weights, perturbation
    )
    if functional.lower_bound != upper.radius:
        raise ValueError(
            "P89 completeness requires matching exact lower and upper bounds"
        )
    return P89CompleteLinearParityCertificate(
        optimum=functional.lower_bound,
        functional=functional,
        upper=upper,
    )
