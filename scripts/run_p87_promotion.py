"""Run the guarded P87 publication migration with current reader layouts."""

from __future__ import annotations

import promote_p87_publication as promotion


def promote_navigation() -> None:
    path = "docs/research_navigation.md"
    text = promotion._read(path)
    text = text.replace(
        "The current documented theorem frontier is **P86**.",
        "The current documented theorem frontier is **P87**.",
    )
    text = text.replace("P1 through P86", "P1 through P87")
    text = text.replace("P71-P86 form", "P71-P87 form")
    text = text.replace(
        "dependency structure from P1 through P86",
        "dependency structure from P1 through P87",
    )

    recommended_anchor = (
        "22. [P86 exact minimally weighted four-event projection-parity functional]"
        "(proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md) "
        "for the minimally non-uniform four-event shared-parameter audit, 10,560 "
        "exact `{1,1,1,2}` weighted functionals, P86 >= P85 dominance, and the strict "
        "`L85 = 0 < L86 = 1/192` witness.\n"
    )
    if "[P87 exact bounded primitive four-event" not in text:
        addition = recommended_anchor + (
            "23. [P87 exact bounded primitive four-event projection-parity functional]"
            "(proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md) "
            "for the complete nonzero primitive coefficient box `|c_i| <= 2`, 39,600 "
            "exact four-event functionals, P87 >= P86 dominance, and the strict "
            "`L86 = 1/192 < L87 = 1/96` witness.\n"
        )
        text = promotion._replace_once(
            text,
            recommended_anchor,
            addition,
            "navigation recommended P87",
        )

    p86_branch = (
        "| Minimally weighted four-event projection-parity functional separation | P86 | "
        "Adds 10,560 exact `{1,1,1,2}` weighted four-event shared-parameter functionals "
        "beyond the complete P85 triple-functional certificate | "
        "[P86](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md) |"
    )
    if "| Bounded primitive four-event projection-parity functional separation | P87 |" not in text:
        p87_branch = (
            p86_branch
            + "\n| Bounded primitive four-event projection-parity functional separation | P87 | "
            "Completes all nonzero primitive four-event coefficient vectors with `|c_i| <= 2`, "
            "yielding 39,600 exact functionals and a strict strengthening of P86 | "
            "[P87](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md) |"
        )
        text = promotion._replace_once(
            text,
            p86_branch,
            p87_branch,
            "navigation P87 branch row",
        )

    text = text.replace(
        "The current theorem frontier is P85, but the physical-to-experiential bridge itself remains open.",
        "The current theorem frontier is P87, but the physical-to-experiential bridge itself remains open.",
    )
    frontier_p85 = (
        "| P85 | exact three-event parity-functional shared-parameter constraints | "
        "[P85](proposition_85_exact_triple_projection_parity_functional.md) |"
    )
    if "| P87 | complete bounded primitive four-event" not in text:
        frontier_rows = "\n".join(
            (
                frontier_p85,
                "| P86 | minimally weighted four-event shared-parameter constraints | [P86](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md) |",
                "| P87 | complete bounded primitive four-event shared-parameter constraints | [P87](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md) |",
            )
        )
        text = promotion._replace_once(
            text,
            frontier_p85,
            frontier_rows,
            "navigation frontier resources",
        )

    text = text.replace(
        "**Previous frontier provenance:** [P85 equation and provenance record](p85_equation_provenance.md).",
        "**Previous frontier provenance:** [P86 equation and provenance record](p86_equation_provenance.md).",
    )
    text = text.replace(
        "**Current frontier provenance:** [P86 equation and provenance record](p86_equation_provenance.md).",
        "**Current frontier provenance:** [P87 equation and provenance record](p87_equation_provenance.md).",
    )
    text = text.replace("## P86 current frontier record", "## P86 previous frontier record")
    text = text.replace(
        "P85 remains the previous theorem frontier and its proof, figure, implementation, and exact witness remain part of the permanent scientific record.",
        "P86 remains the previous theorem frontier and its proof, figure, implementation, and exact witness remain part of the permanent scientific record.",
    )

    if "## P87 current frontier record" not in text:
        text += """


## P87 current frontier record

| Proposition | Direct proof | Main role |
| --- | --- | --- |
| P87 | [Exact bounded primitive four-event projection-parity functional](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md) | 39,600 exact bounded primitive four-event shared-parameter functionals; strict `L86 = 1/192 < L87 = 1/96` hierarchy witness |

- [P87 equation and provenance record](p87_equation_provenance.md)
- [P87 implementation](../src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py)
- [P87 regression tests](../tests/test_bounded_primitive_quad_projection_parity_functional_separation.py)
- [P87 theorem figure](figures/p87_exact_bounded_primitive_quad_projection_parity.svg)

P87 is the current theorem frontier. The physical-to-experiential bridge remains open.
"""

    promotion._write(path, text)


