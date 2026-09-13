"""Finalize P88 reader/publication consistency after guarded promotion.

This helper is intentionally one-shot. The promotion workflow runs it only after
``promote_p88_public_frontier.py`` has formalized Proposition 88. It repairs
reader surfaces that historically encoded P87 literally, adds the required SVG
scientific-status metadata, and leaves the repository ready for figure-manifest
regeneration and the full regression suite.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P88_PROOF = "proposition_88_heldout_selected_parity_functional_certification.md"
P88_FIGURE = "p88_heldout_selected_parity_functional_certification.svg"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace(path: str, pairs: tuple[tuple[str, str], ...]) -> None:
    text = read(path)
    for old, new in pairs:
        text = text.replace(old, new)
    write(path, text)


def update_readme() -> None:
    replace(
        "README.md",
        (
            (
                "| Equation-driven quantitative figures | **71** |",
                "| Equation-driven quantitative figures | **72** |",
            ),
            (
                "P1 through P87 with explicit dependency branches",
                "P1 through P88 with explicit dependency branches",
            ),
            ("P1 through P87", "P1 through P88"),
        ),
    )


def update_svg_accessibility() -> None:
    path = f"docs/figures/{P88_FIGURE}"
    text = read(path)
    if "Scientific status:" not in text:
        anchor = (
            "The theorem is box-specific unless a separate global covering argument "
            "is supplied and does not identify the latent state with consciousness."
        )
        replacement = (
            "Scientific status: proved conditional finite-sample theorem under the "
            "declared discovery/validation independence and frozen-box assumptions. "
            + anchor
        )
        if anchor not in text:
            raise RuntimeError("P88 SVG description anchor not found")
        text = text.replace(anchor, replacement, 1)
    if text.count("Scientific status:") != 1:
        raise RuntimeError("P88 SVG must contain exactly one scientific-status boundary")
    write(path, text)


def update_start_here() -> None:
    path = "website/start-here.html"
    text = read(path)
    replacements = (
        ("87-result theorem program", "88-result theorem program"),
        ("current P87 frontier", "current P88 frontier"),
        ("Open all 87 results", "Open all 88 results"),
        (
            "<strong>87</strong><span>proposition-level results</span>",
            "<strong>88</strong><span>proposition-level results</span>",
        ),
        (
            "<strong>P87</strong><span>current theorem frontier</span>",
            "<strong>P88</strong><span>current theorem frontier</span>",
        ),
        ("P75-P87", "P75-P88"),
        ("The 87 propositions by scientific role", "The 88 propositions by scientific role"),
        ("You do not need to read 87 proofs in order", "You do not need to read 88 proofs in order"),
        ("complete 87-result dependency structure", "complete 88-result dependency structure"),
        (
            "P78-P87 progressively tighten global separation from the declared continuous model family",
            "P78-P88 connect exact continuous-family separation to held-out finite-sample validation",
        ),
    )
    for old, new in replacements:
        text = text.replace(old, new)

    old_p87 = (
        "<p><strong>P87 is the current exact frontier.</strong> It exhausts every nonzero "
        "primitive integer four-event coefficient vector with |c_i| at most 2, modulo one "
        "global sign. The family contains 39,600 exact functionals, and on the same rational "
        "witness it gives <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p>"
    )
    new_p87 = (
        "<p><strong>P87 is the previous deterministic exact frontier.</strong> It exhausts "
        "every nonzero primitive integer four-event coefficient vector with |c_i| at most 2, "
        "modulo one global sign. The family contains 39,600 exact functionals, and on the same "
        "rational witness it gives <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p>"
        "\n      <p><strong>P88 is the current finite-sample frontier.</strong> Discovery freezes "
        "a P75 parameter box and one P87 functional before an independent validation sample is "
        "examined. Conditional scalar Hoeffding certification then avoids a 39,600-way "
        "functional penalty. The stored exact witness has a 95% certified design threshold of "
        "<strong>n = 1063</strong> and a positive full-law lower confidence bound at n = 2400. "
        "The result remains box-specific unless a separate covering theorem makes it global.</p>"
    )
    if old_p87 in text:
        text = text.replace(old_p87, new_p87, 1)
    elif "P88 is the current finite-sample frontier." not in text:
        raise RuntimeError("could not locate P87 current-frontier paragraph in Start Here")

    old_link = (
        'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/'
        'docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md">Read P87</a>'
    )
    new_link = (
        'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/'
        f'docs/{P88_PROOF}">Read P88</a>'
    )
    text = text.replace(old_link, new_link)
    write(path, text)


def update_plain_language() -> None:
    replace(
        "website/plain-language.html",
        (
            ("87 results", "88 results"),
            ("What the 87 results are doing", "What the 88 results are doing"),
            ("shows how all 87 results connect", "shows how all 88 results connect"),
            ("actual P87 research frontier", "actual P88 research frontier"),
            ("P75-P87", "P75-P88"),
            (
                "<strong>87</strong><span>proposition-level results</span>",
                "<strong>88</strong><span>proposition-level results</span>",
            ),
            (
                "<strong>P87</strong><span>current theorem frontier</span>",
                "<strong>P88</strong><span>current theorem frontier</span>",
            ),
        ),
    )


def update_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    replacements = (
        ("through Proposition 87", "through Proposition 88"),
        ("Eighty-seven results", "Eighty-eight results"),
        ("P71-P87", "P71-P88"),
        ("P73-P87", "P73-P88"),
        ("P77-P87", "P77-P88"),
        (
            "<strong>87</strong><span>proposition-level results</span>",
            "<strong>88</strong><span>proposition-level results</span>",
        ),
        ("index.html#p87-frontier", "index.html#p88-frontier"),
        ("Continue to the current P87 frontier", "Continue to the current P88 frontier"),
        ("None of P71-P87", "None of P71-P88"),
        ("Current exact frontier · P87", "Previous exact deterministic frontier · P87"),
    )
    for old, new in replacements:
        text = text.replace(old, new)

    old_stage = (
        "Recover the declared binary target channel, test the model itself, then strengthen "
        "rejection from selected constraints to exact global separation of the continuous P75 "
        "family, culminating in P87 exact bounded primitive four-event shared-parameter "
        "parity-functional separation."
    )
    new_stage = (
        "Recover the declared binary target channel, test the model itself, strengthen rejection "
        "through exact continuous-family separation, and then add P88 held-out finite-sample "
        "validation for a discovery-frozen P75 box/P87 functional pair."
    )
    text = text.replace(old_stage, new_stage)

    if 'id="p88-reader-frontier"' not in text:
        section = (
            "\n<section class=\"boundary\" id=\"p88-reader-frontier\"><div class=\"section-head\">"
            "<p class=\"eyebrow\">Current finite-sample frontier · P88</p>"
            "<h2>Held-out validation after discovery selection</h2>"
            "<p>P88 freezes a P75 parameter box and one P87 functional using discovery-only "
            "information, then evaluates that pair once on an independent validation sample. "
            "The exact witness has a certified 95% validation threshold of 1063 observations "
            "for its specified gap and a positive full-law lower confidence bound at n = 2400.</p>"
            "<p>The theorem is box-specific without a separate covering argument, and the "
            "physical-to-experiential bridge remains open.</p></div></section>\n"
        )
        if "</main>" not in text:
            raise RuntimeError("research-map.html is missing </main>")
        text = text.replace("</main>", section + "</main>", 1)
    write(path, text)


def update_other_reader_pages() -> None:
    common = (
        ("current P87 frontier", "current P88 frontier"),
        ("actual P87 research frontier", "actual P88 research frontier"),
        (
            "<strong>P87</strong><span>current theorem frontier</span>",
            "<strong>P88</strong><span>current theorem frontier</span>",
        ),
        ("P1-P87 proposition record", "P1-P88 proposition record"),
        ("Stage 06 · P73-P87", "Stage 06 · P73-P88"),
        ("P73-P87 build a continuous chain", "P73-P88 build a continuous chain"),
        ("P77-P87", "P77-P88"),
        ("P75-P87", "P75-P88"),
        ("P71-P87", "P71-P88"),
    )
    for relative in ("website/implementation.html", "website/sources.html"):
        replace(relative, common)


def main() -> None:
    if not (ROOT / "docs" / P88_PROOF).is_file():
        raise RuntimeError("P88 formal proof must exist before final consistency pass")
    update_readme()
    update_svg_accessibility()
    update_start_here()
    update_plain_language()
    update_research_map()
    update_other_reader_pages()
    print("[p88-finalize] reader, SVG, and README consistency repaired")


if __name__ == "__main__":
    main()
