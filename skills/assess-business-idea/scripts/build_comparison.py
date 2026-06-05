#!/usr/bin/env python3
"""Aggregate all SCORECARD.md files under a root into a ranked RANKING.md.

Usage: build_comparison.py <assessments-root>
Reads each <root>/*/SCORECARD.md, extracts its fenced ```scorecard JSON block,
ranks by "adjusted" descending, writes <root>/_comparison/RANKING.md.
"""
import json
import os
import re
import sys

BLOCK = re.compile(r"```scorecard\s*(\{.*?\})\s*```", re.DOTALL)


def load_scorecards(root):
    cards = []
    for entry in sorted(os.listdir(root)):
        d = os.path.join(root, entry)
        sc = os.path.join(d, "SCORECARD.md")
        if entry == "_comparison" or not os.path.isfile(sc):
            continue
        m = BLOCK.search(open(sc, encoding="utf-8").read())
        if not m:
            continue
        try:
            cards.append(json.loads(m.group(1)))
        except json.JSONDecodeError:
            continue
    return cards


def render(cards):
    cards = sorted(cards, key=lambda c: c.get("adjusted", 0), reverse=True)
    lines = ["# Idea comparison — ranked", "",
             "| Rank | Idea | Adjusted score | Verdict |",
             "|---|---|---|---|"]
    for i, c in enumerate(cards, 1):
        lines.append(f"| {i} | {c.get('idea','?')} | {c.get('adjusted','?')} | {c.get('verdict','?')} |")
    lines.append("")
    return "\n".join(lines)


def main(argv):
    if len(argv) != 2:
        print("usage: build_comparison.py <assessments-root>", file=sys.stderr)
        return 2
    root = argv[1]
    cards = load_scorecards(root)
    if not cards:
        print("build_comparison: no scorecards found", file=sys.stderr)
        return 1
    out_dir = os.path.join(root, "_comparison")
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, "RANKING.md"), "w", encoding="utf-8").write(render(cards))
    print(f"build_comparison: ranked {len(cards)} ideas -> {out_dir}/RANKING.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
