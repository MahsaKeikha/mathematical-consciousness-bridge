"""Verify the public reader experience and high-value research links.

The repository deliberately keeps landing pages concise while preserving a deep
technical audit trail. This verifier protects that contract without requiring
exact prose or freezing the research presentation to one layout.
"""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HTML_HREF = re.compile(r'href=["\']([^"\']+)["\']')


def _frontier() -> int:
    numbers: list[int] = []
    for path in DOCS.glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    if not numbers:
        raise RuntimeError("no proposition files found")
    return max(numbers)


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def _resolve_local_link(source: Path, target: str) -> Path | None:
    target = unquote(target.strip())
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    path_part = target.split("#", 1)[0].split("?", 1)[0]
    if not path_part:
        return None
    return (source.parent / path_part).resolve()


def _check_local_markdown_links(relative: str) -> None:
    source = ROOT / relative
    text = source.read_text(encoding="utf-8")
    missing: list[str] = []
    for target in MARKDOWN_LINK.findall(text):
        resolved = _resolve_local_link(source, target)
        if resolved is not None and not resolved.exists():
            missing.append(target)
    _require(not missing, f"{relative} has broken local links: {missing}")


def _check_local_html_links(relative: str) -> None:
    source = ROOT / relative
    text = source.read_text(encoding="utf-8")
    missing: list[str] = []
    for target in HTML_HREF.findall(text):
        resolved = _resolve_local_link(source, target)
        if resolved is not None and not resolved.exists():
            missing.append(target)
    _require(not missing, f"{relative} has broken local hrefs: {missing}")


def verify_reader_linkability() -> None:
    frontier = _frontier()
    readme = _read("README.md")
    start = _read("START_HERE.md")
    home = _read("website/index.html")
    website_start = _read("website/start-here.html")
    research_map = _read("website/research-map.html")
    navigation = _read("docs/research_navigation.md")
    traceability = _read("docs/research_traceability_index.md")
    publication_standard = _read("docs/publication_page_standard.md")
    p88 = _read("docs/proposition_88_heldout_selected_parity_functional_certification.md")

    # Landing pages are invitations, not archives.
    _require(len(readme.encode("utf-8")) < 25000, "README has grown beyond the reader-first size budget")
    _require(len(start.encode("utf-8")) < 25000, "START_HERE has grown beyond the reader-first size budget")
    _require("Start in one click" in readme, "README lacks a one-click reader gateway")
    _require("Start with the question, not the 88 propositions" in website_start, "website Start Here lost its reader-first opening")
    _require("See the scientific structure without reading 88 proofs in order" in research_map, "research map lost its reader-first orientation")

    # One current frontier should dominate the homepage visually.
    _require(f"P{frontier}" in home, "website home omits the current frontier")
    _require("p88_heldout_selected_parity_functional_certification.svg" in home, "website home omits the current-frontier figure")
    _require("p87_exact_bounded_primitive_quad_projection_parity.svg" not in home, "website home stacks the previous P87 frontier figure")
    _require("p86_exact_minimally_weighted_quad_projection_parity.svg" not in home, "website home stacks the previous P86 frontier figure")

    # High-value reader routes must be available without folder hunting.
    readme_routes = (
        "START_HERE.md",
        "docs/research_architecture.md",
        "docs/research_traceability_index.md",
        "docs/theorem_roadmap.md",
        "docs/figure_catalog.md",
        "docs/reproducibility.md",
    )
    for route in readme_routes:
        _require(route in readme, f"README does not expose reader route {route}")

    for route in (
        "research_traceability_index.md",
        "theorem_roadmap.md",
        "detailed_proposition_record.md",
        "equation_and_citation_map.md",
    ):
        _require(route in navigation, f"research navigation omits deep route {route}")

    # P88 must expose the complete audit trail and the corrected permanent provenance path.
    p88_artifacts = (
        "p88_equation_provenance.md",
        "heldout_selected_parity_functional_certification.py",
        "test_heldout_selected_parity_functional_certification.py",
        "p88_heldout_selected_parity_functional_certification.svg",
        "reproducibility.md",
    )
    for artifact in p88_artifacts:
        _require(artifact in p88 or artifact in traceability, f"P88 audit trail omits {artifact}")

    _require("p88_candidate_equation_provenance.md" not in p88, "P88 still links the obsolete candidate provenance filename")
    _require("What P88 does and does not solve" in p88, "P88 theorem page lacks a scientific-boundary section")
    _require("box-specific" in p88.lower(), "P88 theorem page lost the box-specific boundary")
    _require("independent" in p88.lower(), "P88 theorem page lost the independence requirement")

    # The standard itself should keep future publication changes aligned.
    for token in (
        "Use progressive disclosure",
        "The homepage is not the archive",
        "theorem → provenance → implementation → tests → figure → reproduction",
    ):
        _require(token in publication_standard, f"publication standard lost required principle: {token}")

    # Selected first-reader surfaces must carry explicit interpretation boundaries.
    for name, source in (
        ("README.md", readme),
        ("START_HERE.md", start),
        ("website/index.html", home),
        ("website/start-here.html", website_start),
        ("website/research-map.html", research_map),
    ):
        _require("physical-to-experiential bridge" in source.lower(), f"{name} lost the bridge boundary")

    for relative in (
        "README.md",
        "START_HERE.md",
        "docs/research_navigation.md",
        "docs/research_traceability_index.md",
        "docs/publication_page_standard.md",
        "docs/proposition_88_heldout_selected_parity_functional_certification.md",
    ):
        _check_local_markdown_links(relative)

    for relative in (
        "website/index.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        _check_local_html_links(relative)

    print(f"[reader] reader-first publication and linkability checks pass at P{frontier}")


def main() -> None:
    verify_reader_linkability()


if __name__ == "__main__":
    main()
