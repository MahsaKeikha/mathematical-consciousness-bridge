"""Promote the validated P87 theorem across permanent publication surfaces.

This temporary migration is strict and idempotent. It updates only reader-facing
current-frontier statements, preserves P86 as history, inserts the formal P87
record, and hardens verifier/test expectations before the branch is merged.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def _replace_once(text: str, old: str, new: str, label: str) -> str:
    if old in text:
        return text.replace(old, new, 1)
    if new in text:
        return text
    raise RuntimeError(f"missing P87 migration anchor for {label}: {old!r}")


def _replace_all(text: str, old: str, new: str) -> str:
    return text.replace(old, new)


def _insert_before(text: str, marker: str, block: str, guard: str, label: str) -> str:
    if guard in text:
        return text
    if marker not in text:
        raise RuntimeError(f"missing insertion marker for {label}: {marker!r}")
    return text.replace(marker, block + marker, 1)


def _promote_common_reader_text(text: str) -> str:
    replacements = (
        ("86-result theorem program and current P86 frontier", "87-result theorem program and current P87 frontier"),
        ("86-result theorem program", "87-result theorem program"),
        ("Open all 86 results", "Open all 87 results"),
        ("<strong>86</strong><span>proposition-level results</span>", "<strong>87</strong><span>proposition-level results</span>"),
        ("<strong>P86</strong><span>current theorem frontier</span>", "<strong>P87</strong><span>current theorem frontier</span>"),
        ("The 86 propositions by scientific role", "The 87 propositions by scientific role"),
        ("What the 86 results are doing", "What the 87 results are doing"),
        ("complete 86-result dependency structure", "complete 87-result dependency structure"),
        ("You do not need to read 86 proofs in order", "You do not need to read 87 proofs in order"),
        ("shows how all 86 results connect", "shows how all 87 results connect"),
        ("through Proposition 86", "through Proposition 87"),
        ("Eighty-six results", "Eighty-seven results"),
        ("actual P86 research frontier", "actual P87 research frontier"),
        ("P1-P86 proposition record", "P1-P87 proposition record"),
        ("P1-P86 program map", "P1-P87 program map"),
        ("P73-P86", "P73-P87"),
        ("P75-P86", "P75-P87"),
        ("P78-P86 progressively tighten", "P78-P87 progressively tighten"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def promote_readme() -> None:
    path = "README.md"
    text = _read(path)
    replacements = (
        ("P1-P86 program map, and the current P86 frontier", "P1-P87 program map, and the current P87 frontier"),
        ("| Public theorem frontier | **P86** |", "| Public theorem frontier | **P87** |"),
        ("| Proposition-level results | **86** |", "| Proposition-level results | **87** |"),
        ("P1 to P86 detailed proposition record", "P1 to P87 detailed proposition record"),
        ("**86 proposition-level results**", "**87 proposition-level results**"),
        ("The repository now contains 86 proposition-level results. The theorem frontier is P86.", "The repository now contains 87 proposition-level results. The theorem frontier is P87."),
        ("Current theorem frontier: **P86**", "Current theorem frontier: **P87**"),
        ("P71-P86 formalize", "P71-P87 formalize"),
    )
    for old, new in replacements:
        text = text.replace(old, new)

    block = """
P87 closes the next same-order completeness gap. P86 proves that the minimal non-uniform primitive four-event magnitude pattern `{1,1,1,2}` can expose shared-parameter incompatibility beyond P85. P87 exhausts the entire nonzero primitive integer coefficient box `|c_i| <= 2` at four-event order: 120 sign-normalized coefficient patterns for each of 330 four-event subsets, or **39,600 exact functionals**. On the same exact rational witness, the complete P86 value is `1/192`, while P87 attains `1/96` with coefficients `(1,-1,-2,2)`. Thus

\[
\boxed{L_{85}=0<L_{86}=1/192<L_{87}=1/96.}
\]

![P87 exact bounded primitive four-event projection-parity functional certificate](docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg)

