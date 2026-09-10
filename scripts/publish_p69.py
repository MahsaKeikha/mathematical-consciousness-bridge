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
text = replace_once(text, "version-0.68.0-2563eb", "version-0.69.0-2563eb", path)
p68_abstract = "**P68** turns the same Lagrangian machinery into a quantitative fallback: every positive multiplier gives a rigorous lower bound on the unrestricted P63 optimum, so any feasible candidate receives a certified additive optimality-gap bound, with P67 recovered as the zero-gap special case."
p69_abstract = p68_abstract + " **P69** optimizes that one-dimensional dual family itself: concavity and exact supergradient intervals give a monotone multiplier search, while opposing supporting lines certify how close the best evaluated lower bound is to the strongest P68 dual value without assuming strong duality."
text = replace_once(text, p68_abstract, p69_abstract, path)
text = replace_once(text, "68 proposition-level results", "69 proposition-level results", path)
text = replace_once(
    text,
    "## Latest proved extension: P68 Lagrangian optimality gap certificate",
    "## Previous proved extension: P68 Lagrangian optimality gap certificate",
    path,
)
p69_block = r'''## Latest proved extension: P69 certified dual-optimal multiplier search

![P69 certified dual-optimal multiplier search](docs/figures/p69_dual_optimal_multiplier.svg)

P68 proves that every positive multiplier \(\lambda\) gives a valid Lagrangian lower bound on the unrestricted P63 integer optimum. P69 asks how strong that lower bound can become **within the P68 dual family itself**, and certifies the numerical search without assuming that the dual optimum equals the primal optimum.

Define

\[
\boxed{
q(\lambda)
=
\sum_e
\min_{j\ge1,\;j\in\mathbb N}
\left(
\frac{b_e}{\sqrt j}+\lambda c_ej
\right)
-\lambda B,
\qquad \lambda>0.
}
\]

Because each edge term is the pointwise infimum of affine functions of \(\lambda\),

\[
\boxed{q(\lambda)\text{ is concave on }(0,\infty).}
\]

Let \(M_e(\lambda)\) be the exact set of integer counts minimizing the edgewise Lagrangian term. The complete one-dimensional supergradient interval is

\[
\boxed{
\partial^+q(\lambda)
=
\left[
\sum_e c_e\min M_e(\lambda)-B,
\sum_e c_e\max M_e(\lambda)-B
\right].
}
\]

The minimizing counts decrease monotonically as \(\lambda\) increases. Therefore the total minimizing spend is also monotone. If the supergradient interval contains zero, then \(\lambda\) is a global maximizer of the P68 dual. If the interval is positive, the maximizer lies to the right; if it is negative, the maximizer lies to the left.

For a sign-changing bracket \(\lambda_L<\lambda_R\), choose a positive supergradient \(g_L\) on the left and a negative supergradient \(g_R\) on the right. Concavity gives two global affine upper supports. Their intersection produces a computable upper bound \(Q_{\rm up}\) on the unknown strongest dual value \(q^*\), while the best evaluated dual value gives \(Q_{\rm low}\). Hence

\[
\boxed{
Q_{\rm low}
\le
q^*
\le
Q_{\rm up}.
}
\]

The P69 search stops only when

\[
\boxed{
Q_{\rm up}-Q_{\rm low}
\le
\varepsilon_{\rm dual}.
}
\]

Thus the returned multiplier achieves a valid P68 lower bound within the declared additive tolerance of the **strongest possible lower bound in this Lagrangian family**.

This does not assert strong duality. In general,

\[
\boxed{
Q_{\rm low}
\le q^*
\le U_{\rm int}^*(B).
}
\]

P67 remains the additional primal exactness theorem: when a budget-tight candidate shares a common edgewise minimizing multiplier, the primal candidate, the P68 dual value, and the P63 optimum coincide. P69 dual optimality by itself does not imply that coincidence.

The scientific boundary remains strict. P69 optimizes a certificate for the declared calibration surrogate. It does not identify that surrogate with consciousness, does not solve the physical-to-experiential bridge, and makes no claim that quantum theory is incomplete.

[Read Proposition 69](docs/proposition_69_dual_optimal_multiplier.md). The [P69 visual](docs/figures/p69_dual_optimal_multiplier.svg), [implementation](src/consciousness_bridge/dual_optimal_multiplier.py), and [tests](tests/test_dual_optimal_multiplier.py) expose the proof-to-code path.

---

'''
text = replace_once(text, "# Scientific status discipline", p69_block + "# Scientific status discipline", path)
text = text.replace("P1 through P68 with explicit dependency branches", "P1 through P69 with explicit dependency branches")
write(path, text)

