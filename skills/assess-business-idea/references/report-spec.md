# Report spec: interactive HTML

One self-contained REPORT.html (inline CSS/JS/data, no server, no external calls,
double-click to open). It renders the verified dossier and never re-analyses, so it
cannot introduce a claim the dossier didn't verify. Zero data loss is structural: the
full dossier data is embedded; the UI only controls visibility.

## Four layers (progressive disclosure; nothing deleted, only collapsed)
1. The Answer: verdict + adjusted score + one-sentence why. Ten-second read.
2. The Ten Axes: interactive scorecard; each axis one plain sentence; click to expand.
3. The Reasoning: per axis/phase, what we found, what it means, confidence, what would
   change the score.
4. The Atomic Evidence: every source, triangulated claim, competitor card, full panel
   transcript, integrity statement. Nothing omitted.

## Tier-1 spine (always present; comparability depends on it)
A "what this is" lead, meaning the Characterize product description plus customer
definition in plain language, appears BEFORE the verdict hero, so a reader learns what
the product is before seeing the score. Then: verdict hero (score animates up); 10-axis
scorecard with a live lens toggle that re-weights and re-animates; kill-risk cards that
flip to "why it could sink it / what would de-risk it"; must-be-true assumptions as a
chain showing joint fragility; visible integrity panel; evidence drawer (any claim links
to source + confidence stars + triangulation status).

## Tier-2 visuals (open-ended; the skill selects or invents per pitch)
Beyond the spine, choose the diagrams that best convey this pitch's findings. NOT a
closed list. Examples: opportunity-space map (landscape white-space plus encroachment
vectors); risk register / risk heatmap drawn from the Characterize plus Phase 5 risks;
flywheel for marketplaces; approval-timeline for regulated plays; tech-readiness ladder
for deep-tech; LTV:CAC waterfall and payback curve; positioning map / feature matrix /
analog timeline; bottom-up TAM/SAM/SOM funnel; channel-economics tree;
strength-of-evidence ladder (paid > committed > said-they'd-pay > liked-it); trend
triangulation with the why-now moment marked; risk heatmap; assumption-dependency graph;
scenario (riskiest assumption true vs. false). Invent new ones when the content calls for
it. The report states in one line why it chose each.

## Visual Selection Charter (every Tier-2 visual must pass all six)
1. Earn-its-place: include only if it makes a finding clearer than prose would.
2. Plain-Language Charter applies: labels, legends, tooltips, captions, and ALL prose in
   plain words. This includes the charter's "Scannable, not dense" and "No em dashes or
   en dashes" principles. Body prose (verdict, axis details, kill-card faces, panel
   positions, captions) is broken into short paragraphs and bulleted/numbered lists
   wherever the content is a list, and contains no em or en dashes anywhere (headings,
   captions, chart labels, list markers, and CSS `::before` content all included). Ranges
   read "X to Y", not "X-Y".
3. Zero data loss: every visual is a view on the dossier data, drillable to evidence.
4. Honesty markers: directional/low-confidence visuals carry the caveat on the visual.
5. Constructive pairing: a visual showing a problem is paired with the fix/test note.
6. Render-safe & content-sized: must render correctly in a STATIC preview (e.g. an
   image/thumbnail renderer, not just a live browser) and must never clip content.
   Concretely: do NOT build reveal/flip interactions on 3D transforms or
   `backface-visibility` (they bleed/clip in static-preview renderers). Use an
   opacity/visibility toggle with both states stacked in one CSS-grid cell so the
   container sizes to the TALLER state. Never give a card/box a fixed height that its
   text can overflow; height follows content. The interaction degrades gracefully with
   JS off (the default/front state is fully readable).

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

## Post-render check (do this before declaring the report done)
Open REPORT.html in a real browser (or a headless render) and confirm:
- Injected innerHTML regions (axis details, kill-card faces, panel positions) actually
  parsed into the intended `<p>`/`<ul>`/`<ol>` tree, not a broken string. A valid JS
  string can still produce malformed markup.
- No prose block is a wall of text; lists render as lists.
- A search for em dash and en dash characters across the whole file returns nothing in
  any visible string, including CSS `content:` values.
- The render-safe reveal still shows every face fully with no clipping.
