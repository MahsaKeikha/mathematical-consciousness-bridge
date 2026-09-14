"""Temporary self-removing repair for final P89 promoter contracts."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "promote_p89_public_frontier.py"

text = TARGET.read_text(encoding="utf-8")

old_heading = "<h3>Exact complete-linear optimum</h3>"
new_heading = "<h3>Exact complete real linear optimum</h3>"
if old_heading in text:
    text = text.replace(old_heading, new_heading)
elif new_heading not in text:
    raise RuntimeError("P89 Research Map completeness heading was not found")

anchor_pair = '("index.html#p88-frontier", "index.html#p89-frontier"),'

research_map_marker = '("Current theorem frontier · P88", "Current theorem frontier · P89"),'
if anchor_pair not in text[
    text.find("def promote_research_map") :
    text.find("def promote_misc_website", text.find("def promote_research_map"))
]:
    if research_map_marker not in text:
        raise RuntimeError("P89 Research Map replacement marker was not found")
    text = text.replace(
        research_map_marker,
        research_map_marker + "\n            " + anchor_pair,
        1,
    )

# The P89 Research Map may already have been created by the documentation
# synchronizer before this promoter runs. Normalize an existing section too,
# instead of only changing the insertion template.
old_tail = '        text = text.replace("</main>", section + "</main>", 1)\n    write(path, text)'
new_tail = (
    '        text = text.replace("</main>", section + "</main>", 1)\n'
    '    text = text.replace("<h3>Exact complete-linear optimum</h3>", '
    '"<h3>Exact complete real linear optimum</h3>")\n'
    '    text = text.replace("P89 complete-linear certificate", '
    '"P89 complete real linear certificate")\n'
    '    text = text.replace("index.html#p88-frontier", "index.html#p89-frontier")\n'
    '    write(path, text)'
)
if old_tail in text:
    text = text.replace(old_tail, new_tail, 1)
elif 'text = text.replace("P89 complete-linear certificate"' not in text:
    raise RuntimeError("P89 Research Map post-normalization hook was not found")

secondary_marker = '("P77-P88", "P77-P89"),'
if secondary_marker in text:
    tail = text.find(secondary_marker)
    nearby = text[tail : tail + 800]
    if anchor_pair not in nearby:
        text = text[:tail] + text[tail:].replace(
            secondary_marker,
            secondary_marker + "\n        " + anchor_pair,
            1,
        )

TARGET.write_text(text, encoding="utf-8")
Path(__file__).unlink()
print("[repair] aligned P89 promoter completeness wording and frontier links")
