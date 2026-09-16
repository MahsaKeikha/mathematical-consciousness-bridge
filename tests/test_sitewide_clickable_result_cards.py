from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
READER_LINKS = ROOT / "website" / "reader-links.js"


def test_reader_script_wires_whole_result_cards() -> None:
    script = READER_LINKS.read_text(encoding="utf-8")

    required = (
        "function wireAllResultCards()",
        "function wireWholeResultCard(card)",
        "function primaryCardHref(card)",
        ".result-grid, .results-grid, .theorem-grid, .theorem-cards",
        ".result-card, .result-tile, .theorem-card, .theorem-tile",
        "card.classList.add('interactive-card')",
        "card.setAttribute('role', 'link')",
        "wireAllResultCards();",
    )
    for token in required:
        assert token in script


def test_research_map_normalizes_proposition_result_boxes() -> None:
    script = READER_LINKS.read_text(encoding="utf-8")

    required = (
        "function normalizeResearchMapResultBoxes()",
        "research-map-detail-grid",
        "number: 74",
        "number: 75",
        "number: 76",
        "#p92-research-map",
        "#p93-research-map",
        "#p94-research-map",
        "normalizeResearchMapResultBoxes();",
    )
    for token in required:
        assert token in script


def test_whole_card_click_preserves_nested_link_behavior() -> None:
    script = READER_LINKS.read_text(encoding="utf-8")

    assert "event.target.closest('a, button, input, select, textarea, summary')" in script
    assert "if (card.dataset.clickableReady === 'true') return;" in script
    assert "card.dataset.clickableReady = 'true';" in script
    assert "window.location.href = href;" in script