**P87 current-frontier figure.** P87 completes a mathematically declared bounded primitive coefficient family rather than merely increasing proposition number or event order. The result remains conditional on the declared P75 model family and does not identify a latent state with consciousness.

"""
    text = _insert_before(
        text,
        "These results establish a rigorous **test architecture**",
        block,
        "P87 current-frontier figure.",
        "README P87 narrative",
    )
    _write(path, text)


def promote_start_here_markdown() -> None:
    path = "START_HERE.md"
    text = _promote_common_reader_text(_read(path))
    text = text.replace("The repository contains **86 proposition-level results**. The current theorem frontier is **P86**.", "The repository contains **87 proposition-level results**. The current theorem frontier is **P87**.")
    text = text.replace("The 86 results, organized by scientific role", "The 87 results, organized by scientific role")
    text = text.replace("The current frontier: P71-P86 in plain language", "The current frontier: P71-P87 in plain language")
    text = text.replace("P77-P86 as the progression", "P77-P87 as the progression")
    text = text.replace("used in P75-P86", "used in P75-P87")
    text = text.replace("**Proposition frontier:** P86", "**Proposition frontier:** P87")
    text = text.replace("**Proposition-level results:** 86", "**Proposition-level results:** 87")

    block = """
**P85: three-event shared-parameter functionals.** P85 exhausts 660 sign-normalized three-event unit-weight functionals and can detect incompatibility beyond the complete P84 pairwise audit.

**P86: minimally weighted four-event functionals.** P86 introduces the smallest non-uniform primitive magnitude pattern `{1,1,1,2}` across four parity events. Its exact witness gives `L85 = 0 < L86 = 1/192`.

**P87: complete bounded primitive four-event functionals.** P87 keeps the same four-event order but completes every nonzero primitive integer coefficient vector with `|c_i| <= 2`, modulo one global sign. The exact family has 39,600 functionals and the same rational witness gives `L86 = 1/192 < L87 = 1/96`. This is the current theorem frontier.

"""
    text = _insert_before(
        text,
        "---\n\n## How to read any theorem in this repository",
        block,
        "**P87: complete bounded primitive four-event functionals.**",
        "START_HERE P87 frontier",
    )
    _write(path, text)


def promote_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = _read(path)
    text = text.replace("The current documented theorem frontier is **P86**.", "The current documented theorem frontier is **P87**.")
    text = text.replace("P1 through P86", "P1 through P87")
    text = text.replace("P71-P86 return", "P71-P87 return")
    p86_dependency = "&\\text{P86: minimally weighted four-event parity functionals test compatibility beyond the complete P85 triple certificate}"
    if "\\text{P87:" not in text:
        text = _replace_once(
            text,
            p86_dependency,
            p86_dependency + "\\\\\n&\\Downarrow\\\\\n&\\text{P87: bounded primitive four-event parity functionals complete the nonzero coefficient box with |c_i| <= 2}",
            "roadmap dependency P87",
        )

    p84_row = "| [P84](proposition_84_exact_projection_parity_contrast.md) | exact joint parity-event contrasts at common response-coordinate vertices | shared-parameter compatibility test that strictly strengthens P83 | proved conditional computational theorem |"
    if "| [P87](proposition_87_" not in text:
        rows = "\n".join(
            (
                p84_row,
                "| [P85](proposition_85_exact_triple_projection_parity_functional.md) | exact three-event shared-parameter parity functionals | strict strengthening beyond the complete P84 pairwise certificate | proved conditional computational theorem |",
                "| [P86](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md) | minimally weighted four-event parity functionals | strict strengthening beyond the complete P85 triple certificate | proved conditional computational theorem |",
                "| [P87](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md) | complete bounded primitive four-event parity functionals | same-order coefficient-family completion that strictly strengthens P86 | proved conditional computational theorem |",
            )
        )
        text = _replace_once(text, p84_row, rows, "roadmap proposition rows")

    text = text.replace("After P86, the target-side chain", "After P87, the target-side chain")
    text = text.replace("continuation beyond P86", "continuation beyond P87")
    text = text.replace("None of P71-P86", "None of P71-P87")
    text = text.replace("## After P86", "## After P87")
    text = text.replace("Any P87 claim must close", "Any P88 claim must close")

    p87_block = """

