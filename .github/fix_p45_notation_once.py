from pathlib import Path

path = Path("docs/proposition_45_shared_preparation_graph_allocation.md")
text = path.read_text(encoding="utf-8")
old = r"\boxed{\nu_l^*"
if text.count(old) != 1:
    raise RuntimeError(f"expected exactly one malformed P45 marker, found {text.count(old)}")
text = text.replace(old, "\\boxed{\nu_l^*", 1)
path.write_text(text, encoding="utf-8")
