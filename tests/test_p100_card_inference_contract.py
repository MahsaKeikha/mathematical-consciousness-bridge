from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"


def test_app_proposition_parser_supports_p100() -> None:
    app = (WEBSITE / "app.js").read_text(encoding="utf-8")

    assert r"/\bP(\d{1,3})\b/gi" in app
    assert "function propositionMentions(text)" in app
    assert "function hasAmbiguousPropositionText(text)" in app


def test_app_refuses_to_infer_whole_card_link_for_ranges_or_multiple_propositions() -> None:
    app = (WEBSITE / "app.js").read_text(encoding="utf-8")

    assert r"/\bP\d{1,3}\s*-\s*P?\d{1,3}\b/i" in app
    assert "new Set(propositionMentions(text)).size > 1" in app
    assert "if (hasAmbiguousPropositionText(text)) return null;" in app


def test_direct_links_still_win_before_ambiguity_guard() -> None:
    app = (WEBSITE / "app.js").read_text(encoding="utf-8")

    inferred = app.split("function inferredCardHref(card)", 1)[1].split("function activateCard", 1)[0]
    assert inferred.index("const direct = card.querySelector('a[href]');") < inferred.index(
        "if (hasAmbiguousPropositionText(text)) return null;"
    )


def test_auto_research_anchor_creation_does_not_guess_for_range_sections() -> None:
    app = (WEBSITE / "app.js").read_text(encoding="utf-8")
    anchors = app.split("function addResearchAnchors()", 1)[1].split("function addBackToTop", 1)[0]

    assert "if (hasAmbiguousPropositionText(text)) return;" in anchors
    assert "const number = propositionNumber(text);" in anchors


def test_footer_range_guard_remains_the_second_layer_contract() -> None:
    footer = (WEBSITE / "footer.js").read_text(encoding="utf-8")

    assert "function hasAmbiguousPropositionScope(card)" in footer
    assert r"/\bP\d{1,3}\s*-\s*P?\d{1,3}\b/i" in footer
    assert "neutralizeAmbiguousWholeCard(card);" in footer
