"""P88 complete parity-linear separation with exact primal-dual certification.

P83-P87 build an increasingly strong hierarchy of exact linear functionals of the
11 nontrivial even-parity observables on four binary views. P88 closes the linear
parity-witness class by admitting every real linear combination of those 11 parity
coordinates, rather than enlarging another finite coefficient box.

For a coefficient vector c and parity-feature vector h(p), define Q_c=c^T h(p).
Let A be the 16-by-11 incidence matrix whose (x,J) entry is one when outcome x has
even parity on view set J. Mass conservation gives the exact transfer norm

    D(c) = min_a ||A c - a 1||_1.

The complete parity-linear component over a P75 parameter box B is

    L88_par(B) = sup_{D(c) <= 1}
        [c^T h_hat - max_{v in Vert(B)} c^T h(v)].

The P75 parity coordinates are multi-affine in the nine box parameters, so support
extrema occur at parameter-box vertices. The resulting optimization is a finite
linear program with exact dual

    min mu
    s.t. lambda is a probability vector on parameter-box vertices,
         1^T r = 0,
         A^T r = h_hat - sum_v lambda_v h(v),
         |r_x| <= mu.

A matching rational primal witness and rational dual feasible point therefore
certify the parity-linear optimum exactly without trusting floating-point output.

Crucially, the published P87 certificate is recursive: it retains earlier
non-parity lower bounds as well as P83-P87 parity witnesses. Therefore the full P88
hierarchy is defined as

    L88(B) = max(L87(B), L88_par(B)).

This makes pointwise dominance over P87 exact without falsely claiming that parity
features subsume every earlier non-parity certificate.

P88 is a conditional model-separation theorem for the declared P75 family. It
closes the linear parity-witness class, but it does not prove that parity
observables are complete for the full law, identify a latent state with
consciousness, establish nonphysicality, or solve the physical-to-experiential
bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product

from consciousness_bridge.bounded_primitive_quad_projection_parity_functional_separation import (
    p75_box_p87_linf_lower_bound_exact,
)
from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.projection_parity_model_separation import (
    empirical_projection_parity_probability_exact,
)

_VIEW_COUNT = 4
_OUTCOME_COUNT = 16
_PARAMETER_COUNT = 9

ParityCoefficientVector = tuple[Fraction, ...]
ParameterVertex = tuple[Fraction, ...]
WeightedParameterVertex = tuple[Fraction, ParameterVertex]


def _standard_even_view_sets() -> tuple[tuple[int, ...], ...]:
    return tuple(
        views
        for size in range(2, _VIEW_COUNT + 1)
        for views in combinations(range(_VIEW_COUNT), size)
    )


_STANDARD_VIEW_SETS = _standard_even_view_sets()
_PARITY_DIMENSION = len(_STANDARD_VIEW_SETS)
_OUTCOMES = tuple(product((0, 1), repeat=_VIEW_COUNT))
_INCIDENCE = tuple(
    tuple(
        int(sum(outcome[view] for view in views) % 2 == 0)
        for views in _STANDARD_VIEW_SETS
    )
    for outcome in _OUTCOMES
)


@dataclass(frozen=True)
class P88ParityLinearWitness:
    """One exact parity-linear full-law L-infinity lower-bound witness."""

    lower_bound: Fraction
    coefficients: ParityCoefficientVector
    empirical_value: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    interval_gap: Fraction
    centered_coefficient_norm: Fraction
    centering_constant: Fraction


@dataclass(frozen=True)
class P88DualCertificate:
    """Exact dual feasible point for the complete P88 parity-linear LP."""

    bound: Fraction
    vertex_weights: tuple[WeightedParameterVertex, ...]
    residual: tuple[Fraction, ...]


@dataclass(frozen=True)
class P88ParityOptimalityCertificate:
    """Matching exact primal and dual certificates for the parity-linear optimum."""

    optimum: Fraction
    primal: P88ParityLinearWitness
    dual: P88DualCertificate


@dataclass(frozen=True)
class P88HierarchyCertificate:
    """Full P88 certificate retaining the recursive P87 baseline."""

    lower_bound: Fraction
    p87_lower_bound: Fraction
    parity_optimum: Fraction
    parity_certificate: P88ParityOptimalityCertificate


def p88_standard_parity_dimension() -> int:
    """Return the 11 nontrivial even-parity coordinates used by P88."""

    return _PARITY_DIMENSION


def p88_standard_even_view_sets() -> tuple[tuple[int, ...], ...]:
    """Return the canonical order of the 11 P88 parity coordinates."""

    return _STANDARD_VIEW_SETS


def _as_fraction(value: Fraction | int, *, name: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} entries must be integers or fractions.Fraction values")
    return Fraction(value)


def _coefficient_vector_exact(
    coefficients: tuple[Fraction | int, ...],
) -> ParityCoefficientVector:
    if len(coefficients) != _PARITY_DIMENSION:
        raise ValueError(f"coefficients must contain {_PARITY_DIMENSION} entries")
    result = tuple(_as_fraction(value, name="coefficient") for value in coefficients)
    if all(value == 0 for value in result):
        raise ValueError("P88 coefficient vector must be nonzero")
    return result


def _validate_empirical_law(empirical_law: tuple[Fraction, ...]) -> None:
    if len(empirical_law) != _OUTCOME_COUNT:
        raise ValueError("empirical_law must contain sixteen probabilities")
    if any(not isinstance(value, Fraction) for value in empirical_law):
        raise TypeError("empirical_law entries must be fractions.Fraction values")
    if any(value < 0 for value in empirical_law):
        raise ValueError("empirical_law entries must be nonnegative")
    if sum(empirical_law, start=Fraction(0)) != 1:
        raise ValueError("empirical_law must sum exactly to one")


def empirical_even_parity_feature_vector_exact(
    empirical_law: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    """Return the exact 11-coordinate even-parity feature vector."""

    _validate_empirical_law(empirical_law)
    return tuple(
        empirical_projection_parity_probability_exact(empirical_law, views, 0)
        for views in _STANDARD_VIEW_SETS
    )


def _parity_probability_from_responses(
    responses: tuple[Fraction, ...],
    views: tuple[int, ...],
) -> Fraction:
    parity_product = Fraction(1)
    for view in views:
        parity_product *= responses[view]
    return (1 + parity_product) / 2


def parity_feature_vector_from_parameters_exact(
    parameters: ParameterVertex,
) -> tuple[Fraction, ...]:
    """Return the exact P75 even-parity feature vector at one parameter point."""

    if len(parameters) != _PARAMETER_COUNT:
        raise ValueError("P75 parameter vector must contain nine entries")
    if any(not isinstance(value, Fraction) for value in parameters):
        raise TypeError("P75 parameter entries must be fractions.Fraction values")

    prevalence = parameters[0]
    minus_responses = tuple(1 - 2 * parameters[1 + 2 * view] for view in range(4))
    plus_responses = tuple(1 - 2 * parameters[2 + 2 * view] for view in range(4))
    return tuple(
        (1 - prevalence) * _parity_probability_from_responses(minus_responses, views)
        + prevalence * _parity_probability_from_responses(plus_responses, views)
        for views in _STANDARD_VIEW_SETS
    )


def p75_box_parameter_vertices_exact(
    box: P78ParameterBox,
) -> tuple[ParameterVertex, ...]:
    """Return all distinct exact endpoint vertices of a rational P75 box."""

    if len(box.lower) != _PARAMETER_COUNT or len(box.upper) != _PARAMETER_COUNT:
        raise ValueError("P88 requires a nine-parameter P75 box")
    endpoints = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    return tuple(dict.fromkeys(product(*endpoints)))


def p75_box_parity_feature_vertices_exact(
    box: P78ParameterBox,
) -> tuple[tuple[Fraction, ...], ...]:
    """Return distinct parity-feature vectors attained at box vertices."""

    return tuple(
        dict.fromkeys(
            parity_feature_vector_from_parameters_exact(vertex)
            for vertex in p75_box_parameter_vertices_exact(box)
        )
    )


def _dot_exact(
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
) -> Fraction:
    return sum(
        (a * b for a, b in zip(left, right, strict=True)),
        start=Fraction(0),
    )


def parity_linear_centered_coefficient_norm_exact(
    coefficients: tuple[Fraction | int, ...],
) -> tuple[Fraction, Fraction]:
    """Return D(c)=min_a ||A c-a1||_1 and one minimizing center exactly."""

    c = _coefficient_vector_exact(coefficients)
    outcome_coefficients = tuple(
        sum(
            (
                c[index] * incidence
                for index, incidence in enumerate(incidence_row)
            ),
            start=Fraction(0),
        )
        for incidence_row in _INCIDENCE
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
        raise RuntimeError("nonzero parity coefficient vector unexpectedly has zero norm")
    return norm, center


def p75_box_parity_linear_interval_exact(
    box: P78ParameterBox,
    coefficients: tuple[Fraction | int, ...],
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 box interval of an arbitrary parity-linear functional."""

    c = _coefficient_vector_exact(coefficients)
    values = tuple(
        _dot_exact(c, feature_vector)
        for feature_vector in p75_box_parity_feature_vertices_exact(box)
    )
    return min(values), max(values)


