from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_required(text: str, old: str, new: str, *, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing integration marker: {label}")
    return text.replace(old, new, 1)


def integrate_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## 13.20 P47 - anytime-valid sequential witness-graph refinement" in text:
        return

    text = replace_required(
        text,
        "version-0.46.0-2563eb",
        "version-0.47.0-2563eb",
        label="README version badge",
    )
    p46_sentence = (
        "**P46** adds the hard-budget discrete layer: it proves the induced witness "
        "value is monotone and supermodular, proves the general budgeted selection "
        "problem is NP-hard by reduction from CLIQUE, and gives a computable "
        "weighted-degree relaxation that certifies an upper bound on the unknown "
        "optimum."
    )
    p47_sentence = (
        p46_sentence
        + " **P47** closes the adaptive-sampling validity gap: preparation-level "
        "time-uniform confidence sequences are combined into one finite-family "
        "event that remains valid under non-anticipating adaptive preparation "
        "sampling, graph refinement, witness selection, safe pruning, and stopping."
    )
    text = replace_required(
        text,
        p46_sentence,
        p47_sentence,
        label="README P46 abstract sentence",
    )
    text = replace_required(
        text,
        "The public research record now contains **46 proposition-level results",
        "The public research record now contains **47 proposition-level results",
        label="README proposition count",
    )
    text = text.replace("P1 through P46", "P1 through P47")

    p46_row = (
        "| budget-constrained witness graph | "
        "[Proposition 46](docs/proposition_46_budget_constrained_witness_graph.md) | "
        "hard-budget preparation selection, NP-hardness, weighted-degree upper "
        "bound, and exact small-instance solver |"
    )
    p47_row = (
        p46_row
        + "\n| anytime sequential witness graph | "
        "[Proposition 47](docs/proposition_47_anytime_sequential_witness_graph.md) | "
        "time-uniform adaptive preparation sampling, safe pruning, post-selection, "
        "and stopping under one simultaneous family event |"
    )
    text = replace_required(text, p46_row, p47_row, label="README P46 nav row")

    section = r'''
## 13.20 P47 - anytime-valid sequential witness-graph refinement

![P47 anytime-valid sequential witness graph](docs/figures/p47_sequential_graph_refinement.svg)

P46 exposes a practical statistical gap. A real experiment may use early observations to decide which preparation to sample next, which witness edges remain active, how shared precision is allocated, and when the experiment stops. Fixed-sample guarantees do not automatically remain valid when the local sample counts are themselves chosen from the data.

P47 closes that gap by assigning every declared preparation-level target and quantum stream an all-local-sample-size confidence sequence. If

\[
\mathcal E_*
=
\bigcap_{i\in V}
\left(\mathcal E_{Y,i}\cap\mathcal E_{Q,i}\right),
\]

then finite-family error allocation gives

\[
\boxed{
\Pr(\mathcal E_*)
\ge
1-\alpha_Y-\alpha_Q.
}
\]

On this one event, the preparation-level uncertainty bounds are valid for every local sample size. They therefore remain valid after substitution of the random local counts produced by any non-anticipating adaptive policy.

For an edge \(e=\{i,j\}\), let

\[
M_e=d_{Y,e}-L_e d_{Q,e}
\]

be the population regularity margin. The adaptive-time edge interval is

\[
\boxed{
\underline M_e(t)
\le
M_e
\le
\overline M_e(t)
\qquad
\forall e\in E,
\ \forall t,
}
\]

where the lower endpoint uses the smallest target separation and largest quantum separation compatible with the current preparation-level confidence radii, and the upper endpoint uses the reverse choices.

This simultaneous statement has three immediate consequences.

First, any data-dependent edge selector \(\widehat e_t\) remains covered. Second, an edge with \(\overline M_e(t)<0\) can be eliminated safely, and a preparation can be pruned when all of its incident declared edges are certified negative. Third, any stopping rule \(\tau\) based on the observed history remains valid because the certificate already holds at every global time.

Thus

\[
\boxed{
\underline M_{\widehat e_\tau}(\tau)>0
\Longrightarrow
M_{\widehat e_\tau}>0
}
\]

with the declared global confidence level.

The full adaptive design chain is now

\[
\boxed{
\text{P24 all-time validity}
+
\text{P44 family post-selection}
+
\text{P45 shared precision}
+
\text{P46 budgeted graph selection}
\longrightarrow
\text{P47 sequential graph refinement and stopping}.
}
\]

P47 deliberately separates **validity** from **efficiency**. P45 and P46 may be used inside the adaptive policy to decide where measurements are most valuable, while P47 guarantees that such history-dependent choices do not invalidate the final certificate. If a truly positive-margin edge continues to receive samples and the preparation-level radii converge to zero, its lower margin converges to the positive population margin and is eventually detected under the stated consistency assumptions.

The scientific boundary remains strict. A positive P47 margin rejects only the declared regular bridge class for the declared physical and target models. It does not establish quantum incompleteness, an extra physical dimension, or an experiential interpretation.

[Read Proposition 47](docs/proposition_47_anytime_sequential_witness_graph.md). The [P47 theorem map](docs/figures/p47_sequential_graph_refinement.svg), [implementation](src/consciousness_bridge/sequential_witness_graph.py), and [tests](tests/test_sequential_witness_graph.py) expose the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = replace_required(text, marker, section + marker, label="README P47 insertion")
    write(path, text)


def integrate_theorem_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P47](proposition_47_anytime_sequential_witness_graph.md)" in text:
        return
    visual = (
        "![P46 budget-constrained witness graph](figures/p46_budget_constrained_witness_graph.svg)"
    )
    text = replace_required(
        text,
        visual,
        visual
        + "\n\n![P47 anytime-valid sequential witness graph]"
        "(figures/p47_sequential_graph_refinement.svg)",
        label="roadmap P46 visual",
    )
    row = (
        "| [P46](proposition_46_budget_constrained_witness_graph.md) | monotone "
        "supermodular induced-edge objective, CLIQUE reduction, and fractional "
        "degree-knapsack bound | hard-budget preparation selection with certified "
        "optimality gap | proved combinatorial design theorem |"
    )
    row47 = (
        row
        + "\n| [P47](proposition_47_anytime_sequential_witness_graph.md) | "
        "finite-family all-local-time confidence event plus adaptive local-count "
        "substitution and simultaneous edge envelopes | valid non-anticipating "
        "adaptive preparation sampling, graph refinement, witness selection, "
        "pruning, and stopping | proved anytime-valid sequential-design theorem |"
    )
    text = replace_required(text, row, row47, label="roadmap P46 row")
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P47 | [Anytime sequential witness graph]" in text:
        return
    text = text.replace("P1 through P46", "P1 through P47")
    row = (
        "| P46 | [Budget-constrained witness graph]"
        "(proposition_46_budget_constrained_witness_graph.md) | discrete preparation "
        "selection, NP-hardness, relaxation upper bound, and exact small-instance "
        "certification |"
    )
    row47 = (
        row
        + "\n| P47 | [Anytime sequential witness graph]"
        "(proposition_47_anytime_sequential_witness_graph.md) | time-uniform "
        "adaptive preparation sampling, graph refinement, witness selection, "
        "safe pruning, and stopping |"
    )
    text = replace_required(text, row, row47, label="navigation P46 row")
    write(path, text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 36. P47 anytime-valid sequential witness graph" in text:
        return
    addition = r'''

---

# 36. P47 anytime-valid sequential witness graph

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\mathcal E_*=\bigcap_i(\mathcal E_{Y,i}\cap\mathcal E_{Q,i})\) | one event covering every declared preparation stream and every local sample size | repository definition | [P47](proposition_47_anytime_sequential_witness_graph.md) |
| \(\Pr(\mathcal E_*)\ge1-\alpha_Y-\alpha_Q\) | finite-family simultaneous coverage | proved by union bound from preparation-level confidence sequences | [P47](proposition_47_anytime_sequential_witness_graph.md) |
| \(N_{Y,i}(t),N_{Q,i}(t)\) | history-dependent local sample counts | adaptive design object | [P47](proposition_47_anytime_sequential_witness_graph.md) |
| \(\underline M_e(t)\le M_e\le\overline M_e(t)\) | simultaneous regularity-margin envelope for every declared edge and global time | proved from metric triangle inequalities on \(\mathcal E_*\) | [P47](proposition_47_anytime_sequential_witness_graph.md) |
| \(\underline M_{\widehat e_\tau}(\tau)>0\Rightarrow M_{\widehat e_\tau}>0\) | selected-edge stopping-time certificate | proved from the simultaneous event | [P47](proposition_47_anytime_sequential_witness_graph.md) |
| \(\overline M_e(t)<0\) | safe edge elimination criterion | proved from simultaneous upper coverage | [P47](proposition_47_anytime_sequential_witness_graph.md) |

