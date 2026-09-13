"""Run structural checks for repository reproducibility and publication consistency.

This verifier complements pytest. It checks the reader-facing status, proposition
record, local links, exact figure publication record, core scripts, and CI surfaces
without requiring network access.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

from verify_frontier_publication import verify_frontier_publication

ROOT = Path(__file__).resolve().parents[1]
CURRENT_VERSION = "0.82.0"
CURRENT_FRONTIER = "P88"
CURRENT_FRONTIER_FIGURE = "p88_exact_radius3_bounded_primitive_quad_projection_parity.svg"

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
    "docs/claim_evidence_standard.md",
    "docs/claim_source_matrix.md",
    "docs/reference_audit.md",
    "docs/literature_map.md",
    "docs/theorem_roadmap.md",
    "docs/detailed_proposition_record.md",
    "docs/equation_and_citation_map.md",
    "docs/figure_catalog.md",
    "docs/falsification_program.md",
    "docs/figures/README.md",
    "docs/figures/p84_exact_joint_projection_parity_contrast.svg",
    "docs/figures/p85_exact_triple_projection_parity_functional.svg",
    "docs/figures/p86_exact_minimally_weighted_quad_projection_parity.svg",
    "docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg",
    "docs/figures/p88_exact_radius3_bounded_primitive_quad_projection_parity.svg",
    "docs/proposition_84_exact_projection_parity_contrast.md",
    "docs/proposition_85_exact_triple_projection_parity_functional.md",
    "docs/p85_equation_provenance.md",
    "docs/proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md",
    "docs/p86_equation_provenance.md",
    "docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md",
    "docs/p87_equation_provenance.md",
    "docs/proposition_88_exact_radius3_bounded_primitive_quad_projection_parity_functional.md",
    "docs/p88_equation_provenance.md",
    "figures/README.md",
    "figures/CURRENT_FRONTIER.md",
    "figures/manifest.json",
    "website/index.html",
    "website/plain-language.html",
    "website/start-here.html",
    "website/research-map.html",
    "website/visual-atlas.html",
    "website/sources.html",
    "website/reader-experience-v2.css",
    "scripts/generate_all_figures.py",
    "scripts/generate_quantitative_atlas.py",
    "scripts/generate_quantum_foundations_atlas.py",
    "scripts/enrich_figure_documentation.py",
    "scripts/sync_figure_publication.py",
    "scripts/prepare_website.py",
    "scripts/reproducibility_audit.py",
    "scripts/verify_frontier_publication.py",
    "tests/test_figure_publication_sync.py",
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
    "docs/claim_evidence_standard.md",
    "docs/claim_source_matrix.md",
    "docs/reference_audit.md",
    "docs/literature_map.md",
    "docs/theorem_roadmap.md",
    "figures/README.md",
    "figures/CURRENT_FRONTIER.md",
)

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

# Earlier frontiers may remain as historical sections. Only stale *current* status
# language is rejected.
STALE_READER_FRONTIER_MARKERS = (
    "87-result theorem program and current P87 frontier",
    "Current theorem frontier · P87",
    "Current exact frontier · P87",
    "<strong>P87</strong><span>current theorem frontier</span>",
    "86-result theorem program and current P86 frontier",
    "Current theorem frontier · P86",
    "Current exact frontier · P86",
    "<strong>P86</strong><span>current theorem frontier</span>",
    "85-result theorem program and current P85 frontier",
    "Current frontier · P85",
    "<strong>P85</strong><span>current theorem frontier</span>",
    "<strong>P84</strong><span>current theorem frontier</span>",
)


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def _require_core_files() -> None:
    missing = [path for path in CORE_FILES if not (ROOT / path).is_file()]
    if missing:
        raise RuntimeError(f"missing core repository files: {missing}")


def _verify_reader_frontier_freshness() -> None:
    offenders: dict[str, list[str]] = {}
    for path in sorted((ROOT / "website").glob("*.html")):
        source = path.read_text(encoding="utf-8")
        hits = [marker for marker in STALE_READER_FRONTIER_MARKERS if marker in source]
        if hits:
            offenders[path.name] = hits
    if offenders:
        raise RuntimeError(f"reader-facing website contains stale current-frontier text: {offenders}")


def _verify_release_consistency() -> None:
    pyproject = _read("pyproject.toml")
    citation = _read("CITATION.cff")
    readme = _read("README.md")
    start_here = _read("START_HERE.md")
    navigation = _read("docs/research_navigation.md")
    roadmap = _read("docs/theorem_roadmap.md")
    figure_readme = _read("docs/figures/README.md")
    figure_gateway = _read("figures/README.md")
    figure_frontier = _read("figures/CURRENT_FRONTIER.md")
    website = _read("website/index.html")
    website_plain = _read("website/plain-language.html")
    website_start = _read("website/start-here.html")
    research_map = _read("website/research-map.html")
    visual_atlas = _read("website/visual-atlas.html")
    sources_page = _read("website/sources.html")

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
        ("docs/figures/README.md", figure_readme),
        ("figures/README.md", figure_gateway),
        ("figures/CURRENT_FRONTIER.md", figure_frontier),
        ("website/index.html", website),
        ("website/plain-language.html", website_plain),
        ("website/start-here.html", website_start),
        ("website/research-map.html", research_map),
        ("website/visual-atlas.html", visual_atlas),
        ("website/sources.html", sources_page),
    )
    for path, source in frontier_markers:
        if CURRENT_FRONTIER not in source:
            raise RuntimeError(f"{path} does not mention frontier {CURRENT_FRONTIER}")

    if (
        "10.1016/j.chaos.2015.03.014" not in sources_page
        or "arXiv:1401.1219" not in sources_page
    ):
        raise RuntimeError("sources page does not expose the verified Tegmark research-origin citation")
    if (
        "important conceptual starting point" not in sources_page
        or "distinct mathematical framework" not in sources_page
    ):
        raise RuntimeError("sources page does not expose the collegial Tegmark research-origin context")

    scholarly_origin_files = (
        "website/start-here.html",
        "website/sources.html",
        "docs/claim_evidence_standard.md",
        "docs/literature_map.md",
        "docs/reference_audit.md",
        "docs/claim_source_matrix.md",
    )
    defensive_origin_phrases = (
        "this origin citation does not make Tegmark's paper evidence",
        "not evidence for the repository's later original propositions",
        "not evidential support for later repository-original propositions",
    )
    for relative_path in scholarly_origin_files:
        source = _read(relative_path)
        hits = [phrase for phrase in defensive_origin_phrases if phrase in source]
        if hits:
            raise RuntimeError(f"{relative_path} contains defensive research-origin wording: {hits}")

    _verify_reader_frontier_freshness()


def _verify_proposition_files() -> None:
    missing: list[int] = []
    duplicates: dict[int, list[str]] = {}
    for number in range(1, 89):
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


def _verify_figure_publication_sync() -> None:
    manifest = json.loads(_read("figures/manifest.json"))
    if manifest.get("current_frontier") != CURRENT_FRONTIER:
        raise RuntimeError("figure manifest does not report the current theorem frontier")
    current_figure = str(manifest.get("current_frontier_figure", ""))
    if not current_figure.endswith(CURRENT_FRONTIER_FIGURE):
        raise RuntimeError("figure manifest does not point to the canonical P88 SVG")

    canonical = sorted((ROOT / "docs" / "figures").rglob("*.svg"))
    records = manifest.get("figures")
    if not isinstance(records, list):
        raise TypeError("figure manifest does not contain a figure record list")
    declared_paths = {
        str(record.get("path")) for record in records if isinstance(record, dict)
    }
    actual_paths = {path.relative_to(ROOT).as_posix() for path in canonical}
    if manifest.get("figure_count") != len(canonical) or declared_paths != actual_paths:
        raise RuntimeError("complete figure manifest is not aligned with docs/figures")

    visual_atlas = _read("website/visual-atlas.html")
    p88 = visual_atlas.index('id="p88-frontier"')
    p87 = visual_atlas.index('id="p87-frontier"')
    p86 = visual_atlas.index('id="p86-frontier"')
    if not (p88 < p87 < p86):
        raise RuntimeError("Visual Atlas does not lead with P88 before historical P87/P86")
    if "Current theorem frontier · P87" in visual_atlas:
        raise RuntimeError("Visual Atlas still labels P87 as current")

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "sync_figure_publication.py"), "--check"],
        cwd=ROOT,
        check=True,
    )


def _verify_test_and_source_surfaces() -> None:
    test_files = sorted((ROOT / "tests").glob("test_*.py"))
    source_files = sorted((ROOT / "src" / "consciousness_bridge").glob("*.py"))
    if not test_files:
        raise RuntimeError("no pytest files found")
    if not source_files:
        raise RuntimeError("no package source files found")
    required_workflows = (
        "test.yml",
        "figures.yml",
        "reproducibility.yml",
        "pages.yml",
    )
    missing_workflows = [
        name
        for name in required_workflows
        if not (ROOT / ".github" / "workflows" / name).is_file()
    ]
    if missing_workflows:
        raise RuntimeError(f"missing GitHub Actions workflows: {missing_workflows}")
    print(
        f"[verify] discovered {len(test_files)} pytest modules and "
        f"{len(source_files)} package modules"
    )


def main() -> None:
    _require_core_files()
    _verify_release_consistency()
    verify_frontier_publication(ROOT)
    _verify_proposition_files()
    _verify_local_markdown_links()
    _verify_figure_publication_sync()
    _verify_test_and_source_surfaces()
    print(
        "[verify] repository publication and reproducibility checks passed "
        f"for v{CURRENT_VERSION} / {CURRENT_FRONTIER}"
    )


if __name__ == "__main__":
    main()
