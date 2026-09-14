"""Run lightweight structural checks for repository reproducibility.

This script complements pytest. It verifies that the publication surfaces,
proposition record, figure publication record, core scripts, manifests, and
local documentation links are internally consistent with the current release.

Run with::

    python scripts/verify_repository.py

The command intentionally avoids network access so it can run in CI and in a
fresh local clone.
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
CURRENT_FRONTIER = "P90"

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
    "docs/figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg",
    "docs/figures/p89_complete_linear_parity_duality.svg",
    "docs/figures/p90_exact_nonlinear_rank_one_separation.svg",
    "docs/proposition_84_exact_projection_parity_contrast.md",
    "docs/proposition_85_exact_triple_projection_parity_functional.md",
    "docs/p85_equation_provenance.md",
    "docs/proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md",
    "docs/p86_equation_provenance.md",
    "docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md",
    "docs/p87_equation_provenance.md",
    "docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md",
    "docs/p88_equation_provenance.md",
    "docs/proposition_89_complete_linear_parity_duality.md",
    "docs/p89_equation_provenance.md",
    "docs/proposition_90_exact_nonlinear_rank_one_separation.md",
    "docs/p90_equation_provenance.md",
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
    "scripts/promote_p89_public_frontier.py",
    "scripts/promote_p90_public_frontier.py",
    "scripts/synchronize_p89_reader_frontier_phrases.py",
    "scripts/prepare_website.py",
    "scripts/reproducibility_audit.py",
    "scripts/verify_frontier_publication.py",
    "tests/test_figure_publication_sync.py",
    "tests/test_exact_nonlinear_rank_one_separation.py",
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

STALE_READER_FRONTIER_MARKERS = (
    "Current theorem frontier · P88",
    "current P88 frontier",
    "<strong>P88</strong><span>current theorem frontier</span>",
    "87-result theorem program and current P87 frontier",
    "Current theorem frontier · P87",
    "<strong>87</strong><span>proposition-level results</span>",
    "<strong>P87</strong><span>current theorem frontier</span>",
    "current P87 frontier",
    "actual P87 research frontier",
    "What the 87 results are doing",
    "shows how all 87 results connect",
    "through Proposition 87",
    "Eighty-seven results",
    "The 87 propositions by scientific role",
    "complete 87-result dependency structure",
    "You do not need to read 87 proofs in order",
    "86-result theorem program and current P86 frontier",
    "Current theorem frontier · P86",
    "<strong>86</strong><span>proposition-level results</span>",
    "<strong>P86</strong><span>current theorem frontier</span>",
    "current P86 frontier",
    "actual P86 research frontier",
    "What the 86 results are doing",
    "shows how all 86 results connect",
    "through Proposition 86",
    "Eighty-six results",
    "The 86 propositions by scientific role",
    "complete 86-result dependency structure",
    "You do not need to read 86 proofs in order",
    "85-result theorem program and current P86 frontier",
    "<h2>P78-P85 progressively tighten global separation from the declared continuous model family</h2>",
    "Current frontier · P85",
    "<strong>85</strong><span>proposition-level results</span>",
    "<strong>P85</strong><span>current theorem frontier</span>",
    "current P85 frontier",
    "actual P85 research frontier",
    "What the 85 results are doing",
    "shows how all 85 results connect",
    "through Proposition 85",
    "Eighty-five results",
    "Open all 85 results",
    "The 85 propositions by scientific role",
    "complete 85-result dependency structure",
    "You do not need to read 85 proofs in order",
    "<strong>84</strong><span>proposition-level results</span>",
    "<strong>P84</strong><span>current theorem frontier</span>",
    "current P84 frontier",
    "actual P84 research frontier",
    "What the 84 results are doing",
    "shows how all 84 results connect",
    "through Proposition 84",
    "Eighty-four results",
    "Open all 84 results",
    "The 84 propositions by scientific role",
    "complete 84-result dependency structure",
    "You do not need to read 84 proofs in order",
)


def _assert_required_files() -> None:
    missing = [path for path in CORE_FILES if not (ROOT / path).is_file()]
    if missing:
        raise RuntimeError(f"missing required repository files: {missing}")


def _assert_version_consistency() -> None:
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    website = (ROOT / "website" / "index.html").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    expected_cff = f'version: "{CURRENT_VERSION}"'
    if expected_cff not in cff:
        raise RuntimeError("CITATION.cff version does not match CURRENT_VERSION")
    expected_pyproject = f'version = "{CURRENT_VERSION}"'
    if expected_pyproject not in pyproject:
        raise RuntimeError("pyproject.toml version does not match CURRENT_VERSION")
    if f"v{CURRENT_VERSION}" not in website:
        raise RuntimeError("website version does not match CURRENT_VERSION")
    if f"v{CURRENT_VERSION}" not in readme:
        raise RuntimeError("README version does not match CURRENT_VERSION")


def _assert_no_stale_reader_frontier() -> None:
    surfaces = (
        ROOT / "README.md",
        ROOT / "START_HERE.md",
        ROOT / "docs" / "glossary.md",
        ROOT / "docs" / "research_navigation.md",
        ROOT / "docs" / "research_map.md",
        ROOT / "docs" / "theorem_roadmap.md",
        ROOT / "website" / "index.html",
        ROOT / "website" / "plain-language.html",
        ROOT / "website" / "start-here.html",
        ROOT / "website" / "research-map.html",
        ROOT / "website" / "research-lineage.html",
        ROOT / "website" / "visual-atlas.html",
    )
    stale: list[str] = []
    for path in surfaces:
        text = path.read_text(encoding="utf-8")
        for marker in STALE_READER_FRONTIER_MARKERS:
            if marker in text:
                stale.append(f"{path.relative_to(ROOT)} -> {marker}")
    if stale:
        raise RuntimeError(
            "stale reader-facing frontier markers remain:\n" + "\n".join(stale)
        )


def _assert_citation_integrity() -> None:
    citation = (ROOT / "CITATION.md").read_text(encoding="utf-8")
    if "Current documented theorem frontier: P90" not in citation:
        raise RuntimeError("CITATION.md does not declare P90 as the current theorem frontier")
    if "P90" not in (ROOT / "CITATION.cff").read_text(encoding="utf-8"):
        raise RuntimeError("CITATION.cff does not mention P90")


def _assert_detailed_proposition_record() -> None:
    record = (ROOT / "docs" / "detailed_proposition_record.md").read_text(
        encoding="utf-8"
    )
    covered: set[int] = set()
    for match in re.finditer(r"\bP(\d+)(?:\s*(?:-|to|through)\s*P?(\d+))?\b", record):
        start = int(match.group(1))
        end = int(match.group(2) or start)
        if end < start:
            start, end = end, start
        covered.update(range(start, end + 1))
    missing = [number for number in range(1, 91) if number not in covered]
    if missing:
        raise RuntimeError(
            f"detailed proposition record is missing proposition references: {missing}"
        )


def _assert_figure_manifest() -> None:
    manifest = json.loads((ROOT / "figures" / "manifest.json").read_text(encoding="utf-8"))
    current = manifest.get("current_frontier")
    if current != CURRENT_FRONTIER:
        raise RuntimeError(
            f"figure manifest current frontier is {current!r}, expected {CURRENT_FRONTIER!r}"
        )
    figure_path = manifest.get("current_frontier_figure")
    if not isinstance(figure_path, str):
        raise TypeError("figure manifest current_frontier_figure is missing")
    if not figure_path.endswith("p90_exact_nonlinear_rank_one_separation.svg"):
        raise RuntimeError("figure manifest does not point to the canonical P90 SVG")
    figures = manifest.get("figures")
    if not isinstance(figures, list) or len(figures) != 148:
        raise RuntimeError("figure manifest does not contain the canonical 148 figures")


def _assert_visual_atlas_order() -> None:
    visual_atlas = (ROOT / "website" / "visual-atlas.html").read_text(encoding="utf-8")
    p90 = visual_atlas.index('id="p90-frontier"')
    p89 = visual_atlas.index('id="p89-frontier"')
    p88 = visual_atlas.index('id="p88-frontier"')
    if not (p90 < p89 < p88):
        raise RuntimeError("Visual Atlas does not lead with the current P90 figure")


def _assert_no_policy_punctuation() -> None:
    targets = list((ROOT / "docs").rglob("*.md"))
    targets.extend((ROOT / "website").rglob("*.html"))
    targets.extend((ROOT / "docs" / "figures").rglob("*.svg"))
    targets.extend((ROOT / "figures").rglob("*.md"))
    targets.extend([ROOT / "README.md", ROOT / "START_HERE.md", ROOT / "CITATION.md"])
    violations: list[str] = []
    for path in targets:
        text = path.read_text(encoding="utf-8")
        if "–" in text or "—" in text:
            violations.append(str(path.relative_to(ROOT)))
    if violations:
        raise RuntimeError(
            "reader-facing punctuation policy violation in: " + ", ".join(violations)
        )


def _assert_local_markdown_links() -> None:
    failures: list[str] = []
    for relative in LINK_SURFACES:
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            raw_target = match.group(1).strip()
            if not raw_target or raw_target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = raw_target.split("#", 1)[0]
            if not target:
                continue
            decoded = unquote(target)
            candidate = (path.parent / decoded).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                failures.append(f"{relative} -> {raw_target} escapes repository root")
                continue
            if not candidate.exists():
                failures.append(f"{relative} -> {raw_target}")
    if failures:
        raise RuntimeError(
            "broken local Markdown links:\n" + "\n".join(failures)
        )


def _assert_python_sources_compile() -> None:
    sources = list((ROOT / "src").rglob("*.py"))
    sources.extend((ROOT / "scripts").glob("*.py"))
    sources.extend((ROOT / "tests").glob("*.py"))
    failures: list[str] = []
    for path in sources:
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", str(path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            failures.append(f"{path.relative_to(ROOT)}: {result.stderr.strip()}")
    if failures:
        raise RuntimeError("Python compilation failures:\n" + "\n".join(failures))


def main() -> None:
    _assert_required_files()
    _assert_version_consistency()
    _assert_no_stale_reader_frontier()
    _assert_citation_integrity()
    _assert_detailed_proposition_record()
    _assert_figure_manifest()
    _assert_visual_atlas_order()
    _assert_no_policy_punctuation()
    _assert_local_markdown_links()
    _assert_python_sources_compile()
    verify_frontier_publication(ROOT)
    print(
        f"[verify] repository publication and reproducibility checks passed for "
        f"v{CURRENT_VERSION} / {CURRENT_FRONTIER}"
    )


if __name__ == "__main__":
    main()