# Theorem roadmap
path = "docs/theorem_roadmap.md"
text = read(path)
text = replace_once(
    text,
    "![P68 Lagrangian optimality gap certificate](figures/p68_lagrangian_optimality_gap.svg)",
    "![P68 Lagrangian optimality gap certificate](figures/p68_lagrangian_optimality_gap.svg)\n![P69 certified dual-optimal multiplier search](figures/p69_dual_optimal_multiplier.svg)",
    path,
)
text = replace_once(
    text,
    "| [P68](proposition_68_lagrangian_optimality_gap.md) | exact one-edge integer Lagrangian minimization plus weak duality | quantitative lower bound on the unrestricted P63 optimum and certified candidate optimality gap | proved Lagrangian gap certificate |",
    "| [P68](proposition_68_lagrangian_optimality_gap.md) | exact one-edge integer Lagrangian minimization plus weak duality | quantitative lower bound on the unrestricted P63 optimum and certified candidate optimality gap | proved Lagrangian gap certificate |\n| [P69](proposition_69_dual_optimal_multiplier.md) | concave dual supergradient bracketing plus supporting-line certification | strongest P68 dual lower bound to declared additive tolerance without assuming strong duality | proved dual-optimization certificate |",
    path,
)
write(path, text)

# Research navigation
path = "docs/research_navigation.md"
text = read(path)
text = text.replace("P1 through P68", "P1 through P69")
text = replace_once(
    text,
    "| P68 | [Lagrangian optimality gap certificate](proposition_68_lagrangian_optimality_gap.md) | weak-duality lower bound and quantitative additive or multiplicative candidate-quality certificate for the unrestricted P63 problem |",
    "| P68 | [Lagrangian optimality gap certificate](proposition_68_lagrangian_optimality_gap.md) | weak-duality lower bound and quantitative additive or multiplicative candidate-quality certificate for the unrestricted P63 problem |\n| P69 | [Certified dual-optimal multiplier search](proposition_69_dual_optimal_multiplier.md) | concave one-dimensional optimization of the P68 dual with exact supergradient intervals and a certified dual-value tolerance |",
    path,
)
write(path, text)

# Equation and citation map
path = "docs/equation_and_citation_map.md"
text = read(path)
section = r'''

# 58. P69 certified dual-optimal multiplier search

The P68 dual family is

\[
q(\lambda)
=
\sum_e\min_{j\ge1,\;j\in\mathbb N}
\left(\frac{b_e}{\sqrt j}+\lambda c_ej\right)-\lambda B.
\]

P69 proves that \(q\) is concave and that, for exact minimizing-count sets \(M_e(\lambda)\),

\[
\partial^+q(\lambda)
=
\left[
\sum_e c_e\min M_e(\lambda)-B,
\sum_e c_e\max M_e(\lambda)-B
\right].
\]

A zero-containing interval certifies a global dual maximizer. Otherwise monotone minimizing spend provides a sign-changing multiplier bracket. Concave supporting lines at the bracket endpoints give

\[
Q_{\rm low}\le q^*\le Q_{\rm up},
\]

and the search stops when

\[
Q_{\rm up}-Q_{\rm low}\le\varepsilon_{\rm dual}.
\]

**Provenance:** repository-original Proposition 69, building on P63, P67, and P68 plus standard concave supporting-line analysis. P69 does not assume \(q^*=U_{\rm int}^*(B)\).
'''
if "# 58. P69 certified dual-optimal multiplier search" not in text:
    text = text.rstrip() + section + "\n"
write(path, text)

# Website index
path = "website/index.html"
text = read(path)
text = text.replace("<strong>68</strong><span>proposition-level results</span>", "<strong>69</strong><span>proposition-level results</span>")
text = text.replace("<strong>v0.68.0</strong><span>current documented release</span>", "<strong>v0.69.0</strong><span>current documented release</span>")
text = text.replace("See all 68 results grouped by scientific role", "See all 69 results grouped by scientific role")
text = text.replace("P58-P68 form the newest quantitative chain.", "P58-P69 form the newest quantitative chain.")
p68_card = '<article class="result"><span>P68</span><h3>Lagrangian optimality gap</h3><p>Any positive multiplier gives a rigorous lower bound on the unrestricted P63 optimum and therefore a quantitative candidate-gap certificate. P67 is the zero-gap special case.</p></article>'
p69_card = p68_card + '\n        <article class="result"><span>P69</span><h3>Certified dual optimization</h3><p>Concavity, exact supergradient intervals, and supporting-line bounds optimize the P68 multiplier family to a certified dual-value tolerance without assuming strong duality.</p></article>'
text = replace_once(text, p68_card, p69_card, path)
text = text.replace("docs/figures/p68_lagrangian_optimality_gap.svg", "docs/figures/p69_dual_optimal_multiplier.svg")
text = text.replace('alt="P68 Lagrangian optimality gap certificate"', 'alt="P69 certified dual-optimal multiplier search"')
write(path, text)

