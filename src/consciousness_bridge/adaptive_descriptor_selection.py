"""Adaptive physical-descriptor selection for Proposition 23.

Proposition 23 extends the shared-base-law confidence construction of P22 to
post-selection inference.  A single confidence ball for the finite joint law
``(Omega, E)`` is pushed through every declared deterministic descriptor map.
Because total variation contracts under deterministic pushforward, the same
base event controls every candidate even when the final descriptor is selected
from the observed data.

The result is intentionally finite-alphabet and fixed-sample.  It does not
justify optional stopping across sample sizes, descriptors that are not genuine
functions of the declared physical state, or any claim of physical completeness.
"""

from collections.abc import Hashable, Iterable, Mapping, Sequence
from dataclasses import dataclass

from consciousness_bridge.descriptor_refinement_residual import (
    is_descriptor_refinement,
)
from consciousness_bridge.finite_sample_residual_certification import (
    conditional_information_continuity_bound,
    hoeffding_joint_tv_radius,
    maximum_conditional_mutual_information,
)
from consciousness_bridge.fundamental_physical_sufficiency import (
    conditional_mutual_information,
    empirical_joint_from_records,
)


@dataclass(frozen=True)
class AdaptiveCandidateCertificate:
    """Simultaneous residual and gain certificate for one candidate refinement."""

    name: str
    gain_estimate: float
    gain_lower: float
    gain_upper: float
    gain_continuity_radius: float
    residual_estimate: float
    residual_lower: float
    residual_upper: float
    residual_continuity_radius: float
    empirical_chain_rule_error: float
    certified_positive_gain: bool


@dataclass(frozen=True)
class AdaptiveDescriptorSelectionCertificate:
    """Post-selection certificate for the empirically best declared refinement."""

    candidates: tuple[AdaptiveCandidateCertificate, ...]
    selected_name: str
    selected_index: int
    coarse_residual_estimate: float
    coarse_residual_lower: float
    coarse_residual_upper: float
    base_tv_radius: float
    alpha: float
    simultaneous_coverage: float
    sample_size: int
    candidate_count: int
    candidate_count_penalty_applied: bool
    maximum_gain_radius: float
    generic_selection_regret_bound: float
    data_dependent_selection_regret_bound: float
    selected_residual_excess_bound: float
    selected_gain_certified_positive: bool


