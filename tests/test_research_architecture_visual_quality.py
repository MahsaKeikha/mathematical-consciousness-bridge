from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG = (ROOT / "docs" / "figures" / "research_architecture.svg").read_text(
    encoding="utf-8"
)


def test_research_architecture_uses_dense_diagram_canvas_standard() -> None:
    assert 'width="1800"' in SVG
    assert 'viewBox="0 0 1800 1080"' in SVG


def test_research_architecture_has_distinct_academic_color_families() -> None:
    required = (
        "#eff6ff",
        "#ecfeff",
        "#ecfdf5",
        "#f5f3ff",
        "#fff7ed",
        "#fffbeb",
        "#f0fdf4",
        "#fff1f2",
    )
    for color in required:
        assert color in SVG


def test_research_architecture_keeps_all_eight_stages_explicit() -> None:
    headings = (
        "1. Physical realization",
        "2. Physical quotient",
        "3. Candidate physical signature",
        "4. Bridge structure",
        "5. Experiential quotient",
        "6. Observable predictions",
        "7. Finite-data recovery",
        "8. Falsification",
    )
    for heading in headings:
        assert heading in SVG


def test_research_architecture_splits_strongest_target_over_two_lines() -> None:
    assert "physical first principles + validated bridge premises" in SVG
    assert "formal experiential property" in SVG
    assert SVG.count("Strongest target") == 1
