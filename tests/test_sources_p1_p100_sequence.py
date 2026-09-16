import re
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "website" / "sources.html"
RESEARCH_MAP = ROOT / "website" / "research-map.html"
FOOTER = ROOT / "website" / "footer.js"


def _block(text: str, begin: str, end: str) -> str:
    return text.split(begin, 1)[1].split(end, 1)[0]


def _cards(block: str) -> list[tuple[int, str, str]]:
    pattern = re.compile(
        r'<a(?: id="[^"]+")? class="proposition-nav-card" '
        r'data-proposition="P(\d+)" href="([^"]+)">.*?'
        r'<strong>(.*?)</strong>',
        flags=re.DOTALL,
    )
    return [
        (int(number), href, unescape(re.sub(r"<.*?>", "", title)).strip())
        for number, href, title in pattern.findall(block)
    ]


def test_sources_has_exact_ordered_p1_p100_source_sequence():
    text = SOURCES.read_text(encoding="utf-8")
    block = _block(
        text,
        "<!-- BEGIN COMPLETE SOURCE SEQUENCE -->",
        "<!-- END COMPLETE SOURCE SEQUENCE -->",
    )
    cards = _cards(block)
    assert [number for number, _, _ in cards] == list(range(1, 101))
    assert len({number for number, _, _ in cards}) == 100
    assert [int(value) for value in re.findall(r'id="source-p(\d+)"', block)] == list(range(1, 101))
    assert "Follow every theorem source from P1 through P100 in order" in block
    assert "Complete theorem roadmap P1-P100" in block
    assert "Core bridge lineage: P1-P24 then P71-P100" in block
    assert "physical-to-experiential bridge remains open" in block
    assert "\u2013" not in block
    assert "\u2014" not in block


def test_sources_sequence_matches_research_map_canonical_cards():
    sources = SOURCES.read_text(encoding="utf-8")
    research = RESEARCH_MAP.read_text(encoding="utf-8")
    source_block = _block(
        sources,
        "<!-- BEGIN COMPLETE SOURCE SEQUENCE -->",
        "<!-- END COMPLETE SOURCE SEQUENCE -->",
    )
    research_block = _block(
        research,
        "<!-- BEGIN COMPLETE PROPOSITION NAVIGATOR -->",
        "<!-- END COMPLETE PROPOSITION NAVIGATOR -->",
    )
    assert _cards(source_block) == _cards(research_block)


def test_sources_group_index_is_complete_and_scannable():
    text = SOURCES.read_text(encoding="utf-8")
    block = _block(
        text,
        "<!-- BEGIN COMPLETE SOURCE SEQUENCE -->",
        "<!-- END COMPLETE SOURCE SEQUENCE -->",
    )
    expected = [
        "p1-p10",
        "p11-p18",
        "p19-p24",
        "p25-p37",
        "p38-p44",
        "p45-p53",
        "p54-p60",
        "p61-p70",
        "p71-p76",
        "p77-p89",
        "p90-p95",
        "p96-p100",
    ]
    ids = re.findall(r'id="source-sequence-(p\d+-p\d+)"', block)
    assert ids == expected
    hrefs = re.findall(r'href="#source-sequence-(p\d+-p\d+)"', block)
    assert hrefs == expected


def test_detailed_source_records_are_strictly_ascending_without_gaps():
    text = SOURCES.read_text(encoding="utf-8")
    detailed = [int(value) for value in re.findall(r'<section id="p(\d+)-source"', text)]
    assert detailed == list(range(86, 101))
    assert "Detailed theorem source records, P86 through P100, in order" in text
    assert text.count("Current theorem source · P100") == 1
    assert not re.search(r"Current theorem source[^<]*· P(?:8[6-9]|9[0-9])", text)


def test_static_sources_frontier_is_not_rewritten_when_p100_exists():
    footer = FOOTER.read_text(encoding="utf-8")
    function = footer.split("function syncSourcesFrontier()", 1)[1].split(
        "function wireSourceCards()", 1
    )[0]
    assert function.index("document.querySelector('#p100-source')") < function.index(
        "document.querySelector('#p99-source')"
    )
