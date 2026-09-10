from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, path: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one occurrence of {old!r}, found {count}")
    return text.replace(old, new, 1)


# README
path = "README.md"
text = read(path)
text = replace_once(text, "version-0.69.0-2563eb", "version-0.70.0-2563eb", path)
p69_abstract = "**P69** optimizes that one-dimensional dual family itself: concavity and exact supergradient intervals give a monotone multiplier search, while opposing supporting lines certify how close the best evaluated lower bound is to the strongest P68 dual value without assuming strong duality."
p70_abstract = p69_abstract + " **P70** makes the resulting certificate diagnostic rather than opaque: for any feasible integer candidate and any positive multiplier, its candidate-to-dual gap decomposes exactly into nonnegative edgewise Lagrangian regrets plus a multiplier-weighted unused-budget penalty, with the zero decomposition recovering the P67 certificate conditions."
text = replace_once(text, p69_abstract, p70_abstract, path)
text = replace_once(text, "69 proposition-level results", "70 proposition-level results", path)
text = replace_once(
    text,
    "## Latest proved extension: P69 certified dual-optimal multiplier search",
    "## Previous proved extension: P69 certified dual-optimal multiplier search",
    path,
)
p70_block = r'''## Latest proved extension: P70 exact primal-dual gap decomposition

![P70 exact primal-dual gap decomposition](docs/figures/p70_primal_dual_gap_decomposition.svg)

P68 gives a valid lower bound from any positive Lagrange multiplier, and P69 finds the strongest value in that one-dimensional dual family to a declared tolerance. P70 asks a different question: when a feasible integer candidate still lies above the dual certificate, **where does that gap come from?**

For a feasible integer allocation \(k\), define

\[
U(k)=\sum_e\frac{b_e}{\sqrt{k_e}},
\qquad
q(\lambda)=\sum_e\phi_e(\lambda)-\lambda B,
\]

where

\[
\phi_e(\lambda)
=
\min_{j\ge1,\;j\in\mathbb N}
\left(
\frac{b_e}{\sqrt j}+\lambda c_ej
\right).
\]

For each edge, define the nonnegative Lagrangian regret

\[
\boxed{
r_e(k_e;\lambda)
=
\frac{b_e}{\sqrt{k_e}}+\lambda c_ek_e-\phi_e(\lambda)
\ge0.
}
\]

Then P70 proves the exact identity

\[
\boxed{
U(k)-q(\lambda)
=
\sum_e r_e(k_e;\lambda)
+
\lambda\left(B-\sum_e c_ek_e\right).
}
\]

The first term measures coordinate-level failure of the common-multiplier optimality conditions. The second term is the penalty from unused budget. Both are nonnegative for a feasible candidate and \(\lambda>0\).

The decomposition is zero exactly when the budget is tight and every chosen count minimizes its one-edge Lagrangian term at the same positive multiplier. Those are the P67 certificate conditions, so

\[
\boxed{
\text{zero P70 decomposition}
\Longrightarrow
U(k)=q(\lambda)=U_{\rm int}^*(B).
}
\]

P70 also composes with P69. If P69 certifies

\[
Q_{\rm low}\le q^*\le Q_{\rm up},
\]

then the candidate-to-best-dual gap satisfies

\[
\boxed{
\max\{0,U(k)-Q_{\rm up}\}
\le
U(k)-q^*
\le
\max\{0,U(k)-Q_{\rm low}\}.
}
\]

The upper endpoint also bounds the true P63 candidate suboptimality because weak duality gives \(q^*\le U_{\rm int}^*(B)\). The lower endpoint is only a lower bound on the candidate-to-best-dual gap, not on the true primal suboptimality.

Edgewise regrets are **certificate diagnostics**, not guaranteed one-edge primal improvements. Changing one count can consume budget needed elsewhere, so the coupled primal problem must remain distinct from coordinate-level attribution.

The scientific boundary remains strict. P70 is an optimization theorem for the declared transition-calibration surrogate. It does not identify the surrogate with consciousness, does not solve the physical-to-experiential bridge, and makes no claim about quantum incompleteness or ontology.

[Read Proposition 70](docs/proposition_70_primal_dual_gap_decomposition.md). The [P70 visual](docs/figures/p70_primal_dual_gap_decomposition.svg), [implementation](src/consciousness_bridge/primal_dual_gap_decomposition.py), and [tests](tests/test_primal_dual_gap_decomposition.py) expose the proof-to-code path.

---

'''
text = replace_once(text, "# Scientific status discipline", p70_block + "# Scientific status discipline", path)
text = text.replace("P1 through P69 with explicit dependency branches", "P1 through P70 with explicit dependency branches")
write(path, text)

