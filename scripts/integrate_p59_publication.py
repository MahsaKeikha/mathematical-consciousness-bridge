from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P59 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text: str, token: str, new_line: str, label: str) -> str:
    if new_line in text:
        return text
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if token in line:
            lines.insert(index + 1, new_line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P59 line marker: {label}")


def integrate_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## 13.32 P59 - optimal transition-calibration allocation" in text:
        return

    text = replace_once(text, "version-0.58.0-2563eb", "version-0.59.0-2563eb", "README version")
    text = replace_once(
        text,
        "The public research record now contains **58 proposition-level results",
        "The public research record now contains **59 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P58", "P1 through P59")

    p58 = (
        "**P58** removes the known-metric restriction: bounded noisy pairwise transition measurements generate simultaneous edge-confidence intervals, whose lower and upper route envelopes bracket the unknown true P54 optimum without requiring the empirical center itself to satisfy the triangle inequality. The upper-envelope minimizer is a robust route, and the envelope width certifies its worst-case regret on the shared confidence event."
    )
    p59 = (
        p58
        + " **P59** solves the next calibration-design layer exactly for a declared inverse-square-root uncertainty surrogate: under a fixed total transition-measurement budget, the unique continuous optimum allocates effort in proportion to the two-thirds power of each edge's combined uncertainty coefficient and sensitivity weight, with closed-form optimal uncertainty and target-budget formulas."
    )
    text = replace_once(text, p58, p59, "README abstract P58 sentence")

    text = insert_after_line(
        text,
        "[Proposition 58](docs/proposition_58_finite_data_metric_uncertainty.md)",
        "| optimal transition-calibration allocation | [Proposition 59](docs/proposition_59_optimal_transition_calibration.md) | exact two-thirds-power allocation of a fixed calibration budget for the P58 inverse-square-root uncertainty surrogate |",
        "README proposition navigation",
    )

    section = r'''
## 13.32 P59 - optimal transition-calibration allocation

![P59 optimal transition-calibration allocation](docs/figures/p59_optimal_transition_calibration.svg)

P58 tells us how uncertainty in measured transition costs propagates into uncertainty about the best experimental route. P59 asks the next practical question: if transition measurements themselves cost time or resources, where should a limited calibration budget be spent?

For each calibrated transition edge \(e\), suppose its uncertainty radius has the form

\[
\rho_e(n_e)=\frac{a_e}{\sqrt{n_e}},
\]

where \(n_e\) is the calibration effort allocated to that transition and \(a_e\) summarizes how difficult that transition is to estimate. Let \(w_e>0\) be a declared sensitivity weight describing how strongly that edge contributes to the chosen route-uncertainty surrogate.

P59 minimizes

\[
\boxed{
U(n)=\sum_e\frac{w_ea_e}{\sqrt{n_e}}
}
\]

subject to a fixed total calibration budget

\[
\boxed{
\sum_e n_e=N.
}
\]

Define

\[
b_e=w_ea_e,
\qquad
S=\sum_j b_j^{2/3}.
\]

The objective is strictly convex, so there is one unique continuous optimum:

\[
\boxed{
n_e^*=N\frac{b_e^{2/3}}{S}.
}
\]

In plain language, transitions receive more measurements when they are harder to estimate or more important to the declared routing objective, but the allocation grows sublinearly. If one transition has an effective coefficient eight times larger than another, it receives four times as much continuous calibration effort, not eight times as much.

The minimum achievable surrogate uncertainty is

\[
\boxed{
U^*(N)=\frac{S^{3/2}}{\sqrt N}.
}
\]

Therefore a target uncertainty \(\varepsilon>0\) is achievable for this declared continuous surrogate exactly when

\[
\boxed{
N\ge\frac{S^3}{\varepsilon^2}.
}
\]

This closes the first resource-allocation loop for P58:

\[
\boxed{
\text{finite-data metric uncertainty}
\longrightarrow
\text{quantified route uncertainty}
\longrightarrow
\text{optimal continuous calibration allocation}.
}
\]

The scientific boundary is important. P59 solves this explicit convex surrogate exactly. It does not claim that the sensitivity weights are uniquely determined by nature, does not solve the full combinatorial robust-routing design problem, does not justify adaptive edge discovery, and does not turn any switching or scheduling quantity into a measure of consciousness.

[Read Proposition 59](docs/proposition_59_optimal_transition_calibration.md). The [P59 theorem visual](docs/figures/p59_optimal_transition_calibration.svg), [implementation](src/consciousness_bridge/optimal_transition_calibration.py), and [tests](tests/test_optimal_transition_calibration.py) expose the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = replace_once(text, marker, section + marker, "README P59 section")
    write(path, text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P59](proposition_59_optimal_transition_calibration.md)" in text:
        return
    text = insert_after_line(
        text,
        "p58_finite_data_metric_uncertainty.svg",
        "![P59 optimal transition-calibration allocation](figures/p59_optimal_transition_calibration.svg)",
        "roadmap figure",
    )
    text = insert_after_line(
        text,
        "| [P58](proposition_58_finite_data_metric_uncertainty.md)",
        "| [P59](proposition_59_optimal_transition_calibration.md) | strict convexity plus KKT allocation of inverse-square-root edge uncertainty | unique two-thirds-power calibration allocation, closed-form optimum, and target-budget formula | proved resource-allocation theorem |",
        "roadmap proposition row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P59 | [Optimal transition-calibration allocation]" in text:
        return
    text = text.replace("P1 through P58", "P1 through P59")
    text = insert_after_line(
        text,
        "| P58 | [Finite-data switching-metric uncertainty]",
        "| P59 | [Optimal transition-calibration allocation](proposition_59_optimal_transition_calibration.md) | exact two-thirds-power allocation of a finite calibration budget for the declared P58 route-uncertainty surrogate |",
        "navigation proposition row",
    )
    write(path, text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "P59 optimal transition-calibration allocation" in text:
        return
    addition = r'''

---

# P59 optimal transition-calibration allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\rho_e(n_e)=a_e/\sqrt{n_e}\) | declared inverse-square-root transition-calibration uncertainty model | repository design model, with Hoeffding coefficient available from P58 | [P58](proposition_58_finite_data_metric_uncertainty.md), [P59](proposition_59_optimal_transition_calibration.md) |
| \(U(n)=\sum_e w_ea_e/\sqrt{n_e}\) | weighted route-uncertainty surrogate under edge-specific calibration effort | repository definition | [P59](proposition_59_optimal_transition_calibration.md) |
| \(n_e^*=N(w_ea_e)^{2/3}/\sum_j(w_ja_j)^{2/3}\) | unique minimum-uncertainty continuous allocation | proved by strict convexity and KKT conditions | [P59](proposition_59_optimal_transition_calibration.md) |
| \(U^*(N)=S^{3/2}/\sqrt N\) | exact minimum value of the declared surrogate | proved by substitution at the unique optimum | [P59](proposition_59_optimal_transition_calibration.md) |
| \(N\ge S^3/\varepsilon^2\) | exact continuous budget threshold for target surrogate uncertainty \(\varepsilon\) | algebraic consequence of the optimum | [P59](proposition_59_optimal_transition_calibration.md) |

P59 is an exact resource-allocation result for a declared convex uncertainty surrogate. It does not establish optimality for the full combinatorial robust-routing design problem.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace_once(text, 'version = "0.58.0"', 'version = "0.59.0"', "pyproject version")
    if "optimal transition-calibration allocation" not in text:
        text = text.replace(
            "finite-data switching-metric uncertainty, robust experiment design",
            "finite-data switching-metric uncertainty, optimal transition-calibration allocation, robust experiment design",
        )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = replace_once(text, "version: 0.58.0", "version: 0.59.0", "citation version")
    if "optimal transition-calibration allocation" not in text:
        text = text.replace(
            "finite-data switching-metric uncertainty, robust experiment design",
            "finite-data switching-metric uncertainty, optimal transition-calibration allocation, robust experiment design",
        )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.59.0 - 2026-09-10"):
        entry = """# 0.59.0 - 2026-09-10

- Add P59 optimal transition-calibration allocation.
- Prove the unique continuous two-thirds-power allocation law for the declared P58 inverse-square-root uncertainty surrogate.
- Derive the exact minimum surrogate uncertainty and the exact continuous budget threshold for a target uncertainty level.
- Add implementation, regression tests, theorem visual, equation provenance, and front-page integration.
- Preserve the explicit boundary between this convex surrogate result and the unresolved full combinatorial robust-routing design problem.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(
        text,
        '    "p58_finite_data_metric_uncertainty.svg",',
        '    "p58_finite_data_metric_uncertainty.svg",\n    "p59_optimal_transition_calibration.svg",',
        "main-page P59 figure guard",
    )
    text = text.replace("for index in range(1, 59):", "for index in range(1, 60):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.58.0-2563eb", "version-0.59.0-2563eb")
    text = text.replace('version = "0\\.58\\.0"', 'version = "0\\.59\\.0"')
    text = text.replace("version: 0\\.58\\.0", "version: 0\\.59\\.0")
    marker = (
        '        "Proposition 58",\n'
        '        "p58_finite_data_metric_uncertainty.svg",\n'
        '        "finite_data_metric_uncertainty.py",\n'
        '        "test_finite_data_metric_uncertainty.py",\n'
    )
    replacement = marker + (
        '        "Proposition 59",\n'
        '        "p59_optimal_transition_calibration.svg",\n'
        '        "optimal_transition_calibration.py",\n'
        '        "test_optimal_transition_calibration.py",\n'
    )
    text = replace_once(text, marker, replacement, "release P59 path guards")
    write(path, text)

    write(
        "tests/test_optimal_transition_calibration_publication.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef test_p59_is_visible_on_main_page():\n    text = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "P59 - optimal transition-calibration allocation",\n        "p59_optimal_transition_calibration.svg",\n        "optimal_transition_calibration.py",\n        "test_optimal_transition_calibration.py",\n    ):\n        assert token in text\n\n\ndef test_p59_is_in_public_research_maps():\n    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")\n    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")\n    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")\n    assert "[P59](proposition_59_optimal_transition_calibration.md)" in roadmap\n    assert "| P59 | [Optimal transition-calibration allocation]" in navigation\n    assert "P59 optimal transition-calibration allocation" in equations\n''',
    )


def main() -> None:
    integrate_readme()
    integrate_roadmap()
    integrate_navigation()
    integrate_equation_map()
    integrate_metadata()
    integrate_tests()


if __name__ == "__main__":
    main()
