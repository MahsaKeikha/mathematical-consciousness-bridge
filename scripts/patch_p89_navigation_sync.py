"""Temporary self-removing repair for the P89 navigation synchronizer."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "synchronize_p89_reader_frontier_phrases.py"

old = '''    audit_pattern = re.compile(r"For P88:\\n\\n\\| Audit surface \\| Canonical route \\|\\n\\| --- \\| --- \\|\\n.*?(?=\\n\\n|\\Z)", re.DOTALL)
    audit = \'\'\'For P89:\\n\\n| Audit surface | Canonical route |\\n| --- | --- |\\n| Direct theorem | [P89 proposition](proposition_89_complete_linear_parity_duality.md) |\\n| Equation and method provenance | [P89 provenance](p89_equation_provenance.md) |\\n| Implementation | [`complete_linear_parity_duality.py`](../src/consciousness_bridge/complete_linear_parity_duality.py) |\\n| Regression tests | [`test_complete_linear_parity_duality.py`](../tests/test_complete_linear_parity_duality.py) |\\n| Theorem figure | [P89 complete-linear certificate](figures/p89_complete_linear_parity_duality.svg) |\'\'\'
'''

new = '''    audit_pattern = re.compile(
        r"For P88:\\n\\n\\| What you want \\| Direct link \\|\\n\\| --- \\| --- \\|\\n.*?(?=\\n\\nP88 is a conditional model separation result)",
        re.DOTALL,
    )
    audit = \'\'\'For P89:\\n\\n| What you want | Direct link |\\n| --- | --- |\\n| The theorem and proof | [P89 proposition](proposition_89_complete_linear_parity_duality.md) |\\n| Equation and method provenance | [P89 provenance](p89_equation_provenance.md) |\\n| Implementation | [`complete_linear_parity_duality.py`](../src/consciousness_bridge/complete_linear_parity_duality.py) |\\n| Regression tests | [`test_complete_linear_parity_duality.py`](../tests/test_complete_linear_parity_duality.py) |\\n| Figure | [P89 complete-linear certificate](figures/p89_complete_linear_parity_duality.svg) |\\n| Repository reproduction | [Reproducibility Guide](reproducibility.md) |\'\'\'
'''

text = TARGET.read_text(encoding="utf-8")
if old not in text:
    if new not in text:
        raise RuntimeError("expected P89 navigation synchronizer block was not found")
else:
    TARGET.write_text(text.replace(old, new, 1), encoding="utf-8")

# The helper is only needed to repair the migration source once.
Path(__file__).unlink()
print("[repair] aligned P89 navigation synchronizer with canonical navigation table")
