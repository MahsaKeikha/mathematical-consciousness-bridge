from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P48 publication marker: {label}")
    return text.replace(old, new, 1)


def integrate_readme() -> None:
    text = read("README.md")
    if "## 13.21 P48 - gap-dependent sequential stopping complexity" in text:
        return

    text = replace_once(
        text,
        "version-0.47.0-2563eb",
        "version-0.48.0-2563eb",
        "README version",
    )

    p47 = (
        "**P47** closes the adaptive-sampling validity gap: preparation-level "
        "time-uniform confidence sequences are combined into one finite-family "
        "event that remains valid under non-anticipating adaptive preparation "
        "sampling, graph refinement, witness selection, safe pruning, and stopping."
    )
    p48 = (
        p47
        + " **P48** converts that qualitative eventual-detection result into an "
        "explicit gap-dependent stopping bound under a declared logarithmic "
        "confidence-sequence envelope, including positive-witness, all-negative, "
        "zero-gap, and acquisition-cost cases."
    )
    text = replace_once(text, p47, p48, "README abstract")
    text = replace_once(
        text,
        "The public research record now contains **47 proposition-level results",
        "The public research record now contains **48 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P47", "P1 through P48")

    p47_row = (
        "| anytime sequential witness graph | "
        "[Proposition 47](docs/proposition_47_anytime_sequential_witness_graph.md) | "
        "time-uniform adaptive preparation sampling, safe pruning, post-selection, "
        "and stopping under one simultaneous family event |"
    )
    p48_row = (
        p47_row
        + "\n| gap-dependent sequential stopping complexity | "
        "[Proposition 48](docs/proposition_48_gap_dependent_stopping_complexity.md) | "
        "explicit nonzero-margin local sample bound, positive/all-negative stopping "
        "epochs, zero-gap boundary, and pruning-aware acquisition-cost control |"
    )
    text = replace_once(text, p47_row, p48_row, "README navigation")

    section = r'''
## 13.21 P48 - gap-dependent sequential stopping complexity

![P48 gap-dependent stopping complexity](docs/figures/p48_gap_dependent_stopping_complexity.svg)

P47 proves that adaptive sampling and stopping can remain statistically valid. P48 answers the next quantitative question: **under an explicit shrinking confidence-sequence envelope, how much data is sufficient before the sequential witness graph must reach a sign conclusion?**

For edge \(e=\{i,j\}\), retain the population regularity margin

\[
M_e=d_{Y,e}-L_e d_{Q,e},
\qquad
g_e=|M_e|.
\]

Assume the preparation-level target and quantum confidence radii are bounded by terms of the form

\[
A_i\sqrt{\frac{\log(B_i n^2)}{n}}.
\]

Combining both endpoint target uncertainties and both endpoint quantum uncertainties gives the edge envelope

\[
\boxed{
U_e(n)
\le
A_e\sqrt{\frac{\log(B_e n^2)}{n}},
}
\]

with

\[
A_e
=
A_{Y,i}+A_{Y,j}
+
L_e(A_{Q,i}+A_{Q,j}),
\]

and \(B_e\) equal to the largest endpoint logarithmic factor.

On the P47 simultaneous event, the lower and upper population-margin certificates satisfy the deterministic perturbation bounds

\[
\underline M_e(n)
\ge
M_e-2U_e(n),
\qquad
\overline M_e(n)
\le
M_e+2U_e(n).
\]

Therefore the sign of any nonzero margin is certified once

\[
U_e(n)<\frac{g_e}{2}.
\]

P48 explicitly inverts the logarithmic envelope. Define

\[
q_e
=
\left(\frac{2A_e}{g_e}\right)^2,
\qquad
Q_e=\max\{q_e,1\}.
\]

Then the sufficient local count

\[
\boxed{
N_e
=
\left\lceil
4Q_e\log\left(4Q_e\sqrt{B_e}\right)
\right\rceil
}
\]

satisfies

\[
U_e(n)<\frac{g_e}{2}
\qquad
\forall n\ge N_e.
\]

For the concrete P48 active round-robin policy, every currently active preparation receives one additional target sample and one additional quantum/tomography sample per epoch, while P47-certified negative edges are eliminated and isolated vertices are pruned.

If at least one positive-margin witness exists, a true positive edge cannot be removed by the negative-elimination rule on the simultaneous P47 event. Hence its endpoints continue to receive data. The procedure must stop no later than

\[
\boxed{
K_+
=
\min_{e:M_e>0}N_e.
}
\]

If every declared edge is strictly negative, all edges must be eliminated by

\[
\boxed{
K_-
=
\max_{e\in E}N_e.
}
\]

Both conclusions inherit the P47 family-level probability guarantee

\[
\boxed{
1-\alpha_Y-\alpha_Q.
}
\]

Exactly zero population margin is treated separately: without an additional separation assumption there is no generic finite sign-certification bound. This boundary is explicit rather than hidden inside asymptotic notation.

The dominant scaling is

\[
\boxed{
N_e
=
O\left(
\frac{A_e^2}{g_e^2}
\log\left[
\frac{A_e^2\sqrt{B_e}}{g_e^2}
\right]
\right),
}
\]

so small population margins are quantitatively harder to resolve.

Finally, if \(c_i\) is the cost of one complete sampling epoch for preparation \(i\), then full-family round robin costs

\[
C_{\rm full}(K)
=
K\sum_{i\in V}c_i,
\]

while P47 safe pruning gives

\[
\boxed{
C_{\rm active}(K)
\le
C_{\rm full}(K).
}
\]

P48 is a sufficient stopping upper bound, not a minimax lower bound and not an adaptive-optimality theorem. Its scientific conclusion remains a finite-data certificate for a declared regular physical-to-target bridge class; it does not establish quantum incompleteness, an extra physical dimension, or consciousness.

[Read Proposition 48](docs/proposition_48_gap_dependent_stopping_complexity.md). The [P48 theorem map](docs/figures/p48_gap_dependent_stopping_complexity.svg), [implementation](src/consciousness_bridge/gap_stopping_complexity.py), and [tests](tests/test_gap_stopping_complexity.py) expose the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = replace_once(text, marker, section + marker, "README P48 section")
    write("README.md", text)


def integrate_roadmap() -> None:
    text = read("docs/theorem_roadmap.md")
    if "[P48](proposition_48_gap_dependent_stopping_complexity.md)" in text:
        return
    visual = "![P47 anytime-valid sequential witness graph](figures/p47_sequential_graph_refinement.svg)"
    text = replace_once(
        text,
        visual,
        visual + "\n\n![P48 gap-dependent stopping complexity](figures/p48_gap_dependent_stopping_complexity.svg)",
        "roadmap visual",
    )
    row = (
        "| [P47](proposition_47_anytime_sequential_witness_graph.md) | finite-family "
        "all-local-time confidence event plus adaptive local-count substitution and "
        "simultaneous edge envelopes | valid non-anticipating adaptive preparation "
        "sampling, graph refinement, witness selection, pruning, and stopping | "
        "proved anytime-valid sequential-design theorem |"
    )
    row48 = (
        row
        + "\n| [P48](proposition_48_gap_dependent_stopping_complexity.md) | "
        "explicit inversion of a logarithmic confidence-sequence envelope plus "
        "margin perturbation bounds | gap-dependent positive/all-negative stopping "
        "epochs and pruning-aware acquisition-cost upper bound | proved sequential "
        "stopping-complexity theorem |"
    )
    text = replace_once(text, row, row48, "roadmap row")
    write("docs/theorem_roadmap.md", text)


def integrate_navigation() -> None:
    text = read("docs/research_navigation.md")
    if "| P48 | [Gap-dependent stopping complexity]" in text:
        return
    text = text.replace("P1 through P47", "P1 through P48")
    row = (
        "| P47 | [Anytime sequential witness graph]"
        "(proposition_47_anytime_sequential_witness_graph.md) | time-uniform "
        "adaptive preparation sampling, graph refinement, witness selection, safe "
        "pruning, and stopping |"
    )
    row48 = (
        row
        + "\n| P48 | [Gap-dependent stopping complexity]"
        "(proposition_48_gap_dependent_stopping_complexity.md) | explicit "
        "nonzero-margin sequential stopping counts, all-negative certification, "
        "zero-gap boundary, and acquisition-cost control |"
    )
    text = replace_once(text, row, row48, "navigation row")
    write("docs/research_navigation.md", text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 37. P48 gap-dependent stopping complexity" in text:
        return
    addition = r'''

