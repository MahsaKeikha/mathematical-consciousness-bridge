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
text = replace_once(text, "version-0.67.0-2563eb", "version-0.68.0-2563eb", path)
text = replace_once(
    text,
    "**P67** adds a sufficient global-optimality certificate: if a budget-tight integer allocation has a common Lagrange multiplier lying in every edge's discrete marginal interval, weak duality proves that allocation is also the unrestricted P63 global optimum.",
    "**P67** adds a sufficient global-optimality certificate: if a budget-tight integer allocation has a common Lagrange multiplier lying in every edge's discrete marginal interval, weak duality proves that allocation is also the unrestricted P63 global optimum. **P68** turns the same Lagrangian machinery into a quantitative fallback: every positive multiplier gives a rigorous lower bound on the unrestricted P63 optimum, so any feasible candidate receives a certified additive optimality-gap bound, with P67 recovered as the zero-gap special case.",
    path,
)
text = replace_once(text, "67 proposition-level results", "68 proposition-level results", path)
text = replace_once(
    text,
    "## Latest proved extension: P67 global integer optimality certificate",
    "## Previous proved extension: P67 global integer optimality certificate",
    path,
)
p68_block = r'''## Latest proved extension: P68 Lagrangian optimality gap certificate

![P68 Lagrangian optimality gap certificate](docs/figures/p68_lagrangian_optimality_gap.svg)

P67 can sometimes certify a candidate integer allocation as exactly equal to the unrestricted P63 optimum. P68 covers the complementary case without weakening the scientific standard: when exact certification does not close, it computes a rigorous **lower bound** on the unknown P63 optimum and therefore a quantitative upper bound on the candidate's possible suboptimality.

For any positive multiplier \(\lambda>0\), define

\[
\boxed{
q(\lambda)
=
\sum_e
\min_{j\ge1,\ j\in\mathbb N}
\left[
\frac{b_e}{\sqrt j}+\lambda c_ej
\right]
-\lambda B.
}
\]

Weak duality gives

\[
\boxed{q(\lambda)\le U_{\rm int}^*(B).}
\]

Therefore every feasible integer candidate \(\widehat k\) satisfies

\[
\boxed{
0\le U(\widehat k)-U_{\rm int}^*(B)
\le U(\widehat k)-q(\lambda).
}
\]

When \(q(\lambda)>0\), P68 also gives the multiplicative certificate

\[
\boxed{
\frac{U(\widehat k)}{U_{\rm int}^*(B)}
\le
\frac{U(\widehat k)}{q(\lambda)}.
}
\]

Each one-edge Lagrangian minimum is exact. The continuous stationary count is

\[
\boxed{
x_e^{(0)}=
\left(\frac{b_e}{2\lambda c_e}\right)^{2/3},
}
\]

and strict convexity means the integer minimum is attained among the neighboring integer counts around \(\max\{1,x_e^{(0)}\}\). Thus a fixed-multiplier P68 certificate is computable in \(O(m)\) time after the candidate is known.

If P67 succeeds, its common multiplier makes the candidate minimize every edgewise Lagrangian term and the tight budget removes the penalty term. P68 then recovers

\[
\boxed{q(\lambda)=U(\widehat k)=U_{\rm int}^*(B),}
\]

so the additive gap is exactly zero. If P67 fails, P68 does not call the candidate suboptimal. It reports a quantitative bound whose validity holds for every declared positive multiplier. The automatic multiplier selection is only a reproducible witness rule and is not claimed to maximize the dual.

The scientific boundary remains strict. P68 is an optimization theorem for the declared calibration surrogate. A small optimization gap is not evidence that the surrogate identifies consciousness, and the theorem makes no claim about a physical-to-experiential bridge or quantum completeness.

[Read Proposition 68](docs/proposition_68_lagrangian_optimality_gap.md). The [P68 visual](docs/figures/p68_lagrangian_optimality_gap.svg), [implementation](src/consciousness_bridge/lagrangian_optimality_gap.py), and [tests](tests/test_lagrangian_optimality_gap.py) expose the proof-to-code path.

---

'''
text = replace_once(text, "# Scientific status discipline", p68_block + "# Scientific status discipline", path)
text = text.replace("P1 through P67 with explicit dependency branches", "P1 through P68 with explicit dependency branches")
write(path, text)

