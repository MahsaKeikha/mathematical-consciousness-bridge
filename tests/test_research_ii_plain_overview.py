from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OVERVIEW = ROOT / "website" / "index.html"
APP = ROOT / "website" / "app.js"
README = ROOT / "README.md"
PLAIN = ROOT / "docs" / "research_ii_in_plain_language.md"
IGNORE = ROOT / ".gitignore"
PYTHON_VERSION = ROOT / ".python-version"
READER_CSS = ROOT / "website" / "reader-experience-v2.css"
RESEARCH_II_VISUAL = ROOT / "website" / "research-ii-sufficiency-falsification-overview.svg"
P100_VISUAL = ROOT / "website" / "p100-anytime-valid-sequence-overview.svg"


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


def test_overview_collapses_dense_p100_svg_behind_technical_disclosure() -> None:
    overview = _text(OVERVIEW)
    frontier_start = overview.index('id="p100-frontier"')
    frontier_end = overview.index('id="research-iii-overview"')
    frontier = overview[frontier_start:frontier_end]

    assert "P100 plain-language evidence sequence" in frontier
    assert '<details class="technical-figure-details">' in frontier
    assert "Open the full technical P100 theorem figure" in frontier
    assert "p100_anytime_sequential_eprocess.svg" in frontier
    assert frontier.index("P100 plain-language evidence sequence") < frontier.index(
        "p100_anytime_sequential_eprocess.svg"
    )


def test_overview_runtime_adds_reader_friendly_research_ii_visuals() -> None:
    app = _text(APP)
    assert "function addResearchTwoVisuals()" in app
    assert "research-ii-sufficiency-falsification-overview.svg" in app
    assert "Research II testing architecture" in app
    assert "p100-anytime-valid-sequence-overview.svg" in app
    assert "P100 sequential evidence architecture" in app
    assert "addResearchTwoVisuals();" in app
    assert "current physical-to-experiential test architecture through P100" in app
    assert "Bridge-test program through P100" in app


def test_research_ii_visual_is_compact_self_explanatory_and_bounded() -> None:
    visual = _text(RESEARCH_II_VISUAL)
    for token in (
        "Research II sufficiency test in four steps",
        "Descriptor D",
        "Independent target Y",
        "Equivalent cases",
        "D(x₁) = D(x₂)",
        "Y(x₁) ?= Y(x₂)",
        "NO TARGET SEPARATION",
        "TARGET DIFFERS",
        "Survives this test",
        "Sufficiency fails",
        "Richer physical descriptions may remain possible",
    ):
        assert token in visual
    assert "<desc" in visual
    assert 'viewBox="0 0 1200 620"' in visual
    assert 'width="1600" height="920"' not in visual


def test_research_ii_visual_has_attached_flow_arrows() -> None:
    visual = _text(RESEARCH_II_VISUAL)

    for segment in (
        'x1="290" y1="258" x2="344" y2="258"',
        'x1="586" y1="258" x2="640" y2="258"',
        'x1="882" y1="258" x2="936" y2="258"',
        'M1044 365 L1044 405 L753 405 L753 442',
        'M1044 405 L1044 442',
    ):
        assert segment in visual


def test_p100_visual_separates_reader_overview_from_technical_theorem_art() -> None:
    visual = _text(P100_VISUAL)
    for token in (
        "Anytime-valid evidence across fresh certification rounds",
        "PAST INFORMATION",
        "FREEZE THE PLAN",
        "FRESH DATA",
        "ROUND-LEVEL EVIDENCE",
        "Fₜ = (1 - ηₜ) + ηₜEₜ",
        "Mₜ = ∏ Fₛ",
        "Mₜ ≥ 1 / α",
        "EXACT 95% CHECKPOINT",
        "M₂ = 45.5625",
        "SCIENTIFIC BOUNDARY",
    ):
        assert token in visual
    assert "<desc" in visual
    assert 'viewBox="0 0 1600 920"' in visual


def test_repository_has_matching_plain_language_research_ii_path() -> None:
    readme = _text(README)
    plain = _text(PLAIN)

    assert "## Research II in plain language" in readme
    assert "docs/research_ii_in_plain_language.md" in readme
    assert "Visual architecture without the dense diagram" in readme
    assert "```mermaid" in readme
    assert "research_architecture.svg" not in readme
    assert "**Figure 1. Scientific architecture of the project.**" in readme

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
