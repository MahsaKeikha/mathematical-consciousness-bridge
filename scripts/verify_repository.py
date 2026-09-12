"""Run lightweight structural checks for repository reproducibility.

This script complements pytest. It verifies that the publication surfaces,
proposition record, core scripts, manifests, and local documentation links are
internally consistent with the current release.

Run with::

    python scripts/verify_repository.py

The command intentionally avoids network access so it can run in CI and in a
fresh local clone.
"""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
CURRENT_VERSION = "0.82.0"
CURRENT_FRONTIER = "P85"

CORE_FILES = (
    "README.md",
    "START_HERE.md",
    "CONTRIBUTING.md",
    "CITATION.cff",
    "CITATION.md",
    "pyproject.toml",
    ".python-version",
    "requirements-figures.txt",
    "requirements-reproducibility.txt",
    "docs/glossary.md",
    "docs/reproducibility.md",
    "docs/research_navigation.md",
    "docs/reader_experience_and_visual_standard.md",
    "docs/figure_caption_and_description_standard.md",
    "docs/theorem_roadmap.md",
    "docs/detailed_proposition_record.md",
    "docs/equation_and_citation_map.md",
    "docs/figure_catalog.md",
    "docs/falsification_program.md",
    "docs/proposition_84_exact_projection_parity_contrast.md",
    "docs/proposition_85_exact_triple_projection_parity_functional.md",
    "docs/p85_equation_provenance.md",
    "website/index.html",
    "website/start-here.html",
    "website/research-map.html",
    "website/visual-atlas.html",
    "website/reader-experience-v2.css",
    "scripts/generate_all_figures.py",
    "scripts/generate_quantitative_atlas.py",
    "scripts/generate_quantum_foundations_atlas.py",
    "scripts/enrich_figure_documentation.py",
    "scripts/reproducibility_audit.py",
)

LINK_SURFACES = (
    "README.md",
    "START_HERE.md",
    "CONTRIBUTING.md",
    "docs/glossary.md",
    "docs/reproducibility.md",
    "docs/research_navigation.md",
    "docs/reader_experience_and_visual_standard.md",
    "docs/figure_caption_and_description_standard.md",
    "docs/theorem_roadmap.md",
)

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def _require_core_files() -> None:
    missing = [path for path in CORE_FILES if not (ROOT / path).is_file()]
    if missing:
        raise RuntimeError(f"missing core repository files: {missing}")


def _verify_release_consistency() -> None:
    pyproject = _read("pyproject.toml")
    citation = _read("CITATION.cff")
    readme = _read("README.md")
    start_here = _read("START_HERE.md")
    navigation = _read("docs/research_navigation.md")
    roadmap = _read("docs/theorem_roadmap.md")
    website = _read("website/index.html")
    website_start = _read("website/start-here.html")
    research_map = _read("website/research-map.html")

    expected_version_markers = (
        ("pyproject.toml", pyproject, f'version = "{CURRENT_VERSION}"'),
        ("CITATION.cff", citation, f"version: {CURRENT_VERSION}"),
        ("README.md", readme, CURRENT_VERSION),
        ("START_HERE.md", start_here, CURRENT_VERSION),
        ("website/index.html", website, CURRENT_VERSION),
        ("website/start-here.html", website_start, CURRENT_VERSION),
    )
    for path, source, marker in expected_version_markers:
        if marker not in source:
            raise RuntimeError(f"{path} does not report release {CURRENT_VERSION}")

    frontier_markers = (
        ("README.md", readme),
        ("START_HERE.md", start_here),
        ("docs/research_navigation.md", navigation),
        ("docs/theorem_roadmap.md", roadmap),
        ("website/index.html", website),
        ("website/start-here.html", website_start),
        ("website/research-map.html", research_map),
    )
    for path, source in frontier_markers:
        if CURRENT_FRONTIER not in source:
            raise RuntimeError(f"{path} does not mention frontier {CURRENT_FRONTIER}")

    stale_frontier_markers = (
        "current P83 frontier",
        "through Proposition 83",
        "Eighty-three results",
        "current P84 frontier",
        "through Proposition 84",
        "Eighty-four results",
    )
    for marker in stale_frontier_markers:
        if marker in website_start or marker in research_map:
            raise RuntimeError(f"reader-facing surface contains stale frontier text: {marker}")

    if "P80**" in navigation or "P80**" in roadmap:
        raise RuntimeError("a reader-facing frontier marker is still pinned to P80")


def _verify_proposition_files() -> None:
    missing: list[int] = []
    duplicates: dict[int, list[str]] = {}
    for number in range(1, 86):
        matches = sorted((ROOT / "docs").glob(f"proposition_{number}_*.md"))
        if not matches:
            missing.append(number)
        elif len(matches) > 1:
            duplicates[number] = [path.name for path in matches]
    if missing:
        raise RuntimeError(f"missing proposition proof files: {missing}")
    if duplicates:
        raise RuntimeError(f"duplicate proposition proof files: {duplicates}")


def _verify_local_markdown_links() -> None:
    failures: list[str] = []
    for relative_path in LINK_SURFACES:
        source_path = ROOT / relative_path
        source = source_path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(source):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_without_anchor = unquote(target.split("#", 1)[0])
            if not target_without_anchor:
                continue
            resolved = (source_path.parent / target_without_anchor).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                failures.append(f"{relative_path}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                failures.append(f"{relative_path}: missing local link target: {target}")
    if failures:
        raise RuntimeError("broken local documentation links:\n" + "\n".join(failures))


def _verify_test_and_source_surfaces() -> None:
    test_files = sorted((ROOT / "tests").glob("test_*.py"))
    source_files = sorted((ROOT / "src" / "consciousness_bridge").glob("*.py"))
    if not test_files:
        raise RuntimeError("no pytest files found")
    if not source_files:
        raise RuntimeError("no package source files found")
    if not (ROOT / ".github" / "workflows" / "test.yml").is_file():
        raise RuntimeError("missing GitHub Actions test workflow")
    if not (ROOT / ".github" / "workflows" / "figures.yml").is_file():
        raise RuntimeError("missing GitHub Actions figure workflow")
    if not (ROOT / ".github" / "workflows" / "reproducibility.yml").is_file():
        raise RuntimeError("missing GitHub Actions reproducibility workflow")
    print(
        f"[verify] discovered {len(test_files)} pytest modules and "
        f"{len(source_files)} package modules"
    )


def main() -> None:
    _require_core_files()
    _verify_release_consistency()
    _verify_proposition_files()
    _verify_local_markdown_links()
    _verify_test_and_source_surfaces()
    print(
        "[verify] repository publication and reproducibility checks passed "
        f"for v{CURRENT_VERSION} / {CURRENT_FRONTIER}"
    )


if __name__ == "__main__":
    main()
