"""Verify that current-frontier publication surfaces agree without duplicating layers.

The public repository intentionally uses a reader-first README and compact research
navigation. Complete proposition chronology lives in the detailed record; dependency
structure lives in the theorem roadmap. This verifier checks that those layers agree
rather than requiring every layer to repeat the complete technical archive.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _frontier(root: Path) -> int:
    values: list[int] = []
    for path in (root / "docs").glob("proposition_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match is not None:
            values.append(int(match.group(1)))
    if not values:
        raise RuntimeError("no proposition files found")
    return max(values)


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def verify_frontier_publication(root: Path = ROOT) -> None:
    frontier = _frontier(root)
    pfrontier = f"P{frontier}"

    # Reader-first README: concise public status plus routes to canonical records.
    readme = (root / "README.md").read_text(encoding="utf-8")
    count = re.search(
        r"current public record contains \*\*(\d+) proposition-level results\*\*",
        readme,
        flags=re.IGNORECASE,
    )
    _require(count is not None, "README is missing the concise proposition-count status")
    assert count is not None
    _require(int(count.group(1)) == frontier, "README proposition count is stale")
    _require(
        f"current public theorem frontier is **{pfrontier}**" in readme,
        "README current-frontier sentence is stale",
    )
    _require(
        f"**Public theorem frontier:** {pfrontier}" in readme,
        "README footer frontier is stale",
    )
    _require(
        f"docs/proposition_{frontier}_" in readme,
        "README current-frontier link is missing",
    )
    for route in (
        "docs/detailed_proposition_record.md",
        "docs/theorem_roadmap.md",
        "docs/figure_catalog.md",
        "docs/reproducibility.md",
    ):
        _require(route in readme, f"README is missing reader route {route}")

    # Formal dependency layer.
    roadmap = (root / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    _require(
        f"The current documented theorem frontier is **{pfrontier}**." in roadmap,
        "theorem roadmap current-frontier declaration is stale",
    )
    _require(
        f"P1 through {pfrontier}" in roadmap,
        "theorem roadmap proposition range is stale",
    )
    dependency = roadmap.split("## 2. Target-side bridge lineage", 1)[0]
    _require(
        f"\\text{{{pfrontier}:" in dependency,
        "theorem roadmap dependency map omits the current frontier",
    )
    _require(
        f"## After {pfrontier}" in roadmap,
        "theorem roadmap lacks a current-frontier future-work boundary",
    )
    for value in re.findall(r"Any P(\d+) claim", roadmap):
        _require(
            int(value) > frontier,
            f"theorem roadmap still describes closed P{value} as future work",
        )

    # Compact navigation should route to the full archive rather than duplicate it.
    navigation = (root / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    _require(
        f"The current documented theorem frontier is **{pfrontier}**." in navigation,
        "research navigation current-frontier declaration is stale",
    )
    _require(
        f"**Results:** P75 through {pfrontier}" in navigation,
        "research navigation model-adequacy range is stale",
    )
    _require(
        f"**Current frontier:** [{pfrontier}:" in navigation,
        "research navigation current-frontier link is stale",
    )
    _require(
        "Detailed Proposition Record" in navigation
        and "intentionally does **not** duplicate the full" in navigation,
        "research navigation no longer expresses the layered archive design",
    )

    # Complete chronology must carry the full range even though navigation is compact.
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    _require(
        f"Complete P1 to {pfrontier} chronology" in record,
        "detailed proposition record range is stale",
    )
    _require(
        f"**{pfrontier}**" in record,
        "detailed proposition record omits the current frontier",
    )

    # Reproducibility layer must point to the current theorem, implementation, test, and figure.
    reproducibility = (root / "docs" / "reproducibility.md").read_text(encoding="utf-8")
    _require(
        f"The current public theorem frontier is **{pfrontier}**." in reproducibility,
        "reproducibility guide current-frontier declaration is stale",
    )
    _require(
        f"## 5. Focused audit of the current {pfrontier} frontier" in reproducibility,
        "reproducibility focused-audit section is stale",
    )
    _require(
        f"### {pfrontier} exact frontier check" in reproducibility,
        "reproducibility reviewer frontier check is stale",
    )
    _require(
        f"proposition_{frontier}_" in reproducibility,
        "reproducibility guide omits current proposition path",
    )

    # Figure gateway and manifest provide exact byte-level publication identity.
    manifest_path = root / "figures" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    _require(
        manifest.get("current_frontier") == pfrontier,
        "figure manifest current frontier is stale",
    )
    frontier_figure = str(manifest.get("current_frontier_figure", ""))
    _require(
        f"p{frontier}_" in frontier_figure,
        "figure manifest current-frontier figure is stale",
    )
    _require((root / frontier_figure).is_file(), "manifest current-frontier figure is missing")

    gateway = (root / "figures" / "README.md").read_text(encoding="utf-8")
    current_visual = (root / "figures" / "CURRENT_FRONTIER.md").read_text(encoding="utf-8")
    _require(
        f"## Current theorem frontier: {pfrontier}" in gateway,
        "figure gateway frontier is stale",
    )
    _require(
        f"# Current visual frontier: P71-{pfrontier}" in current_visual,
        "current visual frontier range is stale",
    )

    # Public website must retain the restored reader-first identity while exposing P88.
    home = (root / "website" / "index.html").read_text(encoding="utf-8")
    plain = (root / "website" / "plain-language.html").read_text(encoding="utf-8")
    _require(
        "What would a scientifically testable bridge from physical description to experience actually require?"
        in home,
        "homepage reader-first identity is missing",
    )
    _require(
        f"Current theorem frontier · {pfrontier}" in home,
        "homepage current frontier is stale",
    )
    _require(
        f"Explore all {frontier} results" in home,
        "homepage result count is stale",
    )
    _require(
        "Explain it in 60 seconds" in plain
        and "Seven questions have to be kept separate" in plain,
        "plain-language reader layer is missing",
    )
    _require(
        f"Current exact frontier · {pfrontier}" in plain,
        "plain-language current frontier is stale",
    )

    print(
        f"[frontier] reader, formal, reproducibility, figure, and website layers "
        f"agree with {pfrontier}"
    )


def main() -> None:
    verify_frontier_publication()


if __name__ == "__main__":
    main()
