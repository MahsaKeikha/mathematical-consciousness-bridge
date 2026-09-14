from __future__ import annotations

from html.parser import HTMLParser
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


class VisibleTextParser(HTMLParser):
    """Collect text that a reader can see while ignoring code and scripts."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._ignored_depth = 0
        self.text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "code", "pre"}:
            self._ignored_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "code", "pre"} and self._ignored_depth:
            self._ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self._ignored_depth:
            self.text_parts.append(data)

    @property
    def visible_text(self) -> str:
        return " ".join(self.text_parts)


def test_public_website_has_no_long_dash_characters() -> None:
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
