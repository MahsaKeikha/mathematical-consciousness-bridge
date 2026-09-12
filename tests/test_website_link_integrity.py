"""Internal link-integrity checks for the public research website."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.srcs: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)
        href = values.get("href")
        if href:
            self.hrefs.append(href)
        src = values.get("src")
        if src:
            self.srcs.append(src)


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def is_external(value: str) -> bool:
    split = urlsplit(value)
    return bool(split.scheme or split.netloc or value.startswith("//"))


def test_all_local_website_links_and_assets_resolve() -> None:
    pages = sorted(WEBSITE.glob("*.html"))
    assert pages, "website must contain HTML pages"
    parsed = {page.resolve(): parse_page(page) for page in pages}

    problems: list[str] = []

    for page in pages:
        parser = parsed[page.resolve()]
        for raw in parser.hrefs:
            if raw.startswith(("mailto:", "tel:", "javascript:")) or is_external(raw):
                continue

            split = urlsplit(raw)
            path_part = unquote(split.path)
            fragment = unquote(split.fragment)

            target = page if not path_part else (page.parent / path_part).resolve()
            if target.is_dir():
                target = target / "index.html"

            if not target.exists():
                problems.append(f"{page.name}: missing href target {raw!r}")
                continue

            if fragment and target.suffix.lower() == ".html":
                target_parser = parsed.get(target.resolve())
                if target_parser is None:
                    target_parser = parse_page(target)
                    parsed[target.resolve()] = target_parser
                if fragment not in target_parser.ids:
                    problems.append(
                        f"{page.name}: missing fragment #{fragment} in {target.name} for {raw!r}"
                    )

        for raw in parser.srcs:
            if is_external(raw):
                continue
            split = urlsplit(raw)
            path_part = unquote(split.path)
            if not path_part:
                continue
            target = (page.parent / path_part).resolve()
            if not target.exists():
                problems.append(f"{page.name}: missing src target {raw!r}")

    assert not problems, "Website link integrity failures:\n" + "\n".join(problems)


def test_research_i_page_uses_authoritative_previous_repository_paths() -> None:
    text = (WEBSITE / "observer-research.html").read_text(encoding="utf-8")
    required = (
        "spatiotemporal-observer-math/blob/main/docs/visual_research_guide.md",
        "spatiotemporal-observer-math/blob/main/docs/physics_guide.md",
        "spatiotemporal-observer-math/blob/main/docs/physics_mathematics_citation_map.md",
        "spatiotemporal-observer-math/blob/main/docs/research_overview.md",
        "spatiotemporal-observer-math/blob/main/docs/research_index.md",
        "spatiotemporal-observer-math/blob/main/docs/assumption_ledger.md",
        "spatiotemporal-observer-math/blob/main/docs/reproducible_results.md",
    )
    for path in required:
        assert path in text

    # Guard against two previously introduced guessed paths that do not exist in Research I.
    assert "docs/scientific_foundations.md" not in text
    assert "docs/figures/physics_to_observer_pipeline.svg" not in text
