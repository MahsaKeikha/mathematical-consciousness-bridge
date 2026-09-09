"""Exact finite robust experiment design for Proposition 10."""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from itertools import combinations
from typing import TypeVar

from consciousness_bridge.robust_signature_recovery import (
    signature_spread_and_separation,
)

P = TypeVar("P", bound=Hashable)
Protocol = TypeVar("Protocol", bound=Hashable)
Outcome = TypeVar("Outcome", bound=Hashable)
Z = TypeVar("Z", bound=Hashable)


def robust_signature_gap(
    predictions: Mapping[P, Mapping[Protocol, Mapping[Outcome, float]]],
    feature: Mapping[P, Z],
    protocols: Iterable[Protocol],
) -> float:
    """Return delta(S) - omega(S) for a finite protocol family."""
    selected = tuple(protocols)
    if not selected:
        raise ValueError("Protocol family must be nonempty.")

    restricted: dict[P, dict[Protocol, Mapping[Outcome, float]]] = {}
    for physical_state, protocol_table in predictions.items():
        missing = [protocol for protocol in selected if protocol not in protocol_table]
        if missing:
            raise ValueError(f"Missing protocols for {physical_state!r}: {missing!r}")
        restricted[physical_state] = {
            protocol: protocol_table[protocol] for protocol in selected
        }

    within, between = signature_spread_and_separation(restricted, feature)
    return between - within


def protocol_addition_effect(
    predictions: Mapping[P, Mapping[Protocol, Mapping[Outcome, float]]],
    feature: Mapping[P, Z],
    current: Iterable[Protocol],
    added: Protocol,
) -> tuple[float, float, float]:
    """Return (between gain, within inflation, robust-gap change)."""
    current_tuple = tuple(current)
    if not current_tuple:
        raise ValueError("Current protocol family must be nonempty.")
    if added in current_tuple:
        raise ValueError("Added protocol is already in the current family.")

    current_table = _restricted_table(predictions, current_tuple)
    expanded_table = _restricted_table(predictions, current_tuple + (added,))

    current_within, current_between = signature_spread_and_separation(
        current_table, feature
    )
    expanded_within, expanded_between = signature_spread_and_separation(
        expanded_table, feature
    )

    between_gain = expanded_between - current_between
    within_inflation = expanded_within - current_within
    gap_change = between_gain - within_inflation
    return between_gain, within_inflation, gap_change


def optimal_protocol_family(
    predictions: Mapping[P, Mapping[Protocol, Mapping[Outcome, float]]],
    feature: Mapping[P, Z],
    max_protocol_count: int,
) -> tuple[tuple[Protocol, ...], float]:
    """Return an exact max-gap family under a finite protocol-count budget.

    Ties are resolved by preferring fewer protocols and then repr order.
    """
    if max_protocol_count < 1:
        raise ValueError("max_protocol_count must be positive.")
    if not predictions:
        raise ValueError("Physical domain must be nonempty.")

    protocol_sets = [set(table) for table in predictions.values()]
    common = set.intersection(*protocol_sets)
    if not common:
        raise ValueError("No common protocols are available.")

    ordered = tuple(sorted(common, key=repr))
    limit = min(max_protocol_count, len(ordered))

    candidates: list[tuple[tuple[Protocol, ...], float]] = []
    for size in range(1, limit + 1):
        for family in combinations(ordered, size):
            gap = robust_signature_gap(predictions, feature, family)
            candidates.append((family, gap))

    return min(
        candidates,
        key=lambda item: (-item[1], len(item[0]), tuple(map(repr, item[0]))),
    )


def _restricted_table(
    predictions: Mapping[P, Mapping[Protocol, Mapping[Outcome, float]]],
    protocols: tuple[Protocol, ...],
) -> dict[P, dict[Protocol, Mapping[Outcome, float]]]:
    restricted: dict[P, dict[Protocol, Mapping[Outcome, float]]] = {}
    for physical_state, protocol_table in predictions.items():
        if any(protocol not in protocol_table for protocol in protocols):
            raise ValueError("Every selected protocol must exist for every physical state.")
        restricted[physical_state] = {
            protocol: protocol_table[protocol] for protocol in protocols
        }
    return restricted
