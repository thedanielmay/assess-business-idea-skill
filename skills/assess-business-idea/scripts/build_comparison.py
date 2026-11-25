#!/usr/bin/env python3
"""Aggregate all SCORECARD.md files under a root into a ranked RANKING.md.

Usage: build_comparison.py <assessments-root> [lens]
Reads every fenced ```scorecard JSON block in each <root>/*/SCORECARD.md. Ranks by
one lens only. With no lens argument, the default is the lens of the first block of
the first scorecard file. Lens names compare without regard to case. compare is a
mode, not a lens, and is rejected. Ideas that cannot be ranked are listed with a
reason. Writes <root>/_comparison/RANKING.md.
"""
import json
import math
import os
import re
import sys

BLOCK = re.compile(r"```scorecard\s*(\{.*?\})\s*```", re.DOTALL)


def lens_key(value):
    """Normalise a lens name for comparison."""
    if value is None:
        return None
    return str(value).strip().lower()


def score_number(value):
    """Return a number when possible, otherwise None."""
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, float)):
        return value if math.isfinite(value) else None
    if isinstance(value, str):
        try:
            number = float(value.strip())
        except ValueError:
            return None
        return number if math.isfinite(number) else None
    return None


def display_number(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def idea_name(block, folder):
    """Use the recorded idea name only when it is a non-empty string."""
    name = block.get("idea")
    if isinstance(name, str) and name.strip():
        return name
    return folder


def reject_compare(lens):
    if lens == "compare":
        print("build_comparison: 'compare' is a mode, not a lens. "
              "Choose founder, investor, operator or consultant.", file=sys.stderr)
        return True
    return False


def load_scorecards(root):
    """Return one record per scorecard file, in sorted file order."""
    cards = []
    for entry in sorted(os.listdir(root)):
        d = os.path.join(root, entry)
        sc = os.path.join(d, "SCORECARD.md")
        if entry == "_comparison" or not os.path.isfile(sc):
            continue
        with open(sc, encoding="utf-8") as handle:
            raws = BLOCK.findall(handle.read())
        blocks = []
        for raw in raws:
            try:
                blocks.append(json.loads(raw))
            except json.JSONDecodeError:
                continue
        error = None
        if not raws:
            error = "no scorecard block"
        elif not blocks:
            error = "no valid scorecard block"
        cards.append({"folder": entry, "blocks": blocks, "error": error})
    return cards


def select(cards, lens):
    """Return (ranked cards, unranked name and reason pairs) for the lens."""
    ranked = []
    unranked = []
    for card in cards:
        folder = card["folder"]
        if card["error"]:
            unranked.append((folder, card["error"]))
            continue
        matches = [b for b in card["blocks"]
                   if lens_key(b.get("lens")) == lens]
        if not matches:
            unranked.append((idea_name(card["blocks"][0], folder),
                             "no block for lens " + str(lens)))
            continue
        block = matches[-1]
        score = score_number(block.get("adjusted"))
        if score is None:
            unranked.append((idea_name(block, folder),
                             "adjusted score is not a number"))
            continue
        ranked.append({"name": idea_name(block, folder), "score": score,
                       "verdict": block.get("verdict", "?")})
    ranked.sort(key=lambda c: c["score"], reverse=True)
    return ranked, unranked


def render(ranked, unranked, lens):
    lines = ["# Idea comparison — ranked", "",
             "| Rank | Idea | Adjusted score | Verdict |",
             "|---|---|---|---|"]
    for i, c in enumerate(ranked, 1):
        lines.append(f"| {i} | {c['name']} | {display_number(c['score'])} | {c['verdict']} |")
    if unranked:
        shown = lens if lens is not None else "(no lens)"
        lines += ["", "## Not ranked", "", "Lens: " + str(shown), ""]
        lines += ["- " + name + ": " + reason for name, reason in unranked]
    lines.append("")
    return "\n".join(lines)


def main(argv):
    if len(argv) not in (2, 3):
        print("usage: build_comparison.py <assessments-root> [lens]", file=sys.stderr)
        return 2
    root = argv[1]
    supplied = lens_key(argv[2]) if len(argv) == 3 else None
    if reject_compare(supplied):
        return 2
    cards = load_scorecards(root)
    if not cards:
        print("build_comparison: no scorecards found", file=sys.stderr)
        return 1
    if supplied is not None:
        lens = supplied
    else:
        first = next((c["blocks"][0].get("lens") for c in cards if c["blocks"]), None)
        lens = lens_key(first)
    if reject_compare(lens):
        return 2
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
