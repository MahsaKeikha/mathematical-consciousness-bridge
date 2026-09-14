"""Verify that canonical current-frontier publication surfaces agree.

The repository uses reader-first navigation rather than one monolithic status
page. This verifier therefore checks each canonical surface in the structure it
actually publishes: README, figure manifest, theorem roadmap, research
navigation, and reproducibility guide.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

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
    previous = f"P{frontier - 1}"
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
    _require(
        f"[Read the current frontier](docs/{proposition.name})" in readme,
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
    current_figure = manifest.get("current_frontier_figure")
    _require(
        isinstance(current_figure, str) and current_figure.startswith("docs/figures/"),
        "figure publication manifest has no canonical current-frontier figure",
    )
    _require(
        (root / current_figure).is_file(),
        "manifest current-frontier figure does not exist",
    )
    current_figure_name = Path(current_figure).name

    roadmap = (root / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    _require(
        f"The current documented theorem frontier is **{pfrontier}**." in roadmap,
        "theorem roadmap current-frontier declaration is stale",
    )
    _require(
        f"P1 through P{frontier} with explicit dependency branches" in roadmap,
        "theorem roadmap proposition-range declaration is stale",
    )
    dependency = roadmap.split("## 2. Target-side bridge lineage", 1)[0]
    _require(
        f"\\text{{{pfrontier}:" in dependency,
        "theorem roadmap dependency map omits the current frontier",
    )
    _require(
        f"[{pfrontier}]({proposition.name})" in roadmap,
        "theorem roadmap proposition index omits the canonical current theorem",
    )
    _require(
        f"## {pfrontier}:" in roadmap,
        "theorem roadmap lacks a dedicated current-frontier section",
    )
    _require(
        f"## After {pfrontier}" in roadmap,
        "theorem roadmap lacks a current-frontier future-work boundary",
    )
    for value in re.findall(r"Any P(\d+) (?:candidate|claim)", roadmap):
        _require(
            int(value) > frontier,
            f"theorem roadmap still describes closed P{value} as future work",
        )
    for value in re.findall(r"continuation beyond P(\d+)", roadmap):
        _require(
            int(value) >= frontier,
            f"theorem roadmap future-work language is pinned below {pfrontier}",
        )
    _require(
        f"The current documented theorem frontier is **{previous}**." not in roadmap,
        "theorem roadmap still marks the previous proposition as current",
    )

    navigation = (root / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    _require(
        f"The current documented theorem frontier is **{pfrontier}**." in navigation,
        "research navigation documented-frontier declaration is stale",
    )
    _require(
        f"**Results:** P75 through P{frontier}" in navigation,
        "research navigation model-adequacy range is stale",
    )
    _require(
        re.search(
            rf"\*\*Current frontier:\*\* \[{pfrontier}:[^\]]+\]\({re.escape(proposition.name)}\)",
            navigation,
        )
        is not None,
        "research navigation current-frontier link is stale",
    )
    _require(
        f"For {pfrontier}:" in navigation,
        "research navigation current-frontier audit block is stale",
    )
    _require(
        proposition.name in navigation,
        "research navigation audit block omits the canonical proposition",
    )
    _require(
        f"p{frontier}_equation_provenance.md" in navigation,
        "research navigation audit block omits current equation provenance",
    )
    _require(
        current_figure_name in navigation,
        "research navigation audit block omits the canonical current figure",
    )
    _require(
        f"the full {frontier} proposition index" in navigation,
        "research navigation proposition-count wording is stale",
    )
    _require(
        f"**Current frontier:** [{previous}:" not in navigation,
        "research navigation still marks the previous proposition as current",
    )

    reproducibility = (root / "docs" / "reproducibility.md").read_text(encoding="utf-8")
    _require(
        f"The current public theorem frontier is **{pfrontier}**." in reproducibility,
        "reproducibility guide public-frontier declaration is stale",
    )
    _require(
        f"## 5. Focused audit of the current {pfrontier} frontier" in reproducibility,
        "reproducibility guide focused-audit section is stale",
    )
    _require(
        f"The current theorem frontier is **{pfrontier}**." in reproducibility,
        "reproducibility guide current-theorem declaration is stale",
    )
    _require(
        f"docs/{proposition.name}" in reproducibility,
        "reproducibility guide omits the canonical current proposition",
    )
    _require(
        current_figure in reproducibility,
        "reproducibility guide omits the canonical current figure",
    )
    _require(
        f"The current theorem frontier is **{previous}**." not in reproducibility,
        "reproducibility guide still marks the previous proposition as current",
    )

    print(
        f"[frontier] publication surfaces agree with {pfrontier}; "
        f"formal release=v{version}; figure manifest count={figure_count}"
    )


def main() -> None:
    verify_frontier_publication()


if __name__ == "__main__":
    main()
