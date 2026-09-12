from pathlib import Path

from scripts.prepare_website import (
    FOOTER_SCRIPT_TAG,
    NAVIGATION_STYLE_TAG,
    PUBLICATION_STYLE_TAG,
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


def test_prepare_website_is_idempotent(tmp_path: Path) -> None:
    source = tmp_path / "website"
    first = tmp_path / "first"
    second = tmp_path / "second"
    source.mkdir()
    _write_assets(source)
    (source / "index.html").write_text(
        f"<html><head>{NAVIGATION_STYLE_TAG}{PUBLICATION_STYLE_TAG}{SCRIPT_TAG}"
        f"{READER_LINKS_SCRIPT_TAG}{FOOTER_SCRIPT_TAG}</head><body></body></html>",
        encoding="utf-8",
    )

    prepare_website(source, first)
    prepare_website(first, second)

    assert (first / "index.html").read_text(encoding="utf-8") == (
        second / "index.html"
    ).read_text(encoding="utf-8")


def test_publication_type_scale_stays_restrained() -> None:
    css = Path("website/publication.css").read_text(encoding="utf-8")

    assert "clamp(2rem, 3.5vw, 3rem)" in css
    assert "clamp(1.9rem, 3vw, 2.65rem)" in css
    assert "clamp(1.45rem, 2vw, 1.95rem)" in css
    assert "clamp(1.4rem, 1.95vw, 1.82rem)" in css


def test_footer_identifies_research_author() -> None:
    script = Path("website/footer.js").read_text(encoding="utf-8")

    assert "Mahsa Keikha" in script
    assert "https://github.com/MahsaKeikha" in script
    assert "Research by " in script
    assert "Mathematical Consciousness Bridge" in script
