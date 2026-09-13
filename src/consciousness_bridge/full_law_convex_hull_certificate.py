"""P88 exact full-law convex-hull certificate for the P75 model family.

P78-P87 build increasingly strong exact lower bounds on the full-law L-infinity
distance from an empirical four-bit distribution to the declared P75 latent
measurement family. P88 adds the complete *linear full-law* relaxation on each
rational parameter box.

The P75 four-view law F(theta) is vector-valued multi-affine in its nine parameters.
For every axis-aligned box B, multilinear interpolation therefore gives

    F(B) subset conv{F(v) : v is a vertex of B} = C_B.

Consequently

    dist_inf(p_hat, C_B) <= dist_inf(p_hat, F(B)),

so distance to the finite vertex convex hull is a certified model-distance lower
bound. It is computable by a finite linear program.

The same quantity has a complete linear-separation form. For arbitrary sixteen-cell
coefficients g, probability-mass conservation permits centering by any constant,
with exact transfer norm

    D(g) = min_a ||g - a 1||_1.

Thus

    dist_inf(p_hat, C_B)
      = sup_{D(g) <= 1} [g^T p_hat - max_{v in Vert(B)} g^T F(v)].

The implementation does not need to trust a floating-point LP optimum. A rational
linear witness gives a lower bound on the convex-hull distance, while a rational
convex combination of box-vertex laws gives an upper bound. Matching values certify
the convex-hull optimum exactly.

The published P87 hierarchy recursively retains earlier specialized lower bounds.
For maximal caution, the full P88 hierarchy is therefore defined as

    L88(B) = max(L87(B), L88_ch(B)),

where L88_ch is the exact full-law convex-hull distance.

On the common exact P86-P87 witness box, P88 has an especially simple strict
certificate: the signed cell contrast P(1000)-P(1010) has empirical gap 1/8,
centered norm 2, and nonpositive P75 box support, giving 1/16. A seven-vertex
rational convex combination lies exactly 1/16 from the empirical law, proving
L88_ch=1/16. Since L87=1/96 on the same witness, P88 is strictly stronger.

P88 is a conditional model-separation theorem. It does not identify the P75 latent
state with consciousness, prove that the convex hull equals the nonlinear P75
family, establish nonphysicality, or solve the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product

from consciousness_bridge.bounded_primitive_quad_projection_parity_functional_separation import (
    p75_box_p87_linf_lower_bound_exact,
)
from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    p75_four_view_law_exact,
)

_OUTCOME_COUNT = 16
_PARAMETER_COUNT = 9
ParameterVertex = tuple[Fraction, ...]
WeightedParameterVertex = tuple[Fraction, ParameterVertex]


@dataclass(frozen=True)
class P88FullLawLinearWitness:
    """One exact linear full-law separating witness."""

    lower_bound: Fraction
    coefficients: tuple[Fraction, ...]
    empirical_value: Fraction
    support_lower: Fraction
    support_upper: Fraction
    support_gap: Fraction
    centered_coefficient_norm: Fraction
    centering_constant: Fraction


@dataclass(frozen=True)
class P88ConvexHullPoint:
    """One exact point in the convex hull of P75 parameter-box vertex laws."""

    distance: Fraction
    vertex_weights: tuple[WeightedParameterVertex, ...]
    law: tuple[Fraction, ...]


@dataclass(frozen=True)
class P88ConvexHullOptimalityCertificate:
    """Matching exact lower and upper witnesses for the convex-hull distance."""

    optimum: Fraction
    linear_witness: P88FullLawLinearWitness
    convex_hull_point: P88ConvexHullPoint


@dataclass(frozen=True)
class P88HierarchyCertificate:
    """Full P88 certificate retaining the recursive P87 baseline."""

    lower_bound: Fraction
    p87_lower_bound: Fraction
    convex_hull_lower_bound: Fraction
    convex_hull_certificate: P88ConvexHullOptimalityCertificate


def _validate_empirical_law(empirical_law: tuple[Fraction, ...]) -> None:
    if len(empirical_law) != _OUTCOME_COUNT:
        raise ValueError("empirical_law must contain sixteen probabilities")
    if any(not isinstance(value, Fraction) for value in empirical_law):
        raise TypeError("empirical_law entries must be fractions.Fraction values")
    if any(value < 0 for value in empirical_law):
        raise ValueError("empirical_law entries must be nonnegative")
    if sum(empirical_law, start=Fraction(0)) != 1:
        raise ValueError("empirical_law must sum exactly to one")


def _validate_coefficients(coefficients: tuple[Fraction | int, ...]) -> tuple[Fraction, ...]:
    if len(coefficients) != _OUTCOME_COUNT:
        raise ValueError("full-law coefficient vector must contain sixteen entries")
    exact: list[Fraction] = []
    for value in coefficients:
        if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
            raise TypeError("coefficients must be integers or fractions.Fraction values")
        exact.append(Fraction(value))
    if len(set(exact)) == 1:
        raise ValueError("coefficient vector must be nonconstant modulo mass conservation")
    return tuple(exact)


def p75_box_parameter_vertices_exact(
    box: P78ParameterBox,
) -> tuple[ParameterVertex, ...]:
    """Return all distinct endpoint vertices of a rational nine-parameter box."""

    if len(box.lower) != _PARAMETER_COUNT or len(box.upper) != _PARAMETER_COUNT:
        raise ValueError("P88 requires a nine-parameter P75 box")
    endpoints = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    return tuple(product(*endpoints))


def p75_box_law_vertices_exact(
    box: P78ParameterBox,
) -> tuple[tuple[Fraction, ...], ...]:
    """Return the distinct P75 full laws attained at parameter-box vertices."""

    return tuple(
        dict.fromkeys(
            p75_four_view_law_exact(vertex)
            for vertex in p75_box_parameter_vertices_exact(box)
        )
    )


def centered_full_law_coefficient_norm_exact(
    coefficients: tuple[Fraction | int, ...],
) -> tuple[Fraction, Fraction]:
    """Return min_a ||g-a1||_1 and one exact minimizing center."""

    g = _validate_coefficients(coefficients)
    candidates = tuple(sorted(set(g)))
    norm, center = min(
        (
            sum((abs(value - candidate) for value in g), start=Fraction(0)),
            candidate,
        )
        for candidate in candidates
    )
    if norm <= 0:
        raise RuntimeError("nonconstant full-law functional unexpectedly has zero norm")
    return norm, center


def _dot_exact(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum(
        (a * b for a, b in zip(left, right, strict=True)),
        start=Fraction(0),
    )


def p75_box_full_law_linear_interval_exact(
    box: P78ParameterBox,
    coefficients: tuple[Fraction | int, ...],
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 box support interval of one linear full-law functional."""

    g = _validate_coefficients(coefficients)
    values = tuple(_dot_exact(g, law) for law in p75_box_law_vertices_exact(box))
    return min(values), max(values)


