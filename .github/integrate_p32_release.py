from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


# README
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.31.0-2563eb", "version-0.32.0-2563eb", "README version badge")
text = replace_once(
    text,
    "**P31** formalizes intervention-label quotienting itself: a many-to-one intervention map defines a unique coarse response law exactly when every retained response law is constant on each intervention fiber, and the quotient ambiguity defect quantifies representative dependence when exact descent fails.",
    "**P31** formalizes intervention-label quotienting itself: a many-to-one intervention map defines a unique coarse response law exactly when every retained response law is constant on each intervention fiber, and the quotient ambiguity defect quantifies representative dependence when exact descent fails. **P32** proves the temporal analogue: a delay quotient defines a unique coarse response table exactly when the retained response laws are constant on each delay fiber, with a separate tolerance-relative certificate that is never relabeled as exact equality.",
    "README abstract P32",
)
text = replace_once(text, "**31 proposition-level results", "**32 proposition-level results", "README public record count")
text = replace_once(text, "P1 through P31 with explicit dependency branches", "P1 through P32 with explicit dependency branches", "README navigation range")
text = replace_once(
    text,
    "| intervention-quotient theorem | [Proposition 31](docs/proposition_31_intervention_quotient_compatibility.md) | exact intervention-label descent, quotient ambiguity defect, and representative-stability bound |",
    "| intervention-quotient theorem | [Proposition 31](docs/proposition_31_intervention_quotient_compatibility.md) | exact intervention-label descent, quotient ambiguity defect, and representative-stability bound |\n| delay-quotient theorem | [Proposition 32](docs/proposition_32_delay_quotient_compatibility.md) | exact delay-label descent, temporal ambiguity defect, and representative-stability bound |",
    "README navigation P32",
)
text = replace_once(
    text,
    "| implementation of P31 | [intervention_quotient_compatibility.py](src/consciousness_bridge/intervention_quotient_compatibility.py) | exact intervention-label quotient audit and ambiguity/stability certificate |",
    "| implementation of P31 | [intervention_quotient_compatibility.py](src/consciousness_bridge/intervention_quotient_compatibility.py) | exact intervention-label quotient audit and ambiguity/stability certificate |\n| implementation of P32 | [delay_quotient_compatibility.py](src/consciousness_bridge/delay_quotient_compatibility.py) | exact delay-label quotient audit with distinct tolerance-relative certification |",
    "README implementation P32",
)
text = replace_once(
    text,
    "| **11.7 P31 intervention quotient compatibility** | When may several fine intervention labels be represented by one coarse intervention without representative-dependent response laws? |",
    "| **11.7 P31 intervention quotient compatibility** | When may several fine intervention labels be represented by one coarse intervention without representative-dependent response laws? |\n| **11.8 P32 delay quotient compatibility** | When may several fine delays be represented by one coarse temporal label without representative-dependent response laws? |",
    "README paper map P32",
)
# Repair the stale glance record left by the previous release while advancing to P32.
text = replace_once(text, "| proposition-level results | **30** |", "| proposition-level results | **32** |", "README glance proposition count")
text = replace_once(text, "| research-software version | **0.30.0** |", "| research-software version | **0.32.0** |", "README glance version")
# The heading still carries a historical P29 label even though later rows are already present.
text = replace_once(text, "# 7. Theorem roadmap - P1 through P31", "# 7. Theorem roadmap - P1 through P32", "README theorem heading")
text = replace_once(
    text,
    "| **P31** | an intervention quotient descends exactly iff response laws are constant on every intervention fiber; nonzero quotient ambiguity bounds representative-dependent coarse geometry | proved operational quotient theorem | [P31](docs/proposition_31_intervention_quotient_compatibility.md) |",
    "| **P31** | an intervention quotient descends exactly iff response laws are constant on every intervention fiber; nonzero quotient ambiguity bounds representative-dependent coarse geometry | proved operational quotient theorem | [P31](docs/proposition_31_intervention_quotient_compatibility.md) |\n| **P32** | a delay quotient descends exactly iff response laws are constant on every delay fiber; temporal ambiguity bounds representative-dependent coarse response geometry | proved operational quotient theorem | [P32](docs/proposition_32_delay_quotient_compatibility.md) |",
    "README theorem table P32",
)
p32_section = r'''## 13.10 P32 - delay-quotient compatibility

![P32 delay-quotient compatibility](docs/figures/p32_delay_quotient_compatibility.svg)

P31 changes the intervention labels while keeping delays fixed. P32 closes the complementary temporal loophole: when may several fine delay labels be represented by one coarse temporal label without making the response law depend on which fine delay was silently chosen?

Let

\[
\boxed{
q:\mathcal T_f\twoheadrightarrow\mathcal T_c
}
\]

be a declared surjective delay-label quotient, with a fixed intervention set \(\mathcal U\). All response laws must already live on one common physical response space.

There exists a unique coarse-delay response table \(Q^{u,t}\) satisfying

\[
P^{u,\tau}=Q^{u,q(\tau)}
\quad\forall u,\tau
\]

if and only if

\[
\boxed{
q(\tau)=q(\tau')
\Longrightarrow
P^{u,\tau}=P^{u,\tau'}
\quad\forall u\in\mathcal U.
}
\]

Define the delay-quotient ambiguity defect

\[
\boxed{
\eta_q
=
\sup_{u\in\mathcal U}
\sup_{\tau,\tau':q(\tau)=q(\tau')}
\|P^{u,\tau}-P^{u,\tau'}\|_{\mathrm{TV}}.
}
\]

Then

\[
\boxed{
\eta_q=0
\iff
\text{exact delay-quotient descent}.
}
\]

If a representative \(s(t)\in q^{-1}(t)\) is chosen for each coarse delay and

\[
Q_s^{u,t}=P^{u,s(t)},
\]

then any two representative choices satisfy

\[
\boxed{
\sup_{u,t}
\|Q_s^{u,t}-Q_{s'}^{u,t}\|_{\mathrm{TV}}
\le\eta_q.
}
\]

For the induced P11 response geometry,

\[
G_s(u,v,t)=\|Q_s^{u,t}-Q_s^{v,t}\|_{\mathrm{TV}},
\]

P32 proves

\[
\boxed{
\sup_{u,v,t}
|G_s(u,v,t)-G_{s'}(u,v,t)|
\le2\eta_q.
}
\]

The implementation deliberately distinguishes exact and approximate certification. `exact_descent_certified` requires \(\eta_q=0\). A separate `within_tolerance_certified` field reports only whether \(\eta_q\le\varepsilon\) for a declared numerical tolerance. A positive tolerance is never promoted to an exact factorization statement, and the unique descended response table is constructed only under exact descent.

The interpretation boundary is

\[
\boxed{
\text{same coarse delay label}
\neq
\text{same physical time}
\neq
\text{dynamical equivalence}.
}
\]

Thus a small \(\eta_q\) may reflect temporal stability, limited measurement sensitivity, or insufficient temporal resolution. It does not prove a fundamental discretization of time, equality of physical propagators or trajectories, physical completeness, or consciousness.

P31 and P32 now expose the same structural principle on both experiment-grid coordinates: coarse labels are legitimate quotients only when the observable response structure factors through them. The next theorem burden is a joint node/intervention/delay quotient assembly that prevents individually valid but mutually incompatible quotient constructions from being combined into one false scale certificate.

[Read Proposition 32](docs/proposition_32_delay_quotient_compatibility.md). The [P32 theorem map](docs/figures/p32_delay_quotient_compatibility.svg), [implementation](src/consciousness_bridge/delay_quotient_compatibility.py), and [tests](tests/test_delay_quotient_compatibility.py) expose the complete proof-to-code path.

'''
text = replace_once(
    text,
    "[Read Proposition 31](docs/proposition_31_intervention_quotient_compatibility.md). The [P31 theorem map](docs/figures/p31_intervention_quotient_compatibility.svg), [implementation](src/consciousness_bridge/intervention_quotient_compatibility.py), and [tests](tests/test_intervention_quotient_compatibility.py) expose the complete proof-to-code path.\n\n---",
    "[Read Proposition 31](docs/proposition_31_intervention_quotient_compatibility.md). The [P31 theorem map](docs/figures/p31_intervention_quotient_compatibility.svg), [implementation](src/consciousness_bridge/intervention_quotient_compatibility.py), and [tests](tests/test_intervention_quotient_compatibility.py) expose the complete proof-to-code path.\n\n" + p32_section + "---",
    "README P32 full section",
)
path.write_text(text, encoding="utf-8")

