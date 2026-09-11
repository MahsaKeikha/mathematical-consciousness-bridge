from pathlib import Path

README = Path(__file__).resolve().parents[1] / "README.md"


def test_how_to_read_table_has_direct_navigation_links() -> None:
    text = README.read_text(encoding="utf-8")
    required_links = [
        "[Abstract](#abstract)",
        "[core scientific thesis](#the-core-scientific-thesis-in-one-view)",
        "[Research at a glance](#research-at-a-glance)",
        "[Section 1: Mathematical formulation of the bridge problem](#1-mathematical-formulation-of-the-bridge-problem)",
        "[Section 2](#2-from-physical-dynamics-to-operational-structure)",
        "[Section 3](#3-time-composition-and-scale-cannot-be-ignored)",
        "[Section 4](#4-turning-a-population-theorem-into-a-finite-experiment)",
        "[measurement map](docs/figures/conscious_state_measurement_map.svg)",
        "[response-geometry map](docs/figures/information_geometry_response_manifold.svg)",
        "[Scientific status discipline](#scientific-status-discipline)",
        "[Theorem roadmap](docs/theorem_roadmap.md)",
        "[What has actually been established](#what-has-actually-been-established)",
        "[Falsification logic](#falsification-logic)",
        "[Falsification program](docs/falsification_program.md)",
        "[What remains open](#what-remains-open)",
        "[Current scientific status](#current-scientific-status)",
        "[Research navigation](docs/research_navigation.md)",
        "[Detailed proposition record](docs/detailed_proposition_record.md)",
        "[Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md)",
    ]
    for link in required_links:
        assert link in text
