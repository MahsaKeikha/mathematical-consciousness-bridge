from pathlib import Path

from scripts.prepare_website import NAVIGATION_STYLE_TAG, SCRIPT_TAG, prepare_website


def test_prepare_website_injects_shared_navigation_assets(tmp_path: Path) -> None:
    source = tmp_path / "website"
    output = tmp_path / "_site"
    source.mkdir()
    (source / "app.js").write_text("console.log('ok')", encoding="utf-8")
    (source / "styles.css").write_text("body{}", encoding="utf-8")
    (source / "navigation.css").write_text("nav{}", encoding="utf-8")
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
        assert built.count(NAVIGATION_STYLE_TAG) == 1


def test_prepare_website_is_idempotent(tmp_path: Path) -> None:
    source = tmp_path / "website"
    first = tmp_path / "first"
    second = tmp_path / "second"
    source.mkdir()
    (source / "app.js").write_text("console.log('ok')", encoding="utf-8")
    (source / "styles.css").write_text("body{}", encoding="utf-8")
    (source / "navigation.css").write_text("nav{}", encoding="utf-8")
    (source / "index.html").write_text(
        f"<html><head>{NAVIGATION_STYLE_TAG}{SCRIPT_TAG}</head><body></body></html>",
        encoding="utf-8",
    )

    prepare_website(source, first)
    prepare_website(first, second)

    assert (first / "index.html").read_text(encoding="utf-8") == (
        second / "index.html"
    ).read_text(encoding="utf-8")
