from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace(text: str, old: str, new: str) -> str:
    return text.replace(old, new) if old in text else text


def insert_before(text: str, marker: str, addition: str) -> str:
    if addition.strip() in text:
        return text
    if marker not in text:
        raise RuntimeError(f"missing insertion marker: {marker[:100]!r}")
    return text.replace(marker, addition + marker, 1)


def insert_after(text: str, marker: str, addition: str) -> str:
    if addition.strip() in text:
        return text
    if marker not in text:
        raise RuntimeError(f"missing insertion marker: {marker[:100]!r}")
    return text.replace(marker, marker + addition, 1)


def update_pyproject() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace(text, 'version = "0.79.0"', 'version = "0.80.0"')
    anchor = "certified rational P77 sampling-radius envelopes, exact-rational logarithm and dyadic square-root certification,"
    addition = (
        "certified rational P77 sampling-radius envelopes, exact-rational logarithm and dyadic square-root certification, "
        "simplex-coupled interval relaxations, exact-rational probability-simplex distance certification,"
    )
    text = replace(text, anchor, addition)
    write(path, text)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    text = replace(text, "version-0.79.0-2563eb", "version-0.80.0-2563eb")
    text = replace(text, "Version 0.79.0", "Version 0.80.0")
    text = replace(text, "v0.79.0", "v0.80.0")
    text = replace(text, "P1 through P79", "P1 through P80")
    text = replace(text, "P1 to P79", "P1 to P80")
    text = replace(text, "P19-P24, P71-P79", "P19-P24, P71-P80")
    text = replace(text, "P71-P79 return", "P71-P80 return")
    text = replace(text, "P71-P79 form", "P71-P80 form")
    text = replace(text, "P71-P79", "P71-P80")
    text = replace(text, "**79 proposition-level results**", "**80 proposition-level results**")
    text = replace(text, "**67 equation-driven quantitative figures**", "**68 equation-driven quantitative figures**")
    text = replace(text, "The theorem frontier is P79.", "The theorem frontier is P80.")
    text = replace(text, "| Public theorem frontier | **P79** |", "| Public theorem frontier | **P80** |")
    text = replace(text, "| Documented version | **v0.79.0** |", "| Documented version | **v0.80.0** |")
    text = replace(text, "| Proposition-level results | **79** |", "| Proposition-level results | **80** |")
    text = replace(text, "| Equation-driven quantitative figures | **67** |", "| Equation-driven quantitative figures | **68** |")

    p80_plain = """

P80 tightens the continuous-family certificate itself. P78 encloses each observed probability cell over a parameter box, but its original lower bound treats those cell intervals independently. Every admissible probability law must also sum to one. P80 intersects the exact P78 intervals with that probability-simplex constraint and computes the resulting L-infinity distance exactly in rational arithmetic. The tightened relaxation still contains every P75 law in the parameter box, so the bound remains conservative, while the smaller feasible set can only make the lower bound stronger. The P80 bound therefore dominates the corresponding P78 box bound and can certify separation with fewer refinements in cases where normalization coupling matters. This is a computational tightening of the declared P75 model test, not a new consciousness assumption.
"""
    if "P80 tightens the continuous-family certificate itself" not in text:
        marker = "\nOnly after the physical description, the target, and the way the target is measured are all scientifically defensible"
        text = insert_before(text, marker, p80_plain)

    if "P80 supplies a tighter simplex-coupled" not in text:
        old = "Together they are intended to remove hidden assumptions one by one."
        new = (
            "P80 then strengthens the P78 continuous-family lower bound by retaining probability-simplex normalization inside every exact interval relaxation. "
            "Together they are intended to remove hidden assumptions one by one."
        )
        text = replace(text, old, new)

    p80_section = r'''

## 1.14 P80: simplex-coupled continuous-family lower bound

P78 encloses each of the sixteen observed probabilities over a P75 parameter box by exact rational intervals. P80 retains one additional fact that the uncoupled P78 box relaxation discards: every observed law is normalized.

For a parameter box $B$, define

$$
\mathcal R_\Delta(B)
=
\left\{q:\ell_i(B)\le q_i\le u_i(B),\ \sum_i q_i=1\right\}.
$$

Because the true P75 box image satisfies

$$
\mathcal M(B)\subseteq\mathcal R_\Delta(B)
\subseteq
\prod_i[\ell_i(B),u_i(B)],
$$

its exact interval-simplex distance obeys

$$
\boxed{L_{80}(B)\ge L_{78}(B)}
$$

while still remaining a valid lower bound on distance to the true box image. For radius $r$, feasibility requires both coordinatewise overlap and

$$
\sum_i\max(\ell_i,\widehat p_i-r)\le1
\le
\sum_i\min(u_i,\widehat p_i+r).
$$

The coordinatewise threshold is exactly the P78 product-box distance. The two mass thresholds are monotone piecewise-linear functions with rational breakpoints, so P80 computes the coupled distance exactly using `Fraction` arithmetic. A strict P79 handoff remains unchanged: full-law rejection requires the certified P80 lower bound to exceed the P79 sampling-radius upper bound.

![P80 simplex-coupled model separation](docs/figures/p80_simplex_coupled_model_separation.svg)

**P80 theorem figure. Simplex-coupled continuous-model certification.** P80 intersects the P78 exact coordinate intervals with probability normalization, producing a smaller certified superset of the true P75 box image and therefore a lower bound that is never weaker than P78's coordinatewise relaxation.

Direct proof: [Proposition 80](docs/proposition_80_simplex_coupled_model_separation.md). Equation and literature classification: [P80 provenance record](docs/p80_equation_provenance.md). Implementation: [`simplex_coupled_model_separation.py`](src/consciousness_bridge/simplex_coupled_model_separation.py). Tests: [`test_simplex_coupled_model_separation.py`](tests/test_simplex_coupled_model_separation.py) and [`test_p80_figure_geometry.py`](tests/test_p80_figure_geometry.py).
'''
    if "## 1.14 P80: simplex-coupled continuous-family lower bound" not in text:
        text = insert_before(text, "\n---\n\n# 2. From physical dynamics to operational structure", p80_section + "\n")

    old = (
        "P78 then supplies an exact-rational branch-and-bound lower-bound certificate for the continuous P75 latent family. "
        "P79 completes the one-sided numerical handoff by certifying an exact-rational upper envelope for the P77 sampling radius. "
        "The remaining challenges are faster and tighter global optimization, sharper statistical power, and broader dependent-view alternatives."
    )
    new = (
        "P78 then supplies an exact-rational branch-and-bound lower-bound certificate for the continuous P75 latent family. "
        "P79 completes the one-sided numerical handoff by certifying an exact-rational upper envelope for the P77 sampling radius. "
        "P80 tightens the P78 box relaxation by enforcing probability-simplex normalization while preserving exact-rational certification. "
        "The remaining challenges are still tighter global relaxations, sharper statistical power, and broader dependent-view alternatives."
    )
    text = replace(text, old, new)

    p79_status = "| One-sided sampling-radius numerical certificate | **P79 proved with exact-rational logarithm bracketing and integer-certified dyadic square-root enclosure for the P77 radius** |"
    p80_status = "| Simplex-coupled continuous-family certificate | **P80 proved for the P75 family by intersecting exact P78 cell intervals with probability normalization and solving the resulting L-infinity relaxation exactly in rational arithmetic** |"
    if p80_status not in text and p79_status in text:
        text = text.replace(p79_status, p79_status + "\n" + p80_status, 1)

    p79_evidence = "| [P79 equation and provenance record](docs/p79_equation_provenance.md) | Exact-rational logarithm bounds, dyadic square-root enclosure, and the directionally safe P78/P79 rejection handoff |"
    p80_evidence = "| [P80 equation and provenance record](docs/p80_equation_provenance.md) | Interval-simplex relaxation, exact rational feasibility crossings, P80 >= P78 dominance, and the P79 rejection handoff |"
    if p80_evidence not in text and p79_evidence in text:
        text = text.replace(p79_evidence, p79_evidence + "\n" + p80_evidence, 1)

    p79_fals = "| P77/P78 rejection comparison is numerically certified | A P78 model-distance lower bound is strictly larger than the P79 exact-rational sampling-radius upper bound | Comparing rounded decimal approximations without a one-sided enclosure |"
    p80_fals = "| Continuous P75 separation uses the tighter simplex-coupled certificate | A P80 global lower bound exceeds the P79 sampling-radius upper certificate | Treating probability-cell intervals as independent when normalization coupling can strengthen the certified lower bound |"
    if p80_fals not in text and p79_fals in text:
        text = text.replace(p79_fals, p79_fals + "\n" + p80_fals, 1)

    write(path, text)


