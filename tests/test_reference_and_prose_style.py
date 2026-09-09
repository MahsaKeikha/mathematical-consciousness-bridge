from pathlib import Path

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
        if "\u2013" in text or "\u2014" in text:
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
