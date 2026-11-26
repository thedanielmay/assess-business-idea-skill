# Trends and demand-signal sources

Trend data is directional only. Never rest a conclusion on it; always triangulate
across at least two independent signals. Every trend visual carries this caveat.

## Google Trends
Run `scripts/google_trends.py "<term>" ["<term2>" ...]` for interest-over-time JSON.
If it returns {"status":"unavailable",...}, record Google Trends as a gap with the reason.
If the script fails, move to a free browser read of the public trends.google.com page
automatically. Do not stop to ask. Check availability with `python3 -c "import playwright"`
first. If that fails, say Playwright is not installed and leave the gap in place. Never sign
in or solve a captcha. Ask the user before a paid service. A 429 response means wait
or log the gap, not a browser read. Treat both the script result and any browser read as
directional.

## Triangulation sources (use several, note independence)
- Reddit, niche forums, review sites (G2, Capterra, app stores) — unfiltered
  complaints = real pain and incumbent weakness.
- Funding flows (Crunchbase-style, via research-intel, company mode) — where smart money is moving.
- Job postings and patents (OSINT, via research-intel, topic mode) — what incumbents are quietly
  building.
- Exploding-topics-style early-signal sites — rising niches.

## The directional-only rule
Trends modify confidence on the Why-now / timing axis. They never stand alone as proof
of demand — that is what the deep-research demand verification in Phase 3 is for.