## P87: complete bounded primitive four-event parity-functional separation

P87 closes the bounded-coefficient completeness gap left intentionally open by P86. It exhausts every nonzero primitive integer coefficient vector with `|c_i| <= 2` across four distinct canonical even-parity observables, modulo one global sign. There are 120 coefficient patterns per four-event subset and therefore 39,600 exact functionals.

The same multi-affine endpoint argument gives exact rational P75 box intervals, and mass-conservation centering transfers functional mismatch to a full-law L-infinity lower bound. On the exact P86 witness, exhaustive P87 enumeration gives

\[
\boxed{L_{86}=1/192<L_{87}=1/96.}
\]

The stronger functional uses coefficients `(1,-1,-2,2)`, empirical value `-17/24`, exact P75 interval `[-1/2,2]`, gap `5/24`, and centered coefficient norm `20`.

- Proof: [P87](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md)
- Provenance: [p87_equation_provenance.md](p87_equation_provenance.md)
- Figure: [P87 bounded primitive four-event certificate](figures/p87_exact_bounded_primitive_quad_projection_parity.svg)
- Source: [`bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py)
- Tests: [`test_bounded_primitive_quad_projection_parity_functional_separation.py`](../tests/test_bounded_primitive_quad_projection_parity_functional_separation.py)

P87 remains a conditional model-separation theorem for the declared P75 family. It does not identify the latent state with consciousness or close the physical-to-experiential bridge.

"""
    text = _insert_before(
        text,
        "## After P87",
        p87_block,
        "## P87: complete bounded primitive four-event parity-functional separation",
        "roadmap P87 theorem block",
    )
    _write(path, text)


def promote_navigation() -> None:
    path = "docs/research_navigation.md"
    text = _read(path)
    text = text.replace("The current documented theorem frontier is **P86**.", "The current documented theorem frontier is **P87**.")
    text = text.replace("P1 through P86", "P1 through P87")
    text = text.replace("P71-P86 form", "P71-P87 form")
    text = text.replace("dependency structure from P1 through P86", "dependency structure from P1 through P87")

    if "[P87 exact bounded primitive four-event" not in text:
        anchor = "22. [P86 exact minimally weighted four-event projection-parity functional](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md) for the minimally non-uniform four-event shared-parameter audit, 10,560 exact `{1,1,1,2}` weighted functionals, P86 >= P85 dominance, and the strict `L85 = 0 < L86 = 1/192` witness.\n"
        addition = anchor + "23. [P87 exact bounded primitive four-event projection-parity functional](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md) for the complete nonzero primitive coefficient box `|c_i| <= 2`, 39,600 exact four-event functionals, P87 >= P86 dominance, and the strict `L86 = 1/192 < L87 = 1/96` witness.\n"
        text = _replace_once(text, anchor, addition, "navigation recommended P87")

    p86_branch = "| Minimally weighted four-event projection-parity functional separation | P86 | Adds 10,560 exact `{1,1,1,2}` weighted four-event shared-parameter functionals beyond the complete P85 triple-functional certificate | [P86](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md) |"
    if "| Bounded primitive four-event projection-parity functional separation | P87 |" not in text:
        text = _replace_once(
            text,
            p86_branch,
            p86_branch + "\n| Bounded primitive four-event projection-parity functional separation | P87 | Completes all nonzero primitive four-event coefficient vectors with `|c_i| <= 2`, yielding 39,600 exact functionals and a strict strengthening of P86 | [P87](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md) |",
            "navigation P87 branch row",
        )

    if "| P87 | [Exact bounded primitive four-event" not in text:
        marker = "## Reproducibility and review"
        row = "| P87 | [Exact bounded primitive four-event projection-parity functional](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md) | complete bounded primitive four-event parity-functional separation |\n\n"
        text = _insert_before(text, marker, row, "| P87 | [Exact bounded primitive four-event", "navigation proposition index")
    _write(path, text)


def promote_detailed_record() -> None:
    path = "docs/detailed_proposition_record.md"
    text = _read(path)
    if "## Proposition 87:" not in text:
        text += """


## Proposition 87: Exact bounded primitive four-event projection-parity functional certificate

**Scientific question.** Does the P86 `{1,1,1,2}` family exhaust all primitive four-event shared-parameter relations with coefficient magnitudes at most two?

**Result.** No. P87 exhausts every nonzero primitive coefficient vector with `|c_i| <= 2`, modulo one global sign. This gives 120 coefficient patterns per four-event subset and 39,600 exact functionals. On the same exact rational witness used for P86, the complete P86 lower bound is `1/192`, while P87 attains `1/96` with coefficients `(1,-1,-2,2)`, empirical value `-17/24`, exact P75 interval `[-1/2,2]`, gap `5/24`, and centered coefficient norm `20`.

**Boundary.** This is a conditional separation theorem for the declared P75 family. It does not identify a latent state with consciousness or close the physical-to-experiential bridge.

- Proof: [`proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md`](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md)
- Provenance: [`p87_equation_provenance.md`](p87_equation_provenance.md)
- Implementation: [`bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py)
- Tests: [`test_bounded_primitive_quad_projection_parity_functional_separation.py`](../tests/test_bounded_primitive_quad_projection_parity_functional_separation.py)
- Figure: [`p87_exact_bounded_primitive_quad_projection_parity.svg`](figures/p87_exact_bounded_primitive_quad_projection_parity.svg)
"""
    _write(path, text)


def promote_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = _read(path)
    if "# P87 - bounded primitive four-event parity-functional separation" not in text:
        text += """

