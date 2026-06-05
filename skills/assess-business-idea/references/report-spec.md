# Report spec — interactive HTML

One self-contained REPORT.html (inline CSS/JS/data, no server, no external calls,
double-click to open). It renders the verified dossier — never re-analyses — so it
cannot introduce a claim the dossier didn't verify. Zero data loss is structural: the
full dossier data is embedded; the UI only controls visibility.

## Four layers (progressive disclosure; nothing deleted, only collapsed)
1. The Answer — verdict + adjusted score + one-sentence why. Ten-second read.
2. The Ten Axes — interactive scorecard; each axis one plain sentence; click to expand.
3. The Reasoning — per axis/phase: what we found, what it means, confidence, what would
   change the score.
4. The Atomic Evidence — every source, triangulated claim, competitor card, full panel
   transcript, integrity statement. Nothing omitted.

## Tier-1 spine (always present — comparability depends on it)
Verdict hero (score animates up); 10-axis scorecard with a live lens toggle that
re-weights and re-animates; kill-risk cards that flip to "why it could sink it / what
would de-risk it"; must-be-true assumptions as a chain showing joint fragility; visible
integrity panel; evidence drawer (any claim → source + confidence stars + triangulation
status).

## Tier-2 visuals (open-ended — the skill selects or invents per pitch)
Beyond the spine, choose the diagrams that best convey this pitch's findings. NOT a
closed list. Examples: flywheel for marketplaces; approval-timeline for regulated
plays; tech-readiness ladder for deep-tech; LTV:CAC waterfall and payback curve;
positioning map / feature matrix / analog timeline; bottom-up TAM/SAM/SOM funnel;
channel-economics tree; strength-of-evidence ladder (paid > committed > said-they'd-pay
> liked-it); trend triangulation with the why-now moment marked; risk heatmap;
assumption-dependency graph; scenario (riskiest assumption true vs. false). Invent new
ones when the content calls for it. The report states in one line why it chose each.

## Visual Selection Charter (every Tier-2 visual must pass all five)
1. Earn-its-place — include only if it makes a finding clearer than prose would.
2. Plain-Language Charter applies — labels, legends, tooltips in plain words.
3. Zero data loss — every visual is a view on the dossier data, drillable to evidence.
4. Honesty markers — directional/low-confidence visuals carry the caveat on the visual.
5. Constructive pairing — a visual showing a problem is paired with the fix/test note.

## Data contract
The generator is fed the verified dossier as JSON: the SCORECARD machine block (see
scorecard.md), kill-risks, must-be-true assumptions, per-axis reasoning + evidence,
competitor cards, panel transcript, and the integrity statement.

## Build / delegation
Delegate rendering to frontend-design (distinctive, polished, non-generic) and
data-visualization (charts). The skill owns the selection and justification (the
judgment); rendering is mechanical. Any charting library is inlined into the single
file so it stays self-contained with no external calls. The REPORT.html template is a
shell: fixed Tier-1 spine plus a flexible region populated with the chosen Tier-2
visuals.
