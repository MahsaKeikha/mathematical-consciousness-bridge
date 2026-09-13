.PHONY: install test lint figures figures-check frontier-check publication-check website-check verify check reproduce

PYTHON ?= python

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m ruff check .

figures:
	$(PYTHON) scripts/generate_all_figures.py

figures-check:
	$(PYTHON) scripts/generate_all_figures.py --validate-only

frontier-check:
	$(PYTHON) scripts/verify_frontier_publication.py

publication-check:
	$(PYTHON) scripts/sync_figure_publication.py --check

website-check:
	$(PYTHON) scripts/prepare_website.py --source website --output .site-check
	rm -rf .site-check

verify: frontier-check publication-check
	$(PYTHON) scripts/verify_repository.py

check: test lint figures-check verify website-check

reproduce:
	$(PYTHON) scripts/reproducibility_audit.py