---

# P87 - bounded primitive four-event parity-functional separation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| `c_i in {-2,-1,1,2}`, `gcd(|c_1|,...,|c_4|)=1` | bounded primitive four-event coefficient family | repository definition | P87 |
| `(4^4 - 2^4)/2 = 120` | sign-normalized primitive coefficient-pattern count | elementary finite counting | P87 provenance |
| `C(11,4) * 120 = 39,600` | complete P87 functional-family size | repository finite construction | P87 |
| `Q(p)=sum_i c_i P(H_{J_i})` | bounded primitive four-event parity functional | repository construction using inherited parity events | P83-P87 |
| exact P75 interval by common endpoint vertices | exact functional model range | elementary multi-affine endpoint derivation | P78/P86/P87 provenance |
| `D(Q)=min_a sum_x |g(x)-a|` | centered full-law transfer denominator | inherited exact transfer construction | P85-P87 |
| `L87(B)=max(L86(B),L_bp4(B))` | current bounded primitive lower-bound hierarchy | repository definition | P87 |
| `L86=1/192 < L87=1/96` | strict exact rational hierarchy witness | repository-original exact construction | P87 proof, implementation, tests |

P87 is a conditional model-separation theorem for the declared P75 family. Its equations do not identify the latent state with consciousness or supply the still-open physical-to-experiential bridge.
"""
    _write(path, text)


def promote_figure_catalog() -> None:
    path = "docs/figure_catalog.md"
    text = _read(path)
    if "p87_exact_bounded_primitive_quad_projection_parity.svg" not in text:
        text += """

## P87 exact bounded primitive four-event projection-parity certificate

**File:** `docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg`

**What it shows.** P87 completes the nonzero primitive four-event coefficient family with `|c_i| <= 2`, increasing the exact audit from P86's 10,560 functionals to 39,600. The displayed strict witness has `L86 = 1/192 < L87 = 1/96`.

**How to read it.** Read left to right: P86's deliberately restricted coefficient family, the P87 bounded primitive completion, then the exact rational witness with empirical value `-17/24`, P75 interval `[-1/2,2]`, gap `5/24`, centered norm `20`, and final lower bound `1/96`.

