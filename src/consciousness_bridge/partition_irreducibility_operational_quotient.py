"""Proposition 36: partition irreducibility under operational quotient ambiguity."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PartitionOperationalCertificate:
    partition_semantics_descend: bool
    block_count: int
    node_state_bound: float
    operational_ambiguity_bound: float
    full_upper_bound: float


def product_reference_perturbation_bound(block_count: int, eta: float) -> float:
    """Return m * eta for an m-block product reference."""
    _validate(block_count, eta)
    return block_count * eta


def fixed_partition_irreducibility_bound(block_count: int, eta: float) -> float:
    """Return (m+1) * eta for kappa_pi(P)=TV(P, product marginals)."""
    _validate(block_count, eta)
    return (block_count + 1) * eta


def full_partition_irreducibility_upper_bound(
    *,
    rho_response: float,
    rho_partition_reference: float,
    max_block_count: int,
    joint_ambiguity: float,
) -> float:
    """Return rho_P + rho_Pi + (m_max+1) eta_joint."""
    _validate(max_block_count, rho_response, rho_partition_reference, joint_ambiguity)
    return (
        rho_response
        + rho_partition_reference
        + (max_block_count + 1) * joint_ambiguity
    )


def separate_audit_partition_upper_bound(
    *,
    rho_response: float,
    rho_partition_reference: float,
    max_block_count: int,
    intervention_ambiguity: float,
    delay_ambiguity: float,
) -> float:
    """Use eta_joint <= eta_b + eta_a from P33."""
    _validate(
        max_block_count,
        rho_response,
        rho_partition_reference,
        intervention_ambiguity,
        delay_ambiguity,
    )
    return (
        rho_response
        + rho_partition_reference
        + (max_block_count + 1) * (intervention_ambiguity + delay_ambiguity)
    )


def partition_operational_certificate(
    *,
    rho_response: float,
    rho_partition_reference: float,
    block_count: int,
    joint_ambiguity: float,
    partition_semantics_descend: bool,
) -> PartitionOperationalCertificate:
    """Assemble the P36 semantic and numerical certificate."""
    _validate(block_count, rho_response, rho_partition_reference, joint_ambiguity)
    node_bound = rho_response + rho_partition_reference
    op_bound = (block_count + 1) * joint_ambiguity
    return PartitionOperationalCertificate(
        partition_semantics_descend=partition_semantics_descend,
        block_count=block_count,
        node_state_bound=node_bound,
        operational_ambiguity_bound=op_bound,
        full_upper_bound=node_bound + op_bound,
    )


def _validate(block_count: int, *values: float) -> None:
    if block_count < 1:
        raise ValueError("block_count must be at least 1")
    if any(value < 0.0 for value in values):
        raise ValueError("all distortion and ambiguity values must be nonnegative")
