# Contributing

Thank you for reviewing or contributing to the **Mathematical Consciousness Bridge** research repository.

The project combines mathematical proofs, executable certificates, finite-sample statistics, optimization, and publication-quality documentation. Contributions are expected to preserve the distinction among **proved mathematics**, **modeling assumptions**, **numerical computation**, **empirical evidence**, and **open physical-to-experiential interpretation**.

For a first orientation, read [START_HERE.md](START_HERE.md). For exact setup and verification commands, use the [Reproducibility Guide](docs/reproducibility.md).

---

## Development setup

```bash
git clone https://github.com/MahsaKeikha/mathematical-consciousness-bridge.git
cd mathematical-consciousness-bridge
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Supported Python versions are **3.10, 3.11, and 3.12**.

---

## Before opening a pull request

Run the complete local check:

```bash
make check
```

If `make` is unavailable, run:

```bash
python -m pytest
python -m ruff check .
python scripts/generate_all_figures.py --validate-only
python scripts/verify_repository.py
```

If your change affects the generated atlases, also run:

```bash
python scripts/generate_all_figures.py
```

Then inspect the changed SVGs and manifests before committing them.

---

## Standards for a new proposition

A mature proposition should normally include, where applicable:

1. a precise scientific question or gap;
2. explicitly declared assumptions;
3. a formal theorem/proposition statement;
4. a proof with inequality directions and edge cases stated clearly;
5. an implementation when the result is computational;
6. regression/unit tests, including exact witnesses where possible;
7. an equation/provenance record distinguishing standard ingredients from repository-original results;
8. a theorem figure or visual explanation when it materially improves comprehension;
9. integration into the theorem roadmap, proposition record, research navigation, and figure catalog;
10. an explicit scientific-boundary statement describing what stronger conclusion is **not** justified.

Proposition numbering records development chronology, not necessarily a single linear dependency chain.

---

## Mathematical and scientific writing standard

Prefer statements that can be audited. In particular:

- state the model before stating the conclusion;
- distinguish necessary conditions from sufficient conditions;
- distinguish lower bounds from upper bounds;
- do not turn a local numerical fit into a global optimization claim;
- do not turn non-rejection into model validation;
- do not identify a latent statistical state with consciousness without an independent semantic and empirical argument;
- do not treat physical or quantum completeness as experiential completeness;
- keep imported standard mathematics, repository-specific definitions, and novel theorem content visibly separate.

The [Equation and Citation Map](docs/equation_and_citation_map.md) and proposition-level provenance records are the reference style for this separation.

---

## Tests

Tests live under `tests/` and are run by GitHub Actions on Python 3.10, 3.11, and 3.12.

A good theorem test suite should include more than a happy-path numerical example. Depending on the result, include:

- exact algebraic identities;
- boundary and degenerate cases;
- monotonicity or dominance checks;
- strict-improvement witnesses;
- invalid-input behavior;
- comparison against brute force on small instances;
- direction-of-inequality regression tests;
- figure geometry/content guards when a figure encodes theorem claims;
- publication consistency checks when a release frontier changes.

Run a focused test with:

```bash
python -m pytest tests/test_name.py
```

Run the complete suite with:

```bash
python -m pytest
```

---

## Figures

The repository has two visual classes.

### Computational atlases

These are generated from code:

```bash
python scripts/generate_all_figures.py
```

The canonical generators are:

- `scripts/generate_quantitative_atlas.py`
- `scripts/generate_quantum_foundations_atlas.py`

Their SVG outputs and manifests live under:

- `docs/figures/quantitative/`
- `docs/figures/quantum/`

### Theorem and architecture SVGs

These are source-controlled publication diagrams under `docs/figures/`. They communicate theorem structure, dependency, assumptions, inequalities, and scientific status. They are validated by the repository figure checks and should not be presented as if they were simulated empirical outputs.

See the [Figure Catalog](docs/figure_catalog.md), [Figure Style Guide](docs/figure_style_guide.md), and [Figure Caption and Description Standard](docs/figure_caption_and_description_standard.md).

---

## Documentation changes

When a theorem frontier, release version, or major scientific branch changes, check at minimum:

- `README.md`
- `START_HERE.md`
- `docs/research_navigation.md`
- `docs/theorem_roadmap.md`
- `docs/detailed_proposition_record.md`
- `docs/equation_and_citation_map.md`
- `docs/figure_catalog.md`
- `CITATION.md`
- `CITATION.cff`
- `CHANGELOG.md`
- `website/index.html`
- `website/research-map.html`
- `website/visual-atlas.html`

Run `python scripts/verify_repository.py` to catch core release/frontier inconsistencies and broken local links on the principal reader surfaces.

---

## Pull-request scope

Prefer focused pull requests with a clear scientific or publication purpose. A PR description should state:

- what mathematical or documentation gap it closes;
- which assumptions are required;
- what files constitute the proof/implementation/test record;
- what validation was run;
- what remains scientifically open.

The goal is for an external reviewer to understand the change without reconstructing the development history from commits.
