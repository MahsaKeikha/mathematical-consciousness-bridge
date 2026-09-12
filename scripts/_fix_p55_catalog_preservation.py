from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "enrich_figure_documentation.py"
TEST = ROOT / "tests" / "test_reproducibility_contract.py"


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    old = '''            safe_title = record.title.replace("|", "\\\\|")
            safe_desc = record.description.replace("|", "\\\\|")
            safe_status = record.status.replace("|", "\\\\|")
            lines.append(
                f"| [{safe_title}]({docs_rel}) | {safe_desc} | {safe_status} | {_context_link(rel)} |"
            )
'''
    new = '''            safe_title = record.title.replace("|", "\\\\|")
            safe_desc = record.description.replace("|", "\\\\|")
            safe_status = record.status.replace("|", "\\\\|")
            if Path(rel).name == "p55_pruning_aware_switching_monotonicity.svg":
                p55_scope = (
                    " Scope guide: metric shortcutting proves the route monotonicity; "
                    "the support-preserving case has zero route release; the shortcut lower "
                    "certificate quantifies guaranteed switching savings after support deletion; "
                    "and the physical-to-experiential bridge remains open."
                )
                if "metric shortcutting" not in safe_desc:
                    safe_desc += p55_scope
            lines.append(
                f"| [{safe_title}]({docs_rel}) | {safe_desc} | {safe_status} | {_context_link(rel)} |"
            )
'''
    if old not in text:
        if "p55_scope = (" not in text:
            raise RuntimeError("catalog row construction marker not found")
    else:
        text = text.replace(old, new, 1)
    TARGET.write_text(text, encoding="utf-8")

    test_text = TEST.read_text(encoding="utf-8")
    addition = '''

def test_generated_catalog_preserves_p55_scope_language() -> None:
    catalog = _read("docs/figure_catalog.md")
    for token in (
        "metric shortcutting",
        "support-preserving",
        "shortcut lower certificate",
        "physical-to-experiential bridge",
    ):
        assert token in catalog
'''
    if "test_generated_catalog_preserves_p55_scope_language" not in test_text:
        TEST.write_text(test_text.rstrip() + addition + "\n", encoding="utf-8")

    print("P55 generated-catalog scope preservation integrated")


if __name__ == "__main__":
    main()
