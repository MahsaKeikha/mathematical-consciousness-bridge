from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
FIGURE = ROOT / "docs" / "figures" / "theorem_roadmap.svg"
CATALOG = ROOT / "docs" / "figure_catalog.md"


def test_readme_roadmap_caption_matches_displayed_scope_and_frontier():
    text = README.read_text(encoding="utf-8")
    assert "P1 through P80 with explicit dependency branches" in text
    assert "Figure 3 below displays the P1-P31 foundational portion" in text
    assert "Figure 3. Theorem dependency map for P1-P31." in text
    assert "arrows show actual mathematical and scientific prerequisites" in text
    assert "An absent arrow means no dependency is being asserted." in text


def test_theorem_roadmap_embedded_description_explains_arrow_semantics():
    text = FIGURE.read_text(encoding="utf-8")
    assert "the theorem roadmap for Propositions 1 through 31" in text
    assert "follow the arrows, not just the page order" in text
    assert "An absent arrow means that the figure is not asserting a prerequisite." in text
    assert "Later P61-P70 and P71-P80 are separate continuations" in text


def test_figure_catalog_preserves_specific_roadmap_description():
    text = CATALOG.read_text(encoding="utf-8")
    assert "Theorem dependency map for P1-P31" in text
    assert "the arrow topology records dependency structure" in text
