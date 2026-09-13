from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DETAILED_RECORD = ROOT / "docs" / "detailed_proposition_record.md"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"


def test_readme_is_a_concise_reader_first_front_door() -> None:
    text = README.read_text(encoding="utf-8")

    required = (
        "# Mathematical Consciousness Bridge",
        "website/plain-language.html",
        "START_HERE.md",
        "website/research-map.html",
        "docs/detailed_proposition_record.md",
        "docs/research_navigation.md",
        "website/visual-atlas.html",
        "87 proposition-level results through P87",
        "v0.82.0",
        "physical-to-experiential bridge remains open",
    )
    for marker in required:
        assert marker in text


def test_complete_proposition_chronology_lives_in_detailed_record() -> None:
    text = DETAILED_RECORD.read_text(encoding="utf-8")

    assert "Complete P1 to P87 chronology" in text
    for i in range(1, 88):
        assert f"P{i}" in text, f"Detailed proposition record is missing P{i}"


def test_visual_atlas_carries_the_figure_publication_layer() -> None:
    text = VISUAL_ATLAS.read_text(encoding="utf-8")

    assert "P87" in text
    assert "p87_exact_bounded_primitive_quad_projection_parity.svg" in text
    assert "Scientific boundary" in text


def test_readme_does_not_duplicate_the_full_technical_record() -> None:
    text = README.read_text(encoding="utf-8")

    # The README is intentionally a front door. The complete chronology and
    # visual publication record are linked from it rather than duplicated there.
    assert "docs/detailed_proposition_record.md" in text
    assert "website/visual-atlas.html" in text
    assert text.count("## ") < 20
