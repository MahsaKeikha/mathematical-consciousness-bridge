from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
FRONTIER = "docs/calibration_optimization_frontier_p61_p70.md"

text = README.read_text(encoding="utf-8")

# 1. Replace the detailed Section 7 with a concise reader-facing pointer.
start = text.index("# 7. Calibration and optimization: the current theorem frontier")
end = text.index("# What has actually been established", start)
replacement = '''# 7. Calibration and optimization as a downstream experimental layer

The later calibration and discrete-optimization results belong to the **experimental implementation layer**, not to the conceptual introduction to the consciousness bridge itself. Their role is to determine how finite calibration measurements should be allocated and how candidate integer designs can be certified once the bridge hypothesis, physical descriptor, witness family, uncertainty model, and experimental constraints have already been declared.

To keep this main page readable for a first-time scientific reader, the complete P61-P70 theorem sequence, derivations, figures, implementations, tests, assumptions, and primal-dual certificates are documented separately:

**[Read the complete Calibration and Optimization Frontier: P61-P70](docs/calibration_optimization_frontier_p61_p70.md).**

The main scientific conclusion does not depend on reading that optimization branch first. It is supporting machinery for executing and certifying experiments, not a proposed definition or measure of consciousness.

---

'''
text = text[:start] + replacement + text[end:]

# 2. Remove P61-P70 from the collapsed proof/code audit index on the README.
first = text.find("- **Proposition 61**:")
if first != -1:
    close = text.find("\n\n</details>", first)
    if close == -1:
        raise SystemExit("Could not find end of proof audit index")
    text = text[:first] + text[close:]

# 3. Point the stage-7 overview directly to the dedicated technical page.
old_stage = "| 7. Transition calibration and integer optimization | **P59-P70** | How should finite calibration resources be allocated and certified under discrete counts and heterogeneous costs? | Proved / implemented / tested | [P70 proposition](docs/proposition_70_primal_dual_gap_decomposition.md) |"
new_stage = "| 7. Calibration and integer optimization | Downstream experimental layer | How should finite calibration resources be allocated and certified after the scientific witness and uncertainty model are declared? | Proved / implemented / tested | [Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md) |"
if old_stage in text:
    text = text.replace(old_stage, new_stage, 1)

# 4. Add the frontier page to navigation.
needle = "| Read the proposition chronology | [Detailed proposition record](docs/detailed_proposition_record.md) |"
navline = "| Inspect the P61-P70 calibration and optimization branch | [Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md) |"
if navline not in text:
    text = text.replace(needle, needle + "\n" + navline, 1)

README.write_text(text, encoding="utf-8")

# Redirect P61-P64 publication-surface tests from README to the dedicated page.
for rel in [
    "tests/test_exact_integer_transition_calibration_publication.py",
    "tests/test_heterogeneous_cost_transition_calibration_publication.py",
    "tests/test_exact_heterogeneous_integer_calibration_publication.py",
    "tests/test_fast_heterogeneous_integer_approximation_publication.py",
]:
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    s = s.replace('(ROOT / "README.md").read_text(encoding="utf-8")', f'(ROOT / "{FRONTIER}").read_text(encoding="utf-8")')
    s = s.replace("is_visible_on_main_page", "is_visible_on_calibration_frontier_page")
    p.write_text(s, encoding="utf-8")

# Redirect P65-P69 historical public-record assertions to the dedicated page.
for rel in [
    "tests/test_p65_publication_integration.py",
    "tests/test_p66_publication_integration.py",
    "tests/test_p67_publication_integration.py",
    "tests/test_p68_publication_integration.py",
    "tests/test_p69_publication_integration.py",
]:
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    s = s.replace('"README.md": [', f'"{FRONTIER}": [', 1)
    p.write_text(s, encoding="utf-8")

# P70: keep high-level project frontier metadata on README, move theorem-specific
# visibility requirements to the dedicated calibration page.
p70 = ROOT / "tests/test_p70_publication_integration.py"
s = p70.read_text(encoding="utf-8")
old = '''        "README.md": [
            "version-0.70.0-2563eb",
            "70 proposition-level results",
            "Latest proved extension: P70 exact primal-dual gap decomposition",
            "p70_primal_dual_gap_decomposition.svg",
            "P1 through P70 with explicit dependency branches",
            "# Research at a glance",
            "# Detailed proposition record",
            "docs/quantum_foundations_and_bridge_test.md",
        ],'''
