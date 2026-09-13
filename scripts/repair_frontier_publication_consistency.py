"""One-time guarded repair for frontier publication consistency."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise RuntimeError(
            f"expected exactly one {label} in {path.relative_to(ROOT)}, "
            f"found {text.count(old)}"
        )
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def repair_readme() -> None:
    path = ROOT / "README.md"
    replacements = (
        (
            "The repository now contains 85 proposition-level results. The theorem frontier is P86.",
            "The repository now contains 86 proposition-level results. The theorem frontier is P86.",
            "stale README current-result sentence",
        ),
        (
            "| Public theorem frontier | **P82** |",
            "| Public theorem frontier | **P86** |",
            "stale README public frontier row",
        ),
        (
            "| Proposition-level results | **81** |",
            "| Proposition-level results | **86** |",
            "stale README proposition count row",
        ),
        (
            "| Equation-driven quantitative figures | **70** |",
            "| Equation-driven quantitative figures | **71** |",
            "stale README equation-driven figure count row",
        ),
        (
            "Current release: **Version 0.82.0**. Current theorem frontier: **P82**.",
            "Current release: **Version 0.82.0**. Current theorem frontier: **P86**.",
            "stale README citation frontier",
        ),
    )
    for old, new, label in replacements:
        _replace_once(path, old, new, label)


def repair_roadmap() -> None:
    path = ROOT / "docs" / "theorem_roadmap.md"
    text = path.read_text(encoding="utf-8")

    p85 = (
        "&\\text{P85: three-event parity functionals test compatibility beyond the "
        "complete P84 pairwise certificate}"
    )
    p86 = (
        "&\\text{P86: minimally weighted four-event parity functionals test "
        "compatibility beyond the complete P85 triple certificate}"
    )
    if p86 not in text:
        needle = p85 + "\n\\end{aligned}"
        replacement = p85 + "\\\\\n&\\Downarrow\\\\\n" + p86 + "\n\\end{aligned}"
        if text.count(needle) != 1:
            raise RuntimeError("could not locate P85 dependency-map terminus")
        text = text.replace(needle, replacement, 1)

    old = (
        "The next computational question is therefore not another cosmetic bound. "
        "A substantive continuation beyond P84 should retain **higher-order "
        "simultaneous dependence among three or more overlapping observables**, or "
        "introduce a demonstrably tighter exact-rational convex or semialgebraic "
        "relaxation while preserving the certified lower-bound direction. Any P85 "
        "candidate should come with a strict witness showing information not already "
        "captured by the complete P84 audit. Statistical extensions remain open as "
        "well, including sharper power analysis and target-view models with residual "
        "dependence, shared bias, temporal drift, or learned measurement pipelines."
    )
    new = (
        "P86 closes the first minimally non-uniform four-event weighting step beyond "
        "the complete P85 triple-functional audit. The next computational question "
        "should not be chosen merely by increasing functional order or proposition "
        "number. A substantive continuation beyond P86 must close a separately "
        "stated mathematical or statistical gap and preserve the certified lower-bound "
        "direction. Natural candidates include an exact-rational support-function or "
        "convex relaxation of the full parity-coordinate image, with a certificate not "
        "already implied by P86, or an observable-specific finite-sample rejection "
        "theorem that propagates uncertainty through a selected P86 score rather than "
        "only through the global sixteen-cell radius. Target-view models with residual "
        "dependence, shared bias, temporal drift, or learned measurement pipelines also "
        "remain open."
    )
    if old not in text:
        raise RuntimeError("could not locate stale pre-P85 roadmap frontier paragraph")
    text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")


def repair_navigation() -> None:
    path = ROOT / "docs" / "research_navigation.md"
    text = path.read_text(encoding="utf-8")
    start = text.index("## Recommended reading order")
    end = text.index("## Scientific branch map", start)
    prefix, section, suffix = text[:start], text[start:end], text[end:]

    p86_line = (
        "[P86 exact minimally weighted four-event projection-parity functional]"
        "(proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md)"
    )
    if p86_line not in section:
        lines = section.splitlines()
        p85_index = next(
            index
            for index, line in enumerate(lines)
            if "[P85 exact three-event projection-parity functional]" in line
        )
        lines.insert(
            p85_index + 1,
            "0. " + p86_line
            + " for the minimally non-uniform four-event shared-parameter audit, "
            "10,560 exact `{1,1,1,2}` weighted functionals, P86 >= P85 dominance, "
            "and the strict `L85 = 0 < L86 = 1/192` witness.",
        )
        number = 0
        renumbered: list[str] = []
        for line in lines:
            if re.match(r"^\d+\. ", line):
                number += 1
                line = re.sub(r"^\d+\. ", f"{number}. ", line, count=1)
            renumbered.append(line)
        section = "\n".join(renumbered) + ("\n" if section.endswith("\n") else "")

    branch_start = suffix.index("## Scientific branch map")
    branch_end = suffix.index("## Complete proposition index", branch_start)
    branch = suffix[branch_start:branch_end]
    p86_row = (
        "| Minimally weighted four-event projection-parity functional separation | P86 | "
        "Adds 10,560 exact `{1,1,1,2}` weighted four-event shared-parameter functionals "
        "beyond the complete P85 triple-functional certificate | "
        "[P86](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md) |"
    )
    if "| Minimally weighted four-event projection-parity functional separation | P86 |" not in branch:
        p85_row_pattern = re.compile(
            r"^\| Three-event projection-parity functional separation \| P85 \|.*$",
            re.MULTILINE,
        )
        match = p85_row_pattern.search(branch)
        if match is None:
            raise RuntimeError("could not locate P85 branch-map row")
        branch = branch[: match.end()] + "\n" + p86_row + branch[match.end() :]
        suffix = suffix[:branch_start] + branch + suffix[branch_end:]

    path.write_text(prefix + section + suffix, encoding="utf-8")


def write_permanent_checker() -> None:
    path = ROOT / "scripts" / "verify_frontier_publication.py"
    path.write_text(
        '''"""Verify that all current-frontier publication surfaces agree."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _frontier(root: Path) -> int:
    values: list[int] = []
    for path in (root / "docs").glob("proposition_*.md"):
        match = re.match(r"proposition_(\\d+)_", path.name)
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
        r"The research currently contains \\*\\*(\\d+) proposition-level results\\*\\* "
        r"and \\*\\*(\\d+) equation-driven quantitative figures\\*\\*\\.",
        readme,
    )
    _require(summary is not None, "README is missing the current research-count summary")
    assert summary is not None
    summary_results = int(summary.group(1))
    summary_figures = int(summary.group(2))
    _require(summary_results == frontier, "README summary proposition count is stale")

    status = re.search(
        r"The repository now contains (\\d+) proposition-level results\\. "
        r"The theorem frontier is P(\\d+)\\.",
        readme,
    )
    _require(status is not None, "README current scientific status sentence is missing")
    assert status is not None
    _require(
        int(status.group(1)) == frontier and int(status.group(2)) == frontier,
        "README current scientific status sentence disagrees with the proposition tree",
    )

    public_rows = re.findall(
        r"\\| Public theorem frontier \\| \\*\\*P(\\d+)\\*\\* \\|", readme
    )
    _require(bool(public_rows), "README has no public theorem frontier row")
    _require(
        all(int(value) == frontier for value in public_rows),
        "README contains a stale public theorem frontier row",
    )

    result_rows = re.findall(
        r"\\| Proposition-level results \\| \\*\\*(\\d+)\\*\\* \\|", readme
    )
    _require(bool(result_rows), "README has no proposition-level result row")
    _require(
        all(int(value) == frontier for value in result_rows),
        "README contains a stale proposition-level result row",
    )

    figure_rows = re.findall(
        r"\\| Equation-driven quantitative figures \\| \\*\\*(\\d+)\\*\\* \\|",
        readme,
    )
    _require(bool(figure_rows), "README has no equation-driven figure-count row")
    _require(
        all(int(value) == summary_figures for value in figure_rows),
        "README equation-driven figure count disagrees with its research summary",
    )

    citation_frontiers = re.findall(r"Current theorem frontier: \\*\\*P(\\d+)\\*\\*", readme)
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
        f"\\\\text{{{pfrontier}:" in dependency,
        "theorem roadmap dependency map omits the current frontier",
    )
    _require(
        f"## After {pfrontier}" in roadmap,
        "theorem roadmap lacks a current-frontier future-work boundary",
    )
    for value in re.findall(r"Any P(\\d+) candidate", roadmap):
        _require(
            int(value) > frontier,
            f"theorem roadmap still describes closed P{value} as a future candidate",
        )
    for value in re.findall(r"continuation beyond P(\\d+)", roadmap):
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
        re.search(rf"^\\| [^|]+ \\| P{frontier} \\|", branch, re.MULTILINE)
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
''',
        encoding="utf-8",
    )


def write_permanent_test() -> None:
    path = ROOT / "tests" / "test_frontier_publication_consistency.py"
    path.write_text(
        '''import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_current_frontier_publication_surfaces_are_consistent() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify_frontier_publication.py")],
        cwd=ROOT,
        check=True,
    )
