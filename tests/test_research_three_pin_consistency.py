from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT_RESEARCH_III_PIN = "3cf9202977953644c980246c1f3e46a3514b3a4a"
PREVIOUS_RESEARCH_III_PIN = "5d1d979231aed62fde34383281fa8f252a3d2fa7"

PUBLIC_SURFACES = (
    ROOT / "website" / "measurement-science.html",
    ROOT / "website" / "index.html",
    ROOT / "website" / "research-lineage.html",
    ROOT / "website" / "source-section-visuals.js",
    ROOT / "website" / "research-iii-atlas-refresh.js",
    ROOT / "website" / "atlas-architecture-refresh.js",
)


def test_all_public_research_three_surfaces_share_current_pin() -> None:
    for path in PUBLIC_SURFACES:
        text = path.read_text(encoding="utf-8")
        assert CURRENT_RESEARCH_III_PIN in text, f"{path} is not on the current Research III pin"
        assert PREVIOUS_RESEARCH_III_PIN not in text, f"{path} still exposes the previous Research III pin"


def test_synchronizer_declares_current_pin_and_migrates_previous_pin() -> None:
    sync = (ROOT / "scripts" / "synchronize_research_three_website.py").read_text(
        encoding="utf-8"
    )
    assert f'CURRENT_RESEARCH_THREE_PIN = "{CURRENT_RESEARCH_III_PIN}"' in sync
    assert f'    "{PREVIOUS_RESEARCH_III_PIN}",' in sync


def test_visual_and_narrative_pin_contract_is_not_split() -> None:
    narrative = (
        ROOT / "website" / "measurement-science.html",
        ROOT / "website" / "index.html",
        ROOT / "website" / "research-lineage.html",
    )
    visuals = (
        ROOT / "website" / "source-section-visuals.js",
        ROOT / "website" / "research-iii-atlas-refresh.js",
        ROOT / "website" / "atlas-architecture-refresh.js",
    )
    assert all(CURRENT_RESEARCH_III_PIN in path.read_text(encoding="utf-8") for path in narrative)
    assert all(CURRENT_RESEARCH_III_PIN in path.read_text(encoding="utf-8") for path in visuals)