def p75_box_full_law_linear_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    coefficients: tuple[Fraction | int, ...],
) -> P88FullLawLinearWitness:
    """Return one exact linear lower bound on distance to the P75 box."""

    _validate_empirical_law(empirical_law)
    g = _validate_coefficients(coefficients)
    empirical_value = _dot_exact(g, empirical_law)
    support_lower, support_upper = p75_box_full_law_linear_interval_exact(box, g)
    if empirical_value < support_lower:
        support_gap = support_lower - empirical_value
    elif empirical_value > support_upper:
        support_gap = empirical_value - support_upper
    else:
        support_gap = Fraction(0)
    norm, center = centered_full_law_coefficient_norm_exact(g)
    return P88FullLawLinearWitness(
        lower_bound=support_gap / norm,
        coefficients=g,
        empirical_value=empirical_value,
        support_lower=support_lower,
        support_upper=support_upper,
        support_gap=support_gap,
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


def p88_convex_hull_point_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    vertex_weights: tuple[WeightedParameterVertex, ...],
) -> P88ConvexHullPoint:
    """Verify and return one exact convex combination of P75 box-vertex laws."""

    _validate_empirical_law(empirical_law)
    if not vertex_weights:
        raise ValueError("at least one weighted parameter vertex is required")

    total_weight = Fraction(0)
    law = [Fraction(0) for _ in range(_OUTCOME_COUNT)]
    for weight, parameters in vertex_weights:
        if not isinstance(weight, Fraction):
            raise TypeError("convex-hull weights must be fractions.Fraction values")
        if weight < 0:
            raise ValueError("convex-hull weights must be nonnegative")
        if any(not isinstance(value, Fraction) for value in parameters):
            raise TypeError("parameter vertices must contain fractions.Fraction values")
        if not _is_box_vertex(box, parameters):
            raise ValueError("convex-hull support point is not a vertex of the P75 box")
        total_weight += weight
        vertex_law = p75_four_view_law_exact(parameters)
        for index, value in enumerate(vertex_law):
            law[index] += weight * value
    if total_weight != 1:
        raise ValueError("convex-hull weights must sum exactly to one")

    exact_law = tuple(law)
    distance = max(
        abs(empirical - model)
        for empirical, model in zip(empirical_law, exact_law, strict=True)
    )
    return P88ConvexHullPoint(
        distance=distance,
        vertex_weights=vertex_weights,
        law=exact_law,
    )


