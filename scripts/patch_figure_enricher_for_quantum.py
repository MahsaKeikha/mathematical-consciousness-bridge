from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts" / "enrich_figure_documentation.py"


def replace_once(text: str, old: str, new: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise RuntimeError(f"expected patch marker not found: {old[:120]!r}")
    return text.replace(old, new, 1)


def main() -> None:
    text = PATH.read_text(encoding="utf-8")

    text = replace_once(
        text,
        "from quantum_figure_records import build_quantum_records, write_quantum_visual_guide\n",
        "from conceptual_figure_records import build_special_conceptual_records\n"
        "from quantum_figure_records import build_quantum_records, write_quantum_visual_guide\n",
    )

    text = replace_once(
        text,
        "        **build_quantum_records(ROOT, FigureRecord, _plain),\n"
        "    }\n",
        "        **build_quantum_records(ROOT, FigureRecord, _plain),\n"
        "        **build_special_conceptual_records(ROOT, FigureRecord, _plain),\n"
        "    }\n",
    )

    text = replace_once(
        text,
        "    if existing_desc and len(existing_desc) >= 160:\n"
        "        description = existing_desc\n",
        "    if existing_desc and len(existing_desc) >= 160:\n"
        "        # Existing SVG metadata may already contain the status suffix from a\n"
        "        # previous enrichment run. Strip it before rebuilding metadata so the\n"
        "        # generator is idempotent rather than appending duplicate status text.\n"
        "        description = existing_desc.split(\" Scientific status:\", 1)[0].strip()\n",
    )

    text = replace_once(
        text,
        "    if \"quantum\" in path.parts:\n"
        "        return \"[Quantum visual guide](quantum_visual_guide.md)\"\n"
        "    match = re.match(r\"p(\\d+)_\", path.name, flags=re.I)\n",
        "    if \"quantum\" in path.parts:\n"
        "        return \"[Quantum visual guide](quantum_visual_guide.md)\"\n"
        "    if path.name == \"proposition_32_delay_quotient.svg\":\n"
        "        return \"[Proposition 32](proposition_32_delay_quotient_compatibility.md)\"\n"
        "    match = re.match(r\"p(\\d+)_\", path.name, flags=re.I)\n",
    )

    PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