def _validate_positive_integer(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")


def _bounded_interval(
    estimate: float,
    radius: float,
    maximum: float,
) -> tuple[float, float]:
    estimate = min(maximum, max(0.0, estimate))
    return max(0.0, estimate - radius), min(maximum, estimate + radius)


def _validate_descriptor_map(
    descriptor: Mapping[Hashable, Hashable],
    omega_states: Sequence[Hashable],
    declared_size: int,
    name: str,
) -> None:
    _validate_positive_integer(declared_size, f"{name}_size")
    omega_set = set(omega_states)
    if set(descriptor) != omega_set:
        raise ValueError(f"{name} must be defined on every declared omega state")
    if len(set(descriptor.values())) > declared_size:
        raise ValueError(f"{name} uses more labels than its declared alphabet size")


def _empirical_residual(
    records: Sequence[tuple[Hashable, Hashable]],
    descriptor: Mapping[Hashable, Hashable],
) -> float:
    joint = empirical_joint_from_records(
        (omega, descriptor[omega], target) for omega, target in records
    )
    return conditional_mutual_information(joint)


def _empirical_gain(
    records: Sequence[tuple[Hashable, Hashable]],
    coarse: Mapping[Hashable, Hashable],
    fine: Mapping[Hashable, Hashable],
) -> float:
    joint = empirical_joint_from_records(
        (fine[omega], coarse[omega], target) for omega, target in records
    )
    return conditional_mutual_information(joint)


def certify_adaptive_descriptor_selection_from_records(
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
) -> AdaptiveDescriptorSelectionCertificate:
    """Certify post-selection validity for an adaptive refinement choice.

    ``records`` are ``(omega, target)`` samples from one finite IID base law.
    ``candidate_descriptors`` may be searched and compared using these same
    records.  Every candidate must nevertheless be a declared deterministic
    map on the full ``omega_states`` alphabet and must refine the common coarse
    descriptor.

    The selected candidate maximizes empirical P21 refinement gain.  One P22
    base-TV event controls every candidate simultaneously, so the returned
    intervals remain valid for the selected candidate without a separate
    candidate-count union-bound penalty.
    """
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between 0 and 1")
    if tolerance < 0.0:
        raise ValueError("tolerance must be non-negative")
    _validate_positive_integer(target_size, "target_size")

    omega_tuple = tuple(omega_states)
    if not omega_tuple:
        raise ValueError("omega_states must contain at least one state")
    if len(set(omega_tuple)) != len(omega_tuple):
        raise ValueError("omega_states must not contain duplicates")

    materialized = list(records)
    if not materialized:
        raise ValueError("records must contain at least one sample")
    if any(len(record) != 2 for record in materialized):
        raise ValueError("each record must contain omega and target")

    omega_set = set(omega_tuple)
    if any(omega not in omega_set for omega, _ in materialized):
        raise ValueError("records contain omega labels outside omega_states")
    if len({target for _, target in materialized}) > target_size:
        raise ValueError("observed target labels exceed target_size")

    _validate_descriptor_map(
        coarse_descriptor,
        omega_tuple,
        coarse_size,
        "coarse_descriptor",
    )

    if not candidate_descriptors:
        raise ValueError("candidate_descriptors must contain at least one candidate")
    if set(candidate_descriptors) != set(candidate_sizes):
        raise ValueError("candidate_sizes must have exactly the candidate names")

    candidate_names = sorted(candidate_descriptors)
    for name in candidate_names:
        if not name:
            raise ValueError("candidate names must be non-empty strings")
        fine = candidate_descriptors[name]
        _validate_descriptor_map(
            fine,
            omega_tuple,
            candidate_sizes[name],
            f"candidate_descriptors[{name!r}]",
        )
        coarse_values = [coarse_descriptor[omega] for omega in omega_tuple]
        fine_values = [fine[omega] for omega in omega_tuple]
        if not is_descriptor_refinement(coarse_values, fine_values):
            raise ValueError(f"candidate {name!r} does not refine the coarse descriptor")

    omega_size = len(omega_tuple)
    sample_size = len(materialized)
    base_tv_radius = hoeffding_joint_tv_radius(
        sample_size=sample_size,
        alphabet_size=omega_size * target_size,
        alpha=alpha,
    )

    coarse_residual_estimate = _empirical_residual(
        materialized,
        coarse_descriptor,
    )
    coarse_residual_radius = conditional_information_continuity_bound(
        base_tv_radius,
        omega_size=omega_size,
        physical_size=coarse_size,
        target_size=target_size,
    )
    coarse_residual_maximum = maximum_conditional_mutual_information(
        omega_size=omega_size,
        target_size=target_size,
    )
    coarse_residual_lower, coarse_residual_upper = _bounded_interval(
        coarse_residual_estimate,
        coarse_residual_radius,
        coarse_residual_maximum,
    )

    candidate_certificates: list[AdaptiveCandidateCertificate] = []
    for name in candidate_names:
        fine = candidate_descriptors[name]
        fine_size = candidate_sizes[name]

        gain_estimate = _empirical_gain(
            materialized,
            coarse_descriptor,
            fine,
        )
        gain_radius = conditional_information_continuity_bound(
            base_tv_radius,
            omega_size=fine_size,
            physical_size=coarse_size,
            target_size=target_size,
        )
        gain_maximum = maximum_conditional_mutual_information(
            omega_size=fine_size,
            target_size=target_size,
        )
        gain_lower, gain_upper = _bounded_interval(
            gain_estimate,
            gain_radius,
            gain_maximum,
        )

        residual_estimate = _empirical_residual(materialized, fine)
        residual_radius = conditional_information_continuity_bound(
            base_tv_radius,
            omega_size=omega_size,
            physical_size=fine_size,
            target_size=target_size,
        )
        residual_maximum = maximum_conditional_mutual_information(
            omega_size=omega_size,
            target_size=target_size,
        )
        residual_lower, residual_upper = _bounded_interval(
            residual_estimate,
            residual_radius,
            residual_maximum,
        )

        chain_rule_error = abs(
            coarse_residual_estimate - residual_estimate - gain_estimate
        )
        if chain_rule_error > tolerance:
            raise AssertionError(
                f"empirical P21 identity did not close for candidate {name!r}"
            )

        candidate_certificates.append(
            AdaptiveCandidateCertificate(
                name=name,
                gain_estimate=gain_estimate,
                gain_lower=gain_lower,
                gain_upper=gain_upper,
                gain_continuity_radius=gain_radius,
                residual_estimate=residual_estimate,
                residual_lower=residual_lower,
                residual_upper=residual_upper,
                residual_continuity_radius=residual_radius,
                empirical_chain_rule_error=chain_rule_error,
                certified_positive_gain=gain_lower > 0.0,
            )
        )

    selected_index = max(
        range(len(candidate_certificates)),
        key=lambda index: candidate_certificates[index].gain_estimate,
    )
    selected = candidate_certificates[selected_index]

    maximum_gain_radius = max(
        candidate.gain_continuity_radius for candidate in candidate_certificates
    )
    universal_gain_maximum = max(
        maximum_conditional_mutual_information(
            omega_size=candidate_sizes[candidate.name],
            target_size=target_size,
        )
        for candidate in candidate_certificates
    )
    generic_selection_regret_bound = min(
        universal_gain_maximum,
        2.0 * maximum_gain_radius,
    )

    best_population_gain_upper = max(
        candidate.gain_upper for candidate in candidate_certificates
    )
    data_dependent_selection_regret_bound = min(
        universal_gain_maximum,
        max(0.0, best_population_gain_upper - selected.gain_lower),
    )

    return AdaptiveDescriptorSelectionCertificate(
        candidates=tuple(candidate_certificates),
        selected_name=selected.name,
        selected_index=selected_index,
        coarse_residual_estimate=coarse_residual_estimate,
        coarse_residual_lower=coarse_residual_lower,
        coarse_residual_upper=coarse_residual_upper,
        base_tv_radius=base_tv_radius,
        alpha=alpha,
        simultaneous_coverage=1.0 - alpha,
        sample_size=sample_size,
        candidate_count=len(candidate_certificates),
        candidate_count_penalty_applied=False,
        maximum_gain_radius=maximum_gain_radius,
        generic_selection_regret_bound=generic_selection_regret_bound,
        data_dependent_selection_regret_bound=(
            data_dependent_selection_regret_bound
        ),
        selected_residual_excess_bound=(
            data_dependent_selection_regret_bound
        ),
        selected_gain_certified_positive=selected.certified_positive_gain,
    )