def p75_box_parity_linear_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    coefficients: tuple[Fraction | int, ...],
) -> P88ParityLinearWitness:
    """Return one exact P88 parity-linear full-law lower-bound witness."""

    c = _coefficient_vector_exact(coefficients)
    empirical_features = empirical_even_parity_feature_vector_exact(empirical_law)
    empirical_value = _dot_exact(c, empirical_features)
    interval_lower, interval_upper = p75_box_parity_linear_interval_exact(box, c)
    if empirical_value < interval_lower:
        interval_gap = interval_lower - empirical_value
    elif empirical_value > interval_upper:
        interval_gap = empirical_value - interval_upper
    else:
        interval_gap = Fraction(0)
    norm, center = parity_linear_centered_coefficient_norm_exact(c)
    return P88ParityLinearWitness(
        lower_bound=interval_gap / norm,
        coefficients=c,
        empirical_value=empirical_value,
        interval_lower=interval_lower,
        interval_upper=interval_upper,
        interval_gap=interval_gap,
        centered_coefficient_norm=norm,
        centering_constant=center,
    )


def _is_box_vertex(box: P78ParameterBox, parameters: ParameterVertex) -> bool:
    if len(parameters) != _PARAMETER_COUNT:
        return False
    return all(
        value == lower or value == upper
        for value, lower, upper in zip(
            parameters,
            box.lower,
            box.upper,
            strict=True,
        )
    )


