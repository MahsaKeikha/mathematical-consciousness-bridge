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
text = replace_once(text, "version-0.66.0-2563eb", "version-0.67.0-2563eb", path)
text = replace_once(
    text,
    "**P66** then uses the budget left after P65 flooring exactly within the floor-dominating integer class: the residual budget is always smaller than the mandatory one-observation baseline cost, so a residual dynamic program can improve the P65 allocation without scaling with the full original budget magnitude.",
    "**P66** then uses the budget left after P65 flooring exactly within the floor-dominating integer class: the residual budget is always smaller than the mandatory one-observation baseline cost, so a residual dynamic program can improve the P65 allocation without scaling with the full original budget magnitude. **P67** adds a sufficient global-optimality certificate: if a budget-tight integer allocation has a common Lagrange multiplier lying in every edge's discrete marginal interval, weak duality proves that allocation is also the unrestricted P63 global optimum.",
    path,
)
text = replace_once(text, "66 proposition-level results", "67 proposition-level results", path)
text = replace_once(
    text,
    "## Latest proved extension: P66 residual-exact calibration augmentation",
    "## Previous proved extension: P66 residual-exact calibration augmentation",
    path,
)
p67_block = r'''## Latest proved extension: P67 global integer optimality certificate

![P67 global integer optimality certificate](docs/figures/p67_global_integer_optimality_certificate.svg)

P63 is the unrestricted globally exact heterogeneous-cost integer solver, while P66 is exact only inside the floor-dominating class inherited from P65. P67 asks a sharper question: **when can a candidate integer allocation be certified as the unrestricted P63 optimum without rerunning the full P63 dynamic program?**

For effective coefficients \(b_e>0\), positive integer costs \(c_e\), and integer counts \(k_e\ge1\), define the marginal objective reduction from one additional observation by

\[
\boxed{
\Delta_e(j)=b_e\left(j^{-1/2}-(j+1)^{-1/2}\right).
}
\]

For a multiplier \(\lambda>0\), the count \(k_e\) minimizes its one-edge Lagrangian term exactly when

\[
\boxed{
\frac{\Delta_e(k_e)}{c_e}
\le \lambda
\le
\frac{\Delta_e(k_e-1)}{c_e},
}
\]

with only the lower bound required when \(k_e=1\). Therefore define the common interval

\[
\boxed{
\lambda_{\rm low}=\max_e\frac{\Delta_e(k_e)}{c_e},
\qquad
\lambda_{\rm high}=\min_{e:k_e>1}\frac{\Delta_e(k_e-1)}{c_e}.
}
\]

P67 proves the following sufficient certificate. If the candidate is feasible, spends the budget exactly, and

\[
\boxed{
\lambda_{\rm low}\le\lambda_{\rm high},
}
\]

then a common multiplier exists and the separable Lagrangian plus weak duality gives

\[
\boxed{
U(k)=U_{\rm int}^*(B).
}
\]

So a P66 allocation that passes the P67 test is no longer merely restricted-exact or approximately certified: it is proved globally optimal for the unrestricted P63 integer problem. If the budget is slack or the interval intersection is empty, P67 returns **not certified**. That outcome is explicitly inconclusive and does not prove suboptimality.

The certificate is computable in \(O(m)\) time for \(m\) calibrated edges after the candidate allocation is known. It is sufficient, not necessary, and it does not replace P63 when certification fails.

The scientific boundary remains strict. P67 is an integer resource-allocation theorem for the declared calibration surrogate. It does not identify any calibration quantity with consciousness, does not solve the physical-to-experiential bridge, and makes no claim about quantum completeness.

[Read Proposition 67](docs/proposition_67_global_integer_optimality_certificate.md). The [P67 visual](docs/figures/p67_global_integer_optimality_certificate.svg), [implementation](src/consciousness_bridge/global_integer_optimality_certificate.py), and [tests](tests/test_global_integer_optimality_certificate.py) expose the proof-to-code path.

---

'''
text = replace_once(text, "# Scientific status discipline", p67_block + "# Scientific status discipline", path)
text = text.replace("P1 through P66 with explicit dependency branches", "P1 through P67 with explicit dependency branches")
write(path, text)

