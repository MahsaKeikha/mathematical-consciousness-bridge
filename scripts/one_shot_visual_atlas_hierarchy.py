from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "website" / "visual-atlas.html"
START = ROOT / "website" / "start-here.html"
MAP = ROOT / "website" / "research-map.html"
LINEAGE = ROOT / "website" / "research-lineage.html"
TEST = ROOT / "tests" / "test_visual_atlas_frontier_hierarchy.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def normalize_atlas() -> None:
    text = ATLAS.read_text(encoding="utf-8")

    text = replace_once(
        text,
        '<body><header class="topbar"><a class="brand" href="index.html">Mathematical Consciousness Bridge</a><nav>',
        '<body><header class="topbar"><a class="brand" href="index.html">Mathematical Consciousness Bridge</a><button class="nav-toggle" aria-label="Toggle navigation">Menu</button><nav>',
        "Visual Atlas mobile navigation",
    )
    text = replace_once(
        text,
        '<a href="visual-atlas.html">Visual Atlas</a>',
        '<a href="visual-atlas.html" aria-current="page">Visual Atlas</a>',
        "Visual Atlas active navigation",
    )

    hero_old = '<section class="hero compact-hero"><p class="eyebrow">Visual research atlas</p><h1>Figures as navigational aids to the mathematics</h1><p class="lede">The figures below are selected entry points into the formal record. They are diagrams, quantitative illustrations, or computational visualizations. They do not replace proofs, and each should be read together with its theorem, assumptions, and provenance.</p></section>'
    hero_new = '<section class="hero compact-hero"><p class="eyebrow">Visual research atlas</p><h1>Figures as navigational aids to the mathematics</h1><p class="lede">The figures below are selected entry points into the formal record. They are diagrams, quantitative illustrations, or computational visualizations. They do not replace proofs, and each should be read together with its theorem, assumptions, and provenance.</p><div class="hero-actions"><a class="button primary" href="#p100-frontier">Current P100 frontier</a><a class="button" href="#p99-frontier">Follow frontier history</a><a class="button" href="research-map.html#continuous-model-frontier">Read P77-P100 chronologically</a><a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_catalog.md">Complete figure catalog</a></div></section>'
    text = replace_once(text, hero_old, hero_new, "Visual Atlas hero")

    boundary_old = '<section class="boundary"><h2>How to read every figure</h2>'
    boundary_new = '<section class="boundary" id="atlas-reading-rule"><h2>How to read every figure</h2><p><strong>Reading order:</strong> this atlas is intentionally current-first. P100 appears first, followed by P99 and the earlier P98-P86 theorem frontiers in descending historical order. For the chronological scientific progression, use the <a href="research-map.html#continuous-model-frontier">P77-P100 Research Map sequence</a>.</p>'
    text = replace_once(text, boundary_old, boundary_new, "Visual Atlas reading rule")

    for number in range(86, 100):
        pattern = re.compile(
            rf'<section id="p{number}-frontier" class="theorem-frontier(?: current-frontier-visual| )*">'
        )
        text, count = pattern.subn(
            f'<section id="p{number}-frontier" class="theorem-frontier">', text, count=1
        )
        if count != 1:
            raise RuntimeError(f"P{number}: expected one theorem-frontier section, found {count}")

    text = text.replace("Previous theorem frontier · P99", "Immediate predecessor · P99")
    for number in range(86, 99):
        text = text.replace(
            f"Previous theorem frontier · P{number}",
            f"Historical theorem frontier · P{number}",
        )

    if text.count('class="theorem-frontier current-frontier-visual"') != 1:
        raise RuntimeError("Visual Atlas must have exactly one current-frontier-visual section")
    if '<section id="p100-frontier" class="theorem-frontier current-frontier-visual">' not in text:
        raise RuntimeError("P100 must be the unique current-frontier visual")

    ATLAS.write_text(text, encoding="utf-8")


