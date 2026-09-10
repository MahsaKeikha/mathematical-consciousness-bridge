from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


# README
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.30.0-2563eb", "version-0.31.0-2563eb", "README version")
text = replace_once(
    text,
    "**P30** then assembles the P27 partition, P28 directed-influence, and P29 response-geometry branches under one shared node quotient, experiment grid, state map, and reconstruction declaration, yielding a simultaneous P11 distortion certificate while proving that zero numerical distortion cannot compensate for failed semantic compatibility.",
    "**P30** then assembles the P27 partition, P28 directed-influence, and P29 response-geometry branches under one shared node quotient, experiment grid, state map, and reconstruction declaration, yielding a simultaneous P11 distortion certificate while proving that zero numerical distortion cannot compensate for failed semantic compatibility. **P31** formalizes intervention-label quotienting itself: a many-to-one intervention map defines a unique coarse response law exactly when every retained response law is constant on each intervention fiber, and the quotient ambiguity defect quantifies representative dependence when exact descent fails.",
    "README abstract P31",
)
text = replace_once(text, "**30 proposition-level results", "**31 proposition-level results", "README research record")
text = replace_once(text, "P1 through P30 with explicit dependency branches", "P1 through P31 with explicit dependency branches", "README navigation range")
text = replace_once(
    text,
    "| full P11 scale-compatibility theorem | [Proposition 30](docs/proposition_30_full_p11_scale_compatibility.md) | simultaneous G/A/K transport under one shared scale declaration with a no-semantic-compensation guard |",
    "| full P11 scale-compatibility theorem | [Proposition 30](docs/proposition_30_full_p11_scale_compatibility.md) | simultaneous G/A/K transport under one shared scale declaration with a no-semantic-compensation guard |\n| intervention-quotient theorem | [Proposition 31](docs/proposition_31_intervention_quotient_compatibility.md) | exact intervention-label descent, quotient ambiguity defect, and representative-stability bound |",
    "README navigation P31",
)
text = replace_once(
    text,
    "| **11.6 P30 full P11 scale compatibility** | When can G, A, and K be transported together under one shared scale declaration? |",
    "| **11.6 P30 full P11 scale compatibility** | When can G, A, and K be transported together under one shared scale declaration? |\n| **11.7 P31 intervention quotient compatibility** | When may several fine intervention labels be represented by one coarse intervention without representative-dependent response laws? |",
    "README paper map P31",
)
text = replace_once(text, "# 7. Theorem roadmap - P1 through P29", "# 7. Theorem roadmap - P1 through P31", "README theorem heading")
text = replace_once(
    text,
    "| **P30** | simultaneous response-geometry, directed-influence, and partition transport requires one shared scale declaration; zero numerical distortion cannot replace semantic compatibility | proved assembly theorem | [P30](docs/proposition_30_full_p11_scale_compatibility.md) |",
    "| **P30** | simultaneous response-geometry, directed-influence, and partition transport requires one shared scale declaration; zero numerical distortion cannot replace semantic compatibility | proved assembly theorem | [P30](docs/proposition_30_full_p11_scale_compatibility.md) |\n| **P31** | an intervention quotient descends exactly iff response laws are constant on every intervention fiber; nonzero quotient ambiguity bounds representative-dependent coarse geometry | proved operational quotient theorem | [P31](docs/proposition_31_intervention_quotient_compatibility.md) |",
    "README theorem table P31",
)
text = replace_once(
    text,
    "| implementation of P30 | [full_p11_scale_compatibility.py](src/consciousness_bridge/full_p11_scale_compatibility.py) | assembly certificate for simultaneous declared P11 scale transport |",
    "| implementation of P30 | [full_p11_scale_compatibility.py](src/consciousness_bridge/full_p11_scale_compatibility.py) | assembly certificate for simultaneous declared P11 scale transport |\n| implementation of P31 | [intervention_quotient_compatibility.py](src/consciousness_bridge/intervention_quotient_compatibility.py) | exact intervention-label quotient audit and ambiguity/stability certificate |",
    "README implementation P31",
)
p31_section = r'''## 13.9 P31 - intervention-quotient compatibility

![P31 intervention-quotient compatibility](docs/figures/p31_intervention_quotient_compatibility.svg)

P30 deliberately keeps the intervention set fixed. P31 addresses the next scale operation directly: when may several fine intervention labels be identified as one coarse intervention label without making the response law depend on which fine representative was chosen?

Let

\[
\boxed{
b:\mathcal U_f\twoheadrightarrow\mathcal U_c
}
\]

be a declared surjective intervention-label quotient. Assume all compared responses already live on one common physical response space, for example after any independently declared node/state map,

\[
\overline P^{u,\tau}=(C_a)_\#P^{u,\tau}.
\]

A unique coarse response table \(Q^{c,\tau}\) exists exactly when the fine response family is constant on every fiber of \(b\):

\[
\boxed{
b(u)=b(v)
\Longrightarrow
\overline P^{u,\tau}=\overline P^{v,\tau}
\quad\forall\tau\in\mathcal T.}
\]

Equivalently,

\[
\boxed{
\overline P^{u,\tau}=Q^{b(u),\tau}
\quad\forall u,\tau
}
\]

for one uniquely defined descended table. This is an exact quotient criterion, not a relabeling convention.

When exact descent fails, P31 defines the intervention-quotient ambiguity defect

\[
\boxed{
\eta_b
=
\sup_{\tau\in\mathcal T}
\sup_{u,v:\,b(u)=b(v)}
\left\|
\overline P^{u,\tau}-\overline P^{v,\tau}
\right\|_{\mathrm{TV}}.
}
\]

Then

\[
\boxed{
\eta_b=0
\iff
\text{exact intervention-quotient descent}.
}
\]

If a coarse table is nevertheless built by selecting one representative \(s(c)\in b^{-1}(c)\), with

\[
Q_s^{c,\tau}=\overline P^{s(c),\tau},
\]

then any two selections satisfy

\[
\boxed{
\sup_{c,\tau}
\|Q_s^{c,\tau}-Q_{s'}^{c,\tau}\|_{\mathrm{TV}}
\le\eta_b.
}
\]

The induced coarse response geometry therefore obeys

\[
\boxed{
\sup_{c,d,\tau}
|G_s(c,d,\tau)-G_{s'}(c,d,\tau)|
\le2\eta_b.
}
\]

Thus a nonzero \(\eta_b\) is a quantitative warning that the proposed coarse intervention geometry is representative dependent. It measures hidden response variation inside the intervention quotient fibers.

The scientific interpretation remains narrow:

\[
\boxed{
\text{same coarse intervention label}
\neq
\text{same physical actuator}
\neq
\text{simultaneous intervention}.
}
\]

A small \(\eta_b\) says only that the declared response experiment is relatively insensitive to which fine intervention in a quotient fiber was used. It does not prove mechanistic or ontological identity.

P31 therefore supplies the missing theorem needed before extending P30 from a fixed intervention set to a changing intervention set. The next unresolved scale operation is a delay/time quotient: when may several fine delays be represented by one coarse temporal label without representative-dependent response structure?

[Read Proposition 31](docs/proposition_31_intervention_quotient_compatibility.md). The [P31 theorem map](docs/figures/p31_intervention_quotient_compatibility.svg), [implementation](src/consciousness_bridge/intervention_quotient_compatibility.py), and [tests](tests/test_intervention_quotient_compatibility.py) expose the complete proof-to-code path.

'''
text = replace_once(
    text,
    "[Read Proposition 30](docs/proposition_30_full_p11_scale_compatibility.md). The [P30 theorem map](docs/figures/p30_full_p11_scale_compatibility.svg), [implementation](src/consciousness_bridge/full_p11_scale_compatibility.py), and [tests](tests/test_full_p11_scale_compatibility.py) expose the complete proof-to-code path.\n\n---\n\n# 14. Observer-to-bridge handoff",
    "[Read Proposition 30](docs/proposition_30_full_p11_scale_compatibility.md). The [P30 theorem map](docs/figures/p30_full_p11_scale_compatibility.svg), [implementation](src/consciousness_bridge/full_p11_scale_compatibility.py), and [tests](tests/test_full_p11_scale_compatibility.py) expose the complete proof-to-code path.\n\n" + p31_section + "---\n\n# 14. Observer-to-bridge handoff",
    "README P31 section",
)
path.write_text(text, encoding="utf-8")

