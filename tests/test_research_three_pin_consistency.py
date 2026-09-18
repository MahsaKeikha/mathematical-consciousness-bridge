from __future__ import annotations

import shutil
from pathlib import Path

from scripts.synchronize_research_three_website import (
    CURRENT_RESEARCH_THREE_PIN,
    LEGACY_RESEARCH_THREE_PINS,
    synchronize_site,
)

ROOT = Path(__file__).resolve().parents[1]
CURRENT_RESEARCH_III_PIN = "b3f240f2c7c8fa4c94667d2fea4d8f9f07df360c"

KEY_PUBLIC_SURFACES = (
    "measurement-science.html",
    "visual-atlas.html",
    "sources.html",
    "index.html",
    "research-lineage.html",
    "source-section-visuals.js",
    "research-iii-atlas-refresh.js",
    "atlas-architecture-refresh.js",
    "research-orientation.js",
)


def test_synchronizer_declares_exact_v1_v30_pin() -> None:
    assert CURRENT_RESEARCH_THREE_PIN == CURRENT_RESEARCH_III_PIN
    assert "a9ef67ed15595c26b0c9f4e449f53f8078d6a1ee" in LEGACY_RESEARCH_THREE_PINS
    assert "64b2bc47461fe110b135080f8dc70883552d6fd9" in LEGACY_RESEARCH_THREE_PINS
    assert "7a2a1a3a60263e48b7a268642eecc6941e84d1b4" in LEGACY_RESEARCH_THREE_PINS
    assert "d93e768d9a7d6054ff208de2a1b9c14e79192bc5" in LEGACY_RESEARCH_THREE_PINS
    assert "771bca04b92cf775eb4f75fb3b576be6f43e0940" in LEGACY_RESEARCH_THREE_PINS


def test_primary_dynamic_research_three_surfaces_are_authored_on_current_pin() -> None:
    for relative in ("research-orientation.js", "research-iii-atlas-refresh.js"):
        text = (ROOT / "website" / relative).read_text(encoding="utf-8")
        assert CURRENT_RESEARCH_III_PIN in text


def test_synchronizer_normalizes_all_public_research_three_surfaces(tmp_path: Path) -> None:
    site = tmp_path / "website"
    shutil.copytree(ROOT / "website", site)

    changed = synchronize_site(site, write=True)
    assert changed
    assert synchronize_site(site, write=False) == []

    for relative in KEY_PUBLIC_SURFACES:
        text = (site / relative).read_text(encoding="utf-8")
        assert CURRENT_RESEARCH_III_PIN in text, f"{relative} is not on the current pin"
        for legacy in LEGACY_RESEARCH_THREE_PINS:
            assert legacy not in text, f"{relative} still contains legacy pin {legacy}"


def test_visual_and_narrative_pin_contract_is_not_split_after_sync(tmp_path: Path) -> None:
    site = tmp_path / "website"
    shutil.copytree(ROOT / "website", site)
    synchronize_site(site, write=True)

    narrative = (
        site / "measurement-science.html",
        site / "index.html",
        site / "research-lineage.html",
        site / "research-orientation.js",
    )
    visuals = (
        site / "source-section-visuals.js",
        site / "research-iii-atlas-refresh.js",
        site / "atlas-architecture-refresh.js",
    )
    assert all(CURRENT_RESEARCH_III_PIN in path.read_text(encoding="utf-8") for path in narrative)
    assert all(CURRENT_RESEARCH_III_PIN in path.read_text(encoding="utf-8") for path in visuals)
