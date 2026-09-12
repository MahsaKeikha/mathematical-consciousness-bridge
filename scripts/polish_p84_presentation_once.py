from pathlib import Path

path = Path("website/implementation.html")
text = path.read_text(encoding="utf-8")
duplicated = (
    "P73-P84 build a continuous chain from channel recovery to certified model-family separation. "
    "P73-P84 build a continuous chain from channel recovery to certified model-family separation. "
)
text = text.replace(
    duplicated,
    "P73-P84 build a continuous chain from channel recovery to certified model-family separation. ",
)
path.write_text(text, encoding="utf-8")