def update_proposition80() -> None:
    path = "docs/proposition_80_simplex_coupled_model_separation.md"
    text = read(path)
    old = r'''For intervals on the real line, a target total of one is attainable exactly when the sum of the lower endpoints does not exceed one and the sum of the upper endpoints is at least one. Therefore radius $r$ is feasible if and only if

\[
\boxed{
A(r):=\sum_i\max(\ell_i,\widehat p_i-r)\le1
\le
C(r):=\sum_i\min(u_i,\widehat p_i+r).
}
\]

$A(r)$ is continuous, monotone nonincreasing, and piecewise linear. Its breakpoints are the positive rational values $\widehat p_i-\ell_i$. Similarly, $C(r)$ is continuous, monotone nondecreasing, and piecewise linear with positive rational breakpoints $u_i-\widehat p_i$.

Consequently the first radius at which $A(r)\le1$ and the first radius at which $C(r)\ge1$ can each be found exactly by linear interpolation on rational breakpoint intervals. If these radii are $r_A$ and $r_C$, then

\[
\boxed{
L_{80}(B)=\max(r_A,r_C).
}
\]
'''
    new = r'''The clipped interval $I_i(r)$ must first be nonempty for every coordinate. The smallest radius that guarantees this is exactly the uncoupled P78 product-box distance

\[
r_\square
=
\max_i d\!\left(\widehat p_i,[\ell_i,u_i]\right).
\]

Once the clipped coordinate intervals are nonempty, a target total of one is attainable exactly when the sum of their lower endpoints does not exceed one and the sum of their upper endpoints is at least one. Therefore radius $r$ is feasible if and only if

\[
\boxed{
r\ge r_\square,
\qquad
A(r):=\sum_i\max(\ell_i,\widehat p_i-r)\le1
\le
C(r):=\sum_i\min(u_i,\widehat p_i+r).
}
\]

$A(r)$ is continuous, monotone nonincreasing, and piecewise linear. Its breakpoints are the positive rational values $\widehat p_i-\ell_i$. Similarly, $C(r)$ is continuous, monotone nondecreasing, and piecewise linear with positive rational breakpoints $u_i-\widehat p_i$.

Consequently the first radius at which $A(r)\le1$ and the first radius at which $C(r)\ge1$ can each be found exactly by linear interpolation on rational breakpoint intervals. If these radii are $r_A$ and $r_C$, then

\[
\boxed{
L_{80}(B)=\max(r_\square,r_A,r_C).
}
\]
'''
    text = replace(text, old, new)
    write(path, text)


