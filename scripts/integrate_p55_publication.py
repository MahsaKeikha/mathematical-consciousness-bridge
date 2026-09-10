from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P55 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text: str, token: str, new_line: str, label: str) -> str:
    if new_line in text:
        return text
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if token in line:
            lines.insert(index + 1, new_line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P55 line marker: {label}")


def integrate_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## 13.28 P55 - pruning-aware metric switching-cost monotonicity" in text:
        return

    text = replace_once(text, "version-0.54.0-2563eb", "version-0.55.0-2563eb", "README version")
    text = replace_once(
        text,
        "The public research record now contains **54 proposition-level results",
        "The public research record now contains **55 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P54", "P1 through P55")

    p54 = (
        "**P54** adds metric preparation-switching costs and proves that an optimal residual "
        "schedule can batch every positive-demand preparation into one contiguous block, reducing "
        "the switching term exactly to a shortest Hamiltonian path problem."
    )
    p55 = (
        p54
        + " **P55** proves that this metric execution optimum remains monotone under "
        "componentwise residual decrease: acquisition savings are exact, support deletion cannot "
        "increase the shortest switching route, and old-route shortcutting gives a computable "
        "lower bound on additional route savings."
    )
    text = replace_once(text, p54, p55, "README abstract P54 sentence")

    text = insert_after_line(
        text,
        "[Proposition 54](docs/proposition_54_metric_switching_cost_residual_scheduling.md)",
        "| pruning-aware metric switching-cost monotonicity | [Proposition 55](docs/proposition_55_pruning_aware_switching_monotonicity.md) | exact acquisition-plus-route release under residual decrease, support-deletion monotonicity, and shortcut certificate |",
        "README proposition navigation",
    )

    section = r'''
## 13.28 P55 - pruning-aware metric switching-cost monotonicity

![P55 pruning-aware metric switching-cost monotonicity](docs/figures/p55_pruning_aware_switching_monotonicity.svg)

P54 decomposes deterministic residual execution cost into a fixed acquisition term and an optimal metric switching route. P55 asks how that exact optimum changes as sequential evidence reduces residual demands or valid P47-safe pruning removes preparations from the active support.

For residual vectors \(r'\le r\) componentwise, define

\[
S(r)=\{i:r_i>0\},\qquad S(r')\subseteq S(r).
\]

With the same metric switching geometry and the same current setup state \(s\), P54 gives

\[
C^*(r;s)=a\sum_i r_i+L^*(S(r);s).
\]

Metric shortcutting proves support-deletion monotonicity:

\[
\boxed{L^*(S(r');s)\le L^*(S(r);s).}
\]

Subtracting the two exact P54 objectives yields the P55 release identity

\[
\boxed{
C^*(r;s)-C^*(r';s)
=
a\left(\sum_i r_i-\sum_i r_i'\right)
+
\left[L^*(S(r);s)-L^*(S(r');s)\right].
}
\]

Both terms are nonnegative. Thus additional samples or valid safe pruning cannot increase the optimal deterministic execution cost under a fixed metric and fixed start state.

If positive support is unchanged, then the route problem is identical and

\[
\boxed{
C^*(r;s)-C^*(r';s)
=
a\left(\sum_i r_i-\sum_i r_i'\right).
}
\]

If support shrinks, deleting vanished preparations from the old optimal route gives a computable shortcut saving \(\Delta_{\rm shortcut}\) satisfying

\[
\boxed{
0\le\Delta_{\rm shortcut}
\le L^*(S(r);s)-L^*(S(r');s).
}
\]

This separates a continuous acquisition effect from a discrete routing effect: reducing a positive demand preserves the route support, while driving a demand to zero may eliminate an entire preparation setup from the switching problem.

P55 requires the same metric and the same start/setup state across the two residual states. It does not independently justify pruning, claim statistical minimaxity of the P48 thresholds, or make any ontological claim about consciousness or quantum mechanics.

[Read Proposition 55](docs/proposition_55_pruning_aware_switching_monotonicity.md). The [P55 theorem map](docs/figures/p55_pruning_aware_switching_monotonicity.svg), [implementation](src/consciousness_bridge/pruning_aware_switching_monotonicity.py), and [tests](tests/test_pruning_aware_switching_monotonicity.py) expose the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = replace_once(text, marker, section + marker, "README P55 section")
    write(path, text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P55](proposition_55_pruning_aware_switching_monotonicity.md)" in text:
        return
    text = insert_after_line(
        text,
        "p54_metric_switching_cost_residual_scheduling.svg",
        "![P55 pruning-aware metric switching-cost monotonicity](figures/p55_pruning_aware_switching_monotonicity.svg)",
        "roadmap figure",
    )
    text = insert_after_line(
        text,
        "| [P54](proposition_54_metric_switching_cost_residual_scheduling.md)",
        "| [P55](proposition_55_pruning_aware_switching_monotonicity.md) | metric support-deletion shortcutting plus exact P54 cost subtraction | monotone optimal residual execution cost with exact acquisition and route-release decomposition | proved deterministic scheduling theorem |",
        "roadmap proposition row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P55 | [Pruning-aware metric switching-cost monotonicity]" in text:
        return
    text = text.replace("P1 through P54", "P1 through P55")
    text = insert_after_line(
        text,
        "| P54 | [Metric switching-cost residual scheduling]",
        "| P55 | [Pruning-aware metric switching-cost monotonicity](proposition_55_pruning_aware_switching_monotonicity.md) | exact acquisition-plus-route release, support-deletion monotonicity, and computable old-route shortcut certificate |",
        "navigation proposition row",
    )
    write(path, text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 44. P55 pruning-aware metric switching-cost monotonicity" in text:
        return
    addition = r'''

---

# 44. P55 pruning-aware metric switching-cost monotonicity

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(S(r')\subseteq S(r)\) for \(r'\le r\) | support nesting under componentwise residual decrease | immediate consequence | [P55](proposition_55_pruning_aware_switching_monotonicity.md) |
| \(L^*(S(r');s)\le L^*(S(r);s)\) | optimal metric route monotonicity under support deletion | proved by shortcutting | [P55](proposition_55_pruning_aware_switching_monotonicity.md) |
| \(C^*(r;s)-C^*(r';s)=a(\sum r_i-\sum r_i')+[L^*(S(r);s)-L^*(S(r');s)]\) | exact deterministic optimal cost-release decomposition | proved by P54 subtraction plus route monotonicity | [P55](proposition_55_pruning_aware_switching_monotonicity.md) |
| \(0\le\Delta_{\rm shortcut}\le L^*(S(r);s)-L^*(S(r');s)\) | computable lower certificate on route release | proved from retained old optimal route | [P55](proposition_55_pruning_aware_switching_monotonicity.md) |

P55 compares states under one fixed metric and fixed start/setup state. A moving start requires a separate stability theorem.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace_once(text, 'version = "0.54.0"', 'version = "0.55.0"', "pyproject version")
    text = replace_once(
        text,
        "metric switching-cost residual scheduling, robust experiment design",
        "metric switching-cost residual scheduling, pruning-aware metric switching-cost monotonicity, robust experiment design",
        "pyproject description",
    )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = replace_once(text, "version: 0.54.0", "version: 0.55.0", "citation version")
    text = replace_once(
        text,
        "metric switching-cost residual scheduling, robust experiment design",
        "metric switching-cost residual scheduling, pruning-aware metric switching-cost monotonicity, robust experiment design",
        "citation abstract",
    )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.55.0 - 2026-09-10"):
        entry = """# 0.55.0 - 2026-09-10

- Add P55 pruning-aware metric switching-cost monotonicity.
- Prove shortest metric route monotonicity under active-support deletion.
- Prove the exact acquisition-plus-route optimal cost-release identity.
- Prove the support-preserving case has zero route release exactly.
- Add a computable shortcut certificate lower-bounding route savings after support deletion.
- Add implementation, tests, theorem visual, equation provenance, and front-page integration.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(
        text,
        '    "p54_metric_switching_cost_residual_scheduling.svg",',
        '    "p54_metric_switching_cost_residual_scheduling.svg",\n    "p55_pruning_aware_switching_monotonicity.svg",',
        "main-page P55 figure guard",
    )
    text = text.replace("for index in range(1, 55):", "for index in range(1, 56):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.54.0-2563eb", "version-0.55.0-2563eb")
    text = text.replace('version = "0\\.54\\.0"', 'version = "0\\.55\\.0"')
    text = text.replace("version: 0\\.54\\.0", "version: 0\\.55\\.0")
    marker = (
        '        "Proposition 54",\n'
        '        "p54_metric_switching_cost_residual_scheduling.svg",\n'
        '        "metric_switching_residual_schedule.py",\n'
        '        "test_metric_switching_residual_schedule.py",\n'
    )
    replacement = marker + (
        '        "Proposition 55",\n'
        '        "p55_pruning_aware_switching_monotonicity.svg",\n'
        '        "pruning_aware_switching_monotonicity.py",\n'
        '        "test_pruning_aware_switching_monotonicity.py",\n'
    )
    text = replace_once(text, marker, replacement, "release P55 path guards")
    write(path, text)

    write(
        "tests/test_pruning_aware_switching_publication.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef test_p55_is_visible_on_main_page():\n    text = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "P55 - pruning-aware metric switching-cost monotonicity",\n        "p55_pruning_aware_switching_monotonicity.svg",\n        "pruning_aware_switching_monotonicity.py",\n        "test_pruning_aware_switching_monotonicity.py",\n        "**55 proposition-level results",\n    ):\n        assert token in text\n\n\ndef test_p55_is_in_public_research_maps():\n    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")\n    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")\n    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")\n    assert "[P55](proposition_55_pruning_aware_switching_monotonicity.md)" in roadmap\n    assert "| P55 | [Pruning-aware metric switching-cost monotonicity]" in navigation\n    assert "# 44. P55 pruning-aware metric switching-cost monotonicity" in equations\n''',
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
