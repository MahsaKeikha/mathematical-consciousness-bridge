"""P91 mixed-prevalence rank-two flattening separation for the P75 model.

P90 proves an exact nonlinear separation on the strict P75 face where the
latent prevalence is fixed at zero. P91 removes that boundary-case prevalence
restriction. For arbitrary prevalence, every bipartite 4 by 4 flattening of the
four-view two-component latent model is a sum of two rank-one matrices and
therefore has matrix rank at most two. Consequently every 3 by 3 minor vanishes.

For the established exact empirical witness, one selected 3 by 3 minor of the
(X1, X4) versus (X2, X3) flattening has determinant 1/512. Exact enumeration of
the 512 vertices of the nonnegative entrywise L-infinity box at radius 1/42
shows that the determinant remains at least 23/677376, which is strictly
positive. Hence no P75 model law, at any prevalence in [0, 1], can lie in the
closed L-infinity ball of radius 1/42 around the empirical law.

An explicit rational P75 parameter point with prevalence 4/5 attains full-law
L-infinity distance exactly 1/24. Thus P91 gives the certified global bracket

    1/42 < d_inf(P_emp, M_75) <= 1/24.

This is a conditional model-separation theorem for the declared P75 model
family. It does not identify the latent state with consciousness, establish
nonphysicality, validate an alternative theory, or solve the
physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product

from consciousness_bridge.certified_continuous_model_separation import (
    linf_distance_exact,
    p75_four_view_law_exact,
)

_OUTCOME_COUNT = 16
_P75_PARAMETER_COUNT = 9
_FLATTENING_ROW_VIEWS = (0, 3)
_FLATTENING_COLUMN_VIEWS = (1, 2)
_SELECTED_ROWS = (1, 2, 3)
_SELECTED_COLUMNS = (0, 1, 3)
_P91_RADIUS = Fraction(1, 42)


@dataclass(frozen=True)
class P91MinorIntervalCertificate:
    """Exact entrywise-box certificate for the selected flattening minor."""

    radius: Fraction
    empirical_minor: tuple[tuple[Fraction, ...], ...]
    empirical_determinant: Fraction
    minimum_vertex_determinant: Fraction
    maximum_vertex_determinant: Fraction
    vertex_count: int
    excludes_rank_two: bool


@dataclass(frozen=True)
class P91UpperCertificate:
    """Exact upper certificate from one genuinely mixed P75 parameter point."""

    radius: Fraction
    parameters: tuple[Fraction, ...]
    model_law: tuple[Fraction, ...]
    prevalence: Fraction
    flattening_rank_at_most_two: bool


@dataclass(frozen=True)
class P91MixedPrevalenceBracket:
    """Certified lower exclusion radius and explicit upper model radius."""

    excluded_closed_radius: Fraction
    upper_bound: Fraction
    lower: P91MinorIntervalCertificate
    upper: P91UpperCertificate
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


def _validate_parameters(parameters: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if len(parameters) != _P75_PARAMETER_COUNT:
        raise ValueError("exactly nine P75 parameters are required")
    for value in parameters:
        if not isinstance(value, Fraction):
            raise TypeError("P75 parameters must be fractions.Fraction")
        if value < 0 or value > 1:
            raise ValueError("P75 parameters must lie in [0, 1]")
    return parameters


def determinant_3_by_3_exact(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    """Return the exact determinant of a 3 by 3 rational matrix."""

    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("matrix must be 3 by 3")
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def p91_bipartite_flattening_exact(
    law: tuple[Fraction, ...],
) -> tuple[tuple[Fraction, ...], ...]:
    """Return the 4 by 4 (X1,X4) versus (X2,X3) probability flattening.

    Row and column states are both ordered lexicographically as
    ``00, 01, 10, 11``. The input law uses the repository-wide lexicographic
    ordering ``0000, 0001, ..., 1111``.
    """

    law = _validate_law(law)
    states = tuple(product((0, 1), repeat=2))
    rows: list[tuple[Fraction, ...]] = []
    for row_state in states:
        entries = []
        for column_state in states:
            pattern = [0, 0, 0, 0]
            for view, observed in zip(
                _FLATTENING_ROW_VIEWS, row_state, strict=True
            ):
                pattern[view] = observed
            for view, observed in zip(
                _FLATTENING_COLUMN_VIEWS, column_state, strict=True
            ):
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


def p91_selected_minor_exact(
    law: tuple[Fraction, ...],
) -> tuple[tuple[Fraction, ...], ...]:
    """Return the selected P91 3 by 3 flattening minor."""

    flattening = p91_bipartite_flattening_exact(law)
    return tuple(
        tuple(flattening[row][column] for column in _SELECTED_COLUMNS)
        for row in _SELECTED_ROWS
    )


def all_3_by_3_flattening_minors_exact(
    law: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    """Return all sixteen 3 by 3 minors of the canonical 4 by 4 flattening."""

    flattening = p91_bipartite_flattening_exact(law)
    minors = []
    for rows in combinations(range(4), 3):
        for columns in combinations(range(4), 3):
            matrix = tuple(
                tuple(flattening[row][column] for column in columns)
                for row in rows
            )
            minors.append(determinant_3_by_3_exact(matrix))
    return tuple(minors)


def _entry_interval(value: Fraction, radius: Fraction) -> tuple[Fraction, Fraction]:
    return max(Fraction(0), value - radius), min(Fraction(1), value + radius)


def p91_minor_interval_certificate_exact(
    empirical_law: tuple[Fraction, ...],
    *,
    radius: Fraction = _P91_RADIUS,
) -> P91MinorIntervalCertificate:
    """Certify that the selected minor cannot vanish inside a closed L-infinity ball.

    The determinant is multi-affine in its nine matrix entries. Therefore its
    minimum and maximum over the rectangular entrywise uncertainty box occur at
    vertices. Nonnegativity is retained by clipping each lower endpoint at zero.
    The routine enumerates all 2^9 = 512 vertices exactly with Fraction
    arithmetic.
    """

    empirical_law = _validate_law(empirical_law)
    if not isinstance(radius, Fraction):
        raise TypeError("radius must be a fractions.Fraction")
    if radius < 0:
        raise ValueError("radius must be nonnegative")

    minor = p91_selected_minor_exact(empirical_law)
    empirical_determinant = determinant_3_by_3_exact(minor)
    intervals = tuple(
        _entry_interval(value, radius)
        for row in minor
        for value in row
    )

    determinants: list[Fraction] = []
    for endpoint_choices in product((0, 1), repeat=9):
        entries = tuple(
            intervals[index][choice]
            for index, choice in enumerate(endpoint_choices)
        )
        vertex = (
            entries[0:3],
            entries[3:6],
            entries[6:9],
        )
        determinants.append(determinant_3_by_3_exact(vertex))

    minimum = min(determinants)
    maximum = max(determinants)
    excludes_rank_two = minimum > 0 or maximum < 0
    return P91MinorIntervalCertificate(
        radius=radius,
        empirical_minor=minor,
        empirical_determinant=empirical_determinant,
        minimum_vertex_determinant=minimum,
        maximum_vertex_determinant=maximum,
        vertex_count=len(determinants),
        excludes_rank_two=excludes_rank_two,
    )


def verify_p91_mixed_upper_certificate_exact(
    empirical_law: tuple[Fraction, ...],
    parameters: tuple[Fraction, ...],
) -> P91UpperCertificate:
    """Verify an explicit mixed-prevalence P75 model point and its exact radius."""

    empirical_law = _validate_law(empirical_law)
    parameters = _validate_parameters(parameters)
    prevalence = parameters[0]
    if prevalence <= 0 or prevalence >= 1:
        raise ValueError("P91 upper certificate requires genuinely mixed prevalence")

    model_law = p75_four_view_law_exact(parameters)
    radius = linf_distance_exact(empirical_law, model_law)
    minors = all_3_by_3_flattening_minors_exact(model_law)
    rank_at_most_two = all(value == 0 for value in minors)
    if not rank_at_most_two:
        raise RuntimeError("P75 model flattening unexpectedly violates rank at most two")

    return P91UpperCertificate(
        radius=radius,
        parameters=parameters,
        model_law=model_law,
        prevalence=prevalence,
        flattening_rank_at_most_two=rank_at_most_two,
    )


def certify_p91_mixed_prevalence_bracket_exact(
    empirical_law: tuple[Fraction, ...],
    parameters: tuple[Fraction, ...],
    *,
    radius: Fraction = _P91_RADIUS,
) -> P91MixedPrevalenceBracket:
    """Return the exact P91 global mixed-prevalence distance bracket."""

    lower = p91_minor_interval_certificate_exact(empirical_law, radius=radius)
    if not lower.excludes_rank_two:
        raise ValueError("selected P91 minor does not exclude rank two at this radius")
    upper = verify_p91_mixed_upper_certificate_exact(empirical_law, parameters)
    if upper.radius <= radius:
        raise RuntimeError("upper certificate conflicts with the strict lower exclusion")
    return P91MixedPrevalenceBracket(
        excluded_closed_radius=radius,
        upper_bound=upper.radius,
        lower=lower,
        upper=upper,
        conclusion=(
            "every P75 law is farther than the excluded closed radius, and the "
            "explicit mixed P75 law supplies the stated upper bound"
        ),
    )
