from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website/research-map.html"






def test_research_map_gives_direct_audit_paths():
    text = MAP.read_text(encoding="utf-8")
    required = [
        "theorem_roadmap.md",
        "research_navigation.md",
        "equation_and_citation_map.md",
        "visual-atlas.html",
        "tests/",
        "src/consciousness_bridge/",
        "proposition_71_target_provenance_noncircularity.md",
        "proposition_72_target_measurement_channel_robustness.md",
        "proposition_73_target_channel_identifiability.md",
        "proposition_74_finite_sample_target_channel_recovery.md",
        "proposition_75_target_model_adequacy_overidentification.md",
        "proposition_76_finite_sample_target_model_adequacy.md",
        "proposition_77_full_law_model_set_separation.md",
        "proposition_78_certified_continuous_model_separation.md",
        "proposition_79_certified_sampling_radius.md",
        "proposition_80_simplex_coupled_model_separation.md",
        "proposition_81_projection_event_model_separation.md",
        "p82_equation_provenance.md",
        "proposition_82_exact_nested_projection_contrast.md",
        "p83_equation_provenance.md",
        "proposition_83_exact_projection_parity.md",
        "proposition_84_exact_projection_parity_contrast.md",
        "joint_projection_parity_contrast_separation.py",
        "test_joint_projection_parity_contrast_separation.py",
        'index.html#p88-frontier',
    ]
    for token in required:
        assert token in text, token




def test_p84_previous_frontier_is_unique_and_structurally_inside_main():
    text = MAP.read_text(encoding="utf-8")
    main_open = text.index("<main>")
    main_close = text.index("</main>")
    p84 = text.index('id="p84"')
    p84_text = text[p84:main_close]
    assert text.count('id="p84"') == 1
    assert main_open < p84 < main_close
    assert "Previous certified frontier · P84" in p84_text
    assert "Current certified frontier" not in p84_text
    assert "P84 proof" in p84_text
    assert "P84 proof" not in text[main_close:]


def test_continuous_frontier_keeps_p82_and_p83_provenance_auditable():
    text = MAP.read_text(encoding="utf-8")
    frontier = text.index('id="continuous-model-frontier"')
    main_close = text.index("</main>", frontier)
    frontier_text = text[frontier:main_close]
    assert "p82_equation_provenance.md" in frontier_text
    assert "p83_equation_provenance.md" in frontier_text
