from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p95_formal_record_is_preserved() -> None:
    proof = _read("docs/proposition_95_drift_aware_stratified_sign_coherence.md")
    assert "predeclared" in proof.lower()
    assert "3645" in proof and "3648" in proof
    assert "familywise" in proof.lower()
    for path in (
        "docs/p95_equation_provenance.md",
        "docs/figures/p95_drift_aware_stratified_sign_coherence.svg",
        "src/consciousness_bridge/drift_aware_stratified_sign_coherence.py",
        "tests/test_drift_aware_stratified_sign_coherence.py",
    ):
        assert (ROOT / path).is_file()


def test_p95_remains_visible_below_p96_and_p97() -> None:
    atlas = _read("website/visual-atlas.html")
    research = _read("website/research-map.html")
    assert atlas.index('id="p97-frontier"') < atlas.index('id="p96-frontier"')
    assert atlas.index('id="p96-frontier"') < atlas.index('id="p95-frontier"')
    assert "Historical theorem frontier · P95" in atlas
    assert research.index('id="p97-research-map"') < research.index('id="p96-research-map"')
    assert research.index('id="p96-research-map"') < research.index('id="p95-research-map"')


def test_p95_scientific_boundary_remains_visible() -> None:
    proof = _read("docs/proposition_95_drift_aware_stratified_sign_coherence.md").lower()
    assert "predeclared" in proof
    assert "physical-to-experiential bridge" in proof
