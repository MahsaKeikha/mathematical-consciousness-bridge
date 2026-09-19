from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_all_core_reader_pages_have_scientific_orientation_contracts() -> None:
    script = _read("website/research-orientation.js")
    pages = (
        "index.html",
        "plain-language.html",
        "start-here.html",
        "observer-research.html",
        "research-lineage.html",
        "research-map.html",
        "measurement-science.html",
        "physics-mathematics.html",
        "visual-atlas.html",
        "sources.html",
    )

    for page in pages:
        assert f"'{page}':" in script

    assert script.count("question:") == len(pages)
    assert script.count("established:") == len(pages)
    assert script.count("open:") == len(pages)
    assert script.count("links:") == len(pages)


def test_orientation_keeps_claim_boundary_and_audit_visible() -> None:
    script = _read("website/research-orientation.js")

    for label in ("Question", "Established here", "Still open", "Evidence and audit"):
        assert label in script

    assert "physical-to-experiential bridge remains open" in script
    assert "not automatically a conscious subject" in script
    assert "Surviving the tests also does not establish" in script
    assert "Principled non-identification remains an allowed result." in script
    assert "Traceability is necessary for rigor" in script


def test_orientation_is_accessible_and_injected_once_below_the_hero() -> None:
    script = _read("website/research-orientation.js")

    assert "main.querySelector('.scientific-orientation')" in script
    assert "aria-labelledby" in script
    assert "aria-label=\"Evidence and audit links\"" in script
    assert "hero.insertAdjacentElement('afterend', section)" in script
    assert "document.readyState === 'loading'" in script


def test_app_loads_orientation_assets_sitewide() -> None:
    app = _read("website/app.js")

    assert "research-orientation.css" in app
    assert "research-orientation.js" in app
    assert "loadScientificOrientation" in app


def test_orientation_styles_are_responsive_and_visually_structured() -> None:
    css = _read("website/research-orientation.css")

    assert ".scientific-orientation-grid" in css
    assert "grid-template-columns: repeat(2, minmax(0, 1fr));" in css
    assert ".orientation-audit nav" in css
    assert "@media (max-width: 820px)" in css
    assert "@media (max-width: 520px)" in css



def test_research_three_orientation_keeps_intro_with_heading() -> None:
    script = _read("website/research-orientation.js")
    css = _read("website/research-orientation.css")
    app = _read("website/app.js")
    orientation = _read("website/research-orientation.js")

    assert "heading: 'Scientific scope and validation status'" in script
    assert "The formal results below concern identifiability, uncertainty, robustness, and measurement design." in script
    assert '<p class="scientific-orientation-intro">${contract.intro' in script
    assert "</p>\n        </div>\n      </div>" in script
    assert "grid-template-columns: minmax(0, 1fr);" not in css
    assert ".scientific-orientation-head > div" in css
    assert "research-orientation.css?v=20260919-r3-redesigned-figures" in app
    assert "research-orientation.js?v=20260919-r3-redesigned-figures" in app
    assert "research-iii-atlas-refresh.js?v=20260919-r3-redesigned-figures" in orientation

def test_new_reader_surface_respects_dash_policy() -> None:
    for path in ("website/research-orientation.js", "website/research-orientation.css"):
        text = _read(path)
        assert "\u2013" not in text
        assert "\u2014" not in text