# Theorem roadmap
path = Path("docs/theorem_roadmap.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "![P1-P31 theorem roadmap]", "![P1-P32 theorem roadmap]", "roadmap image alt")
text = replace_once(
    text,
    "| [P31](proposition_31_intervention_quotient_compatibility.md) | quotient factorization of intervention-conditioned response laws | exact criterion for changing the intervention set plus a representative-ambiguity budget | proved operational quotient theorem |",
    "| [P31](proposition_31_intervention_quotient_compatibility.md) | quotient factorization of intervention-conditioned response laws | exact criterion for changing the intervention set plus a representative-ambiguity budget | proved operational quotient theorem |\n| [P32](proposition_32_delay_quotient_compatibility.md) | quotient factorization of delay-conditioned response laws | exact criterion for changing the delay set plus a temporal representative-ambiguity budget | proved operational quotient theorem |",
    "roadmap index P32",
)
p32_roadmap = r'''## P32 - delay-quotient compatibility

Let \(q:\mathcal T_f\twoheadrightarrow\mathcal T_c\) be a declared many-to-one map on delay labels after the physical response space has been fixed. P32 proves that a unique coarse-delay response table exists if and only if

\[
\boxed{
q(\tau)=q(\tau')
\Longrightarrow
P^{u,\tau}=P^{u,\tau'}
\quad\forall u.
}
\]

Define

\[
\boxed{
\eta_q
=
\sup_u\sup_{q(\tau)=q(\tau')}
\|P^{u,\tau}-P^{u,\tau'}\|_{\mathrm{TV}}.
}
\]

Then \(\eta_q=0\) is equivalent to exact quotient descent. Representative selections obey

\[
\boxed{
\sup_{u,t}\|Q_s^{u,t}-Q_{s'}^{u,t}\|_{\mathrm{TV}}\le\eta_q,
\qquad
\sup_{u,v,t}|G_s-G_{s'}|\le2\eta_q.
}
\]

Exact and tolerance-relative certification are reported separately in the executable implementation. The theorem is operational: it does not identify distinct physical times or dynamical states.

Direct proof: [Proposition 32](proposition_32_delay_quotient_compatibility.md). Implementation: [delay_quotient_compatibility.py](../src/consciousness_bridge/delay_quotient_compatibility.py). Tests: [test_delay_quotient_compatibility.py](../tests/test_delay_quotient_compatibility.py).

'''
text = replace_once(
    text,
    "Direct proof: [Proposition 31](proposition_31_intervention_quotient_compatibility.md). Implementation: [intervention_quotient_compatibility.py](../src/consciousness_bridge/intervention_quotient_compatibility.py). Tests: [test_intervention_quotient_compatibility.py](../tests/test_intervention_quotient_compatibility.py).\n\n---",
    "Direct proof: [Proposition 31](proposition_31_intervention_quotient_compatibility.md). Implementation: [intervention_quotient_compatibility.py](../src/consciousness_bridge/intervention_quotient_compatibility.py). Tests: [test_intervention_quotient_compatibility.py](../tests/test_intervention_quotient_compatibility.py).\n\n" + p32_roadmap + "---",
    "roadmap P32 section",
)
path.write_text(text, encoding="utf-8")

# Research navigation
path = Path("docs/research_navigation.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "from P1 through P31", "from P1 through P32", "navigation range")
text = replace_once(
    text,
    "17. [Proposition 31](proposition_31_intervention_quotient_compatibility.md) for exact intervention-label quotienting and representative-ambiguity control.\n18. [Fundamental Theory to Consciousness program]",
    "17. [Proposition 31](proposition_31_intervention_quotient_compatibility.md) for exact intervention-label quotienting and representative-ambiguity control.\n18. [Proposition 32](proposition_32_delay_quotient_compatibility.md) for exact delay-label quotienting and temporal representative-ambiguity control.\n19. [Fundamental Theory to Consciousness program]",
    "navigation reading order P32",
)
for old, new in [
    ("19. [Stochastic fundamental bridge]", "20. [Stochastic fundamental bridge]"),
    ("20. [Falsification program]", "21. [Falsification program]"),
    ("21. [Citation and Reference Policy]", "22. [Citation and Reference Policy]"),
]:
    text = replace_once(text, old, new, f"navigation renumber {old[:2]}")
text = replace_once(
    text,
    "| P31 | [Intervention-quotient compatibility](proposition_31_intervention_quotient_compatibility.md) | exact intervention-label descent and quantitative representative ambiguity |",
    "| P31 | [Intervention-quotient compatibility](proposition_31_intervention_quotient_compatibility.md) | exact intervention-label descent and quantitative representative ambiguity |\n| P32 | [Delay-quotient compatibility](proposition_32_delay_quotient_compatibility.md) | exact delay-label descent and quantitative temporal representative ambiguity |",
    "navigation proposition index P32",
)
text = replace_once(
    text,
    "| [P31 intervention-quotient compatibility](proposition_31_intervention_quotient_compatibility.md) | exact operational intervention quotient and representative-stability bounds |",
    "| [P31 intervention-quotient compatibility](proposition_31_intervention_quotient_compatibility.md) | exact operational intervention quotient and representative-stability bounds |\n| [P32 delay-quotient compatibility](proposition_32_delay_quotient_compatibility.md) | exact operational delay quotient, tolerance separation, and representative-stability bounds |",
    "navigation fundamental table P32",
)
text = replace_once(
    text,
    "The P31 intervention-quotient layer is implemented in [intervention_quotient_compatibility.py](../src/consciousness_bridge/intervention_quotient_compatibility.py), tested in [test_intervention_quotient_compatibility.py](../tests/test_intervention_quotient_compatibility.py), and summarized by [p31_intervention_quotient_compatibility.svg](figures/p31_intervention_quotient_compatibility.svg).",
    "The P31 intervention-quotient layer is implemented in [intervention_quotient_compatibility.py](../src/consciousness_bridge/intervention_quotient_compatibility.py), tested in [test_intervention_quotient_compatibility.py](../tests/test_intervention_quotient_compatibility.py), and summarized by [p31_intervention_quotient_compatibility.svg](figures/p31_intervention_quotient_compatibility.svg). The P32 delay-quotient layer is implemented in [delay_quotient_compatibility.py](../src/consciousness_bridge/delay_quotient_compatibility.py), tested in [test_delay_quotient_compatibility.py](../tests/test_delay_quotient_compatibility.py), and summarized by [p32_delay_quotient_compatibility.svg](figures/p32_delay_quotient_compatibility.svg).",
    "navigation reproducibility P32",
)
path.write_text(text, encoding="utf-8")

# Equation and citation map
path = Path("docs/equation_and_citation_map.md")
text = path.read_text(encoding="utf-8")
p32_eq = r'''# 26. P32 delay-quotient compatibility

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(q:\mathcal T_f\twoheadrightarrow\mathcal T_c\) | declared surjective quotient of operational delay labels | repository definition | [P32](proposition_32_delay_quotient_compatibility.md) |
| \(q(\tau)=q(\tau')\Rightarrow P^{u,\tau}=P^{u,\tau'}\;\forall u\) | exact delay-fiber constancy condition | necessary and sufficient for unique response-law descent | [P32](proposition_32_delay_quotient_compatibility.md) |
| \(\eta_q=\sup_u\sup_{q(\tau)=q(\tau')}\|P^{u,\tau}-P^{u,\tau'}\|_{\mathrm{TV}}\) | operational delay-quotient ambiguity defect | repository definition | [P32](proposition_32_delay_quotient_compatibility.md) |
| \(\eta_q=0\iff\) exact delay-quotient descent | exact quotient certificate | proved | [P32](proposition_32_delay_quotient_compatibility.md) |
| \(\sup_{u,t}\|Q_s^{u,t}-Q_{s'}^{u,t}\|_{\mathrm{TV}}\le\eta_q\) | representative-selection stability | proved | [P32](proposition_32_delay_quotient_compatibility.md) |
| \(\sup_{u,v,t}|G_s-G_{s'}|\le2\eta_q\) | induced coarse temporal response-geometry ambiguity | proved by reverse triangle inequality | [P32](proposition_32_delay_quotient_compatibility.md) |
| exact certificate \(\eta_q=0\) versus tolerance certificate \(\eta_q\le\varepsilon\) | prevents approximate numerical agreement from being called exact factorization | implementation and interpretation guard | [P32](proposition_32_delay_quotient_compatibility.md) |
| same coarse delay label \(\ne\) same physical time | prevents operational time-bin quotienting from being overinterpreted as physical temporal identity | interpretation boundary | [P32](proposition_32_delay_quotient_compatibility.md) |

P32 changes delay labels only after a common response space is declared. It does not establish time quantization, dynamical equivalence, consciousness, or physical completeness. Joint node/intervention/delay assembly remains a separate theorem burden.

---

'''
text = replace_once(text, "# 26. Candidate consciousness-theory feature families", p32_eq + "# 27. Candidate consciousness-theory feature families", "equation map P32")
text = replace_once(text, "# 27. Citation discipline", "# 28. Citation discipline", "equation map citation renumber")
path.write_text(text, encoding="utf-8")

# Release metadata
path = Path("pyproject.toml")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version = "0.31.0"', 'version = "0.32.0"', "pyproject version")
text = replace_once(text, "intervention-quotient compatibility, recoverability", "intervention-quotient compatibility, delay-quotient compatibility, recoverability", "pyproject description")
path.write_text(text, encoding="utf-8")

path = Path("CITATION.cff")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version: 0.31.0", "version: 0.32.0", "citation version")
text = replace_once(text, "intervention-quotient compatibility, robust experiment design", "intervention-quotient compatibility, delay-quotient compatibility, robust experiment design", "citation abstract")
path.write_text(text, encoding="utf-8")

path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
entry = r'''## 0.32.0 - 2026-09-09

### Proposition 32 - delay-quotient compatibility

- Introduced a declared surjective delay-label quotient \(q:\mathcal T_f\twoheadrightarrow\mathcal T_c\) after the physical response space has been fixed.
- Proved that a unique coarse-delay response table exists if and only if all retained response laws are constant on every delay fiber for every intervention.
- Defined the delay-quotient ambiguity defect \(\eta_q\) as the worst total-variation separation hidden inside a proposed coarse temporal label.
- Proved \(\eta_q=0\) if and only if exact delay-quotient descent holds.
- Proved representative-selection stability \(\sup_{u,t}\|Q_s^{u,t}-Q_{s'}^{u,t}\|_{\mathrm{TV}}\le\eta_q\).
- Proved induced response-geometry ambiguity \(\sup_{u,v,t}|G_s-G_{s'}|\le2\eta_q\).
- Separated literal exact descent from tolerance-relative approximation in the executable certificate and restricted the unique descended table to exact descent only.
- Explicitly separated operational delay quotienting from physical time identity, dynamical equivalence, and time quantization.
- Added executable mathematics, nine dedicated regression tests, a publication theorem map, full main-paper integration, theorem-roadmap integration, navigation, equation provenance, release consistency guards, and synchronized 0.32.0 metadata.
- Preserved joint node/intervention/delay assembly, physical completeness, and experiential interpretation as separate open theorem burdens.

'''
text = replace_once(text, "## 0.31.0 - 2026-09-09", entry + "## 0.31.0 - 2026-09-09", "changelog P32")
path.write_text(text, encoding="utf-8")

# Main-page guards
path = Path("tests/test_main_page_visual_paper.py")
text = path.read_text(encoding="utf-8")
text = replace_once(text, '    "p31_intervention_quotient_compatibility.svg",', '    "p31_intervention_quotient_compatibility.svg",\n    "p32_delay_quotient_compatibility.svg",', "main page figure guard")
text = replace_once(text, "for index in range(1, 32):", "for index in range(1, 33):", "main page proposition guard")
path.write_text(text, encoding="utf-8")

# Release consistency guard: prevent badge, metadata, and glance record from drifting apart.
Path("tests/test_release_metadata_consistency.py").write_text(r'''from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def _project_version() -> str:
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version = "([0-9]+\.[0-9]+\.[0-9]+)"$', text, re.MULTILINE)
    assert match
    return match.group(1)


def _citation_version() -> str:
    text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    match = re.search(r'^version: ([0-9]+\.[0-9]+\.[0-9]+)$', text, re.MULTILINE)
    assert match
    return match.group(1)


def test_release_version_is_synchronized_across_public_surfaces():
    version = _project_version()
    assert _citation_version() == version
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert f"version-{version}-2563eb" in readme
    assert f"| research-software version | **{version}** |" in readme


def test_public_proposition_count_matches_released_chain():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "**32 proposition-level results" in readme
    assert "| proposition-level results | **32** |" in readme
''', encoding="utf-8")

# Global theorem roadmap SVG
path = Path("docs/figures/theorem_roadmap.svg")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'height="3800" viewBox="0 0 1600 3800"', 'height="4040" viewBox="0 0 1600 4040"', "SVG outer size")
text = replace_once(text, '<rect width="1600" height="3560" fill="#ffffff"/>', '<rect width="1600" height="4040" fill="#ffffff"/>', "SVG background size")
text = replace_once(text, "through Proposition 31", "through Proposition 32", "SVG title")
text = replace_once(text, "Theorem Roadmap - P1 through P31", "Theorem Roadmap - P1 through P32", "SVG heading")
old_frontier = '''  <rect x="95" y="3720" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="3745" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="3768" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Delay/time quotienting, physical completeness, experiential formalization, and the bridge theorem remain open.</text>'''
new_frontier = '''  <rect x="225" y="3720" width="1150" height="190" rx="20" fill="#fff7ed" stroke="#ea580c" stroke-width="1.8"/>
  <text x="265" y="3757" class="label">DELAY QUOTIENT · P32</text>
  <text x="265" y="3795" class="head">Coarse delays require fiberwise response agreement</text>
  <text x="265" y="3829" class="body">Time labels may merge only when retained response laws descend.</text>
  <text x="265" y="3864" class="eq">ηq = supu supq(τ)=q(τ′) ||Pᵘ,τ−Pᵘ,τ′||TV</text>
  <text x="930" y="3864" class="eq">ηq=0 ⇔ exact descent</text>
  <text x="265" y="3894" class="body">Representative-dependent geometry is bounded by 2ηq.</text>

  <rect x="95" y="3960" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="3985" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="4008" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Joint quotient assembly, physical completeness, experiential formalization, and the bridge theorem remain open.</text>'''
text = replace_once(text, old_frontier, new_frontier, "SVG P32 card")
path.write_text(text, encoding="utf-8")
