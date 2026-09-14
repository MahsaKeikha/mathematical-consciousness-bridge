from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WEBSITE = REPO_ROOT / "website"

PUBLIC_MARKDOWN = (
    REPO_ROOT / "README.md",
    REPO_ROOT / "START_HERE.md",
    REPO_ROOT / "docs" / "research_map.md",
    REPO_ROOT / "docs" / "research_navigation.md",
    REPO_ROOT / "docs" / "research_architecture.md",
)

LONG_DASHES = ("\u2013", "\u2014")


def test_public_website_has_no_en_dash_or_em_dash_characters() -> None:
    failures: list[str] = []
    for path in sorted(WEBSITE.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        if any(char in text for char in LONG_DASHES):
            failures.append(path.relative_to(REPO_ROOT).as_posix())
    assert not failures, f"Long dash punctuation found in public HTML: {failures}"


def test_reader_markdown_has_no_en_dash_or_em_dash() -> None:
    failures: list[str] = []
    for path in PUBLIC_MARKDOWN:
        text = path.read_text(encoding="utf-8")
        if any(char in text for char in LONG_DASHES):
            failures.append(path.relative_to(REPO_ROOT).as_posix())
    assert not failures, f"Long dash punctuation found in reader Markdown: {failures}"


def test_normal_hyphenated_scientific_terms_remain_allowed() -> None:
    public_text = "\n".join(path.read_text(encoding="utf-8") for path in PUBLIC_MARKDOWN)
    assert "physical-to-experiential" in public_text
    assert "reader-facing" in public_text or "finite-data" in public_text
