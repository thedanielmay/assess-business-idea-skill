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
(two sources citing the same original = one source); grade each claim with the two grades
in Section 4 of INTELLIGENCE-STANDARDS.md, source reliability A to F and information
credibility 1 to 6 written together (for example B2), with ⚠ for a claim another source
contradicts; official or primary sources rate A, credible independent sources B,
self-reported or unverified sources C or lower; what the company does NOT disclose
is itself a finding; use real web research, never invent facts; respect each site's terms,
robots rules and rate limits; a 429 response means wait or log the source as a gap, never a
browser read; when a web search or fetch fails, move to a free browser read of a public page
automatically and name the source and why; log a failed browser read or missing Playwright
as a gap with the reason; never solve a captcha, and log a captcha as a gap unless a person can
reach the page; use no paid scraping service without the user's yes; never log in to a source,
never use LinkedIn, and never reuse session cookies; never use stealth tools or user-agent
spoofing; for a sensitive integrity investigation, confirm with the user before any Layer 4; cover
structure/ownership, funding/revenue, customers & scale, product capability TODAY, plus the
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
    'product_capability','key_question_answer','threat_level','grade','sources'],
  properties:{ name:{type:'string'}, what_it_is:{type:'string'},
    ownership_structure:{type:'string'}, funding:{type:'string'},
    customers_traction:{type:'string'}, product_capability:{type:'string'},
    key_question_answer:{type:'string'},
    threat_level:{type:'string',enum:['existential','high','moderate','low','proof-of-model-positive']},
    grade:{type:'string',pattern:'^[A-F][1-6]$'},
    sources:{type:'array',items:{type:'string'}} } };

const REALISM_SCHEMA = { type:'object', additionalProperties:false,
  required:['name','claim_tested','verdict','reasoning','revised_window_months','grade'],
  properties:{ name:{type:'string'}, claim_tested:{type:'string'},
    verdict:{type:'string',enum:['realistic-and-near','realistic-but-slow','unlikely','speculative']},
    reasoning:{type:'string'}, revised_window_months:{type:'string'},
    grade:{type:'string',pattern:'^[A-F][1-6]$'} } };

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

// Wave 3 is a PANEL wave (steel-man under fire + verdict), NOT the verifier — it needs
// its own schema, not VERIFICATION_SCHEMA. (Common copy-paste trap.)
const WAVE3_SCHEMA = { type:'object', additionalProperties:false,
  required:['steelman_target','steelman_under_fire','panel_verdict','surviving_tensions','evidence_that_changes_mind'],
  properties:{ steelman_target:{type:'string',description:"the panel's own preferred alternative, now under attack"},
    steelman_under_fire:{type:'string',description:'does the alternative survive the panel turning its fire on it?'},
    panel_verdict:{type:'string'},
    surviving_tensions:{type:'array',items:{type:'string'},description:'unresolved by design — do not smooth'},
    evidence_that_changes_mind:{type:'string',description:'the single artefact that would most move the verdict'} } };
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
  { label:'panel:wave3', phase:'Panel', schema:WAVE3_SCHEMA });
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