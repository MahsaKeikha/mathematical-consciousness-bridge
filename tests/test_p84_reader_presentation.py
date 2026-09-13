from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def _section(html: str, section_id: str) -> str:
    start = html.index(f'<section id="{section_id}"')
    end = html.index("</section>", start) + len("</section>")
    return html[start:end]


def test_p84_homepage_uses_figure_first_publication_layout() -> None:
    section = _section(_read("website/index.html"), "p84-frontier")
    assert 'class="theorem-frontier"' in section
    assert 'class="theorem-figure-shell"' in section
    assert 'class="frontier-summary-grid"' in section
    assert section.count('class="frontier-summary-card"') == 3
    assert 'class="two-col"' not in section
    assert '<aside class="card">' not in section
    assert "two tests can pass separately and still fail together" in section
    assert "220 coupled contrasts" in section
    assert "L83 = 0" in section
    assert "L84 = 1/32" in section
    assert "does not close the physical-to-experiential bridge" in section


def test_p84_visual_atlas_uses_same_nonoverlapping_reading_order() -> None:
    section = _section(_read("website/visual-atlas.html"), "p84-frontier")
    assert 'class="theorem-figure-shell"' in section
    assert 'class="frontier-summary-grid"' in section
    assert section.count('class="frontier-summary-card"') == 3
    assert 'class="two-col"' not in section
    assert "Read the left panel" in section
    assert "Read the middle panel" in section
    assert "Read the right panel" in section


def test_shared_css_prevents_wide_figures_from_overflowing_grid_columns() -> None:
    css = _read("website/styles.css")
    required = (
        "/* Publication-safe theorem figures */",
        ".two-col > *",
        ".figure-card > *",
        "min-width: 0;",
        ".theorem-figure-shell",
        ".theorem-figure-shell img",
        "max-width: 100%;",
        ".frontier-summary-grid",
    )
    for token in required:
        assert token in css


def test_p84_reader_documentation_explains_the_shared_parameter_question() -> None:
    proposition = _read("docs/proposition_84_exact_projection_parity_contrast.md")
    roadmap = _read("docs/theorem_roadmap.md")
    implementation = _read("website/implementation.html")
    svg = _read("docs/figures/p84_exact_joint_projection_parity_contrast.svg")

    assert "## Plain-language meaning" in proposition
    assert "can the same parameter choice explain two such observations at once?" in proposition
    assert "**Plain-language interpretation.**" in roadmap
    frontier = max(
        int(path.name.split("_")[1])
        for path in (ROOT / "docs").glob("proposition_*.md")
    )
    target_range = f"P73-P{frontier}"
    assert f"Stage 06 · {target_range}" in implementation
    assert implementation.count(
        f"{target_range} build a continuous chain from channel recovery to certified model-family separation."
    ) == 1
    assert "P84" in implementation
    assert "joint shared-parameter" in implementation
    assert "P84 Joint Parity Compatibility Certificate" in svg
    assert "Two parity checks can pass separately yet fail under one shared P75 parameter assignment" in svg
