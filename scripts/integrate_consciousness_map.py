from pathlib import Path


def integrate_research_architecture() -> None:
    path = Path("docs/research_architecture.md")
    text = path.read_text(encoding="utf-8")
    marker = "![High-level consciousness map](figures/consciousness_map.svg)"
    if marker in text:
        return

    anchor = "# Research Architecture\n\n"
    insert = (
        "# Research Architecture\n\n"
        "## High-level consciousness map\n\n"
        "![High-level consciousness map](figures/consciousness_map.svg)\n\n"
        "**High-level map.** Theory, measurement, dynamics, and the sufficiency bridge are deliberately separated so that theoretical adequacy, measurement validity, and dynamical sufficiency cannot be mistaken for the still-open physical-to-experiential bridge.\n\n"
        "## Detailed research architecture\n\n"
    )
    if anchor not in text:
        raise RuntimeError("Research architecture heading not found")
    path.write_text(text.replace(anchor, insert, 1), encoding="utf-8")


def integrate_conceptual_record() -> None:
    path = Path("scripts/conceptual_figure_records.py")
    text = path.read_text(encoding="utf-8")
    figure_path = '"docs/figures/consciousness_map.svg"'
    if figure_path in text:
        return

    anchor = "RECORDS: dict[str, dict[str, str]] = {\n"
    block = (
        '    "docs/figures/consciousness_map.svg": {\n'
        '        "title": "Consciousness map: theory, measurement, dynamics, and sufficiency bridge",\n'
        '        "description": (\n'
        '            "What this figure shows: a high-level separation of four scientific obligations in consciousness research: theory, measurement, dynamics, and the sufficiency bridge. "\n'
        '            "How to read it: begin at Theory, follow the labeled theoretical-sufficiency route to Measurement and the model-implied-evolution route to Dynamics, then read Measurement and Dynamics as independent constraints on the Sufficiency bridge. The arrows are logical research dependencies and do not identify physical variables with experience. "\n'
        '            "Main takeaway: theoretical adequacy, measurement validity, and dynamical sufficiency are distinct requirements; satisfying them can support or falsify a declared model but does not by itself close the physical-to-experiential bridge."\n'
        '        ),\n'
        '        "status": (\n'
        '            "Research-architecture figure. It separates physical, measurement, and sufficiency obligations; it is not an empirical consciousness result or a theorem identifying any physical state with consciousness. The physical-to-experiential bridge remains open."\n'
        '        ),\n'
        '    },\n'
    )
    if anchor not in text:
        raise RuntimeError("Conceptual record anchor not found")
    path.write_text(text.replace(anchor, anchor + block, 1), encoding="utf-8")


def main() -> None:
    integrate_research_architecture()
    integrate_conceptual_record()


if __name__ == "__main__":
    main()
