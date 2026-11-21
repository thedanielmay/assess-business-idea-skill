# Phase 0.5 — Characterize (describe before judging)

Runs between Stage 0 (Normalize) and Phase 1 (Triage). REQUIRED in every tier; depth
scales the detail, never the presence. Nothing downstream may judge what this phase has
not first described. Phase 1 (Triage), Phase 3 (Demand), Phase 4 (Competition), Phase 5
(risk enrichment) and Phase 9 (Report) all reference the artifacts produced here.

## The claims-vs-characterization rule (the reason this is its own phase)
The Stage 0 Idea Brief holds the FOUNDER's claims as hypotheses-to-verify. Characterize
holds OUR OWN neutral description. Keep the line clean: tag every element as either
`founder-stated (to verify)` or `our characterization`. Characterize never launders a
founder claim into an asserted fact — it describes the proposition as it stands, marking
what is asserted vs. what is established.

## The five required artifacts
1. **Product description** — what it is, how it actually works, the core mechanism.
2. **Customer definition** — who buys, who uses (buyer ≠ user made explicit), segmented
   with rough sizes.
3. **Landscape placement** — the category, adjacent categories, what it is an
   alternative to (including "do nothing" / a spreadsheet).
4. **Why-now / timing context** — what changed in the world to make this possible or
   relevant now: regulatory shifts, tech enablers, market events, dated forcing-
   functions. DESCRIPTION ONLY — "here is the timing situation." The scorecard why-now
   axis (#8) and Phase 5 still JUDGE whether the timing is a strength and whether the
   window is as wide as claimed. Characterize supplies the raw timing inputs the axis
   later evaluates; it does not score them.
5. **Initial risk register** — the candidate risks, plainly listed, BEFORE any are
   judged. Enriched into the analyzed/scored version at Phase 5.

## Depth scaling
| Artifact | quick | standard | deep |
|---|---|---|---|
| Product description | 1 paragraph | ~½ page | full user flows + how-it-works walkthrough + built-vs-assumed |
| Customer definition | named segments | segmented + JTBD per segment | + per-segment opportunity sizing feeding TAM/SAM/SOM |
| Landscape placement | 1 paragraph | positioning sketch | opportunity-space map (white-space, encroachment vectors, where opportunity concentrates) |
| Why-now / timing | 1–2 sentences | dated forcing-functions listed | feeds opportunity-space map + window analysis |
| Initial risk register | flat list | categorized (market / execution / regulatory / financial) | + likelihood × impact, risk drill-down + concrete failure scenarios |

## Output
Write to `assessments/<slug>/characterize.md` using `templates/CHARACTERIZE.md`. The
dossier (Phase 7) carries a Characterize section ahead of Triage; the report (Phase 9)
LEADS with the product description so a reader learns what the thing is before the
verdict.

## Deep-tier note
At deep tier the competitor profiles (Phase 4) become fuller company portraits
(structure, funding, customers, capability as a standalone profile) with the
threat/realism assessment layered on top — see `references/deep-tier-workflow.md`. The
landscape artifact becomes the opportunity-space map; the risk register becomes the risk
drill-down + scenarios.
