import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p92_proof_states_exact_global_distance_and_boundary() -> None:
    text = _read("docs/proposition_92_exact_global_mixed_prevalence_distance.md")
    lower = text.lower()
    assert "1/24" in text
    assert "sign-coherence" in lower
    assert "exact global" in lower
    assert "physical-to-experiential bridge remains open" in lower


def test_p92_is_historical_beneath_the_declared_homepage_frontier() -> None:
    manifest = json.loads(_read("figures/manifest.json"))
    current = str(manifest["current_frontier"]).lower()
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    assert f'id="{current}-frontier"' in home
    assert 'id="p92-frontier"' not in home
    current_position = atlas.index(f'id="{current}-frontier"')
    p92 = atlas.index('id="p92-frontier"')
    assert current_position < p92
    historical = atlas[p92:]
    assert "Historical theorem frontier · P92" in historical
    assert "p92_exact_global_mixed_prevalence_distance.svg" in historical
    assert "proposition_92_exact_global_mixed_prevalence_distance.md" in historical
    assert "p92_equation_provenance.md" in historical


def test_visual_atlas_orders_p92_before_p91_and_p90() -> None:
    text = _read("website/visual-atlas.html")
    p92 = text.index('id="p92-frontier"')
    p91 = text.index('id="p91-frontier"')
    p90 = text.index('id="p90-frontier"')
    assert p92 < p91 < p90
    assert "p92_exact_global_mixed_prevalence_distance.svg" in text[p92:p91]


def test_p92_historical_reader_surfaces_preserve_scientific_boundary() -> None:
    for path in (
        "docs/proposition_92_exact_global_mixed_prevalence_distance.md",
        "website/visual-atlas.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p92" in text
        assert "physical-to-experiential bridge" in text


def test_p92_start_here_preserves_history_while_plain_language_stays_conceptual() -> None:
    start = _read("website/start-here.html")
    plain = _read("website/plain-language.html")
    assert "P92" in start and "92" in start
    assert 'id="p92-reader-frontier"' in start
    assert 'id="p92-reader-frontier"' not in plain
    assert "100 linked results · technical endpoint P100" in plain


def test_p92_workflows_are_read_only_publication_gates() -> None:
    for path in (".github/workflows/figures.yml", ".github/workflows/reproducibility.yml", ".github/workflows/validate-research-three-website.yml"):
        text = _read(path)
        assert "contents: read" in text
        assert "contents: write" not in text
        assert "git push" not in text
