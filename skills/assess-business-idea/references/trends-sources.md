# Trends and demand-signal sources

Trend data is directional only. Never rest a conclusion on it; always triangulate
across at least two independent signals. Every trend visual carries this caveat.

## Google Trends
Run `scripts/google_trends.py "<term>" ["<term2>" ...]` for interest-over-time JSON.
If it returns {"status":"unavailable",...}, fall back to the Playwright browser on
trends.google.com (navigate, read the interest-over-time chart). Treat both as
directional.

## Triangulation sources (use several, note independence)
- Reddit, niche forums, review sites (G2, Capterra, app stores) — unfiltered
  complaints = real pain and incumbent weakness.
- Funding flows (Crunchbase-style, via company-intel) — where smart money is moving.
- Job postings and patents (OSINT, via topic-intel) — what incumbents are quietly
  building.
- Exploding-topics-style early-signal sites — rising niches.

## The directional-only rule
Trends modify confidence on the Why-now / timing axis. They never stand alone as proof
of demand — that is what the deep-research demand verification in Phase 3 is for.