**Scientific status.** Source-controlled theorem illustration for a proved conditional computational theorem. It is not empirical consciousness evidence.
"""
    _write(path, text)


def promote_claim_matrix() -> None:
    path = "docs/claim_source_matrix.md"
    text = _read(path)
    p86 = "| P86 weighted four-event compatibility | A minimally non-uniform four-event parity functional can strictly strengthen the complete P85 certificate | repository theorem | [P86 proof](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md), [P86 provenance](p86_equation_provenance.md), [`weighted_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/weighted_quad_projection_parity_functional_separation.py), [tests](../tests/test_weighted_quad_projection_parity_functional_separation.py), [figure](figures/p86_exact_minimally_weighted_quad_projection_parity.svg) | `L85 = 0 < L86 = 1/192` is an exact synthetic strict witness inside the declared P75 family |"
    if "| P87 bounded primitive four-event compatibility |" not in text:
        p87 = "| P87 bounded primitive four-event compatibility | Completing every nonzero primitive four-event coefficient vector with `|c_i| <= 2` can strictly strengthen the complete P86 certificate | repository theorem | [P87 proof](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md), [P87 provenance](p87_equation_provenance.md), [`bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py), [tests](../tests/test_bounded_primitive_quad_projection_parity_functional_separation.py), [figure](figures/p87_exact_bounded_primitive_quad_projection_parity.svg) | `L86 = 1/192 < L87 = 1/96` is an exact synthetic strict witness inside the declared P75 family |"
        text = _replace_once(text, p86, p86 + "\n" + p87, "claim matrix P87 row")
    text = text.replace("The current repository contains 86 proposition-level results", "The current repository contains 87 proposition-level results")
    text = text.replace("P86 is the current theorem frontier", "P87 is the current theorem frontier")
    _write(path, text)


def promote_reproducibility() -> None:
    path = "docs/reproducibility.md"
    text = _read(path)
    text = text.replace("The current theorem frontier is **P86**.", "The current theorem frontier is **P87**.")
    text = text.replace("## 12. Reproduce the current P86 implementation checks directly", "## 12. Reproduce the current P87 implementation checks directly")
    text = text.replace("test_weighted_quad_projection_parity_functional_separation.py", "test_bounded_primitive_quad_projection_parity_functional_separation.py")
    _write(path, text)


def promote_website_start() -> None:
    path = "website/start-here.html"
    text = _promote_common_reader_text(_read(path))
    text = text.replace("<strong>P86 is the current exact frontier.</strong>", "<strong>P86 is the previous exact frontier.</strong>")
    p86_para = re.search(r"<p><strong>P86 is the previous exact frontier\.</strong>.*?</p>", text, re.DOTALL)
    if p86_para is None:
        raise RuntimeError("website Start Here P86 paragraph not found")
    if "P87 is the current exact frontier." not in text:
        p87 = "<p><strong>P87 is the current exact frontier.</strong> It exhausts every nonzero primitive integer four-event coefficient vector with |c_i| at most 2, modulo one global sign. The family contains 39,600 exact functionals, and on the same rational witness it gives <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p>\n"
        text = text[: p86_para.end()] + "\n      " + p87 + text[p86_para.end() :]
    text = text.replace(
        'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md">Read P86</a>',
        'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md">Read P87</a>',
    )
    _write(path, text)


def promote_simple_website_pages() -> None:
    for path in ("website/plain-language.html", "website/research-map.html"):
        text = _promote_common_reader_text(_read(path))
        text = text.replace("current P86 frontier", "current P87 frontier")
        if "P87 bounded primitive" not in text:
            block = """
