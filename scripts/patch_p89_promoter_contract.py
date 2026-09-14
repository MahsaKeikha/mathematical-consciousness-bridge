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
if anchor_pair not in text[text.find("def promote_research_map"):text.find("def promote_secondary", text.find("def promote_research_map")) if "def promote_secondary" in text else len(text)]:
    if research_map_marker not in text:
        raise RuntimeError("P89 Research Map replacement marker was not found")
    text = text.replace(
        research_map_marker,
        research_map_marker + "\n            " + anchor_pair,
        1,
    )

secondary_marker = '("P77-P88", "P77-P89"),'
if secondary_marker in text:
    # This tuple feeds implementation and other specialist pages. Replacing the
    # obsolete homepage frontier anchor here keeps navigation internally valid.
    tail = text.find(secondary_marker)
    nearby = text[tail:tail + 800]
    if anchor_pair not in nearby:
        text = text[:tail] + text[tail:].replace(
            secondary_marker,
            secondary_marker + "\n        " + anchor_pair,
            1,
        )

TARGET.write_text(text, encoding="utf-8")
Path(__file__).unlink()
print("[repair] aligned P89 promoter completeness wording and frontier links")
