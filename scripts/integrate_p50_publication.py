from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P50 publication marker: {label}")
    return text.replace(old, new, 1)


def integrate_readme() -> None:
    text = read("README.md")
    if "## 13.23 P50 - bounded-starvation asynchronous sampling" in text:
        return

    text = replace_once(text, "version-0.49.0-2563eb", "version-0.50.0-2563eb", "README version")

    p49 = (
        "**P49** proves that full graph certification need only be evaluated at "
        "dyadic sample counts: the first checkpoint above any finite P48 threshold "
        "is strictly below twice that threshold, while the number of complete "
        "certification looks grows only logarithmically."
    )
    p50 = (
        p49
        + " **P50** converts P48 local thresholds into finite global-round bounds "
        "for asynchronous priority sampling under an explicit bounded-starvation "
        "condition, while proving that no finite global-time guarantee follows from "
        "P47 validity alone if a required preparation can be ignored indefinitely."
    )
    text = replace_once(text, p49, p50, "README abstract")
    text = replace_once(
        text,
        "The public research record now contains **49 proposition-level results",
        "The public research record now contains **50 proposition-level results",
        "README proposition count",
    )
    text = text.replace("P1 through P49", "P1 through P50")

    p49_row = (
        "| dyadic certification schedule | "
        "[Proposition 49](docs/proposition_49_dyadic_stopping_overhead.md) | "
        "logarithmic full-graph certification looks with strictly less than twofold "
        "sample-threshold and linear-cost overhead |"
    )
    p50_row = (
        p49_row
        + "\n| bounded-starvation asynchronous sampling | "
        "[Proposition 50](docs/proposition_50_bounded_starvation_asynchronous_sampling.md) | "
        "priority-based one-preparation-at-a-time sampling with H-fair progress, "
        "finite global-round stopping bounds, and a no-fairness impossibility result |"
    )
    text = replace_once(text, p49_row, p50_row, "README navigation")

    section = r'''
## 13.23 P50 - bounded-starvation asynchronous sampling

![P50 bounded-starvation asynchronous sampling](docs/figures/p50_bounded_starvation_asynchronous_sampling.svg)

P47 permits non-anticipating adaptive sampling while preserving statistical validity, but P48's finite stopping theorem is expressed in **local samples received by the required preparations**. P50 closes the gap between local precision and global experimental time.

At global round \(t\), an asynchronous policy selects one active preparation \(I_t\). Fix a starvation horizon \(H\ge1\). The policy is **\(H\)-fair** when every preparation that remains active throughout any block of \(H\) consecutive rounds is sampled at least once in that block.

For a preparation active throughout the first \(T\) rounds, this gives the deterministic service bound

\[
\boxed{
N_i(T)\ge\left\lfloor\frac{T}{H}\right\rfloor.
}
\]

Hence after \(HN\) rounds, every preparation active throughout that period has at least \(N\) local samples.

If at least one positive-margin edge exists, let the P48 local stopping threshold be

\[
K_+=\min_{e:M_e>0}N_e.
\]

A truly positive edge cannot be removed by P47's certified-negative pruning rule on the simultaneous good event, so both of its endpoints remain active until positive certification. Under \(H\)-fairness they therefore reach the required local count by global round

\[
\boxed{
\tau_{+,H}\le HK_+.
}
\]

If every declared edge is strictly negative and

\[
K_-=\max_{e\in E}N_e,
\]

then each negative edge either disappears earlier or, if still active, accumulates enough endpoint samples to force its P48 negative certificate. Thus

\[
\boxed{
\tau_{0,H}\le HK_-.
}
\]

Both bounds inherit the P47 simultaneous confidence guarantee

\[
\boxed{1-\alpha_Y-\alpha_Q.}
\]

The bounded-starvation premise is mathematically substantive. Without it, an adaptive policy can sample unrelated preparations indefinitely while never advancing a needed endpoint. P47 remains statistically valid at the realized local counts, but no finite global-time stopping theorem follows. P50 therefore proves the separation

\[
\boxed{
\text{statistical validity}\neq\text{sampling progress}.
}
\]

Priority sampling remains flexible: within the starvation constraint the policy may use P45 shared-uncertainty pressure, P46 graph value, P47 interval state, P48 threshold pressure, P49 batching state, or another non-anticipating score. Once a preparation is safely pruned, it no longer creates a fairness obligation.

P49 composes directly with P50. For the dyadic threshold \(D(N_e)<2N_e\), an always-active endpoint reaches that checkpoint within

\[
\boxed{
H D(N_e)<2HN_e.
}
\]

P50 is a scheduling/progress theorem. It does not prove the priority policy optimal, does not strengthen the regularity obstruction into an ontological claim, and does not establish quantum incompleteness, an extra physical dimension, or consciousness.

[Read Proposition 50](docs/proposition_50_bounded_starvation_asynchronous_sampling.md). The [P50 theorem map](docs/figures/p50_bounded_starvation_asynchronous_sampling.svg), [implementation](src/consciousness_bridge/bounded_starvation_sampling.py), and [tests](tests/test_bounded_starvation_sampling.py) expose the proof-to-code path.

'''
    marker = "---\n\n# 14. Observer-to-bridge handoff"
    text = replace_once(text, marker, section + marker, "README P50 section")
    write("README.md", text)


