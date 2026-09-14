"""Synchronize the public website with the validated Research III snapshot.

This script keeps the cross-repository handoff auditable. It updates pinned
Research III asset references, removes duplicated P88 source markers, and
checks that the reader-facing Research III surfaces point at one exact
validated commit.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

CURRENT_RESEARCH_THREE_PIN = "b874eda1f6940f5601b7f89200b6a276b5ecbbc3"
LEGACY_RESEARCH_THREE_PINS = (
    "8bbb7b029d70c43cc6a9dbf8b44dfe5069d0993d",
    "7a106820158e0d33ea651f7cdeaa505206f1ccc7",
)
P88_HOME_MARKER = "<!-- current-frontier-home: P88 -->"


def _replace_research_three_pins(text: str) -> str:
    for legacy in LEGACY_RESEARCH_THREE_PINS:
        text = text.replace(legacy, CURRENT_RESEARCH_THREE_PIN)
    return text


def _collapse_frontier_markers(text: str) -> str:
    marker_pattern = re.compile(
        rf"(?:{re.escape(P88_HOME_MARKER)}\s*){{2,}}",
        flags=re.MULTILINE,
    )
    return marker_pattern.sub(f"{P88_HOME_MARKER}\n", text)


def synchronize_site(site: Path, *, write: bool) -> list[str]:
    """Return changed paths and optionally write synchronized source files."""

    targets = {
        "measurement-science.html": _replace_research_three_pins,
        "research-lineage.html": _replace_research_three_pins,
        "index.html": _collapse_frontier_markers,
    }
    changed: list[str] = []

    for relative, transform in targets.items():
        path = site / relative
        if not path.is_file():
            raise FileNotFoundError(f"missing website surface: {path}")
        original = path.read_text(encoding="utf-8")
        updated = transform(original)
        if updated != original:
            changed.append(relative)
            if write:
                path.write_text(updated, encoding="utf-8")

    validation_text = {
        name: (site / name).read_text(encoding="utf-8")
        for name in targets
    }
    if validation_text["index.html"].count(P88_HOME_MARKER) != 1:
        raise RuntimeError("homepage must contain exactly one current P88 source marker")

    for surface in ("measurement-science.html", "research-lineage.html"):
        text = validation_text[surface]
        if CURRENT_RESEARCH_THREE_PIN not in text:
            raise RuntimeError(
                f"{surface} is not pinned to Research III {CURRENT_RESEARCH_THREE_PIN}"
            )
        stale = [pin for pin in LEGACY_RESEARCH_THREE_PINS if pin in text]
        if stale:
            raise RuntimeError(f"{surface} still contains stale Research III pins: {stale}")

    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, default=Path("website"))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()

    changed = synchronize_site(args.site, write=args.write)
    if args.check and changed:
        raise SystemExit(
            "Research III website synchronization required for: " + ", ".join(changed)
        )
    if changed:
        action = "updated" if args.write else "would update"
        print(f"{action}: {', '.join(changed)}")
    else:
        print("Research III website surfaces are synchronized.")


if __name__ == "__main__":
    main()
