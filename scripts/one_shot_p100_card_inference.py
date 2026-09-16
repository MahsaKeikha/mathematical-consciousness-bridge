from pathlib import Path

path = Path("website/app.js")
text = path.read_text(encoding="utf-8")

old_parser = r'''  function propositionNumber(text) {
    const match = text.match(/\bP(\d{1,2})\b/i);
    return match ? Number(match[1]) : null;
  }
'''
new_parser = r'''  function propositionMentions(text) {
    return Array.from(String(text || '').matchAll(/\bP(\d{1,3})\b/gi), (match) => Number(match[1]));
  }

  function propositionNumber(text) {
    const mentions = propositionMentions(text);
    return mentions.length ? mentions[0] : null;
  }

  function hasAmbiguousPropositionText(text) {
    const value = String(text || '');
    if (/\bP\d{1,3}\s*-\s*P?\d{1,3}\b/i.test(value)) return true;
    return new Set(propositionMentions(value)).size > 1;
  }
'''
if text.count(old_parser) != 1:
    raise RuntimeError(f"expected one old proposition parser, found {text.count(old_parser)}")
text = text.replace(old_parser, new_parser, 1)

old_inferred = r'''  function inferredCardHref(card) {
    const direct = card.querySelector('a[href]');
    if (direct) return direct.href;

    const number = propositionNumber(card.textContent || '');
    if (number && propositionLinks[number]) return propositionLinks[number];
    if (number) return `research-map.html#p${number}`;

    const image = card.querySelector('img[src]');
    if (image) return image.src;
    return null;
  }
'''
new_inferred = r'''  function inferredCardHref(card) {
    const direct = card.querySelector('a[href]');
    if (direct) return direct.href;

    const text = card.textContent || '';
    if (hasAmbiguousPropositionText(text)) return null;

    const number = propositionNumber(text);
    if (number && propositionLinks[number]) return propositionLinks[number];
    if (number) return `research-map.html#p${number}`;

    const image = card.querySelector('img[src]');
    if (image) return image.src;
    return null;
  }
'''
if text.count(old_inferred) != 1:
    raise RuntimeError(f"expected one inferredCardHref block, found {text.count(old_inferred)}")
text = text.replace(old_inferred, new_inferred, 1)

old_anchor = r'''      const text = section.textContent || '';
      const number = propositionNumber(text);
      if (number) section.id = `p${number}`;
'''
new_anchor = r'''      const text = section.textContent || '';
      if (hasAmbiguousPropositionText(text)) return;
      const number = propositionNumber(text);
      if (number) section.id = `p${number}`;
'''
if text.count(old_anchor) != 1:
    raise RuntimeError(
        f"expected one research-anchor inference block, found {text.count(old_anchor)}"
    )
text = text.replace(old_anchor, new_anchor, 1)

path.write_text(text, encoding="utf-8")
