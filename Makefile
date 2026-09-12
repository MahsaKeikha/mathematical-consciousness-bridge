.PHONY: install test lint figures figures-check verify check

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

verify:
	$(PYTHON) scripts/verify_repository.py

check: test lint figures-check verify
