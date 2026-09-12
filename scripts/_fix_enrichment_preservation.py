from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "enrich_figure_documentation.py"
TEST = ROOT / "tests" / "test_reproducibility_contract.py"


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")

    function_marker = '''def _existing_metadata(svg: str) -> tuple[str | None, str | None]:
    title_match = re.search(r"<title\\b[^>]*>(.*?)</title>", svg, flags=re.IGNORECASE | re.DOTALL)
    desc_match = re.search(r"<desc\\b[^>]*>(.*?)</desc>", svg, flags=re.IGNORECASE | re.DOTALL)
    title = _plain(title_match.group(1)) if title_match else None
    desc = _plain(desc_match.group(1)) if desc_match else None
    return title, desc
'''
    helper = function_marker + '''

def _has_curated_metadata(svg: str) -> bool:
    """Return True when an SVG already carries substantive publication metadata.

    Source-authored theorem figures can contain proposition-specific witness text,
    accessibility instructions, and scientific-boundary language that is more
    precise than a generic catalog record. Regeneration must preserve that authored
    material rather than replace it with a shorter synthesized description.
    """

    title, desc = _existing_metadata(svg)
    return bool(
        title
        and desc
        and len(desc) >= 160
        and "What this figure shows:" in desc
        and "Scientific status:" in desc
    )
'''
    if "def _has_curated_metadata" not in text:
        if function_marker not in text:
            raise RuntimeError("existing metadata function marker not found")
        text = text.replace(function_marker, helper, 1)

    old_block = '''        record = combined.get(rel)
        if record is None:
            record = _proposition_record(path, svg)
        if record is None:
            record = _fallback_record(path, svg)

        enriched = _replace_or_insert_metadata(svg, record)
        if enriched != original:
            _write(path, enriched)
        rows.append((rel, record))
'''
    new_block = '''        existing_title, existing_desc = _existing_metadata(svg)
        if _has_curated_metadata(svg):
            assert existing_title is not None
            assert existing_desc is not None
            description, status = existing_desc.split("Scientific status:", 1)
            record = FigureRecord(
                title=existing_title,
                description=description.strip(),
                status=status.strip(),
            )
            enriched = svg
        else:
            record = combined.get(rel)
            if record is None:
                record = _proposition_record(path, svg)
            if record is None:
                record = _fallback_record(path, svg)
            enriched = _replace_or_insert_metadata(svg, record)

        if enriched != original:
            _write(path, enriched)
        rows.append((rel, record))
'''
    if old_block not in text:
        if new_block not in text:
            raise RuntimeError("figure enrichment loop marker not found")
    else:
        text = text.replace(old_block, new_block, 1)

    TARGET.write_text(text, encoding="utf-8")

    test_text = TEST.read_text(encoding="utf-8")
    addition = '''

def test_figure_enrichment_preserves_curated_theorem_metadata() -> None:
    source = _read("scripts/enrich_figure_documentation.py")
    assert "def _has_curated_metadata" in source
    assert "if _has_curated_metadata(svg):" in source
    assert 'enriched = svg' in source
'''
    if "test_figure_enrichment_preserves_curated_theorem_metadata" not in test_text:
        TEST.write_text(test_text.rstrip() + addition + "\n", encoding="utf-8")

    print("curated figure metadata preservation integrated")


if __name__ == "__main__":
    main()
