"""Descriptor-refinement and residual-persistence tools for Proposition 21.

The results in this module formalize an omitted-physics control.  A residual
relative to one declared physical descriptor is not treated as an ontological
conclusion.  Instead, the descriptor is refined and the remaining residual is
tracked exactly.

For nested deterministic descriptors ``T_coarse = c(T_fine)`` with ``T_fine``
a function of the sampled physical state ``Omega``, the chain rule gives

    I(E; Omega | T_coarse)
      = I(E; T_fine | T_coarse) + I(E; Omega | T_fine).

Hence refinement cannot increase the residual, and the decrease is exactly the
target-relevant information captured by the added physical detail.
"""

from collections.abc import Hashable, Iterable, Sequence
from dataclasses import dataclass

from consciousness_bridge.fundamental_physical_sufficiency import (
    conditional_mutual_information,
    empirical_joint_from_records,
)


@dataclass(frozen=True)
class RefinementResidualCertificate:
    """Exact pairwise residual decomposition for one descriptor refinement."""

    coarse_residual: float
    fine_residual: float
    captured_by_refinement: float
    decomposition_error: float
    residual_persists: bool


@dataclass(frozen=True)
class RefinementChainCertificate:
    """Residual trajectory and information increments along a nested chain."""

    residuals: tuple[float, ...]
    captured_increments: tuple[float, ...]
    telescoping_error: float
    monotone: bool
    terminal_residual: float


def descriptor_refinement_violations(
    coarse_labels: Sequence[Hashable], fine_labels: Sequence[Hashable]
) -> list[tuple[int, int]]:
    """Return witnesses that ``coarse`` is not a function of ``fine``.

    A valid refinement requires equal fine labels to imply equal coarse labels.
    Each returned pair contains two sample indices with the same fine label and
    different coarse labels.
    """
    if len(coarse_labels) != len(fine_labels):
        raise ValueError("coarse_labels and fine_labels must have equal length")

    first_seen: dict[Hashable, tuple[int, Hashable]] = {}
    violations: list[tuple[int, int]] = []
    for index, (coarse, fine) in enumerate(zip(coarse_labels, fine_labels)):
        previous = first_seen.get(fine)
        if previous is None:
            first_seen[fine] = (index, coarse)
            continue
        previous_index, previous_coarse = previous
        if coarse != previous_coarse:
            violations.append((previous_index, index))
    return violations


def is_descriptor_refinement(
    coarse_labels: Sequence[Hashable], fine_labels: Sequence[Hashable]
) -> bool:
    """Whether ``fine`` refines ``coarse`` on the observed domain."""
    return not descriptor_refinement_violations(coarse_labels, fine_labels)


def unresolved_target_collision_pairs(
    physical_labels: Sequence[Hashable], target_labels: Sequence[Hashable]
) -> set[tuple[int, int]]:
    """Return all observed equal-physical / unequal-target collision pairs."""
    if len(physical_labels) != len(target_labels):
        raise ValueError("physical_labels and target_labels must have equal length")

    collisions: set[tuple[int, int]] = set()
    for left in range(len(physical_labels)):
        for right in range(left + 1, len(physical_labels)):
            if (
                physical_labels[left] == physical_labels[right]
                and target_labels[left] != target_labels[right]
            ):
                collisions.add((left, right))
    return collisions


def refinement_collision_sets(
    coarse_labels: Sequence[Hashable],
    fine_labels: Sequence[Hashable],
    target_labels: Sequence[Hashable],
) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
    """Return coarse and fine collision sets after validating refinement.

    For a valid refinement, every fine collision is also a coarse collision.
    The function asserts that theorem invariant before returning the two sets.
    """
    if len(coarse_labels) != len(target_labels):
        raise ValueError("all label sequences must have equal length")
    if len(fine_labels) != len(target_labels):
        raise ValueError("all label sequences must have equal length")
    if not is_descriptor_refinement(coarse_labels, fine_labels):
        raise ValueError("fine_labels do not refine coarse_labels")

    coarse_collisions = unresolved_target_collision_pairs(coarse_labels, target_labels)
    fine_collisions = unresolved_target_collision_pairs(fine_labels, target_labels)
    if not fine_collisions.issubset(coarse_collisions):
        raise AssertionError("refinement collision monotonicity was violated")
    return coarse_collisions, fine_collisions


def _validate_descriptor_is_function_of_state(
    omega_labels: Sequence[Hashable],
    descriptor_labels: Sequence[Hashable],
    name: str,
) -> None:
    if len(omega_labels) != len(descriptor_labels):
        raise ValueError("omega and descriptor labels must have equal length")
    violations = descriptor_refinement_violations(descriptor_labels, omega_labels)
    if violations:
        raise ValueError(f"{name} must be a deterministic function of omega")


