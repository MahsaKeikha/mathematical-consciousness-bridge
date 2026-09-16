"""Regression tests for the journal-facing P1-P100 manuscript package."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "scripts" / "verify_publication_manuscript.py"


def _load_verifier():
    spec = importlib.util.spec_from_file_location("verify_publication_manuscript", VERIFIER)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_publication_manuscript_contracts() -> None:
    verifier = _load_verifier()
    assert verifier.validate() == []


def test_publication_citation_parser_ignores_email_addresses() -> None:
    verifier = _load_verifier()
    text = (
        "Correspondence: mahsa@connectioncare.net. "
        "See [@sethbayne2022theories; @cogitate2025adversarial]."
    )
    assert verifier._citation_keys(text) == {
        "sethbayne2022theories",
        "cogitate2025adversarial",
    }