# Theorem roadmap
path = "docs/theorem_roadmap.md"
text = read(path)
text = replace_once(
    text,
    "![P67 global integer optimality certificate](figures/p67_global_integer_optimality_certificate.svg)",
    "![P67 global integer optimality certificate](figures/p67_global_integer_optimality_certificate.svg)\n![P68 Lagrangian optimality gap certificate](figures/p68_lagrangian_optimality_gap.svg)",
    path,
)
text = replace_once(
    text,
    "| [P67](proposition_67_global_integer_optimality_certificate.md) | discrete marginal intervals, common Lagrange multiplier, and weak duality | sufficient certificate upgrading a budget-tight candidate to the unrestricted P63 optimum | proved global-optimality certificate |",
    "| [P67](proposition_67_global_integer_optimality_certificate.md) | discrete marginal intervals, common Lagrange multiplier, and weak duality | sufficient certificate upgrading a budget-tight candidate to the unrestricted P63 optimum | proved global-optimality certificate |\n| [P68](proposition_68_lagrangian_optimality_gap.md) | exact one-edge integer Lagrangian minimization plus weak duality | quantitative lower bound on the unrestricted P63 optimum and certified candidate optimality gap | proved Lagrangian gap certificate |",
    path,
)
write(path, text)

# Research navigation
path = "docs/research_navigation.md"
text = read(path)
text = text.replace("P1 through P67", "P1 through P68")
text = replace_once(
    text,
    "| P67 | [Global integer optimality certificate](proposition_67_global_integer_optimality_certificate.md) | common-multiplier sufficient certificate for unrestricted P63 global optimality of a budget-tight integer candidate |",
    "| P67 | [Global integer optimality certificate](proposition_67_global_integer_optimality_certificate.md) | common-multiplier sufficient certificate for unrestricted P63 global optimality of a budget-tight integer candidate |\n| P68 | [Lagrangian optimality gap certificate](proposition_68_lagrangian_optimality_gap.md) | weak-duality lower bound and quantitative additive or multiplicative candidate-quality certificate for the unrestricted P63 problem |",
    path,
)
write(path, text)

# Equation and citation map
path = "docs/equation_and_citation_map.md"
text = read(path)
section = r'''

# 57. P68 Lagrangian optimality gap certificate

For any positive multiplier \(\lambda>0\), define

\[
q(\lambda)
=
\sum_e\min_{j\ge1,\ j\in\mathbb N}
\left(\frac{b_e}{\sqrt j}+\lambda c_ej\right)-\lambda B.
\]

Weak duality gives

\[
q(\lambda)\le U_{\rm int}^*(B).
\]

Hence every feasible candidate \(\widehat k\) satisfies

\[
0\le U(\widehat k)-U_{\rm int}^*(B)
\le U(\widehat k)-q(\lambda).
\]

For a fixed edge, the real Lagrangian stationary point is

\[
x_e^{(0)}=\left(\frac{b_e}{2\lambda c_e}\right)^{2/3},
\]

and strict convexity reduces exact integer minimization to the neighboring integers around \(\max\{1,x_e^{(0)}\}\). P67 is the zero-gap special case when its common multiplier exists and the candidate spends the budget tightly.

**Provenance:** repository-original Proposition 68. The automatic multiplier is a reproducible witness-selection rule, not a claim of dual maximization. The result is an optimization guarantee for the declared calibration surrogate only.
'''
if "# 57. P68 Lagrangian optimality gap certificate" not in text:
    text = text.rstrip() + section + "\n"
write(path, text)

# Website index
path = "website/index.html"
text = read(path)
text = text.replace("<strong>67</strong><span>proposition-level results</span>", "<strong>68</strong><span>proposition-level results</span>")
text = text.replace("<strong>v0.67.0</strong><span>current documented release</span>", "<strong>v0.68.0</strong><span>current documented release</span>")
text = text.replace("See all 67 results grouped by scientific role", "See all 68 results grouped by scientific role")
text = text.replace("P58-P67 form the newest quantitative chain.", "P58-P68 form the newest quantitative chain.")
text = replace_once(
    text,
    '<article class="result"><span>P67</span><h3>Global optimality certificate</h3><p>A common discrete marginal multiplier can certify that a budget-tight integer candidate is the unrestricted P63 optimum. Failure of the sufficient test remains inconclusive.</p></article>',
    '<article class="result"><span>P67</span><h3>Global optimality certificate</h3><p>A common discrete marginal multiplier can certify that a budget-tight integer candidate is the unrestricted P63 optimum. Failure of the sufficient test remains inconclusive.</p></article>\n        <article class="result"><span>P68</span><h3>Lagrangian optimality gap</h3><p>Any positive multiplier gives a rigorous lower bound on the unrestricted P63 optimum and therefore a quantitative candidate-gap certificate. P67 is the zero-gap special case.</p></article>',
    path,
)
text = text.replace(
    "docs/figures/p67_global_integer_optimality_certificate.svg",
    "docs/figures/p68_lagrangian_optimality_gap.svg",
)
text = text.replace('alt="P67 global integer optimality certificate"', 'alt="P68 Lagrangian optimality gap certificate"')
write(path, text)

