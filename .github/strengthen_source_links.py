from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing source-link marker: {label}")
    return text.replace(old, new, 1)


# Main page: turn the scientific-anchor paragraph into a compact source table.
readme = Path("README.md")
text = readme.read_text(encoding="utf-8")
old = """## Scientific anchors

The fundamental-theory layer is motivated by peer-reviewed work showing that quantum information can constrain questions about gravity and emergent spacetime: Jacobson's entanglement-equilibrium derivation of the semiclassical Einstein equation, holographic quantum error-correcting-code models, recent information-theoretic quantum-gravity test programs, and holographic spacetime/entanglement relations. The experiential side is kept independent using mathematical consciousness frameworks and adversarial empirical theory testing.

## Where *My Big TOE* fits
"""
new = """## Scientific anchors

The fundamental-theory layer is connected to external literature through explicit source roles. These papers motivate mathematical and experimental directions. None is cited as a proof of consciousness.

| Source | Role in this repository | Direct record |
| --- | --- | --- |
| Jacobson, 2016 | entanglement-equilibrium route connecting quantum information and semiclassical spacetime dynamics | [DOI 10.1103/PhysRevLett.116.201101](https://doi.org/10.1103/PhysRevLett.116.201101) |
| Pastawski, Yoshida, Harlow, and Preskill, 2015 | holographic quantum error correction and bulk-boundary structure | [DOI 10.1007/JHEP06(2015)149](https://doi.org/10.1007/JHEP06(2015)149) |
| Marletto and Vedral, 2025 | information-theoretic methods for laboratory tests relevant to quantum gravity | [DOI 10.1103/RevModPhys.97.015006](https://doi.org/10.1103/RevModPhys.97.015006) |
| Takayanagi, 2025 | quantum-information perspective on emergent holographic spacetime | [DOI 10.1103/pg4r-fy8n](https://doi.org/10.1103/pg4r-fy8n) |
| Kleiner, 2020 | mathematical formalization of consciousness models and experiential spaces | [DOI 10.3390/e22060609](https://doi.org/10.3390/e22060609) |
| Cogitate Consortium et al., 2025 | adversarial empirical testing of predictions from IIT and GNWT | [DOI 10.1038/s41586-025-08888-1](https://doi.org/10.1038/s41586-025-08888-1) |

The evidential classification and bibliographic metadata for these sources are maintained in the [Reference Audit](docs/reference_audit.md). The broader physics and mathematical foundation is maintained in the [Foundational Bibliography](docs/foundational_physics_mathematics_bibliography.md).

## Where *My Big TOE* fits
"""
text = replace_once(text, old, new, "README scientific anchors")
old_campbell = """Thomas W. Campbell's *My Big TOE* proposes that consciousness is fundamental and physical reality is virtual. Those broad claims are **not treated as established scientific facts here**. Campbell, Owhadi, Sauvageau, and Watkinson did publish a narrower simulation-theory experiment proposal based on explicit finite-resource assumptions and wave/particle tests. That work is included only as a **speculative, falsifiable antecedent**, not as a premise of the present framework.
"""
new_campbell = """Thomas W. Campbell's *My Big TOE* proposes that consciousness is fundamental and physical reality is virtual. Those broad claims are **not treated as established scientific facts here**. Campbell, Owhadi, Sauvageau, and Watkinson published a narrower simulation-theory experiment proposal based on explicit finite-resource assumptions and wave/particle tests. The paper is available as [arXiv:1703.00058](https://arxiv.org/abs/1703.00058). It is included only as a **speculative, falsifiable antecedent**, not as a premise of the present framework.
"""
text = replace_once(text, old_campbell, new_campbell, "README Campbell link")
readme.write_text(text, encoding="utf-8")

# Add a standard reference for the differential argument.
bib = Path("docs/foundational_physics_mathematics_bibliography.md")
btext = bib.read_text(encoding="utf-8")
marker = """## Ay, Jost, Le, and Schwachhofer 2017

Nihat Ay, Jurgen Jost, Hong Van Le, and Lorenz Schwachhofer, *Information Geometry*. Ergebnisse der Mathematik und ihrer Grenzgebiete 64, Springer, 2017. DOI: [10.1007/978-3-319-56478-4](https://doi.org/10.1007/978-3-319-56478-4).

**Role:** rigorous mathematical foundations for statistical manifolds, Fisher metric, Amari-Chentsov tensor, sufficient statistics, and geometric inference.

---
"""
replacement = marker + """
# 2.1 Differential topology and smooth maps

## Lee 2013

John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Graduate Texts in Mathematics 218, Springer, 2013. DOI: [10.1007/978-1-4419-9982-5](https://doi.org/10.1007/978-1-4419-9982-5).

**Role:** standard reference for smooth manifolds, differentials, the chain rule, rank, submersions, immersions, and local smooth-map structure.

**Repository use:** mathematical background for the differential rank obstruction in Proposition 19. The P19 statement itself is proved in this repository from the chain rule and does not originate in this text.

---
"""
btext = replace_once(btext, marker, replacement, "Lee bibliography insertion")
bib.write_text(btext, encoding="utf-8")

