# Design Spec — `assess-business-idea` Upgrade

**Date:** 2026-06-05
**Status:** Approved design, pending implementation plan
**Origin:** Friction + gaps observed during a real deep-tier run (FaithSafe assessment, 2026-06-05). Every change traces to an observed gap.

---

## 1. Problem statement

Two classes of problem surfaced from a live deep-tier run:

**(A) The skill judges before it describes.** The pipeline goes Normalize (founder's claims-to-verify) → Triage (verdict) → … . It never produces a clear, neutral account of *what the product is, how it works, who buys it, why now, or what the risks are* before it starts judging. A reader who didn't already know the business could not learn it from the output. The FaithSafe DOSSIER opened with the verdict; the idea-brief was a normalized-input stub. This is a structural gap, not a one-run accident.

**(B) The deep tier is under-specified and has a latent bug.** The skill says "wrap the deep-tier fan-out in a Workflow" but: (1) gives no recipe for *how*, so the orchestration must be reinvented each run; (2) contains a latent failure — `company-intel`/`expert-panel` are **skills, not registered agent personas**, so passing them as `agentType` throws (this run's first Workflow dispatch failed on exactly this); (3) reduces the regulatory-seeded critic to a single clause despite it being one of the highest-value parts of the run.

## 2. Goals / non-goals

**Goals**
- Every assessment *describes before it judges*: product, customers, landscape, why-now, and risks are established as neutral foundation before the first verdict.
- The deep tier is repeatable from a written recipe, not reinvented.
- The `agentType` pitfall is documented with the working pattern.
- The regulatory-seeded 3-wave panel is codified.
- Preserve the skill's thin-orchestrator / fat-references design.
- Preserve cross-assessment comparability: **no scoring-semantics changes.**

**Non-goals (explicitly out of scope — logged as future work)**
- Split-window scoring framework (`frameworks.md`).
- The "execution-risk multiplier swallows axis movement" scoring fix (`scorecard.md`).
- Any "augment / resume a completed assessment at a higher tier" protocol.
- Changing the FaithSafe assessment itself — the re-run is handled *after* this upgrade; mode TBD.

## 3. Design

### 3.1 New Phase 0.5 — "Characterize" (describe before judging)

Inserted between Stage 0 (Normalize) and Phase 1 (Triage). **Required in every tier**; depth scales. Downstream phases reference it.

**Five required artifacts:**

| Artifact | Answers | quick / standard / deep |
|---|---|---|
| Product description | What is it? How does it actually work? Core mechanism? | 1 para / ~½ page / full user flows + how-it-works walkthrough + built-vs-assumed |
| Customer definition | Who buys, who uses (buyer ≠ user explicit), segmented + rough sizes | named segments / segmented + JTBD per segment / + per-segment opportunity sizing feeding TAM/SAM/SOM |
| Landscape placement | Category, adjacent categories, what it's an alternative to | 1 para / positioning sketch / **opportunity-space map** |
| Why-now / timing context | What changed in the world to make this possible/relevant now (neutral factual context: regulatory shifts, tech enablers, dated forcing-functions) | 1–2 sentences / dated forcing-functions listed / feeds opportunity-space map + window analysis |
| Initial risk register | Candidate risks, plainly listed, before any are judged | flat list / categorized (market/exec/regulatory/financial) / + likelihood×impact, **risk drill-down + scenarios** |

**Critical rule — keep the claims/analysis line clean.** The Idea Brief (Stage 0) holds the *founder's* claims as hypotheses-to-verify. Characterize holds *our own neutral description*, explicitly tagging each element as `founder-stated (to verify)` vs. `our characterization`. This is why Characterize is a separate phase, not a fatter Idea Brief — it preserves the existing discipline that founder claims never enter as facts.

**Separation of concerns with downstream "why-now":** Characterize *describes* the timing context ("here is the situation"). Scorecard axis #8 and Phase 5 still *judge* it ("is the timing a strength; is the window as wide as claimed"). Describe vs. judge — same line as the other artifacts. No duplication: Characterize provides the raw timing inputs the axis later evaluates.

**Downstream wiring:**
- Phase 1 (Triage) references the Characterize product description instead of re-deriving it.
- Phase 3 (Demand) references the customer definition.
- Phase 4 (Competition) references the landscape placement.
- Phase 5 (Moat/Econ/Regulatory) **enriches** the risk register into the analyzed/scored version (deep tier: + drill-down + scenarios).
- Phase 9 (Report) **leads** with the product description — the report opens by telling the reader what the thing *is* before the verdict.

### 3.2 Deep-tier hardening (Theme A)

Lives in a new `references/deep-tier-workflow.md`, pointed to from SKILL.md's depth-modulation section.

**A1 — `agentType` pitfall fix.** Warning + working pattern:
> Skills ≠ agent types. In a Workflow, `agentType` resolves against the subagent registry (general-purpose, Explore, …), NOT the skill list. To apply a skill's methodology inside a workflow agent, **inject the method into the prompt and use the default/general-purpose agent** — do not pass the skill name as `agentType`.

**A2 — Reusable deep-tier Workflow recipe.** Codifies the pattern this run proved:
- **Method-injection blocks** — short `COMPANY_INTEL_METHOD` / `EXPERT_PANEL_METHOD` prompt snippets (confidence ratings, triangulation, "what they don't say is a finding") injected into default-agent prompts.
- **Pipeline shape** — per-competitor `dossier → adversarial realism check` (pipelined, not barriered); panel runs concurrently; verifier gated behind both.
- **Structured-output schemas** — reusable starting schemas: dossier, realism check, panel-wave, verification.
- **Separation of powers** — the verification agent must NOT author the synthesis; the recipe shows how Workflow control-flow enforces it (`verification.md` mandates this but doesn't show the mechanism).

**A3 — Regulatory-critic 3-wave panel structure.**
- **Seeding** — seed the 4th critic to stress-test *the specific beams the assessment's upside hangs on* (general pattern: seed against the assessment's own load-bearing optimism).
- **3 waves** — opening objections (severities pre-committed, **locked**) → cross-rebuttal (each attacks the others' strongest claim) → steel-man-under-fire (the panel attacks its *own* preferred alternative) + verdict.
- **Locked-severity discipline** — maintain or escalate, never soften on tone; downgrades require explicit named justification.

### 3.3 Deep-tier enrichment of the Characterize artifacts
- **Competitor dossiers → fuller company portraits**: structure, funding, customers, product capability *as a standalone profile*, with the threat/realism assessment layered on top (not instead).
- **Landscape → opportunity-space map**: white-space, adjacent-category encroachment vectors, where customer opportunity concentrates.
- **Risk register → risk drill-down + scenarios**: enriched register + concrete failure scenarios as a first-class artifact (not buried in the panel transcript).

### 3.4 Structural cleanup (pointers only, no content moves)
- `verification.md` → cross-pointer to `deep-tier-workflow.md` (separation-of-powers mechanism).
- SKILL.md's expert-panel reference → pointer to the 3-wave spec, so the deep tier is followable as one coherent procedure.

## 4. File manifest

| File | Change |
|---|---|
| `SKILL.md` | Add Phase 0.5 to pipeline; pointers to `characterize.md` + `deep-tier-workflow.md`; `agentType` warning line in depth-modulation |
| `references/characterize.md` | **NEW** — Phase 0.5 how-to, 5 artifacts, claims-vs-characterization rule, depth scaling |
| `references/deep-tier-workflow.md` | **NEW** — agentType fix, Workflow recipe, schemas, separation-of-powers, regulatory-critic 3-wave spec |
| `templates/CHARACTERIZE.md` | **NEW** — output structure for the 5 artifacts |
| `references/verification.md` | Cross-pointer to `deep-tier-workflow.md` |
| `references/report-spec.md` | Report leads with product description; Tier-2 visuals may include opportunity-space map + risk register |
| `references/scorecard.md` | One line: why-now axis references the Characterize timing context (no scoring change) |

## 5. Testing / validation

This is a skill (prose + a JS recipe). Validation =
1. The recipe's example Workflow script is internally consistent: valid JSON schemas, **valid agent types only** (no skill-name `agentType`), pipeline/parallel shapes correct.
2. Dry read-through of the full pipeline: Phase 0.5 references resolve downstream, no phase contradicts another, the claims-vs-characterization rule is stated once and referenced.
3. Plain-Language Charter still satisfied by new prose.

No code units to test.

## 6. Open future work (captured, not built)
- Split-window competitive-window framework.
- Multiplier-vs-axis scoring fix (so real axis movement isn't masked by the execution-risk multiplier).
- Augment/resume protocol for re-running a completed assessment at a higher tier.

---

*Note: the skill directory is not a git repo and neither is the working project, so this spec is saved alongside the skill it documents rather than committed. If the skill is later version-controlled, move/commit accordingly.*
