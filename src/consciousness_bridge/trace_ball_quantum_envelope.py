"""Proposition 41: trace-ball quantum envelope and end-to-end regularity test.

The module turns per-preparation trace-distance confidence balls around estimated
quantum states into pairwise upper bounds for the P40 continuous-region envelope.
It can then combine those quantum bounds with simultaneous target-law TV bounds
and a declared Lipschitz bridge class.

The certificate is conditional on the stated confidence events and bridge
regularity assumption. It does not establish quantum incompleteness or identify
any target with consciousness.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from typing import TypeVar

Preparation = TypeVar("Preparation", bound=Hashable)


@dataclass(frozen=True)
class TraceBallPairCertificate:
    """One pairwise end-to-end P40 certificate."""

    quantum_distance_upper_bound: float
    target_separation_lower_bound: float
    allowed_target_variation: float
    obstruction_margin: float
    certified: bool


@dataclass(frozen=True)
class TraceBallGlobalCertificate:
    """Global certificate over a finite preparation family."""

    maximum_obstruction_margin: float
    witness_pair_count: int
    confidence_lower_bound: float
    certified: bool


def trace_ball_pairwise_upper_bound(
    estimated_trace_distance: float,
    first_radius: float,
    second_radius: float,
) -> float:
    """Upper-bound true pairwise trace distance from two confidence balls.

    If D(rho_x, rho_hat_x) <= r_x and D(rho_y, rho_hat_y) <= r_y, then triangle
    inequality gives D(rho_x, rho_y) <= D(rho_hat_x, rho_hat_y) + r_x + r_y.
    Trace distance is at most one, so the bound is clipped to one.
    """
    _unit_interval(estimated_trace_distance, "estimated_trace_distance")
    _unit_interval(first_radius, "first_radius")
    _unit_interval(second_radius, "second_radius")
    return min(1.0, estimated_trace_distance + first_radius + second_radius)


def target_pairwise_lower_bound(
    estimated_target_tv: float,
    first_radius: float,
    second_radius: float,
) -> float:
    """Lower-bound true target-law TV separation from simultaneous TV balls."""
    _unit_interval(estimated_target_tv, "estimated_target_tv")
    _unit_interval(first_radius, "first_radius")
    _unit_interval(second_radius, "second_radius")
    return max(0.0, estimated_target_tv - first_radius - second_radius)


def lipschitz_trace_ball_pair_certificate(
    estimated_quantum_trace_distance: float,
    first_quantum_radius: float,
    second_quantum_radius: float,
    estimated_target_tv: float,
    first_target_radius: float,
    second_target_radius: float,
    lipschitz_constant: float,
    *,
    tolerance: float = 1e-12,
) -> TraceBallPairCertificate:
    """Return the direct P40 obstruction certificate for one pair."""
    if lipschitz_constant < 0.0:
        raise ValueError("lipschitz_constant must be nonnegative")
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")

    quantum_upper = trace_ball_pairwise_upper_bound(
        estimated_quantum_trace_distance,
        first_quantum_radius,
        second_quantum_radius,
    )
    target_lower = target_pairwise_lower_bound(
        estimated_target_tv,
        first_target_radius,
        second_target_radius,
    )
    allowed = lipschitz_constant * quantum_upper
    margin = target_lower - allowed
    return TraceBallPairCertificate(
        quantum_distance_upper_bound=quantum_upper,
        target_separation_lower_bound=target_lower,
        allowed_target_variation=allowed,
        obstruction_margin=margin,
        certified=margin > tolerance,
    )


def trace_ball_global_lipschitz_certificate(
    preparations: Sequence[Preparation],
    estimated_quantum_distances: Mapping[tuple[Preparation, Preparation], float],
    quantum_radii: Mapping[Preparation, float],
    estimated_target_distances: Mapping[tuple[Preparation, Preparation], float],
    target_radii: Mapping[Preparation, float],
    lipschitz_constant: float,
    *,
    alpha_quantum: float,
    alpha_target: float,
    tolerance: float = 1e-12,
) -> TraceBallGlobalCertificate:
    """Audit every preparation pair under simultaneous quantum and target balls.

    The quantum coverage premise is that every true state lies in its declared
    trace-distance ball simultaneously with probability at least 1-alpha_quantum.
    The target premise is the analogous simultaneous TV event with probability at
    least 1-alpha_target. Their joint event has probability at least the clipped
    union-bound value 1-alpha_quantum-alpha_target.
    """
    if lipschitz_constant < 0.0:
        raise ValueError("lipschitz_constant must be nonnegative")
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    _alpha(alpha_quantum, "alpha_quantum")
    _alpha(alpha_target, "alpha_target")

    preps = tuple(preparations)
    _validate_preparations(preps)
    _validate_pairwise(preps, estimated_quantum_distances, "estimated_quantum_distances")
    _validate_pairwise(preps, estimated_target_distances, "estimated_target_distances")
    _validate_radii(preps, quantum_radii, "quantum_radii")
    _validate_radii(preps, target_radii, "target_radii")

    margins: list[float] = []
    for index, first in enumerate(preps):
        for second in preps[index + 1 :]:
            pair = lipschitz_trace_ball_pair_certificate(
                _pair_value(estimated_quantum_distances, first, second),
                quantum_radii[first],
                quantum_radii[second],
                _pair_value(estimated_target_distances, first, second),
                target_radii[first],
                target_radii[second],
                lipschitz_constant,
                tolerance=tolerance,
            )
            margins.append(pair.obstruction_margin)

    maximum = max(margins)
    return TraceBallGlobalCertificate(
        maximum_obstruction_margin=maximum,
        witness_pair_count=sum(margin > tolerance for margin in margins),
        confidence_lower_bound=max(0.0, 1.0 - alpha_quantum - alpha_target),
        certified=maximum > tolerance,
    )


def _validate_preparations(preparations: tuple[Preparation, ...]) -> None:
    if len(preparations) < 2:
        raise ValueError("at least two preparations are required")
    if len(set(preparations)) != len(preparations):
        raise ValueError("preparations must be unique")


def _validate_pairwise(
    preparations: tuple[Preparation, ...],
    table: Mapping[tuple[Preparation, Preparation], float],
    name: str,
) -> None:
    expected = {
        (first, second)
        for index, first in enumerate(preparations)
        for second in preparations[index + 1 :]
    }
    allowed = expected | {(second, first) for first, second in expected}
    if not set(table) <= allowed:
        raise ValueError(f"{name} contains undeclared or diagonal pairs")
    for first, second in expected:
        if (first, second) not in table and (second, first) not in table:
            raise ValueError(f"{name} must cover every unordered pair")
        _unit_interval(_pair_value(table, first, second), name)


def _validate_radii(
    preparations: tuple[Preparation, ...],
    radii: Mapping[Preparation, float],
    name: str,
) -> None:
    if set(radii) != set(preparations):
        raise ValueError(f"{name} must cover every and only declared preparation")
    for radius in radii.values():
        _unit_interval(radius, name)


def _pair_value(
    table: Mapping[tuple[Preparation, Preparation], float],
    first: Preparation,
    second: Preparation,
) -> float:
    if (first, second) in table:
        return table[(first, second)]
    return table[(second, first)]


def _unit_interval(value: float, name: str) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must lie in [0, 1]")


def _alpha(value: float, name: str) -> None:
    if not 0.0 <= value < 1.0:
        raise ValueError(f"{name} must lie in [0, 1)")
