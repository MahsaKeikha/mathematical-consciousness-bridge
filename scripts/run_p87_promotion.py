"""Run the guarded P87 publication migration with the current navigation layout."""

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


promotion.promote_navigation = promote_navigation

if __name__ == "__main__":
    promotion.main()
