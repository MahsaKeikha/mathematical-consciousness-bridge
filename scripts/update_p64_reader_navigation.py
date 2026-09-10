from pathlib import Path

README = Path("README.md")
text = README.read_text(encoding="utf-8")

old_frontier = "P1 through P60 with explicit dependency branches"
new_frontier = "P1 through P64 with explicit dependency branches"
assert text.count(old_frontier) == 1
text = text.replace(old_frontier, new_frontier, 1)

p60_row = "| integer transition-calibration allocation | [Proposition 60](docs/proposition_60_integer_transition_calibration.md) | hard-budget whole-measurement construction with explicit rounding overhead and target-budget guarantee |"
assert text.count(p60_row) == 1

rows = """| exact integer transition-calibration allocation | [Proposition 61](docs/proposition_61_exact_integer_transition_calibration.md) | exact whole-measurement allocation by decreasing marginal uncertainty gains |
| heterogeneous-cost transition-calibration allocation | [Proposition 62](docs/proposition_62_heterogeneous_cost_transition_calibration.md) | unique continuous allocation when transition observations have unequal per-measurement costs |
| exact heterogeneous-cost integer calibration | [Proposition 63](docs/proposition_63_exact_heterogeneous_integer_calibration.md) | exact Bellman allocation with gcd budget compression and the P62 continuous lower bound |
| fast certified heterogeneous integer approximation | [Proposition 64](docs/proposition_64_fast_heterogeneous_integer_approximation.md) | linear-time floor construction with an explicit approximation certificate relative to P63 |"""

for marker in (
    "docs/proposition_61_exact_integer_transition_calibration.md",
    "docs/proposition_62_heterogeneous_cost_transition_calibration.md",
    "docs/proposition_63_exact_heterogeneous_integer_calibration.md",
    "docs/proposition_64_fast_heterogeneous_integer_approximation.md",
):
    assert marker not in text[text.index("# Reader navigation"):]

text = text.replace(p60_row, p60_row + "\n" + rows, 1)
README.write_text(text, encoding="utf-8")
