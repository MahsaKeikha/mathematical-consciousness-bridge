"""Repair narrow P92 migration contracts before canonical synchronization.

This helper exists only for the P92 branch migration. Delete it together with
the branch-only write workflow before merging P92 to main.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def patch_homepage() -> None:
    path = "website/index.html"
    text = read(path)
    replacements = (
        (
            "<strong>91</strong><span>proposition-level results</span>",
            "<strong>92</strong><span>proposition-level results</span>",
        ),
        (
            "P91 current theorem frontier · v0.82.0",
            "P92 current theorem frontier · v0.82.0",
        ),
        ("Explore all 91 results", "Explore all 92 results"),
        (
            "Current record:</strong> 91 proposition-level results through P91",
            "Current record:</strong> 92 proposition-level results through P92",
        ),
        ("The 91-result program", "The 92-result program"),
        ("all 91 propositions", "all 92 propositions"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    write(path, text)


def patch_visual_atlas() -> None:
    path = "website/visual-atlas.html"
    text = read(path)
    text = text.replace(
        "Historical mixed-prevalence frontier · P91",
        "Previous theorem frontier · P91",
    )
    text = text.replace(
        "Current theorem frontier · P91",
        "Previous theorem frontier · P91",
    )
    write(path, text)


def patch_reader_dashboards() -> None:
    path = "website/plain-language.html"
    text = read(path)
    replacements = (
        (
            "<strong>Research II</strong><span>91 results · current frontier P91</span>",
            "<strong>Research II</strong><span>92 results · current frontier P92</span>",
        ),
        (
            "This is the 91-result Research II theorem program currently reaching P91.",
            "This is the 92-result Research II theorem program currently reaching P92.",
        ),
        ("A 91-result sufficiency and falsification architecture", "A 92-result sufficiency and falsification architecture"),
        ("The 91-result proposition program", "The 92-result proposition program"),
        ("The current theorem frontier is P91.", "The current theorem frontier is P92."),
        ("P91 is the current checkpoint", "P92 is the current checkpoint"),
        ("P91 is the current mathematical checkpoint", "P92 is the current mathematical checkpoint"),
        ("all 91 Research II results", "all 92 Research II results"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    write(path, text)

    path = "website/start-here.html"
    text = read(path)
    replacements = (
        (
            "<strong>Research II</strong><span>91 results · current frontier P91</span>",
            "<strong>Research II</strong><span>92 results · current frontier P92</span>",
        ),
        ("current Research II P91 frontier", "current Research II P92 frontier"),
        ("Open all 91 Research II results", "Open all 92 Research II results"),
        ("The 91 propositions are the formal theorem record of Research II", "The 92 propositions are the formal theorem record of Research II"),
        ("P1-P91 build the mathematical conditions", "P1-P92 build the mathematical conditions"),
        ("P75-P91 test the declared target-measurement model", "P75-P92 test the declared target-measurement model"),
        ("<span>P75-P91</span>", "<span>P75-P92</span>"),
        ("The 91 Research II propositions by scientific role", "The 92 Research II propositions by scientific role"),
        ("You do not need to read 91 Research II proofs in order", "You do not need to read 92 Research II proofs in order"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    write(path, text)


def patch_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    replacements = (
        (
            "P89 closes the complete real linear parity-functional class, P90 adds exact nonlinear single-component separation, and P91 extends nonlinear separation to arbitrary latent mixing through a rank-two flattening certificate.",
            "P89 closes the complete real linear parity-functional class, P90 adds exact nonlinear single-component separation, P91 extends nonlinear separation to arbitrary latent mixing through a rank-two flattening certificate, and P92 closes the remaining mixed-prevalence distance bracket at the exact value 1/24.",
        ),
        ("The current theorem frontier is P91.", "The current theorem frontier is P92."),
        ("<div><strong>91</strong><span>proposition-level results</span></div>", "<div><strong>92</strong><span>proposition-level results</span></div>"),
        ("<div><strong>P91</strong><span>current theorem frontier</span></div>", "<div><strong>P92</strong><span>current theorem frontier</span></div>"),
        ('href="index.html#p91-frontier">Continue to the current P92 frontier', 'href="index.html#p92-frontier">Continue to the current P92 frontier'),
        ('href="visual-atlas.html#p91-frontier">See the P91 figure', 'href="visual-atlas.html#p92-frontier">See the P92 figure'),
        ('docs/p91_equation_provenance.md">Audit P91 provenance', 'docs/p92_equation_provenance.md">Audit P92 provenance'),
        ("Research Map · Current theorem frontier P91", "Research Map · Current theorem frontier P92"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    write(path, text)


def patch_svg_accessibility() -> None:
    path = "docs/figures/p92_exact_global_mixed_prevalence_distance.svg"
    text = read(path)
    old = (
        '<desc id="desc">Exact nonlinear sign-coherence certificate proving the '
        'full P75 L-infinity distance is one over twenty-four.</desc>'
    )
    new = (
        '<desc id="desc">This theorem figure compares three exact empirical '
        'conditional determinants with their sign-stability radii, states the '
        'universal nonnegative determinant-product constraint for the full P75 '
        'mixture family, and shows the matching exact distance boundary at one '
        'over twenty-four. Scientific status: conditional model-separation '
        'theorem only; it does not identify consciousness or establish a '
        'replacement ontology.</desc>'
    )
    if old not in text and new not in text:
        raise RuntimeError("P92 SVG description anchor changed unexpectedly")
    text = text.replace(old, new)
    write(path, text)


def patch_machine_citation() -> None:
    for path in ("CITATION.cff", "CITATION.bib", "CITATION.md"):
        text = read(path)
        text = text.replace(
            "Current documented theorem frontier: P91",
            "Current documented theorem frontier: P92",
        )
        text = text.replace(
            "current documented frontier, P91",
            "current documented frontier, P92",
        )
        write(path, text)


def patch_implementation_range() -> None:
    path = "website/implementation.html"
    text = read(path).replace("P73-P91", "P73-P92")
    write(path, text)


def main() -> None:
    patch_homepage()
    patch_visual_atlas()
    patch_reader_dashboards()
    patch_research_map()
    patch_svg_accessibility()
    patch_machine_citation()
    patch_implementation_range()
    print("[P92] branch migration contracts repaired")


if __name__ == "__main__":
    main()
