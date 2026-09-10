from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P56 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text: str, token: str, new_line: str, label: str) -> str:
    if new_line in text:
        return text
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if token in line:
            lines.insert(index + 1, new_line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P56 line marker: {label}")


def integrate_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## 13.29 P56 - moving-start metric reoptimization stability" in text:
        return
    text = replace_once(text, "version-0.55.0-2563eb", "version-0.56.0-2563eb", "README version")
    text = replace_once(
        text,
        "The public research record now contains **55 proposition-level results",
        "The public research record now contains **56 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P55", "P1 through P56")

    p55 = (
        "**P55** proves that this metric execution optimum remains monotone under "
        "componentwise residual decrease: acquisition savings are exact, support deletion cannot "
        "increase the shortest switching route, and old-route shortcutting gives a computable "
        "lower bound on additional route savings."
    )
    p56 = (
        p55
        + " **P56** removes the fixed-start restriction: the optimal metric route is "
        "1-Lipschitz in the setup origin, so moving the apparatus from s to s' can erode a P55 "
        "saving by at most the metric displacement c(s,s')."
    )
    text = replace_once(text, p55, p56, "README abstract P55 sentence")
    text = insert_after_line(
        text,
        "[Proposition 55](docs/proposition_55_pruning_aware_switching_monotonicity.md)",
        "| moving-start metric reoptimization stability | [Proposition 56](docs/proposition_56_moving_start_metric_reoptimization_stability.md) | sharp start-state Lipschitz control and residual reoptimization bound under setup displacement |",
        "README proposition navigation",
    )

    section = r'''
## 13.29 P56 - moving-start metric reoptimization stability

![P56 moving-start metric reoptimization stability](docs/figures/p56_moving_start_metric_reoptimization_stability.svg)

P55 proves monotone residual execution cost when the switching metric and current setup state remain fixed. P56 removes the fixed-start restriction while keeping one declared metric geometry.

For any nonempty active preparation support \(S\), let \(L^*(S;s)\) be the P54 shortest switching path beginning at setup state \(s\). Reusing an optimal route from a second start changes only the first transition, so the triangle inequality gives the sharp start-state stability theorem

\[
\boxed{
|L^*(S;s)-L^*(S;s')|\le c(s,s').
}
\]

The coefficient one is tight even for a single remaining preparation on a line metric.

For residual demand \(r'\le r\), define the P55 fixed-start saving

\[
\Delta_{\rm fixed}=C^*(r;s)-C^*(r';s)\ge0.
\]

P56 then proves

\[
\boxed{
C^*(r;s)-C^*(r';s')
\ge
\Delta_{\rm fixed}-c(s,s').
}
\]

Thus setup motion can erase at most one metric displacement worth of the improvement certified by P55. In particular,

\[
\boxed{
\Delta_{\rm fixed}>c(s,s')
\Longrightarrow
C^*(r';s')<C^*(r;s).
}
\]

Combining P55 and P56 separates three deterministic experimental effects: acquisition release from reduced residual counts, route release from support deletion, and a bounded penalty from moving the apparatus origin.

P56 assumes one unchanged metric switching geometry. If transition costs themselves change between states, a separate metric-perturbation theorem is required. P56 does not independently justify pruning, establish statistical minimaxity, or make an ontological claim about consciousness or quantum mechanics.

[Read Proposition 56](docs/proposition_56_moving_start_metric_reoptimization_stability.md). The [P56 theorem map](docs/figures/p56_moving_start_metric_reoptimization_stability.svg), [implementation](src/consciousness_bridge/moving_start_metric_reoptimization.py), and [tests](tests/test_moving_start_metric_reoptimization.py) expose the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = replace_once(text, marker, section + marker, "README P56 section")
    write(path, text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P56](proposition_56_moving_start_metric_reoptimization_stability.md)" in text:
        return
    text = insert_after_line(
        text,
        "p55_pruning_aware_switching_monotonicity.svg",
        "![P56 moving-start metric reoptimization stability](figures/p56_moving_start_metric_reoptimization_stability.svg)",
        "roadmap figure",
    )
    text = insert_after_line(
        text,
        "| [P55](proposition_55_pruning_aware_switching_monotonicity.md)",
        "| [P56](proposition_56_moving_start_metric_reoptimization_stability.md) | triangle-inequality perturbation of the first route edge plus P55 composition | sharp 1-Lipschitz start-state stability and moving-setup residual cost certificate | proved deterministic perturbation theorem |",
        "roadmap proposition row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P56 | [Moving-start metric reoptimization stability]" in text:
        return
    text = text.replace("P1 through P55", "P1 through P56")
    text = insert_after_line(
        text,
        "| P55 | [Pruning-aware metric switching-cost monotonicity]",
        "| P56 | [Moving-start metric reoptimization stability](proposition_56_moving_start_metric_reoptimization_stability.md) | sharp start-state Lipschitz bound, P55 saving erosion bound, and strict-decrease certificate under setup motion |",
        "navigation proposition row",
    )
    write(path, text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 45. P56 moving-start metric reoptimization stability" in text:
        return
    addition = r'''

---

# 45. P56 moving-start metric reoptimization stability

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(|L^*(S;s)-L^*(S;s')|\le c(s,s')\) | start-state perturbation of the optimal P54 route | proved sharp 1-Lipschitz theorem | [P56](proposition_56_moving_start_metric_reoptimization_stability.md) |
| \(|C^*(r;s)-C^*(r;s')|\le c(s,s')\) | fixed-residual total-cost start stability | immediate from P56 route theorem | [P56](proposition_56_moving_start_metric_reoptimization_stability.md) |
| \(C^*(r;s)-C^*(r';s')\ge\Delta_{\rm fixed}-c(s,s')\) | residual decrease with moving setup origin | proved P55-P56 perturbation bound | [P56](proposition_56_moving_start_metric_reoptimization_stability.md) |
| \(\Delta_{\rm fixed}>c(s,s')\) | sufficient strict-decrease condition | proved consequence | [P56](proposition_56_moving_start_metric_reoptimization_stability.md) |

P56 assumes the metric itself is unchanged. Time-varying switching geometry requires a separate perturbation analysis.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace_once(text, 'version = "0.55.0"', 'version = "0.56.0"', "pyproject version")
    text = replace_once(
        text,
        "pruning-aware metric switching-cost monotonicity, robust experiment design",
        "pruning-aware metric switching-cost monotonicity, moving-start metric reoptimization stability, robust experiment design",
        "pyproject description",
    )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = replace_once(text, "version: 0.55.0", "version: 0.56.0", "citation version")
    text = replace_once(
        text,
        "pruning-aware metric switching-cost monotonicity, robust experiment design",
        "pruning-aware metric switching-cost monotonicity, moving-start metric reoptimization stability, robust experiment design",
        "citation abstract",
    )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.56.0 - 2026-09-10"):
        entry = """# 0.56.0 - 2026-09-10

- Add P56 moving-start metric reoptimization stability.
- Prove the optimal P54 switching route is sharply 1-Lipschitz in the setup origin.
- Bound erosion of a P55 fixed-start saving by the metric setup displacement.
- Add a sufficient strict-decrease certificate when fixed-start savings exceed start movement.
- Add a tightness example and make the fixed-metric boundary explicit.
- Add implementation, tests, theorem visual, equation provenance, and front-page integration.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(
        text,
        '    "p55_pruning_aware_switching_monotonicity.svg",',
        '    "p55_pruning_aware_switching_monotonicity.svg",\n    "p56_moving_start_metric_reoptimization_stability.svg",',
        "main-page P56 figure guard",
    )
    text = text.replace("for index in range(1, 56):", "for index in range(1, 57):")
    write(path, text)

    # Historical publication tests should test their theorem, not freeze the global count.
    p55_test = "tests/test_pruning_aware_switching_publication.py"
    text = read(p55_test)
    text = text.replace('        "**55 proposition-level results",\n', "")
    write(p55_test, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.55.0-2563eb", "version-0.56.0-2563eb")
    text = text.replace('version = "0\\.55\\.0"', 'version = "0\\.56\\.0"')
    text = text.replace("version: 0\\.55\\.0", "version: 0\\.56\\.0")
    marker = (
        '        "Proposition 55",\n'
        '        "p55_pruning_aware_switching_monotonicity.svg",\n'
        '        "pruning_aware_switching_monotonicity.py",\n'
        '        "test_pruning_aware_switching_monotonicity.py",\n'
    )
    replacement = marker + (
        '        "Proposition 56",\n'
        '        "p56_moving_start_metric_reoptimization_stability.svg",\n'
        '        "moving_start_metric_reoptimization.py",\n'
        '        "test_moving_start_metric_reoptimization.py",\n'
    )
    text = replace_once(text, marker, replacement, "release P56 path guards")
    write(path, text)

    write(
        "tests/test_moving_start_metric_reoptimization_publication.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef test_p56_is_visible_on_main_page():\n    text = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "P56 - moving-start metric reoptimization stability",\n        "p56_moving_start_metric_reoptimization_stability.svg",\n        "moving_start_metric_reoptimization.py",\n        "test_moving_start_metric_reoptimization.py",\n    ):\n        assert token in text\n\n\ndef test_p56_is_in_public_research_maps():\n    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")\n    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")\n    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")\n    assert "[P56](proposition_56_moving_start_metric_reoptimization_stability.md)" in roadmap\n    assert "| P56 | [Moving-start metric reoptimization stability]" in navigation\n    assert "# 45. P56 moving-start metric reoptimization stability" in equations\n''',
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
