from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected exactly one {label}, found {count}")
    return text.replace(old, new, 1)


def patch_roadmap() -> None:
    path = ROOT / "docs" / "theorem_roadmap.md"
    text = path.read_text(encoding="utf-8")

    start = text.index("&\\text{P89: complete linear parity-functional duality")
    end = text.index("&\\text{P91:", start)
    dependency = r'''&\text{P89: complete linear parity-functional duality closes all real linear directions on the eleven canonical parity coordinates}\\
&\Downarrow\\
&\text{P90: nonlinear rank-one slice identity yields exact strict-box distance 5/72 beyond the complete P89 linear envelope}\\
&\Downarrow\\
'''
    text = text[:start] + dependency + text[end:]

    table_start = text.index(
        "| [P89](proposition_89_complete_linear_parity_duality.md) |"
    )
    section4 = text.index("## 4. Calibration branch remains separate", table_start)
    table_tail = '''| [P89](proposition_89_complete_linear_parity_duality.md) | complete real linear parity-functional duality | removes coefficient-radius/support cutoffs and gives matching exact lower/upper certificates | proved conditional computational theorem |
| [P90](proposition_90_exact_nonlinear_rank_one_separation.md) | nonlinear rank-one slice identity | exact single-component strict-box model separation at 5/72 | proved conditional nonlinear theorem |
| [P91](proposition_91_mixed_prevalence_rank_two_flattening_separation.md) | rank-two bipartite flattening and exact 3 by 3 minor interval exclusion | full mixed-prevalence P75 separation bracket `1/42 < d_inf <= 1/24` | proved conditional nonlinear theorem |
| [P92](proposition_92_exact_global_mixed_prevalence_distance.md) | three-minor conditional sign coherence | exact full-cube mixed-prevalence P75 distance `d_inf = 1/24` | proved conditional nonlinear theorem |
| [P93](proposition_93_localized_sign_coherence_rejection.md) | seven-cell finite-sample sign preservation | localized IID rejection of P75 | proved conditional statistical theorem |
| [P94](proposition_94_finite_range_dependent_sign_coherence.md) | finite-range coloring, Holder-Hoeffding concentration, exact rational radius certification | localized finite-range dependent rejection plus temporal-pooling no-go | proved conditional statistical theorem |
| [P95](proposition_95_drift_aware_stratified_sign_coherence.md) | predeclared drift regimes, local P94 gates, familywise error allocation | drift-aware rejection of the all-regimes P75 null | proved conditional statistical theorem |
| [P96](proposition_96_selection_valid_holdout_stratification.md) | pilot selection with independent holdout certification | post-selection-valid drift-regime certification under a frozen plan | proved conditional statistical theorem |
| [P97](proposition_97_simultaneous_candidate_family_selection.md) | simultaneous finite-family error accounting | same-data selection over a finite predeclared candidate family | proved conditional statistical theorem |
| [P98](proposition_98_cross_fitted_selection_valid_certification.md) | rotated independent-block holdouts and foldwise error control | cross-fitted selection-valid certification without own-fold leakage | proved conditional statistical theorem |
| [P99](proposition_99_cross_fitted_evalue_aggregation.md) | conditional e-values and convex cross-fold aggregation | distributed cross-fitted evidence accumulation without fold independence | proved conditional statistical theorem |
| [P100](proposition_100_anytime_sequential_eprocess.md) | predictable reserve stakes, supermartingale products, and Ville control | anytime-valid repeated inspection and stopping across fresh P99 rounds | proved conditional sequential inference theorem |

'''
    text = text[:table_start] + table_tail + text[section4:]

    frontier_start = text.index("## 5. Current open frontier")
    frontier_end = text.index("## P83 predecessor frontier:", frontier_start)
    frontier = '''## 5. Current frontier and remaining scientific boundary

Through P100, the target-side chain now separates several obligations that must not be collapsed into one claim:

1. target provenance must be non-circular relative to the physical descriptor being tested;
2. the target-observation channel must be scientifically defensible and sufficiently informative for the claimed witness;
3. channel reliability must be identified or externally calibrated under a declared measurement model;
4. finite data must resolve the channel far enough from singularity for recovery to be certified;
5. the target-measurement model must survive adequacy tests rather than being accepted because it can be fit;
6. finite data must separate genuine adequacy failure from sampling noise before rejection is claimed;
7. full-law rejection must be defined against the complete declared model family;
8. continuous-family separation must use a certified global lower bound rather than a local optimizer value;
9. the sampling-radius side of the rejection gate must have a certified upper direction;
10. computational relaxations must preserve the lower-bound direction while retaining as much exact probability structure as possible;
11. nonlinear structure beyond the complete P89 linear parity envelope must be tested explicitly rather than inferred from linear closure;
12. temporal drift and finite-range dependence must be handled by declared local laws and valid error allocation rather than uncontrolled pooling;
13. post-selection certification must use an independent holdout, simultaneous finite-family control, or leakage-free cross-fitting under its stated assumptions; and
14. repeated inspection and stopping across fresh rounds must preserve conditional e-value validity with predictable stakes.

P78-P89 build the certified continuous-family and parity-separation machinery, ending with the complete real linear parity-functional certificate on the declared eleven-coordinate family. P90-P92 move beyond that linear closure with nonlinear rank and sign-coherence structure and close the declared mixed-prevalence P75 distance at the exact witness value `1/24`.

P93-P95 convert that population obstruction into localized finite-sample, finite-range dependent, and drift-aware rejection statements. P96-P98 then protect regime selection through independent holdout certification, simultaneous finite candidate-family control, and rotated independent-block cross-fitting. P99 converts valid fold-level rejection evidence into exact e-values and aggregates them without requiring fold independence. P100 adds the outer sequential layer: fresh P99 rounds may be inspected repeatedly and stopped adaptively when current-round conditional validity and predictable-stake requirements hold.

None of P71-P100 identifies a latent variable with consciousness. None proves that failure of one declared physical descriptor implies nonphysical consciousness. Non-rejection does not establish model truth. The physical-to-experiential bridge remains open.


'''
    text = text[:frontier_start] + frontier + text[frontier_end:]
    path.write_text(text, encoding="utf-8")