# theorem roadmap markdown
path = Path("docs/theorem_roadmap.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "![P1-P30 theorem roadmap]", "![P1-P31 theorem roadmap]", "roadmap image alt")
text = replace_once(
    text,
    "| [P30](proposition_30_full_p11_scale_compatibility.md) | assembly of P27-P29 under one scale declaration | simultaneous declared P11 physical-signature transport with a no-semantic-compensation guard | proved assembly theorem |",
    "| [P30](proposition_30_full_p11_scale_compatibility.md) | assembly of P27-P29 under one scale declaration | simultaneous declared P11 physical-signature transport with a no-semantic-compensation guard | proved assembly theorem |\n| [P31](proposition_31_intervention_quotient_compatibility.md) | quotient factorization of intervention-conditioned response laws | exact criterion for changing the intervention set plus a representative-ambiguity budget | proved operational quotient theorem |",
    "roadmap index P31",
)
p31_roadmap = r'''## P31 - intervention-quotient compatibility

Let \(b:\mathcal U_f\twoheadrightarrow\mathcal U_c\) be a declared many-to-one map on intervention labels after the physical response space has been fixed. P31 proves that a unique coarse response table exists if and only if

\[
\boxed{
b(u)=b(v)\Longrightarrow \overline P^{u,\tau}=\overline P^{v,\tau}\quad\forall\tau.}
\]

Define

\[
\boxed{
\eta_b=\sup_{\tau}\sup_{b(u)=b(v)}
\|\overline P^{u,\tau}-\overline P^{v,\tau}\|_{\mathrm{TV}}.
}
\]

Then \(\eta_b=0\) is equivalent to exact quotient descent. If representatives are used despite nonzero ambiguity, P31 bounds the resulting response-table and geometry dependence by

\[
\boxed{
\sup_{c,\tau}\|Q_s^{c,\tau}-Q_{s'}^{c,\tau}\|_{\mathrm{TV}}\le\eta_b,
\qquad
\sup_{c,d,\tau}|G_s-G_{s'}|\le2\eta_b.
}
\]

The quotient is operational and experiment relative. It does not identify distinct physical actuators or define a simultaneous perturbation.

Direct proof: [Proposition 31](proposition_31_intervention_quotient_compatibility.md). Implementation: [intervention_quotient_compatibility.py](../src/consciousness_bridge/intervention_quotient_compatibility.py). Tests: [test_intervention_quotient_compatibility.py](../tests/test_intervention_quotient_compatibility.py).

'''
text = replace_once(
    text,
    "Direct proof: [Proposition 30](proposition_30_full_p11_scale_compatibility.md). Implementation: [full_p11_scale_compatibility.py](../src/consciousness_bridge/full_p11_scale_compatibility.py). Tests: [test_full_p11_scale_compatibility.py](../tests/test_full_p11_scale_compatibility.py).\n\n---\n\n# 8. Fundamental physical sufficiency: P19",
    "Direct proof: [Proposition 30](proposition_30_full_p11_scale_compatibility.md). Implementation: [full_p11_scale_compatibility.py](../src/consciousness_bridge/full_p11_scale_compatibility.py). Tests: [test_full_p11_scale_compatibility.py](../tests/test_full_p11_scale_compatibility.py).\n\n" + p31_roadmap + "---\n\n# 8. Fundamental physical sufficiency: P19",
    "roadmap P31 section",
)
path.write_text(text, encoding="utf-8")

# research navigation
path = Path("docs/research_navigation.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "from P1 through P30", "from P1 through P31", "navigation range")
text = replace_once(
    text,
    "16. [Proposition 30](proposition_30_full_p11_scale_compatibility.md) for simultaneous P11 scale compatibility under one shared declaration.\n17. [Fundamental Theory to Consciousness program]",
    "16. [Proposition 30](proposition_30_full_p11_scale_compatibility.md) for simultaneous P11 scale compatibility under one shared declaration.\n17. [Proposition 31](proposition_31_intervention_quotient_compatibility.md) for exact intervention-label quotienting and representative-ambiguity control.\n18. [Fundamental Theory to Consciousness program]",
    "navigation reading order P31",
)
# renumber later reading-order entries
for old, new in [("18. [Stochastic fundamental bridge]", "19. [Stochastic fundamental bridge]"), ("19. [Falsification program]", "20. [Falsification program]"), ("20. [Citation and Reference Policy]", "21. [Citation and Reference Policy]")]:
    text = replace_once(text, old, new, f"navigation renumber {old[:2]}")
text = replace_once(
    text,
    "| P30 | [Full declared P11 scale compatibility](proposition_30_full_p11_scale_compatibility.md) | simultaneous G/A/K transport under one shared scale declaration and no-semantic-compensation guard |",
    "| P30 | [Full declared P11 scale compatibility](proposition_30_full_p11_scale_compatibility.md) | simultaneous G/A/K transport under one shared scale declaration and no-semantic-compensation guard |\n| P31 | [Intervention-quotient compatibility](proposition_31_intervention_quotient_compatibility.md) | exact intervention-label descent and quantitative representative ambiguity |",
    "navigation proposition index P31",
)
text = replace_once(
    text,
    "| [P30 full P11 scale compatibility](proposition_30_full_p11_scale_compatibility.md) | simultaneous P11 physical-signature transport under one auditable scale declaration |",
    "| [P30 full P11 scale compatibility](proposition_30_full_p11_scale_compatibility.md) | simultaneous P11 physical-signature transport under one auditable scale declaration |\n| [P31 intervention-quotient compatibility](proposition_31_intervention_quotient_compatibility.md) | exact operational intervention quotient and representative-stability bounds |",
    "navigation fundamental table P31",
)
text = replace_once(
    text,
    "The P30 assembly layer is implemented in [full_p11_scale_compatibility.py](../src/consciousness_bridge/full_p11_scale_compatibility.py), tested in [test_full_p11_scale_compatibility.py](../tests/test_full_p11_scale_compatibility.py), and summarized by [p30_full_p11_scale_compatibility.svg](figures/p30_full_p11_scale_compatibility.svg).",
    "The P30 assembly layer is implemented in [full_p11_scale_compatibility.py](../src/consciousness_bridge/full_p11_scale_compatibility.py), tested in [test_full_p11_scale_compatibility.py](../tests/test_full_p11_scale_compatibility.py), and summarized by [p30_full_p11_scale_compatibility.svg](figures/p30_full_p11_scale_compatibility.svg). The P31 intervention-quotient layer is implemented in [intervention_quotient_compatibility.py](../src/consciousness_bridge/intervention_quotient_compatibility.py), tested in [test_intervention_quotient_compatibility.py](../tests/test_intervention_quotient_compatibility.py), and summarized by [p31_intervention_quotient_compatibility.svg](figures/p31_intervention_quotient_compatibility.svg).",
    "navigation reproducibility P31",
)
path.write_text(text, encoding="utf-8")

# equation and citation map
path = Path("docs/equation_and_citation_map.md")
text = path.read_text(encoding="utf-8")
p31_eq = r'''# 25. P31 intervention-quotient compatibility

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(b:\mathcal U_f\twoheadrightarrow\mathcal U_c\) | declared surjective quotient of operational intervention labels | repository definition | [P31](proposition_31_intervention_quotient_compatibility.md) |
| \(b(u)=b(v)\Rightarrow\overline P^{u,\tau}=\overline P^{v,\tau}\;\forall\tau\) | exact fiber-constancy condition | necessary and sufficient for unique response-law descent | [P31](proposition_31_intervention_quotient_compatibility.md) |
| \(\eta_b=\sup_\tau\sup_{b(u)=b(v)}\|\overline P^{u,\tau}-\overline P^{v,\tau}\|_{\mathrm{TV}}\) | operational quotient ambiguity defect | repository definition | [P31](proposition_31_intervention_quotient_compatibility.md) |
| \(\eta_b=0\iff\) exact intervention-quotient descent | exact quotient certificate | proved | [P31](proposition_31_intervention_quotient_compatibility.md) |
| \(\sup_{c,\tau}\|Q_s^{c,\tau}-Q_{s'}^{c,\tau}\|_{\mathrm{TV}}\le\eta_b\) | representative-selection stability | proved | [P31](proposition_31_intervention_quotient_compatibility.md) |
| \(\sup_{c,d,\tau}|G_s-G_{s'}|\le2\eta_b\) | induced coarse response-geometry ambiguity | proved by reverse triangle inequality | [P31](proposition_31_intervention_quotient_compatibility.md) |
| same coarse intervention label \(\ne\) same physical actuator | prevents operational quotienting from being overinterpreted as mechanism identity | interpretation boundary | [P31](proposition_31_intervention_quotient_compatibility.md) |

P31 changes intervention labels only after a common response space is declared. It does not establish physical actuator identity, simultaneity, consciousness, or physical completeness. Delay/time quotienting remains a separate theorem burden.

---

'''
text = replace_once(text, "# 25. Candidate consciousness-theory feature families", p31_eq + "# 26. Candidate consciousness-theory feature families", "equation map P31")
text = replace_once(text, "# 26. Citation discipline", "# 27. Citation discipline", "equation map citation renumber")
path.write_text(text, encoding="utf-8")

# metadata
path = Path("pyproject.toml")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version = "0.30.0"', 'version = "0.31.0"', "pyproject version")
text = replace_once(text, "response-geometry node aggregation, full P11 scale compatibility, recoverability", "response-geometry node aggregation, full P11 scale compatibility, intervention-quotient compatibility, recoverability", "pyproject description")
path.write_text(text, encoding="utf-8")

path = Path("CITATION.cff")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version: 0.30.0", "version: 0.31.0", "citation version")
text = replace_once(text, "response-geometry node aggregation, full P11 scale compatibility, robust experiment design", "response-geometry node aggregation, full P11 scale compatibility, intervention-quotient compatibility, robust experiment design", "citation abstract")
path.write_text(text, encoding="utf-8")

# changelog
path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
entry = r'''## 0.31.0 - 2026-09-09

### Proposition 31 - intervention-quotient compatibility

- Introduced a declared surjective intervention-label quotient \(b:\mathcal U_f\twoheadrightarrow\mathcal U_c\) after the physical response space has been fixed.
- Proved that a unique coarse response table exists if and only if all fine response laws are constant on every quotient fiber at every retained delay.
- Defined the intervention-quotient ambiguity defect \(\eta_b\) as the worst total-variation separation between response laws assigned the same coarse intervention label.
- Proved \(\eta_b=0\) if and only if exact response-law descent holds.
- Proved representative-selection stability \(\sup_{c,\tau}\|Q_s^{c,\tau}-Q_{s'}^{c,\tau}\|_{\mathrm{TV}}\le\eta_b\).
- Proved the induced response-geometry ambiguity bound \(\sup_{c,d,\tau}|G_s-G_{s'}|\le2\eta_b\).
- Explicitly separated operational intervention quotienting from physical actuator identity and simultaneous intervention.
- Added executable mathematics, nine dedicated regression tests, a publication theorem map, main-paper integration, theorem-roadmap integration, navigation, equation provenance, release guards, and synchronized 0.31.0 metadata.
- Preserved delay/time quotienting, physical completeness, genuine physical fusion, and experiential interpretation as separate open theorem burdens.

'''
text = replace_once(text, "## 0.30.0 - 2026-09-09", entry + "## 0.30.0 - 2026-09-09", "changelog P31")
path.write_text(text, encoding="utf-8")

# main page release guards
path = Path("tests/test_main_page_visual_paper.py")
text = path.read_text(encoding="utf-8")
text = replace_once(text, '    "p30_full_p11_scale_compatibility.svg",', '    "p30_full_p11_scale_compatibility.svg",\n    "p31_intervention_quotient_compatibility.svg",', "main page figure guard")
text = replace_once(text, "for index in range(1, 31):", "for index in range(1, 32):", "main page proposition guard")
path.write_text(text, encoding="utf-8")

# global SVG roadmap
path = Path("docs/figures/theorem_roadmap.svg")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'height="3560" viewBox="0 0 1600 3560"', 'height="3800" viewBox="0 0 1600 3800"', "SVG size")
text = replace_once(text, "through Proposition 30", "through Proposition 31", "SVG title")
text = replace_once(text, "Theorem Roadmap - P1 through P30", "Theorem Roadmap - P1 through P31", "SVG heading")
old_frontier = '''  <rect x="95" y="3490" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="3515" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="3538" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Intervention/time quotienting, physical completeness, experiential formalization, and the bridge theorem remain open.</text>'''
new_frontier = '''  <rect x="225" y="3490" width="1150" height="190" rx="20" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="265" y="3527" class="label">INTERVENTION QUOTIENT · P31</text>
  <text x="265" y="3565" class="head">Coarse interventions require fiberwise response agreement</text>
  <text x="265" y="3599" class="body">Merging labels is valid only when retained response laws descend through the quotient.</text>
  <text x="265" y="3634" class="eq">ηb = supτ supb(u)=b(v) ||P̄u,τ−P̄v,τ||TV</text>
  <text x="900" y="3634" class="eq">ηb=0 ⇔ exact descent</text>
  <text x="265" y="3664" class="body">Representative-dependent geometry is bounded by 2ηb.</text>

  <rect x="95" y="3720" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="3745" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="3768" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Delay/time quotienting, physical completeness, experiential formalization, and the bridge theorem remain open.</text>'''
text = replace_once(text, old_frontier, new_frontier, "SVG P31 card")
path.write_text(text, encoding="utf-8")
