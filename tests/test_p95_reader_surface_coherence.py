from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p95_formal_record_is_complete() -> None:
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


def test_p95_is_current_reader_frontier() -> None:
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")
    assert 'id="p95-frontier"' in home
    assert "Current theorem frontier · P95" in home
    assert atlas.index('id="p95-frontier"') < atlas.index('id="p94-frontier"')
    assert "Previous theorem frontier · P94" in atlas
    assert 'id="p95-reader-frontier"' in plain
    assert 'id="p95-reader-frontier"' in start
    assert 'id="p95-research-map"' in research
    assert "95 results · current frontier P95" in plain
    assert "95 results · current frontier P95" in start


def test_p95_scientific_boundary_is_visible() -> None:
    for path in (
        "README.md",
        "website/index.html",
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p95" in text
        assert "predeclared" in text
        assert "physical-to-experiential bridge" in text