def update_p80_provenance() -> None:
    path = "docs/p80_equation_provenance.md"
    text = read(path)
    text = replace(
        text,
        "| Radius feasibility | $\\sum_i\\max(\\ell_i,\\widehat p_i-r)\\le1\\le\\sum_i\\min(u_i,\\widehat p_i+r)$ | Standard interval-sum feasibility specialized to an $L_\\infty$ ball | [P80 proof](proposition_80_simplex_coupled_model_separation.md) |",
        "| Radius feasibility | $r\\ge r_\\square$ and $\\sum_i\\max(\\ell_i,\\widehat p_i-r)\\le1\\le\\sum_i\\min(u_i,\\widehat p_i+r)$ | Coordinatewise interval overlap plus standard interval-sum feasibility specialized to an $L_\\infty$ ball | [P80 proof](proposition_80_simplex_coupled_model_separation.md) |",
    )
    old = r'''\boxed{
 d_\infty(\widehat p,\mathcal R_\Delta)
=
\inf\left\{r\ge0:
\sum_i\max(\ell_i,\widehat p_i-r)\le1\le
\sum_i\min(u_i,\widehat p_i+r)
\right\}.
}'''
    new = r'''\boxed{
 d_\infty(\widehat p,\mathcal R_\Delta)
=
\inf\left\{r\ge r_\square:
\sum_i\max(\ell_i,\widehat p_i-r)\le1\le
\sum_i\min(u_i,\widehat p_i+r)
\right\},
}'''
    text = replace(text, old, new)
    if "where $r_\\square$ is the exact P78 product-box" not in text:
        marker = "\nBecause the endpoint sums are monotone piecewise-linear functions"
        text = insert_before(
            text,
            marker,
            "\nwhere $r_\\square$ is the exact P78 product-box L-infinity distance needed to guarantee that every clipped coordinate interval is nonempty.\n",
        )
    write(path, text)