def certify_p88_convex_hull_optimum_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    coefficients: tuple[Fraction | int, ...],
    vertex_weights: tuple[WeightedParameterVertex, ...],
) -> P88ConvexHullOptimalityCertificate:
    """Certify the exact convex-hull distance when lower and upper witnesses match."""

    linear_witness = p75_box_full_law_linear_witness_exact(
        empirical_law,
        box,
        coefficients,
    )
    convex_hull_point = p88_convex_hull_point_exact(
        empirical_law,
        box,
        vertex_weights,
    )
    if linear_witness.lower_bound != convex_hull_point.distance:
        raise ValueError("P88 linear and convex-hull certificate values do not match")
    return P88ConvexHullOptimalityCertificate(
        optimum=linear_witness.lower_bound,
        linear_witness=linear_witness,
        convex_hull_point=convex_hull_point,
    )


def certify_p88_hierarchy_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    coefficients: tuple[Fraction | int, ...],
    vertex_weights: tuple[WeightedParameterVertex, ...],
) -> P88HierarchyCertificate:
    """Return max(P87, exact full-law convex-hull certificate)."""

    convex_hull_certificate = certify_p88_convex_hull_optimum_exact(
        empirical_law,
        box,
        coefficients,
        vertex_weights,
    )
    p87 = p75_box_p87_linf_lower_bound_exact(empirical_law, box)
    return P88HierarchyCertificate(
        lower_bound=max(p87, convex_hull_certificate.optimum),
        p87_lower_bound=p87,
        convex_hull_lower_bound=convex_hull_certificate.optimum,
        convex_hull_certificate=convex_hull_certificate,
    )


def p88_strict_witness_box() -> P78ParameterBox:
    """Return the common exact P86-P88 strict-comparison box."""

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
    """Return the exact 24-sample empirical law used from P86 onward."""

    counts = (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    return tuple(Fraction(count, 24) for count in counts)


def p88_strict_linear_coefficients() -> tuple[Fraction, ...]:
    """Return g=1_{1000}-1_{1010} in lexicographic four-bit order."""

    coefficients = [Fraction(0) for _ in range(_OUTCOME_COUNT)]
    coefficients[8] = Fraction(1)
    coefficients[10] = Fraction(-1)
    return tuple(coefficients)


def p88_strict_convex_hull_weights() -> tuple[WeightedParameterVertex, ...]:
    """Return the seven-vertex exact upper witness for distance 1/16."""

    return (
        (
            Fraction(10, 27),
            (
                Fraction(0), Fraction(1, 4), Fraction(1, 2),
                Fraction(1, 4), Fraction(3, 4), Fraction(1, 2),
                Fraction(1, 2), Fraction(1), Fraction(3, 4),
            ),
        ),
        (
            Fraction(2, 27),
            (
                Fraction(0), Fraction(1, 4), Fraction(1, 2),
                Fraction(1), Fraction(3, 4), Fraction(1, 2),
                Fraction(1, 2), Fraction(1), Fraction(3, 4),
            ),
        ),
        (
            Fraction(2, 9),
            (
                Fraction(0), Fraction(1), Fraction(1, 2),
                Fraction(1, 4), Fraction(3, 4), Fraction(1, 2),
                Fraction(1, 2), Fraction(1, 4), Fraction(3, 4),
            ),
        ),
        (
            Fraction(7, 54),
            (
                Fraction(0), Fraction(1), Fraction(1, 2),
                Fraction(1, 4), Fraction(3, 4), Fraction(1, 2),
                Fraction(1, 2), Fraction(1), Fraction(3, 4),
            ),
        ),
        (
            Fraction(1, 18),
            (
                Fraction(0), Fraction(1), Fraction(1, 2),
                Fraction(1, 4), Fraction(3, 4), Fraction(1),
                Fraction(1, 2), Fraction(1), Fraction(3, 4),
            ),
        ),
        (
            Fraction(1, 27),
            (
                Fraction(0), Fraction(1), Fraction(1, 2),
                Fraction(1), Fraction(3, 4), Fraction(1, 2),
                Fraction(1, 2), Fraction(1), Fraction(3, 4),
            ),
        ),
        (
            Fraction(1, 9),
            (
                Fraction(0), Fraction(1), Fraction(1, 2),
                Fraction(1), Fraction(3, 4), Fraction(1),
                Fraction(1, 2), Fraction(1), Fraction(3, 4),
            ),
        ),
    )


@lru_cache(maxsize=1)
def p88_strict_convex_hull_certificate_exact() -> P88ConvexHullOptimalityCertificate:
    """Return the exact full-law convex-hull optimum 1/16 on the strict witness."""

    return certify_p88_convex_hull_optimum_exact(
        p88_strict_witness_empirical_law(),
        p88_strict_witness_box(),
        p88_strict_linear_coefficients(),
        p88_strict_convex_hull_weights(),
    )


@lru_cache(maxsize=1)
def p88_strict_hierarchy_certificate_exact() -> P88HierarchyCertificate:
    """Return the exact full P88 hierarchy certificate on the common witness."""

    return certify_p88_hierarchy_exact(
        p88_strict_witness_empirical_law(),
        p88_strict_witness_box(),
        p88_strict_linear_coefficients(),
        p88_strict_convex_hull_weights(),
    )