# Website research map
path = "website/research-map.html"
text = read(path)
text = text.replace("Sixty-eight results", "Sixty-nine results")
text = text.replace("P54-P68", "P54-P69")
text = text.replace("P62-P68", "P62-P69")
text = text.replace(
    "then add the P67 common-multiplier exact certificate and P68 quantitative Lagrangian gap bound.",
    "then add the P67 common-multiplier exact certificate, P68 quantitative Lagrangian gap bound, and P69 certified optimization of the dual multiplier family.",
)
write(path, text)

# Package and citation metadata
path = "pyproject.toml"
text = read(path)
text = replace_once(text, 'version = "0.68.0"', 'version = "0.69.0"', path)
if "certified dual multiplier optimization" not in text:
    text = text.replace("Lagrangian optimality gap certification", "Lagrangian optimality gap certification, certified dual multiplier optimization")
write(path, text)

path = "CITATION.cff"
text = read(path)
text = replace_once(text, "version: 0.68.0", "version: 0.69.0", path)
if "certified dual multiplier optimization" not in text:
    text = text.replace("Lagrangian optimality gap certification", "Lagrangian optimality gap certification, certified dual multiplier optimization")
write(path, text)

path = "CHANGELOG.md"
text = read(path)
entry = '''# 0.69.0 - 2026-09-10

- Added P69 certified dual-optimal multiplier search.
- Proved concavity of the P68 one-dimensional Lagrangian dual and derived its exact supergradient interval from edgewise minimizing integer spends.
- Proved minimizing spend is monotone in the multiplier, enabling a certified sign-changing bracket search.
- Added supporting-line lower/upper certification of the strongest P68 dual value to a declared additive tolerance.
- Kept dual optimality distinct from primal exactness and retained P67 as the separate zero-primal-duality-gap certificate.
- Added proof, implementation, regression tests, theorem visual, geometry guards, README integration, roadmap/navigation updates, equation provenance, and website integration.

'''
if not text.startswith("# 0.69.0 - 2026-09-10"):
    text = entry + text
write(path, text)

# Release metadata guard
path = "tests/test_release_metadata_consistency.py"
text = read(path)
text = text.replace("version-0.68.0-2563eb", "version-0.69.0-2563eb")
text = text.replace(r'^version = "0\.68\.0"$', r'^version = "0\.69\.0"$')
text = text.replace(r'^version: 0\.68\.0$', r'^version: 0\.69\.0$')
needle = '        "test_lagrangian_optimality_gap.py",\n'
addition = needle + '        "Proposition 69",\n        "p69_dual_optimal_multiplier.svg",\n        "dual_optimal_multiplier.py",\n        "test_dual_optimal_multiplier.py",\n'
text = replace_once(text, needle, addition, path)
write(path, text)

# Website latest-figure guard
path = "tests/test_research_website_integrity.py"
text = read(path)
text = text.replace(
    'figure = "docs/figures/p68_lagrangian_optimality_gap.svg"',
    'figure = "docs/figures/p69_dual_optimal_multiplier.svg"',
)
write(path, text)

# Preserve P68 historically rather than requiring it to remain current release.
path = "tests/test_p68_publication_integration.py"
text = read(path)
start = text.index("def test_p68_is_integrated_across_public_record():")
end = text.index("\n\ndef test_p68_permanent_proof_code_visual_and_tests_exist():")
historical = '''def test_p68_is_preserved_in_public_record():
    required = {
        "README.md": ["Proposition 68", "p68_lagrangian_optimality_gap.svg"],
        "docs/theorem_roadmap.md": ["P68", "proposition_68_lagrangian_optimality_gap.md"],
        "docs/research_navigation.md": ["proposition_68_lagrangian_optimality_gap.md"],
        "docs/equation_and_citation_map.md": ["P68 Lagrangian optimality gap certificate", "q(\\\\lambda)"],
        "CHANGELOG.md": ["# 0.68.0 - 2026-09-10", "P68 Lagrangian optimality gap certificate"],
    }
    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing historical P68 token: {token}"
'''
text = text[:start] + historical + text[end:]
write(path, text)

# Historical P65 map range follows the current calibration frontier.
path = "tests/test_p65_publication_integration.py"
text = read(path)
text = text.replace('"P62-P68"', '"P62-P69"')
write(path, text)