# Theorem roadmap
path = "docs/theorem_roadmap.md"
text = read(path)
text = replace_once(
    text,
    "![P66 residual-exact calibration augmentation](figures/p66_residual_exact_calibration_augmentation.svg)",
    "![P66 residual-exact calibration augmentation](figures/p66_residual_exact_calibration_augmentation.svg)\n![P67 global integer optimality certificate](figures/p67_global_integer_optimality_certificate.svg)",
    path,
)
text = replace_once(
    text,
    "| [P66](proposition_66_residual_exact_calibration_augmentation.md) | P65 floor, bounded residual budget, and exact residual-spend dynamic programming | best floor-dominating integer augmentation with improved computable certificate | proved restricted-exact augmentation theorem |",
    "| [P66](proposition_66_residual_exact_calibration_augmentation.md) | P65 floor, bounded residual budget, and exact residual-spend dynamic programming | best floor-dominating integer augmentation with improved computable certificate | proved restricted-exact augmentation theorem |\n| [P67](proposition_67_global_integer_optimality_certificate.md) | discrete marginal intervals, common Lagrange multiplier, and weak duality | sufficient certificate upgrading a budget-tight candidate to the unrestricted P63 optimum | proved global-optimality certificate |",
    path,
)
write(path, text)

# Research navigation
path = "docs/research_navigation.md"
text = read(path)
text = text.replace("P1 through P66", "P1 through P67")
text = replace_once(
    text,
    "| P66 | [Residual-exact calibration augmentation](proposition_66_residual_exact_calibration_augmentation.md) | exact bounded-residual optimization above the P65 floor with monotone objective improvement and a sharpened computable approximation certificate |",
    "| P66 | [Residual-exact calibration augmentation](proposition_66_residual_exact_calibration_augmentation.md) | exact bounded-residual optimization above the P65 floor with monotone objective improvement and a sharpened computable approximation certificate |\n| P67 | [Global integer optimality certificate](proposition_67_global_integer_optimality_certificate.md) | common-multiplier sufficient certificate for unrestricted P63 global optimality of a budget-tight integer candidate |",
    path,
)
write(path, text)

# Equation and citation map
path = "docs/equation_and_citation_map.md"
text = read(path)
section = r'''

# 56. P67 global integer optimality certificate

For the declared separable integer calibration objective, define the one-step marginal reduction

\[
\Delta_e(j)=b_e\left(j^{-1/2}-(j+1)^{-1/2}\right).
\]

A candidate count \(k_e\) minimizes the edgewise Lagrangian term at multiplier \(\lambda>0\) when

\[
\frac{\Delta_e(k_e)}{c_e}\le\lambda\le\frac{\Delta_e(k_e-1)}{c_e},
\]

with the upper bound omitted at \(k_e=1\). For a budget-tight feasible candidate, a nonempty common interval

\[
\max_e\frac{\Delta_e(k_e)}{c_e}
\le
\min_{e:k_e>1}\frac{\Delta_e(k_e-1)}{c_e}
\]

is sufficient, by separable Lagrangian minimization and weak duality, to prove

\[
U(k)=U_{\rm int}^*(B).
\]

**Provenance:** repository-original Proposition 67. This is a sufficient integer resource-allocation certificate. Failure of the interval test is inconclusive and is not a proof of suboptimality.
'''
if "# 56. P67 global integer optimality certificate" not in text:
    text = text.rstrip() + section + "\n"
write(path, text)

# Website index
path = "website/index.html"
text = read(path)
text = text.replace("<strong>66</strong><span>proposition-level results</span>", "<strong>67</strong><span>proposition-level results</span>")
text = text.replace("<strong>v0.66.0</strong><span>current documented release</span>", "<strong>v0.67.0</strong><span>current documented release</span>")
text = text.replace("See all 66 results grouped by scientific role", "See all 67 results grouped by scientific role")
text = text.replace("P58-P66 form the newest quantitative chain.", "P58-P67 form the newest quantitative chain.")
text = replace_once(
    text,
    '<article class="result"><span>P66</span><h3>Residual-exact augmentation</h3><p>The budget left after P65 flooring is bounded by the baseline cost, enabling exact residual optimization inside the floor-dominating integer class without a full-budget dynamic-program axis.</p></article>',
    '<article class="result"><span>P66</span><h3>Residual-exact augmentation</h3><p>The budget left after P65 flooring is bounded by the baseline cost, enabling exact residual optimization inside the floor-dominating integer class without a full-budget dynamic-program axis.</p></article>\n        <article class="result"><span>P67</span><h3>Global optimality certificate</h3><p>A common discrete marginal multiplier can certify that a budget-tight integer candidate is the unrestricted P63 optimum. Failure of the sufficient test remains inconclusive.</p></article>',
    path,
)
text = text.replace(
    "docs/figures/p66_residual_exact_calibration_augmentation.svg",
    "docs/figures/p67_global_integer_optimality_certificate.svg",
)
text = text.replace('alt="P66 residual-exact calibration augmentation"', 'alt="P67 global integer optimality certificate"')
write(path, text)

