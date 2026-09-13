from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START = ROOT / "START_HERE.md"
INDEX = ROOT / "website/index.html"
APP = ROOT / "website/app.js"


def test_public_reader_documents_keep_progressive_disclosure():
    assert len(README.read_text(encoding="utf-8")) < 12_000
    assert len(START.read_text(encoding="utf-8")) < 9_000


def test_readme_is_gateway_not_monolithic_paper():
    text = README.read_text(encoding="utf-8")
    for target in (
        "START_HERE.md",
        "docs/research_map.md",
        "docs/figure_catalog.md",
        "docs/detailed_proposition_record.md",
        "docs/reproducibility.md",
    ):
        assert target in text
    assert "The current public theorem frontier is **P88**" in text


def test_start_here_exposes_current_identity_without_forcing_theorem_sequence():
    text = START.read_text(encoding="utf-8")
    assert "88" in text
    assert "P88" in text
    assert "v0.82.0" in text
    assert "You do not need to read" in text


def test_homepage_is_visual_gateway_with_current_status():
    text = INDEX.read_text(encoding="utf-8")
    assert "Explore all 88 results" in text
    assert "Current theorem frontier · P88" in text
    assert 'href="start-here.html"' in text
    assert 'href="research-map.html"' in text
    assert 'href="visual-atlas.html"' in text
    assert text.count('id="p88-frontier"') == 1


def test_navigation_script_exposes_reader_routes():
    text = APP.read_text(encoding="utf-8")
    for token in (
        "Start Here",
        "Research II",
        "Research III",
        "measurement-science.html",
        "visual-atlas.html",
    ):
        assert token in text
