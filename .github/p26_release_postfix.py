from pathlib import Path


def replace_once(path: str, old: str, new: str, label: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"expected one marker for {label} in {path}, found {count}"
        )
    file_path.write_text(text.replace(old, new, 1), encoding="utf-8")


replace_once(
    "docs/figures/p26_partition_irreducibility_scale_certification.svg",
    "P26 certifies one partition under compatible observation. Partition-lattice aggregation, physical fusion, full P11 scale equivalence, and experience remain open.",
    "P26 certifies one partition under compatible observation. Lattice aggregation, physical fusion, full P11 scale equivalence, and experience remain open.",
    "P26 canonical footer length",
)

replace_once(
    "docs/figures/theorem_roadmap.svg",
    "P11 partition structure + P17 contraction + P18 reconstruction",
    "P11 partition structure + P17-P18 scale control",
    "P26 roadmap heading length",
)

# The release integrator is itself executable Python. A non-raw string in an
# earlier draft encoded the leading characters of \varepsilon as a vertical tab.
# Normalize that generated README token before validation.
readme = Path("README.md")
text = readme.read_text(encoding="utf-8")
text = text.replace("\x0barepsilon_{\\pi}^{u,\\tau}", "\\varepsilon_{\\pi}^{u,\\tau}")
readme.write_text(text, encoding="utf-8")
