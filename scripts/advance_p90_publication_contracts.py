"""Advance explicit P89 publication contracts to the P90 frontier.

This script updates only contracts whose purpose is to track the current public
frontier. Historical P89 theorem content remains unchanged.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch(path: str, replacements: tuple[tuple[str, str], ...]) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    original = text
    for old, new in replacements:
        text = text.replace(old, new)
    if text != original:
        target.write_text(text, encoding="utf-8")


def main() -> None:
    patch(
        "scripts/verify_repository.py",
        (
            ('CURRENT_FRONTIER = "P89"', 'CURRENT_FRONTIER = "P90"'),
            (
                '    "docs/figures/p89_complete_linear_parity_duality.svg",',
                '    "docs/figures/p89_complete_linear_parity_duality.svg",\n'
                '    "docs/figures/p90_exact_nonlinear_rank_one_separation.svg",',
            ),
            (
                '    "docs/p89_equation_provenance.md",',
                '    "docs/p89_equation_provenance.md",\n'
                '    "docs/proposition_90_exact_nonlinear_rank_one_separation.md",\n'
                '    "docs/p90_equation_provenance.md",',
            ),
            (
                '    "scripts/promote_p89_public_frontier.py",',
                '    "scripts/promote_p89_public_frontier.py",\n'
                '    "scripts/promote_p90_public_frontier.py",\n'
                '    "scripts/advance_p90_publication_contracts.py",',
            ),
            (
                '    "tests/test_figure_publication_sync.py",',
                '    "tests/test_figure_publication_sync.py",\n'
                '    "tests/test_exact_nonlinear_rank_one_separation.py",',
            ),
            ("for number in range(1, 90):", "for number in range(1, 91):"),
        ),
    )

    patch(
        "scripts/synchronize_research_three_website.py",
        (
            ("P89_HOME_MARKER", "CURRENT_HOME_MARKER"),
            (
                'CURRENT_HOME_MARKER = "<!-- current-frontier-home: P89 -->"',
                'CURRENT_HOME_MARKER = "<!-- current-frontier-home: P90 -->"',
            ),
        ),
    )

    patch(
        "scripts/prepare_website.py",
        (
            ("P89_HOME_MARKER", "CURRENT_HOME_MARKER"),
            (
                '"p89_complete_linear_parity_duality.svg"',
                '"p90_exact_nonlinear_rank_one_separation.svg"',
            ),
            (
                'CURRENT_RECORD_TEXT = "Current record:</strong> 89 proposition-level results through P89"',
                'CURRENT_RECORD_TEXT = "Current record:</strong> 90 proposition-level results through P90"',
            ),
            ("internally consistent with P89", "internally consistent with P90"),
            ("current P89 theorem figure", "current P90 theorem figure"),
            ("bundled P89 theorem figure", "bundled P90 theorem figure"),
            ('id="p89-frontier"', 'id="p90-frontier"'),
            ("not synchronized to 89/P89", "not synchronized to 90/P90"),
            ("pre-P89 reader text", "pre-P90 reader text"),
        ),
    )

    patch(
        "tests/test_reader_experience.py",
        (
            (
                "test_repository_verifier_tracks_p89_and_all_89_propositions",
                "test_repository_verifier_tracks_p90_and_all_90_propositions",
            ),
            ('CURRENT_FRONTIER = "P89"', 'CURRENT_FRONTIER = "P90"'),
            ("for number in range(1, 90):", "for number in range(1, 91):"),
            (
                '"docs/proposition_89_complete_linear_parity_duality.md"',
                '"docs/proposition_90_exact_nonlinear_rank_one_separation.md"',
            ),
            ('id="p89-frontier"', 'id="p90-frontier"'),
        ),
    )

    patch(
        "tests/test_figure_publication_sync.py",
        (
            ('P89_FIGURE = "p89_complete_linear_parity_duality.svg"',
             'P90_FIGURE = "p90_exact_nonlinear_rank_one_separation.svg"'),
            ('== "P89"', '== "P90"'),
            ("P89_FIGURE", "P90_FIGURE"),
            ("tracks_p89", "tracks_p90"),
            ("P71-P89", "P71-P90"),
            ("Current theorem frontier: P89", "Current theorem frontier: P90"),
            ("L88 = 1/64 < L89 = 5/168", "L89 = 5/168 < L90 = 5/72"),
            ('"| P89 |"', '"| P90 |"'),
            ("leads_with_p89", "leads_with_p90"),
            ('p89 = text.index(\'id="p89-frontier"\')', 'p90 = text.index(\'id="p90-frontier"\')'),
            ("assert p89 < p88 < p87", "assert p90 < p89 < p88"),
            ("current = text[p89:p88]", "current = text[p90:p89]"),
            ("Current theorem frontier · P89", "Current theorem frontier · P90"),
            ('"5/168" in current', '"5/72" in current'),
            ('"complete_linear_parity_duality.py" in current', '"exact_nonlinear_rank_one_separation.py" in current'),
            ('"test_complete_linear_parity_duality.py" in current', '"test_exact_nonlinear_rank_one_separation.py" in current'),
            ("Previous theorem frontier · P88", "Previous theorem frontier · P89"),
            ('p89 = text.index(\'id="p89-frontier"\')', 'p90 = text.index(\'id="p90-frontier"\')'),
            ("assert research_i < p89 < research_iii < reader_paths", "assert research_i < p90 < research_iii < reader_paths"),
            ("current = text[p89:research_iii]", "current = text[p90:research_iii]"),
            ("text[research_i:p89]", "text[research_i:p90]"),
            ("The 89 results form several dependency branches.", "The 90 results form several dependency branches."),
            ("all 89 propositions", "all 90 propositions"),
            ("89 results · current frontier P89", "90 results · current frontier P90"),
            ("The 89 Research II propositions by scientific role", "The 90 Research II propositions by scientific role"),
            ("bundles_exact_commit_p89_figure", "bundles_exact_commit_p90_figure"),
            ("deployed_p89", "deployed_p90"),
            ('id="p89-frontier"', 'id="p90-frontier"'),
            ("p89 = home.index", "p90 = home.index"),
            ("research_i < p89 < research_iii", "research_i < p90 < research_iii"),
        ),
    )

    patch(
        ".github/workflows/figures.yml",
        (("docs/figures/p89_complete_linear_parity_duality.svg", "docs/figures/p90_exact_nonlinear_rank_one_separation.svg"),),
    )

    patch(
        ".github/workflows/validate-research-three-website.yml",
        (
            ("Explore all 89 results", "Explore all 90 results"),
            ("89 proposition-level results through P89", "90 proposition-level results through P90"),
            ("Current theorem frontier · P89", "Current theorem frontier · P90"),
            ('id="p89-frontier"', 'id="p90-frontier"'),
            ("current-frontier-home: P89", "current-frontier-home: P90"),
            ("89 results · current frontier P89", "90 results · current frontier P90"),
            ("The 89 Research II propositions by scientific role", "The 90 Research II propositions by scientific role"),
            ("P89: What is the strongest possible real linear certificate", "P90: How much stronger is the actual nonlinear P75 image than its complete linear envelope?"),
            ("p89-research-map", "p90-research-map"),
            ("index.html#p89-frontier", "index.html#p90-frontier"),
            ("current-frontier-visual: P89", "current-frontier-visual: P90"),
            ("p89_complete_linear_parity_duality.svg", "p90_exact_nonlinear_rank_one_separation.svg"),
            ("<strong>89</strong><span>proposition-level results</span>", "<strong>90</strong><span>proposition-level results</span>"),
            ("<strong>P89</strong><span>current theorem frontier</span>", "<strong>P90</strong><span>current theorem frontier</span>"),
        ),
    )

    print("advanced explicit P90 publication contracts")


if __name__ == "__main__":
    main()