def update_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = replace(text, "frontier is **P79**", "frontier is **P80**")
    text = replace(text, "P1 through P79", "P1 through P80")
    text = replace(text, "P71-P79 return", "P71-P80 return")
    text = replace(text, "P71-P79 form", "P71-P80 form")
    text = replace(text, "P71-P79", "P71-P80")

    dependency_old = r'''&\text{P77: full-law confidence regions must be separated from the complete declared model set}\\
&\Downarrow\\
&\text{P78: continuous P75 model distance must be lower-bounded globally and certifiably}
'''
    dependency_new = r'''&\text{P77: full-law confidence regions must be separated from the complete declared model set}\\
&\Downarrow\\
&\text{P78: continuous P75 model distance must be lower-bounded globally and certifiably}\\
&\Downarrow\\
&\text{P79: the sampling-radius side of the rejection gate must have certified numerical direction}\\
&\Downarrow\\
&\text{P80: probability-simplex coupling tightens the continuous-family box certificate}
'''
    text = replace(text, dependency_old, dependency_new)
    text = replace(
        text,
        "The proposition number records development order. It does not imply that P78 depends on P70. P78 depends scientifically on P77 and the P75 continuous target-model family, which descend from P19 and the P71-P76 target-side lineage.",
        "The proposition number records development order. It does not imply that P80 depends on P70. P80 depends scientifically on P78's continuous-family certificate and uses the P79 one-sided sampling-radius handoff; both descend from P77, the P75 continuous target-model family, P19, and the P71-P76 target-side lineage.",
    )

    p80 = r'''

### P80: simplex-coupled continuous P75 separation

P78's exact cell intervals define a Cartesian-product relaxation for each P75 parameter box. P80 intersects those same intervals with the probability-simplex constraint and computes the exact L-infinity distance to the resulting smaller certified superset:

\[
\mathcal R_\Delta(B)
=
\{q:\ell_i(B)\le q_i\le u_i(B),\ \sum_i q_i=1\}.
\]

The set inclusions

\[
\mathcal M(B)\subseteq\mathcal R_\Delta(B)\subseteq\mathcal R_\square(B)
\]

imply

\[
\boxed{L_{80}(B)\ge L_{78}(B)}
\]

while $L_{80}(B)$ remains a valid lower bound on distance to the true P75 box image. Exact radius feasibility combines the P78 coordinatewise threshold $r_\square$ with two rational monotone mass crossings:

\[
\boxed{
r\ge r_\square,
\quad
\sum_i\max(\ell_i,\widehat p_i-r)\le1
\le
\sum_i\min(u_i,\widehat p_i+r).
}
\]

The global active-box minimum is therefore a certified continuous-family lower bound that is never weaker than the P78 bound on the same partition. P79 supplies the independent sampling-radius upper certificate for the strict rejection handoff.

![P80 simplex-coupled model separation](figures/p80_simplex_coupled_model_separation.svg)

Direct proof: [P80](proposition_80_simplex_coupled_model_separation.md). Provenance: [P80 equation record](p80_equation_provenance.md). Implementation: [`simplex_coupled_model_separation.py`](../src/consciousness_bridge/simplex_coupled_model_separation.py). Tests: [`test_simplex_coupled_model_separation.py`](../tests/test_simplex_coupled_model_separation.py).
'''
    if "### P80: simplex-coupled continuous P75 separation" not in text:
        text = insert_before(text, "\n## 3. Complete proposition index", p80 + "\n")

    p79_row = "| [P79](proposition_79_certified_sampling_radius.md) | exact-rational logarithm and dyadic square-root enclosure | one-sided numerical certification of the P77 sampling radius | proved numerical-certification theorem |"
    p80_row = "| [P80](proposition_80_simplex_coupled_model_separation.md) | probability-simplex interval relaxation and exact rational feasibility crossings | tighter certified continuous P75 full-law model separation | proved conditional computational theorem |"
    if p80_row not in text and p79_row in text:
        text = text.replace(p79_row, p79_row + "\n" + p80_row, 1)

    text = replace(text, "After P79, the target side has nine explicit requirements:", "After P80, the target side retains nine explicit requirements:")
    text = replace(
        text,
        "P78 closes the eighth item for the specific P75 four-view binary latent family in L-infinity distance. P79 closes the ninth item for the P77 finite-alphabet sampling radius by exact-rational one-sided numerical enclosure. It supplies an exact-rational multi-affine box certificate and an explicit mesh-gap guarantee. The remaining computational problem is efficiency: stronger pruning, tighter relaxations, or moment-SOS lower bounds may reduce the number of boxes required for a decisive certificate.",
        "P78 closes the eighth item for the specific P75 four-view binary latent family in L-infinity distance, and P80 strengthens that same item by retaining probability-simplex normalization inside each exact interval relaxation. P79 closes the ninth item for the P77 finite-alphabet sampling radius by exact-rational one-sided numerical enclosure. P78 still supplies the explicit mesh-gap guarantee; P80 supplies a never-weaker boxwise lower bound on the same active partition. The remaining computational problem is efficiency: stronger pruning, still tighter convex or semialgebraic relaxations, or moment-SOS lower bounds may further reduce the number of boxes required for a decisive certificate.",
    )
    write(path, text)


