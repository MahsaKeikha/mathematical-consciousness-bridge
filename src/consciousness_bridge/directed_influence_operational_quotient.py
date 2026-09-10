"""Proposition 35: approximate directed-influence stability.

The bound is valid only after matched intervention-pair semantics have descended.
Numerically, changing either endpoint response law within a joint operational
quotient fiber by at most eta_joint changes their TV distance by at most 2 eta_joint.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DirectedInfluenceOperationalCertificate:
    source_semantics_descend: bool
    node_state_bound: float
    operational_ambiguity_bound: float
    full_upper_bound: float
    threshold_margin: float | None
    threshold_classification_certified: bool | None


def directed_influence_representative_bound(joint_ambiguity: float) -> float:
    """Return 2 eta_joint."""
    _validate_nonnegative(joint_ambiguity)
    return 2.0 * joint_ambiguity


def full_directed_influence_upper_bound(
    rho_directed: float, joint_ambiguity: float
) -> float:
    """Return 2 rho_A + 2 eta_joint."""
    _validate_nonnegative(rho_directed, joint_ambiguity)
    return 2.0 * rho_directed + 2.0 * joint_ambiguity


def separate_audit_directed_influence_upper_bound(
    rho_directed: float,
    intervention_ambiguity: float,
    delay_ambiguity: float,
) -> float:
    """Return 2 rho_A + 2(eta_b + eta_a)."""
    _validate_nonnegative(
        rho_directed, intervention_ambiguity, delay_ambiguity
    )
    return 2.0 * rho_directed + 2.0 * (
        intervention_ambiguity + delay_ambiguity
    )


def threshold_margin_certified(
    influence_value: float,
    threshold: float,
    full_upper_bound: float,
) -> bool:
    """Certify threshold classification when |A-theta| exceeds the distortion bound."""
    _validate_nonnegative(influence_value, threshold, full_upper_bound)
    return abs(influence_value - threshold) > full_upper_bound


def directed_influence_operational_certificate(
    *,
    rho_directed: float,
    joint_ambiguity: float,
    source_semantics_descend: bool,
    influence_value: float | None = None,
    threshold: float | None = None,
) -> DirectedInfluenceOperationalCertificate:
    """Assemble the P35 numerical and semantic certificate."""
    _validate_nonnegative(rho_directed, joint_ambiguity)
    node_bound = 2.0 * rho_directed
    op_bound = 2.0 * joint_ambiguity
    full = node_bound + op_bound

    if (influence_value is None) != (threshold is None):
        raise ValueError("influence_value and threshold must be supplied together")

    margin = None
    certified = None
    if influence_value is not None and threshold is not None:
        _validate_nonnegative(influence_value, threshold)
        margin = abs(influence_value - threshold)
        certified = source_semantics_descend and margin > full

    return DirectedInfluenceOperationalCertificate(
        source_semantics_descend=source_semantics_descend,
        node_state_bound=node_bound,
        operational_ambiguity_bound=op_bound,
        full_upper_bound=full,
        threshold_margin=margin,
        threshold_classification_certified=certified,
    )


def _validate_nonnegative(*values: float) -> None:
    if any(value < 0.0 for value in values):
        raise ValueError("all values must be nonnegative")
