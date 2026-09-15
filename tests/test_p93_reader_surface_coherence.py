from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p93_proof_states_localized_rejection_and_boundary() -> None:
    text = _read("docs/proposition_93_localized_sign_coherence_rejection.md")
    lower = text.lower()
    assert "seven" in lower
    assert "1622" in text
    assert "1623" in text
    assert "1632" in text
    assert "7444" in text
    assert "non-rejection remains inconclusive" in lower
    assert "physical-to-experiential bridge remains open" in lower


def test_p93_homepage_is_current_and_links_complete_record() -> None:
    text = _read("website/index.html")
    assert 'id="p93-frontier"' in text
    assert "Current theorem frontier · P93" in text
    assert "p93_localized_sign_coherence_rejection.svg" in text
    assert "proposition_93_localized_sign_coherence_rejection.md" in text
    assert "p93_equation_provenance.md" in text
    assert "localized_sign_coherence_rejection.py" in text
    assert "test_localized_sign_coherence_rejection.py" in text
    assert "1632" in text


def test_visual_atlas_orders_p93_before_historical_frontiers() -> None:
    text = _read("website/visual-atlas.html")
    p93 = text.index('id="p93-frontier"')
    p92 = text.index('id="p92-frontier"')
    p91 = text.index('id="p91-frontier"')
    assert p93 < p92 < p91
    assert "p93_localized_sign_coherence_rejection.svg" in text[p93:p92]
    assert "Previous theorem frontier · P92" in text[p92:p91]


def test_p93_reader_surfaces_preserve_scientific_boundary() -> None:
    for path in (
        "README.md",
        "website/index.html",
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p93" in text
        assert "physical-to-experiential bridge" in text


def test_p93_start_here_and_plain_language_are_current() -> None:
    start = _read("website/start-here.html")
    plain = _read("website/plain-language.html")
    assert "P93" in start and "93" in start
    assert "P93" in plain and "93" in plain
    assert 'id="p93-reader-frontier"' in plain


def test_p92_is_preserved_as_historical_population_frontier() -> None:
    text = _read("website/visual-atlas.html")
    assert 'id="p92-frontier"' in text
    assert "Previous theorem frontier · P92" in text
    proof = _read("docs/proposition_92_exact_global_mixed_prevalence_distance.md")
    assert "=\n\\frac1{24}" in proof or "\\frac1{24}" in proof


def test_p93_permanent_workflows_are_read_only_publication_gates() -> None:
    for path in (
        ".github/workflows/figures.yml",
        ".github/workflows/reproducibility.yml",
        ".github/workflows/validate-research-three-website.yml",
    ):
        text = _read(path)
        assert "contents: read" in text
        assert "contents: write" not in text
        assert "git push" not in text
