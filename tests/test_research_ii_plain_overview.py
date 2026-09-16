from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OVERVIEW = ROOT / "website" / "index.html"
README = ROOT / "README.md"
PLAIN = ROOT / "docs" / "research_ii_in_plain_language.md"
IGNORE = ROOT / ".gitignore"
PYTHON_VERSION = ROOT / ".python-version"
READER_CSS = ROOT / "website" / "reader-experience-v2.css"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_overview_explains_research_ii_before_p100_jargon() -> None:
    overview = _text(OVERVIEW)
    plain_start = overview.index('id="research-ii-overview"')
    frontier_start = overview.index('id="p100-frontier"')
    assert plain_start < frontier_start

    plain = overview[plain_start:frontier_start]
    required = (
        "Does the chosen physical description really contain everything needed",
        "Say exactly what information the theory claims is enough",
        "Define the target without building the answer into it",
        "Try to falsify",
        "What Research II has actually established",
        "What it has not established",
        "P19: the core sufficiency theorem",
        "P71-P95: make the test scientifically defensible",
        "P96-P100: keep evidence valid while analysis adapts",
    )
    for token in required:
        assert token in plain


def test_overview_keeps_dense_p100_svg_out_of_first_reader_page() -> None:
    overview = _text(OVERVIEW)
    frontier_start = overview.index('id="p100-frontier"')
    frontier_end = overview.index('id="research-iii-overview"')
    frontier = overview[frontier_start:frontier_end]

    assert "p100_anytime_sequential_eprocess.svg" not in frontier
    assert "P100 plain-language evidence sequence" in frontier
    assert "Open the full P100 theorem figure" in frontier


def test_repository_has_matching_plain_language_research_ii_path() -> None:
    readme = _text(README)
    plain = _text(PLAIN)

    assert "## Research II in plain language" in readme
    assert "docs/research_ii_in_plain_language.md" in readme
    assert "Visual architecture without the dense diagram" in readme
    assert "```mermaid" in readme
    assert "research_architecture.svg" not in readme

    assert "## The testing sequence" in plain
    assert "## What has actually been completed" in plain
    assert "## What Research II does not establish" in plain
    assert "100 proposition-level results through P100" in plain


def test_overview_layout_has_grid_containment_contract() -> None:
    css = _text(READER_CSS)
    assert ".figure-card > *" in css
    assert "min-width: 0;" in css
    assert "overflow-wrap: anywhere;" in css


def test_gitignore_tracks_current_local_artifacts() -> None:
    ignore = _text(IGNORE)
    for token in (
        ".mypy_cache/",
        ".coverage",
        "coverage.xml",
        "htmlcov/",
        ".ipynb_checkpoints/",
        ".env.*",
        "publication-output/",
        "submission-output/",
    ):
        assert token in ignore


def test_python_reference_runtime_is_intentional_not_stale_metadata() -> None:
    assert _text(PYTHON_VERSION).strip() == "3.12.14"
    readme = _text(README)
    assert "exact reproducibility environment" in readme
    assert "Runtime upgrades are treated as compatibility migrations" in readme
