"""Finite experiment-design helpers for Proposition 4."""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from itertools import combinations
from typing import TypeVar

from consciousness_bridge.identifiability import total_variation_discrete

Theory = TypeVar("Theory", bound=Hashable)
Protocol = TypeVar("Protocol", bound=Hashable)
Outcome = TypeVar("Outcome", bound=Hashable)

TheoryPredictions = Mapping[Protocol, Mapping[Outcome, float]]
TheoryFamily = Mapping[Theory, TheoryPredictions]


def _common_protocols(theories: TheoryFamily) -> tuple[Protocol, ...]:
    if len(theories) < 2:
        raise ValueError("At least two theories are required.")

    protocol_sets = [set(predictions) for predictions in theories.values()]
    first = protocol_sets[0]
    if not first:
        raise ValueError("Protocol class must be nonempty.")
    if any(protocols != first for protocols in protocol_sets[1:]):
        raise ValueError("All theories must use the same protocol class.")
    return tuple(sorted(first, key=repr))


def _theory_pairs(theories: TheoryFamily) -> tuple[tuple[Theory, Theory], ...]:
    names = tuple(sorted(theories, key=repr))
    return tuple(combinations(names, 2))


def protocol_pair_separations(
    theories: TheoryFamily,
    protocol: Protocol,
) -> dict[tuple[Theory, Theory], float]:
    """Return pairwise TV separations for one protocol."""
    protocols = set(_common_protocols(theories))
    if protocol not in protocols:
        raise ValueError("Protocol is not in the common protocol class.")

    result: dict[tuple[Theory, Theory], float] = {}
    for first, second in _theory_pairs(theories):
        result[(first, second)] = total_variation_discrete(
            theories[first][protocol], theories[second][protocol]
        )
    return result


def distinguishable_pairs(theories: TheoryFamily) -> frozenset[tuple[Theory, Theory]]:
    """Return theory pairs separated by at least one protocol."""
    protocols = _common_protocols(theories)
    pairs = _theory_pairs(theories)
    distinguishable: set[tuple[Theory, Theory]] = set()
    for pair in pairs:
        first, second = pair
        if any(
            total_variation_discrete(
                theories[first][protocol], theories[second][protocol]
            )
            > 0.0
            for protocol in protocols
        ):
            distinguishable.add(pair)
    return frozenset(distinguishable)


def protocol_set_utility(
    theories: TheoryFamily,
    selected_protocols: set[Protocol],
) -> float:
    """Return worst-pair best-protocol separation U(S)."""
    protocols = set(_common_protocols(theories))
    if not selected_protocols:
        raise ValueError("At least one protocol must be selected.")
    if not selected_protocols <= protocols:
        raise ValueError("Selected protocol is outside the common class.")

    universe = distinguishable_pairs(theories)
    if not universe:
        raise ValueError("No theory pair is distinguishable in the full class.")

    pair_values = []
    for first, second in universe:
        pair_values.append(
            max(
                total_variation_discrete(
                    theories[first][protocol], theories[second][protocol]
                )
                for protocol in selected_protocols
            )
        )
    return min(pair_values)


def best_single_protocol(
    theories: TheoryFamily,
) -> tuple[Protocol, float]:
    """Return a maximin single protocol and its utility."""
    protocols = _common_protocols(theories)
    scored = [
        (protocol, protocol_set_utility(theories, {protocol}))
        for protocol in protocols
    ]
    scored.sort(key=lambda item: (-item[1], repr(item[0])))
    return scored[0]


def minimal_discriminating_protocol_sets(
    theories: TheoryFamily,
) -> tuple[frozenset[Protocol], ...]:
    """Return all minimum-cardinality protocol sets with positive utility."""
    protocols = _common_protocols(theories)
    universe = distinguishable_pairs(theories)
    if not universe:
        raise ValueError("No theory pair is distinguishable in the full class.")

    for size in range(1, len(protocols) + 1):
        solutions = []
        for selected in combinations(protocols, size):
            selected_set = set(selected)
            if protocol_set_utility(theories, selected_set) > 0.0:
                solutions.append(frozenset(selected_set))
        if solutions:
            return tuple(sorted(solutions, key=lambda value: sorted(map(repr, value))))

    raise RuntimeError("Full protocol class should separate its distinguishable pairs.")
