"""Proposition 34: joint P11 operational-scale compatibility.

This module assembles the exact semantic conditions needed to combine the P30
node/state scale theorem with the P33 intervention-delay operational quotient.
It intentionally gives an approximate quantitative extension only for the
response-geometry branch, where total-variation representative ambiguity has a
direct two-sided pairwise geometry bound.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class JointP11OperationalScaleCertificate:
    """Certificate for exact full-P11 descent and approximate geometry control."""

    p30_conditions_hold: bool
    joint_response_descent_holds: bool
    directed_semantics_descend: bool
    partition_domain_descends: bool
    exact_full_p11_descent_certified: bool
    p30_uniform_budget: float
    joint_ambiguity: float
    geometry_full_upper_bound: float


def p30_uniform_budget(
    rho_geometry: float,
    rho_directed: float,
    rho_response: float,
    rho_partition_reference: float,
) -> float:
    """Return max{2 rho_G, 2 rho_A, rho_P + rho_Pi}."""
    _validate_nonnegative(
        rho_geometry,
        rho_directed,
        rho_response,
        rho_partition_reference,
    )
    return max(
        2.0 * rho_geometry,
        2.0 * rho_directed,
        rho_response + rho_partition_reference,
    )


def full_geometry_upper_bound(rho_geometry: float, joint_ambiguity: float) -> float:
    """Return the P34 geometry bound 2 rho_G + 2 eta_joint."""
    _validate_nonnegative(rho_geometry, joint_ambiguity)
    return 2.0 * rho_geometry + 2.0 * joint_ambiguity


def separate_audit_geometry_upper_bound(
    rho_geometry: float,
    intervention_ambiguity: float,
    delay_ambiguity: float,
) -> float:
    """Return 2 rho_G + 2(eta_b + eta_a) using the P33 additive bound."""
    _validate_nonnegative(rho_geometry, intervention_ambiguity, delay_ambiguity)
    return 2.0 * rho_geometry + 2.0 * (
        intervention_ambiguity + delay_ambiguity
    )


def joint_p11_operational_scale_certificate(
    *,
    rho_geometry: float,
    rho_directed: float,
    rho_response: float,
    rho_partition_reference: float,
    joint_ambiguity: float,
    p30_conditions_hold: bool,
    directed_semantics_descend: bool,
    partition_domain_descends: bool,
    tolerance: float = 1e-12,
) -> JointP11OperationalScaleCertificate:
    """Certify the exact P34 assembly conditions.

    Exact full-P11 descent requires:
    1. the P30 node/state compatibility conditions,
    2. exact product intervention-delay response descent,
    3. descended directed-influence semantics,
    4. descended partition-statistic domain semantics.

    A nonzero joint ambiguity does not invalidate the separate geometry bound, but
    it blocks the exact full-signature descent certificate.
    """
    _validate_nonnegative(
        rho_geometry,
        rho_directed,
        rho_response,
        rho_partition_reference,
        joint_ambiguity,
        tolerance,
    )
    joint_response_descent_holds = joint_ambiguity <= tolerance
    exact = (
        p30_conditions_hold
        and joint_response_descent_holds
        and directed_semantics_descend
        and partition_domain_descends
    )
    return JointP11OperationalScaleCertificate(
        p30_conditions_hold=p30_conditions_hold,
        joint_response_descent_holds=joint_response_descent_holds,
        directed_semantics_descend=directed_semantics_descend,
        partition_domain_descends=partition_domain_descends,
        exact_full_p11_descent_certified=exact,
        p30_uniform_budget=p30_uniform_budget(
            rho_geometry,
            rho_directed,
            rho_response,
            rho_partition_reference,
        ),
        joint_ambiguity=joint_ambiguity,
        geometry_full_upper_bound=full_geometry_upper_bound(
            rho_geometry, joint_ambiguity
        ),
    )


def exact_component_bounds(
    rho_geometry: float,
    rho_directed: float,
    rho_response: float,
    rho_partition_reference: float,
    *,
    exact_full_p11_descent_certified: bool,
) -> dict[str, float]:
    """Return inherited P30 component bounds only under exact P34 descent."""
    _validate_nonnegative(
        rho_geometry,
        rho_directed,
        rho_response,
        rho_partition_reference,
    )
    if not exact_full_p11_descent_certified:
        raise ValueError(
            "exact P11 component transport requires exact operational descent and semantic compatibility"
        )
    return {
        "geometry": 2.0 * rho_geometry,
        "directed_influence": 2.0 * rho_directed,
        "partition_irreducibility": rho_response + rho_partition_reference,
    }


def _validate_nonnegative(*values: float) -> None:
    if any(value < 0.0 for value in values):
        raise ValueError("all distortion, ambiguity, and tolerance values must be nonnegative")