def patch_reader_sources() -> None:
    research_map_path = ROOT / "website" / "research-map.html"
    research_map = research_map_path.read_text(encoding="utf-8")
    research_map = replace_once(
        research_map,
        "Scientific dependency map of the Mathematical Consciousness Bridge through Proposition 99.",
        "Scientific dependency map of the Mathematical Consciousness Bridge through Proposition 100.",
        "stale Research Map meta description",
    )
    research_map_path.write_text(research_map, encoding="utf-8")

    plain_path = ROOT / "website" / "plain-language.html"
    plain = plain_path.read_text(encoding="utf-8")
    for old, new in (
        (
            "A 99-result sufficiency and falsification architecture",
            "A 100-result sufficiency and falsification architecture",
        ),
        ("currently through P99.", "currently through P100."),
        ("The 99-result proposition program asks", "The 100-result proposition program asks"),
        ("The current theorem frontier is P99.", "The current theorem frontier is P100."),
    ):
        if old not in plain:
            raise SystemExit(f"Expected stale plain-language phrase: {old}")
        plain = plain.replace(old, new)
    plain_path.write_text(plain, encoding="utf-8")


def write_regression_test() -> None:
    path = ROOT / "tests" / "test_p100_roadmap_coherence.py"
    path.write_text(
        '''from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def test_complete_proposition_index_is_one_contiguous_p1_p100_table() -> None:
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    block = roadmap.split("## 3. Complete proposition index", 1)[1].split(
        "## 4. Calibration branch remains separate", 1
    )[0]
    rows = re.findall(r"^\\| \\[P(\\d+)\\]\\(", block, flags=re.MULTILINE)
    assert rows == [str(number) for number in range(1, 101)]
    assert "\\n\\n| [P90]" not in block
    assert "\\n\\n| [P96]" not in block


def test_p100_roadmap_frontier_language_is_current() -> None:
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    assert "## 5. Current frontier and remaining scientific boundary" in roadmap
    assert "None of P71-P100 identifies a latent variable with consciousness." in roadmap
    assert "After P89, the target-side chain" not in roadmap
    assert "None of P71-P95" not in roadmap


def test_static_reader_sources_are_p100_current() -> None:
    research_map = (ROOT / "website" / "research-map.html").read_text(encoding="utf-8")
    plain = (ROOT / "website" / "plain-language.html").read_text(encoding="utf-8")
    assert "through Proposition 100" in research_map
    assert "through Proposition 99" not in research_map
    assert "A 100-result sufficiency and falsification architecture" in plain
    assert "The 100-result proposition program asks" in plain
    assert "The current theorem frontier is P100." in plain
    assert "A 99-result sufficiency and falsification architecture" not in plain
    assert "The 99-result proposition program asks" not in plain
    assert "The current theorem frontier is P99." not in plain
''',
        encoding="utf-8",
    )


if __name__ == "__main__":
    patch_roadmap()
    patch_reader_sources()
    write_regression_test()
