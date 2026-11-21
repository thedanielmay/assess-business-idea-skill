# Plain-Language Charter (binding)

Governs the entire dossier; enforced hardest in the HTML report. The verification
phase checks compliance.

## No jargon
Define every term in plain words at first use, or don't use it. Not "TAM" but "the
total number of people who could ever buy this, and what that's worth." Not "moat" but
"what stops a competitor copying you." Not "GTM" but "how you actually reach customers."

## No buzzwords or slick business-speak
Banned register includes: leverage, synergies, disrupt, unlock value, move the needle,
best-in-class, paradigm, and vague uses of "at scale." If a sentence would sound at
home in a consultant's deck, rewrite it plainly.

## Complete, not simplified
Plain is not dumbed-down. Every detail stays; only the wording is made clear. Never
thin the content to make it readable. Make the words clear instead.

## Explanatory, not just terse
Plain wording is necessary but NOT sufficient. A sentence can use only common words and
still assume the reader already knows why it matters. Write to EXPLAIN, not just to
state. Each finding should walk the reader through three steps: the situation, then why
it matters, then what it means for this venture. Don't just name a mechanism, explain how
it works the first time it appears. For example, not "the accountability paradox" full
stop, but "the people who would pay for this are the institutions it is designed to hold
accountable, so you are asking them to buy something that constrains them. That is the
accountability paradox." Spell out and define every acronym at first use (WTP =
willingness to pay; ARR = annual recurring revenue, the predictable yearly subscription
income). Use a short analogy or worked example when a concept is abstract. Assume an
intelligent reader with ZERO domain knowledge of startups, the sector, or finance. The
test: could a smart board member or community member who has never seen a pitch deck
follow every sentence? This adds connective tissue and the occasional defining clause. It
does NOT mean padding, repetition, or hedging. Tight AND explanatory, not one at the cost
of the other.

## Unflinching but constructive
Name flaws plainly, without softening. Then, wherever possible, say what would fix the
flaw or what cheap test would settle it. Critical and solution-oriented together, never
just one.

## Scannable, not dense
Plain words in a wall of text still read as a wall. Break prose up so a reader can skim
the shape of the argument before reading it in full.
- Keep paragraphs short: 2 to 4 sentences. One idea per paragraph. When a paragraph
  turns to a new point (situation, then why, then what it means), start a new paragraph.
- Whenever content is genuinely a list (drivers, risks, conditions, the fronts of a
  problem, the steps of a test), render it as a bulleted or numbered list with a short
  lead-in line, NOT as a run-on sentence with semicolons. Bold the lead phrase of each
  item when the items have a name ("**The sales cycle.** ...").
- Judge each block on its merits: bullet the true enumerations, keep flowing argument as
  short paragraphs. Don't bullet everything; don't bullet nothing.
- In the HTML report this applies inside expandable regions too (axis details, kill-card
  faces, panel positions). Because those are injected via innerHTML, use real `<p>`,
  `<ul>`, and `<ol>` tags, not one long string. Verify they render (a valid JS string can
  still produce broken markup).

## No em dashes or en dashes; hyphens sparingly
This is a hard typographic rule, enforced across the whole dossier and the report,
including headings, captions, chart labels, list markers, and CSS `::before` content.
- NEVER use an em dash or an en dash, anywhere, for any purpose. Not as an aside, not as
  a citation marker, not as a list bullet, not in a range.
- Recast every construction that would have used one. An aside becomes a comma pair, a
  colon, or its own sentence. A number range becomes "X to Y" ("6 to 18 months", not
  "6-18"). A citation attribution drops the leading dash (style it with a CSS marker like
  a guillemet if a visual cue is wanted).
- Hyphens are allowed ONLY in genuine compound modifiers (faith-based, survivor-led,
  purpose-built, role-based) and should be used sparingly. Do not hyphenate where two
  separate words read fine.
- The skill's own reference files follow this rule too: a charter that bans dashes must
  not contain them.