# P19: add a direct source and implementation trail.
p19 = Path("docs/proposition_19_fundamental_physical_sufficiency.md")
ptext = p19.read_text(encoding="utf-8")
old_heading = """# 10. Computational audit

The implementation is in

`src/consciousness_bridge/fundamental_physical_sufficiency.py`.
"""
new_heading = """# 10. Scientific provenance and direct audit path

P19 combines repository-original sufficiency statements with standard mathematical ingredients. The lineage is explicit:

| Ingredient | Status in P19 | Direct source |
| --- | --- | --- |
| factorization through fibers | proved here for the declared maps | [P19 proof on this page](#2-p19a---exact-factorization-theorem), with earlier bridge-factorization structure in [P5](proposition_5_feature_sufficiency.md) |
| conditional mutual information and conditional independence | standard finite-alphabet information theory applied here | [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006) |
| differential, chain rule, and rank | standard smooth-map mathematics applied here | [Lee 2013](foundational_physics_mathematics_bibliography.md#lee-2013) |
| physical interpretation limits | repository scientific-boundary rule | [Citation and Reference Policy](citation_and_reference_policy.md) |
| empirical burden | open scientific program | [Falsification Program](falsification_program.md) |
| fundamental-theory context | open candidate-theory interface | [Fundamental Theory to Consciousness](fundamental_theory_consciousness_program.md) |

The theorem does not inherit a consciousness ontology from any of these references. The experiential descriptor remains an independently specified target whose scientific validity must be established separately.

---

# 11. Computational audit

The implementation is [fundamental_physical_sufficiency.py](../src/consciousness_bridge/fundamental_physical_sufficiency.py), with claim-level regression tests in [test_fundamental_physical_sufficiency.py](../tests/test_fundamental_physical_sufficiency.py).
"""
ptext = replace_once(ptext, old_heading, new_heading, "P19 provenance section")
p19.write_text(ptext, encoding="utf-8")

# Equation map: make the named standard references directly clickable.
eq = Path("docs/equation_and_citation_map.md")
etext = eq.read_text(encoding="utf-8")
etext = etext.replace(
    "P19; Cover and Thomas 2006 |",
    "[P19](proposition_19_fundamental_physical_sufficiency.md); [Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006) |",
)
etext = etext.replace(
    "Cover and Thomas 2006; P19 |",
    "[Cover and Thomas 2006](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006); [P19](proposition_19_fundamental_physical_sufficiency.md) |",
)
etext = etext.replace(
    "P19; standard differential calculus |",
    "[P19](proposition_19_fundamental_physical_sufficiency.md); [Lee 2013](foundational_physics_mathematics_bibliography.md#lee-2013) |",
)
# Link remaining P19 provenance labels in the P19 table where doing so improves navigation.
etext = etext.replace(
    "| repository abstraction | P19 |",
    "| repository abstraction | [P19](proposition_19_fundamental_physical_sufficiency.md) |",
)
etext = etext.replace(
    "| proved | P19 |",
    "| proved | [P19](proposition_19_fundamental_physical_sufficiency.md) |",
)
eq.write_text(etext, encoding="utf-8")

# Reference audit: add the standard differential source used by P19.
audit = Path("docs/reference_audit.md")
atext = audit.read_text(encoding="utf-8")
anchor = "| Kleiner, 2020 | *Entropy* 22, 609. DOI: [10.3390/e22060609](https://doi.org/10.3390/e22060609) | mathematical formalization of consciousness models and experiential spaces | peer-reviewed mathematical consciousness paper |"
addition = anchor + "\n| Lee, 2013 | *Introduction to Smooth Manifolds*, 2nd ed. DOI: [10.1007/978-1-4419-9982-5](https://doi.org/10.1007/978-1-4419-9982-5) | standard differential and rank background used in the P19 local obstruction | standard scholarly monograph |"
atext = replace_once(atext, anchor, addition, "Reference audit Lee row")
audit.write_text(atext, encoding="utf-8")

# Navigation: expose the P19 figure and tests directly.
nav = Path("docs/research_navigation.md")
ntext = nav.read_text(encoding="utf-8")
old_impl = """The executable P19 implementation is [fundamental_physical_sufficiency.py](../src/consciousness_bridge/fundamental_physical_sufficiency.py), with regression tests in [test_fundamental_physical_sufficiency.py](../tests/test_fundamental_physical_sufficiency.py).

The repository-wide test workflow is [test.yml](../.github/workflows/test.yml). The quantitative figure generators and tests are linked directly from their atlas pages.
"""
new_impl = """The executable P19 implementation is [fundamental_physical_sufficiency.py](../src/consciousness_bridge/fundamental_physical_sufficiency.py), with regression tests in [test_fundamental_physical_sufficiency.py](../tests/test_fundamental_physical_sufficiency.py) and the publication figure in [p19_fundamental_physical_sufficiency.svg](figures/p19_fundamental_physical_sufficiency.svg).

The repository-wide test workflow is [test.yml](../.github/workflows/test.yml). Local documentation, figure, and anchor integrity is enforced by [test_document_link_integrity.py](../tests/test_document_link_integrity.py). The quantitative figure generators and tests are linked directly from their atlas pages.
"""
ntext = replace_once(ntext, old_impl, new_impl, "navigation implementation trail")
nav.write_text(ntext, encoding="utf-8")
