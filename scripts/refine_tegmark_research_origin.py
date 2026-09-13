"""Refine Tegmark research-origin wording to be collegial and scientifically precise."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str, label: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if new in text and old not in text:
        return
    if old not in text:
        raise RuntimeError(f"missing wording anchor for {label} in {path}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    replace_once(
        "website/start-here.html",
        "The earliest conceptual line that eventually led to this research program began while studying Max Tegmark's <em>Consciousness as a State of Matter</em> (2015). That paper motivated questions about physical subsystem structure, factorization, information, integration, independence, and dynamics. The present repository subsequently developed its own theorem program, assumptions, proofs, computational certificates, and falsification boundaries.",
        "The earliest conceptual line that eventually led to this research program began while studying Max Tegmark's <em>Consciousness as a State of Matter</em> (2015), particularly its treatment of physical subsystem structure, factorization, information, integration, independence, and dynamics. The paper provided an important conceptual starting point for questions that this project later developed in a further mathematical direction, with its own assumptions, derivations, computational methods, and tests.",
        "Start Here origin paragraph",
    )
    replace_once(
        "website/start-here.html",
        "See <a href=\"sources.html#research-origins\">Sources &amp; Reproducibility</a> for the exact evidential role.",
        "See <a href=\"sources.html#research-origins\">Sources &amp; Reproducibility</a> for bibliographic context and research provenance.",
        "Start Here citation role",
    )
    replace_once(
        "website/start-here.html",
        "<p><strong>Boundary:</strong> this origin citation does not make Tegmark's paper evidence for the later P1-P86 results and does not imply that any physical-to-experiential ontology has been established.</p>",
        "<p><strong>Research context:</strong> Tegmark's paper is acknowledged here as an important conceptual starting point. The subsequent proposition sequence develops a distinct mathematical framework and provides its own derivations, implementations, tests, and reproducibility record.</p>",
        "Start Here origin boundary",
    )

    replace_once(
        "website/sources.html",
        "<h2>An intellectual starting point, not an evidential shortcut</h2>",
        "<h2>An intellectual starting point and a continuing line of questions</h2>",
        "Sources origin heading",
    )
    replace_once(
        "website/sources.html",
        "The earliest conceptual line that eventually led to this research program began while studying Max Tegmark's <em>Consciousness as a State of Matter</em>. The paper asks how information, integration, independence, dynamics, subsystem structure, and factorization might enter a physical treatment of consciousness. Those questions helped motivate the initial direction of this project.",
        "The earliest conceptual line that eventually led to this research program began while studying Max Tegmark's <em>Consciousness as a State of Matter</em>. Its treatment of information, integration, independence, dynamics, subsystem structure, and factorization provided an important conceptual starting point for questions that this project later pursued in a further mathematical direction.",
        "Sources origin paragraph",
    )
    replace_once(
        "website/sources.html",
        "<p><strong>Scope of this citation:</strong> Tegmark's paper is cited here as intellectual and physical-context background. It is not evidence for the repository's later original propositions, exact model-separation certificates, or any claim that a consciousness ontology has been established. Those later results stand or fall on their own assumptions, proofs, implementations, tests, and provenance records.</p>",
        "<p><strong>Role of this reference:</strong> Tegmark's paper is cited as an important conceptual starting point for the research program. The subsequent proposition sequence develops a distinct mathematical framework whose results are supported by their own assumptions, derivations, implementations, tests, and reproducibility record.</p>",
        "Sources citation role",
    )

    replace_once(
        "docs/claim_evidence_standard.md",
        "## 7. Research origins versus evidential support",
        "## 7. Research origins and scholarly provenance",
        "claim standard heading",
    )
    replace_once(
        "docs/claim_evidence_standard.md",
        "Intellectual origin and evidential support are different roles. A paper may motivate a question without proving later repository results.",
        "Intellectual origin and mathematical support are complementary scholarly roles. A paper may open a line of questions, while later results carry their own proof and reproducibility records.",
        "claim standard role paragraph",
    )
    replace_once(
        "docs/claim_evidence_standard.md",
        "That paper is cited here as an intellectual starting point for questions about physical subsystem structure, factorization, information, integration, independence, and dynamics. It is **not** cited as evidence for the repository's later original propositions, exact parity certificates, or any claim that a consciousness ontology has been established.",
        "That paper is cited here as an important conceptual starting point for questions about physical subsystem structure, factorization, information, integration, independence, and dynamics. The subsequent proposition sequence develops a distinct mathematical framework, with its own assumptions, derivations, implementations, tests, and provenance.",
        "claim standard Tegmark paragraph",
    )

    replace_once(
        "docs/literature_map.md",
        "**Use here:** motivates part of the physical-subsystem problem and the companion observer program. It does not supply the physical-to-experiential bridge developed in this repository.",
        "**Use here:** motivates part of the physical-subsystem problem and the companion observer program, and provided an important conceptual starting point for the questions pursued here. The later bridge formalism and proposition sequence are developed within this repository.",
        "literature map use",
    )
    replace_once(
        "docs/literature_map.md",
        "**Research-origin note:** this was the earliest paper whose physical framing directly prompted the line of questions that grew into this program. That historical role is distinct from evidential support: the later repository propositions require their own proofs, code, tests, and provenance.",
        "**Research-origin note:** this was the earliest paper whose physical framing directly prompted the line of questions that grew into this program. The later work takes those questions in a further mathematical direction through an independently documented theorem, implementation, and reproducibility record.",
        "literature map origin note",
    )

    replace_once(
        "docs/reference_audit.md",
        "intellectual starting point for questions about physical subsystem structure, information, integration, independence, dynamics, and factorization; not evidential support for later repository-original propositions",
        "important conceptual starting point for questions about physical subsystem structure, information, integration, independence, dynamics, and factorization; the later proposition sequence develops a distinct mathematical framework with its own proof and reproducibility record",
        "reference audit Tegmark row",
    )

    replace_once(
        "docs/claim_source_matrix.md",
        "| Research origin | The earliest conceptual line that grew into this project began while studying Max Tegmark's *Consciousness as a State of Matter* | intellectual provenance | Tegmark 2015, DOI [10.1016/j.chaos.2015.03.014](https://doi.org/10.1016/j.chaos.2015.03.014), [arXiv:1401.1219](https://arxiv.org/abs/1401.1219); [Literature Map](literature_map.md) | origin is not evidential validation of later propositions |",
        "| Research origin | The earliest conceptual line that grew into this project began while studying Max Tegmark's *Consciousness as a State of Matter* | intellectual provenance | Tegmark 2015, DOI [10.1016/j.chaos.2015.03.014](https://doi.org/10.1016/j.chaos.2015.03.014), [arXiv:1401.1219](https://arxiv.org/abs/1401.1219); [Literature Map](literature_map.md) | the later proposition sequence has its own assumptions, derivations, and reproducibility record |",
        "claim matrix research origin",
    )
    replace_once(
        "docs/claim_source_matrix.md",
        "| Formal consciousness modeling | A rigorous consciousness theory should make its physical and experiential mathematical objects explicit | external methodological background plus repository formulation | Kleiner 2020; Kleiner and Tull 2020/2021 in [Literature Map](literature_map.md); [Equation and Citation Map](equation_and_citation_map.md) | these sources do not validate this repository's bridge hypotheses |",
        "| Formal consciousness modeling | A rigorous consciousness theory should make its physical and experiential mathematical objects explicit | external methodological background plus repository formulation | Kleiner 2020; Kleiner and Tull 2020/2021 in [Literature Map](literature_map.md); [Equation and Citation Map](equation_and_citation_map.md) | these sources provide methodological context; repository bridge hypotheses are evaluated through their own stated assumptions and tests |",
        "claim matrix formal modeling",
    )

    replace_once(
        "tests/test_scholarly_provenance_surface.py",
        "def test_sources_page_records_tegmark_origin_without_overclaiming() -> None:",
        "def test_sources_page_records_tegmark_origin_with_collegial_scope() -> None:",
        "scholarly test name",
    )
    replace_once(
        "tests/test_scholarly_provenance_surface.py",
        '    assert "intellectual and physical-context background" in sources\n    assert "not evidence for the repository\'s later original propositions" in sources',
        '    assert "important conceptual starting point" in sources\n    assert "distinct mathematical framework" in sources',
        "scholarly sources assertions",
    )
    replace_once(
        "tests/test_scholarly_provenance_surface.py",
        '        "Research origins versus evidential support",',
        '        "Research origins and scholarly provenance",',
        "scholarly standard heading assertion",
    )
    replace_once(
        "tests/test_scholarly_provenance_surface.py",
        "def test_reference_audit_classifies_tegmark_as_origin_not_validation() -> None:",
        "def test_reference_audit_records_tegmark_as_research_origin() -> None:",
        "reference audit test name",
    )
    replace_once(
        "tests/test_scholarly_provenance_surface.py",
        '    assert "intellectual starting point" in audit\n    assert "not evidential support for later repository-original propositions" in audit',
        '    assert "important conceptual starting point" in audit\n    assert "distinct mathematical framework" in audit',
        "reference audit assertions",
    )
    replace_once(
        "tests/test_scholarly_provenance_surface.py",
        '        "Tegmark validates this framework",\n        "Tegmark proves this framework",',
        '        "Tegmark validates this framework",\n        "Tegmark proves this framework",\n        "this origin citation does not make Tegmark\'s paper evidence",\n        "not evidence for the repository\'s later original propositions",\n        "not evidential support for later repository-original propositions",',
        "defensive wording guard",
    )

    replace_once(
        "scripts/verify_repository.py",
        '    if "intellectual and physical-context background" not in sources_page:\n        raise RuntimeError("sources page does not distinguish research origin from evidential support")',
        '    if "important conceptual starting point" not in sources_page or "distinct mathematical framework" not in sources_page:\n        raise RuntimeError("sources page does not expose the collegial Tegmark research-origin context")',
        "repository verifier origin check",
    )

    forbidden_origin_phrases = (
        "this origin citation does not make Tegmark's paper evidence",
        "not evidence for the repository's later original propositions",
        "not evidential support for later repository-original propositions",
    )
    origin_files = (
        "website/start-here.html",
        "website/sources.html",
        "docs/claim_evidence_standard.md",
        "docs/literature_map.md",
        "docs/reference_audit.md",
        "docs/claim_source_matrix.md",
    )
    offenders = []
    for relative in origin_files:
        text = (ROOT / relative).read_text(encoding="utf-8")
        for phrase in forbidden_origin_phrases:
            if phrase in text:
                offenders.append((relative, phrase))
    if offenders:
        raise RuntimeError(f"defensive Tegmark origin wording remains: {offenders}")


if __name__ == "__main__":
    main()
