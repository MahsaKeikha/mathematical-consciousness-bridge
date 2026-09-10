from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P61 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text: str, token: str, new_line: str, label: str) -> str:
    if new_line in text:
        return text
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if token in line:
            lines.insert(index + 1, new_line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P61 line marker: {label}")


def integrate_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## Latest proved extension: P61 exact integer calibration" in text:
        return

    text = replace_once(text, "version-0.60.0-2563eb", "version-0.61.0-2563eb", "README version")
    text = replace_once(
        text,
        "The public research record now contains **60 proposition-level results",
        "The public research record now contains **61 proposition-level results",
        "README proposition count",
    )
    p60 = (
        "**P60** converts that fractional design into whole measurement counts under a hard integer budget: "
        "reserving one rounding unit per calibrated edge, solving P59 on the remaining budget, and rounding upward "
        "yields a feasible integer allocation whose uncertainty is at most the continuous full-budget optimum multiplied by sqrt(B/(B-m))."
    )
    p61 = (
        p60
        + " **P61** closes the remaining discrete optimization gap for the same separable surrogate: starting from one measurement per edge, repeatedly assigning the next whole measurement to the edge with the largest current marginal uncertainty reduction is globally optimal because those marginal gains decrease strictly with repeated sampling."
    )
    text = replace_once(text, p60, p61, "README abstract P60 sentence")

    block = r'''
## Latest proved extension: P61 exact integer calibration

![P61 exact integer transition-calibration allocation](docs/figures/p61_exact_integer_transition_calibration.svg)

P59 gives the exact continuous allocation of a transition-calibration budget, and P60 gives a simple integer rounding rule with a provable overhead. P61 goes one step further and solves the declared whole-measurement allocation problem **exactly**.

For edge \(e\), let

\[
\boxed{
U(k)=\sum_e\frac{b_e}{\sqrt{k_e}},
\qquad
k_e\in\{1,2,3,\ldots\},
\qquad
\sum_e k_e=B.
}
\]

If edge \(e\) currently has \(k\) measurements, the benefit of one more measurement is

\[
\boxed{
\Delta_e(k)
=
b_e\left(\frac1{\sqrt{k}}-\frac1{\sqrt{k+1}}\right).
}
\]

P61 proves that \(\Delta_e(k)\) strictly decreases as \(k\) grows. Therefore the exact integer optimum is obtained by a transparent rule:

> Give every calibrated edge one measurement, then repeatedly give the next available measurement to the edge with the largest current marginal uncertainty reduction.

This is not merely a heuristic. For the declared separable P59-P61 surrogate it is the **global integer optimum**. The implementation uses a priority queue, so the exact solution is practical even when the total budget is large.

The result closes the continuous-to-integer calibration chain:

\[
\boxed{
\text{P58 finite-data uncertainty}
\to
\text{P59 continuous optimal allocation}
\to
\text{P60 certified integer rounding}
\to
\text{P61 exact integer allocation}.
}
\]

The scientific boundary remains unchanged: P61 optimizes an experimental calibration surrogate. It does not establish that the sensitivity weights are uniquely correct, does not solve the full combinatorial robust-routing design problem, and does not make any claim that consciousness is a physical quantity, a quantum variable, or an additional spacetime dimension.

[Read Proposition 61](docs/proposition_61_exact_integer_transition_calibration.md). The [P61 theorem visual](docs/figures/p61_exact_integer_transition_calibration.svg), [implementation](src/consciousness_bridge/exact_integer_transition_calibration.py), and [tests](tests/test_exact_integer_transition_calibration.py) expose the complete proof-to-code path.

---

'''
    marker = "# Scientific status discipline"
    text = replace_once(text, marker, block + marker, "README P61 latest-result block")
    write(path, text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P61](proposition_61_exact_integer_transition_calibration.md)" in text:
        return
    text = insert_after_line(
        text,
        "p60_integer_transition_calibration.svg",
        "![P61 exact integer transition-calibration allocation](figures/p61_exact_integer_transition_calibration.svg)",
        "roadmap P61 figure",
    )
    text = insert_after_line(
        text,
        "| [P60](proposition_60_integer_transition_calibration.md)",
        "| [P61](proposition_61_exact_integer_transition_calibration.md) | discrete diminishing returns and exchange optimality for the P59 separable surrogate | exact whole-measurement allocation by largest current marginal uncertainty reduction | proved exact discrete allocation theorem |",
        "roadmap P61 row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P61 | [Exact integer transition-calibration allocation]" in text:
        return
    text = text.replace("P1 through P60", "P1 through P61")
    text = insert_after_line(
        text,
        "| P60 | [Integer transition-calibration allocation]",
        "| P61 | [Exact integer transition-calibration allocation](proposition_61_exact_integer_transition_calibration.md) | exact hard-budget whole-measurement solution for the declared separable calibration surrogate using diminishing marginal gain |",
        "navigation P61 row",
    )
    write(path, text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 50. P61 exact integer transition-calibration allocation" in text:
        return
    addition = r'''

---

# 50. P61 exact integer transition-calibration allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(U(k)=\sum_e b_e/\sqrt{k_e}\) with integer \(k_e\ge1\) | hard-budget whole-measurement version of the P59 separable uncertainty surrogate | repository definition | [P61](proposition_61_exact_integer_transition_calibration.md) |
| \(\Delta_e(k)=b_e(k^{-1/2}-(k+1)^{-1/2})\) | marginal uncertainty reduction from one additional calibration measurement | repository definition | [P61](proposition_61_exact_integer_transition_calibration.md) |
| \(\Delta_e(k+1)<\Delta_e(k)\) | strict diminishing marginal gain on each calibrated edge | proved discrete-convexity property | [P61](proposition_61_exact_integer_transition_calibration.md) |
| largest-current-\(\Delta\) allocation rule | exact integer optimizer under \(\sum_e k_e=B\) | proved by prefix representation and exchange argument | [P61](proposition_61_exact_integer_transition_calibration.md) |
| selected/unselected marginal exchange condition | directly checkable certificate of discrete optimality | proved optimality condition | [P61](proposition_61_exact_integer_transition_calibration.md) |

P61 exactness applies to the declared unit-cost separable calibration surrogate. It is not a proof that the full robust-routing experiment-design problem is greedy-solvable.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace_once(text, 'version = "0.60.0"', 'version = "0.61.0"', "pyproject version")
    text = replace_once(
        text,
        "integer transition-calibration allocation, robust experiment design",
        "integer transition-calibration allocation, exact integer transition-calibration allocation, robust experiment design",
        "pyproject description",
    )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = replace_once(text, "version: 0.60.0", "version: 0.61.0", "citation version")
    text = replace_once(
        text,
        "integer transition-calibration allocation, robust experiment design",
        "integer transition-calibration allocation, exact integer transition-calibration allocation, robust experiment design",
        "citation abstract",
    )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.61.0 - 2026-09-10"):
        entry = """# 0.61.0 - 2026-09-10

- Add P61 exact integer transition-calibration allocation by diminishing marginal gain.
- Prove strict diminishing returns for each edge's uncertainty reduction sequence.
- Prove that the largest-current-marginal-gain allocation rule is globally optimal for the declared hard-budget separable integer surrogate.
- Add a priority-queue implementation, brute-force regression checks on small instances, theorem visual, public navigation, provenance, and release integration.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.60.0-2563eb", "version-0.61.0-2563eb")
    text = text.replace('version = "0\\.60\\.0"', 'version = "0\\.61\\.0"')
    text = text.replace("version: 0\\.60\\.0", "version: 0\\.61\\.0")
    marker = (
        '        "Proposition 60",\n'
        '        "p60_integer_transition_calibration.svg",\n'
        '        "integer_transition_calibration.py",\n'
        '        "test_integer_transition_calibration.py",\n'
    )
    replacement = marker + (
        '        "Proposition 61",\n'
        '        "p61_exact_integer_transition_calibration.svg",\n'
        '        "exact_integer_transition_calibration.py",\n'
        '        "test_exact_integer_transition_calibration.py",\n'
    )
    text = replace_once(text, marker, replacement, "release P61 guards")
    write(path, text)

    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    if '"p61_exact_integer_transition_calibration.svg"' not in text:
        text = replace_once(
            text,
            '    "p60_integer_transition_calibration.svg",',
            '    "p60_integer_transition_calibration.svg",\n    "p61_exact_integer_transition_calibration.svg",',
            "main page P61 figure guard",
        )
    text = text.replace("for index in range(1, 61):", "for index in range(1, 62):")
    write(path, text)

    write(
        "tests/test_exact_integer_transition_calibration_publication.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef test_p61_is_visible_on_main_page():\n    text = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "P61 exact integer calibration",\n        "p61_exact_integer_transition_calibration.svg",\n        "exact_integer_transition_calibration.py",\n        "test_exact_integer_transition_calibration.py",\n    ):\n        assert token in text\n\n\ndef test_p61_is_in_public_research_maps():\n    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")\n    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")\n    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")\n    assert "[P61](proposition_61_exact_integer_transition_calibration.md)" in roadmap\n    assert "| P61 | [Exact integer transition-calibration allocation]" in navigation\n    assert "# 50. P61 exact integer transition-calibration allocation" in equations\n''',
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