def update_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = replace(text, "frontier is **P79**", "frontier is **P80**")
    text = replace(text, "P1 through P79", "P1 through P80")
    text = replace(text, "P71-P79 form", "P71-P80 form")
    text = replace(text, "P71-P79", "P71-P80")

    p79_read = "15. [P79 certified rational sampling-radius envelope](proposition_79_certified_sampling_radius.md) for exact-rational logarithm brackets, integer-certified dyadic square-root enclosure, and the one-sided P78/P79 rejection comparison."
    p80_read = "16. [P80 simplex-coupled continuous P75 separation](proposition_80_simplex_coupled_model_separation.md) for exact probability-simplex interval relaxation, P80 >= P78 dominance, and the strict P80/P79 rejection handoff."
    if p80_read not in text and p79_read in text:
        text = text.replace(p79_read, p79_read + "\n" + p80_read, 1)

    renumber = {
        "15. [P11-P18 and P25-P37": "17. [P11-P18 and P25-P37",
        "16. [P38-P44 quantum": "18. [P38-P44 quantum",
        "17. [P45-P60 adaptive": "19. [P45-P60 adaptive",
        "18. [P61-P70 Calibration": "20. [P61-P70 Calibration",
        "19. [Equation and citation map": "21. [Equation and citation map",
        "20. [P72 equation": "22. [P72 equation",
        "21. [P73 equation": "23. [P73 equation",
        "22. [P74 equation": "24. [P74 equation",
        "23. [P75 equation": "25. [P75 equation",
        "24. [Falsification program": "26. [Falsification program",
        "25. [P78 equation": "27. [P78 equation",
        "26. [Citation guide": "29. [Citation guide",
    }
    for old, new in renumber.items():
        text = replace(text, old, new)
    if "28. [P80 equation and provenance record]" not in text:
        marker = "27. [P78 equation and provenance record](p78_equation_provenance.md) for multi-affine box bounds, global distance certification, and the P77 handoff."
        if marker in text:
            text = insert_after(
                text,
                marker,
                "\n28. [P80 equation and provenance record](p80_equation_provenance.md) for the simplex-coupled interval relaxation, exact feasibility crossings, and P80/P78 dominance.",
            )

    p79_branch = "| Certified sampling-radius envelope | P79 | Supplies an exact-rational upper bound for the P77 sampling radius so the P78 rejection comparison has certified numerical direction | [P79](proposition_79_certified_sampling_radius.md) |"
    p80_branch = "| Simplex-coupled continuous target-model separation | P80 | Tightens each P78 box lower bound by intersecting exact cell intervals with probability normalization while preserving the global lower-bound direction | [P80](proposition_80_simplex_coupled_model_separation.md) |"
    if p80_branch not in text and p79_branch in text:
        text = text.replace(p79_branch, p79_branch + "\n" + p80_branch, 1)

    row79 = "| P79 | [Certified rational sampling-radius envelope](proposition_79_certified_sampling_radius.md) | exact-rational one-sided certification of the P77 sampling radius |"
    row80 = "| P80 | [Simplex-coupled continuous P75 separation](proposition_80_simplex_coupled_model_separation.md) | exact-rational probability-simplex tightening of the P78 continuous-family lower bound |"
    if row80 not in text and row79 in text:
        text = text.replace(row79, row79 + "\n" + row80, 1)
    write(path, text)


