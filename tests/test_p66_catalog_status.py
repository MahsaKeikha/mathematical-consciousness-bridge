from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs/figure_catalog.md"


def test_p66_catalog_keeps_scientific_status_boundary():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P66 residual-exact augmentation after P65 flooring" in text
    assert "Discrete resource-allocation theorem for the declared calibration surrogate" in text
    assert "physical-to-experiential bridge theorem" in text
    assert "quantum-ontology claim" in text