def refinement_residual_decomposition(
    records: Iterable[tuple[Hashable, Hashable, Hashable, Hashable]],
    *,
    tolerance: float = 1e-12,
) -> RefinementResidualCertificate:
    """Compute the exact P21 decomposition from finite weighted-by-count records.

    Each record is ``(omega, coarse, fine, target)``.  ``fine`` must be a
    deterministic function of ``omega`` and ``coarse`` must be a deterministic
    function of ``fine`` on the observed support.
    """
    if tolerance < 0:
        raise ValueError("tolerance must be non-negative")

    materialized = list(records)
    if not materialized:
        raise ValueError("records must contain at least one sample")
    if any(len(record) != 4 for record in materialized):
        raise ValueError("each record must contain omega, coarse, fine, target")

    omega_labels = [record[0] for record in materialized]
    coarse_labels = [record[1] for record in materialized]
    fine_labels = [record[2] for record in materialized]
    target_labels = [record[3] for record in materialized]

    _validate_descriptor_is_function_of_state(omega_labels, fine_labels, "fine")
    if not is_descriptor_refinement(coarse_labels, fine_labels):
        raise ValueError("coarse must be a deterministic function of fine")

    coarse_joint = empirical_joint_from_records(
        (omega, coarse, target)
        for omega, coarse, _fine, target in materialized
    )
    fine_joint = empirical_joint_from_records(
        (omega, fine, target)
        for omega, _coarse, fine, target in materialized
    )
    increment_joint = empirical_joint_from_records(
        (fine, coarse, target)
        for _omega, coarse, fine, target in materialized
    )

    coarse_residual = conditional_mutual_information(coarse_joint)
    fine_residual = conditional_mutual_information(fine_joint)
    captured = conditional_mutual_information(increment_joint)
    decomposition_error = abs(coarse_residual - fine_residual - captured)

    if fine_residual > coarse_residual + tolerance:
        raise AssertionError("descriptor refinement increased the residual")
    if decomposition_error > max(tolerance, 1e-10):
        raise AssertionError("conditional-information chain rule did not close")

    return RefinementResidualCertificate(
        coarse_residual=coarse_residual,
        fine_residual=fine_residual,
        captured_by_refinement=captured,
        decomposition_error=decomposition_error,
        residual_persists=fine_residual > tolerance,
    )


def refinement_chain_residuals(
    records: Iterable[tuple[Hashable, Sequence[Hashable], Hashable]],
    *,
    tolerance: float = 1e-12,
) -> RefinementChainCertificate:
    """Compute the residual trajectory for a nested descriptor chain.

    Each record is ``(omega, descriptors, target)`` where ``descriptors`` is
    ordered from coarsest to finest.  Every level must be a deterministic
    function of ``omega`` and every level must refine the preceding one.
    """
    if tolerance < 0:
        raise ValueError("tolerance must be non-negative")

    materialized = list(records)
    if not materialized:
        raise ValueError("records must contain at least one sample")
    if any(len(record) != 3 for record in materialized):
        raise ValueError("each record must contain omega, descriptors, target")

    level_count = len(materialized[0][1])
    if level_count < 1:
        raise ValueError("descriptor chains must contain at least one level")
    if any(len(record[1]) != level_count for record in materialized):
        raise ValueError("all descriptor chains must have the same length")

    omega_labels = [record[0] for record in materialized]
    target_labels = [record[2] for record in materialized]
    levels = [
        [record[1][level] for record in materialized]
        for level in range(level_count)
    ]

    for level, labels in enumerate(levels):
        _validate_descriptor_is_function_of_state(
            omega_labels, labels, f"descriptor level {level}"
        )
    for level in range(1, level_count):
        if not is_descriptor_refinement(levels[level - 1], levels[level]):
            raise ValueError(
                f"descriptor level {level} does not refine level {level - 1}"
            )

    residuals = tuple(
        conditional_mutual_information(
            empirical_joint_from_records(
                (omega, descriptor, target)
                for omega, descriptor, target in zip(
                    omega_labels, labels, target_labels
                )
            )
        )
        for labels in levels
    )

    increments = tuple(
        conditional_mutual_information(
            empirical_joint_from_records(
                (fine, coarse, target)
                for fine, coarse, target in zip(
                    levels[level], levels[level - 1], target_labels
                )
            )
        )
        for level in range(1, level_count)
    )

    telescoping_error = abs(residuals[0] - residuals[-1] - sum(increments))
    monotone = all(
        later <= earlier + tolerance
        for earlier, later in zip(residuals, residuals[1:])
    )
    if not monotone:
        raise AssertionError("nested refinement increased the residual")
    if telescoping_error > max(tolerance, 1e-10):
        raise AssertionError("nested conditional-information decomposition did not close")

    return RefinementChainCertificate(
        residuals=residuals,
        captured_increments=increments,
        telescoping_error=telescoping_error,
        monotone=monotone,
        terminal_residual=residuals[-1],
    )
