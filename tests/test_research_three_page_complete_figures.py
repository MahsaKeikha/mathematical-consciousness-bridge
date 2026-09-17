from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIENTATION = (ROOT / "website" / "research-orientation.js").read_text(encoding="utf-8")
PAGE_FIGURES = (ROOT / "website" / "research-iii-page-figures.js").read_text(encoding="utf-8")


EXPECTED_FIGURES = (
    "research_program_map.svg",
    "target_evidence_matrix.svg",
    "measurement_architecture.svg",
    "cep_anatomy.svg",
    "identification_uncertainty_pipeline.svg",
    "structural_measurement_pipeline.svg",
    "validation_program_map.svg",
    "theory_falsification_map.svg",
    "claim_ladder.svg",
)


def test_research_three_page_loads_complete_figure_refresh() -> None:
    assert "function loadResearchIIIPageFigures()" in ORIENTATION
    assert "currentFile() !== 'measurement-science.html'" in ORIENTATION
    assert "research-iii-page-figures.js" in ORIENTATION
    assert "loadResearchIIIPageFigures();" in ORIENTATION


def test_research_three_page_exposes_all_nine_canonical_figures() -> None:
    assert "3cf9202977953644c980246c1f3e46a3514b3a4a" in PAGE_FIGURES
    assert "All 9 canonical Research III scientific figures" in PAGE_FIGURES
    assert "grid.dataset.researchIiiCompleteGallery = '9'" in PAGE_FIGURES
    assert "Full-resolution SVG" in PAGE_FIGURES
    assert "Scientific context" in PAGE_FIGURES
    assert "Repository source" in PAGE_FIGURES
    for filename in EXPECTED_FIGURES:
        assert PAGE_FIGURES.count(f"file: '{filename}'") == 1