---

# 37. P48 gap-dependent stopping complexity

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(g_e=|M_e|\) | population sign gap for a declared regularity witness | repository definition | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(U_e(n)\le A_e\sqrt{\log(B_e n^2)/n}\) | common edge-level uncertainty envelope from target and quantum endpoint radii | proved envelope reduction | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(\underline M_e\ge M_e-2U_e\), \(\overline M_e\le M_e+2U_e\) | deterministic sign-certification perturbation bounds | proved from P47 interval geometry | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(N_e=\lceil4Q_e\log(4Q_e\sqrt{B_e})\rceil\) | explicit sufficient local count for every nonzero margin | proved elementary inversion bound | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(K_+=\min_{M_e>0}N_e\) | positive-witness stopping-epoch upper bound | proved on the P47 simultaneous event | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(K_-=\max_eN_e\) when all \(M_e<0\) | all-negative stopping-epoch upper bound | proved on the P47 simultaneous event | [P48](proposition_48_gap_dependent_stopping_complexity.md) |
| \(C_{\rm active}(K)\le C_{\rm full}(K)\) | safe-pruning acquisition-cost comparison | proved by active-set inclusion | [P48](proposition_48_gap_dependent_stopping_complexity.md) |

P48 is a sufficient sequential upper bound. It is not a minimax lower bound or an adaptive-optimality theorem.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    text = read("pyproject.toml")
    text = replace_once(text, 'version = "0.47.0"', 'version = "0.48.0"', "pyproject version")
    text = replace_once(
        text,
        "anytime-valid sequential witness-graph refinement, robust experiment design",
        "anytime-valid sequential witness-graph refinement, gap-dependent sequential stopping complexity, robust experiment design",
        "pyproject description",
    )
    write("pyproject.toml", text)

    text = read("CITATION.cff")
    text = replace_once(text, "version: 0.47.0", "version: 0.48.0", "citation version")
    text = replace_once(
        text,
        "anytime-valid sequential witness-graph refinement, robust experiment design",
        "anytime-valid sequential witness-graph refinement, gap-dependent sequential stopping complexity, robust experiment design",
        "citation abstract",
    )
    write("CITATION.cff", text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.48.0 - 2026-09-10"):
        entry = """# 0.48.0 - 2026-09-10

- Add P48 gap-dependent stopping complexity for the P47 sequential witness graph.
- Prove deterministic lower/upper margin perturbation bounds from the edge uncertainty proxy.
- Derive an explicit sufficient local count for logarithmic time-uniform confidence envelopes.
- Prove positive-witness and all-negative finite stopping-epoch bounds.
- Make the exactly-zero-margin no-finite-bound boundary explicit.
- Add full-family and safely pruned acquisition-cost comparisons.
- Add implementation, regression tests, equation-map provenance, and a publication visual.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(
        text,
        '    "p47_sequential_graph_refinement.svg",',
        '    "p47_sequential_graph_refinement.svg",\n    "p48_gap_dependent_stopping_complexity.svg",',
        "main figure guard",
    )
    text = text.replace("for index in range(1, 48):", "for index in range(1, 49):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.47.0-2563eb", "version-0.48.0-2563eb")
    text = text.replace('version = "0\\.47\\.0"', 'version = "0\\.48\\.0"')
    text = text.replace("version: 0\\.47\\.0", "version: 0\\.48\\.0")
    marker = (
        '        "Proposition 47",\n'
        '        "p47_sequential_graph_refinement.svg",\n'
        '        "sequential_witness_graph.py",\n'
        '        "test_sequential_witness_graph.py",\n'
    )
    replacement = marker + (
        '        "Proposition 48",\n'
        '        "p48_gap_dependent_stopping_complexity.svg",\n'
        '        "gap_stopping_complexity.py",\n'
        '        "test_gap_stopping_complexity.py",\n'
    )
    text = replace_once(text, marker, replacement, "release path guards")
    write(path, text)

    write(
        "tests/test_gap_stopping_complexity_documentation.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nDOC = ROOT / "docs" / "proposition_48_gap_dependent_stopping_complexity.md"\nFIGURE = ROOT / "docs" / "figures" / "p48_gap_dependent_stopping_complexity.svg"\n\n\ndef test_p48_documentation_exposes_core_results():\n    text = DOC.read_text(encoding="utf-8")\n    for phrase in (\n        "Proposition 48A",\n        "Proposition 48B",\n        "Proposition 48C",\n        "Zero-gap boundary",\n        "Measurement-cost bound",\n        "What P48 does not prove",\n    ):\n        assert phrase in text\n\n\ndef test_p48_visual_and_proof_to_code_path_are_public():\n    assert FIGURE.exists()\n    readme = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "p48_gap_dependent_stopping_complexity.svg",\n        "gap_stopping_complexity.py",\n        "test_gap_stopping_complexity.py",\n        "P48 - gap-dependent sequential stopping complexity",\n    ):\n        assert token in readme\n''',
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