def promote_research_map_current_frontier() -> None:
    path = "website/research-map.html"
    text = promotion._read(path)
    text = text.replace("P71-P86", "P71-P87")
    text = text.replace(
        "culminating in P86 exact minimally weighted four-event shared-parameter parity-functional separation.",
        "culminating in P87 exact bounded primitive four-event shared-parameter parity-functional separation.",
    )
    text = text.replace(
        "and P86 adds exact minimally weighted four-event functionals with primitive coefficient magnitudes {1,1,1,2} beyond the complete P85 certificate.",
        "P86 adds exact minimally weighted four-event functionals with primitive coefficient magnitudes {1,1,1,2}, while P87 completes every nonzero primitive four-event coefficient vector with magnitude at most two and strictly strengthens the P86 certificate.",
    )
    text = text.replace("index.html#p86-frontier", "index.html#p87-frontier")
    text = text.replace(
        "Continue to the current P86 frontier",
        "Continue to the current P87 frontier",
    )
    text = text.replace(
        "P77-P86: from full-law rejection to exact dependency-aware certification",
        "P77-P87: from full-law rejection to exact dependency-aware certification",
    )
    if "index.html#p87-frontier" not in text:
        raise RuntimeError("Research Map did not acquire the P87 current-frontier link")
    if "Continue to the current P86 frontier" in text:
        raise RuntimeError("Research Map retained the stale P86 current-frontier label")
    promotion._write(path, text)


def promote_regression_tests() -> None:
    reader_path = "tests/test_reader_experience.py"
    reader = promotion._read(reader_path)
    reader = reader.replace("through Proposition 86", "through Proposition 87")
    reader = reader.replace(
        '    assert "<strong>86</strong>" in research_map\n',
        '    assert "<strong>87</strong>" in research_map\n',
    )
    promotion._write(reader_path, reader)

    scholarly_path = "tests/test_scholarly_provenance_surface.py"
    scholarly = promotion._read(scholarly_path)
    old_block = '''def test_sources_page_points_to_current_p86_audit_record() -> None:
    sources = _read("website/sources.html")
    assert 'id="p86-source"' in sources
    assert "Current theorem source · P86" in sources
    assert "L85 = 0 &lt; L86 = 1/192" in sources
    assert "proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md" in sources
    assert "p86_equation_provenance.md" in sources
    assert "weighted_quad_projection_parity_functional_separation.py" in sources
    assert "test_weighted_quad_projection_parity_functional_separation.py" in sources
    assert "claim_source_matrix.md" in sources
    assert "Claim-to-source matrix" in sources
'''
    new_block = '''def test_sources_page_points_to_current_p87_and_previous_p86_audit_records() -> None:
    sources = _read("website/sources.html")
    assert 'id="p87-source"' in sources
    assert "Current theorem source · P87" in sources
    assert "L86 = 1/192 &lt; L87 = 1/96" in sources
    assert "proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md" in sources
    assert "p87_equation_provenance.md" in sources
    assert "bounded_primitive_quad_projection_parity_functional_separation.py" in sources
    assert "test_bounded_primitive_quad_projection_parity_functional_separation.py" in sources
    assert 'id="p86-source"' in sources
    assert "Previous theorem source · P86" in sources
    assert "L85 = 0 &lt; L86 = 1/192" in sources
    assert "claim_source_matrix.md" in sources
    assert "Claim-to-source matrix" in sources
'''
    scholarly = promotion._replace_once(
        scholarly,
        old_block,
        new_block,
        "scholarly P87 current-source regression",
    )
    scholarly = scholarly.replace(
        '        "P86 mathematical backbone",\n',
        '        "P86 mathematical backbone",\n        "P87 bounded primitive four-event compatibility",\n        "L86 = 1/192 < L87 = 1/96",\n',
    )
    promotion._write(scholarly_path, scholarly)

    orientation_path = "tests/test_website_research_orientation.py"
    orientation = promotion._read(orientation_path)
    orientation = orientation.replace(
        "Eighty-six results, one dependency-aware scientific program",
        "Eighty-seven results, one dependency-aware scientific program",
    )
    orientation = orientation.replace("P73-P86", "P73-P87")
    orientation = orientation.replace("through Proposition 86", "through Proposition 87")
    orientation = orientation.replace(
        "test_research_map_presents_p77_through_p86_with_p84_history",
        "test_research_map_presents_p77_through_p87_with_p84_history",
    )
    orientation = orientation.replace("P77-P86:", "P77-P87:")
    orientation = orientation.replace("p86_navigation", "p87_navigation")
    orientation = orientation.replace("index.html#p86-frontier", "index.html#p87-frontier")
    orientation = orientation.replace(
        "Continue to the current P86 frontier",
        "Continue to the current P87 frontier",
    )
    p86_assert = '    assert "P86 adds exact minimally weighted four-event functionals" in text\n'
    if '    assert \'id="p87-reader-frontier"\' in text\n' not in orientation:
        orientation = orientation.replace(
            p86_assert,
            p86_assert
            + '    assert \'id="p87-reader-frontier"\' in text\n'
            + '    assert "39,600" in text\n'
            + '    assert "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96" in text\n',
            1,
        )
    promotion._write(orientation_path, orientation)


promotion.promote_navigation = promote_navigation

if __name__ == "__main__":
    promotion.main()
    promote_research_map_current_frontier()
    promote_regression_tests()
