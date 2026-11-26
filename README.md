# assess-business-idea skill

Exhaustive, market-based, empirical, and critical assessment of a business idea or pitch.

## What it does

Takes a business idea — a few sentences, a pitch deck, a written plan, or a founder
conversation — and runs a structured, evidence-grounded assessment that ends in a
scored verdict, a cited dossier, and an optional interactive HTML report.

It is a **thin orchestrator**. It does not re-implement market research or adversarial
critique; it delegates those to other skills (topic-intel, company-intel,
deep-research, expert-panel, fact-check-workflow, frontend-design, data-visualization)
and supplies the parts those skills don't: the business framework spine, the scorecard,
verification of its own output, and the report.

## The five lenses

The evidence is the same; the lens changes how the verdict is framed. The first four
combine freely; `compare` stands alone.

| Lens | The question it answers |
|---|---|
| founder | Should I pursue this with my own time, savings, and reputation? |
| investor *(default)* | Should I put money, time, or credibility behind this? |
| operator | We're building this — what do we de-risk next? |
| consultant | An independent, defensible read for someone else's decision |
| compare | Rank several ideas on one consistent rubric |

## Three depth tiers

All frameworks run at every tier; depth changes only how much evidence sits behind
each. `quick` (fast triage) · `standard` (default) · `deep` (multi-wave research,
per-competitor background pulls, a four-critic adversarial panel).

## The ten scored dimensions

Market pull · demand evidence · go-to-market · moat / defensibility · unit economics ·
scalability · regulatory / legal · why-now / timing · founder-fit · capital path —
each weighted differently per lens, with an execution-risk multiplier applied to the
whole so a single fatal dependency can't be hidden by strong scores.

## The pipeline

Normalize → triage gate (can kill a fatal idea in minutes) → market → demand →
competition → moat + economics + regulatory → adversarial panel → synthesize →
verify-and-integrity → finalize → optional interactive HTML report.

## How to use

```
/assess-business-idea                       walks you through every choice
/assess-business-idea "<idea or file>"      asks only for what you left unspecified
/assess-business-idea "<idea>" --depth=deep --lens=founder,investor --report
/assess-business-idea --help                prints the parameter reference, does nothing else
```

Every parameter follows one rule: if you specified it, it's used; if you were silent,
the skill asks before launching.

## Install

Install from the marketplace in this repo:

    /plugin install assess-business-idea --marketplace thedanielmay/assess-business-idea-skill

Or link a local checkout into your skills folder:

    ln -s ~/projects/agent-tools/skills/assess-business-idea-skill/skills/assess-business-idea ~/.claude/skills/assess-business-idea

Changes are in [CHANGELOG.md](CHANGELOG.md).

## Principles

- Founder claims always enter as hypotheses to verify, never as facts.
- Trends data is directional only — always triangulated, never rested on.
- The report loses no data: progressive disclosure from a ten-second answer down to the
  atomic evidence behind any single number.
- Plain language throughout — no jargon, no buzzwords, complete but clear, unflinching
  but constructive.
- A failed web search or fetch falls back to a free browser read of a public page.
  Paid scraping stays opt in. The browser never signs in or solves a captcha. A 429 means
  wait or log a gap. Each site's terms, robots rules and rate limits apply.

## Author

Daniel May