def integrate_roadmap() -> None:
    text = read("docs/theorem_roadmap.md")
    if "[P50](proposition_50_bounded_starvation_asynchronous_sampling.md)" in text:
        return
    visual = "![P49 dyadic stopping overhead](figures/p49_dyadic_stopping_overhead.svg)"
    text = replace_once(
        text,
        visual,
        visual + "\n\n![P50 bounded-starvation asynchronous sampling](figures/p50_bounded_starvation_asynchronous_sampling.svg)",
        "roadmap visual",
    )
    row = (
        "| [P49](proposition_49_dyadic_stopping_overhead.md) | dyadic ceiling "
        "geometry and deterministic checkpoint-count bound | logarithmic complete "
        "certification looks with strictly less than twofold stopping-threshold and "
        "linear-cost overhead | proved sequential scheduling theorem |"
    )
    row50 = (
        row
        + "\n| [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) | "
        "finite-window H-fair service guarantee plus P48 local stopping thresholds | "
        "finite global-round stopping for asynchronous priority sampling and a "
        "no-progress impossibility result without fairness | proved asynchronous "
        "scheduling theorem |"
    )
    text = replace_once(text, row, row50, "roadmap row")
    write("docs/theorem_roadmap.md", text)


def integrate_navigation() -> None:
    text = read("docs/research_navigation.md")
    if "| P50 | [Bounded-starvation asynchronous sampling]" in text:
        return
    text = text.replace("P1 through P49", "P1 through P50")
    row = (
        "| P49 | [Dyadic certification schedule]"
        "(proposition_49_dyadic_stopping_overhead.md) | logarithmic certification "
        "looks with strictly less than twofold stopping-threshold overhead |"
    )
    row50 = (
        row
        + "\n| P50 | [Bounded-starvation asynchronous sampling]"
        "(proposition_50_bounded_starvation_asynchronous_sampling.md) | H-fair "
        "priority sampling with finite global-round stopping and explicit "
        "no-starvation necessity |"
    )
    text = replace_once(text, row, row50, "navigation row")
    write("docs/research_navigation.md", text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 39. P50 bounded-starvation asynchronous sampling" in text:
        return
    addition = r'''

---

# 39. P50 bounded-starvation asynchronous sampling

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(H\)-fairness | every continuously active preparation receives service in each H-round window | repository definition | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |
| \(N_i(T)\ge\lfloor T/H\rfloor\) | deterministic local-count growth from bounded starvation | proved block-counting lemma | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |
| \(\tau_{+,H}\le HK_+\) | positive-witness global-round stopping bound | proved from P47 positive-edge persistence, P48 threshold, and H-fairness | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |
| \(\tau_{0,H}\le HK_-\) | all-negative global-round stopping bound | proved from P48 edge elimination and H-fairness | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |
| unrestricted starvation counterexample | demonstrates that P47 validity alone gives no finite global-time progress bound | proved impossibility construction | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |
| \(H D(N_e)<2HN_e\) | P49 dyadic batching composed with P50 asynchronous fairness | proved composition bound | [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) |

P50 is a progress/scheduling theorem. It does not alter the scientific meaning of the underlying regularity margin.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    text = read("pyproject.toml")
    text = replace_once(text, 'version = "0.49.0"', 'version = "0.50.0"', "pyproject version")
    text = replace_once(
        text,
        "dyadic certification scheduling, robust experiment design",
        "dyadic certification scheduling, bounded-starvation asynchronous sampling, robust experiment design",
        "pyproject description",
    )
    write("pyproject.toml", text)

    text = read("CITATION.cff")
    text = replace_once(text, "version: 0.49.0", "version: 0.50.0", "citation version")
    text = replace_once(
        text,
        "dyadic certification scheduling, robust experiment design",
        "dyadic certification scheduling, bounded-starvation asynchronous sampling, robust experiment design",
        "citation abstract",
    )
    write("CITATION.cff", text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.50.0 - 2026-09-10"):
        entry = """# 0.50.0 - 2026-09-10

- Add P50 bounded-starvation asynchronous sampling.
- Define H-fair finite-window service for still-active preparations.
- Prove local-count growth N_i(T) >= floor(T/H).
- Lift P48 positive and all-negative local thresholds to finite global-round bounds H K_+ and H K_-.
- Prove that unrestricted starvation prevents any finite global-time theorem from P47 validity alone.
- Preserve dynamic safe pruning and non-anticipating priority freedom.
- Compose P49 dyadic batching with P50 fairness via H D(N_e) < 2 H N_e.
- Add implementation, regression tests, theorem visual, and equation-map provenance.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    text = replace_once(
        text,
        '    "p49_dyadic_stopping_overhead.svg",',
        '    "p49_dyadic_stopping_overhead.svg",\n    "p50_bounded_starvation_asynchronous_sampling.svg",',
        "main figure guard",
    )
    text = text.replace("for index in range(1, 50):", "for index in range(1, 51):")
    write(path, text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.49.0-2563eb", "version-0.50.0-2563eb")
    text = text.replace('version = "0\\.49\\.0"', 'version = "0\\.50\\.0"')
    text = text.replace("version: 0\\.49\\.0", "version: 0\\.50\\.0")
    marker = (
        '        "Proposition 49",\n'
        '        "p49_dyadic_stopping_overhead.svg",\n'
        '        "dyadic_stopping_overhead.py",\n'
        '        "test_dyadic_stopping_overhead.py",\n'
    )
    replacement = marker + (
        '        "Proposition 50",\n'
        '        "p50_bounded_starvation_asynchronous_sampling.svg",\n'
        '        "bounded_starvation_sampling.py",\n'
        '        "test_bounded_starvation_sampling.py",\n'
    )
    text = replace_once(text, marker, replacement, "release path guards")
    write(path, text)

    write(
        "tests/test_bounded_starvation_sampling_documentation.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nDOC = ROOT / "docs" / "proposition_50_bounded_starvation_asynchronous_sampling.md"\nFIGURE = ROOT / "docs" / "figures" / "p50_bounded_starvation_asynchronous_sampling.svg"\n\n\ndef test_p50_documentation_exposes_core_results():\n    text = DOC.read_text(encoding="utf-8")\n    for phrase in (\n        "Proposition 50A",\n        "Proposition 50B",\n        "Proposition 50C",\n        "Bounded-starvation condition",\n        "Dynamic pruning is compatible",\n        "Scientific interpretation boundary",\n    ):\n        assert phrase in text\n\n\ndef test_p50_visual_and_proof_to_code_path_are_public():\n    assert FIGURE.exists()\n    readme = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "p50_bounded_starvation_asynchronous_sampling.svg",\n        "bounded_starvation_sampling.py",\n        "test_bounded_starvation_sampling.py",\n        "P50 - bounded-starvation asynchronous sampling",\n    ):\n        assert token in readme\n''',
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
