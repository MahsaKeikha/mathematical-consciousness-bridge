from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_visual_atlas_has_one_unambiguous_current_frontier() -> None:
    atlas = _read("website/visual-atlas.html")
    assert atlas.count('class="theorem-frontier current-frontier-visual"') == 1
    assert '<section id="p100-frontier" class="theorem-frontier current-frontier-visual">' in atlas
    for number in range(86, 100):
        assert f'<section id="p{number}-frontier" class="theorem-frontier">' in atlas


def test_visual_atlas_explains_current_first_order() -> None:
    atlas = _read("website/visual-atlas.html")
    assert 'id="atlas-reading-rule"' in atlas
    assert "this atlas is intentionally current-first" in atlas
    assert 'research-map.html#continuous-model-frontier' in atlas
    assert atlas.index('id="p100-frontier"') < atlas.index('id="p99-frontier"')
    for number in range(99, 86, -1):
        assert atlas.index(f'id="p{number}-frontier"') < atlas.index(f'id="p{number - 1}-frontier"')


def test_visual_atlas_frontier_labels_are_semantically_consistent() -> None:
    atlas = _read("website/visual-atlas.html")
    assert "Current theorem frontier · P100" in atlas
    assert "Immediate predecessor · P99" in atlas
    for number in range(86, 99):
        assert f"Historical theorem frontier · P{number}" in atlas
    assert "Previous theorem frontier · P98" not in atlas
    assert "Previous theorem frontier · P93" not in atlas


def test_core_reader_navigation_has_mobile_controls_and_active_page_state() -> None:
    atlas = _read("website/visual-atlas.html")
    research = _read("website/research-map.html")
    assert '<button class="nav-toggle" aria-label="Toggle navigation">Menu</button>' in atlas
    assert '<button class="nav-toggle" aria-label="Toggle navigation">Menu</button>' in research
    assert '<a href="visual-atlas.html" aria-current="page">Visual Atlas</a>' in atlas
    assert '<a href="research-map.html" aria-current="page">Research Map</a>' in research


def test_p100_metadata_and_cache_labels_do_not_advertise_p88_or_p99() -> None:
    start = _read("website/start-here.html")
    lineage = _read("website/research-lineage.html")
    assert "current Research II P100 frontier" in start
    assert "current Research II P99 frontier" not in start
    assert "20260913-mobile18-p88" not in lineage
    assert "20260916-p100" in lineage


def test_changed_reader_surfaces_obey_punctuation_policy() -> None:
    for path in (
        "website/visual-atlas.html",
        "website/start-here.html",
        "website/research-map.html",
        "website/research-lineage.html",
    ):
        text = _read(path)
        assert "\u2013" not in text
        assert "\u2014" not in text
