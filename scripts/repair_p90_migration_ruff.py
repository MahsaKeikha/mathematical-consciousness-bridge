"""Normalize adjacent string literals in the P90 publication migration script."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "advance_p90_publication_contracts.py"


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    replacements = (
        (
            "'    \"docs/figures/p89_complete_linear_parity_duality.svg\",\\n'\n                '    \"docs/figures/p90_exact_nonlinear_rank_one_separation.svg\",'",
            "'    \"docs/figures/p89_complete_linear_parity_duality.svg\",\\n    \"docs/figures/p90_exact_nonlinear_rank_one_separation.svg\",'",
        ),
        (
            "'    \"docs/p89_equation_provenance.md\",\\n'\n                '    \"docs/proposition_90_exact_nonlinear_rank_one_separation.md\",\\n'\n                '    \"docs/p90_equation_provenance.md\",'",
            "'    \"docs/p89_equation_provenance.md\",\\n    \"docs/proposition_90_exact_nonlinear_rank_one_separation.md\",\\n    \"docs/p90_equation_provenance.md\",'",
        ),
        (
            "'    \"scripts/promote_p89_public_frontier.py\",\\n'\n                '    \"scripts/promote_p90_public_frontier.py\",\\n'\n                '    \"scripts/advance_p90_publication_contracts.py\",'",
            "'    \"scripts/promote_p89_public_frontier.py\",\\n    \"scripts/promote_p90_public_frontier.py\",\\n    \"scripts/advance_p90_publication_contracts.py\",'",
        ),
        (
            "'    \"tests/test_figure_publication_sync.py\",\\n'\n                '    \"tests/test_exact_nonlinear_rank_one_separation.py\",'",
            "'    \"tests/test_figure_publication_sync.py\",\\n    \"tests/test_exact_nonlinear_rank_one_separation.py\",'",
        ),
    )
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
    TARGET.write_text(text, encoding="utf-8")
    print("P90 migration Ruff string literals normalized")


if __name__ == "__main__":
    main()
