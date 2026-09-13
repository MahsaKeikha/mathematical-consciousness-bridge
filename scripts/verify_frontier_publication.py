"""Verify that all current-frontier publication surfaces agree."""

from __future__ import annotations

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

    readme = (root / "README.md").read_text(encoding="utf-8")
    summary = re.search(
        r"The research currently contains \*\*(\d+) proposition-level results\*\* "
        r"and \*\*(\d+) equation-driven quantitative figures\*\*\.",
        readme,
    )
    _require(summary is not None, "README is missing the current research-count summary")
    assert summary is not None
    summary_results = int(summary.group(1))
    summary_figures = int(summary.group(2))
    _require(summary_results == frontier, "README summary proposition count is stale")

    status = re.search(
        r"The repository now contains (\d+) proposition-level results\. "
        r"The theorem frontier is P(\d+)\.",
        readme,
    )
    _require(status is not None, "README current scientific status sentence is missing")
    assert status is not None
    _require(
        int(status.group(1)) == frontier and int(status.group(2)) == frontier,
        "README current scientific status sentence disagrees with the proposition tree",
    )

    public_rows = re.findall(
        r"\| Public theorem frontier \| \*\*P(\d+)\*\* \|", readme
    )
    _require(bool(public_rows), "README has no public theorem frontier row")
    _require(
        all(int(value) == frontier for value in public_rows),
        "README contains a stale public theorem frontier row",
    )

    result_rows = re.findall(
        r"\| Proposition-level results \| \*\*(\d+)\*\* \|", readme
    )
    _require(bool(result_rows), "README has no proposition-level result row")
    _require(
        all(int(value) == frontier for value in result_rows),
        "README contains a stale proposition-level result row",
    )

    figure_rows = re.findall(
        r"\| Equation-driven quantitative figures \| \*\*(\d+)\*\* \|",
        readme,
    )
    _require(bool(figure_rows), "README has no equation-driven figure-count row")
    _require(
        all(int(value) == summary_figures for value in figure_rows),
        "README equation-driven figure count disagrees with its research summary",
    )

    citation_frontiers = re.findall(r"Current theorem frontier: \*\*P(\d+)\*\*", readme)
    _require(bool(citation_frontiers), "README citation section has no current frontier")
    _require(
        all(int(value) == frontier for value in citation_frontiers),
        "README citation section contains a stale current frontier",
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
    recommended = navigation.split("## Recommended reading order", 1)[1].split(
        "## Scientific branch map", 1
    )[0]
    _require(
        f"[P{frontier} " in recommended,
        "recommended reading order omits the current frontier",
    )
    branch = navigation.split("## Scientific branch map", 1)[1].split(
        "## Complete proposition index", 1
    )[0]
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
        f"README equation-driven figure count={summary_figures}"
    )


def main() -> None:
    verify_frontier_publication()


if __name__ == "__main__":
    main()
