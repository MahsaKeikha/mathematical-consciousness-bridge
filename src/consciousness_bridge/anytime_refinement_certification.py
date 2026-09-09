"""Anytime-valid adaptive physical-refinement certification for Proposition 24.

P24 converts the fixed-sample P23 post-selection certificate into a time-uniform
certificate by allocating the total error probability across all positive sample
sizes.  At time n it uses

    alpha_n = 6 alpha / (pi^2 n^2),

so that sum_n alpha_n = alpha.  A union bound over the P22 base-law confidence
events then yields one event with probability at least 1-alpha on which every
sample size is valid simultaneously.  P23's deterministic-pushforward and
post-selection results can therefore be applied at every time and at any finite
data-dependent stopping time.

The construction is deliberately conservative.  It assumes one finite-alphabet
IID stream, fixed declared physical and target alphabets, and deterministic
candidate descriptor maps.  It is not an optimal confidence-sequence method and
it does not establish physical completeness or an experiential conclusion.
"""

from collections.abc import Hashable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from math import pi

from consciousness_bridge.adaptive_descriptor_selection import (
    AdaptiveDescriptorSelectionCertificate,
    certify_adaptive_descriptor_selection_from_records,
)
from consciousness_bridge.finite_sample_residual_certification import (
    hoeffding_joint_tv_radius,
)


@dataclass(frozen=True)
class AnytimeAdaptiveSelectionSnapshot:
    """One time-indexed P23 certificate inside the P24 confidence sequence."""

    time_index: int
    alpha_spending_level: float
    base_tv_radius: float
    selection: AdaptiveDescriptorSelectionCertificate


@dataclass(frozen=True)
class AnytimeAdaptiveSelectionPath:
    """Finite computed prefix of the infinite P24 time-uniform certificate."""

    snapshots: tuple[AnytimeAdaptiveSelectionSnapshot, ...]
    alpha: float
    time_uniform_coverage: float
    spending_mass_through_last_snapshot: float
    remaining_spending_mass: float


def _validate_time_index(time_index: int) -> None:
    if isinstance(time_index, bool) or not isinstance(time_index, int):
        raise ValueError("time_index must be a positive integer")
    if time_index < 1:
        raise ValueError("time_index must be a positive integer")


def _validate_alpha(alpha: float) -> None:
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between 0 and 1")


def alpha_spending_level(time_index: int, alpha: float = 0.05) -> float:
    """Return the P24 error allocation alpha_n = 6 alpha/(pi^2 n^2)."""
    _validate_time_index(time_index)
    _validate_alpha(alpha)
    return 6.0 * alpha / (pi * pi * time_index * time_index)


def alpha_spending_mass_through(
    time_index: int,
    alpha: float = 0.05,
) -> float:
    """Return the cumulative error budget spent through ``time_index``."""
    _validate_time_index(time_index)
    _validate_alpha(alpha)
    return sum(alpha_spending_level(index, alpha) for index in range(1, time_index + 1))


def anytime_base_tv_radius(
    sample_size: int,
    base_alphabet_size: int,
    alpha: float = 0.05,
) -> float:
    """Return the P24 time-indexed base-law total-variation radius."""
    _validate_time_index(sample_size)
    if (
        isinstance(base_alphabet_size, bool)
        or not isinstance(base_alphabet_size, int)
        or base_alphabet_size < 1
    ):
        raise ValueError("base_alphabet_size must be a positive integer")
    local_alpha = alpha_spending_level(sample_size, alpha)
    return hoeffding_joint_tv_radius(
        sample_size=sample_size,
        alphabet_size=base_alphabet_size,
        alpha=local_alpha,
    )


def certify_anytime_adaptive_selection_at_time(
    records: Iterable[tuple[Hashable, Hashable]],
    *,
    omega_states: Sequence[Hashable],
    coarse_descriptor: Mapping[Hashable, Hashable],
    coarse_size: int,
    candidate_descriptors: Mapping[str, Mapping[Hashable, Hashable]],
    candidate_sizes: Mapping[str, int],
    target_size: int,
    alpha: float = 0.05,
    tolerance: float = 1e-10,
) -> AnytimeAdaptiveSelectionSnapshot:
    """Return the P23 certificate at one time with P24 alpha spending.

    The number of records is the time index.  The returned P23 certificate uses
    ``alpha_n`` rather than the full ``alpha``.  Across all positive sample
    sizes, the P24 theorem allocates at most ``alpha`` total failure probability.
    """
    materialized = list(records)
    if not materialized:
        raise ValueError("records must contain at least one sample")
    time_index = len(materialized)
    local_alpha = alpha_spending_level(time_index, alpha)
    selection = certify_adaptive_descriptor_selection_from_records(
        materialized,
        omega_states=omega_states,
        coarse_descriptor=coarse_descriptor,
        coarse_size=coarse_size,
        candidate_descriptors=candidate_descriptors,
        candidate_sizes=candidate_sizes,
        target_size=target_size,
        alpha=local_alpha,
        tolerance=tolerance,
    )
    return AnytimeAdaptiveSelectionSnapshot(
        time_index=time_index,
        alpha_spending_level=local_alpha,
        base_tv_radius=selection.base_tv_radius,
        selection=selection,
    )


def certify_anytime_adaptive_selection_path(
    records: Iterable[tuple[Hashable, Hashable]],
    *,
    inspection_times: Sequence[int],
    omega_states: Sequence[Hashable],
    coarse_descriptor: Mapping[Hashable, Hashable],
    coarse_size: int,
    candidate_descriptors: Mapping[str, Mapping[Hashable, Hashable]],
    candidate_sizes: Mapping[str, int],
    target_size: int,
    alpha: float = 0.05,
    tolerance: float = 1e-10,
) -> AnytimeAdaptiveSelectionPath:
    """Compute selected P24 snapshots along one observed IID data stream.

    ``inspection_times`` only controls which snapshots are materialized.  The
    mathematical P24 guarantee allocates error over *all* positive integer sample
    sizes, not only the requested inspection times.
    """
    _validate_alpha(alpha)
    materialized = list(records)
    if not materialized:
        raise ValueError("records must contain at least one sample")
    if not inspection_times:
        raise ValueError("inspection_times must contain at least one time")

    times = tuple(inspection_times)
    for time_index in times:
        _validate_time_index(time_index)
    if tuple(sorted(set(times))) != times:
        raise ValueError("inspection_times must be strictly increasing and unique")
    if times[-1] > len(materialized):
        raise ValueError("inspection_times cannot exceed the number of records")

    snapshots = tuple(
        certify_anytime_adaptive_selection_at_time(
            materialized[:time_index],
            omega_states=omega_states,
            coarse_descriptor=coarse_descriptor,
            coarse_size=coarse_size,
            candidate_descriptors=candidate_descriptors,
            candidate_sizes=candidate_sizes,
            target_size=target_size,
            alpha=alpha,
            tolerance=tolerance,
        )
        for time_index in times
    )

    spent = alpha_spending_mass_through(times[-1], alpha)
    return AnytimeAdaptiveSelectionPath(
        snapshots=snapshots,
        alpha=alpha,
        time_uniform_coverage=1.0 - alpha,
        spending_mass_through_last_snapshot=spent,
        remaining_spending_mass=max(0.0, alpha - spent),
    )


def first_time_selected_gain_is_certified_positive(
    path: AnytimeAdaptiveSelectionPath,
) -> AnytimeAdaptiveSelectionSnapshot | None:
    """Return the first inspected time with a certified positive selected gain."""
    for snapshot in path.snapshots:
        if snapshot.selection.selected_gain_certified_positive:
            return snapshot
    return None
