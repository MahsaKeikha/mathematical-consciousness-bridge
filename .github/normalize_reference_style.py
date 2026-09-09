from pathlib import Path
import re
import subprocess


def normalize_dashes(text: str) -> str:
    text = text.replace(" — ", " - ")
    text = text.replace(" – ", " - ")
    text = text.replace("—", "-")
    text = text.replace("–", "-")
    return text


tracked = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
for name in tracked:
    path = Path(name)
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    new = normalize_dashes(text)
    if new != text:
        path.write_text(new, encoding="utf-8")

for name in (
    "docs/foundational_physics_mathematics_bibliography.md",
    "docs/literature_map.md",
):
    path = Path(name)
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r"DOI Part I:\s*`(10\.[^`]+)`\.?",
        r"DOI Part I: [\1](https://doi.org/\1).",
        text,
    )
    text = re.sub(
        r"DOI:\s*`(10\.[^`]+)`\.?",
        r"DOI: [\1](https://doi.org/\1).",
        text,
    )
    text = re.sub(
        r"DOI:\s*(10\.[0-9A-Za-z./()_-]+)\.",
        lambda match: (
            f"DOI: [{match.group(1)}](https://doi.org/{match.group(1)})."
        ),
        text,
    )
    path.write_text(text, encoding="utf-8")

bib = Path("docs/fundamental_theory_references.bib")
btext = bib.read_text(encoding="utf-8")
if "doi     = {10.1023/A:1026654312961}" not in btext:
    btext = btext.replace(
        "  archivePrefix = {arXiv}\n}\n\n@article{kleiner2020models,",
        "  archivePrefix = {arXiv},\n"
        "  doi     = {10.1023/A:1026654312961}\n"
        "}\n\n@article{kleiner2020models,",
        1,
    )
if "url     = {https://arxiv.org/abs/1703.00058}" not in btext:
    btext = btext.replace(
        "  archivePrefix = {arXiv},\n"
        "  note    = {Included as a speculative falsifiable antecedent, not as established fundamental physics}\n"
        "}",
        "  archivePrefix = {arXiv},\n"
        "  url     = {https://arxiv.org/abs/1703.00058},\n"
        "  note    = {Included as a speculative falsifiable antecedent, not as established fundamental physics}\n"
        "}",
        1,
    )
bib.write_text(normalize_dashes(btext), encoding="utf-8")

policy = """# Citation and Reference Policy

This repository uses explicit provenance rules so that readers can distinguish standard mathematics, established physics, external empirical evidence, repository-original results, and speculative antecedents.

## Citation standard

1. External scientific claims must be traceable to a primary paper, a major scholarly review, a standard monograph, or an authoritative institutional source.
2. Peer-reviewed sources are preferred for scientific claims. Preprints are identified as preprints and are not presented as equivalent to peer-reviewed evidence.
3. DOI links use the canonical form `https://doi.org/<DOI>` whenever a DOI is available.
4. Repository-original propositions are cited by proposition number and linked to their proof document. They are not attributed to external literature.
5. Standard equations are identified as standard results and linked to an appropriate source in the equation and citation map.
6. Empirical consciousness findings are described as evidence about measured neural or behavioral states. They are not described as proofs of a physical-to-experiential bridge.
7. Speculative proposals are labeled explicitly. Thomas W. Campbell and coauthors are included only for the falsifiable simulation-test proposal, not as an established theory of fundamental physics or consciousness.
8. The wording of a source's scientific role must not exceed what the cited source establishes.

## Reference layers

- [Equation and Citation Map](equation_and_citation_map.md): equation-level provenance and proposition lineage.
- [Foundational Physics, Mathematics, and Spaceflight Bibliography](foundational_physics_mathematics_bibliography.md): standard mathematics, physics, statistics, empirical work, and application sources.
- [Literature Map](literature_map.md): consciousness-theory sources and the specific role each source plays in this project.
- [Fundamental Theory References](fundamental_theory_references.bib): machine-readable references for the fundamental-theory interface.
- [Reference Audit](reference_audit.md): metadata and evidence-classification checks for the most consequential sources.

## Writing standard

The main page and research documentation use direct technical prose. En dashes and em dashes are not used. Sentences are rewritten with commas, periods, parentheses, or ordinary hyphens where appropriate. Mathematical minus signs remain unchanged.

Claims are written in the smallest defensible form. Terms such as `proves`, `establishes`, and `demonstrates` are reserved for results that meet the corresponding mathematical or empirical standard.
"""
Path("docs/citation_and_reference_policy.md").write_text(policy, encoding="utf-8")