''',
        encoding="utf-8",
    )


def repair_repository_verifier() -> None:
    path = ROOT / "scripts" / "verify_repository.py"
    text = path.read_text(encoding="utf-8")
    import_line = "from verify_frontier_publication import verify_frontier_publication\n"
    if import_line not in text:
        needle = "from urllib.parse import unquote\n"
        if text.count(needle) != 1:
            raise RuntimeError("could not locate verifier import anchor")
        text = text.replace(needle, needle + "\n" + import_line, 1)

    core = '    "scripts/verify_frontier_publication.py",\n'
    if core not in text:
        needle = '    "scripts/reproducibility_audit.py",\n'
        if text.count(needle) != 1:
            raise RuntimeError("could not locate verifier core-file anchor")
        text = text.replace(needle, needle + core, 1)

    call = "    verify_frontier_publication(ROOT)\n"
    if call not in text:
        needle = "    _verify_release_consistency()\n"
        if text.count(needle) != 1:
            raise RuntimeError("could not locate verifier main anchor")
        text = text.replace(needle, needle + call, 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    repair_readme()
    repair_roadmap()
    repair_navigation()
    write_permanent_checker()
    write_permanent_test()
    repair_repository_verifier()
    print("frontier publication consistency repair applied")


if __name__ == "__main__":
    main()
