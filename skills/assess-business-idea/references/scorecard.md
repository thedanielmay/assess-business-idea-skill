# Scorecard — axes, weights, multiplier, machine format

## The 10 axes (plain questions)
1. Market pull — is the pain real, urgent, widespread?
2. Demand evidence — is there verified willingness to pay?
3. Go-to-market — can you reach buyers affordably, at scale?
4. Moat / defensibility — why won't this get copied to death?
5. Unit economics — does the per-customer math work?
6. Scalability — can it get big enough to matter?
7. Regulatory / legal — can a regulator switch it off?
8. Why-now / timing — what changed to make this inevitable now? (Judges the timing
   context described in Phase 0.5 Characterize — this axis SCORES it; Characterize only
   describes it.)
9. Founder-fit — do you have an unfair right to win?
10. Capital / financing path — fundable to the next proof point?

Each axis is scored out of its weight and cites the phase evidence that produced it.
An axis with no cited evidence is marked EVIDENCE GAP, scores 0 and is listed in the
verdict section. An axis with weak evidence is scored on its merits and downrated by
its confidence grade.

## Per-lens weighting (weights sum to 100 per lens)
The same evidence scores differently per lens — that is what makes lenses substantive.

| Axis | investor | founder | operator | consultant |
|---|---|---|---|---|
| Market pull | 12 | 12 | 12 | 13 |
| Demand evidence | 12 | 12 | 14 | 13 |
| Go-to-market | 9 | 10 | 14 | 11 |
| Moat / defensibility | 11 | 8 | 10 | 11 |
| Unit economics | 11 | 10 | 12 | 11 |
| Scalability | 11 | 6 | 8 | 10 |
| Regulatory / legal | 7 | 10 | 10 | 9 |
| Why-now / timing | 7 | 8 | 6 | 8 |
| Founder-fit | 15 | 14 | 6 | 6 |
| Capital / financing path | 5 | 10 | 8 | 8 |

Founder-fit carries 15 for the investor lens. The other nine investor cells give up 11
points in proportion to their size. Each gives up one point, and the two largest cells
give up one more each. The investor column still sums to 100.

When lenses are combined, render one scorecard per lens.

## Execution-risk multiplier
Count the load-bearing "must all go right" assumptions and assess their joint
fragility. Convert to a multiplier applied to the aggregate (not averaged in as an
axis, so a single fatal dependency cannot be masked by strong axes):

- 1–2 load-bearing assumptions, each plausible: ×0.95–1.00
- 3–4: ×0.85–0.95
- 5–6: ×0.70–0.85
- 7+ or any single assumption with no test path: ×0.50–0.70

adjusted = round(raw_total × multiplier)

## Verdict bands (applied to adjusted score; investor vocabulary shown)
- 75–100: GO
- 55–74: CONDITIONAL (state the conditions that would lift it to GO)
- 0–54: PASS
A fatal flaw at triage overrides the band with KILL regardless of score. List every
EVIDENCE GAP axis in this verdict section alongside the band and the score.

## Machine-readable block (REQUIRED in every SCORECARD.md)
SCORECARD.md must contain one fenced block of this shape per active lens, so a
combined-lens run has one block per lens. build_comparison.py reads every block and
ranks by one chosen lens. The HTML report consumes the block for its active lens:

```scorecard
{"idea":"<short name>","lens":"investor","raw":68,"multiplier":0.85,"adjusted":58,
 "verdict":"CONDITIONAL","axes":{"market_pull":13,"demand_evidence":11,"gtm":7,
 "moat":8,"unit_economics":9,"scalability":7,"regulatory":6,"why_now":5,
 "founder_fit":2,"capital_path":4}}
```