P47 is a time-uniform statistical and experimental-design result. It does not convert a regularity obstruction into an ontological or experiential conclusion.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_release_metadata() -> None:
    pyproject = read("pyproject.toml")
    pyproject = replace_required(
        pyproject,
        'version = "0.46.0"',
        'version = "0.47.0"',
        label="pyproject version",
    )
    pyproject = replace_required(
        pyproject,
        "budget-constrained witness-graph selection, robust experiment design",
        "budget-constrained witness-graph selection, anytime-valid sequential "
        "witness-graph refinement, robust experiment design",
        label="pyproject description",
    )
    write("pyproject.toml", pyproject)

    citation = read("CITATION.cff")
    citation = replace_required(
        citation,
        "version: 0.46.0",
        "version: 0.47.0",
        label="citation version",
    )
    citation = replace_required(
        citation,
        "date-released: 2026-09-09",
        "date-released: 2026-09-10",
        label="citation release date",
    )
    citation = replace_required(
        citation,
        "budget-constrained witness-graph selection, robust experiment design",
        "budget-constrained witness-graph selection, anytime-valid sequential "
        "witness-graph refinement, robust experiment design",
        label="citation abstract",
    )
    write("CITATION.cff", citation)

    changelog = read("CHANGELOG.md")
    if not changelog.startswith("# 0.47.0 - 2026-09-10"):
        entry = """# 0.47.0 - 2026-09-10

- Add P47 anytime-valid sequential witness-graph refinement.
- Prove simultaneous preparation-level confidence coverage over every local sample size.
- Prove validity under non-anticipating adaptive preparation sampling and random local counts.
- Add simultaneous lower and upper regularity-margin envelopes for every declared edge and global time.
- Add valid data-dependent witness selection, stopping, safe edge elimination, and vertex pruning.
- Connect P24, P44, P45, and P46 into one sequential experimental-design theorem.
- Add a publication visual, implementation, regression tests, and strict scientific-boundary language.

"""
        write("CHANGELOG.md", entry + changelog)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    if '"p47_sequential_graph_refinement.svg"' not in text:
        text = replace_required(
            text,
            '    "p46_budget_constrained_witness_graph.svg",',
            '    "p46_budget_constrained_witness_graph.svg",\n'
            '    "p47_sequential_graph_refinement.svg",',
            label="main-page figure guard",
        )
    text = text.replace("for index in range(1, 47):", "for index in range(1, 48):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.46.0-2563eb", "version-0.47.0-2563eb")
    text = text.replace('version = "0\\.46\\.0"', 'version = "0\\.47\\.0"')
    text = text.replace("version: 0\\.46\\.0", "version: 0\\.47\\.0")
    p46_tokens = (
        '        "Proposition 46",\n'
        '        "p46_budget_constrained_witness_graph.svg",\n'
        '        "budget_constrained_witness_graph.py",\n'
        '        "test_budget_constrained_witness_graph.py",\n'
    )
    if '        "Proposition 47",' not in text:
        p47_tokens = p46_tokens + (
            '        "Proposition 47",\n'
            '        "p47_sequential_graph_refinement.svg",\n'
            '        "sequential_witness_graph.py",\n'
            '        "test_sequential_witness_graph.py",\n'
        )
        text = replace_required(
            text,
            p46_tokens,
            p47_tokens,
            label="release P47 path guards",
        )
    write(path, text)

    doc_test = ROOT / "tests" / "test_sequential_witness_graph_documentation.py"
    doc_test.write_text(
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nDOC = ROOT / "docs" / "proposition_47_anytime_sequential_witness_graph.md"\nFIGURE = ROOT / "docs" / "figures" / "p47_sequential_graph_refinement.svg"\n\n\ndef test_p47_documentation_exposes_core_theorem_objects():\n    text = DOC.read_text(encoding="utf-8")\n    for phrase in (\n        "Proposition 47A",\n        "Proposition 47B",\n        "Proposition 47C",\n        "Proposition 47D",\n        "Proposition 47E",\n        "Proposition 47F",\n        "adaptive local-count substitution",\n        "safe elimination",\n        "Scientific boundary",\n    ):\n        assert phrase in text\n\n\ndef test_p47_publication_visual_exists_and_is_linked():\n    assert FIGURE.exists()\n    readme = (ROOT / "README.md").read_text(encoding="utf-8")\n    assert "p47_sequential_graph_refinement.svg" in readme\n    assert "P47 sequential graph refinement and stopping" in readme\n''',
        encoding="utf-8",
    )


def normalize_p47_visual() -> None:
    source = ROOT / "figures" / "p47_sequential_graph_refinement.svg"
    destination = ROOT / "docs" / "figures" / "p47_sequential_graph_refinement.svg"
    destination.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    source.unlink()

    path = "docs/proposition_47_anytime_sequential_witness_graph.md"
    text = read(path)
    text = text.replace(
        "[`p47_sequential_graph_refinement.svg`](../figures/p47_sequential_graph_refinement.svg)",
        "[`p47_sequential_graph_refinement.svg`](figures/p47_sequential_graph_refinement.svg)",
    )
    write(path, text)


def main() -> None:
    normalize_p47_visual()
    integrate_readme()
    integrate_theorem_roadmap()
    integrate_navigation()
    integrate_equation_map()
    integrate_release_metadata()
    integrate_tests()


if __name__ == "__main__":
    main()
