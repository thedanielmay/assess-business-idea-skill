---
name: assess-business-idea
description: "Exhaustive, market-based, empirical, and critical assessment of a business idea or pitch. Use when the user wants to evaluate, validate, stress-test, or pressure-test a business idea, startup concept, or pitch deck; decide whether to pursue, fund, or back a venture; or compare several ideas. Triggers include: 'assess this idea', 'validate this business', 'is this pitch any good', 'should I pursue this', 'evaluate this startup', 'review this pitch deck', 'compare these ideas'. Produces a scored verdict, a cited dossier, and an optional interactive HTML report."
license: MIT
metadata:
  version: "1.1.0"
---

# Assess Business Idea

Announce at start: "Using assess-business-idea to run a structured, evidence-based
assessment." This skill is a thin orchestrator: it delegates research and critique to
other skills and owns the business spine, scorecard, verification, and report.

## Dependency Check
Check whether these skills are in the session's available list: topic-intel,
company-intel, deep-research, expert-panel, fact-check-workflow, frontend-design,
data-visualization, document-skills:pdf. If any are missing, name them and say each
phase that needs a missing skill will be skipped with an inline note, or the user can
say "continue anyway." If all present, proceed silently. Always read the shared spine
`~/.claude/skills/shared/references/INTELLIGENCE-STANDARDS.md` first to inherit
confidence ratings, triangulation, saturation, and numeric verification.

## Query / help mode
If invoked with --help, ?, or a question about parameters, print the full reference
from `references/parameters.md` and STOP — do no assessment.

## Parameter resolution — explicit-or-ask (the universal rule)
For every parameter (--input, --depth, --lens, --report): if the user specified it,
use it. If silent, ASK via a prompt that shows the plain-language explanation from
`references/parameters.md` so the prompt also reminds. Silence never means a silent
default. Mark the recommended option (investor lens, standard depth) first, but the
user still picks it. Fully-specified invocations run straight through; partial ones ask
only about the gaps.

## Pipeline (read references/frameworks.md, scorecard.md, verification.md as needed)
All frameworks run at every tier; depth changes research rigor only. Founder claims
enter as hypotheses to verify, never as facts. The pipeline diagram is authoritative.

- Stage 0 NORMALIZE — build the Idea Brief (claims vs. to-verify). PDFs via
  document-skills:pdf.
- Phase 0.5 CHARACTERIZE — describe before judging (REQUIRED, every tier). Product
  description, customer definition, landscape placement, why-now/timing context, initial
  risk register. Keeps the founder-claims-vs-our-characterization line clean. See
  references/characterize.md; output via templates/CHARACTERIZE.md. Downstream phases
  reference it; the report leads with the product description.
- Phase 1 TRIAGE GATE — R-W-W + fast legality screen. Fatal flaw (illegal,
  structurally-zero market, no conceivable wedge, banned) → emit KILL verdict and STOP.
- Phase 2 MARKET — delegate to topic-intel: bottom-up TAM/SAM/SOM, Five Forces, trends
  triangulation (see references/trends-sources.md; directional only).
- Phase 3 DEMAND — delegate to deep-research for adversarially-verified demand; Mom
  Test audit of founder claims; Jobs To Be Done reframe.
- Phase 4 COMPETITION — company-intel per rival; positioning map; analog case studies.
- Phase 5 MOAT+ECON+REGULATORY — 7 Powers; unit-economics sanity; regulatory/licensing/
  compliance and trajectory. Enrich the Phase 0.5 risk register into the analyzed/scored
  version here (deep tier: risk drill-down + failure scenarios).
- Phase 6 ADVERSARIAL — delegate to expert-panel (deep tier seeds a regulatory critic).
- Phase 7 SYNTHESIZE — 10-axis weighted scorecard per active lens + execution-risk
  multiplier + lens-framed verdict + dossier draft (templates/DOSSIER.md).
- Phase 7.5 VERIFY — run references/verification.md checks (input fidelity via
  fact-check-workflow, internal consistency, traceability). Deep tier: a SEPARATE
  verification sub-agent, not the synthesis author.
- Phase 8 FINALIZE — corrected dossier + SCORECARD.md (machine block from
  scorecard.md) + on-screen verdict + visible Integrity Statement.
- Phase 9 REPORT — if --report or the user assents (quick tier only on explicit
  request): build REPORT.html per references/report-spec.md (Tier-1 spine + chosen
  Tier-2 visuals), enforcing references/plain-language-charter.md and the Visual
  Selection Charter. Surface it. The Plain-Language Charter
  (references/plain-language-charter.md) also governs the whole dossier, not just the
  report.

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

## Lens routing
founder/investor/operator/consultant are combinable output transforms — render a
section per lens and flag divergence. compare is a standalone aggregation: it leads
with the scorecard and runs scripts/build_comparison.py over the assessments root to
emit _comparison/RANKING.md.

## Output
On screen always: verdict, scorecard (raw × multiplier = adjusted), top 3 kill-risks,
3 must-be-true assumptions (with joint-fragility note), cheapest next test, integrity
note, dossier path. On disk: assessments/<slug>/ with DOSSIER.md, SCORECARD.md,
idea-brief.md, evidence/, competitors/, case-studies/, panel-transcript.md, and
REPORT.html if generated.

## Missing-skill degradation
When a delegated skill is unavailable, do the best reasoned version inline and note
"(skipped — X not available)" in the relevant phase and the Integrity Statement.
