from __future__ import annotations

import shutil
from pathlib import Path

from scripts.synchronize_research_three_website import (
    CURRENT_RESEARCH_THREE_PIN,
    LEGACY_RESEARCH_THREE_PINS,
    synchronize_site,
)

ROOT = Path(__file__).resolve().parents[1]
CURRENT_RESEARCH_III_PIN = "a9ef67ed15595c26b0c9f4e449f53f8078d6a1ee"

KEY_PUBLIC_SURFACES = (
    "measurement-science.html",
    "index.html",
    "research-lineage.html",
    "source-section-visuals.js",
    "research-iii-atlas-refresh.js",
    "atlas-architecture-refresh.js",
    "research-orientation.js",
)


def test_synchronizer_declares_exact_merged_v1_v10_pin() -> None:
    assert CURRENT_RESEARCH_THREE_PIN == CURRENT_RESEARCH_III_PIN
    assert "3cf9202977953644c980246c1f3e46a3514b3a4a" in LEGACY_RESEARCH_THREE_PINS


def test_new_primary_research_three_surfaces_are_authored_on_current_pin() -> None:
    authored = (
        ROOT / "website" / "measurement-science.html",
        ROOT / "website" / "research-iii-atlas-refresh.js",
        ROOT / "website" / "research-orientation.js",
    )
    for path in authored:
        assert CURRENT_RESEARCH_III_PIN in path.read_text(encoding="utf-8")


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
