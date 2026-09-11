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
        '    text = html.unescape(text)\n    return re.sub(r"\\s+", " ", text).strip()\n',
        '    text = html.unescape(text)\n'
        '    text = text.replace("\\u2013", "-").replace("\\u2014", "-")\n'
        '    return re.sub(r"\\s+", " ", text).strip()\n',
    )

    q38_old = (
        '    for old in ("**Fact / interpretation:**", "**Fact:**", "**Interpretation:**"):\n'
        '        text = text.replace(old, "**What the figure shows:**")\n\n'
    )
    q38_new = (
        '    for old in ("**Fact / interpretation:**", "**Fact:**", "**Interpretation:**"):\n'
        '        text = text.replace(old, "**What the figure shows:**")\n\n'
        '    text = text.replace(\n'
        '        "**Object:** a local multiscale variation statistic on a deterministic test signal.  \\n**Boundary:** this is a stress-test signal, not a validated consciousness measure.  \\n**Status:** synthetic test signal.",\n'
        '        "**Object:** a local multiscale variation statistic on a deterministic test signal.  \\n**What the figure shows:** the local complexity trace rises and falls where the deterministic test signal changes its multiscale variation, providing a controlled stress test for the statistic rather than a biological measurement.  \\n**Boundary:** this is a stress-test signal, not a validated consciousness measure.  \\n**Status:** synthetic test signal.",\n'
        '    )\n\n'
    )
    text = replace_once(text, q38_old, q38_new)

    theorem_old = (
        "<h3>Theorem roadmap</h3><p>Dependency-aware visual summary of the proposition program.</p>"
    )
    theorem_new = (
        "<h3>Theorem roadmap</h3><p>Read the roadmap from prerequisite blocks toward later certificates: each connector marks a declared dependency, while separate branches show results that solve different subproblems before rejoining the bridge-sufficiency lineage. Proposition order records development history, not a claim that later numbers automatically strengthen every earlier scientific conclusion.</p>"
    )
    if theorem_new not in text:
        marker = '    replacements = {\n'
        if marker not in text:
            raise RuntimeError("visual-atlas replacement marker not found")
        insertion = (
            '    text = text.replace(\n'
            f'        {theorem_old!r},\n'
            f'        {theorem_new!r},\n'
            '    )\n\n'
        )
        text = text.replace(marker, insertion + marker, 1)

    PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
