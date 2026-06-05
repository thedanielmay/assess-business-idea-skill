# Parameter reference — assess-business-idea

Single source of truth for all parameters. Read by: `--help`/query mode, the
interactive prompts, and the dossier's configuration footer.

## The universal rule: explicit-or-ask

For every parameter: if you specified it, the skill uses it. If you were silent on
it, the skill asks you before launching, showing the explanation below so the prompt
also reminds you of the options. Silence means "ask me," never "guess for me." There
is no separate interactive flag — being asked is the default for anything unspecified.
Where an option is marked "(recommended)" it is pre-selected first, but you still
actively choose it.

## --input — what you're assessing

Accepts a few sentences, a file path (pitch deck PDF, .md, .docx), a transcript, or a
reference to something shared in the conversation ("the deck I shared"). PDFs are read
via the pdf document skill. If you are silent, the skill asks for it.

## --depth — how deep the research goes

All frameworks run at every tier; depth changes only how much evidence sits behind
each one. So a quick run and a deep run are still comparable.

- quick — about ten minutes. Reasoned framework screens, light web checks, a glance at
  trends. Best for triaging a shortlist or a fast gut-check.
- standard (recommended) — real market research, a competitor teardown, one or two
  comparable case studies, and a single critical panel. Best for most assessments.
- deep — multi-wave research, deeper trend digging, a full background pull on each
  competitor, several case studies, and a four-critic adversarial panel. It runs the
  wide parts in parallel and will tell you before it does. Best for high-stakes calls.

## --lens — whose chair you're sitting in

The evidence is the same across lenses; the lens changes how the verdict is framed and
what advice you get. The first four can be combined (for example founder,investor) —
the report then shows a section for each and flags where they disagree, which is often
the most useful part. compare stands alone.

- founder — Should I pursue this with my own time, savings, and reputation? The most
  personal lens. Weighs whether you in particular have an unfair right to win, what
  else you could do with these years, and the riskiest thing to test before you quit
  your job. Ends with a plain "walk away if..." line.
- investor (recommended) — Should I put money, time, or credibility behind this? The
  most demanding lens. Gives a GO / CONDITIONAL / PASS verdict, leads with the things
  most likely to sink it, and states what would turn a CONDITIONAL into a GO.
- operator — We're committed and building this — what do we de-risk next? Assumes the
  decision to pursue is already made. Focuses on what must be true, what to test first,
  and the cheapest experiment to run this week.
- consultant — An independent, defensible read to inform someone else's decision. Holds
  back a pushed recommendation and lays out balanced reasoning with a confidence level
  on each finding.
- compare — Rank several ideas on one consistent rubric. Leads with the scorecard and
  collects results across runs into a ranked table. Cannot be combined with the others.

## --report — the interactive HTML report

Whether to build the self-contained interactive HTML report. If you are silent, the
skill asks. On the quick tier it is only built if you explicitly ask.
