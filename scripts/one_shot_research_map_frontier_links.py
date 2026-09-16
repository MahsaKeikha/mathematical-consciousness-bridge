from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "website" / "research-map.html"
TEST = ROOT / "tests" / "test_complete_research_map_proposition_navigator.py"

REPLACEMENTS = [
    (
        '<a href="visual-atlas.html">See the P96 figure</a>',
        '<a href="visual-atlas.html#p100-frontier">See the current P100 figure</a>',
    ),
    (
        '<a href="visual-atlas.html#p96-frontier">Current frontier</a>',
        '<a href="visual-atlas.html#p100-frontier">Current P100 frontier</a>',
    ),
]


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one stale frontier link, found {count}: {old}")
    return text.replace(old, new, 1)


def main() -> None:
    page = PAGE.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS:
        page = replace_once(page, old, new)
    PAGE.write_text(page, encoding="utf-8")

    test = TEST.read_text(encoding="utf-8").rstrip()
    marker = "def test_research_map_historical_sections_link_to_current_p100_frontier() -> None:"
    if marker not in test:
        test += '''\n\n\ndef test_research_map_historical_sections_link_to_current_p100_frontier() -> None:\n    page = PAGE.read_text(encoding="utf-8")\n    assert 'visual-atlas.html#p100-frontier">See the current P100 figure</a>' in page\n    assert 'visual-atlas.html#p100-frontier">Current P100 frontier</a>' in page\n    assert 'visual-atlas.html#p96-frontier">Current frontier</a>' not in page\n    assert '>See the P96 figure</a>' not in page\n'''
    TEST.write_text(test + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
