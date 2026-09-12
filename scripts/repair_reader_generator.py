"""One-time repair for the canonical Visual Atlas reading-key generator."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "enrich_figure_documentation.py"


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    pattern = re.compile(
        r"    reading_key = \(\n.*?\n    \)\n    if reading_key\.strip\(\) not in text:\n"
        r"        if hero not in text:\n"
        r"            raise RuntimeError\(\"visual atlas hero marker not found\"\)\n"
        r"        text = text\.replace\(hero, hero \+ reading_key, 1\)\n",
        flags=re.DOTALL,
    )
    replacement = '''    legacy_reading_key = (\n        '\\n<section class="boundary"><h2>How to read every figure</h2>'\n        '<p><strong>What you are seeing:</strong> identify the mathematical objects, panels, axes, or regions. '\n        '<strong>How to read it:</strong> follow arrows only as the declared logical, temporal, set-inclusion, or computational relation; compare plotted quantities using the labeled axes and legends. '\n        '<strong>Main takeaway:</strong> use the accompanying text to identify the precise conclusion the visual supports. '\n        '<strong>Scientific boundary:</strong> diagrams, synthetic examples, and simulations do not become empirical consciousness evidence merely because they are visually compelling.</p>'\n        '<p>For a direct index of every SVG, including figures not selected for this web page, open the '\n        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_catalog.md">Complete Figure Catalog</a>. '\n        'The repository-wide rules are in the '\n        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_caption_and_description_standard.md">Figure Caption and Description Standard</a>.</p></section>\\n'\n    )\n    reading_key = (\n        '\\n<section class="boundary"><h2>How to read every figure</h2>'\n        '<p><strong>What you are seeing:</strong> identify the mathematical objects, panels, axes, or regions. '\n        '<strong>How to read it:</strong> follow arrows only as the declared logical, temporal, set-inclusion, or computational relation; compare plotted quantities using the labeled axes and legends. '\n        '<strong>Main takeaway:</strong> use the accompanying text to identify the precise conclusion the visual supports. '\n        '<strong>Scientific boundary:</strong> diagrams, synthetic examples, and simulations do not become empirical consciousness evidence merely because they are visually compelling.</p>'\n        '<p>Figures are intentionally capped at a readable page size: large enough to inspect, but not so large that the explanatory text disappears below the fold. Complex theorem figures use a wider presentation than simple atlas thumbnails, and the full-resolution SVG remains available from the figure link.</p>'\n        '<p>For a direct index of every SVG, including figures not selected for this web page, open the '\n        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_catalog.md">Complete Figure Catalog</a>. '\n        'The repository-wide rules are in the '\n        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_caption_and_description_standard.md">Figure Caption and Description Standard</a> and the '\n        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/reader_experience_and_visual_standard.md">Reader Experience and Visual Presentation Standard</a>.</p></section>\\n'\n    )\n    if legacy_reading_key.strip() in text and reading_key.strip() in text:\n        text = text.replace(legacy_reading_key, "", 1)\n    elif legacy_reading_key.strip() in text:\n        text = text.replace(legacy_reading_key, reading_key, 1)\n    elif reading_key.strip() not in text:\n        if hero not in text:\n            raise RuntimeError("visual atlas hero marker not found")\n        text = text.replace(hero, hero + reading_key, 1)\n'''
    updated, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"expected one Visual Atlas reading-key block, found {count}")
    TARGET.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
