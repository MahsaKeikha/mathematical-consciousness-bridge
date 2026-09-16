from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p93_proof_states_localized_rejection_and_boundary() -> None:
    text = _read("docs/proposition_93_localized_sign_coherence_rejection.md")
    lower = text.lower()
    assert "seven" in lower
    assert "1623" in text
    assert "1632" in text
    assert "non-rejection remains inconclusive" in lower
    assert "physical-to-experiential bridge remains open" in lower


def test_p93_is_preserved_as_historical_iid_frontier() -> None:
    atlas = _read("website/visual-atlas.html")
    assert 'id="p93-frontier"' in atlas
    assert "Historical theorem frontier · P93" in atlas
    assert "p93_localized_sign_coherence_rejection.svg" in atlas
    assert atlas.index('id="p94-frontier"') < atlas.index('id="p93-frontier"')


def test_p93_reader_surfaces_remain_linked_as_history() -> None:
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    assert 'id="p93-reader-frontier"' in plain
    assert "P93" in start
    assert "P93" in plain


def test_permanent_publication_workflows_are_read_only() -> None:
    for path in (
        ".github/workflows/figures.yml",
        ".github/workflows/reproducibility.yml",
        ".github/workflows/validate-research-three-website.yml",
    ):
        text = _read(path)
        assert "contents: read" in text
        assert "contents: write" not in text
        assert "git push" not in text
