"""Promote scholarly provenance files and collegial origin wording into permanent verification."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts" / "verify_repository.py"


def insert_after_once(text: str, anchor: str, insertion: str, label: str) -> str:
    if insertion in text:
        return text
    if anchor not in text:
        raise RuntimeError(f"missing verifier anchor for {label}")
    return text.replace(anchor, anchor + insertion, 1)


def main() -> None:
    text = PATH.read_text(encoding="utf-8")

    core_anchor = '    "docs/claim_evidence_standard.md",\n'
    core_insert = (
        '    "docs/claim_source_matrix.md",\n'
        '    "docs/reference_audit.md",\n'
        '    "docs/literature_map.md",\n'
    )
    for item in core_insert:
        text = insert_after_once(text, core_anchor, item, f"core file {item.strip()}")
        core_anchor = item

    link_anchor = '    "docs/claim_evidence_standard.md",\n'
    link_section = text.index("LINK_SURFACES = (")
    link_end = text.index(")", link_section)
    link_block = text[link_section:link_end]
    for item in (
        '    "docs/claim_source_matrix.md",\n',
        '    "docs/reference_audit.md",\n',
        '    "docs/literature_map.md",\n',
    ):
        if item.strip() not in link_block:
            position = text.find(link_anchor, link_section, link_end)
            if position == -1:
                raise RuntimeError("missing LINK_SURFACES scholarly anchor")
            position += len(link_anchor)
            text = text[:position] + item + text[position:]
            link_end += len(item)
            link_anchor = item
            link_block = text[link_section:link_end]

    positive = (
        '    if "important conceptual starting point" not in sources_page or "distinct mathematical framework" not in sources_page:\n'
        '        raise RuntimeError("sources page does not expose the collegial Tegmark research-origin context")\n'
    )
    if positive not in text:
        old = (
            '    if "intellectual and physical-context background" not in sources_page:\n'
            '        raise RuntimeError("sources page does not distinguish research origin from evidential support")\n'
        )
        if old not in text:
            raise RuntimeError("missing research-origin verifier wording anchor")
        text = text.replace(old, positive, 1)

    release_anchor = '    _verify_reader_frontier_freshness()\n'
    guard = (
        '    scholarly_origin_files = (\n'
        '        "website/start-here.html",\n'
        '        "website/sources.html",\n'
        '        "docs/claim_evidence_standard.md",\n'
        '        "docs/literature_map.md",\n'
        '        "docs/reference_audit.md",\n'
        '        "docs/claim_source_matrix.md",\n'
        '    )\n'
        '    defensive_origin_phrases = (\n'
        '        "this origin citation does not make Tegmark\'s paper evidence",\n'
        '        "not evidence for the repository\'s later original propositions",\n'
        '        "not evidential support for later repository-original propositions",\n'
        '    )\n'
        '    for relative_path in scholarly_origin_files:\n'
        '        source = _read(relative_path)\n'
        '        hits = [phrase for phrase in defensive_origin_phrases if phrase in source]\n'
        '        if hits:\n'
        '            raise RuntimeError(f"{relative_path} contains defensive research-origin wording: {hits}")\n\n'
    )
    if "defensive_origin_phrases = (" not in text:
        if release_anchor not in text:
            raise RuntimeError("missing verifier reader-frontier gate anchor")
        text = text.replace(release_anchor, guard + release_anchor, 1)

    PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
