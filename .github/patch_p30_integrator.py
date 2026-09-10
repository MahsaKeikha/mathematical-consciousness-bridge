from pathlib import Path

path = Path(__file__).with_name("integrate_p30_release.py")
text = path.read_text(encoding="utf-8")

old = '''text = insert_after_line(\n    text,\n    "| **P29** | Response-geometry transport under node aggregation | complete intervention-delay TV geometry with P18 distortion control | proved |",\n    "| **P30** | Full declared P11 scale compatibility | simultaneous response-geometry, directed-influence, and partition transport under one shared scale declaration | proved assembly theorem |",\n    "README theorem table P30",\n)'''
new = '''text = insert_after_line(\n    text,\n    "| **P29** | every response-geometry entry on the fixed intervention-delay grid contracts under node aggregation",\n    "| **P30** | simultaneous response-geometry, directed-influence, and partition transport requires one shared scale declaration; zero numerical distortion cannot replace semantic compatibility | proved assembly theorem | [P30](docs/proposition_30_full_p11_scale_compatibility.md) |",\n    "README theorem table P30",\n)'''
if text.count(old) != 1:
    raise RuntimeError("P30 theorem-table patch marker not found exactly once")
text = text.replace(old, new, 1)

old = '''text = insert_after_line(\n    text,\n    "[Proposition 28](proposition_28_intervention_node_aggregation_compatibility.md) for source-label descent",\n    "15. [Proposition 29](proposition_29_response_geometry_node_aggregation.md) for complete response-geometry transport on the retained intervention-delay grid.\\n16. [Proposition 30](proposition_30_full_p11_scale_compatibility.md) for simultaneous P11 scale compatibility under one shared declaration.",\n    "navigation reading order P30",\n)\n# Remove the pre-existing P29 reading-order line that now follows the inserted block.\ntext = text.replace("15. [Proposition 29](proposition_29_response_geometry_node_aggregation.md) for complete response-geometry transport on the retained intervention-delay grid.\\n", "", 1)'''
new = '''text = replace_once(\n    text,\n    "15. [Proposition 29](proposition_29_response_geometry_node_aggregation.md) for complete response-geometry transport on the retained intervention-delay grid.",\n    "15. [Proposition 29](proposition_29_response_geometry_node_aggregation.md) for complete response-geometry transport on the retained intervention-delay grid.\\n16. [Proposition 30](proposition_30_full_p11_scale_compatibility.md) for simultaneous P11 scale compatibility under one shared declaration.",\n    "navigation reading order P30",\n)'''
if text.count(old) != 1:
    raise RuntimeError("P30 navigation patch marker not found exactly once")
text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
