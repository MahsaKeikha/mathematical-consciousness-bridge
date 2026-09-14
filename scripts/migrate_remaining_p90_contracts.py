from pathlib import Path


def replace_required(path: str, old: str, new: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"missing replacement anchor in {path}: {old}")
    file_path.write_text(text.replace(old, new), encoding="utf-8")


def replace_many(path: str, replacements: list[tuple[str, str]]) -> None:
    for old, new in replacements:
        replace_required(path, old, new)


def main() -> None:
    replace_required("CITATION.cff", 'version: "0.82.0"', "version: 0.82.0")

    replace_many(
        "scripts/verify_repository.py",
        [
            (
                """expected_cff = f'version: "{CURRENT_VERSION}"'""",
                "expected_cff = f'version: {CURRENT_VERSION}'",
            ),
            (
                'if "' + chr(0x2013) + '" in text or "' + chr(0x2014) + '" in text:',
                "if chr(0x2013) in text or chr(0x2014) in text:",
            ),
        ],
    )

    replace_required(
        "website/implementation.html",
        "index.html#p89-frontier",
        "index.html#p90-frontier",
    )
    replace_required(
        "website/research-map.html",
        "index.html#p89-frontier",
        "index.html#p90-frontier",
    )

    replace_required(
        "tests/test_reader_experience.py",
        'assert "for number in range(1, 91):" in verifier',
        'assert "covered: set[int] = set()" in verifier\n    assert "range(1, 91)" in verifier',
    )

    replace_many(
        "tests/test_publication_contract_v2.py",
        [
            ('assert "89" in start', 'assert "90" in start'),
            (
                "does **not** duplicate the full 89 proposition index",
                "does **not** duplicate the full 90 proposition index",
            ),
            ('assert "P89" in text', 'assert "P90" in text'),
            ("## Current theorem frontier: P89", "## Current theorem frontier: P90"),
            ("## Historical theorem frontier: P88", "## Historical theorem frontier: P89"),
            ("## Historical theorem frontier: P87", "## Historical theorem frontier: P88"),
            ("## Current theorem frontier: P88", "## Current theorem frontier: P89"),
            ("Complete P1 to P89 chronology", "Complete P1 to P90 chronology"),
            (
                "P1 through P89 with explicit dependency branches",
                "P1 through P90 with explicit dependency branches",
            ),
            ("range(1, 90)", "range(1, 91)"),
            ('"P89",\n    ):', '"P89",\n        "P90",\n    ):'),
            ('assert "P89" in figures', 'assert "P90" in figures'),
            (
                'assert "p89_complete_linear_parity_duality.svg" in figures',
                'assert "p90_exact_nonlinear_rank_one_separation.svg" in figures',
            ),
            (
                'assert "p89_equation_provenance.md" in equations',
                'assert "p90_equation_provenance.md" in equations',
            ),
            ('assert \'id="p89-source"\' in sources', 'assert \'id="p90-source"\' in sources'),
            ("Current theorem source · P89", "Current theorem source · P90"),
            (
                "proposition_89_complete_linear_parity_duality.md",
                "proposition_90_exact_nonlinear_rank_one_separation.md",
            ),
            ("p89_equation_provenance.md", "p90_equation_provenance.md"),
            ("complete_linear_parity_duality.py", "exact_nonlinear_rank_one_separation.py"),
            (
                "test_complete_linear_parity_duality.py",
                "test_exact_nonlinear_rank_one_separation.py",
            ),
            (
                "p89_complete_linear_parity_duality.svg",
                "p90_exact_nonlinear_rank_one_separation.svg",
            ),
            (
                'assert "Previous theorem source · P88" in sources',
                'assert "Previous theorem source · P89" in sources',
            ),
            ("before_p89", "before_p90"),
            (
                'p89 = overview.index(\'id="p89-frontier"\')',
                'p90 = overview.index(\'id="p90-frontier"\')',
            ),
            ("dashboard < journey < p89", "dashboard < journey < p90"),
            (
                "89</strong><span>proposition-level results",
                "90</strong><span>proposition-level results",
            ),
            (
                "P89 current theorem frontier · v0.82.0",
                "P90 current theorem frontier · v0.82.0",
            ),
            (
                "89 results · current frontier P89",
                "90 results · current frontier P90",
            ),
            (
                "The 89 Research II propositions by scientific role",
                "The 90 Research II propositions by scientific role",
            ),
            (
                "P89</strong><span>current theorem frontier",
                "P90</strong><span>current theorem frontier",
            ),
            ("use_current_p89_state", "use_current_p90_state"),
            ('assert "P89" in research_map', 'assert "P90" in research_map'),
            (
                'assert "P75-P89" in research_map or "P73-P89" in research_map',
                'assert "P75-P90" in research_map or "P73-P90" in research_map',
            ),
            ('id="p89-research-map"', 'id="p90-research-map"'),
            ('assert "5/168" in research_map', 'assert "5/72" in research_map'),
            ("current frontier P89", "current frontier P90"),
            ("current documented frontier, P89", "current documented frontier, P90"),
        ],
    )

    replace_many(
        "tests/test_scholarly_provenance_surface.py",
        [
            ("audited by P75-P89", "audited by P75-P90"),
            (
                "The current repository contains 89 proposition-level results",
                "The current repository contains 90 proposition-level results",
            ),
            (
                "P89 is the current Research II theorem frontier",
                "P90 is the current Research II theorem frontier",
            ),
            (
                "points_to_current_p89_and_previous_p88_p87_p86_records",
                "points_to_current_p90_and_previous_p89_p88_p87_records",
            ),
            (
                """assert 'id="p89-source"' in sources
    assert "Current theorem source · P89" in sources
    assert "5/168" in sources
    assert "proposition_89_complete_linear_parity_duality.md" in sources
    assert "p89_equation_provenance.md" in sources
    assert "complete_linear_parity_duality.py" in sources
    assert "test_complete_linear_parity_duality.py" in sources

    assert 'id="p88-source"' in sources
    assert "Previous theorem source · P88" in sources""",
                """assert 'id="p90-source"' in sources
    assert "Current theorem source · P90" in sources
    assert "5/72" in sources
    assert "proposition_90_exact_nonlinear_rank_one_separation.md" in sources
    assert "p90_equation_provenance.md" in sources
    assert "exact_nonlinear_rank_one_separation.py" in sources
    assert "test_exact_nonlinear_rank_one_separation.py" in sources

    assert 'id="p89-source"' in sources
    assert "Previous theorem source · P89" in sources
    assert "5/168" in sources
    assert "proposition_89_complete_linear_parity_duality.md" in sources
    assert "p89_equation_provenance.md" in sources

    assert 'id="p88-source"' in sources
    assert "Previous theorem source · P88" in sources""",
            ),
            (
                'assert "Current theorem source · P88" not in sources\n    assert "Current theorem source · P87" not in sources',
                'assert "Current theorem source · P89" not in sources\n    assert "Current theorem source · P88" not in sources',
            ),
        ],
    )


if __name__ == "__main__":
    main()
