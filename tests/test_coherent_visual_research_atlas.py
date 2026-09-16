from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"


def _reader_script() -> str:
    return (WEBSITE / "reader-links.js").read_text(encoding="utf-8")


def test_visual_atlas_indexes_every_proposition_exactly_once() -> None:
    script = _reader_script()
    match = re.search(
        r"const PROPOSITION_DOC_SLUGS = \[(.*?)\];",
        script,
        flags=re.DOTALL,
    )
    assert match is not None

    slugs = re.findall(r"^\s*'([^']+)',\s*$", match.group(1), flags=re.MULTILINE)
    assert len(slugs) == 100
    assert len(set(slugs)) == 100
    assert slugs[0] == "representation_invariance"
    assert slugs[18] == "fundamental_physical_sufficiency"
    assert slugs[70] == "target_provenance_noncircularity"
    assert slugs[-1] == "anytime_sequential_eprocess"


def test_visual_atlas_preserves_canonical_proposition_links() -> None:
    script = _reader_script()
    assert "docs/proposition_${number}_${slug}.md" in script
    assert "P1-P100 in one visual, searchable index" in script
    assert "Canonical proposition record" in script
    assert "Open proof record →" in script
    assert "P71-P100 returns to the bridge-sufficiency lineage" in script


def test_visual_atlas_is_searchable_filterable_and_grouped() -> None:
    script = _reader_script()
    for domain in (
        "foundations",
        "physical-structure",
        "bridge-sufficiency",
        "operational-scale",
        "quantum-interface",
        "adaptive-evidence",
        "calibration",
        "target-audit",
    ):
        assert f"id: '{domain}'" in script

    assert 'id="atlas-search"' in script
    assert 'id="atlas-domain-filter"' in script
    assert "atlas.querySelectorAll('.proposition-atlas-card')" in script
    assert "group.hidden = !hasVisibleCard" in script


def test_sitewide_research_spine_exposes_guided_scientific_path() -> None:
    script = _reader_script()
    assert "function addResearchSpine()" in script
    assert "Guided research path" in script
    assert "Research I" in script
    assert "Research II" in script
    assert "Research III" in script
    assert "Visual Atlas" in script
    assert "Provenance and tests" in script
    assert "aria-current" in script


def test_existing_clickable_result_behavior_remains_guarded() -> None:
    script = _reader_script()
    assert "function normalizeResearchMapResultBoxes()" in script
    assert "function wireWholeResultCard(card)" in script
    assert "function wireAllResultCards()" in script
    assert "event.key !== 'Enter' && event.key !== ' '" in script
    assert "a, button, input, select, textarea, summary" in script
