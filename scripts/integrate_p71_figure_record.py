from pathlib import Path

path = Path("scripts/conceptual_figure_records.py")
text = path.read_text(encoding="utf-8")
marker = '    "docs/figures/p72_target_measurement_channel_robustness.svg": {'
record = '''    "docs/figures/p71_target_provenance_noncircularity.svg": {
        "title": "P71 target-provenance non-circularity",
        "description": (
            "What this figure shows: P71 separates mathematical factorization from scientific target provenance. The left panel shows a descriptor-derived target E=h(T), for which the exact bridge and zero conditional residual are guaranteed by construction. The right panel uses the repository's synthetic four-state example to show that a separately declared target can create a same-descriptor/different-target collision and a positive conditional residual. The lower comparison states the provenance limitation: a zero residual observed from values alone cannot establish that the target was independently specified. "
            "How to read it: read the left and right panels as contrasting target-construction protocols, follow only the attached labeled arrows, then compare the two synthetic residual cards. "
            "Main takeaway: a target manufactured from the tested descriptor cannot serve as independent evidence that the same descriptor is sufficient for that target."
        ),
        "status": (
            "Proved target-provenance non-circularity theorem plus a synthetic finite example. The synthetic target is not asserted to represent experience; passing P71 is necessary but not sufficient for a serious physical-to-experiential bridge test."
        ),
    },
'''

if record not in text:
    if marker not in text:
        raise SystemExit("P72 insertion marker not found")
    text = text.replace(marker, record + marker, 1)
    path.write_text(text, encoding="utf-8")
