from pathlib import Path

from scripts.prepare_website import (
    ASSET_VERSION,
    CONTRAST_STYLE_TAG,
    FOOTER_SCRIPT_TAG,
    NAVIGATION_STYLE_TAG,
    NAVIGATION_V2_STYLE_TAG,
    PUBLICATION_STYLE_TAG,
    PUBLICATION_V2_STYLE_TAG,
    READER_LINKS_SCRIPT_TAG,
    RESEARCH_GUIDE_STYLE_TAG,
    SCRIPT_TAG,
    prepare_website,
)


def _write_assets(source: Path) -> None:
    (source / "app.js").write_text("console.log('ok')", encoding="utf-8")
    (source / "reader-links.js").write_text("console.log('links')", encoding="utf-8")
    (source / "footer.js").write_text("console.log('footer')", encoding="utf-8")
    (source / "styles.css").write_text("body{}", encoding="utf-8")
    (source / "navigation.css").write_text("nav{}", encoding="utf-8")
    (source / "navigation-v2.css").write_text(".nav-dropdown{}", encoding="utf-8")
    (source / "publication.css").write_text("h1{}", encoding="utf-8")
    (source / "publication-v2.css").write_text("main h1{}", encoding="utf-8")
    (source / "research-guide-v2.css").write_text(".research-jumpbar{}", encoding="utf-8")
    (source / "contrast-v2.css").write_text(".equation{}", encoding="utf-8")


def test_prepare_website_injects_shared_publication_assets(tmp_path: Path) -> None:
    source = tmp_path / "website"
    output = tmp_path / "_site"
    source.mkdir()
    _write_assets(source)
    (source / "index.html").write_text(
        "<html><head><link rel=\"stylesheet\" href=\"styles.css\"></head><body></body></html>",
        encoding="utf-8",
    )
    (source / "sources.html").write_text(
        f"<html><head>{SCRIPT_TAG}</head><body></body></html>",
        encoding="utf-8",
    )

    prepare_website(source, output)

    for name in ("index.html", "sources.html"):
        built = (output / name).read_text(encoding="utf-8")
        assert built.count(SCRIPT_TAG) == 1
        assert built.count(READER_LINKS_SCRIPT_TAG) == 1
        assert built.count(FOOTER_SCRIPT_TAG) == 1
        assert built.count(NAVIGATION_STYLE_TAG) == 1
        assert built.count(NAVIGATION_V2_STYLE_TAG) == 1
        assert built.count(PUBLICATION_STYLE_TAG) == 1
        assert built.count(PUBLICATION_V2_STYLE_TAG) == 1
        assert built.count(RESEARCH_GUIDE_STYLE_TAG) == 1
        assert built.count(CONTRAST_STYLE_TAG) == 1
        assert built.index(NAVIGATION_V2_STYLE_TAG) > built.index(NAVIGATION_STYLE_TAG)
        assert built.index(PUBLICATION_V2_STYLE_TAG) > built.index(PUBLICATION_STYLE_TAG)
        assert built.index(CONTRAST_STYLE_TAG) > built.index(RESEARCH_GUIDE_STYLE_TAG)


def test_prepare_website_is_idempotent(tmp_path: Path) -> None:
    source = tmp_path / "website"
    first = tmp_path / "first"
    second = tmp_path / "second"
    source.mkdir()
    _write_assets(source)
    (source / "index.html").write_text(
        f"<html><head>{NAVIGATION_STYLE_TAG}{NAVIGATION_V2_STYLE_TAG}"
        f"{PUBLICATION_STYLE_TAG}{PUBLICATION_V2_STYLE_TAG}{RESEARCH_GUIDE_STYLE_TAG}"
        f"{CONTRAST_STYLE_TAG}{SCRIPT_TAG}{READER_LINKS_SCRIPT_TAG}{FOOTER_SCRIPT_TAG}"
        "</head><body></body></html>",
        encoding="utf-8",
    )

    prepare_website(source, first)
    prepare_website(first, second)

    assert (first / "index.html").read_text(encoding="utf-8") == (
        second / "index.html"
    ).read_text(encoding="utf-8")


def test_prepare_website_replaces_stale_navigation_assets_and_fallback(
    tmp_path: Path,
) -> None:
    source = tmp_path / "website"
    output = tmp_path / "_site"
    source.mkdir()
    _write_assets(source)
    (source / "index.html").write_text(
        "<html><head>"
        '<script defer src="app.js"></script>'
        '<link rel="stylesheet" href="navigation-v2.css" />'
        "</head><body>"
        '<header class="topbar"><a class="brand">Brand</a><nav>'
        '<a href="research-lineage.html">Research Lineage</a>'
        '<a href="research-map.html">Research Map</a>'
        '<a href="physics-mathematics.html">Physics &amp; Math</a>'
        '<a href="visual-atlas.html">Visual Atlas</a>'
        "</nav></header>"
        "</body></html>",
        encoding="utf-8",
    )

    prepare_website(source, output)
    built = (output / "index.html").read_text(encoding="utf-8")

    assert f'app.js?v={ASSET_VERSION}' in built
    assert f'navigation-v2.css?v={ASSET_VERSION}' in built
    assert f'research-guide-v2.css?v={ASSET_VERSION}' in built
    assert f'contrast-v2.css?v={ASSET_VERSION}' in built
    assert '<script defer src="app.js"></script>' not in built
    assert 'href="navigation-v2.css"' not in built
    assert '>Research Lineage</a>' not in built
    assert '>Research Map</a>' not in built
    assert '>Physics &amp; Math</a>' not in built
    assert '>Visual Atlas</a>' not in built
    assert '>Research</a>' in built
    assert '>Explore</a>' in built


def test_publication_type_scale_stays_restrained() -> None:
    css = Path("website/publication-v2.css").read_text(encoding="utf-8")

    assert "--publication-title-max: 2.2rem" in css
    assert "--publication-section-max: 1.6rem" in css
    assert "font-size: clamp(1.72rem, 2.25vw, var(--publication-title-max)) !important" in css
    assert "font-size: clamp(1.28rem, 1.65vw, var(--publication-section-max)) !important" in css
    assert "max-width: 42ch !important" in css


def test_every_html_page_uses_shared_heading_classes_without_inline_font_sizes() -> None:
    for path in sorted(Path("website").glob("*.html")):
        text = path.read_text(encoding="utf-8")
        assert "font-size:" not in text, f"inline font sizing found in {path}"
        assert "style=\"font-size" not in text, f"inline title sizing found in {path}"


def test_dropdown_navigation_is_compact_and_responsive() -> None:
    script = Path("website/app.js").read_text(encoding="utf-8")
    css = Path("website/navigation-v2.css").read_text(encoding="utf-8")

    assert "NAV_GROUPS" in script
    assert "observer-research.html" in script
    assert "Research I" in script
    assert "Research II" in script
    assert "nav-dropdown" in script
    assert ".nav-dropdown-menu" in css
    assert ".nav-dropbtn" in css
    assert "@media (max-width: 760px)" in css


def test_footer_identifies_research_author() -> None:
    script = Path("website/footer.js").read_text(encoding="utf-8")

    assert "Mahsa Keikha" in script
    assert "https://github.com/MahsaKeikha" in script
    assert "Research by " in script
    assert "Mathematical Consciousness Bridge" in script
