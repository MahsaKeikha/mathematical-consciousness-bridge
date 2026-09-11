from pathlib import Path

PATH = Path("docs/research_navigation.md")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one anchor, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    text = PATH.read_text(encoding="utf-8")

    replacements = (
        ("13. [P79 bounded target-view dependence]", "15. [P79 bounded target-view dependence]"),
        ("15. [P11-P18 and P25-P37 operational physical structure]", "16. [P11-P18 and P25-P37 operational physical structure]"),
        ("16. [P38-P44 quantum foundations and bridge tests]", "17. [P38-P44 quantum foundations and bridge tests]"),
        ("17. [P45-P60 adaptive experiment design and scheduling]", "18. [P45-P60 adaptive experiment design and scheduling]"),
        ("18. [P61-P70 Calibration and Optimization Frontier]", "19. [P61-P70 Calibration and Optimization Frontier]"),
        ("19. [Equation and citation map]", "20. [Equation and citation map]"),
        ("20. [P72 equation and provenance record]", "21. [P72 equation and provenance record]"),
        ("21. [P73 equation and provenance record]", "22. [P73 equation and provenance record]"),
        ("22. [P74 equation and provenance record]", "23. [P74 equation and provenance record]"),
        ("23. [P75 equation and provenance record]", "24. [P75 equation and provenance record]"),
        ("24. [Falsification program]", "25. [Falsification program]"),
        ("25. [P78 equation and provenance record]", "26. [P78 equation and provenance record]"),
        ("26. [Citation guide]", "27. [Citation guide]"),
    )
    for old, new in replacements:
        text = replace_once(text, old, new, f"numbering {old}")

    p78_branch = "| Certified continuous target-model separation | P78 | Supplies exact-rational global lower bounds for distance to the continuous P75 model family and a convergent mesh certificate | [P78](proposition_78_certified_continuous_model_separation.md) |"
    p79_branch = "| Bounded target-view dependence robustness | P79 | Enlarges the P75 family by an independently justified local-dependence allowance and preserves rejection beyond sampling plus dependence margins | [P79](proposition_79_bounded_target_view_dependence.md) |"
    if p79_branch not in text:
        text = replace_once(text, p78_branch, p78_branch + "\n" + p79_branch, "P79 branch-map row")

    p76_paragraph = "P76 adds finite-data discipline to that adequacy check. One simultaneous sixteen-cell confidence event is propagated to the tracked P75 polynomial constraints. Excluding zero from any necessary-constraint interval certifies model incompatibility at the stated confidence level. If no interval excludes zero, P76 reports only non-rejection, never model acceptance.\n"
    continuation = """

P77 strengthens finite-data adequacy from selected necessary constraints to the complete declared observed-law model set. A full-law rejection requires the simultaneous empirical-law confidence region to be separated from the entire model family. A candidate numerical fit supplies an upper bound on model distance, so it cannot by itself certify rejection of a continuous family.

P78 supplies the missing certified global lower-bound mechanism for the continuous P75 family. Exact-rational multi-affine box refinement lower-bounds the distance to every model in the complete parameter cube, while explicit parameter points provide upper bounds. The lower bound converges under refinement and hands directly into the P77 rejection gate.

P79 weakens exact conditional independence of the target views by adding an independently justified residual-dependence allowance. The resulting population law must stay within that allowance of the P75 family, so robust rejection requires the certified P78 separation to exceed both P77 sampling uncertainty and the P79 dependence budget. The allowance must not be chosen post hoc from the same discrepancy merely to prevent rejection.
"""
    if "P79 weakens exact conditional independence of the target views" not in text:
        text = replace_once(text, p76_paragraph, p76_paragraph + continuation, "P79 bridge-interface continuation")

    p76_figure = "| [P76 figure](figures/p76_finite_sample_target_model_adequacy.svg) | shared finite-sample confidence event, polynomial adequacy intervals, certified rejection, and the non-rejection boundary |"
    extra_figures = """| [P77 figure](figures/p77_full_law_model_set_separation.svg) | full-law confidence-region separation and the lower-bound versus best-fit distinction |
| [P78 figure](figures/p78_certified_continuous_model_separation.svg) | exact-rational box refinement, global lower bounds, upper bounds, and the P77 handoff |
| [P79 figure](figures/p79_bounded_target_view_dependence.svg) | local-dependence defect, robustness envelope, and the sampling-plus-dependence rejection margin |"""
    if "[P79 figure](figures/p79_bounded_target_view_dependence.svg)" not in text:
        text = replace_once(text, p76_figure, p76_figure + "\n" + extra_figures, "P79 figure routes")

    old_evidence = "Use the [Equation and citation map](equation_and_citation_map.md) to distinguish standard identities, repository derivations, and externally supported scientific claims. Use the [P72 provenance record](p72_equation_provenance.md), [P73 provenance record](p73_equation_provenance.md), [P74 provenance record](p74_equation_provenance.md), [P75 provenance record](p75_equation_provenance.md), and [P76 provenance record](p76_equation_provenance.md) for target-side equation classification."
    new_evidence = "Use the [Equation and citation map](equation_and_citation_map.md) to distinguish standard identities, repository derivations, and externally supported scientific claims. Use the [P72 provenance record](p72_equation_provenance.md), [P73 provenance record](p73_equation_provenance.md), [P74 provenance record](p74_equation_provenance.md), [P75 provenance record](p75_equation_provenance.md), [P76 provenance record](p76_equation_provenance.md), [P77 provenance record](p77_equation_provenance.md), [P78 provenance record](p78_equation_provenance.md), and [P79 provenance record](p79_equation_provenance.md) for target-side equation classification."
    text = replace_once(text, old_evidence, new_evidence, "P79 provenance routes")

    old_frontier = "The research remains an ongoing mathematical-physics program. The current theorem frontier is P76, but the physical-to-experiential bridge itself remains open."
    new_frontier = "The research remains an ongoing mathematical-physics program. The current theorem frontier is P79, but the physical-to-experiential bridge itself remains open."
    text = replace_once(text, old_frontier, new_frontier, "P79 navigation frontier")

    PATH.write_text(text, encoding="utf-8")
    print("P79 navigation cleanup: PASS")


if __name__ == "__main__":
    main()