new = '''        "README.md": [
            "version-0.70.0-2563eb",
            "70 proposition-level results",
            "P1 through P70 with explicit dependency branches",
            "# Research at a glance",
            "# Detailed proposition record",
            "docs/quantum_foundations_and_bridge_test.md",
            "docs/calibration_optimization_frontier_p61_p70.md",
        ],
        "docs/calibration_optimization_frontier_p61_p70.md": [
            "Proposition 70: exact primal-dual gap decomposition",
            "p70_primal_dual_gap_decomposition.svg",
            "primal_dual_gap_decomposition.py",
            "test_primal_dual_gap_decomposition.py",
        ],'''
if old not in s:
    raise SystemExit("P70 README requirement block not found")
s = s.replace(old, new, 1)
p70.write_text(s, encoding="utf-8")

# Main-page visual policy: P70 belongs on the technical frontier page, not README.
p = ROOT / "tests/test_main_page_visual_paper.py"
s = p.read_text(encoding="utf-8")
s = s.replace('    "p70_primal_dual_gap_decomposition.svg",\n', '')
anchor = '        "docs/quantum_foundations_and_bridge_test.md",\n'
if '        "docs/calibration_optimization_frontier_p61_p70.md",\n' not in s:
    s = s.replace(anchor, anchor + '        "docs/calibration_optimization_frontier_p61_p70.md",\n', 1)
p.write_text(s, encoding="utf-8")

# Reader-orientation test: stage 7 is now described by function, not theorem ledger.
p = ROOT / "tests/test_readme_research_orientation.py"
s = p.read_text(encoding="utf-8")
s = s.replace('        "P59-P70",\n', '        "Calibration and integer optimization",\n        "docs/calibration_optimization_frontier_p61_p70.md",\n')
p.write_text(s, encoding="utf-8")

# Add a direct structural guard for the new architecture.
guard = ROOT / "tests/test_calibration_frontier_page.py"
guard.write_text('''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nREADME = (ROOT / "README.md").read_text(encoding="utf-8")\nFRONTIER = (ROOT / "docs" / "calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")\n\n\ndef test_main_page_links_frontier_without_embedding_p61_p70_ledger():\n    assert "docs/calibration_optimization_frontier_p61_p70.md" in README\n    assert "Latest proved extension: P70 exact primal-dual gap decomposition" not in README\n    for figure in (\n        "p61_exact_integer_transition_calibration.svg",\n        "p62_heterogeneous_cost_transition_calibration.svg",\n        "p63_exact_heterogeneous_integer_calibration.svg",\n        "p64_fast_heterogeneous_integer_approximation.svg",\n        "p65_lower_bounded_heterogeneous_calibration.svg",\n        "p66_residual_exact_calibration_augmentation.svg",\n        "p67_global_integer_optimality_certificate.svg",\n        "p68_lagrangian_optimality_gap.svg",\n        "p69_dual_optimal_multiplier.svg",\n        "p70_primal_dual_gap_decomposition.svg",\n    ):\n        assert figure not in README\n        assert figure in FRONTIER\n\n\ndef test_frontier_page_is_self_contained_and_auditable():\n    required = (\n        "# P61. Exact integer transition-calibration allocation",\n        "# P62. Heterogeneous-cost transition calibration",\n        "# P63. Exact heterogeneous-cost integer calibration",\n        "# P64. Fast certified heterogeneous integer approximation",\n        "# Proposition 65: lower-bounded heterogeneous calibration",\n        "# Proposition 66: residual-exact calibration augmentation",\n        "# Proposition 67: global integer optimality certificate",\n        "# Proposition 68: Lagrangian optimality gap certificate",\n        "# Proposition 69: certified dual-optimal multiplier search",\n        "# Proposition 70: exact primal-dual gap decomposition",\n        "# Interpretation boundary",\n        "# P61-P70 audit table",\n    )\n    for token in required:\n        assert token in FRONTIER\n''', encoding="utf-8")
