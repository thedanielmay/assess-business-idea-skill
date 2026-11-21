# Phase 7.5: verify and integrity

The research skills verify the world (inherited INTELLIGENCE-STANDARDS spine:
confidence ratings, triangulation, numeric verification; plus deep-research's
adversarial verification). Nobody upstream verifies our own output, so that is this
phase's job. Run it adversarially: a skeptic trying to break the dossier, not an
author admiring it.

## Check 1: input fidelity
Re-read the original input. Tag every founder claim verified / refuted / unverifiable,
each pointing to its evidence. Invoke fact-check-workflow on the founder's factual
claims (its claim, evidence, rating loop). If unavailable, note inline
"(skipped, fact-check-workflow not available)" and do the rating manually.

## Check 2: internal consistency
- Does the headline verdict follow from the scorecard? (Flag a 78/100 that says PASS.)
- Do any two phases contradict? (Big market vs. no scalable channel: surface it.)
- Does every scorecard axis cite the phase evidence behind its number?
- Run the numeric verification protocol on the dossier's own numbers.

## Check 3: traceability
Every load-bearing statement traces to a triangulated, confidence-rated finding or an
explicitly flagged assumption. Anything else is marked "⚠ unsupported" and either
sourced or downgraded. No naked assertions in the verdict.

## Check 4: presentation compliance (Plain-Language Charter)
The charter is binding, not advisory, so verify it like any other contract. Across the
whole dossier and especially the HTML report:
- Jargon defined at first use; no buzzwords; explanatory, not just terse.
- Scannable: no wall-of-text paragraphs; genuine lists rendered as bullets or numbered
  lists, not run-on semicolon sentences.
- Zero em dashes and zero en dashes anywhere, including headings, captions, chart labels,
  list markers, and CSS `content:` values. Ranges read "X to Y". Grep the file to confirm.
- In the report, injected innerHTML regions parsed into the intended tag tree (a valid JS
  string can still emit broken markup), and the render-safe reveal clips nothing. Confirm
  in a real or headless browser, not by reading source alone.

## Separation of powers (deep tier)
On the deep tier, a separate verification sub-agent runs these checks, not the agent
that authored the synthesis. Don't grade your own homework. See
references/deep-tier-workflow.md for the Workflow mechanism that enforces this (the
verifier is a distinct agent gated behind the dossier/panel results, sharing none of
their authorship).

## Integrity Statement (surfaced, not appendixed)
The dossier carries a visible Integrity Statement: what was verified, what couldn't be,
where confidence is thin, and any unresolved internal tensions.
