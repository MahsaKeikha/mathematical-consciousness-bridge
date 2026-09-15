"""P90 exact nonlinear rank-one slice separation for a single-component P75 box.

P89 closes every real linear functional of the eleven canonical parity
coordinates on the declared P75 box. P90 moves beyond that convex linear
envelope and uses a nonlinear rank-one identity of the actual model image.

When the latent prevalence is fixed to either zero or one, the P75 four-view
model reduces to one product Bernoulli law. Any 2 by 2 outcome slice obtained by
fixing two views and varying the other two therefore has determinant zero. For
the canonical strict witness used from P83 through P89, the slice with
(X1, X2) = (1, 0) and varying (X3, X4) has exact empirical entries

    (1/8, 1/24, 0, 5/24).

Its determinant is 5/192. A direct interval argument shows that every rank-one
nonnegative table is at L-infinity distance at least 5/72 from this slice. An
explicit rational P75 parameter point in the declared box realizes full-law
L-infinity distance exactly 5/72. Hence the exact distance from the empirical
law to this single-component P75 box is 5/72.

This is a conditional model-separation theorem for the declared P75 box. It
does not identify the latent state with consciousness, establish
nonphysicality, validate an alternative model, or solve the
physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    linf_distance_exact,
    p75_four_view_law_exact,
)

_OUTCOME_COUNT = 16
_CANONICAL_SLICE_INDICES = (8, 9, 10, 11)


@dataclass(frozen=True)
class P90RankOneLowerCertificate:
    """Exact nonlinear lower certificate from one canonical 2 by 2 slice."""

    lower_bound: Fraction
    slice_entries: tuple[Fraction, Fraction, Fraction, Fraction]
    determinant_residual: Fraction
    slice_mass: Fraction
    orientation: str


@dataclass(frozen=True)
class P90RankOneUpperCertificate:
    """Exact upper certificate from one explicit P75 parameter point."""

    radius: Fraction
    parameters: tuple[Fraction, ...]
    model_law: tuple[Fraction, ...]
    model_slice: tuple[Fraction, Fraction, Fraction, Fraction]
    model_determinant: Fraction


@dataclass(frozen=True)
class P90ExactNonlinearCertificate:
    """Matching lower and upper certificates for the exact P90 distance."""

    optimum: Fraction
    lower: P90RankOneLowerCertificate
    upper: P90RankOneUpperCertificate


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


def _validate_single_component_box(box: P78ParameterBox) -> Fraction:
    if box.lower[0] != box.upper[0]:
        raise ValueError("P90 requires the P75 prevalence coordinate to be fixed")
    prevalence = box.lower[0]
    if prevalence not in (Fraction(0), Fraction(1)):
        raise ValueError("P90 requires prevalence fixed to exactly zero or one")
    return prevalence


def _validate_parameters_in_box(
    parameters: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> tuple[Fraction, ...]:
    if len(parameters) != 9:
        raise ValueError("exactly nine P75 model parameters are required")
    for index, (value, lower, upper) in enumerate(
        zip(parameters, box.lower, box.upper, strict=True)
    ):
        if not isinstance(value, Fraction):
            raise TypeError("P90 parameters must be fractions.Fraction")
        if value < lower or value > upper:
            raise ValueError(f"parameter[{index}] lies outside the declared P75 box")
    return parameters


def p90_canonical_rank_one_slice_exact(
    law: tuple[Fraction, ...],
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return the canonical slice (1000, 1001, 1010, 1011)."""

    if len(law) != _OUTCOME_COUNT:
        raise ValueError("law must contain sixteen probabilities")
    return tuple(law[index] for index in _CANONICAL_SLICE_INDICES)  # type: ignore[return-value]


def rank_one_slice_determinant_exact(
    slice_entries: tuple[Fraction, Fraction, Fraction, Fraction],
) -> Fraction:
    """Return ad-bc for a 2 by 2 slice ordered as (a,b,c,d)."""

    a, b, c, d = slice_entries
    return a * d - b * c


def p90_rank_one_linf_lower_certificate_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P90RankOneLowerCertificate:
    """Certify a nonlinear L-infinity lower bound from the canonical slice.

    In a single-component P75 box every such slice has determinant zero. If
    ad>bc, any law within radius epsilon has

        q_a q_d >= (a-epsilon)(d-epsilon)
        q_b q_c <= (b+epsilon)(c+epsilon).

    The two products cannot meet while epsilon is below

        (ad-bc)/(a+b+c+d),

    provided that radius does not cross either positive factor on the side being
    decreased. The opposite orientation is handled symmetrically.
    """

    empirical_law = _validate_empirical_law(empirical_law)
    _validate_single_component_box(box)
    entries = p90_canonical_rank_one_slice_exact(empirical_law)
    a, b, c, d = entries
    determinant = rank_one_slice_determinant_exact(entries)
    mass = a + b + c + d
    if mass <= 0:
        raise ValueError("canonical P90 slice must have positive mass")
    if determinant == 0:
        return P90RankOneLowerCertificate(
            lower_bound=Fraction(0),
            slice_entries=entries,
            determinant_residual=Fraction(0),
            slice_mass=mass,
            orientation="exact-rank-one",
        )

    radius = abs(determinant) / mass
    if determinant > 0:
        if radius > min(a, d):
            raise ValueError("canonical slice leaves the unclipped P90 certificate regime")
        orientation = "ad>bc"
    else:
        if radius > min(b, c):
            raise ValueError("canonical slice leaves the unclipped P90 certificate regime")
        orientation = "bc>ad"

    return P90RankOneLowerCertificate(
        lower_bound=radius,
        slice_entries=entries,
        determinant_residual=determinant,
        slice_mass=mass,
        orientation=orientation,
    )


def verify_p90_rank_one_upper_certificate_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    parameters: tuple[Fraction, ...],
) -> P90RankOneUpperCertificate:
    """Verify one exact rational model point and its full-law L-infinity radius."""

    empirical_law = _validate_empirical_law(empirical_law)
    _validate_single_component_box(box)
    parameters = _validate_parameters_in_box(parameters, box)
    model_law = p75_four_view_law_exact(parameters)
    model_slice = p90_canonical_rank_one_slice_exact(model_law)
    determinant = rank_one_slice_determinant_exact(model_slice)
    if determinant != 0:
        raise RuntimeError("single-component P75 model slice is unexpectedly not rank one")
    radius = linf_distance_exact(empirical_law, model_law)
    return P90RankOneUpperCertificate(
        radius=radius,
        parameters=parameters,
        model_law=model_law,
        model_slice=model_slice,
        model_determinant=determinant,
    )


def certify_p90_exact_nonlinear_distance_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
    parameters: tuple[Fraction, ...],
) -> P90ExactNonlinearCertificate:
    """Return matching exact P90 lower and upper certificates."""

    lower = p90_rank_one_linf_lower_certificate_exact(empirical_law, box)
    upper = verify_p90_rank_one_upper_certificate_exact(
        empirical_law, box, parameters
    )
    if lower.lower_bound != upper.radius:
        raise ValueError(
            "P90 lower and upper certificates do not match: "
            f"{lower.lower_bound} != {upper.radius}"
        )
    return P90ExactNonlinearCertificate(
        optimum=lower.lower_bound,
        lower=lower,
        upper=upper,
    )
