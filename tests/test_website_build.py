from pathlib import Path

from scripts.prepare_website import (
    FOOTER_SCRIPT_TAG,
    NAVIGATION_STYLE_TAG,
    PUBLICATION_STYLE_TAG,
    PUBLICATION_V2_STYLE_TAG,
    READER_LINKS_SCRIPT_TAG,
    SCRIPT_TAG,
    prepare_website,
)


def _write_assets(source: Path) -> None:
    (source / "app.js").write_text("console.log('ok')", encoding="utf-8")
    (source / "reader-links.js").write_text("console.log('links')", encoding="utf-8")
    (source / "footer.js").write_text("console.log('footer')", encoding="utf-8")
    (source / "styles.css").write_text("body{}", encoding="utf-8")
    (source / "navigation.css").write_text("nav{}", encoding="utf-8")
    (source / "publication.css").write_text("h1{}", encoding="utf-8")
    (source / "publication-v2.css").write_text("main h1{}", encoding="utf-8")


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
        assert built.count(PUBLICATION_STYLE_TAG) == 1
        assert built.count(PUBLICATION_V2_STYLE_TAG) == 1
        assert built.index(PUBLICATION_V2_STYLE_TAG) > built.index(PUBLICATION_STYLE_TAG)


def test_prepare_website_is_idempotent(tmp_path: Path) -> None:
    source = tmp_path / "website"
    first = tmp_path / "first"
    second = tmp_path / "second"
    source.mkdir()
    _write_assets(source)
    (source / "index.html").write_text(
        f"<html><head>{NAVIGATION_STYLE_TAG}{PUBLICATION_STYLE_TAG}"
        f"{PUBLICATION_V2_STYLE_TAG}{SCRIPT_TAG}{READER_LINKS_SCRIPT_TAG}"
        f"{FOOTER_SCRIPT_TAG}</head><body></body></html>",
        encoding="utf-8",
    )

    prepare_website(source, first)
    prepare_website(first, second)

    assert (first / "index.html").read_text(encoding="utf-8") == (
        second / "index.html"
    ).read_text(encoding="utf-8")


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


def test_footer_identifies_research_author() -> None:
    script = Path("website/footer.js").read_text(encoding="utf-8")

    assert "Mahsa Keikha" in script
    assert "https://github.com/MahsaKeikha" in script
    assert "Research by " in script
    assert "Mathematical Consciousness Bridge" in script
