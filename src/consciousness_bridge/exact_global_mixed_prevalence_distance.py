"""P92 exact global mixed-prevalence distance for the full P75 model cube.

P91 proves a strict global lower exclusion radius of 1/42 and gives an explicit
mixed P75 law at full-law L-infinity distance 1/24. P92 closes that gap.

Condition on the observable event X1 = 1 and write A = X2, B = X3, C = X4.
Every P75 law restricts to a nonnegative two-component product mixture on the
resulting 2 by 2 by 2 subtensor. Three selected conditional 2 by 2 minors then
have determinant product greater than or equal to zero. The sign coherence is
an exact nonlinear consequence of the common two-component product mixture.

For the established empirical witness, the three determinants are

    D_AB_given_C1 = -1/48,
    D_AC_given_B0 =  1/64,
    D_BC_given_A0 =  5/192.

Their exact entrywise sign-stability radii are, respectively,

    1/24, 3/56, 5/72.

Therefore every nonnegative law within full-law L-infinity distance strictly
less than 1/24 keeps determinant signs (-,+,+), whose product is negative. No
P75 law can do this. Hence the full P75 distance is at least 1/24. The explicit
mixed P91 parameter point attains exactly 1/24, so

    d_inf(P_emp, M_75) = 1/24.

This is a conditional model-separation theorem for the declared P75 family.
It does not identify the latent state with consciousness, establish
nonphysicality, validate an alternative ontology, or solve the
physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.certified_continuous_model_separation import (
    linf_distance_exact,
    p75_four_view_law_exact,
)

_OUTCOME_COUNT = 16
_PARAMETER_COUNT = 9


@dataclass(frozen=True)
class P92SignCoherenceCertificate:
    """Exact empirical three-minor sign certificate."""

    determinants: tuple[Fraction, Fraction, Fraction]
    sign_stability_radii: tuple[Fraction, Fraction, Fraction]
    certified_radius: Fraction
    determinant_product: Fraction


@dataclass(frozen=True)
class P92ModelSignFactorization:
    """Exact P75 determinant factorization for the three selected minors."""

    actual_determinants: tuple[Fraction, Fraction, Fraction]
    factorized_determinants: tuple[Fraction, Fraction, Fraction]
    determinant_product: Fraction
    sign_coherent: bool


@dataclass(frozen=True)
class P92ExactGlobalDistanceCertificate:
    """Matching exact lower and upper certificates for the full P75 cube."""

    exact_distance: Fraction
    lower: P92SignCoherenceCertificate
    upper_parameters: tuple[Fraction, ...]
    upper_model_law: tuple[Fraction, ...]
    upper_distance: Fraction
    upper_prevalence: Fraction
    conclusion: str


def _validate_law(law: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if len(law) != _OUTCOME_COUNT:
        raise ValueError("law must contain sixteen probabilities")
    if any(not isinstance(value, Fraction) for value in law):
        raise TypeError("law entries must be fractions.Fraction")
    if any(value < 0 or value > 1 for value in law):
        raise ValueError("law entries must lie in [0, 1]")
    if sum(law, start=Fraction(0)) != 1:
        raise ValueError("law must have total mass one")
    return law


def _validate_parameters(parameters: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if len(parameters) != _PARAMETER_COUNT:
        raise ValueError("exactly nine P75 parameters are required")
    if any(not isinstance(value, Fraction) for value in parameters):
        raise TypeError("P75 parameters must be fractions.Fraction")
    if any(value < 0 or value > 1 for value in parameters):
        raise ValueError("P75 parameters must lie in [0, 1]")
    return parameters


def determinant_2_by_2_exact(
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> Fraction:
    """Return the exact determinant of a 2 by 2 rational matrix."""

    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError("matrix must be 2 by 2")
    a, b = matrix[0]
    c, d = matrix[1]
    return a * d - b * c


def p92_x1_one_subtensor_exact(
    law: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    """Return the eight X1 = 1 cells in X2,X3,X4 lexicographic order."""

    law = _validate_law(law)
    return law[8:16]


def p92_selected_minor_matrices_exact(
    law: tuple[Fraction, ...],
) -> tuple[
    tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
    tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
    tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
]:
    """Return the three P92 2 by 2 minors.

    The returned order is AB given C=1, AC given B=0, BC given A=0 after
    setting A=X2, B=X3, C=X4 inside the X1=1 subtensor.
    """

    t000, t001, t010, t011, t100, t101, t110, t111 = (
        p92_x1_one_subtensor_exact(law)
    )
    del t110
    return (
        ((t001, t011), (t101, t111)),
        ((t000, t001), (t100, t101)),
        ((t000, t001), (t010, t011)),
    )


def p92_selected_determinants_exact(
    law: tuple[Fraction, ...],
) -> tuple[Fraction, Fraction, Fraction]:
    """Return the three exact P92 determinant values."""

    return tuple(
        determinant_2_by_2_exact(matrix)
        for matrix in p92_selected_minor_matrices_exact(law)
    )


def determinant_sign_stability_radius_exact(
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> Fraction:
    """Return the exact unclipped entrywise radius that preserves determinant sign.

    For matrix ``[[a,b],[c,d]]`` with nonzero determinant, any nonnegative
    entrywise perturbation smaller than ``abs(ad-bc)/(a+b+c+d)`` preserves the
    determinant sign, provided the product supporting the empirical sign stays
    away from the zero clipping boundary. This routine verifies that condition
    exactly for the supplied matrix.
    """

    determinant = determinant_2_by_2_exact(matrix)
    if determinant == 0:
        raise ValueError("matrix determinant must be nonzero")
    total = sum((value for row in matrix for value in row), start=Fraction(0))
    if total <= 0:
        raise ValueError("matrix must have positive total mass")
    radius = abs(determinant) / total
    a, b = matrix[0]
    c, d = matrix[1]
    supporting_factors = (a, d) if determinant > 0 else (b, c)
    if any(value < radius for value in supporting_factors):
        raise ValueError("unclipped determinant sign certificate is not valid")
    return radius


def certify_p92_empirical_sign_coherence_obstruction_exact(
    empirical_law: tuple[Fraction, ...],
) -> P92SignCoherenceCertificate:
    """Return the exact empirical sign obstruction and its certified radius."""

    matrices = p92_selected_minor_matrices_exact(empirical_law)
    determinants = tuple(determinant_2_by_2_exact(matrix) for matrix in matrices)
    radii = tuple(determinant_sign_stability_radius_exact(matrix) for matrix in matrices)
    product = determinants[0] * determinants[1] * determinants[2]
    if product >= 0:
        raise ValueError("empirical selected minors do not violate P75 sign coherence")
    return P92SignCoherenceCertificate(
        determinants=determinants,
        sign_stability_radii=radii,
        certified_radius=min(radii),
        determinant_product=product,
    )


def p92_model_sign_factorization_exact(
    parameters: tuple[Fraction, ...],
) -> P92ModelSignFactorization:
    """Verify the universal P75 three-minor factorization exactly."""

    parameters = _validate_parameters(parameters)
    prevalence = parameters[0]
    q1_minus, q1_plus = parameters[1], parameters[2]
    a_minus, a_plus = parameters[3], parameters[4]
    b_minus, b_plus = parameters[5], parameters[6]
    c_minus, c_plus = parameters[7], parameters[8]

    lambda_minus = (1 - prevalence) * q1_minus
    lambda_plus = prevalence * q1_plus
    common = lambda_minus * lambda_plus
    delta_a = a_plus - a_minus
    delta_b = b_plus - b_minus
    delta_c = c_plus - c_minus

    factorized = (
        common * c_minus * c_plus * delta_a * delta_b,
        common * (1 - b_minus) * (1 - b_plus) * delta_a * delta_c,
        common * (1 - a_minus) * (1 - a_plus) * delta_b * delta_c,
    )
    model_law = p75_four_view_law_exact(parameters)
    actual = p92_selected_determinants_exact(model_law)
    if actual != factorized:
        raise RuntimeError("P75 selected-minor factorization failed")
    product = actual[0] * actual[1] * actual[2]
    return P92ModelSignFactorization(
        actual_determinants=actual,
        factorized_determinants=factorized,
        determinant_product=product,
        sign_coherent=product >= 0,
    )


def certify_p92_exact_global_distance(
    empirical_law: tuple[Fraction, ...],
    upper_parameters: tuple[Fraction, ...],
) -> P92ExactGlobalDistanceCertificate:
    """Certify the exact full-cube P75 L-infinity distance."""

    empirical_law = _validate_law(empirical_law)
    upper_parameters = _validate_parameters(upper_parameters)
    lower = certify_p92_empirical_sign_coherence_obstruction_exact(empirical_law)
    upper_model_law = p75_four_view_law_exact(upper_parameters)
    upper_distance = linf_distance_exact(empirical_law, upper_model_law)
    upper_factorization = p92_model_sign_factorization_exact(upper_parameters)
    if not upper_factorization.sign_coherent:
        raise RuntimeError("explicit P75 upper certificate violates sign coherence")
    if upper_distance != lower.certified_radius:
        raise ValueError("upper certificate does not close the P92 lower radius")
    prevalence = upper_parameters[0]
    if prevalence <= 0 or prevalence >= 1:
        raise ValueError("P92 upper certificate must have genuinely mixed prevalence")
    return P92ExactGlobalDistanceCertificate(
        exact_distance=upper_distance,
        lower=lower,
        upper_parameters=upper_parameters,
        upper_model_law=upper_model_law,
        upper_distance=upper_distance,
        upper_prevalence=prevalence,
        conclusion="exact global full-cube P75 L-infinity distance certified",
    )
