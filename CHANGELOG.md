# Changelog

## 1.5.2 - 2026-11-26

- A failed web search or fetch now moves to a free browser read of a public page automatically. The skill does not stop to ask for permission first.
- Site terms, rate limits, sign in and captcha rules stay in force. Paid scraping services stay opt in.
- Approval questions use the harness question tool when the user rules require one, and plain text otherwise.

## 1.5.1 - 2026-11-26

- The check for a scraping service key prints only whether it is set. It never prints the key.

## 1.5.0 - 2026-11-26

- Delegated skills use this skill's parameter step instead of their own scoping confirmation. Their output lands in `assessments/<slug>/evidence/` and `assessments/<slug>/competitors/`.
- Only the confidence grade, saturation and numeric verification sections of the shared standards file are read.
- Unit economics thresholds apply only to recurring revenue models. One-off sales, hardware and marketplaces state per unit margin and payback logic in words.
- An axis with no cited evidence is marked EVIDENCE GAP, scores 0 and appears in the verdict.
- Investor Founder-fit is now 15. The other nine investor cells give up 11 points in proportion to size.
- A jurisdiction parameter is captured and drives the legality screen.
- The comparison script reads every scorecard block and ranks by one chosen lens. Ideas without that lens are listed as not ranked.

## 1.4.0 - 2026-11-23

- Confidence now uses the two grades defined in Section 4 of INTELLIGENCE-STANDARDS.md: source reliability A to F and information credibility 1 to 6, written together (for example B2). The ⚠ flag marks a claim that another source contradicts.
- Analyst, industry, think-tank and vendor reports now carry a funder check. Record who paid for the work, who published it and any conflict of interest. A report funded by an interested party cannot grade above C for reliability on that topic.
- Flag 12 now uses likelihood words (remote, unlikely, roughly even, likely, almost certain) instead of a specific probability figure.
- The old star scale is retired. Templates, prose and the deep-tier output schemas now use the two grades and point at Section 4 of INTELLIGENCE-STANDARDS.md.

## 1.3.0 - 2026-11-23

- Layer 4 browser research is opt-in for each source. The skill names the source and why, then runs it only after the user says yes for that source.
- A user refusal or missing Playwright is logged as a gap with the reason. Availability is checked with `python3 -c "import playwright"`.
- Login and cookie reuse are removed. A source behind a login is a gap unless the user reads it and pastes what they want used.
- Stealth and user-agent spoofing are removed. Playwright runs as a normal browser that identifies as automation.
- LinkedIn is not a Layer 4 target. Use only content publicly visible without login through Layers 1 to 3, or content the user pastes.
- One access rule now governs the skill: respect each site's terms and robots rules.

## 1.2.0 - 2026-11-23

- Bundles the three shared reference files (intelligence standards, web access layers, layer 4 Playwright protocol), so the skill works without files outside the repo.

## 1.1.3 - 2026-11-23

- Adds the marketplace icon approved by Daniel (thedanielmay/agent-tools#2).

## 1.1.2 - 2026-11-23

- Marketplace file gains a description, so the full check passes again (thedanielmay/agent-tools#10).

## 1.1.1 - 2026-11-22

- Removed the duplicate root `SKILL.md`. The skill now lives only in `skills/assess-business-idea/SKILL.md`.

## 1.1.0 - 2026-11-22

- Phase 0.5 CHARACTERIZE: describe the product, customer, landscape, timing and an initial risk register before judging (`references/characterize.md`, `templates/CHARACTERIZE.md`). Phase 5 now enriches that risk register.
- Deep-tier Workflow recipe in `references/deep-tier-workflow.md`, including the warning that skills are not agent types.
- Updated the plain-language charter, report spec, scorecard, verification and dossier template.
- These changes were made on 2026-06-05 in the installed copy and were saved to this repo on 2026-11-22, with the design and plan in `docs/`.
- Added a marketplace manifest, an MIT licence and this changelog. Removed the author email from `plugin.json`.

## 1.0.0

- First published version.
