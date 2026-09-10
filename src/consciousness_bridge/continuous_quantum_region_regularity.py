"""Proposition 40: continuous quantum-region regularity obstruction.

The module implements a finite-preparation obstruction theorem for continuous
quantum confidence regions. It separates two facts:

1. if an admissible quantum descriptor is injective on the finite preparation
   set, unrestricted factorization can always fit arbitrary target values on the
   descriptor image;
2. if the bridge is required to obey a declared modulus of continuity, target
   separation can exceed every admissible quantum-state separation allowed by a
   confidence region, yielding a robust non-factorization certificate.

The theorem is descriptor and regularity relative. It does not establish that
quantum mechanics is incomplete or that any target is consciousness.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from typing import TypeVar

Preparation = TypeVar("Preparation", bound=Hashable)


@dataclass(frozen=True)
class ContinuousRegionRegularityCertificate:
    """Certificate for a declared bridge modulus over a quantum confidence region."""

    maximum_obstruction_margin: float
    witness_pair_count: int
    certified: bool


def injective_descriptor_allows_unrestricted_factorization(
    preparations: Sequence[Preparation],
    pairwise_state_distances: Mapping[tuple[Preparation, Preparation], float],
    *,
    zero_tolerance: float = 0.0,
) -> bool:
    """Return whether the finite descriptor is injective from pairwise distances.

    For a finite preparation set, strict positive distance for every distinct pair
    means all descriptor values are distinct. Any target assignment on that finite
    image then factors through some unrestricted map defined on the image.
    """
    if zero_tolerance < 0.0:
        raise ValueError("zero_tolerance must be nonnegative")
    preps = tuple(preparations)
    _validate_preparations(preps)
    _validate_pairwise_table(preps, pairwise_state_distances)
    return all(
        _distance(pairwise_state_distances, first, second) > zero_tolerance
        for index, first in enumerate(preps)
        for second in preps[index + 1 :]
    )


def regularity_obstruction_margin(
    target_separation_lower_bound: float,
    quantum_distance_upper_bound: float,
    modulus_upper_bound: float,
) -> float:
    """Return target lower separation minus the allowed bridge variation.

    ``modulus_upper_bound`` should already equal omega(r), where ``r`` is the
    relevant quantum-distance upper bound. A positive margin rules out every
    factorization obeying the declared modulus at that pair.
    """
    _unit_interval(target_separation_lower_bound, "target_separation_lower_bound")
    _unit_interval(quantum_distance_upper_bound, "quantum_distance_upper_bound")
    if modulus_upper_bound < 0.0:
        raise ValueError("modulus_upper_bound must be nonnegative")
    return target_separation_lower_bound - modulus_upper_bound


def continuous_region_regularity_certificate(
    preparations: Sequence[Preparation],
    target_separation_lower_bounds: Mapping[tuple[Preparation, Preparation], float],
    quantum_distance_upper_bounds: Mapping[tuple[Preparation, Preparation], float],
    modulus_values: Mapping[tuple[Preparation, Preparation], float],
    *,
    tolerance: float = 1e-12,
) -> ContinuousRegionRegularityCertificate:
    """Certify failure of every bridge satisfying the declared pairwise modulus.

    On a joint confidence event, suppose for every preparation pair ``x,x'``:

    * the true target-law total-variation distance is at least ``L[x,x']``;
    * every admissible quantum descriptor in the confidence region has trace
      distance at most ``U[x,x']``;
    * every admissible bridge obeys ``TV(g(rho), g(sigma)) <= omega(D(rho,sigma))``
      and ``modulus_values[x,x']`` is an upper bound on ``omega(U[x,x'])``.

    If some pair satisfies ``L > omega(U)``, then no descriptor in the confidence
    region can support a bridge in the declared regularity class.
    """
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    preps = tuple(preparations)
    _validate_preparations(preps)
    _validate_pairwise_table(preps, target_separation_lower_bounds)
    _validate_pairwise_table(preps, quantum_distance_upper_bounds)
    _validate_pairwise_table(preps, modulus_values, unit_interval=False)

    margins: list[float] = []
    for index, first in enumerate(preps):
        for second in preps[index + 1 :]:
            lower = _distance(target_separation_lower_bounds, first, second)
            upper = _distance(quantum_distance_upper_bounds, first, second)
            modulus = _distance(modulus_values, first, second)
            _unit_interval(lower, "target separation lower bound")
            _unit_interval(upper, "quantum distance upper bound")
            if modulus < 0.0:
                raise ValueError("modulus values must be nonnegative")
            margins.append(regularity_obstruction_margin(lower, upper, modulus))

    maximum = max(margins)
    witness_count = sum(margin > tolerance for margin in margins)
    return ContinuousRegionRegularityCertificate(
        maximum_obstruction_margin=maximum,
        witness_pair_count=witness_count,
        certified=maximum > tolerance,
    )


def lipschitz_modulus_values(
    preparations: Sequence[Preparation],
    quantum_distance_upper_bounds: Mapping[tuple[Preparation, Preparation], float],
    lipschitz_constant: float,
) -> dict[tuple[Preparation, Preparation], float]:
    """Build pairwise omega(U)=L*U values for an L-Lipschitz bridge class."""
    if lipschitz_constant < 0.0:
        raise ValueError("lipschitz_constant must be nonnegative")
    preps = tuple(preparations)
    _validate_preparations(preps)
    _validate_pairwise_table(preps, quantum_distance_upper_bounds)
    result: dict[tuple[Preparation, Preparation], float] = {}
    for index, first in enumerate(preps):
        for second in preps[index + 1 :]:
            upper = _distance(quantum_distance_upper_bounds, first, second)
            _unit_interval(upper, "quantum distance upper bound")
            result[(first, second)] = lipschitz_constant * upper
    return result


def _validate_preparations(preparations: tuple[Preparation, ...]) -> None:
    if len(preparations) < 2:
        raise ValueError("at least two preparations are required")
    if len(set(preparations)) != len(preparations):
        raise ValueError("preparations must be unique")


def _validate_pairwise_table(
    preparations: tuple[Preparation, ...],
    table: Mapping[tuple[Preparation, Preparation], float],
    *,
    unit_interval: bool = True,
) -> None:
    expected = {
        (first, second)
        for index, first in enumerate(preparations)
        for second in preparations[index + 1 :]
    }
    reversed_expected = {(second, first) for first, second in expected}
    keys = set(table)
    if not keys <= expected | reversed_expected:
        raise ValueError("pairwise table contains undeclared or diagonal pairs")
    for first, second in expected:
        if (first, second) not in table and (second, first) not in table:
            raise ValueError("pairwise table must cover every unordered pair")
        value = _distance(table, first, second)
        if unit_interval:
            _unit_interval(value, "pairwise distance")
        elif value < 0.0:
            raise ValueError("pairwise values must be nonnegative")


def _distance(
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