def update_detail() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = replace(text, "Complete P1 to P79 chronology", "Complete P1 to P80 chronology")
    p80 = """

## Proposition 80: Simplex-Coupled Box Certificate for Continuous P75 Separation

**P80** strengthens the P78 boxwise lower-bound relaxation without changing the P75 model family. P78 supplies exact coordinate intervals for every observed-law cell over a parameter box. P80 intersects those intervals with the probability-simplex constraint, computes the exact L-infinity distance to that interval-simplex relaxation in rational arithmetic, and proves that the resulting box lower bound is never weaker than P78's coordinatewise bound. The active-box minimum remains a valid global lower bound on distance to the complete continuous P75 family, while P79 continues to supply the one-sided sampling-radius upper certificate used for strict finite-data rejection.

Proof: [Proposition 80](proposition_80_simplex_coupled_model_separation.md). Provenance: [P80 equation record](p80_equation_provenance.md). Figure: [P80 theorem figure](figures/p80_simplex_coupled_model_separation.svg). Implementation: [`simplex_coupled_model_separation.py`](../src/consciousness_bridge/simplex_coupled_model_separation.py). Tests: [`test_simplex_coupled_model_separation.py`](../tests/test_simplex_coupled_model_separation.py).

P80 is a computational tightening of a declared observed-law model test. It does not identify the P75 latent variable with consciousness and does not close the physical-to-experiential bridge.
"""
    if "## Proposition 80: Simplex-Coupled Box Certificate" not in text:
        text += p80
    write(path, text)


def update_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    p80 = r'''

# P80 simplex-coupled continuous-model certificate

| Object | Equation or certificate | Provenance | Direct route |
| --- | --- | --- | --- |
| P78 exact cell ranges | $\ell_i(B)\le q_i(\theta)\le u_i(B)$ | Inherited exact multi-affine coordinate enclosure | [P78](proposition_78_certified_continuous_model_separation.md) |
| P80 relaxation | $\mathcal R_\Delta(B)=\{q:\ell_i\le q_i\le u_i,\sum_iq_i=1\}$ | P78 intervals intersected with the standard probability simplex | [P80](proposition_80_simplex_coupled_model_separation.md) |
| Nested-set dominance | $\mathcal M(B)\subseteq\mathcal R_\Delta(B)\subseteq\mathcal R_\square(B)$ | Exact set inclusion | [P80 provenance](p80_equation_provenance.md) |
| Exact radius gate | $r\ge r_\square$ and $\sum_i\max(\ell_i,\widehat p_i-r)\le1\le\sum_i\min(u_i,\widehat p_i+r)$ | Coordinatewise overlap plus interval-sum feasibility | [P80 proof](proposition_80_simplex_coupled_model_separation.md) |
| Boxwise improvement | $L_{80}(B)\ge L_{78}(B)$ | Distance monotonicity under nested feasible sets | [P80 figure](figures/p80_simplex_coupled_model_separation.svg) |
| Statistical handoff | $L_{80}>\overline\varepsilon_{79}$ | P80 lower-bounds model distance; P79 upper-bounds sampling uncertainty | [P79](proposition_79_certified_sampling_radius.md), [P80](proposition_80_simplex_coupled_model_separation.md) |
| Executable certificate | exact `Fraction` arithmetic | Repository implementation and tests | [`simplex_coupled_model_separation.py`](../src/consciousness_bridge/simplex_coupled_model_separation.py), [`tests`](../tests/test_simplex_coupled_model_separation.py) |

Scientific boundary: P80 tightens one declared continuous-family numerical certificate. It does not identify a latent state with consciousness and does not solve the physical-to-experiential bridge.
'''
    if "# P80 simplex-coupled continuous-model certificate" not in text:
        text += p80
    write(path, text)


