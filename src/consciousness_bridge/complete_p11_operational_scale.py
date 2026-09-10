"""Proposition 37: complete approximate P11 operational-scale theorem."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompleteP11ScaleCertificate:
    semantic_validity: bool
    geometry_bound: float
    directed_influence_bound: float
    partition_bound: float
    uniform_bound: float
    delta_stable: bool | None


def complete_component_bounds(
    *,
    rho_geometry: float,
    rho_directed: float,
    rho_response: float,
    rho_partition_reference: float,
    max_block_count: int,
    joint_ambiguity: float,
) -> tuple[float, float, float]:
    """Return the P37 geometry, directed, and partition bounds."""
    _validate(max_block_count, rho_geometry, rho_directed, rho_response, rho_partition_reference, joint_ambiguity)
    geometry = 2.0 * rho_geometry + 2.0 * joint_ambiguity
    directed = 2.0 * rho_directed + 2.0 * joint_ambiguity
    partition = (
        rho_response
        + rho_partition_reference
        + (max_block_count + 1) * joint_ambiguity
    )
    return geometry, directed, partition


def complete_uniform_bound(
    *,
    rho_geometry: float,
    rho_directed: float,
    rho_response: float,
    rho_partition_reference: float,
    max_block_count: int,
    joint_ambiguity: float,
) -> float:
    """Return max epsilon across all three P11 components."""
    return max(
        complete_component_bounds(
            rho_geometry=rho_geometry,
            rho_directed=rho_directed,
            rho_response=rho_response,
            rho_partition_reference=rho_partition_reference,
            max_block_count=max_block_count,
            joint_ambiguity=joint_ambiguity,
        )
    )


def separate_audit_uniform_bound(
    *,
    rho_geometry: float,
    rho_directed: float,
    rho_response: float,
    rho_partition_reference: float,
    max_block_count: int,
    intervention_ambiguity: float,
    delay_ambiguity: float,
) -> float:
    """Use eta_joint <= eta_b + eta_a to give a sufficient P37 bound."""
    _validate(
        max_block_count,
        rho_geometry,
        rho_directed,
        rho_response,
        rho_partition_reference,
        intervention_ambiguity,
        delay_ambiguity,
    )
    eta = intervention_ambiguity + delay_ambiguity
    return complete_uniform_bound(
        rho_geometry=rho_geometry,
        rho_directed=rho_directed,
        rho_response=rho_response,
        rho_partition_reference=rho_partition_reference,
        max_block_count=max_block_count,
        joint_ambiguity=eta,
    )


def complete_p11_scale_certificate(
    *,
    rho_geometry: float,
    rho_directed: float,
    rho_response: float,
    rho_partition_reference: float,
    max_block_count: int,
    joint_ambiguity: float,
    semantic_validity: bool,
    tolerance_delta: float | None = None,
) -> CompleteP11ScaleCertificate:
    """Assemble semantic validity and the quantitative P37 scale certificate."""
    geometry, directed, partition = complete_component_bounds(
        rho_geometry=rho_geometry,
        rho_directed=rho_directed,
        rho_response=rho_response,
        rho_partition_reference=rho_partition_reference,
        max_block_count=max_block_count,
        joint_ambiguity=joint_ambiguity,
    )
    uniform = max(geometry, directed, partition)

    delta_stable = None
    if tolerance_delta is not None:
        if tolerance_delta < 0.0:
            raise ValueError("tolerance_delta must be nonnegative")
        delta_stable = semantic_validity and uniform < tolerance_delta

    return CompleteP11ScaleCertificate(
        semantic_validity=semantic_validity,
        geometry_bound=geometry,
        directed_influence_bound=directed,
        partition_bound=partition,
        uniform_bound=uniform,
        delta_stable=delta_stable,
    )


def _validate(block_count: int, *values: float) -> None:
    if block_count < 1:
        raise ValueError("max_block_count must be at least 1")
    if any(value < 0.0 for value in values):
        raise ValueError("all reconstruction and ambiguity values must be nonnegative")
