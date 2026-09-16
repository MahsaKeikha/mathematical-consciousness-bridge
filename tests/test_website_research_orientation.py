import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website/research-map.html"
VERIFIER = ROOT / "scripts" / "verify_repository.py"


def _frontier() -> int:
    text = VERIFIER.read_text(encoding="utf-8")
    match = re.search(r'^CURRENT_FRONTIER = "P(\d+)"$', text, flags=re.MULTILINE)
    assert match is not None
    return int(match.group(1))


def _proof_name(number: int) -> str:
    matches = list((ROOT / "docs").glob(f"proposition_{number}_*.md"))
    assert len(matches) == 1
    return matches[0].name


def test_research_map_gives_direct_audit_paths():
    frontier = _frontier()
    text = MAP.read_text(encoding="utf-8")
    required = [
        "theorem_roadmap.md",
        "research_navigation.md",
        "equation_and_citation_map.md",
        "visual-atlas.html",
        "proposition_71_target_provenance_noncircularity.md",
        "proposition_72_target_measurement_channel_robustness.md",
        "proposition_73_target_channel_identifiability.md",
        "proposition_77_full_law_model_set_separation.md",
        "proposition_78_certified_continuous_model_separation.md",
        "proposition_79_certified_sampling_radius.md",
        "proposition_80_simplex_coupled_model_separation.md",
        "proposition_81_projection_event_model_separation.md",
        "proposition_82_exact_nested_projection_contrast.md",
        "proposition_83_exact_projection_parity.md",
        "proposition_84_exact_projection_parity_contrast.md",
        "proposition_85_exact_triple_projection_parity_functional.md",
        "proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md",
        "proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md",
        "proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md",
        "proposition_89_complete_linear_parity_duality.md",
        "proposition_90_exact_nonlinear_rank_one_separation.md",
        "proposition_91_mixed_prevalence_rank_two_flattening_separation.md",
        "proposition_92_exact_global_mixed_prevalence_distance.md",
        "p92_equation_provenance.md",
        _proof_name(frontier),
        f"p{frontier}_equation_provenance.md",
        f"index.html#p{frontier}-frontier",
    ]
    for token in required:
        assert token in text, token

    assert "P73-P76" in text
    assert "P74 adds finite-data recovery" in text
    assert "P75 introduces fourth-view overidentification" in text
    assert "P76 turns its necessary restrictions into finite-sample rejection certificates" in text
    assert 'index.html#p91-frontier' not in text
    assert 'index.html#p88-frontier' not in text


def test_research_map_current_frontier_labels_do_not_lag():
    frontier = _frontier()
    text = MAP.read_text(encoding="utf-8")
    assert f"through Proposition {frontier}." in text
    assert f"The current theorem frontier is P{frontier}." in text
    assert f"Research Map · Current theorem frontier P{frontier}</p>" in text
    assert f"P77-P{frontier}" in text
    assert f"P{frontier} remains a conditional model-rejection theorem" in text


def test_continuous_model_frontier_is_strictly_ordered_inside_main():
    text = MAP.read_text(encoding="utf-8")
    main_open = text.index("<main>")
    main_close = text.index("</main>")
    positions = [text.index(f'id="p{number}-research-map"') for number in range(77, 101)]

    assert positions == sorted(positions)
    assert main_open < positions[0] < positions[-1] < main_close
    for number in range(77, 101):
        assert text.count(f'id="p{number}-research-map"') == 1

    assert 'id="historical-frontiers"' not in text
    assert 'id="p87-reader-frontier"' not in text
    assert "Historical P90 checkpoint" not in text
    assert "P100 - Current theorem frontier" in text[positions[-1]:main_close]

def test_continuous_frontier_keeps_lineage_and_current_provenance_auditable():
    text = MAP.read_text(encoding="utf-8")
    begin = text.index("<!-- BEGIN CONTINUOUS MODEL FRONTIER -->")
    end = text.index("<!-- END CONTINUOUS MODEL FRONTIER -->")
    frontier_text = text[begin:end]

    for number in range(77, 101):
        assert f'id="p{number}-research-map"' in frontier_text
        assert _proof_name(number) in frontier_text

    assert frontier_text.index('id="p90-research-map"') < frontier_text.index('id="p91-research-map"')
    assert frontier_text.index('id="p99-research-map"') < frontier_text.index('id="p100-research-map"')
    assert "P100 - Current theorem frontier" in frontier_text
    assert "p100_equation_provenance.md" in text
