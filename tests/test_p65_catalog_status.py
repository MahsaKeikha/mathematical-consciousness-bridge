from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs/figure_catalog.md"


def test_p65_catalog_explains_floor_certificate_and_boundary():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P65 lower-bounded heterogeneous calibration" in text
    assert "flooring it is always feasible" in text
    assert "no worse than square-root two" in text
    assert "not claimed to be the exact unrestricted integer optimum" in text
    assert "physical-to-experiential bridge" in text
    assert "quantum mechanics is incomplete" in text
