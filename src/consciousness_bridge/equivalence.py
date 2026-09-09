"""Abstract helpers for finite representation-equivalence experiments.

These utilities do not encode a consciousness theory. They support testing
whether a proposed finite bridge assignment is constant on declared physical
equivalence classes.
"""

from collections.abc import Hashable, Mapping
from typing import TypeVar

P = TypeVar("P", bound=Hashable)
E = TypeVar("E", bound=Hashable)


def bridge_is_class_invariant(
    class_of: Mapping[P, Hashable],
    bridge: Mapping[P, E],
) -> bool:
    """Return whether a finite bridge assignment is constant on each class."""
    seen: dict[Hashable, E] = {}
    for physical_state, class_id in class_of.items():
        experiential_state = bridge[physical_state]
        if class_id in seen and seen[class_id] != experiential_state:
            return False
        seen[class_id] = experiential_state
    return True


def quotient_bridge(
    class_of: Mapping[P, Hashable],
    bridge: Mapping[P, E],
) -> dict[Hashable, E]:
    """Construct the finite quotient bridge when representation invariant."""
    if not bridge_is_class_invariant(class_of, bridge):
        raise ValueError("Bridge is not invariant on physical equivalence classes.")

    result: dict[Hashable, E] = {}
    for physical_state, class_id in class_of.items():
        result[class_id] = bridge[physical_state]
    return result
