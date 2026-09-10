from pathlib import Path

path = Path("README.md")
text = path.read_text(encoding="utf-8")
old = "The repository also distinguishes scientific sources from speculative antecedents. Thomas W. Campbell's *My Big TOE* is treated, where discussed, as a speculative conceptual antecedent rather than peer-reviewed established fundamental physics. It is not used as an assumption in the theorem chain. The same evidential rule applies to any proposed consciousness-first ontology: conceptual inspiration and established physical evidence are different categories."
new = "The repository also distinguishes scientific sources from speculative antecedents. Thomas W. Campbell's *My Big TOE* and similar consciousness-first proposals are **not treated as established scientific facts**. They may be discussed as speculative conceptual antecedents, but they are not used as assumptions in the theorem chain. The same evidential rule applies to any proposed consciousness-first ontology: conceptual inspiration and established physical evidence are different categories."
if old not in text:
    raise SystemExit("Expected disclaimer paragraph not found")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
