from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P60 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text: str, token: str, new_line: str, label: str) -> str:
    if new_line in text:
        return text
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if token in line:
            lines.insert(index + 1, new_line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P60 line marker: {label}")


def integrate_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## 13.33 P60 - integer transition-calibration allocation" in text:
        return
    text = replace_once(text, "version-0.59.0-2563eb", "version-0.60.0-2563eb", "README version")
    text = replace_once(
        text,
        "The public research record now contains **59 proposition-level results",
        "The public research record now contains **60 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P59", "P1 through P60")

    p59 = (
        "**P59** solves the next calibration-design layer exactly for a declared inverse-square-root uncertainty surrogate: under a fixed total transition-measurement budget, the unique continuous optimum allocates effort in proportion to the two-thirds power of each edge's combined uncertainty coefficient and sensitivity weight, with closed-form optimal uncertainty and target-budget formulas."
    )
    p60 = (
        p59
        + " **P60** converts that fractional design into whole measurement counts under a hard integer budget: reserving one rounding unit per calibrated edge, solving P59 on the remaining budget, and rounding upward yields a feasible integer allocation whose uncertainty is at most the continuous full-budget optimum multiplied by sqrt(B/(B-m))."
    )
    text = replace_once(text, p59, p60, "README abstract P59 sentence")
    text = insert_after_line(
        text,
        "[Proposition 59](docs/proposition_59_optimal_transition_calibration.md)",
        "| integer transition-calibration allocation | [Proposition 60](docs/proposition_60_integer_transition_calibration.md) | hard-budget whole-measurement construction with explicit rounding overhead and target-budget guarantee |",
        "README proposition navigation",
    )

    section = r'''
## 13.33 P60 - integer transition-calibration allocation

![P60 integer transition-calibration allocation](docs/figures/p60_integer_transition_calibration.svg)

P59 gives the mathematically ideal allocation of calibration effort, but its solution can contain fractional measurement counts. P60 makes that design directly implementable when every calibration measurement must be a whole number and the experiment has a hard total budget.

Let \(m\) be the number of calibrated transitions and let \(B>m\) be the available integer budget. P60 reserves one possible rounding unit per transition and applies the P59 continuous optimum to

\[
\boxed{B-m}
\]

units of effective budget. If \(\widetilde n_e\) is that continuous allocation, choose

\[
\boxed{k_e=\lceil\widetilde n_e\rceil.}
\]

Because each ceiling adds strictly less than one unit,

\[
\boxed{\sum_e k_e\le B.}
\]

Because increasing a calibration count can only reduce the P59 uncertainty surrogate,

\[
\boxed{U(k)\le U^*(B-m).}
\]

Comparing this with the ideal continuous optimum that could use the full budget \(B\) gives

\[
\boxed{
\frac{U(k)}{U^*(B)}
\le
\sqrt{\frac{B}{B-m}}.
}
\]

This ratio approaches one as the budget becomes large relative to the number of calibrated transitions. In practical terms, the cost of requiring whole measurements becomes negligible in the large-budget regime.

For a desired uncertainty level \(\varepsilon\), P60 also provides the explicit sufficient hard integer budget

\[
\boxed{
B\ge
m+
\left\lceil\frac{S^3}{\varepsilon^2}\right\rceil,
}
\]

where \(S=\sum_e(w_ea_e)^{2/3}\) is the P59 normalization.

The calibration chain is now

\[
\boxed{
\text{P58: quantify transition uncertainty}
\to
\text{P59: allocate divisible calibration effort optimally}
\to
\text{P60: implement the design with whole measurements}.
}
\]

P60 is a constructive guarantee, not yet an exact solution of the discrete integer optimization problem. It deliberately leaves open whether the remaining budget can be allocated by a marginal-gain rule to obtain the exact integer optimum.

[Read Proposition 60](docs/proposition_60_integer_transition_calibration.md). The [P60 theorem visual](docs/figures/p60_integer_transition_calibration.svg), [implementation](src/consciousness_bridge/integer_transition_calibration.py), and [tests](tests/test_integer_transition_calibration.py) expose the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = replace_once(text, marker, section + marker, "README P60 section")
    write(path, text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P60](proposition_60_integer_transition_calibration.md)" in text:
        return
    text = insert_after_line(
        text,
        "p59_optimal_transition_calibration.svg",
        "![P60 integer transition-calibration allocation](figures/p60_integer_transition_calibration.svg)",
        "roadmap figure",
    )
    text = insert_after_line(
        text,
        "| [P59](proposition_59_optimal_transition_calibration.md)",
        "| [P60](proposition_60_integer_transition_calibration.md) | ceiling construction applied to the P59 continuous optimum on a reserved budget | feasible whole-measurement calibration under a hard budget with explicit multiplicative overhead and target-budget bound | proved constructive integer-allocation theorem |",
        "roadmap proposition row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P60 | [Integer transition-calibration allocation]" in text:
        return
    text = text.replace("P1 through P59", "P1 through P60")
    text = insert_after_line(
        text,
        "| P59 | [Optimal transition-calibration allocation]",
        "| P60 | [Integer transition-calibration allocation](proposition_60_integer_transition_calibration.md) | implementable hard-budget whole-measurement allocation with certified rounding overhead relative to P59 |",
        "navigation proposition row",
    )
    write(path, text)


def integrate_equations() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "P60 integer transition-calibration allocation" in text:
        return
    addition = r'''

---

# P60 integer transition-calibration allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(N_0=B-m\) | effective continuous budget after reserving one possible rounding unit per calibrated edge | repository construction | [P60](proposition_60_integer_transition_calibration.md) |
| \(k_e=\lceil n_e^*(B-m)\rceil\) | implementable integer calibration allocation | repository construction | [P60](proposition_60_integer_transition_calibration.md) |
| \(\sum_e k_e\le B\) | hard-budget feasibility guarantee | proved by the ceiling inequality | [P60](proposition_60_integer_transition_calibration.md) |
| \(U(k)\le U^*(B-m)\) | integer uncertainty guarantee | proved by coordinatewise monotonicity of the P59 surrogate | [P60](proposition_60_integer_transition_calibration.md) |
| \(U(k)/U^*(B)\le\sqrt{B/(B-m)}\) | multiplicative implementation overhead relative to the full-budget continuous optimum | proved P59-P60 comparison | [P60](proposition_60_integer_transition_calibration.md) |
| \(B\ge m+\lceil S^3/\varepsilon^2\rceil\) | sufficient hard integer budget for target uncertainty \(\varepsilon\) | proved algebraic consequence | [P60](proposition_60_integer_transition_calibration.md) |

P60 proves a closed-form feasible integer construction and an overhead bound. It does not claim exact discrete optimality.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = replace_once(read(path), 'version = "0.59.0"', 'version = "0.60.0"', "pyproject version")
    if "integer transition-calibration allocation" not in text:
        text = text.replace(
            "optimal transition-calibration allocation, robust experiment design",
            "optimal transition-calibration allocation, integer transition-calibration allocation, robust experiment design",
        )
    write(path, text)

    path = "CITATION.cff"
    text = replace_once(read(path), "version: 0.59.0", "version: 0.60.0", "citation version")
    if "integer transition-calibration allocation" not in text:
        text = text.replace(
            "optimal transition-calibration allocation, robust experiment design",
            "optimal transition-calibration allocation, integer transition-calibration allocation, robust experiment design",
        )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.60.0 - 2026-09-10"):
        entry = """# 0.60.0 - 2026-09-10

- Add P60 integer transition-calibration allocation with hard-budget overhead control.
- Convert the P59 continuous optimum into whole measurement counts using a reserved-budget ceiling construction.
- Prove hard-budget feasibility and the explicit multiplicative uncertainty overhead sqrt(B/(B-m)).
- Derive a sufficient hard integer budget for a target calibration uncertainty.
- Add implementation, regression tests, theorem visual, equation provenance, and front-page integration.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(
        text,
        '    "p59_optimal_transition_calibration.svg",',
        '    "p59_optimal_transition_calibration.svg",\n    "p60_integer_transition_calibration.svg",',
        "main-page P60 visual guard",
    )
    text = text.replace("for index in range(1, 60):", "for index in range(1, 61):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.59.0-2563eb", "version-0.60.0-2563eb")
    text = text.replace('version = "0\\.59\\.0"', 'version = "0\\.60\\.0"')
    text = text.replace("version: 0\\.59\\.0", "version: 0\\.60\\.0")
    marker = (
        '        "Proposition 59",\n'
        '        "p59_optimal_transition_calibration.svg",\n'
        '        "optimal_transition_calibration.py",\n'
        '        "test_optimal_transition_calibration.py",\n'
    )
    replacement = marker + (
        '        "Proposition 60",\n'
        '        "p60_integer_transition_calibration.svg",\n'
        '        "integer_transition_calibration.py",\n'
        '        "test_integer_transition_calibration.py",\n'
    )
    text = replace_once(text, marker, replacement, "release P60 path guards")
    write(path, text)

    write(
        "tests/test_integer_transition_calibration_publication.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef test_p60_is_visible_on_main_page():\n    text = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "P60 - integer transition-calibration allocation",\n        "p60_integer_transition_calibration.svg",\n        "integer_transition_calibration.py",\n        "test_integer_transition_calibration.py",\n    ):\n        assert token in text\n\n\ndef test_p60_is_in_public_research_maps():\n    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")\n    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")\n    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")\n    assert "[P60](proposition_60_integer_transition_calibration.md)" in roadmap\n    assert "| P60 | [Integer transition-calibration allocation]" in navigation\n    assert "P60 integer transition-calibration allocation" in equations\n''',
    )


def main() -> None:
    integrate_readme()
    integrate_roadmap()
    integrate_navigation()
    integrate_equations()
    integrate_metadata()
    integrate_tests()


if __name__ == "__main__":
    main()
