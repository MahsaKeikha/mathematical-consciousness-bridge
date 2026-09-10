from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


def insert_after_line(text, needle, new_line, label):
    lines = text.splitlines()
    matches = [i for i, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise RuntimeError(f"{label}: expected one line marker, found {len(matches)}")
    i = matches[0]
    lines.insert(i + 1, new_line)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


# README / public paper
path = "README.md"
text = read(path)
text = replace_once(text, "version-0.29.0-2563eb", "version-0.30.0-2563eb", "README badge")
text = replace_once(
    text,
    "**P29** transports the complete P11 response geometry on a fixed intervention-delay grid: every pairwise total-variation response distance contracts under node aggregation, while P18 reconstruction bounds the sup-norm distortion of the entire indexed geometry by twice the uniform reconstruction defect.",
    "**P29** transports the complete P11 response geometry on a fixed intervention-delay grid: every pairwise total-variation response distance contracts under node aggregation, while P18 reconstruction bounds the sup-norm distortion of the entire indexed geometry by twice the uniform reconstruction defect. **P30** then assembles the P27 partition, P28 directed-influence, and P29 response-geometry branches under one shared node quotient, experiment grid, state map, and reconstruction declaration, yielding a simultaneous P11 distortion certificate while proving that zero numerical distortion cannot compensate for failed semantic compatibility.",
    "README abstract P30",
)
text = replace_once(text, "**29 proposition-level results", "**30 proposition-level results", "README record prose")
text = replace_once(text, "P1 through P29 with explicit dependency branches", "P1 through P30 with explicit dependency branches", "README reader roadmap")
text = insert_after_line(
    text,
    "response-geometry node-aggregation theorem | [Proposition 29]",
    "| full P11 scale-compatibility theorem | [Proposition 30](docs/proposition_30_full_p11_scale_compatibility.md) | simultaneous G/A/K transport under one shared scale declaration with a no-semantic-compensation guard |",
    "README P30 navigation",
)
text = insert_after_line(
    text,
    "implementation of P29 | [response_geometry_node_aggregation.py]",
    "| implementation of P30 | [full_p11_scale_compatibility.py](src/consciousness_bridge/full_p11_scale_compatibility.py) | assembly certificate for simultaneous declared P11 scale transport |",
    "README P30 implementation navigation",
)
text = insert_after_line(
    text,
    "**11.5 P29 response geometry under node aggregation**",
    "| **11.6 P30 full P11 scale compatibility** | When can G, A, and K be transported together under one shared scale declaration? |",
    "README paper map P30",
)
text = replace_once(text, "| proposition-level results | **29** |", "| proposition-level results | **30** |", "README proposition count")
text = replace_once(text, "| research-software version | **0.29.0** |", "| research-software version | **0.30.0** |", "README software version")
text = insert_after_line(
    text,
    "| **P29** | Response-geometry transport under node aggregation | complete intervention-delay TV geometry with P18 distortion control | proved |",
    "| **P30** | Full declared P11 scale compatibility | simultaneous response-geometry, directed-influence, and partition transport under one shared scale declaration | proved assembly theorem |",
    "README theorem table P30",
)
p30_section = r'''## 13.8 P30 - full declared P11 scale compatibility

![P30 full declared P11 scale compatibility](docs/figures/p30_full_p11_scale_compatibility.svg)

P30 asks when the three changing-node results can legitimately be combined into one statement about the declared P11 physical signature

\[
\mathfrak C=(V,\mathcal U,\mathcal T,\mathcal G,\mathcal A,\mathcal K).
\]

The theorem requires one shared scale declaration: the same surjective node quotient \(a:V_f\twoheadrightarrow V_c\), the same retained intervention set \(\mathcal U\), the same retained delay set \(\mathcal T\), one compatible aggregate-state map \(C_a\), and one declared reconstruction family or compatible restrictions of it.

Define the three component distortions

\[
D_G=\|\mathcal G_f-\mathcal G_c\|_\infty,
\]

\[
D_A=\|\mathcal A_f-\mathcal A_c\|_\infty,
\]

and

\[
D_K=\sup_{\pi_c}\left|\kappa_f(L_a\pi_c)-\kappa_c(\pi_c)\right|,
\]

where \(L_a\pi_c\) is the P27 saturated lift and the directed-influence supremum is restricted to source comparisons whose semantics satisfy P28.

The declared P11 distortion vector is

\[
\boxed{
\mathbf D_{P11}(a)=(D_G,D_A,D_K).
}
\]

Let \(\rho_G^*\) be the P29 response-family reconstruction defect, \(\rho_A^*\) the P28/P25 target-family defect, and \(\rho_P^*,\rho_\Pi^*\) the P27/P26 response and partition-product reconstruction defects. Define

\[
\boxed{
\varepsilon_{P11}
=
\max\left\{
2\rho_G^*,
2\rho_A^*,
\rho_P^*+\rho_\Pi^*
\right\}.
}
\]

Under the shared compatibility conditions and the hypotheses of the component theorems,

\[
\boxed{
\|\mathbf D_{P11}(a)\|_\infty
\le
\varepsilon_{P11}.
}
\]

Thus all three central P11 components are simultaneously reconstruction-controlled under one auditable scale declaration. If all relevant reconstruction defects vanish, then

\[
\boxed{D_G=D_A=D_K=0.}
\]

P30 also makes a logically separate point that prevents a false scale-invariance conclusion:

\[
\boxed{
D_G=D_A=D_K=0
\not\Rightarrow
\text{valid P11 scale transport if the semantic conditions fail}.
}
\]

A zero numerical difference cannot repair an ambiguous source intervention, a non-descendable partition, a mismatched intervention-delay grid, or component calculations performed under different coarse physical maps.

The exact interpretation boundary is therefore

\[
\boxed{
\text{simultaneous transport of a declared physical signature}
\neq
\text{physical completeness}
\neq
\text{consciousness}.
}
\]

P30 also does not identify node aggregation with genuine physical fusion and does not solve intervention or time quotienting. Those remain separate theorem burdens.

[Read Proposition 30](docs/proposition_30_full_p11_scale_compatibility.md). The [P30 theorem map](docs/figures/p30_full_p11_scale_compatibility.svg), [implementation](src/consciousness_bridge/full_p11_scale_compatibility.py), and [tests](tests/test_full_p11_scale_compatibility.py) expose the complete proof-to-code path.

'''
marker = "---\n\n# 14. Observer-to-bridge handoff"
text = replace_once(text, marker, p30_section + marker, "README P30 section")
write(path, text)


# Theorem roadmap markdown
path = "docs/theorem_roadmap.md"
text = read(path)
text = replace_once(text, "P1 through P29", "P1 through P30", "roadmap heading range")
p30_roadmap = r'''## P30 - full declared P11 scale compatibility

P30 assembles the P27, P28, and P29 changing-node branches only when they refer to one shared scale declaration. Define

\[
\mathbf D_{P11}(a)=(D_G,D_A,D_K)
\]

with response-geometry, directed-influence, and partition distortions. The component theorems imply

\[
D_G\le2\rho_G^*,
\qquad
D_A\le2\rho_A^*,
\qquad
D_K\le\rho_P^*+\rho_\Pi^*.
\]

Hence

\[
\boxed{
\|\mathbf D_{P11}(a)\|_\infty
\le
\max\{2\rho_G^*,2\rho_A^*,\rho_P^*+\rho_\Pi^*\}.
}
\]

The theorem requires compatible partition descent, source-pair descent, a common intervention-delay grid, a common state map, and a common reconstruction declaration. Numerical equality alone cannot replace those semantic conditions.

Direct proof: [Proposition 30](proposition_30_full_p11_scale_compatibility.md). Implementation: [full_p11_scale_compatibility.py](../src/consciousness_bridge/full_p11_scale_compatibility.py). Tests: [test_full_p11_scale_compatibility.py](../tests/test_full_p11_scale_compatibility.py).

'''
marker = "---\n\n# 8. Fundamental physical sufficiency: P19"
text = replace_once(text, marker, p30_roadmap + marker, "roadmap P30 section")
write(path, text)


# Theorem roadmap SVG
path = "docs/figures/theorem_roadmap.svg"
text = read(path)
text = replace_once(text, 'height="3330" viewBox="0 0 1600 3330"', 'height="3560" viewBox="0 0 1600 3560"', "roadmap svg dimensions")
text = replace_once(text, "Theorem roadmap through Proposition 29", "Theorem roadmap through Proposition 30", "roadmap svg title")
text = replace_once(text, 'height="3330" fill="#ffffff"', 'height="3560" fill="#ffffff"', "roadmap svg background")
text = replace_once(text, "Theorem Roadmap - P1 through P29", "Theorem Roadmap - P1 through P30", "roadmap svg visible title")
old_tail = '''  <rect x="95" y="3260" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="3285" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="3308" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Simultaneous P11 assembly, intervention/time quotienting, physical completeness, and experiential formalization remain open.</text>
</svg>'''
new_tail = '''  <rect x="225" y="3260" width="1150" height="190" rx="20" fill="#ecfdf5" stroke="#059669" stroke-width="1.8"/>
  <text x="265" y="3297" class="label">FULL P11 ASSEMBLY · P30</text>
  <text x="265" y="3335" class="head">One shared declaration controls G, A, and K</text>
  <text x="265" y="3369" class="body">Semantic compatibility is required before component bounds can be combined.</text>
  <text x="265" y="3404" class="eq">||DP11||∞ ≤ max{2ρG*,2ρA*,ρP*+ρΠ*}</text>
  <text x="820" y="3404" class="eq">zero distortion ≠ semantic compatibility</text>
  <text x="265" y="3434" class="body">The result is a physical-signature certificate, not a consciousness theorem.</text>

  <rect x="95" y="3490" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="3515" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="3538" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Intervention/time quotienting, physical completeness, experiential formalization, and the bridge theorem remain open.</text>
</svg>'''
text = replace_once(text, old_tail, new_tail, "roadmap svg P30 card")
write(path, text)


# Research navigation
path = "docs/research_navigation.md"
text = read(path)
text = replace_once(text, "from P1 through P29", "from P1 through P30", "navigation range")
text = insert_after_line(
    text,
    "[Proposition 28](proposition_28_intervention_node_aggregation_compatibility.md) for source-label descent",
    "15. [Proposition 29](proposition_29_response_geometry_node_aggregation.md) for complete response-geometry transport on the retained intervention-delay grid.\n16. [Proposition 30](proposition_30_full_p11_scale_compatibility.md) for simultaneous P11 scale compatibility under one shared declaration.",
    "navigation reading order P30",
)
# Remove the pre-existing P29 reading-order line that now follows the inserted block.
text = text.replace("15. [Proposition 29](proposition_29_response_geometry_node_aggregation.md) for complete response-geometry transport on the retained intervention-delay grid.\n", "", 1)
# Renumber later fixed lines conservatively.
for old, new in (("16. [Fundamental Theory", "17. [Fundamental Theory"), ("17. [Stochastic fundamental", "18. [Stochastic fundamental"), ("18. [Falsification program", "19. [Falsification program"), ("19. [Citation and Reference Policy", "20. [Citation and Reference Policy")):
    text = text.replace(old, new, 1)
text = insert_after_line(
    text,
    "| P29 | [Response-geometry node aggregation]",
    "| P30 | [Full declared P11 scale compatibility](proposition_30_full_p11_scale_compatibility.md) | simultaneous G/A/K transport under one shared scale declaration and no-semantic-compensation guard |",
    "navigation proposition index P30",
)
text = insert_after_line(
    text,
    "| [P29 response-geometry node aggregation]",
    "| [P30 full P11 scale compatibility](proposition_30_full_p11_scale_compatibility.md) | simultaneous P11 physical-signature transport under one auditable scale declaration |",
    "navigation fundamental table P30",
)
text = replace_once(
    text,
    "The P29 response-geometry layer is implemented in [response_geometry_node_aggregation.py](../src/consciousness_bridge/response_geometry_node_aggregation.py), tested in [test_response_geometry_node_aggregation.py](../tests/test_response_geometry_node_aggregation.py), and summarized by [p29_response_geometry_node_aggregation.svg](figures/p29_response_geometry_node_aggregation.svg).",
    "The P29 response-geometry layer is implemented in [response_geometry_node_aggregation.py](../src/consciousness_bridge/response_geometry_node_aggregation.py), tested in [test_response_geometry_node_aggregation.py](../tests/test_response_geometry_node_aggregation.py), and summarized by [p29_response_geometry_node_aggregation.svg](figures/p29_response_geometry_node_aggregation.svg). The P30 assembly layer is implemented in [full_p11_scale_compatibility.py](../src/consciousness_bridge/full_p11_scale_compatibility.py), tested in [test_full_p11_scale_compatibility.py](../tests/test_full_p11_scale_compatibility.py), and summarized by [p30_full_p11_scale_compatibility.svg](figures/p30_full_p11_scale_compatibility.svg).",
    "navigation implementation P30",
)
write(path, text)


# Equation and citation map
path = "docs/equation_and_citation_map.md"
text = read(path)
p30_eq = r'''# 23. P30 full declared P11 scale compatibility

| Equation / statement | Role | Provenance | Audit path |
| --- | --- | --- | --- |
| \(\mathbf D_{P11}(a)=(D_G,D_A,D_K)\) | combines response-geometry, directed-influence, and partition distortions | repository definition | [P30](proposition_30_full_p11_scale_compatibility.md) |
| \(D_G\le2\rho_G^*\) | complete response-geometry distortion control | P29 + P18 | [P29](proposition_29_response_geometry_node_aggregation.md); [P30](proposition_30_full_p11_scale_compatibility.md) |
| \(D_A\le2\rho_A^*\) | compatible directed-influence distortion control | P28/P25 + P18 | [P28](proposition_28_intervention_node_aggregation_compatibility.md); [P30](proposition_30_full_p11_scale_compatibility.md) |
| \(D_K\le\rho_P^*+\rho_\Pi^*\) | descendable partition-irreducibility distortion control | P27/P26 + P18 | [P27](proposition_27_partition_lattice_node_aggregation.md); [P30](proposition_30_full_p11_scale_compatibility.md) |
| \(\|\mathbf D_{P11}\|_\infty\le\max\{2\rho_G^*,2\rho_A^*,\rho_P^*+\rho_\Pi^*\}\) | simultaneous declared P11 scale certificate | proved assembly theorem | [P30](proposition_30_full_p11_scale_compatibility.md) |
| zero component distortion does not replace semantic compatibility | prevents incomparable scale constructions from being declared equivalent | repository no-semantic-compensation result | [P30](proposition_30_full_p11_scale_compatibility.md) |

P30 is a theorem about simultaneous transport of the declared P11 physical candidate. It does not establish consciousness, physical completeness, genuine node fusion, intervention quotienting, or time quotienting.

---

'''
marker = "# 23. Candidate consciousness-theory feature families"
text = replace_once(text, marker, p30_eq + "# 24. Candidate consciousness-theory feature families", "equation map P30")
text = replace_once(text, "# 24. Citation discipline", "# 25. Citation discipline", "equation map renumber citation")
write(path, text)


# Main-page guards
path = "tests/test_main_page_visual_paper.py"
text = read(path)
text = insert_after_line(text, '"p29_response_geometry_node_aggregation.svg",', '    "p30_full_p11_scale_compatibility.svg",', "main-page figure guard P30")
text = replace_once(text, "for index in range(1, 30):", "for index in range(1, 31):", "main-page proposition range")
write(path, text)

path = "tests/test_visual_and_terminology_quality.py"
text = read(path)
text = insert_after_line(text, '"p29_response_geometry_node_aggregation.svg",', '    "p30_full_p11_scale_compatibility.svg",', "visual figure guard P30")
write(path, text)


# Package metadata
path = "pyproject.toml"
text = read(path)
text = replace_once(text, 'version = "0.29.0"', 'version = "0.30.0"', "pyproject version")
text = replace_once(text, "response-geometry node aggregation, robust experiment design", "response-geometry node aggregation, full P11 scale compatibility, robust experiment design", "pyproject description")
write(path, text)

path = "CITATION.cff"
text = read(path)
text = replace_once(text, "version: 0.29.0", "version: 0.30.0", "citation version")
text = replace_once(text, "response-geometry node aggregation, robust experiment design", "response-geometry node aggregation, full P11 scale compatibility, robust experiment design", "citation abstract")
write(path, text)


# Changelog
path = "CHANGELOG.md"
text = read(path)
entry = r'''## 0.30.0 - 2026-09-09

### Proposition 30 - full declared P11 scale compatibility

- Assembled the P27 partition, P28 directed-influence, and P29 response-geometry scale branches under one shared node quotient and experiment declaration.
- Defined the full declared P11 distortion vector \(\mathbf D_{P11}=(D_G,D_A,D_K)\).
- Required partition compatibility, source-pair compatibility, a common intervention-delay grid, a common state map, and a common reconstruction declaration before assembly is certified.
- Proved \(\|\mathbf D_{P11}\|_\infty\le\max\{2\rho_G^*,2\rho_A^*,\rho_P^*+\rho_\Pi^*\}\).
- Proved exact simultaneous preservation when all relevant reconstruction defects vanish and the semantic compatibility conditions hold.
- Added the no-semantic-compensation guard: zero numerical component distortion does not certify valid transport when the compared structures are semantically incompatible.
- Added executable assembly certification, nine regression tests, a publication theorem map, main-paper integration, roadmap, navigation, provenance, release guards, and synchronized 0.30.0 metadata.
- Preserved the boundary that intervention/time quotienting, physical completeness, genuine physical fusion, and experiential interpretation remain open.

'''
marker = "## 0.29.0 - 2026-09-09"
text = replace_once(text, marker, entry + marker, "changelog P30")
write(path, text)