def normalize_reader_metadata_and_navigation() -> None:
    text = START.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "current Research II P99 frontier.",
        "current Research II P100 frontier.",
        "Start Here metadata frontier",
    )
    START.write_text(text, encoding="utf-8")

    text = MAP.read_text(encoding="utf-8")
    text = replace_once(
        text,
        '  <a class="brand" href="index.html">Mathematical Consciousness Bridge</a>\n  <nav>',
        '  <a class="brand" href="index.html">Mathematical Consciousness Bridge</a>\n  <button class="nav-toggle" aria-label="Toggle navigation">Menu</button>\n  <nav>',
        "Research Map mobile navigation",
    )
    text = replace_once(
        text,
        '<a href="research-map.html">Research Map</a>',
        '<a href="research-map.html" aria-current="page">Research Map</a>',
        "Research Map active navigation",
    )
    MAP.write_text(text, encoding="utf-8")

    text = LINEAGE.read_text(encoding="utf-8")
    text = text.replace("20260913-mobile18-p88", "20260916-p100")
    LINEAGE.write_text(text, encoding="utf-8")


def write_contract() -> None:
    TEST.write_text(
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef _read(path: str) -> str:\n    return (ROOT / path).read_text(encoding="utf-8")\n\n\ndef test_visual_atlas_has_one_unambiguous_current_frontier() -> None:\n    atlas = _read("website/visual-atlas.html")\n    assert atlas.count('class="theorem-frontier current-frontier-visual"') == 1\n    assert '<section id="p100-frontier" class="theorem-frontier current-frontier-visual">' in atlas\n    for number in range(86, 100):\n        assert f'<section id="p{number}-frontier" class="theorem-frontier">' in atlas\n\n\ndef test_visual_atlas_explains_current_first_order() -> None:\n    atlas = _read("website/visual-atlas.html")\n    assert 'id="atlas-reading-rule"' in atlas\n    assert "this atlas is intentionally current-first" in atlas\n    assert 'research-map.html#continuous-model-frontier' in atlas\n    assert atlas.index('id="p100-frontier"') < atlas.index('id="p99-frontier"')\n    for number in range(99, 86, -1):\n        assert atlas.index(f'id="p{number}-frontier"') < atlas.index(f'id="p{number - 1}-frontier"')\n\n\ndef test_visual_atlas_frontier_labels_are_semantically_consistent() -> None:\n    atlas = _read("website/visual-atlas.html")\n    assert "Current theorem frontier · P100" in atlas\n    assert "Immediate predecessor · P99" in atlas\n    for number in range(86, 99):\n        assert f"Historical theorem frontier · P{number}" in atlas\n    assert "Previous theorem frontier · P98" not in atlas\n    assert "Previous theorem frontier · P93" not in atlas\n\n\ndef test_core_reader_navigation_has_mobile_controls_and_active_page_state() -> None:\n    atlas = _read("website/visual-atlas.html")\n    research = _read("website/research-map.html")\n    assert '<button class="nav-toggle" aria-label="Toggle navigation">Menu</button>' in atlas\n    assert '<button class="nav-toggle" aria-label="Toggle navigation">Menu</button>' in research\n    assert '<a href="visual-atlas.html" aria-current="page">Visual Atlas</a>' in atlas\n    assert '<a href="research-map.html" aria-current="page">Research Map</a>' in research\n\n\ndef test_p100_metadata_and_cache_labels_do_not_advertise_p88_or_p99() -> None:\n    start = _read("website/start-here.html")\n    lineage = _read("website/research-lineage.html")\n    assert "current Research II P100 frontier" in start\n    assert "current Research II P99 frontier" not in start\n    assert "20260913-mobile18-p88" not in lineage\n    assert "20260916-p100" in lineage\n\n\ndef test_changed_reader_surfaces_obey_punctuation_policy() -> None:\n    for path in (\n        "website/visual-atlas.html",\n        "website/start-here.html",\n        "website/research-map.html",\n        "website/research-lineage.html",\n    ):\n        text = _read(path)\n        assert "\\u2013" not in text\n        assert "\\u2014" not in text\n''',
        encoding="utf-8",
    )


def main() -> None:
    normalize_atlas()
    normalize_reader_metadata_and_navigation()
    write_contract()


if __name__ == "__main__":
    main()