# Website research map
path = "website/research-map.html"
text = read(path)
text = text.replace("Sixty-seven results", "Sixty-eight results")
text = text.replace("P54-P67", "P54-P68")
text = text.replace("P62-P67", "P62-P68")
text = text.replace(
    "then add the P67 common-multiplier certificate for unrestricted global optimality.",
    "then add the P67 common-multiplier exact certificate and P68 quantitative Lagrangian gap bound.",
)
write(path, text)

# Package and citation metadata
path = "pyproject.toml"
text = read(path)
text = replace_once(text, 'version = "0.67.0"', 'version = "0.68.0"', path)
if "Lagrangian optimality gap" not in text:
    text = text.replace("global integer optimality certification", "global integer optimality certification, Lagrangian optimality gap certification")
write(path, text)

path = "CITATION.cff"
text = read(path)
text = replace_once(text, "version: 0.67.0", "version: 0.68.0", path)
if "Lagrangian optimality gap" not in text:
    text = text.replace("global integer optimality certification", "global integer optimality certification, Lagrangian optimality gap certification")
write(path, text)

path = "CHANGELOG.md"
text = read(path)
entry = '''# 0.68.0 - 2026-09-10

- Added P68 Lagrangian optimality gap certificate.
- Proved that every positive multiplier gives a weak-duality lower bound on the unrestricted P63 integer optimum.
- Added rigorous additive candidate-gap bounds and multiplicative factors when the dual lower bound is positive.
- Proved exact one-edge integer Lagrangian minimization by checking the neighboring integers around the strictly convex continuous stationary point.
- Recovered P67 as the zero-gap special case without claiming that the automatic P68 multiplier maximizes the dual.
- Added proof, implementation, regression tests, theorem visual, geometry guards, README integration, roadmap/navigation updates, equation provenance, and website integration.

'''
if not text.startswith("# 0.68.0 - 2026-09-10"):
    text = entry + text
write(path, text)

# Release metadata guard
path = "tests/test_release_metadata_consistency.py"
text = read(path)
text = text.replace("version-0.67.0-2563eb", "version-0.68.0-2563eb")
text = text.replace(r'^version = "0\.67\.0"$', r'^version = "0\.68\.0"$')
text = text.replace(r'^version: 0\.67\.0$', r'^version: 0\.68\.0$')
needle = '        "test_global_integer_optimality_certificate.py",\n'
addition = needle + '        "Proposition 68",\n        "p68_lagrangian_optimality_gap.svg",\n        "lagrangian_optimality_gap.py",\n        "test_lagrangian_optimality_gap.py",\n'
text = replace_once(text, needle, addition, path)
write(path, text)

# Website latest-figure guard
path = "tests/test_research_website_integrity.py"
text = read(path)
text = text.replace(
    'figure = "docs/figures/p67_global_integer_optimality_certificate.svg"',
    'figure = "docs/figures/p68_lagrangian_optimality_gap.svg"',
)
write(path, text)

# Preserve P67 historically rather than requiring it to remain the current release.
path = "tests/test_p67_publication_integration.py"
text = read(path)
start = text.index("def test_p67_is_integrated_across_public_record():")
end = text.index("\n\ndef test_p67_permanent_proof_code_visual_and_tests_exist():")
historical = '''def test_p67_is_preserved_in_public_record():
    required = {
        "README.md": ["Proposition 67", "p67_global_integer_optimality_certificate.svg"],
        "docs/theorem_roadmap.md": ["P67", "proposition_67_global_integer_optimality_certificate.md"],
        "docs/research_navigation.md": ["proposition_67_global_integer_optimality_certificate.md"],
        "docs/equation_and_citation_map.md": ["P67 global integer optimality certificate", "\\\\Delta_e(j)"],
        "CHANGELOG.md": ["# 0.67.0 - 2026-09-10", "P67 global integer optimality certificate"],
    }
    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing historical P67 token: {token}"
'''
text = text[:start] + historical + text[end:]
write(path, text)
