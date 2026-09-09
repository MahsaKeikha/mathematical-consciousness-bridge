"""Finite observational-equivalence classes for bridge theories.

This module implements the finite fingerprint construction from Proposition 3.
Exact finite probability tables are used; no tolerance-based equivalence relation
is introduced because an approximate relation need not be transitive.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Hashable, Mapping
from typing import TypeVar

from consciousness_bridge.identifiability import total_variation_discrete

Theory = TypeVar("Theory", bound=Hashable)
Protocol = TypeVar("Protocol", bound=Hashable)
Outcome = TypeVar("Outcome", bound=Hashable)

Fingerprint = tuple[
    tuple[Hashable, tuple[tuple[Hashable, float], ...]], ...
]


def observational_fingerprint(
    predictions: Mapping[Protocol, Mapping[Outcome, float]],
) -> Fingerprint:
    """Return an exact canonical fingerprint for a finite protocol family."""
    if not predictions:
        raise ValueError("Protocol class must be nonempty.")

    canonical_protocols = []
    for protocol in sorted(predictions, key=repr):
        distribution = predictions[protocol]
        total_variation_discrete(distribution, distribution)
        canonical_distribution = tuple(
            sorted(distribution.items(), key=lambda item: repr(item[0]))
        )
        canonical_protocols.append((protocol, canonical_distribution))
    return tuple(canonical_protocols)


def observationally_equivalent(
    first: Mapping[Protocol, Mapping[Outcome, float]],
    second: Mapping[Protocol, Mapping[Outcome, float]],
) -> bool:
    """Return exact equality of complete finite observational fingerprints."""
    return observational_fingerprint(first) == observational_fingerprint(second)


def bridge_equivalence_classes(
    theories: Mapping[Theory, Mapping[Protocol, Mapping[Outcome, float]]],
) -> tuple[frozenset[Theory], ...]:
    """Partition a finite theory family into exact observational fibers."""
    if not theories:
        raise ValueError("Theory family must be nonempty.")

    expected_protocols: set[Protocol] | None = None
    fibers: dict[Fingerprint, set[Theory]] = defaultdict(set)

    for theory, predictions in theories.items():
        protocols = set(predictions)
        if expected_protocols is None:
            expected_protocols = protocols
        elif protocols != expected_protocols:
            raise ValueError("All theories must use the same protocol class.")
        fibers[observational_fingerprint(predictions)].add(theory)

    classes = [frozenset(members) for members in fibers.values()]
    return tuple(sorted(classes, key=lambda members: sorted(map(repr, members))))


def restrict_protocols(
    predictions: Mapping[Protocol, Mapping[Outcome, float]],
    protocols: set[Protocol],
) -> dict[Protocol, Mapping[Outcome, float]]:
    """Restrict one theory to a declared subfamily of protocols."""
    if not protocols <= set(predictions):
        raise ValueError("Requested protocol is missing from the theory.")
    return {protocol: predictions[protocol] for protocol in protocols}
