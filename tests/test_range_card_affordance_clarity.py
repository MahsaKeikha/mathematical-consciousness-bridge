from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"


def test_proposition_range_cards_are_not_silently_linked_to_first_result() -> None:
    script = (WEBSITE / "footer.js").read_text(encoding="utf-8")

    assert "function propositionMentions(text)" in script
    assert "function hasAmbiguousPropositionScope(card)" in script
    assert "propositionMentions(text).size > 1" in script
    assert r"/\bP\d{1,3}\s*-\s*P?\d{1,3}\b/i" in script
    assert "if (hasAmbiguousPropositionScope(card))" in script
    assert "neutralizeAmbiguousWholeCard(card);" in script


def test_native_range_navigation_cards_remain_explicit_links() -> None:
    script = (WEBSITE / "footer.js").read_text(encoding="utf-8")

    assert "if (card.matches('a[href]')) return false;" in script
    assert "const nativeLink = card.matches('a[href]');" in script
    assert "if (nativeLink || isAlreadyInteractive)" in script


def test_plain_language_frontier_is_static_p100_with_runtime_fallback() -> None:
    page = (WEBSITE / "plain-language.html").read_text(encoding="utf-8")
    script = (WEBSITE / "footer.js").read_text(encoding="utf-8")

    assert "100-result" in page
    assert "current theorem frontier is P100" in page
    assert "99-result" not in page
    assert "current theorem frontier is P99" not in page
    assert "function syncPlainLanguageFrontier()" in script
    assert "['99-result', '100-result']" in script
    assert "['all 99 Research II results', 'all 100 Research II results']" in script
    assert "['currently through P99', 'currently through P100']" in script
    assert "['current theorem frontier is P99', 'current theorem frontier is P100']" in script
    assert "syncPlainLanguageFrontier();" in script