audit = """# Reference Audit

This audit records the source class and bibliographic metadata for references that carry substantial weight in the fundamental-theory and consciousness sections of the repository. The purpose is not to rank theories. The purpose is to keep scientific claims tied to the correct evidential source.

| Source | Publication record | Repository use | Evidence class |
| --- | --- | --- | --- |
| Marletto and Vedral, 2025 | *Reviews of Modern Physics* 97, 015006. DOI: [10.1103/RevModPhys.97.015006](https://doi.org/10.1103/RevModPhys.97.015006) | quantum-information methods relevant to laboratory tests of quantum gravity | peer-reviewed review article |
| Jacobson, 2016 | *Physical Review Letters* 116, 201101. DOI: [10.1103/PhysRevLett.116.201101](https://doi.org/10.1103/PhysRevLett.116.201101) | entanglement-equilibrium route connecting spacetime dynamics and quantum information | peer-reviewed theoretical physics article |
| Pastawski, Yoshida, Harlow, and Preskill, 2015 | *Journal of High Energy Physics* 2015, 149. DOI: [10.1007/JHEP06(2015)149](https://doi.org/10.1007/JHEP06(2015)149) | holographic quantum error correction and bulk-boundary structure | peer-reviewed theoretical physics article |
| Takayanagi, 2025 | *Physical Review Letters* 134, 240001. DOI: [10.1103/pg4r-fy8n](https://doi.org/10.1103/pg4r-fy8n) | quantum-information perspective on emergent holographic spacetime | peer-reviewed essay in a physics journal |
| Maldacena, 1998 | *Advances in Theoretical and Mathematical Physics* 2, 231-252. DOI: [10.1023/A:1026654312961](https://doi.org/10.1023/A:1026654312961) | holographic duality background | peer-reviewed theoretical physics article |
| Kleiner, 2020 | *Entropy* 22, 609. DOI: [10.3390/e22060609](https://doi.org/10.3390/e22060609) | mathematical formalization of consciousness models and experiential spaces | peer-reviewed mathematical consciousness paper |
| Cogitate Consortium et al., 2025 | *Nature* 642, 133-142. DOI: [10.1038/s41586-025-08888-1](https://doi.org/10.1038/s41586-025-08888-1) | adversarial empirical testing of IIT and GNWT predictions | peer-reviewed empirical neuroscience article |
| Campbell, Owhadi, Sauvageau, and Watkinson, 2017 | *International Journal of Quantum Foundations* 3, 78-99; [arXiv:1703.00058](https://arxiv.org/abs/1703.00058) | historical example of a falsifiable simulation-test proposal | speculative antecedent, not established fundamental physics |

## Interpretation rule

A citation to quantum gravity does not imply a citation to consciousness. A citation to neural correlates does not establish bridge sufficiency. A mathematical consciousness formalism supplies definitions and structural tools, not empirical validation by itself. The repository's own propositions remain conditional on their declared assumptions.

The scientific burden for any future non-reducibility claim remains higher than correlation. Such a result would require a demonstrably adequate physical descriptor, independently justified experiential variables, explicit measurement models, finite-sample certification, omitted-variable controls, and reproducible evidence.
"""
Path("docs/reference_audit.md").write_text(audit, encoding="utf-8")

readme = Path("README.md")
rtext = readme.read_text(encoding="utf-8")
if "# Citation, provenance, and writing standard" not in rtext:
    block = """# Citation, provenance, and writing standard

Scientific provenance is part of the argument, not an afterthought. Standard equations, external empirical findings, repository-original propositions, and speculative antecedents are labeled separately. The main provenance resources are the [Equation and Citation Map](docs/equation_and_citation_map.md), the [Foundational Bibliography](docs/foundational_physics_mathematics_bibliography.md), the [Literature Map](docs/literature_map.md), the machine-readable [Fundamental Theory References](docs/fundamental_theory_references.bib), and the [Reference Audit](docs/reference_audit.md). The complete citation rules are documented in the [Citation and Reference Policy](docs/citation_and_reference_policy.md).

The writing style is deliberately direct and technical. En dashes and em dashes are not used in prose. External claims are kept within the scope of the cited source, and repository results are identified by proposition number rather than presented as literature-derived facts.

---

"""
    marker = "# Paper map"
    if marker not in rtext:
        raise RuntimeError("README insertion marker not found")
    rtext = rtext.replace(marker, block + marker, 1)
readme.write_text(normalize_dashes(rtext), encoding="utf-8")

test = '''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _text_files():
    roots = [ROOT / "README.md", ROOT / "docs", ROOT / "src", ROOT / "scripts", ROOT / "tests"]
    for root in roots:
        if root.is_file():
            yield root
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".md", ".py", ".svg", ".bib", ".txt", ".yml", ".yaml", ".toml", ".cff"}:
                yield path


def test_no_en_or_em_dash_in_repository_text():
    violations = []
    for path in _text_files():
        text = path.read_text(encoding="utf-8")
        if "\\u2013" in text or "\\u2014" in text:
            violations.append(str(path.relative_to(ROOT)))
    assert not violations, f"en dash or em dash found in: {violations}"


def test_main_page_exposes_reference_provenance():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    required = [
        "docs/equation_and_citation_map.md",
        "docs/foundational_physics_mathematics_bibliography.md",
        "docs/literature_map.md",
        "docs/fundamental_theory_references.bib",
        "docs/reference_audit.md",
        "docs/citation_and_reference_policy.md",
    ]
    for item in required:
        assert item in text


def test_reference_audit_keeps_evidence_classes_distinct():
    text = (ROOT / "docs/reference_audit.md").read_text(encoding="utf-8")
    assert "peer-reviewed" in text
    assert "speculative antecedent" in text
    assert "not established fundamental physics" in text
    assert "10.1103/RevModPhys.97.015006" in text
    assert "10.1038/s41586-025-08888-1" in text


def test_fundamental_bib_has_stable_identifiers():
    text = (ROOT / "docs/fundamental_theory_references.bib").read_text(encoding="utf-8")
    for identifier in [
        "10.1103/RevModPhys.97.015006",
        "10.1103/PhysRevLett.116.201101",
        "10.1007/JHEP06(2015)149",
        "10.1103/pg4r-fy8n",
        "10.1023/A:1026654312961",
        "10.3390/e22060609",
        "10.1038/s41586-025-08888-1",
        "1703.00058",
    ]:
        assert identifier in text
'''
Path("tests/test_reference_and_prose_style.py").write_text(test, encoding="utf-8")
