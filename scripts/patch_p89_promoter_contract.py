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

# Rebuild the generated P89 Research Map section on every promotion pass.
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

# Normalize generated Research Map links after the P89 section is inserted.
research_map_start = text.find("def promote_research_map")
research_map_end = text.find("def promote_misc_website", research_map_start)
write_at = text.find("    write(path, text)", research_map_start, research_map_end)
normalizer = '    text = text.replace("index.html#p88-frontier", "index.html#p89-frontier")\n'
if normalizer not in text[research_map_start:research_map_end]:
    if write_at < 0:
        raise RuntimeError("P89 Research Map write hook was not found")
    text = text[:write_at] + normalizer + text[write_at:]

# Specialist pages can carry a link back to the current public frontier.
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

# Sources must expose the current theorem directly rather than only retaining P88
# as an older source record. Add a canonical P89 source section and relabel P88.
misc_start = text.find("def promote_misc_website")
misc_end = text.find("def assert_balanced_reader_state", misc_start)
source_hook = '''\n    sources_path = ROOT / "website/sources.html"\n    if sources_path.is_file():\n        source_text = read("website/sources.html")\n        p89_source = f\'''<section id="p89-source"><div class="section-head"><p class="eyebrow">Current theorem source · P89</p><h2>Complete real linear parity-functional duality certificate</h2><p>P89 removes the finite coefficient-radius and four-observable support restrictions of P88. It optimizes over every real linear functional of all eleven canonical P83 parity coordinates. On the established exact rational witness, the lower functional certificate and the universal convex-vertex plus zero-mass perturbation upper certificate meet at <strong>5/168</strong>, strictly above <strong>L88 = 1/64</strong>.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P89_PROOF}"><h3>Proposition 89</h3><p>Formal statement, finite-dimensional duality, exact lower and upper certificates, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P89_PROVENANCE}"><h3>P89 provenance</h3><p>Separates inherited parity algebra and convex analysis from the repository-original complete real linear certificate.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P89_IMPLEMENTATION}"><h3>P89 implementation</h3><p>Exact rational computation of the complete linear lower certificate and matching dual upper certificate.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P89_TEST}"><h3>P89 exact tests</h3><p>Exact witness, dual certificate, dominance over P88, and scientific-boundary regression tests.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{P89_FIGURE}"><h3>P89 theorem figure</h3><p>Source-controlled visual summary synchronized with the theorem and publication manifest.</p></a></div><div class="boundary"><p><strong>Scientific boundary:</strong> P89 closes only the declared real linear parity-functional class on the stated P75 box. It does not exhaust nonlinear P75 constraints, identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</p></div></section>\n\n\'''\n        source_text = remove_section(source_text, "p89-source")\n        p88_marker = '<section id="p88-source">'\n        if p88_marker not in source_text:\n            raise RuntimeError("P88 source section is missing from website/sources.html")\n        source_text = source_text.replace(\n            '<p class="eyebrow">Current theorem source · P88</p>',\n            '<p class="eyebrow">Previous theorem source · P88</p>',\n            1,\n        )\n        source_text = source_text.replace(p88_marker, p89_source + p88_marker, 1)\n        write("website/sources.html", source_text)\n'''

misc_start = text.find("def promote_misc_website")
misc_end = text.find("def assert_balanced_reader_state", misc_start)
if "p89-source" not in text[misc_start:misc_end]:
    hook_at = text.find("\n\ndef assert_balanced_reader_state", misc_start)
    if hook_at < 0:
        raise RuntimeError("P89 sources insertion hook was not found")
    text = text[:hook_at] + source_hook + text[hook_at:]

TARGET.write_text(text, encoding="utf-8")
Path(__file__).unlink()
print("[repair] finalized P89 Research Map, links, and Sources promotion")