# Theorem roadmap
path = "docs/theorem_roadmap.md"
text = read(path)
text = replace_once(
    text,
    "![P69 certified dual-optimal multiplier search](figures/p69_dual_optimal_multiplier.svg)",
    "![P69 certified dual-optimal multiplier search](figures/p69_dual_optimal_multiplier.svg)\n![P70 exact primal-dual gap decomposition](figures/p70_primal_dual_gap_decomposition.svg)",
    path,
)
text = replace_once(
    text,
    "| [P69](proposition_69_dual_optimal_multiplier.md) | concave dual supergradient bracketing plus supporting-line certification | strongest P68 dual lower bound to declared additive tolerance without assuming strong duality | proved dual-optimization certificate |",
    "| [P69](proposition_69_dual_optimal_multiplier.md) | concave dual supergradient bracketing plus supporting-line certification | strongest P68 dual lower bound to declared additive tolerance without assuming strong duality | proved dual-optimization certificate |\n| [P70](proposition_70_primal_dual_gap_decomposition.md) | exact algebraic decomposition of candidate-to-dual gap | edgewise Lagrangian mismatch plus unused-budget penalty, with P67 as the zero case | proved primal-dual diagnostic decomposition |",
    path,
)
write(path, text)

# Research navigation
path = "docs/research_navigation.md"
text = read(path)
text = text.replace("P1 through P69", "P1 through P70")
text = replace_once(
    text,
    "| P69 | [Certified dual-optimal multiplier search](proposition_69_dual_optimal_multiplier.md) | concave one-dimensional optimization of the P68 dual with exact supergradient intervals and a certified dual-value tolerance |",
    "| P69 | [Certified dual-optimal multiplier search](proposition_69_dual_optimal_multiplier.md) | concave one-dimensional optimization of the P68 dual with exact supergradient intervals and a certified dual-value tolerance |\n| P70 | [Exact primal-dual gap decomposition](proposition_70_primal_dual_gap_decomposition.md) | exact attribution of the P68 candidate-to-dual gap into edgewise Lagrangian regret and unused-budget penalty, with a P69-powered strongest-dual interval |",
    path,
)
write(path, text)

# Equation and citation map
path = "docs/equation_and_citation_map.md"
text = read(path)
section = r'''

# 59. P70 exact primal-dual gap decomposition

For any feasible integer candidate \(k\) and any \(\lambda>0\), define

\[
r_e(k_e;\lambda)
=
\frac{b_e}{\sqrt{k_e}}+\lambda c_ek_e
-
\min_{j\ge1}
\left(\frac{b_e}{\sqrt j}+\lambda c_ej\right).
\]

P70 proves the exact nonnegative decomposition

\[
U(k)-q(\lambda)
=
\sum_e r_e(k_e;\lambda)
+
\lambda\left(B-\sum_e c_ek_e\right).
\]

The decomposition is zero exactly when the candidate is budget-tight and every coordinate is an edgewise minimizer at the common multiplier, recovering the P67 sufficient global-optimality certificate conditions.

With the P69 bracket \(Q_{\rm low}\le q^*\le Q_{\rm up}\), P70 also gives

\[
\max\{0,U(k)-Q_{\rm up}\}
\le
U(k)-q^*
\le
\max\{0,U(k)-Q_{\rm low}\}.
\]

**Provenance:** repository-original Proposition 70, building on P63, P67, P68, and P69. The edgewise terms diagnose certificate mismatch at a common multiplier; they are not guaranteed one-coordinate primal improvements under the coupled budget constraint.
'''
if "# 59. P70 exact primal-dual gap decomposition" not in text:
    text = text.rstrip() + section + "\n"
write(path, text)

# Website index
path = "website/index.html"
text = read(path)
text = text.replace("<strong>69</strong><span>proposition-level results</span>", "<strong>70</strong><span>proposition-level results</span>")
text = text.replace("<strong>v0.69.0</strong><span>current documented release</span>", "<strong>v0.70.0</strong><span>current documented release</span>")
text = text.replace("See all 69 results grouped by scientific role", "See all 70 results grouped by scientific role")
text = text.replace("P58-P69 form the newest quantitative chain.", "P58-P70 form the newest quantitative chain.")
p69_card = '<article class="result"><span>P69</span><h3>Certified dual optimization</h3><p>Concavity, exact supergradient intervals, and supporting-line bounds optimize the P68 multiplier family to a certified dual-value tolerance without assuming strong duality.</p></article>'
p70_card = p69_card + '\n        <article class="result"><span>P70</span><h3>Primal-dual gap decomposition</h3><p>The candidate-to-dual certificate gap splits exactly into edgewise Lagrangian regret plus an unused-budget penalty, making a nonzero certificate diagnostically inspectable.</p></article>'
text = replace_once(text, p69_card, p70_card, path)
text = text.replace("docs/figures/p69_dual_optimal_multiplier.svg", "docs/figures/p70_primal_dual_gap_decomposition.svg")
text = text.replace('alt="P69 certified dual-optimal multiplier search"', 'alt="P70 exact primal-dual gap decomposition"')
write(path, text)

