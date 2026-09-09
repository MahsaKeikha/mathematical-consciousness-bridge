from pathlib import Path

path = Path(".github/integrate_p20_release.py")
lines = path.read_text(encoding="utf-8").splitlines()

label_index = next(
    index for index, line in enumerate(lines) if '"roadmap dependency chain"' in line
)
start = label_index
while start >= 0 and lines[start].strip() != "replace_once(":
    start -= 1
if start < 0:
    raise RuntimeError("could not locate roadmap dependency replacement call")
end = label_index
while end < len(lines) and lines[end].strip() != ")":
    end += 1
if end >= len(lines):
    raise RuntimeError("could not locate end of roadmap dependency replacement call")

replacement = r'''replace_once(
    "docs/theorem_roadmap.md",
    r"""&\text{P17-P18: scale loss + scale sufficiency}.
\end{aligned}""",
    r"""&\text{P17-P18: scale loss + scale sufficiency}\\
&\Downarrow\\
&\text{P19: population physical sufficiency}\\
&\Downarrow\\
&\text{P20: finite-sample residual certification}.
\end{aligned}""",
    "roadmap dependency chain",
)'''.splitlines()

lines[start : end + 1] = replacement
path.write_text("\n".join(lines) + "\n", encoding="utf-8")
