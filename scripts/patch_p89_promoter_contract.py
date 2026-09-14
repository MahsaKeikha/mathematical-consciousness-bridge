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
research_map_start = text.find("def promote_research_map")
research_map_end = text.find("def promote_misc_website", research_map_start)
if research_map_start < 0:
    raise RuntimeError("P89 Research Map promoter function was not found")
if research_map_end < 0:
    research_map_end = len(text)
research_map_source = text[research_map_start:research_map_end]

research_map_marker = '("Current theorem frontier · P88", "Current theorem frontier · P89"),'
if anchor_pair not in research_map_source:
    if research_map_marker not in research_map_source:
        raise RuntimeError("P89 Research Map replacement marker was not found")
    absolute = research_map_start + research_map_source.index(research_map_marker)
    text = text[:absolute] + text[absolute:].replace(
        research_map_marker,
        research_map_marker + "\n            " + anchor_pair,
        1,
    )

# Rebuild the generated P89 Research Map section on every promotion pass. Earlier
# passes created the section conditionally, so later improvements to the canonical
# wording never reached an already-generated page.
research_map_start = text.find("def promote_research_map")
research_map_end = text.find("def promote_misc_website", research_map_start)
if research_map_end < 0:
    research_map_end = len(text)
research_map_source = text[research_map_start:research_map_end]
conditional = "    if 'id=\"p89-research-map\"' not in text:\n"
conditional_at = text.find(conditional, research_map_start, research_map_end)
write_at = text.find("    write(path, text)", research_map_start, research_map_end)
if conditional_at >= 0 and write_at > conditional_at:
    body = text[conditional_at + len(conditional):write_at]
    unindented_lines = []
    for line in body.splitlines(keepends=True):
        if line.startswith("        "):
            line = line[4:]
        unindented_lines.append(line)
    replacement = (
        '    text = remove_section(text, "p89-research-map")\n'
        + "".join(unindented_lines)
    )
    text = text[:conditional_at] + replacement + text[write_at:]
elif 'text = remove_section(text, "p89-research-map")' not in research_map_source:
    raise RuntimeError("P89 Research Map conditional generation block was not found")

# Normalize any surviving wording in the canonical insertion template.
text = text.replace("P89 complete-linear certificate", "P89 complete real linear certificate")
text = text.replace("index.html#p88-frontier", "index.html#p89-frontier")

secondary_marker = '("P77-P88", "P77-P89"),'
if secondary_marker in text:
    tail = text.find(secondary_marker)
    nearby = text[tail : tail + 900]
    if anchor_pair not in nearby:
        text = text[:tail] + text[tail:].replace(
            secondary_marker,
            secondary_marker + "\n        " + anchor_pair,
            1,
        )

TARGET.write_text(text, encoding="utf-8")
Path(__file__).unlink()
print("[repair] made P89 Research Map promotion idempotent and current")