<section class="boundary" id="p87-reader-frontier"><div class="section-head"><p class="eyebrow">Current exact frontier · P87</p><h2>Complete bounded primitive four-event parity audit</h2><p>P87 keeps the same four-event order as P86 but exhausts every nonzero primitive integer coefficient vector with magnitude at most two. The exact family contains 39,600 functionals and the strict rational hierarchy is <strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96</strong>.</p><p>This is a conditional model-separation result for the declared P75 family; the physical-to-experiential bridge remains open.</p></div></section>
"""
            text = _insert_before(text, "</main>", block, "id=\"p87-reader-frontier\"", f"{path} P87 reader block")
        _write(path, text)


def promote_implementation() -> None:
    path = "website/implementation.html"
    text = _promote_common_reader_text(_read(path))
    text = text.replace("P1-P86 proposition record", "P1-P87 proposition record")
    text = text.replace("Stage 06 · P73-P86", "Stage 06 · P73-P87")
    text = text.replace("P73-P86 build a continuous chain", "P73-P87 build a continuous chain")
    if "bounded_primitive_quad_projection_parity_functional_separation.py" not in text:
        anchor = "weighted_quad_projection_parity_functional_separation.py"
        position = text.find(anchor)
        if position == -1:
            raise RuntimeError("implementation page P86 source anchor missing")
        closing = text.find("</a>", position)
        if closing == -1:
            raise RuntimeError("implementation page P86 card closing anchor missing")
        closing += len("</a>")
        p87_card = '\n    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py"><strong>bounded_primitive_quad_projection_parity_functional_separation.py</strong><small>P87 exact 39,600-function bounded primitive four-event separation</small></a>'
        text = text[:closing] + p87_card + text[closing:]
    _write(path, text)


def promote_sources() -> None:
    path = "website/sources.html"
    text = _read(path)
    text = text.replace("Current theorem source · P86", "Previous theorem source · P86")
    if 'id="p87-source"' not in text:
        block = """
<section id="p87-source"><div class="section-head"><p class="eyebrow">Current theorem source · P87</p><h2>Exact bounded primitive four-event projection-parity certificate</h2><p>P87 completes every nonzero primitive four-event coefficient vector with magnitude at most two, yielding 39,600 exact functionals and the strict hierarchy <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md"><h3>Proposition 87</h3><p>Formal statement, exact finite-family count, interval proof, transfer bound, strict witness, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p87_equation_provenance.md"><h3>P87 provenance</h3><p>Separates inherited parity algebra, elementary finite counting and endpoint arguments, and repository-original constructions.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py"><h3>P87 implementation</h3><p>Exact rational exhaustive enumeration of the complete 39,600-function family.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_bounded_primitive_quad_projection_parity_functional_separation.py"><h3>P87 exact tests</h3><p>Family count, exact interval, centered norm, strict witness, dominance, and interpretation-boundary regression tests.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg"><h3>P87 theorem figure</h3><p>Source-controlled visual summary synchronized with the exact theorem and figure publication manifest.</p></a></div></section>

"""
        text = _insert_before(text, '<section id="p86-source">', block, 'id="p87-source"', "sources P87 block")
    _write(path, text)


def promote_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = _read(path)
    text = _replace_once(text, 'CURRENT_FRONTIER = "P86"', 'CURRENT_FRONTIER = "P87"', "verifier frontier")
    text = _replace_once(text, "for number in range(1, 87):", "for number in range(1, 88):", "verifier proposition range")
    if '"docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg",' not in text:
        text = _replace_once(
            text,
            '    "docs/figures/p86_exact_minimally_weighted_quad_projection_parity.svg",',
            '    "docs/figures/p86_exact_minimally_weighted_quad_projection_parity.svg",\n    "docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg",',
            "verifier P87 figure core",
        )
    if '"docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md",' not in text:
        text = _replace_once(
            text,
            '    "docs/p86_equation_provenance.md",',
            '    "docs/p86_equation_provenance.md",\n    "docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md",\n    "docs/p87_equation_provenance.md",',
            "verifier P87 proof core",
        )
    stale_anchor = 'STALE_READER_FRONTIER_MARKERS = (\n'
    p87_stale = (
        '    "86-result theorem program and current P86 frontier",\n'
        '    "Current theorem frontier · P86",\n'
        '    "<strong>86</strong><span>proposition-level results</span>",\n'
        '    "<strong>P86</strong><span>current theorem frontier</span>",\n'
        '    "current P86 frontier",\n'
        '    "actual P86 research frontier",\n'
        '    "What the 86 results are doing",\n'
        '    "shows how all 86 results connect",\n'
        '    "through Proposition 86",\n'
        '    "Eighty-six results",\n'
        '    "The 86 propositions by scientific role",\n'
        '    "complete 86-result dependency structure",\n'
        '    "You do not need to read 86 proofs in order",\n'
    )
    if '    "Current theorem frontier · P86",\n' not in text:
        text = _replace_once(text, stale_anchor, stale_anchor + p87_stale, "verifier stale P86 markers")
    text = text.replace(
        '"p86_exact_minimally_weighted_quad_projection_parity.svg"',
        '"p87_exact_bounded_primitive_quad_projection_parity.svg"',
        1,
    )
    old_block = """    p86 = visual_atlas.index('id=\"p86-frontier\"')
    p84 = visual_atlas.index('id=\"p84-frontier\"')
    p85 = visual_atlas.index('id=\"p85-frontier\"')
    if not p86 < p84 < p85:
        raise RuntimeError("Visual Atlas does not lead with the current P86 figure")
