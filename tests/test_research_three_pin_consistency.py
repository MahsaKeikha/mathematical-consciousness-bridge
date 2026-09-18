from __future__ import annotations

import shutil
from pathlib import Path

from scripts.synchronize_research_three_website import (
    CURRENT_RESEARCH_THREE_PIN,
    LEGACY_RESEARCH_THREE_PINS,
    synchronize_site,
)

ROOT = Path(__file__).resolve().parents[1]
CURRENT_RESEARCH_III_PIN = "0072642d93d77fa594634a643e46e73769af0655"

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


def test_synchronizer_declares_exact_v1_v45_pin() -> None:
    assert CURRENT_RESEARCH_THREE_PIN == CURRENT_RESEARCH_III_PIN
    assert "a9ef67ed15595c26b0c9f4e449f53f8078d6a1ee" in LEGACY_RESEARCH_THREE_PINS
    assert "64b2bc47461fe110b135080f8dc70883552d6fd9" in LEGACY_RESEARCH_THREE_PINS
    assert "7a2a1a3a60263e48b7a268642eecc6941e84d1b4" in LEGACY_RESEARCH_THREE_PINS
    assert "d93e768d9a7d6054ff208de2a1b9c14e79192bc5" in LEGACY_RESEARCH_THREE_PINS
    assert "e5063b0ac1e85577dd3e1a7c4c4003c122210d48" in LEGACY_RESEARCH_THREE_PINS
    assert "c6415f2d50d68b664860f43e9da440d0a36c2997" in LEGACY_RESEARCH_THREE_PINS
    assert "0cd578fb553ab19006155a563c484511b4271a5f" in LEGACY_RESEARCH_THREE_PINS
    assert "b3f240f2c7c8fa4c94667d2fea4d8f9f07df360c" in LEGACY_RESEARCH_THREE_PINS
    assert "771bca04b92cf775eb4f75fb3b576be6f43e0940" in LEGACY_RESEARCH_THREE_PINS


def test_primary_dynamic_research_three_surfaces_are_authored_on_current_pin() -> None:
    for relative in ("research-orientation.js", "research-iii-atlas-refresh.js"):
        text = (ROOT / "website" / relative).read_text(encoding="utf-8")
        assert CURRENT_RESEARCH_III_PIN in text


def test_synchronizer_normalizes_all_public_research_three_surfaces(tmp_path: Path) -> None:
    site = tmp_path / "website"
    shutil.copytree(ROOT / "website", site)

    # The committed public site is already canonical, so synchronization must
    # be idempotent rather than manufacturing a change on every build.
    assert synchronize_site(site, write=False) == []

    # Recreate a genuinely stale public state and verify that every declared
    # Research III surface is repaired back to the immutable current snapshot.
    legacy_pin = LEGACY_RESEARCH_THREE_PINS[0]
    for relative in KEY_PUBLIC_SURFACES:
        path = site / relative
        text = path.read_text(encoding="utf-8")
        assert CURRENT_RESEARCH_III_PIN in text
        path.write_text(
            text.replace(CURRENT_RESEARCH_III_PIN, legacy_pin),
            encoding="utf-8",
        )

    changed = synchronize_site(site, write=True)
    assert set(KEY_PUBLIC_SURFACES).issubset(set(changed))
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


def test_synchronizer_preserves_validation_band_accessibility_ranges(tmp_path: Path) -> None:
    site = tmp_path / "website"
    shutil.copytree(ROOT / "website", site)
    synchronize_site(site, write=True)

    page = (site / "measurement-science.html").read_text(encoding="utf-8")
    assert 'aria-label="V11 to V15 validation sequence"' in page
    assert 'aria-label="V11 to V17 validation sequence"' not in page
    assert 'aria-label="V11 to V18 validation sequence"' not in page