# Website research map
path = "website/research-map.html"
text = read(path)
text = text.replace("P54-P66", "P54-P67")
text = text.replace("P62-P66", "P62-P67")
text = text.replace("P58-P66", "P58-P67")
write(path, text)

# Package and citation metadata
path = "pyproject.toml"
text = read(path)
text = replace_once(text, 'version = "0.66.0"', 'version = "0.67.0"', path)
text = replace_once(text, "residual-exact calibration augmentation, robust experiment design", "residual-exact calibration augmentation, global integer optimality certification, robust experiment design", path)
write(path, text)

path = "CITATION.cff"
text = read(path)
text = replace_once(text, "version: 0.66.0", "version: 0.67.0", path)
text = text.replace("residual-exact calibration augmentation", "residual-exact calibration augmentation, global integer optimality certification")
write(path, text)

path = "CHANGELOG.md"
text = read(path)
entry = '''# 0.67.0 - 2026-09-10

- Added P67 global integer optimality certificate.
- Added an O(m) common-multiplier test for a budget-tight integer candidate.
- Proved that a successful P67 certificate upgrades the candidate to the unrestricted P63 global optimum by separable Lagrangian minimization and weak duality.
- Kept certificate failure explicitly inconclusive: it does not prove suboptimality.
- Added proof, implementation, regression tests, theorem visual, geometry guards, README integration, roadmap/navigation updates, equation provenance, and website integration.

'''
if not text.startswith("# 0.67.0 - 2026-09-10"):
    text = entry + text
write(path, text)

# Release metadata guard
path = "tests/test_release_metadata_consistency.py"
text = read(path)
text = text.replace("version-0.66.0-2563eb", "version-0.67.0-2563eb")
text = text.replace(r'^version = "0\.66\.0"$', r'^version = "0\.67\.0"$')
text = text.replace(r'^version: 0\.66\.0$', r'^version: 0\.67\.0$')
needle = '        "test_residual_exact_calibration_augmentation.py",\n'
addition = needle + '        "Proposition 67",\n        "p67_global_integer_optimality_certificate.svg",\n        "global_integer_optimality_certificate.py",\n        "test_global_integer_optimality_certificate.py",\n'
text = replace_once(text, needle, addition, path)
write(path, text)

# Website latest-figure guard
path = "tests/test_research_website_integrity.py"
text = read(path)
text = text.replace(
    'figure = "docs/figures/p66_residual_exact_calibration_augmentation.svg"',
    'figure = "docs/figures/p67_global_integer_optimality_certificate.svg"',
)
write(path, text)

# Preserve P66 as a historical release rather than the current frontier.
path = "tests/test_p66_publication_integration.py"
text = read(path)
start = text.index("def test_p66_is_integrated_across_public_record():")
end = text.index("\n\ndef test_p66_permanent_proof_code_visual_and_tests_exist():")
historical = '''def test_p66_is_preserved_in_public_record():
    required = {
        "README.md": ["Proposition 66", "p66_residual_exact_calibration_augmentation.svg"],
        "docs/theorem_roadmap.md": ["P66", "proposition_66_residual_exact_calibration_augmentation.md"],
        "docs/research_navigation.md": ["proposition_66_residual_exact_calibration_augmentation.md"],
        "docs/equation_and_citation_map.md": ["P66 residual-exact calibration augmentation", "r_{66}"],
        "CHANGELOG.md": ["# 0.66.0 - 2026-09-10", "P66 residual-exact calibration augmentation"],
    }

    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing historical P66 token: {token}"
'''
text = text[:start] + historical + text[end:]
write(path, text)

# This script is intentionally temporary and is removed before the clean PR.
