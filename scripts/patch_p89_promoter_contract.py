"""Temporary self-removing repair for final P89 promoter contracts."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "promote_p89_public_frontier.py"

text = TARGET.read_text(encoding="utf-8")

# Strengthen the scientific wording in the canonical P89 Research Map template.
text = text.replace(
    "<h3>Exact complete-linear optimum</h3>",
    "<h3>Exact complete real linear optimum</h3>",
)
text = text.replace(
    "P89 complete-linear certificate",
    "P89 complete real linear certificate",
)

research_map_start = text.find("def promote_research_map")
research_map_end = text.find("def promote_misc_website", research_map_start)
if research_map_start < 0:
    raise RuntimeError("P89 Research Map promoter function was not found")
if research_map_end < 0:
    research_map_end = len(text)
research_map_source = text[research_map_start:research_map_end]

# Rebuild the generated P89 Research Map section on every promotion pass. Earlier
# passes created the section conditionally, so later improvements to the canonical
# wording never reached an already-generated page.
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

# Normalize the actual generated Research Map HTML after the new P89 section has
# been inserted. Doing this as executable promoter code avoids accidentally
# rewriting a source replacement tuple into P89 -> P89.
research_map_start = text.find("def promote_research_map")
research_map_end = text.find("def promote_misc_website", research_map_start)
write_at = text.find("    write(path, text)", research_map_start, research_map_end)
normalizer = '    text = text.replace("index.html#p88-frontier", "index.html#p89-frontier")\n'
if normalizer not in text[research_map_start:research_map_end]:
    if write_at < 0:
        raise RuntimeError("P89 Research Map write hook was not found")
    text = text[:write_at] + normalizer + text[write_at:]

# Specialist implementation pages can also carry a link back to the public
# frontier. Keep that link synchronized with P89 through the normal replacement
# table used by promote_misc_website().
misc_start = text.find("def promote_misc_website")
misc_end = text.find("def assert_balanced_reader_state", misc_start)
if misc_start < 0:
    raise RuntimeError("P89 miscellaneous website promoter was not found")
if misc_end < 0:
    misc_end = len(text)
misc_source = text[misc_start:misc_end]
anchor_pair = '("index.html#p88-frontier", "index.html#p89-frontier"),'
if anchor_pair not in misc_source:
    marker = '("P77-P88", "P77-P89"),'
    marker_at = text.find(marker, misc_start, misc_end)
    if marker_at < 0:
        raise RuntimeError("P89 miscellaneous replacement marker was not found")
    insertion_at = marker_at + len(marker)
    text = text[:insertion_at] + "\n        " + anchor_pair + text[insertion_at:]

TARGET.write_text(text, encoding="utf-8")
Path(__file__).unlink()
print("[repair] made P89 Research Map promotion idempotent and frontier links current")