def update_citations() -> None:
    path = "CITATION.cff"
    text = read(path)
    text = replace(text, "version: 0.79.0", "version: 0.80.0")
    text = replace(text, "Current documented theorem frontier: P79", "Current documented theorem frontier: P80")
    text = replace(text, "Version 0.79.0.", "Version 0.80.0.")
    if "Proposition 80 tightens" not in text:
        marker = "Proposition 79 adds an exact-rational upper certificate for the P77 sampling radius using rational logarithm bracketing and integer-certified dyadic square-root enclosure, making the final P78/P79 comparison one-sided and rounding-direction safe."
        if marker in text:
            text = text.replace(
                marker,
                marker + " Proposition 80 tightens the continuous P75 separation side by intersecting P78 exact cell intervals with the probability simplex and computing the resulting L-infinity relaxation distance exactly in rational arithmetic; the P80 box bound is never weaker than P78 on the same parameter box.",
                1,
            )
    write(path, text)

    path = "CITATION.bib"
    text = read(path)
    text = replace(text, "version      = {0.79.0}", "version      = {0.80.0}")
    text = replace(text, "Current documented theorem frontier: P79.", "Current documented theorem frontier: P80.")
    write(path, text)

    path = "CITATION.md"
    text = read(path)
    text = replace(text, "0.79.0", "0.80.0")
    text = replace(text, "P79", "P80") if "Current documented theorem frontier: P79" in text else text
    p80 = """

## Proposition 80

For the simplex-coupled continuous-model certificate, cite the repository together with [Proposition 80](docs/proposition_80_simplex_coupled_model_separation.md) and its [equation provenance record](docs/p80_equation_provenance.md). P80 is a computational tightening of the P78 continuous P75 separation certificate and should not be cited as an identification of consciousness.
"""
    if "## Proposition 80" not in text:
        text += p80
    write(path, text)


def update_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    entry = """# 0.80.0 - 2026-09-11

- Added Proposition 80, Simplex-Coupled Box Certificate for Continuous P75 Separation.
- Tightened each P78 parameter-box relaxation by intersecting exact observed-cell intervals with the probability simplex.
- Added an exact-rational L-infinity interval-simplex distance calculation using the P78 coordinatewise threshold plus two monotone piecewise-linear mass crossings.
- Proved the boxwise dominance relation `L80(B) >= L78(B)` while preserving the lower-bound direction required for global P77 rejection.
- Preserved the P79 one-sided sampling-radius upper certificate for the strict P80/P79 rejection handoff.
- Added the P80 proof, provenance record, implementation, theorem figure, geometry guards, navigation, website integration, and release metadata.
- Preserved the scientific boundary that non-rejection is inconclusive and the physical-to-experiential bridge remains open.

"""
    if "# 0.80.0 - 2026-09-11" not in text:
        text = entry + text
    write(path, text)