# Website research map
path = "website/research-map.html"
text = read(path)
text = text.replace("Sixty-nine results", "Seventy results")
text = text.replace("P54-P69", "P54-P70")
text = text.replace("P62-P69", "P62-P70")
text = text.replace(
    "and P69 certified optimization of the dual multiplier family.",
    "P69 certified optimization of the dual multiplier family, and P70 exact decomposition of the candidate-to-dual certificate gap.",
)
write(path, text)

# Package and citation metadata
path = "pyproject.toml"
text = read(path)
text = replace_once(text, 'version = "0.69.0"', 'version = "0.70.0"', path)
if "primal-dual gap decomposition" not in text:
    text = text.replace("certified dual multiplier optimization", "certified dual multiplier optimization, primal-dual gap decomposition")
write(path, text)

path = "CITATION.cff"
text = read(path)
text = replace_once(text, "version: 0.69.0", "version: 0.70.0", path)
if "primal-dual gap decomposition" not in text:
    text = text.replace("certified dual multiplier optimization", "certified dual multiplier optimization, primal-dual gap decomposition")
write(path, text)

# Changelog
path = "CHANGELOG.md"
text = read(path)
entry = '''# 0.70.0 - 2026-09-10

- Added P70 exact primal-dual gap decomposition and diagnostic attribution.
- Proved that every feasible candidate-to-P68-dual gap decomposes exactly into nonnegative edgewise Lagrangian regrets plus a multiplier-weighted unused-budget penalty.
- Characterized the zero decomposition as the P67 common-multiplier certificate conditions.
- Combined P69 and P70 into a certified interval for the candidate-to-best-dual gap while keeping dual optimality distinct from P63 primal exactness.
- Added proof, implementation, regression tests, theorem visual, geometry guards, README integration, roadmap/navigation updates, equation provenance, and website integration.

'''
if not text.startswith("# 0.70.0 - 2026-09-10"):
    text = entry + text
write(path, text)

# Release metadata guard
path = "tests/test_release_metadata_consistency.py"
text = read(path)
text = text.replace("version-0.69.0-2563eb", "version-0.70.0-2563eb")
text = text.replace(r'^version = "0\.69\.0"$', r'^version = "0\.70\.0"$')
text = text.replace(r'^version: 0\.69\.0$', r'^version: 0\.70\.0$')
needle = '        "test_dual_optimal_multiplier.py",\n'
addition = needle + '        "Proposition 70",\n        "p70_primal_dual_gap_decomposition.svg",\n        "primal_dual_gap_decomposition.py",\n        "test_primal_dual_gap_decomposition.py",\n'
text = replace_once(text, needle, addition, path)
write(path, text)

# Website latest-figure guard
path = "tests/test_research_website_integrity.py"
text = read(path)
text = text.replace(
    'figure = "docs/figures/p69_dual_optimal_multiplier.svg"',
    'figure = "docs/figures/p70_primal_dual_gap_decomposition.svg"',
)
write(path, text)

# Preserve P69 historically rather than requiring it to remain current release.
path = "tests/test_p69_publication_integration.py"
text = read(path)
start = text.index("def test_p69_is_integrated_across_public_record():")
end = text.index("\n\ndef test_p69_permanent_proof_code_visual_and_tests_exist():")
historical = '''def test_p69_is_preserved_in_public_record():
    required = {
        "README.md": ["Proposition 69", "p69_dual_optimal_multiplier.svg"],
        "docs/theorem_roadmap.md": ["P69", "proposition_69_dual_optimal_multiplier.md"],
        "docs/research_navigation.md": ["proposition_69_dual_optimal_multiplier.md"],
        "docs/equation_and_citation_map.md": ["P69 certified dual-optimal multiplier search", "Q_{\\\\rm low}\\\\le q^*\\\\le Q_{\\\\rm up}"],
        "CHANGELOG.md": ["# 0.69.0 - 2026-09-10", "P69 certified dual-optimal multiplier search"],
    }
    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing historical P69 token: {token}"
'''
text = text[:start] + historical + text[end:]
write(path, text)

# Historical P65 map range follows the current calibration frontier.
path = "tests/test_p65_publication_integration.py"
text = read(path)
text = text.replace('"P62-P69"', '"P62-P70"')
write(path, text)