def verify_p88_dual_certificate_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    certificate: P88DualCertificate,
) -> bool:
    """Verify an exact rational upper certificate for the parity-linear LP."""

    _validate_empirical_law(empirical_law)
    if not isinstance(certificate.bound, Fraction):
        raise TypeError("dual bound must be a fractions.Fraction")
    if certificate.bound < 0:
        return False
    if len(certificate.residual) != _OUTCOME_COUNT:
        return False
    if any(not isinstance(value, Fraction) for value in certificate.residual):
        raise TypeError("dual residual entries must be fractions.Fraction values")
    if sum(certificate.residual, start=Fraction(0)) != 0:
        return False
    if any(abs(value) > certificate.bound for value in certificate.residual):
        return False
    if not certificate.vertex_weights:
        return False

    total_weight = Fraction(0)
    weighted_feature = [Fraction(0) for _ in range(_PARITY_DIMENSION)]
    for weight, parameters in certificate.vertex_weights:
        if not isinstance(weight, Fraction):
            raise TypeError("dual vertex weights must be fractions.Fraction values")
        if weight < 0:
            return False
        if any(not isinstance(value, Fraction) for value in parameters):
            raise TypeError("dual parameter vertices must contain fractions.Fraction values")
        if not _is_box_vertex(box, parameters):
            return False
        total_weight += weight
        feature = parity_feature_vector_from_parameters_exact(parameters)
        for index, value in enumerate(feature):
            weighted_feature[index] += weight * value
    if total_weight != 1:
        return False

    empirical_feature = empirical_even_parity_feature_vector_exact(empirical_law)
    for coordinate in range(_PARITY_DIMENSION):
        residual_feature = sum(
            (
                certificate.residual[outcome_index]
                * _INCIDENCE[outcome_index][coordinate]
                for outcome_index in range(_OUTCOME_COUNT)
            ),
            start=Fraction(0),
        )
        if weighted_feature[coordinate] + residual_feature != empirical_feature[coordinate]:
            return False
    return True


def certify_p88_parity_optimality_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    coefficients: tuple[Fraction | int, ...],
    dual: P88DualCertificate,
) -> P88ParityOptimalityCertificate:
    """Certify the complete parity-linear optimum by matching primal and dual."""

    primal = p75_box_parity_linear_witness_exact(empirical_law, box, coefficients)
    if not verify_p88_dual_certificate_exact(empirical_law, box, dual):
        raise ValueError("P88 dual certificate is not feasible")
    if primal.lower_bound != dual.bound:
        raise ValueError("P88 primal and dual certificate values do not match")
    return P88ParityOptimalityCertificate(
        optimum=dual.bound,
        primal=primal,
        dual=dual,
    )


def certify_p88_hierarchy_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    coefficients: tuple[Fraction | int, ...],
    dual: P88DualCertificate,
) -> P88HierarchyCertificate:
    """Return max(P87, certified complete parity-linear optimum) exactly."""

    parity_certificate = certify_p88_parity_optimality_exact(
        empirical_law,
        box,
        coefficients,
        dual,
    )
    p87 = p75_box_p87_linf_lower_bound_exact(empirical_law, box)
    return P88HierarchyCertificate(
        lower_bound=max(p87, parity_certificate.optimum),
        p87_lower_bound=p87,
        parity_optimum=parity_certificate.optimum,
        parity_certificate=parity_certificate,
    )


