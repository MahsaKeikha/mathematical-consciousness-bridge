"""P92 complete single-minor optimality for rank-two flattening certificates.

P91 selected one 3 by 3 minor of the (X1,X4) versus (X2,X3) flattening and
certified separation of the full two-component P75 model at radius 1/42.

P92 audits the complete class of single 3 by 3 minor certificates from all
three 2+2 bipartitions of the four binary views. Every P75 law has rank at
most two in each such 4 by 4 flattening, so all 48 minors vanish.

At the published P91 radius 1/42, exactly one of those 48 minors excludes
rank two under the entrywise L-infinity box relaxation: the P91 minor.

For that selected minor, exact polynomial and Sturm-sequence analysis shows
that the first determinant-vertex zero before radius 1/41 occurs at

    rho_* = (17 - sqrt(193)) / 128,

the smaller root of 512 r^2 - 136 r + 3. Thus the selected single-minor
relaxation excludes rank two for every r < rho_* and cannot certify strict
separation at r = rho_* because one box vertex has zero determinant.

Consequently the full P75 model distance obeys the stronger lower bound

    d_inf(P_emp, M_75) >= rho_*,

while P91's explicit mixed model point still gives the upper bound 1/24.

This is an exact optimality result for the declared single-minor box
certificate class. It is not an exact solution of the full nonlinear P75
distance problem, and it does not identify the latent variable with
consciousness or close the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product

from consciousness_bridge.certified_continuous_model_separation import (
    p75_four_view_law_exact,
)
from consciousness_bridge.mixed_prevalence_rank_two_flattening_separation import (
    determinant_3_by_3_exact,
)

_OUTCOME_COUNT = 16
_BIPARTITIONS = ((0, 1), (0, 2), (0, 3))
_PUBLISHED_RADIUS = Fraction(1, 42)
_ROOT_AUDIT_CEILING = Fraction(1, 41)
_P91_ROW_VIEWS = (0, 3)
_P91_COLUMN_VIEWS = (1, 2)
_P91_ROWS = (1, 2, 3)
_P91_COLUMNS = (0, 1, 3)
_P91_ACTIVE_VERTEX = (1, 1, 0, 0, 0, 1, 0, 0, 1)

Polynomial = tuple[Fraction, ...]


@dataclass(frozen=True)
class MinorIndex:
    """Identify one 3 by 3 minor inside one 2+2 probability flattening."""

    row_views: tuple[int, int]
    column_views: tuple[int, int]
    rows: tuple[int, int, int]
    columns: tuple[int, int, int]


@dataclass(frozen=True)
class MinorBoxCertificate:
    """Exact determinant range over one entrywise uncertainty box."""

    index: MinorIndex
    radius: Fraction
    empirical_determinant: Fraction
    minimum_vertex_determinant: Fraction
    maximum_vertex_determinant: Fraction
    vertex_count: int
    excludes_rank_two: bool


@dataclass(frozen=True)
class QuadraticSurdRadius:
    """Represent (a - sqrt(radicand)) / denominator exactly."""

    a: int
    radicand: int
    denominator: int

    def greater_than_fraction(self, value: Fraction) -> bool:
        """Return whether this exact surd is strictly greater than value."""

        residual = Fraction(self.a) - self.denominator * value
        if residual <= 0:
            return False
        return residual * residual > self.radicand

    def less_than_fraction(self, value: Fraction) -> bool:
        """Return whether this exact surd is strictly less than value."""

        residual = Fraction(self.a) - self.denominator * value
        if residual <= 0:
            return True
        return residual * residual < self.radicand


@dataclass(frozen=True)
class P75BipartiteRankTwoFactorization:
    """Exact two-component outer-product factorization of one P75 flattening."""

    row_views: tuple[int, int]
    column_views: tuple[int, int]
    weights: tuple[Fraction, Fraction]
    row_factors: tuple[tuple[Fraction, ...], tuple[Fraction, ...]]
    column_factors: tuple[tuple[Fraction, ...], tuple[Fraction, ...]]
    flattening: tuple[tuple[Fraction, ...], ...]


@dataclass(frozen=True)
class P92SingleMinorOptimalityCertificate:
    """Complete exact audit of the 48 single-minor rank-two certificates."""

    total_minor_count: int
    published_radius: Fraction
    certifying_minor_count: int
    selected_minor: MinorIndex
    selected_empirical_determinant: Fraction
    selected_minimum_at_published_radius: Fraction
    selected_maximum_at_published_radius: Fraction
    active_vertex: tuple[int, ...]
    active_vertex_polynomial: Polynomial
    root_audit_ceiling: Fraction
    active_root_count_below_ceiling: int
    other_vertex_root_count_below_ceiling: int
    exact_relaxation_ceiling: QuadraticSurdRadius
    conclusion: str


def _validate_law(law: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if len(law) != _OUTCOME_COUNT:
        raise ValueError("law must contain sixteen probabilities")
    for value in law:
        if not isinstance(value, Fraction):
            raise TypeError("law entries must be fractions.Fraction")
        if value < 0 or value > 1:
            raise ValueError("law entries must lie in [0, 1]")
    if sum(law, start=Fraction(0)) != 1:
        raise ValueError("law must have total mass one")
    return law


def bipartite_flattening_exact(
    law: tuple[Fraction, ...],
    row_views: tuple[int, int],
) -> tuple[tuple[Fraction, ...], ...]:
    """Return one exact 4 by 4 flattening for a two-view row bipartition."""

    law = _validate_law(law)
    if len(row_views) != 2 or len(set(row_views)) != 2:
        raise ValueError("row_views must contain two distinct view indices")
    if any(view not in range(4) for view in row_views):
        raise ValueError("view indices must lie in {0,1,2,3}")
    column_views = tuple(view for view in range(4) if view not in row_views)
    states = tuple(product((0, 1), repeat=2))
    rows = []
    for row_state in states:
        entries = []
        for column_state in states:
            pattern = [0, 0, 0, 0]
            for view, observed in zip(row_views, row_state, strict=True):
                pattern[view] = observed
            for view, observed in zip(column_views, column_state, strict=True):
                pattern[view] = observed
            index = (
                8 * pattern[0]
                + 4 * pattern[1]
                + 2 * pattern[2]
                + pattern[3]
            )
            entries.append(law[index])
        rows.append(tuple(entries))
    return tuple(rows)


def p75_bipartite_rank_two_factorization_exact(
    parameters: tuple[Fraction, ...],
    row_views: tuple[int, int],
) -> P75BipartiteRankTwoFactorization:
    """Return the exact two-term outer-product decomposition of a P75 flattening."""

    if len(parameters) != 9:
        raise ValueError("exactly nine P75 parameters are required")
    for value in parameters:
        if not isinstance(value, Fraction):
            raise TypeError("P75 parameters must be fractions.Fraction")
        if value < 0 or value > 1:
            raise ValueError("P75 parameters must lie in [0, 1]")
    if len(row_views) != 2 or len(set(row_views)) != 2:
        raise ValueError("row_views must contain two distinct view indices")
    if any(view not in range(4) for view in row_views):
        raise ValueError("view indices must lie in {0,1,2,3}")

    column_views = tuple(view for view in range(4) if view not in row_views)
    states = tuple(product((0, 1), repeat=2))
    prevalence_plus = parameters[0]
    weights = (1 - prevalence_plus, prevalence_plus)

    def factor(view_set: tuple[int, int], *, plus: bool) -> tuple[Fraction, ...]:
        result = []
        offset = 2 if plus else 1
        for state in states:
            probability = Fraction(1)
            for view, observed in zip(view_set, state, strict=True):
                q = parameters[offset + 2 * view]
                probability *= q if observed else 1 - q
            result.append(probability)
        return tuple(result)

    row_minus = factor(row_views, plus=False)
    row_plus = factor(row_views, plus=True)
    column_minus = factor(column_views, plus=False)
    column_plus = factor(column_views, plus=True)

    flattening = tuple(
        tuple(
            weights[0] * row_minus[row] * column_minus[column]
            + weights[1] * row_plus[row] * column_plus[column]
            for column in range(4)
        )
        for row in range(4)
    )
    law = p75_four_view_law_exact(parameters)
    expected = bipartite_flattening_exact(law, row_views)
    if flattening != expected:
        raise RuntimeError("P75 outer-product factorization does not reconstruct the law")

    return P75BipartiteRankTwoFactorization(
        row_views=row_views,
        column_views=column_views,
        weights=weights,
        row_factors=(row_minus, row_plus),
        column_factors=(column_minus, column_plus),
        flattening=flattening,
    )


def all_single_minor_indices() -> tuple[MinorIndex, ...]:
    """Return the complete 48-minor class across the three 2+2 bipartitions."""

    indices = []
    for row_views in _BIPARTITIONS:
        column_views = tuple(view for view in range(4) if view not in row_views)
        for rows in combinations(range(4), 3):
            for columns in combinations(range(4), 3):
                indices.append(
                    MinorIndex(
                        row_views=row_views,
                        column_views=column_views,
                        rows=rows,
                        columns=columns,
                    )
                )
    return tuple(indices)


def _minor_matrix(
    flattening: tuple[tuple[Fraction, ...], ...],
    index: MinorIndex,
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(flattening[row][column] for column in index.columns)
        for row in index.rows
    )


def all_bipartite_minor_determinants_exact(
    law: tuple[Fraction, ...],
) -> tuple[tuple[MinorIndex, Fraction], ...]:
    """Return all 48 exact 3 by 3 determinant constraints."""

    law = _validate_law(law)
    result = []
    flattenings = {
        row_views: bipartite_flattening_exact(law, row_views)
        for row_views in _BIPARTITIONS
    }
    for index in all_single_minor_indices():
        matrix = _minor_matrix(flattenings[index.row_views], index)
        result.append((index, determinant_3_by_3_exact(matrix)))
    return tuple(result)


def _entry_interval(value: Fraction, radius: Fraction) -> tuple[Fraction, Fraction]:
    return max(Fraction(0), value - radius), min(Fraction(1), value + radius)


def minor_box_certificate_exact(
    law: tuple[Fraction, ...],
    index: MinorIndex,
    *,
    radius: Fraction,
) -> MinorBoxCertificate:
    """Return the exact determinant range over one minor entrywise box."""

    law = _validate_law(law)
    if not isinstance(radius, Fraction):
        raise TypeError("radius must be a fractions.Fraction")
    if radius < 0:
        raise ValueError("radius must be nonnegative")

    flattening = bipartite_flattening_exact(law, index.row_views)
    matrix = _minor_matrix(flattening, index)
    empirical_determinant = determinant_3_by_3_exact(matrix)
    intervals = tuple(
        _entry_interval(value, radius)
        for row in matrix
        for value in row
    )
    determinants = []
    for bits in product((0, 1), repeat=9):
        entries = tuple(
            intervals[position][bit]
            for position, bit in enumerate(bits)
        )
        vertex = (entries[0:3], entries[3:6], entries[6:9])
        determinants.append(determinant_3_by_3_exact(vertex))

    minimum = min(determinants)
    maximum = max(determinants)
    return MinorBoxCertificate(
        index=index,
        radius=radius,
        empirical_determinant=empirical_determinant,
        minimum_vertex_determinant=minimum,
        maximum_vertex_determinant=maximum,
        vertex_count=len(determinants),
        excludes_rank_two=minimum > 0 or maximum < 0,
    )


def complete_minor_box_audit_exact(
    law: tuple[Fraction, ...],
    *,
    radius: Fraction = _PUBLISHED_RADIUS,
) -> tuple[MinorBoxCertificate, ...]:
    """Audit all 48 single-minor certificates at one exact radius."""

    law = _validate_law(law)
    return tuple(
        minor_box_certificate_exact(law, index, radius=radius)
        for index in all_single_minor_indices()
    )


def _poly_trim(poly: Polynomial) -> Polynomial:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def _poly_add(left: Polynomial, right: Polynomial) -> Polynomial:
    size = max(len(left), len(right))
    result = [Fraction(0)] * size
    for index in range(size):
        if index < len(left):
            result[index] += left[index]
        if index < len(right):
            result[index] += right[index]
    return _poly_trim(tuple(result))


def _poly_neg(poly: Polynomial) -> Polynomial:
    return tuple(-value for value in poly)


def _poly_sub(left: Polynomial, right: Polynomial) -> Polynomial:
    return _poly_add(left, _poly_neg(right))


def _poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return _poly_trim(tuple(result))


def _poly_derivative(poly: Polynomial) -> Polynomial:
    if len(poly) == 1:
        return (Fraction(0),)
    return _poly_trim(
        tuple(Fraction(index) * poly[index] for index in range(1, len(poly)))
    )


def _poly_divmod(
    numerator: Polynomial,
    denominator: Polynomial,
) -> tuple[Polynomial, Polynomial]:
    numerator = _poly_trim(numerator)
    denominator = _poly_trim(denominator)
    if denominator == (Fraction(0),):
        raise ZeroDivisionError("polynomial division by zero")
    if len(numerator) < len(denominator):
        return (Fraction(0),), numerator

    quotient = [Fraction(0)] * (len(numerator) - len(denominator) + 1)
    remainder = list(numerator)
    while len(remainder) >= len(denominator) and any(remainder):
        shift = len(remainder) - len(denominator)
        factor = remainder[-1] / denominator[-1]
        quotient[shift] += factor
        for index, coefficient in enumerate(denominator):
            remainder[index + shift] -= factor * coefficient
        remainder = list(_poly_trim(tuple(remainder)))
    return _poly_trim(tuple(quotient)), _poly_trim(tuple(remainder))


def _poly_eval(poly: Polynomial, value: Fraction) -> Fraction:
    total = Fraction(0)
    for coefficient in reversed(poly):
        total = total * value + coefficient
    return total


def _sturm_sequence(poly: Polynomial) -> tuple[Polynomial, ...]:
    poly = _poly_trim(poly)
    derivative = _poly_derivative(poly)
    if derivative == (Fraction(0),):
        return (poly,)
    sequence = [poly, derivative]
    while sequence[-1] != (Fraction(0),):
        _, remainder = _poly_divmod(sequence[-2], sequence[-1])
        if remainder == (Fraction(0),):
            break
        sequence.append(_poly_neg(remainder))
    return tuple(sequence)


def _sign_variations(sequence: tuple[Polynomial, ...], value: Fraction) -> int:
    signs = []
    for poly in sequence:
        evaluated = _poly_eval(poly, value)
        if evaluated > 0:
            signs.append(1)
        elif evaluated < 0:
            signs.append(-1)
    return sum(left != right for left, right in zip(signs, signs[1:]))


def _root_count_open(
    poly: Polynomial,
    lower: Fraction,
    upper: Fraction,
) -> int:
    if not lower < upper:
        raise ValueError("lower must be strictly less than upper")
    if _poly_eval(poly, lower) == 0 or _poly_eval(poly, upper) == 0:
        raise ValueError("Sturm audit endpoints must not be polynomial roots")
    sequence = _sturm_sequence(poly)
    return _sign_variations(sequence, lower) - _sign_variations(sequence, upper)


def _linear_endpoint_polynomial(
    value: Fraction,
    bit: int,
) -> Polynomial:
    if bit not in (0, 1):
        raise ValueError("vertex bits must be zero or one")
    if bit == 1:
        return value, Fraction(1)
    if value == 0:
        return (Fraction(0),)
    return value, Fraction(-1)


def _determinant_polynomial(entries: tuple[Polynomial, ...]) -> Polynomial:
    if len(entries) != 9:
        raise ValueError("nine entry polynomials are required")
    a, b, c, d, e, f, g, h, i = entries
    first = _poly_mul(a, _poly_sub(_poly_mul(e, i), _poly_mul(f, h)))
    second = _poly_mul(b, _poly_sub(_poly_mul(d, i), _poly_mul(f, g)))
    third = _poly_mul(c, _poly_sub(_poly_mul(d, h), _poly_mul(e, g)))
    return _poly_add(_poly_sub(first, second), third)


def selected_minor_vertex_polynomials_exact(
    law: tuple[Fraction, ...],
) -> tuple[tuple[tuple[int, ...], Polynomial], ...]:
    """Return all 512 exact determinant polynomials for the P91 minor."""

    law = _validate_law(law)
    selected = MinorIndex(
        row_views=_P91_ROW_VIEWS,
        column_views=_P91_COLUMN_VIEWS,
        rows=_P91_ROWS,
        columns=_P91_COLUMNS,
    )
    flattening = bipartite_flattening_exact(law, selected.row_views)
    matrix = _minor_matrix(flattening, selected)
    values = tuple(value for row in matrix for value in row)

    positive_values = tuple(value for value in values if value > 0)
    if not positive_values or min(positive_values) <= _ROOT_AUDIT_CEILING:
        raise ValueError("root audit ceiling reaches a lower clipping breakpoint")
    if max(values) + _ROOT_AUDIT_CEILING >= 1:
        raise ValueError("root audit ceiling reaches an upper clipping breakpoint")

    result = []
    for bits in product((0, 1), repeat=9):
        entry_polynomials = tuple(
            _linear_endpoint_polynomial(value, bit)
            for value, bit in zip(values, bits, strict=True)
        )
        result.append((bits, _determinant_polynomial(entry_polynomials)))
    return tuple(result)


def certify_p92_complete_single_minor_optimality_exact(
    law: tuple[Fraction, ...],
) -> P92SingleMinorOptimalityCertificate:
    """Certify complete single-minor optimality and the exact relaxation ceiling."""

    law = _validate_law(law)
    audits = complete_minor_box_audit_exact(law, radius=_PUBLISHED_RADIUS)
    certifying = tuple(certificate for certificate in audits if certificate.excludes_rank_two)

    selected = MinorIndex(
        row_views=_P91_ROW_VIEWS,
        column_views=_P91_COLUMN_VIEWS,
        rows=_P91_ROWS,
        columns=_P91_COLUMNS,
    )
    if len(audits) != 48:
        raise RuntimeError("complete single-minor class must contain 48 minors")
    if len(certifying) != 1 or certifying[0].index != selected:
        raise RuntimeError("P91 minor is not uniquely certifying at radius 1/42")

    vertex_polynomials = selected_minor_vertex_polynomials_exact(law)
    active = dict(vertex_polynomials)[_P91_ACTIVE_VERTEX]
    expected_active = (
        Fraction(1, 512),
        Fraction(-17, 192),
        Fraction(1, 3),
    )
    if active != expected_active:
        raise RuntimeError("unexpected P91 active vertex polynomial")

    active_root_count = _root_count_open(
        active,
        Fraction(0),
        _ROOT_AUDIT_CEILING,
    )
    other_root_count = 0
    for bits, poly in vertex_polynomials:
        if bits == _P91_ACTIVE_VERTEX:
            continue
        other_root_count += _root_count_open(
            poly,
            Fraction(0),
            _ROOT_AUDIT_CEILING,
        )
    if active_root_count != 1 or other_root_count != 0:
        raise RuntimeError("selected minor root-ordering audit failed")

    exact_ceiling = QuadraticSurdRadius(a=17, radicand=193, denominator=128)
    if not exact_ceiling.greater_than_fraction(_PUBLISHED_RADIUS):
        raise RuntimeError("algebraic ceiling must improve the P91 rational radius")
    if not exact_ceiling.less_than_fraction(_ROOT_AUDIT_CEILING):
        raise RuntimeError("algebraic ceiling must lie below the Sturm audit ceiling")

    winner = certifying[0]
    return P92SingleMinorOptimalityCertificate(
        total_minor_count=len(audits),
        published_radius=_PUBLISHED_RADIUS,
        certifying_minor_count=len(certifying),
        selected_minor=selected,
        selected_empirical_determinant=winner.empirical_determinant,
        selected_minimum_at_published_radius=winner.minimum_vertex_determinant,
        selected_maximum_at_published_radius=winner.maximum_vertex_determinant,
        active_vertex=_P91_ACTIVE_VERTEX,
        active_vertex_polynomial=active,
        root_audit_ceiling=_ROOT_AUDIT_CEILING,
        active_root_count_below_ceiling=active_root_count,
        other_vertex_root_count_below_ceiling=other_root_count,
        exact_relaxation_ceiling=exact_ceiling,
        conclusion=(
            "the P91 minor is uniquely optimal among all 48 single-minor "
            "rank-two box certificates, with exact algebraic relaxation ceiling "
            "(17 - sqrt(193)) / 128"
        ),
    )
