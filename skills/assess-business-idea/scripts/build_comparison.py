#!/usr/bin/env python3
"""Aggregate all SCORECARD.md files under a root into a ranked RANKING.md.

Usage: build_comparison.py <assessments-root> [lens]
Reads every fenced ```scorecard JSON block in each <root>/*/SCORECARD.md. Ranks by
one lens only. With no lens argument, the default is the lens of the first block of
the first scorecard file. Ideas with no block for that lens are listed as not ranked.
Writes <root>/_comparison/RANKING.md.
"""
import json
import os
import re
import sys

BLOCK = re.compile(r"```scorecard\s*(\{.*?\})\s*```", re.DOTALL)


def load_scorecards(root):
    """Return one list of blocks per idea, in sorted file order."""
    cards = []
    for entry in sorted(os.listdir(root)):
        d = os.path.join(root, entry)
        sc = os.path.join(d, "SCORECARD.md")
        if entry == "_comparison" or not os.path.isfile(sc):
            continue
        blocks = []
        with open(sc, encoding="utf-8") as handle:
            for raw in BLOCK.findall(handle.read()):
                try:
                    blocks.append(json.loads(raw))
                except json.JSONDecodeError:
                    continue
        if blocks:
            cards.append(blocks)
    return cards


def select(cards, lens):
    """Return (ranked cards, unranked idea names) for the chosen lens."""
    ranked = []
    unranked = []
    for blocks in cards:
        match = next((b for b in blocks if b.get("lens") == lens), None)
        if match is None:
            unranked.append(blocks[0].get("idea", "?"))
        else:
            ranked.append(match)
    ranked.sort(key=lambda c: c.get("adjusted", 0), reverse=True)
    return ranked, unranked


def render(ranked, unranked, lens):
    lines = ["# Idea comparison — ranked", "",
             "| Rank | Idea | Adjusted score | Verdict |",
             "|---|---|---|---|"]
    for i, c in enumerate(ranked, 1):
        lines.append(f"| {i} | {c.get('idea','?')} | {c.get('adjusted','?')} | {c.get('verdict','?')} |")
    if unranked:
        shown = lens if lens is not None else "(no lens)"
        lines += ["", "## Not ranked", "",
                  "No block for lens " + str(shown) + ":", ""]
        lines += ["- " + idea for idea in unranked]
    lines.append("")
    return "\n".join(lines)


def main(argv):
    if len(argv) not in (2, 3):
        print("usage: build_comparison.py <assessments-root> [lens]", file=sys.stderr)
        return 2
    root = argv[1]
    cards = load_scorecards(root)
    if not cards:
        print("build_comparison: no scorecards found", file=sys.stderr)
        return 1
    lens = argv[2] if len(argv) == 3 else cards[0][0].get("lens")
    ranked, unranked = select(cards, lens)
    out_dir = os.path.join(root, "_comparison")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "RANKING.md"), "w", encoding="utf-8") as handle:
        handle.write(render(ranked, unranked, lens))
    print(f"build_comparison: ranked {len(ranked)} ideas by lens {lens}, "
          f"{len(unranked)} not ranked -> {out_dir}/RANKING.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