def p88_dominates_p87_for_certified_hierarchy(
    certificate: P88HierarchyCertificate,
) -> bool:
    """Check the definitional pointwise dominance of the full P88 hierarchy."""

    return certificate.lower_bound >= certificate.p87_lower_bound


def p88_strict_witness_box() -> P78ParameterBox:
    """Return the exact P87/P88 strict-comparison box."""

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


def p88_strict_witness_empirical_law() -> tuple[Fraction, ...]:
    """Return the exact 24-sample empirical law used for strict P88 dominance."""

    counts = (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    return tuple(Fraction(count, 24) for count in counts)


def p88_strict_witness_coefficients() -> ParityCoefficientVector:
    """Return the exact 11-coordinate strict P88 coefficient vector."""

    return tuple(
        Fraction(value)
        for value in (0, 2, 1, -1, -1, -1, 2, 1, 3, -2, 3)
    )


def p88_strict_dual_certificate() -> P88DualCertificate:
    """Return the sparse exact dual certificate with parity optimum 5/168."""

    vertices: tuple[WeightedParameterVertex, ...] = (
        (
            Fraction(4, 189),
            (
                Fraction(0), Fraction(1, 4), Fraction(1, 2),
                Fraction(1, 4), Fraction(3, 4), Fraction(1),
                Fraction(1, 2), Fraction(1, 4), Fraction(3, 4),
            ),
        ),
        (
            Fraction(16, 189),
            (
                Fraction(0), Fraction(1, 4), Fraction(1, 2),
                Fraction(1, 4), Fraction(3, 4), Fraction(1),
                Fraction(1, 2), Fraction(1), Fraction(3, 4),
            ),
        ),
        (
            Fraction(16, 189),
            (
                Fraction(0), Fraction(1, 4), Fraction(1, 2),
                Fraction(1), Fraction(3, 4), Fraction(1),
                Fraction(1, 2), Fraction(1, 4), Fraction(3, 4),
            ),
        ),
        (
            Fraction(5, 42),
            (
                Fraction(0), Fraction(1, 4), Fraction(1, 2),
                Fraction(1), Fraction(3, 4), Fraction(1),
                Fraction(1, 2), Fraction(1), Fraction(3, 4),
            ),
        ),
        (
            Fraction(22, 63),
            (
                Fraction(0), Fraction(1), Fraction(1, 2),
                Fraction(1, 4), Fraction(3, 4), Fraction(1, 2),
                Fraction(1, 2), Fraction(1, 4), Fraction(3, 4),
            ),
        ),
        (
            Fraction(40, 189),
            (
                Fraction(0), Fraction(1), Fraction(1, 2),
                Fraction(1, 4), Fraction(3, 4), Fraction(1),
                Fraction(1, 2), Fraction(1), Fraction(3, 4),
            ),
        ),
        (
            Fraction(7, 54),
            (
                Fraction(0), Fraction(1), Fraction(1, 2),
                Fraction(1), Fraction(3, 4), Fraction(1, 2),
                Fraction(1, 2), Fraction(1), Fraction(3, 4),
            ),
        ),
    )
    residual = (
        Fraction(-5, 168),
        Fraction(-5, 168),
        Fraction(5, 168),
        Fraction(5, 168),
        Fraction(-5, 168),
        Fraction(1, 84),
        Fraction(5, 168),
        Fraction(0),
        Fraction(5, 168),
        Fraction(-5, 168),
        Fraction(-5, 168),
        Fraction(5, 168),
        Fraction(-5, 168),
        Fraction(2, 189),
        Fraction(11, 504),
        Fraction(-11, 756),
    )
    return P88DualCertificate(
        bound=Fraction(5, 168),
        vertex_weights=vertices,
        residual=residual,
    )


def p88_strict_parity_optimality_certificate_exact() -> P88ParityOptimalityCertificate:
    """Return the exact strict parity-linear optimum on the common witness box."""

    return certify_p88_parity_optimality_exact(
        p88_strict_witness_empirical_law(),
        p88_strict_witness_box(),
        p88_strict_witness_coefficients(),
        p88_strict_dual_certificate(),
    )


def p88_strict_hierarchy_certificate_exact() -> P88HierarchyCertificate:
    """Return the exact full P88 hierarchy certificate on the common witness."""

    return certify_p88_hierarchy_exact(
        p88_strict_witness_empirical_law(),
        p88_strict_witness_box(),
        p88_strict_witness_coefficients(),
        p88_strict_dual_certificate(),
    )
