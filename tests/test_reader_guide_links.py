from pathlib import Path

README = Path(__file__).resolve().parents[1] / "README.md"


def test_how_to_read_table_has_direct_navigation_links() -> None:
    text = README.read_text(encoding="utf-8")
    required_links = [
        "[Abstract](#abstract)",
        "[Section 1](#1-mathematical-formulation-of-the-bridge-problem)",
        "[Section 2](#2-from-physical-dynamics-to-operational-structure)",
        "[measurement map](docs/figures/conscious_state_measurement_map.svg)",
        "[P71](docs/proposition_71_target_provenance_noncircularity.md)",
        "[P72](docs/proposition_72_target_measurement_channel_robustness.md)",
        "[Theorem roadmap](docs/theorem_roadmap.md)",
        "[What has actually been established](#what-has-actually-been-established)",
        "[What remains open](#what-remains-open)",
        "[Falsification logic](#falsification-logic)",
        "[Research navigation](docs/research_navigation.md)",
        "[Detailed proposition record](docs/detailed_proposition_record.md)",
        "[Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md)",
    ]
    for link in required_links:
        assert link in text
