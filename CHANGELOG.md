# Changelog

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
