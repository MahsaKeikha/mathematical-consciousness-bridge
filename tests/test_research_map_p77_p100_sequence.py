import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website" / "research-map.html"


def _sequence() -> str:
    text = MAP.read_text(encoding="utf-8")
    return text.split("<!-- BEGIN CONTINUOUS MODEL FRONTIER -->", 1)[1].split(
        "<!-- END CONTINUOUS MODEL FRONTIER -->", 1
    )[0]


def test_research_map_has_one_uniform_p77_p100_card_sequence():
    block = _sequence()
    numbers = [
        int(value)
        for value in re.findall(
            r'<article class="result frontier-sequence-card" id="p(\d+)-research-map"',
            block,
        )
    ]
    assert numbers == list(range(77, 101))


def test_every_frontier_card_links_to_its_canonical_theorem():
    block = _sequence()
    for number in range(77, 101):
        proofs = list((ROOT / "docs").glob(f"proposition_{number}_*.md"))
        assert len(proofs) == 1
        assert proofs[0].name in block
        assert f'data-proposition="P{number}"' in block


def test_scattered_legacy_frontier_blocks_are_gone():
    text = MAP.read_text(encoding="utf-8")
    assert 'id="historical-frontiers"' not in text
    assert 'id="p87-reader-frontier"' not in text
    for number in range(77, 101):
        assert text.count(f'id="p{number}-research-map"') == 1


def test_sequence_precedes_boundary_and_audit_paths():
    text = MAP.read_text(encoding="utf-8")
    end = text.index("<!-- END CONTINUOUS MODEL FRONTIER -->")
    boundary = text.index('id="scientific-boundary"')
    audit = text.index('id="audit-paths"')
    assert end < boundary < audit
    assert "P100 - Current theorem frontier" in _sequence()


def test_sequence_reader_text_respects_dash_policy():
    block = _sequence()
    assert "\u2013" not in block
    assert "\u2014" not in block
