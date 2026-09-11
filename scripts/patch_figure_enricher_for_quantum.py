from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts" / "enrich_figure_documentation.py"


def replace_once(text: str, old: str, new: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise RuntimeError(f"expected patch marker not found: {old[:100]!r}")
    return text.replace(old, new, 1)


def main() -> None:
    text = PATH.read_text(encoding="utf-8")

    text = replace_once(
        text,
        "from pathlib import Path\n",
        "from pathlib import Path\n\nfrom quantum_figure_records import build_quantum_records, write_quantum_visual_guide\n",
    )

    text = replace_once(
        text,
        "    combined = {**_visual_atlas_records(), **_readme_records(), **_quantitative_records()}\n",
        "    combined = {\n"
        "        **_visual_atlas_records(),\n"
        "        **_readme_records(),\n"
        "        **_quantitative_records(),\n"
        "        **build_quantum_records(ROOT, FigureRecord, _plain),\n"
        "    }\n",
    )

    text = replace_once(
        text,
        "    if \"quantitative\" in path.parts:\n        return \"[Quantitative atlas](quantitative_physics_mathematics_atlas.md)\"\n",
        "    if \"quantitative\" in path.parts:\n"
        "        return \"[Quantitative atlas](quantitative_physics_mathematics_atlas.md)\"\n"
        "    if \"quantum\" in path.parts:\n"
        "        return \"[Quantum visual guide](quantum_visual_guide.md)\"\n",
    )

    text = replace_once(
        text,
        "    conceptual = [row for row in rows if \"/quantitative/\" not in row[0] and not re.match(r\"docs/figures/p\\d+_\", row[0], flags=re.I)]\n"
        "    propositions = [row for row in rows if re.match(r\"docs/figures/p\\d+_\", row[0], flags=re.I)]\n"
        "    quantitative = [row for row in rows if \"/quantitative/\" in row[0]]\n",
        "    conceptual = [\n"
        "        row for row in rows\n"
        "        if \"/quantitative/\" not in row[0]\n"
        "        and \"/quantum/\" not in row[0]\n"
        "        and not re.match(r\"docs/figures/p\\d+_\", row[0], flags=re.I)\n"
        "    ]\n"
        "    quantum = [row for row in rows if \"/quantum/\" in row[0]]\n"
        "    propositions = [row for row in rows if re.match(r\"docs/figures/p\\d+_\", row[0], flags=re.I)]\n"
        "    quantitative = [row for row in rows if \"/quantitative/\" in row[0]]\n",
    )

    text = replace_once(
        text,
        "        f\"**Current catalog:** {len(rows)} SVG figures: {len(conceptual)} architecture/conceptual visuals, {len(propositions)} proposition/theorem visuals, and {len(quantitative)} quantitative figures.\",\n",
        "        f\"**Current catalog:** {len(rows)} SVG figures: {len(conceptual)} architecture/conceptual visuals, {len(quantum)} foundational quantum-physics visuals, {len(propositions)} proposition/theorem visuals, and {len(quantitative)} quantitative figures.\",\n",
    )

    text = replace_once(
        text,
        "    add_section(\"Architecture and conceptual figures\", conceptual)\n"
        "    add_section(\"Proposition and theorem figures\", propositions)\n"
        "    add_section(\"Quantitative physics and mathematics figures\", quantitative)\n",
        "    add_section(\"Architecture and conceptual figures\", conceptual)\n"
        "    add_section(\"Foundational quantum-physics figures\", quantum)\n"
        "    add_section(\"Proposition and theorem figures\", propositions)\n"
        "    add_section(\"Quantitative physics and mathematics figures\", quantitative)\n",
    )

    text = replace_once(
        text,
        "    rows = _enrich_svgs()\n    _write_catalog(rows)\n",
        "    rows = _enrich_svgs()\n"
        "    write_quantum_visual_guide(ROOT)\n"
        "    _write_catalog(rows)\n",
    )

    PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
