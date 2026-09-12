"""One-time P82 reader-entry synchronization helper."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def update(path: str, replacements: tuple[tuple[str, str], ...]) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    for old, new in replacements:
        text = text.replace(old, new)
    target.write_text(text, encoding="utf-8")


def main() -> None:
    update(
        "START_HERE.md",
        (
            ("the 81-result theorem program", "the 82-result theorem program"),
            ("**81 proposition-level results**", "**82 proposition-level results**"),
            ("current theorem frontier is **P81**", "current theorem frontier is **P82**"),
            ("Target-model adequacy\\nP75-P81", "Target-model adequacy\\nP75-P82"),
            ("P71-P81", "P71-P82"),
            ("P74-P81", "P74-P82"),
            ("P75-P81", "P75-P82"),
            ("## The 81 results", "## The 82 results"),
            ("## The current frontier: P71-P81", "## The current frontier: P71-P82"),
        ),
    )

    update(
        "website/start-here.html",
        (
            ("the 81 proposition-level results", "the 82 proposition-level results"),
            ("the current P81 frontier", "the current P82 frontier"),
            ("See the 81-result research map", "See the 82-result research map"),
            ("<strong>81</strong><span>proposition-level results</span>", "<strong>82</strong><span>proposition-level results</span>"),
            ("<strong>P81</strong><span>current theorem frontier</span>", "<strong>P82</strong><span>current theorem frontier</span>"),
            ("P75-P81 test", "P75-P82 test"),
            ("read 81 proofs", "read 82 proofs"),
            ("P71-P81", "P71-P82"),
            ("P74-P81", "P74-P82"),
            ("The 81 propositions", "The 82 propositions"),
            ("P75-P81", "P75-P82"),
            ("full 81-result dependency structure", "full 82-result dependency structure"),
            ("P81 strengthens full-law model separation without adding a consciousness assumption", "P82 strengthens full-law model separation without adding a consciousness assumption"),
        ),
    )

    start_path = ROOT / "website" / "start-here.html"
    start = start_path.read_text(encoding="utf-8")
    old_frontier = (
        "<p>P78 introduced exact-rational branch-and-bound for the continuous P75 model family. P80 tightened each box relaxation by enforcing probability normalization. P81 adds exact constraints on every nonempty projected binary event and transfers any event mismatch back to a certified lower bound on the full sixteen-cell L-infinity model distance.</p>\n"
        "      <p>The logical direction matters: P81 can strengthen a rejection certificate for the declared target-measurement model. It does not identify the latent state with consciousness and does not close the physical-to-experiential bridge.</p>\n"
        "      <div class=\"hero-actions\">\n"
        "        <a class=\"button primary\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_81_projection_event_model_separation.md\">Read P81</a>\n"
        "        <a class=\"button\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p81_equation_provenance.md\">P81 provenance</a>"
    )
    new_frontier = (
        "<p>P78 introduced exact-rational branch-and-bound for the continuous P75 model family. P80 enforced probability normalization, and P81 added exact constraints for every nonempty projected cylinder event. P82 now adds exact residual-event constraints from nested parent-child cylinders. Because the parent and newly fixed views use disjoint response coordinates inside each P75 latent branch, the P82 residual interval is computed exactly rather than by subtracting two separate P81 intervals.</p>\n"
        "      <p>The logical direction remains one-sided: P82 can strengthen rejection of the declared target-measurement model. Its 256 new contrasts include a strict exact-rational witness with P80 = 0, P81 = 1/16, and P82 = 1/12. It does not identify the latent state with consciousness and does not close the physical-to-experiential bridge.</p>\n"
        "      <div class=\"hero-actions\">\n"
        "        <a class=\"button primary\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_82_exact_nested_projection_contrast.md\">Read P82</a>\n"
        "        <a class=\"button\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p82_equation_provenance.md\">P82 provenance</a>"
    )
    if old_frontier in start:
        start = start.replace(old_frontier, new_frontier, 1)
    start_path.write_text(start, encoding="utf-8")

    update(
        "docs/figures/theorem_roadmap.svg",
        (
            ("Later P61-P70 and P71-P80 are separate continuations", "Later P61-P70 and P71-P82 are separate continuations"),
            ("Later P61-P70 and P71-P81 are separate continuations", "Later P61-P70 and P71-P82 are separate continuations"),
        ),
    )

    for name in ("visual-atlas.html", "sources.html", "physics-mathematics.html"):
        update(
            f"website/{name}",
            (
                ("81 proposition-level results", "82 proposition-level results"),
                ("81-result", "82-result"),
                ("P71-P81", "P71-P82"),
                ("P74-P81", "P74-P82"),
                ("P75-P81", "P75-P82"),
            ),
        )

    print("P82 reader entry points synchronized")


if __name__ == "__main__":
    main()
