"""Temporary repair for P89 deterministic publication generation.

This helper narrows the reader status-grid rewrites so publication promotion cannot
consume adjacent scientific-boundary or reader-primer sections. It is intended to
be removed once the canonical generated surfaces have been committed.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMOTER = ROOT / "scripts" / "promote_p89_public_frontier.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one source block, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    text = PROMOTER.read_text(encoding="utf-8")

    old_plain = '''    status = re.compile(\n        r'<div class="status-grid" aria-label="Current research status">.*?</div>\\s*</section>',\n        re.DOTALL,\n    )\n    replacement = \'\'\'<div class="status-grid" aria-label="Current research status">\n        <div><strong>Research I</strong><span>physical-system identification</span></div>\n        <div><strong>Research II</strong><span>89 results · current frontier P89</span></div>\n        <div><strong>Research III</strong><span>measurement science under uncertainty</span></div>\n        <div><strong>Open</strong><span>final physical-to-experiential bridge</span></div>\n      </div>\n    </section>\'\'\'\n    text, count = status.subn(replacement, text, count=1)\n'''
    new_plain = '''    status = re.compile(\n        r'<div class="status-grid" aria-label="Current research status">\\n'\n        r'(?:\\s*<div>.*?</div>\\n){4}\\s*</div>'\n    )\n    replacement = \'\'\'<div class="status-grid" aria-label="Current research status">\n        <div><strong>Research I</strong><span>physical-system identification</span></div>\n        <div><strong>Research II</strong><span>89 results · current frontier P89</span></div>\n        <div><strong>Research III</strong><span>measurement science under uncertainty</span></div>\n        <div><strong>Open</strong><span>final physical-to-experiential bridge</span></div>\n      </div>\'\'\'\n    text, count = status.subn(replacement, text, count=1)\n'''
    text = replace_once(text, old_plain, new_plain, "Plain Language status grid")

    old_start = '''    status = re.compile(\n        r'<div class="status-grid" aria-label="Current research status">.*?</div>\\s*'\n        r'<p class="small-note"><strong>Formal repository release:</strong>.*?</p>\\s*</section>',\n        re.DOTALL,\n    )\n    replacement = \'\'\'<div class="status-grid" aria-label="Current research status">\n        <div><strong>Research I</strong><span>physical-system identification</span></div>\n        <div><strong>Research II</strong><span>89 results · current frontier P89</span></div>\n        <div><strong>Research III</strong><span>measurement science under uncertainty</span></div>\n        <div><strong>Open</strong><span>physical-to-experiential bridge</span></div>\n      </div>\n      <p class="small-note"><strong>Formal repository release:</strong> v0.82.0. The documented theorem frontier can advance independently of the packaged release.</p>\n    </section>\'\'\'\n    text, count = status.subn(replacement, text, count=1)\n'''
    new_start = '''    status = re.compile(\n        r'<div class="status-grid" aria-label="Current research status">\\n'\n        r'(?:\\s*<div>.*?</div>\\n){4}\\s*</div>'\n    )\n    replacement = \'\'\'<div class="status-grid" aria-label="Current research status">\n        <div><strong>Research I</strong><span>physical-system identification</span></div>\n        <div><strong>Research II</strong><span>89 results · current frontier P89</span></div>\n        <div><strong>Research III</strong><span>measurement science under uncertainty</span></div>\n        <div><strong>Open</strong><span>physical-to-experiential bridge</span></div>\n      </div>\'\'\'\n    text, count = status.subn(replacement, text, count=1)\n'''
    text = replace_once(text, old_start, new_start, "Start Here status grid")

    PROMOTER.write_text(text, encoding="utf-8")
    print("[repair] narrowed P89 reader status-grid rewrites")


if __name__ == "__main__":
    main()