def update_website() -> None:
    path = "website/index.html"
    text = read(path)
    text = replace(text, "<strong>79</strong><span>proposition-level results</span>", "<strong>80</strong><span>proposition-level results</span>")
    text = replace(text, "<strong>v0.79.0</strong>", "<strong>v0.80.0</strong>")
    text = replace(text, "P71-P79", "P71-P80")
    text = replace(text, "See all 79 results grouped by scientific role", "See all 80 results grouped by scientific role")
    if "p80_simplex_coupled_model_separation.svg" not in text:
        card = '''
      <div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p80_simplex_coupled_model_separation.svg" alt="P80 simplex-coupled model separation certificate"/><div><h3>P80: Simplex-coupled continuous-family certificate</h3><p>P80 intersects the P78 exact probability-cell intervals with normalization. The resulting interval-simplex relaxation still contains every P75 law in the parameter box, but its L-infinity distance is never weaker than the uncoupled P78 lower bound.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_80_simplex_coupled_model_separation.md">Read Proposition 80 -&gt;</a></div></div>
'''
        text = insert_before(text, "\n    <section id=\"falsification\"", card)
    write(path, text)

    path = "website/research-map.html"
    text = read(path)
    text = replace(text, "Seventy-nine results", "Eighty results")
    text = replace(text, "<strong>79</strong><span>proposition-level results</span>", "<strong>80</strong><span>proposition-level results</span>")
    text = replace(text, "P71-P79", "P71-P80")
    p80 = '''
<section><div class="section-head"><p class="eyebrow">IV-J · Tighter continuous-family relaxation</p><h2>P80: Simplex-coupled continuous P75 separation</h2></div><div class="result-grid"><article class="result"><span>P80</span><h3>Normalization-aware certified lower bound</h3><p>P80 intersects P78's exact observed-cell intervals with the probability simplex. The resulting exact-rational L-infinity relaxation distance is a valid global-separation lower bound and is never weaker than the P78 coordinatewise bound on the same parameter partition.</p></article></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p80_simplex_coupled_model_separation.svg" alt="P80 simplex-coupled model separation certificate"/><div><h3>P80 continuous-family tightening</h3><p>Probability normalization couples the observed cells without changing the declared P75 family or the scientific interpretation.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_80_simplex_coupled_model_separation.md">Read Proposition 80 -&gt;</a></div></div></section>

'''
    if "P80: Simplex-coupled continuous P75 separation" not in text:
        text = insert_before(text, "<section><div class=\"section-head\"><p class=\"eyebrow\">V · Operational scale consistency", p80)
    write(path, text)

    path = "website/visual-atlas.html"
    text = read(path)
    if "p80_simplex_coupled_model_separation.svg" not in text:
        card = '''
    <section class="figure-card">
      <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p80_simplex_coupled_model_separation.svg" alt="P80 simplex-coupled model separation certificate" />
      <div>
        <p class="eyebrow">P80</p>
        <h2>Simplex-Coupled Continuous-Family Certificate</h2>
        <p>The figure shows how exact P78 cell intervals are intersected with probability normalization, producing a smaller certified superset whose L-infinity distance is never weaker than the original P78 box lower bound.</p>
        <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_80_simplex_coupled_model_separation.md">Open the P80 proof</a>
      </div>
    </section>

'''
        text = insert_before(text, "</main>", card)
    write(path, text)


def update_tests() -> None:
    path = "tests/test_p80_figure_geometry.py"
    text = read(path)
    text = replace(
        text,
        '"Strongly certified bound" if False else "Stronger certified bound",',
        '"Stronger certified bound",',
    )
    write(path, text)

    path = "tests/test_simplex_coupled_model_separation.py"
    text = read(path)
    text = replace(
        text,
        '"identify a latent state with consciousness",',
        '"does not identify a latent state",\n        "with consciousness",',
    )
    write(path, text)


def cleanup_temporary_files() -> None:
    for relative in (
        "scripts/integrate_p80_publication.py",
        ".github/workflows/p80-publication-integration.yml",
    ):
        target = ROOT / relative
        if target.exists():
            target.unlink()


def main() -> None:
    update_pyproject()
    update_readme()
    update_proposition80()
    update_p80_provenance()
    update_roadmap()
    update_navigation()
    update_detail()
    update_equation_map()
    update_citations()
    update_changelog()
    update_website()
    update_tests()
    cleanup_temporary_files()


if __name__ == "__main__":
    main()
