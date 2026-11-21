# assess-business-idea Upgrade — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a required "Characterize" phase (describe-before-judging) to the assess-business-idea skill, and harden its deep tier with a reusable Workflow recipe, an agentType-pitfall fix, and a codified regulatory-critic 3-wave panel.

**Architecture:** This skill is a thin-orchestrator (SKILL.md) + fat-references (references/*.md) + templates (templates/*) design. New heavy content goes in two NEW reference files and one NEW template; SKILL.md gains a new pipeline phase + short pointers; three existing references get small pointer/lead-in edits. No application code.

**Tech Stack:** Markdown prose (skill files) + one embedded JavaScript Workflow recipe (illustrative, inside a markdown code fence).

---

## ⚠️ Validation model for THIS plan (read first)

This plan edits a **skill**, not application code. There is **no pytest/TDD loop** and **no git** (neither `~/.claude/skills/assess-business-idea/` nor the working project is a git repo). The standard "write failing test → commit" loop does **not** apply.

Replace "run the test" with the spec's actual validation method, applied after each task:
- **Consistency check** — does the new/edited file say the same thing the rest of the skill says? (e.g. phase numbers, the claims-vs-characterization rule stated once, no contradicting another file.)
- **Reference-resolution check** — does every pointer (`references/X.md`, `templates/Y.md`, phase name) point at something that exists after this task?
- **Recipe-validity check** (Tasks touching the JS recipe) — JSON schemas are valid; agent dispatches use **only** valid agent types (`general-purpose`, `Explore`, etc.) and **never** a skill name as `agentType`; `pipeline`/`parallel` shapes are correct.

"Commit" steps are replaced by a **"Save + verify on disk"** step (the file is written; `ls`/`grep` confirms it). If the skill is later version-controlled, add commits then.

Exact paths use `SKILL_DIR = ~/.claude/skills/assess-business-idea`.

---

## File structure (decomposition locked here)

| File | Responsibility | This plan |
|---|---|---|
| `SKILL_DIR/references/characterize.md` | Phase 0.5 how-to: 5 artifacts, claims-vs-characterization rule, depth scaling | **CREATE** (Task 1) |
| `SKILL_DIR/templates/CHARACTERIZE.md` | Output structure for the 5 Characterize artifacts | **CREATE** (Task 2) |
| `SKILL_DIR/SKILL.md` | Orchestrator: insert Phase 0.5 in pipeline; pointers; agentType warning | **MODIFY** (Task 3) |
| `SKILL_DIR/references/deep-tier-workflow.md` | agentType fix + Workflow recipe + schemas + separation-of-powers + 3-wave regulatory critic | **CREATE** (Task 4) |
| `SKILL_DIR/templates/DOSSIER.md` | Add a Characterize section so the dossier describes before judging | **MODIFY** (Task 5) |
| `SKILL_DIR/references/verification.md` | Cross-pointer to deep-tier-workflow.md | **MODIFY** (Task 6) |
| `SKILL_DIR/references/report-spec.md` | Report leads with product description; opportunity-space-map + risk-register as Tier-2 visuals | **MODIFY** (Task 6) |
| `SKILL_DIR/references/scorecard.md` | One line: why-now axis references Characterize timing context | **MODIFY** (Task 6) |

Task order: create the new content first (Tasks 1–2, 4), then wire it into the orchestrator and templates (Tasks 3, 5), then the small pointer edits (Task 6), then a whole-skill consistency pass (Task 7).

---

### Task 1: Create `references/characterize.md` (the Phase 0.5 how-to)

**Files:**
- Create: `SKILL_DIR/references/characterize.md`

- [ ] **Step 1: Write the file with the full Characterize how-to**

Write exactly this content:

```markdown
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
```

- [ ] **Step 2: Save + verify on disk**

Run: `ls -la "$HOME/.claude/skills/assess-business-idea/references/characterize.md" && grep -c "required artifact" "$HOME/.claude/skills/assess-business-idea/references/characterize.md"`
Expected: file exists; grep finds the artifacts section.

- [ ] **Step 3: Consistency check**

Confirm: the five artifacts are listed; the claims-vs-characterization rule is stated; the why-now separation-of-concerns (describe vs. judge) is explicit; depth table has all 5 rows × 3 columns. No contradiction with SKILL.md's existing "Founder claims enter as hypotheses to verify, never as facts."

---

### Task 2: Create `templates/CHARACTERIZE.md` (the output structure)

**Files:**
- Create: `SKILL_DIR/templates/CHARACTERIZE.md`

- [ ] **Step 1: Write the template**

Write exactly this content:

```markdown
# Characterize — {{IDEA_NAME}}

Configuration: depth={{DEPTH}} · date={{DATE}}
> Neutral description, produced BEFORE any judging. Each element tagged
> `[founder-stated — to verify]` or `[our characterization]`.

## 1. Product description
What it is. How it actually works (core mechanism). What is built vs. assumed.

## 2. Customers
Buyer (who pays) and User (who uses) — stated separately. Segments with rough sizes.
The job each segment hires it to do.

## 3. Landscape placement
The category it sits in; adjacent categories; what it is an alternative to (incl. "do
nothing" / paper / a spreadsheet). [deep: opportunity-space map.]

## 4. Why-now / timing context
What changed to make this possible/relevant now (regulatory, technological, market,
dated forcing-functions). Description only — the why-now AXIS judges it later.

## 5. Initial risk register
| # | Risk | Category | [standard+: note] | [deep: likelihood × impact] |
|---|---|---|---|---|
| | | market / execution / regulatory / financial | | |
> Enriched into the analyzed register at Phase 5.
```

- [ ] **Step 2: Save + verify on disk**

Run: `ls -la "$HOME/.claude/skills/assess-business-idea/templates/CHARACTERIZE.md" && grep -c "## " "$HOME/.claude/skills/assess-business-idea/templates/CHARACTERIZE.md"`
Expected: file exists; grep finds 5 section headers.

- [ ] **Step 3: Consistency check**

Confirm the 5 template sections map 1:1 to the 5 artifacts in `characterize.md`, and the `{{IDEA_NAME}}`/`{{DEPTH}}`/`{{DATE}}` placeholders match the style used in `templates/DOSSIER.md`.

---

### Task 3: Wire Phase 0.5 + pointers + agentType warning into `SKILL.md`

**Files:**
- Modify: `SKILL_DIR/SKILL.md` (pipeline list ~lines 37-39; depth-modulation ~lines 63-68)

- [ ] **Step 1: Insert Phase 0.5 into the pipeline list**

Find this exact text (the Stage 0 / Phase 1 boundary):

```
- Stage 0 NORMALIZE — build the Idea Brief (claims vs. to-verify). PDFs via
  document-skills:pdf.
- Phase 1 TRIAGE GATE — R-W-W + fast legality screen. Fatal flaw (illegal,
```

Replace with:

```
- Stage 0 NORMALIZE — build the Idea Brief (claims vs. to-verify). PDFs via
  document-skills:pdf.
- Phase 0.5 CHARACTERIZE — describe before judging (REQUIRED, every tier). Product
  description, customer definition, landscape placement, why-now/timing context, initial
  risk register. Keeps the founder-claims-vs-our-characterization line clean. See
  references/characterize.md; output via templates/CHARACTERIZE.md. Downstream phases
  reference it; the report leads with the product description.
- Phase 1 TRIAGE GATE — R-W-W + fast legality screen. Fatal flaw (illegal,
```

- [ ] **Step 2: Add the risk-register enrichment note to Phase 5**

Find this exact text:

```
- Phase 5 MOAT+ECON+REGULATORY — 7 Powers; unit-economics sanity; regulatory/licensing/
  compliance and trajectory.
```

Replace with:

```
- Phase 5 MOAT+ECON+REGULATORY — 7 Powers; unit-economics sanity; regulatory/licensing/
  compliance and trajectory. Enrich the Phase 0.5 risk register into the analyzed/scored
  version here (deep tier: risk drill-down + failure scenarios).
```

- [ ] **Step 3: Add the agentType warning + recipe pointer to depth-modulation**

Find this exact text:

```
## Depth modulation
quick = reasoned + light web. standard = full single-pass delegation. deep = multi-wave
+ OSINT + company-intel per rival + 4-critic panel; wrap the parallel fan-out of Phase
4 (per-competitor + per-analog agents) and Phase 6 (4 critics) in a Workflow — STATE
the parallel dispatch and token implication and run on the user's confirmation.
quick/standard run inline, never dispatch the Workflow.
```

Replace with:

```
## Depth modulation
quick = reasoned + light web. standard = full single-pass delegation. deep = multi-wave
+ OSINT + company-intel per rival + 4-critic panel; wrap the parallel fan-out of Phase
4 (per-competitor + per-analog agents) and Phase 6 (4 critics) in a Workflow — STATE
the parallel dispatch and token implication and run on the user's confirmation.
quick/standard run inline, never dispatch the Workflow.

For the deep-tier Workflow, read references/deep-tier-workflow.md FIRST — it carries the
reusable recipe (method-injection, structured-output schemas, the per-competitor
dossier→realism pipeline, the separate verification agent, and the regulatory-critic
3-wave panel). PITFALL: `company-intel` and `expert-panel` are SKILLS, not registered
agent personas. In a Workflow, `agentType` resolves against the subagent registry
(general-purpose, Explore, …), NOT the skill list — passing a skill name as `agentType`
throws. Inject the skill's methodology into the prompt and use the default/general-
purpose agent instead.
```

- [ ] **Step 4: Save + verify on disk**

Run: `grep -n "Phase 0.5 CHARACTERIZE\|deep-tier-workflow.md\|are SKILLS, not registered" "$HOME/.claude/skills/assess-business-idea/SKILL.md"`
Expected: three matches (the phase, the pointer, the pitfall warning).

- [ ] **Step 5: Reference-resolution check**

Confirm `references/characterize.md`, `templates/CHARACTERIZE.md`, and `references/deep-tier-workflow.md` all exist (the latter is created in Task 4 — if running Task 3 before Task 4, note the pointer is forward-referencing and Task 4 must complete before the final Task 7 pass).

---

### Task 4: Create `references/deep-tier-workflow.md` (the recipe)

**Files:**
- Create: `SKILL_DIR/references/deep-tier-workflow.md`

- [ ] **Step 1: Write the recipe file**

Write exactly this content:

````markdown
# Deep-tier Workflow recipe

The deep tier wraps the Phase 4 (per-competitor) and Phase 6 (4-critic panel) fan-out in
a single Workflow, plus a SEPARATE verification agent. This file is the reusable recipe.
STATE the parallel dispatch and token implication, and run only on the user's
confirmation, before launching.

## PITFALL (this WILL bite you): skills are not agent types
`company-intel`, `expert-panel`, `topic-intel` etc. are SKILLS. In a Workflow,
`agentType` resolves against the subagent registry (`general-purpose`, `Explore`, and
any registered personas) — NOT the skill list. `agent(prompt, {agentType:
'company-intel'})` throws `agent type 'company-intel' not found`.

**Fix:** use the default workflow agent (omit `agentType`, or use `general-purpose`) and
INJECT the skill's methodology into the prompt as a short method block.

```js
const COMPANY_INTEL_METHOD = `
Apply the COMPANY-INTEL methodology: be exhaustive and transparent about what you found
AND couldn't find; every claim needs a source; triangulate across INDEPENDENT sources
(two sources citing the same original = one source); confidence ★★★ official/primary,
★★ credible independent, ★ self-reported/unverified; what the company does NOT disclose
is itself a finding; use real web research, never invent facts; cover structure/
ownership, funding/revenue, customers & scale, product capability TODAY, plus the
specific intelligence question posed.`;

const EXPERT_PANEL_METHOD = `
Apply the EXPERT-PANEL methodology: the goal is NOT consensus but surfacing failure
modes the author cannot see; an unresolved objection is a valid output; "cannot be
salvaged in current form" must be reachable; each critic speaks in a distinct voice;
severities are pre-committed and LOCKED (maintain or escalate, never soften on tone —
downgrades need explicit named justification); cross-panel tension is mandatory.`;
```

## Pipeline shape
- Phase 4: per competitor, `dossier → adversarial realism check`, PIPELINED (not
  barriered) so each competitor flows independently.
- Phase 6: the 3-wave panel runs CONCURRENTLY with Phase 4.
- Verification: a SEPARATE agent, gated BEHIND both, that did NOT author either — this is
  the deep-tier "separation of powers" (see references/verification.md). Enforce it via
  control-flow: the verifier only runs after the dossier/panel results exist and is a
  distinct `agent()` call.

## Structured-output schemas (reusable starting points)
```js
const DOSSIER_SCHEMA = { type:'object', additionalProperties:false,
  required:['name','what_it_is','ownership_structure','funding','customers_traction',
    'product_capability','key_question_answer','threat_level','confidence','sources'],
  properties:{ name:{type:'string'}, what_it_is:{type:'string'},
    ownership_structure:{type:'string'}, funding:{type:'string'},
    customers_traction:{type:'string'}, product_capability:{type:'string'},
    key_question_answer:{type:'string'},
    threat_level:{type:'string',enum:['existential','high','moderate','low','proof-of-model-positive']},
    confidence:{type:'string',enum:['★★★','★★','★']},
    sources:{type:'array',items:{type:'string'}} } };

const REALISM_SCHEMA = { type:'object', additionalProperties:false,
  required:['name','claim_tested','verdict','reasoning','revised_window_months','confidence'],
  properties:{ name:{type:'string'}, claim_tested:{type:'string'},
    verdict:{type:'string',enum:['realistic-and-near','realistic-but-slow','unlikely','speculative']},
    reasoning:{type:'string'}, revised_window_months:{type:'string'},
    confidence:{type:'string',enum:['★★★','★★','★']} } };

const PANEL_WAVE_SCHEMA = { type:'object', additionalProperties:false,
  required:['wave','critic_positions','wave_synthesis'],
  properties:{ wave:{type:'string'},
    critic_positions:{type:'array',items:{type:'object',additionalProperties:false,
      required:['critic','position','severity'],
      properties:{critic:{type:'string'},position:{type:'string'},severity:{type:'string'}}}},
    wave_synthesis:{type:'string'} } };

const VERIFICATION_SCHEMA = { type:'object', additionalProperties:false,
  required:['flags','contradictions','verdict_pressure','axis_recommendations','overall'],
  properties:{ flags:{type:'array',items:{type:'string'}},
    contradictions:{type:'array',items:{type:'string'}},
    verdict_pressure:{type:'string',enum:['confirms','mild-upward','mild-downward','material-change']},
    axis_recommendations:{type:'array',items:{type:'object',additionalProperties:false,
      required:['axis','direction','reason'],
      properties:{axis:{type:'string'},direction:{type:'string',enum:['up','down','hold']},reason:{type:'string'}}}},
    overall:{type:'string'} } };
```

## Per-competitor pipeline (Phase 4)
```js
const dossiers = await pipeline(
  COMPETITORS,
  (c) => agent(`${CONTEXT}\n${COMPANY_INTEL_METHOD}\n\nDossier on ${c.label}. Answer: ${c.q}`,
    { label:`dossier:${c.key}`, phase:'Dossiers', schema:DOSSIER_SCHEMA }),
  (dossier, c) => agent(`${CONTEXT}\n\nAdversarial realism check on this dossier:\n${JSON.stringify(dossier)}\nStress-test the load-bearing pivot/expansion claim; give a revised window in months.`,
    { label:`realism:${c.key}`, phase:'Realism', schema:REALISM_SCHEMA, agentType:'general-purpose' })
);
```

## Regulatory-critic 3-wave panel (Phase 6)
Seed the 4th critic against THE ASSESSMENT'S OWN LOAD-BEARING OPTIMISM — whatever beams
the upside rests on (e.g. a distribution channel, a funding path, a regulatory
tailwind). Run three waves, severities locked:

1. **Wave 1 — opening objections.** All four critics, each their single sharpest
   objection + pre-committed severity. The regulatory critic opens on the specific
   upside beams.
2. **Wave 2 — cross-rebuttal.** Each attacks the others' strongest claim. Force genuine
   disagreement; surface where critics cannot reconcile.
3. **Wave 3 — steel-man under fire + verdict.** The panel turns its fire on its OWN
   preferred alternative, then delivers the verdict, the surviving unresolved tensions,
   and the single piece of evidence that would most change its mind.

```js
const wave1 = await agent(`${PANEL_CONTEXT}\n${EXPERT_PANEL_METHOD}\nWAVE 1 — opening objections, severities locked.`,
  { label:'panel:wave1', phase:'Panel', schema:PANEL_WAVE_SCHEMA });
const wave2 = await agent(`${PANEL_CONTEXT}\nWAVE 1:\n${JSON.stringify(wave1)}\nWAVE 2 — cross-rebuttal. Force disagreement.`,
  { label:'panel:wave2', phase:'Panel', schema:PANEL_WAVE_SCHEMA });
const wave3 = await agent(`${PANEL_CONTEXT}\nWAVES 1-2:\n${JSON.stringify({wave1,wave2})}\nWAVE 3 — steel-man under fire + verdict.`,
  { label:'panel:wave3', phase:'Panel', schema:VERIFICATION_SCHEMA });
```

## Verification agent (separation of powers)
```js
const verification = await agent(
  `${CONTEXT}\nYou are an INDEPENDENT verifier; you did NOT author the below. Break it, don't admire it.\nDOSSIERS:\n${JSON.stringify(dossiers)}\nPANEL:\n${JSON.stringify({wave1,wave2,wave3})}\nRun input-fidelity, internal-consistency, traceability, numeric checks. State whether the evidence supports keeping the standard verdict or moving an axis, and which axis + direction.`,
  { schema:VERIFICATION_SCHEMA, agentType:'general-purpose' });
```

## Deep-tier competitor profiles
At deep tier the dossier is a fuller COMPANY PORTRAIT (structure, funding, customers,
capability as a standalone profile) with the threat/realism assessment layered ON TOP —
not instead. The `what_it_is` / `ownership_structure` / `funding` / `customers_traction`
/ `product_capability` fields carry the portrait; `key_question_answer` + the realism
check carry the threat assessment.
````

- [ ] **Step 2: Save + verify on disk**

Run: `grep -n "skills are not agent types\|EXPERT_PANEL_METHOD\|Wave 3 — steel-man\|separation of powers" "$HOME/.claude/skills/assess-business-idea/references/deep-tier-workflow.md"`
Expected: matches for the pitfall heading, the method block, the wave-3 step, and separation-of-powers.

- [ ] **Step 3: Recipe-validity check**

Read every `agent(...)` call in the file. Confirm: (a) NO call passes a skill name as `agentType` — only `general-purpose` appears (or `agentType` is omitted); (b) each schema referenced (`DOSSIER_SCHEMA`, `REALISM_SCHEMA`, `PANEL_WAVE_SCHEMA`, `VERIFICATION_SCHEMA`) is defined in the file; (c) `pipeline(...)` has the item list + two stage callbacks; (d) the verifier is a separate call after the dossier/panel results. Fix any mismatch inline.

---

### Task 5: Add a Characterize section to `templates/DOSSIER.md`

**Files:**
- Modify: `SKILL_DIR/templates/DOSSIER.md` (between the Idea Brief and Phase 1 Triage)

- [ ] **Step 1: Insert the Characterize section**

Find this exact text:

```
## Idea Brief (normalized input)
Claims vs. to-verify, problem, customer, solution, model, competitors, gaps.

## Phase 1 — Triage
R-W-W screen and fast legality screen. {{TRIAGE_RESULT}}
```

Replace with:

```
## Idea Brief (normalized input)
Claims vs. to-verify, problem, customer, solution, model, competitors, gaps.

## Characterize (describe before judging)
Product description (what it is, how it works); customers (buyer ≠ user, segmented);
landscape placement; why-now / timing context; initial risk register. Each element
tagged founder-stated-to-verify vs. our-characterization. Full detail in
characterize.md. {{CHARACTERIZE_SUMMARY}}

## Phase 1 — Triage
R-W-W screen and fast legality screen. {{TRIAGE_RESULT}}
```

- [ ] **Step 2: Save + verify on disk**

Run: `grep -n "Characterize (describe before judging)\|CHARACTERIZE_SUMMARY" "$HOME/.claude/skills/assess-business-idea/templates/DOSSIER.md"`
Expected: two matches.

- [ ] **Step 3: Consistency check**

Confirm the section sits AFTER Idea Brief and BEFORE Phase 1 Triage (so the dossier describes before it judges), matching the Phase 0.5 placement in SKILL.md.

---

### Task 6: Small pointer edits to three existing references

**Files:**
- Modify: `SKILL_DIR/references/verification.md` (separation-of-powers section)
- Modify: `SKILL_DIR/references/report-spec.md` (Tier-1 spine + Tier-2 visuals)
- Modify: `SKILL_DIR/references/scorecard.md` (why-now axis line)

- [ ] **Step 1: verification.md — add the recipe cross-pointer**

Find this exact text:

```
## Separation of powers (deep tier)
On the deep tier, a separate verification sub-agent runs these checks — not the agent
that authored the synthesis. Don't grade your own homework.
```

Replace with:

```
## Separation of powers (deep tier)
On the deep tier, a separate verification sub-agent runs these checks — not the agent
that authored the synthesis. Don't grade your own homework. See
references/deep-tier-workflow.md for the Workflow mechanism that enforces this (the
verifier is a distinct agent gated behind the dossier/panel results, sharing none of
their authorship).
```

- [ ] **Step 2: report-spec.md — report leads with the product description**

Find this exact text (the Tier-1 spine paragraph opener):

```
## Tier-1 spine (always present — comparability depends on it)
Verdict hero (score animates up); 10-axis scorecard with a live lens toggle that
```

Replace with:

```
## Tier-1 spine (always present — comparability depends on it)
A "what this is" lead — the Characterize product description + customer definition in
plain language — appears BEFORE the verdict hero, so a reader learns what the product is
before seeing the score. Then: verdict hero (score animates up); 10-axis scorecard with
a live lens toggle that
```

Then find this exact text (the Tier-2 examples list — locate the sentence beginning "Examples:"):

```
Examples: flywheel for marketplaces; approval-timeline for regulated
plays; tech-readiness ladder for deep-tech; LTV:CAC waterfall and payback curve;
```

Replace with:

```
Examples: opportunity-space map (landscape white-space + encroachment vectors); risk
register / risk heatmap drawn from the Characterize + Phase 5 risks; flywheel for
marketplaces; approval-timeline for regulated plays; tech-readiness ladder for deep-tech;
LTV:CAC waterfall and payback curve;
```

- [ ] **Step 3: scorecard.md — why-now axis references Characterize timing context**

Find this exact text (axis #8 in the plain-questions list):

```
8. Why-now / timing — what changed to make this inevitable now?
```

Replace with:

```
8. Why-now / timing — what changed to make this inevitable now? (Judges the timing
   context described in Phase 0.5 Characterize — this axis SCORES it; Characterize only
   describes it.)
```

- [ ] **Step 4: Save + verify on disk**

Run: `grep -n "deep-tier-workflow.md" "$HOME/.claude/skills/assess-business-idea/references/verification.md" && grep -n "what this is\" lead\|opportunity-space map" "$HOME/.claude/skills/assess-business-idea/references/report-spec.md" && grep -n "Characterize" "$HOME/.claude/skills/assess-business-idea/references/scorecard.md"`
Expected: one match in verification.md; two in report-spec.md; one in scorecard.md.

- [ ] **Step 5: Consistency check**

Confirm none of these edits changed any NUMBER, weight, multiplier, or verdict band in scorecard.md (the spec forbids scoring-semantics changes — this is a descriptive pointer only).

---

### Task 7: Whole-skill consistency + reference-resolution pass

**Files:**
- Read-only pass over all of `SKILL_DIR`

- [ ] **Step 1: Reference-resolution sweep**

Run: `cd "$HOME/.claude/skills/assess-business-idea" && grep -rno "references/[a-z-]*\.md\|templates/[A-Z]*\.md" SKILL.md references/ templates/ | sort -u`
For each referenced path, confirm the file exists. Expected: `references/characterize.md`, `references/deep-tier-workflow.md`, `templates/CHARACTERIZE.md` (the new ones) all resolve, alongside the pre-existing references.

- [ ] **Step 2: Phase-numbering consistency**

Confirm "Phase 0.5 CHARACTERIZE" appears in SKILL.md's pipeline between Stage 0 and Phase 1, and that `characterize.md`, `templates/CHARACTERIZE.md`, `templates/DOSSIER.md` all describe the same five artifacts in the same order (product, customers, landscape, why-now, risk register). Fix any drift.

- [ ] **Step 3: claims-vs-characterization stated once, referenced consistently**

Confirm the rule is DEFINED in `characterize.md` and merely REFERENCED (not redefined differently) in SKILL.md and the DOSSIER template. No contradicting wording.

- [ ] **Step 4: agentType pitfall consistency**

Confirm the agentType warning appears in BOTH SKILL.md (short form) and deep-tier-workflow.md (full form), and they don't contradict (both say: skills ≠ agent types; inject method + use general-purpose/default).

- [ ] **Step 5: Plain-Language Charter spot-check**

Read the new prose in `characterize.md` and `deep-tier-workflow.md`. Confirm plain words, no unexplained jargon, consistent with `references/plain-language-charter.md`.

- [ ] **Step 6: Final on-disk manifest check**

Run: `cd "$HOME/.claude/skills/assess-business-idea" && ls references/characterize.md references/deep-tier-workflow.md templates/CHARACTERIZE.md && grep -c "Phase 0.5" SKILL.md`
Expected: three files listed; at least one "Phase 0.5" in SKILL.md.

---

## Self-review (run by plan author after writing — recorded here)

**Spec coverage:** §3.1 Characterize → Tasks 1,2,3,5. §3.2 deep-tier hardening (agentType, recipe, schemas, separation-of-powers, 3-wave critic) → Tasks 3,4. §3.3 deep-tier enrichment (portraits, opportunity-space map, risk drill-down) → Task 4 + characterize.md depth table + report-spec.md. §3.4 cleanup pointers → Task 6. File manifest → all 8 files have a task. Out-of-scope items (split-window, multiplier fix, augment-protocol) → correctly absent. ✓

**Placeholder scan:** No TBD/TODO. Template `{{...}}` placeholders are intentional (they're template variables, matching DOSSIER.md's existing style), not plan gaps. ✓

**Type/name consistency:** Schema names (`DOSSIER_SCHEMA`, `REALISM_SCHEMA`, `PANEL_WAVE_SCHEMA`, `VERIFICATION_SCHEMA`) are defined once in Task 4 and referenced consistently. The five artifacts use the same names and order in Tasks 1, 2, 5, 7. "Phase 0.5 CHARACTERIZE" identical across Tasks 3, 5, 7. ✓

**Forward-reference note:** Task 3 Step 5 flags that SKILL.md points at deep-tier-workflow.md (created in Task 4); Task 7 Step 1 re-verifies resolution after all files exist. ✓
```
