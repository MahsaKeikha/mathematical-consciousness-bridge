# Executable research quick start

This page is for readers who want to run the repository instead of only reading it.

## Strongest reproducibility audit

For the exact v0.81.0 reference environment, use Python 3.12.14 and run:

```bash
python -m pip install -e ".[dev]"
python -m pip install -r requirements-reproducibility.txt
python scripts/reproducibility_audit.py
```

Or, after installation:

```bash
make reproduce
```

This is stronger than a normal test run: it runs the test/static checks, imports the package modules, rebuilds the generated atlases, reapplies figure documentation metadata, and requires two consecutive rebuilds to leave a clean Git tree.

## Fast compatibility validation

```bash
make check
```

The compatibility path is also exercised in CI on Python 3.10, 3.11, and 3.12.

## Regenerate the computational figures

```bash
python scripts/generate_all_figures.py
```

This regenerates:

```text
docs/figures/quantitative/
docs/figures/quantum/
```

and then validates the complete SVG tree.

## What each active script does

| Script | Purpose | Output or check |
| --- | --- | --- |
| `reproducibility_audit.py` | Exact reference audit | Runs tests/static checks, imports modules, regenerates figures twice, and requires a byte-clean Git tree |
| `generate_all_figures.py` | Canonical figure entry point | Regenerates computational atlases, reapplies SVG documentation metadata, and validates all SVG assets |
| `generate_quantitative_atlas.py` | Quantitative physics and mathematics atlas | `docs/figures/quantitative/` plus manifest |
| `generate_quantum_foundations_atlas.py` | Quantum foundations atlas | `docs/figures/quantum/` plus manifest |
| `verify_repository.py` | Repository-wide consistency audit | Checks release/frontier markers, proposition coverage, principal links, workflows, source and test surfaces |
| `conceptual_figure_records.py` | Structured records for theorem and conceptual visuals | Supports figure documentation and auditability |
| `quantum_figure_records.py` | Structured quantum figure records | Supports quantum figure documentation |
| `enrich_figure_documentation.py` | Figure documentation maintenance | Updates documentation surfaces from structured figure records |
| `normalize_typography.py` | Public-text maintenance utility | Enforces repository typography policy |

## Follow one theorem end to end

For the current P81 frontier, inspect these files in order:

```text
docs/proposition_81_projection_event_model_separation.md
src/consciousness_bridge/projection_event_model_separation.py
tests/test_projection_event_model_separation.py
docs/p81_equation_provenance.md
docs/figures/p81_projection_event_model_separation.svg
tests/test_p81_figure_geometry.py
```

This is the repository's intended audit pattern:

```text
scientific question
-> declared assumptions
-> theorem statement
-> proof
-> implementation
-> numerical and regression tests
-> equation provenance
-> visual explanation
-> explicit scientific boundary
```

## Where to go next

- Reader orientation: [`START_HERE.md`](../START_HERE.md)
- Full reproducibility guide: [`docs/reproducibility.md`](../docs/reproducibility.md)
- Visual gateway: [`figures/README.md`](../figures/README.md)
- Current visual frontier: [`figures/CURRENT_FRONTIER.md`](../figures/CURRENT_FRONTIER.md)
- Theorem dependency map: [`docs/theorem_roadmap.md`](../docs/theorem_roadmap.md)
- Complete research navigation: [`docs/research_navigation.md`](../docs/research_navigation.md)

A passing script or test certifies the mathematical or software property encoded by that check. It does not by itself constitute empirical evidence that consciousness has been derived from physics.
