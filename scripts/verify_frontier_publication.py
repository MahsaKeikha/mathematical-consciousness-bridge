"""Verify that current-frontier publication surfaces agree.

The README is intentionally reader-first. Frontier verification therefore checks
its compact current-status declarations and current-theorem link rather than
requiring the older monolithic count table that was removed from the public
landing page. Detailed counts remain machine-verifiable from the proposition
and figure trees.
"""

from __future__ import annotations

import json
import re
import tomllib
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


def _package_version(root: Path) -> str:
    data = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
    version = data.get("project", {}).get("version")
    if not isinstance(version, str) or not version:
        raise RuntimeError("pyproject.toml is missing project.version")
    return version


def _current_proposition(root: Path, frontier: int) -> Path:
    matches = sorted((root / "docs").glob(f"proposition_{frontier}_*.md"))
    _require(
        len(matches) == 1,
        f"expected exactly one proposition file for P{frontier}, found {len(matches)}",
    )
    return matches[0]


def verify_frontier_publication(root: Path = ROOT) -> None:
    frontier = _frontier(root)
    pfrontier = f"P{frontier}"
    version = _package_version(root)
    proposition = _current_proposition(root, frontier)

    readme = (root / "README.md").read_text(encoding="utf-8")
    _require(
        f"The current public theorem frontier is **{pfrontier}**." in readme,
        "README current public theorem-frontier declaration is stale or missing",
    )
    _require(
        f"The formal release remains **v{version}**." in readme,
        "README formal-release declaration disagrees with pyproject.toml",
    )
    _require(
        f"**Public theorem frontier:** {pfrontier}" in readme,
        "README citation/footer frontier declaration is stale or missing",
    )
    _require(
        f"**Formal release:** v{version}" in readme,
        "README citation/footer release declaration disagrees with pyproject.toml",
    )
    expected_frontier_link = (
        f"[Read the current frontier](docs/{proposition.name})"
    )
    _require(
        expected_frontier_link in readme,
        "README current-frontier link does not point to the canonical proposition",
    )

    manifest_path = root / "figures" / "manifest.json"
    _require(manifest_path.is_file(), "figure publication manifest is missing")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    _require(
        manifest.get("current_frontier") == pfrontier,
        "figure publication manifest current frontier is stale",
    )
    figure_count = manifest.get("figure_count")
    _require(
        isinstance(figure_count, int) and figure_count > 0,
        "figure publication manifest has no valid figure count",
    )

    roadmap = (root / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    _require(
        f"The current documented theorem frontier is **{pfrontier}**." in roadmap,
        "theorem roadmap current-frontier declaration is stale",
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
    for value in re.findall(r"Any P(\d+) candidate", roadmap):
        _require(
            int(value) > frontier,
            f"theorem roadmap still describes closed P{value} as a future candidate",
        )
    for value in re.findall(r"continuation beyond P(\d+)", roadmap):
        _require(
            int(value) >= frontier,
            f"theorem roadmap future-work language is still pinned below {pfrontier}",
        )

    navigation = (root / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    _require(
        f"The current documented theorem frontier is **{pfrontier}**." in navigation,
        "research navigation current-frontier declaration is stale",
    )
    recommended_parts = navigation.split("## Recommended reading order", 1)
    _require(len(recommended_parts) == 2, "research navigation lacks recommended reading order")
    recommended = recommended_parts[1].split("## Scientific branch map", 1)[0]
    _require(
        f"[P{frontier} " in recommended,
        "recommended reading order omits the current frontier",
    )
    branch_parts = navigation.split("## Scientific branch map", 1)
    _require(len(branch_parts) == 2, "research navigation lacks scientific branch map")
    branch = branch_parts[1].split("## Complete proposition index", 1)[0]
    _require(
        re.search(rf"^\| [^|]+ \| P{frontier} \|", branch, re.MULTILINE)
        is not None,
        "scientific branch map omits the current frontier",
    )

    reproducibility = (root / "docs" / "reproducibility.md").read_text(encoding="utf-8")
    _require(
        f"The current theorem frontier is **{pfrontier}**." in reproducibility,
        "reproducibility guide current-frontier declaration is stale",
    )
    _require(
        f"## 12. Reproduce the current {pfrontier} implementation checks directly"
        in reproducibility,
        "reproducibility guide focused-audit section is stale",
    )

    print(
        f"[frontier] publication surfaces agree with {pfrontier}; "
        f"formal release=v{version}; figure manifest count={figure_count}"
    )


def main() -> None:
    verify_frontier_publication()


if __name__ == "__main__":
    main()