"""
    new_block = """    p87 = visual_atlas.index('id=\"p87-frontier\"')
    p86 = visual_atlas.index('id=\"p86-frontier\"')
    p84 = visual_atlas.index('id=\"p84-frontier\"')
    p85 = visual_atlas.index('id=\"p85-frontier\"')
    if not (p87 < p86 and p87 < p84 and p87 < p85):
        raise RuntimeError("Visual Atlas does not lead with the current P87 figure")
"""
    text = _replace_once(text, old_block, new_block, "verifier atlas P87 ordering")
    _write(path, text)


def promote_reader_tests() -> None:
    path = "tests/test_reader_experience.py"
    text = _read(path)
    text = text.replace("test_first_reader_surfaces_match_p86_frontier", "test_first_reader_surfaces_match_p87_frontier")
    text = text.replace("P86", "P87")
    text = text.replace("86-result", "87-result")
    text = text.replace("86 propositions", "87 propositions")
    text = text.replace("86 proofs", "87 proofs")
    text = text.replace("86 results", "87 results")
    text = text.replace("Eighty-six", "Eighty-seven")
    text = text.replace("range(1, 87)", "range(1, 88)")
    text = text.replace(
        "proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md",
        "proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md",
    )
    text = text.replace(
        "p86_exact_minimally_weighted_quad_projection_parity.svg",
        "p87_exact_bounded_primitive_quad_projection_parity.svg",
    )
    # Restore explicit stale-P86 assertions after broad current-frontier promotion.
    marker = '    assert "Current frontier · P85" not in start\n'
    stale = '    assert "Current theorem frontier · P86" not in start\n'
    if stale not in text and marker in text:
        text = text.replace(marker, marker + stale, 1)
    _write(path, text)


def promote_pages_workflow() -> None:
    path = ".github/workflows/pages.yml"
    text = _read(path)
    text = text.replace("P86", "P87")
    text = text.replace("p86_exact_minimally_weighted_quad_projection_parity.svg", "p87_exact_bounded_primitive_quad_projection_parity.svg")
    text = text.replace("id=\"p86-frontier\"", "id=\"p87-frontier\"")
    text = text.replace("Current frontier · P85", "Current frontier · P86")
    text = text.replace("Current theorem frontier · P85", "Current theorem frontier · P86")
    text = text.replace("styles.css?v=20260913-mobile16-p86", "styles.css?v=20260913-mobile17-p87")
    text = text.replace("reader-experience-v2.css?v=20260913-mobile16-p86", "reader-experience-v2.css?v=20260913-mobile17-p87")
    _write(path, text)


def main() -> None:
    promote_readme()
    promote_start_here_markdown()
    promote_roadmap()
    promote_navigation()
    promote_detailed_record()
    promote_equation_map()
    promote_figure_catalog()
    promote_claim_matrix()
    promote_reproducibility()
    promote_website_start()
    promote_simple_website_pages()
    promote_implementation()
    promote_sources()
    promote_verifier()
    promote_reader_tests()
    promote_pages_workflow()

    # The figure synchronizer derives the gateway, manifest, canonical figure README,
    # homepage current-frontier section, and Visual Atlas current-frontier section.
    from sync_figure_publication import synchronize

    synchronize(check=False)


if __name__ == "__main__":
    main()
