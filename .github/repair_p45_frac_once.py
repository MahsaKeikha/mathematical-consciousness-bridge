from pathlib import Path

path = Path("docs/proposition_45_shared_preparation_graph_allocation.md")
text = path.read_text(encoding="utf-8")
needle = "\x0crac{"
count = text.count(needle)
if count != 2:
    raise RuntimeError(f"expected exactly two corrupted P45 fraction markers, found {count}")
text = text.replace(needle, "\\frac{")
if "\x0c" in text:
    raise RuntimeError("form-feed remains after P45 repair")
path.write_text(text, encoding="utf-8")
