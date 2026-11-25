#!/usr/bin/env python3
"""Regression checks for the seven faults found by independent review."""
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
BUILD = SKILL / "scripts" / "build_comparison.py"
SKILL_MD = (SKILL / "SKILL.md").read_text(encoding="utf-8")


def add_scorecard(root, folder, blocks, raw=None):
    d = root / folder
    d.mkdir(exist_ok=True)
    if raw is None:
        raw = []
        for block in blocks:
            raw.append("```scorecard\n" + json.dumps(block) + "\n```")
    (d / "SCORECARD.md").write_text("\n".join(raw) + "\n", encoding="utf-8")
    return d


def new_root():
    return Path(tempfile.mkdtemp())


def run_build(root, *args):
    return subprocess.run([sys.executable, str(BUILD), str(root), *args],
                          capture_output=True, text=True)


def section(name, next_name):
    return SKILL_MD.split(name, 1)[1].split(next_name, 1)[0]


def ranked_names(ranking):
    return re.findall(r"^\| \d+ \| ([^|]+?) \|", ranking, re.M)


class Review_1_compare_lens(unittest.TestCase):
    """compare is a mode, not a ranking lens."""

    def test_skill_text(self):
        routing = section("## Lens routing", "## Output")
        self.assertIn("first lens other than compare", routing)
        self.assertIn("ask which lens", routing)

    def test_script_rejects_compare(self):
        root = new_root()
        add_scorecard(root, "idea-a", [{"idea": "A", "lens": "founder", "adjusted": 50}])
        proc = run_build(root, "compare")
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("lens", proc.stderr.lower())
        self.assertIn("compare", proc.stderr.lower())


class Review_2_unparseable_block(unittest.TestCase):
    """A file with no valid block is listed, not dropped."""

    def test_folder_is_not_ranked_with_reason(self):
        root = new_root()
        add_scorecard(root, "idea-good",
                      [{"idea": "Good", "lens": "founder", "adjusted": 50}])
        add_scorecard(root, "idea-broken", [], raw=[
            "# Scorecard broken",
            "```scorecard",
            '{"idea":"Broken","lens":"founder","adjusted":72,}',
            "```",
        ])
        proc = run_build(root, "founder")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ranking = (root / "_comparison" / "RANKING.md").read_text(encoding="utf-8")
        tail = ranking.split("Not ranked", 1)[1]
        self.assertIn("idea-broken", tail)
        self.assertIn("no valid scorecard block", tail)


class Review_3_deep_gate(unittest.TestCase):
    """The deep tier token cost confirmation still happens."""

    def test_deep_gate_excepted(self):
        depth = section("## Depth modulation", "## Lens routing")
        self.assertIn("no further gate", depth)
        self.assertIn("except", depth)
        self.assertIn("deep tier token cost confirmation", depth)
        self.assertIn("before any deep run", depth)


class Review_4_unconditional_read(unittest.TestCase):
    """The three-section read happens on every run."""

    def test_read_is_own_sentence(self):
        dep = section("## Dependency Check", "## Web access")
        self.assertRegex(dep, re.compile(r"proceed silently\.\s*\n\s*Read only three sections"))
        self.assertIn("unconditional", dep)
        self.assertIn('after "continue anyway"', dep)


class Review_5_null_idea(unittest.TestCase):
    """A null idea name falls back to the folder name."""

    def test_null_idea_without_lens(self):
        root = new_root()
        add_scorecard(root, "idea-null",
                      [{"idea": None, "lens": "founder", "adjusted": 50}])
        proc = run_build(root)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ranking = (root / "_comparison" / "RANKING.md").read_text(encoding="utf-8")
        self.assertIn("idea-null", ranking)
        self.assertNotIn("| None |", ranking)

    def test_null_idea_with_lens(self):
        root = new_root()
        add_scorecard(root, "idea-null",
                      [{"idea": None, "lens": "founder", "adjusted": 50}])
        proc = run_build(root, "founder")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ranking = (root / "_comparison" / "RANKING.md").read_text(encoding="utf-8")
        self.assertIn("idea-null", ranking)
        self.assertNotIn("| None |", ranking)


class Review_6_case_insensitive(unittest.TestCase):
    """Lens names compare without regard to case."""

    def test_case(self):
        root = new_root()
        add_scorecard(root, "idea-a",
                      [{"idea": "A", "lens": "Investor", "adjusted": 40}])
        add_scorecard(root, "idea-b",
                      [{"idea": "B", "lens": "investor", "adjusted": 70}])
        proc = run_build(root, "INVESTOR")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ranking = (root / "_comparison" / "RANKING.md").read_text(encoding="utf-8")
        self.assertEqual(ranked_names(ranking), ["B", "A"])
        self.assertNotIn("Not ranked", ranking)


class Review_7_adjusted_and_last_block(unittest.TestCase):
    """Adjusted scores are numbers, and the last matching block wins."""

    def test_invalid_adjusted(self):
        root = new_root()
        add_scorecard(root, "idea-good",
                      [{"idea": "Good", "lens": "founder", "adjusted": 50}])
        add_scorecard(root, "idea-bad",
                      [{"idea": "Bad", "lens": "founder", "adjusted": None}])
        proc = run_build(root, "founder")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ranking = (root / "_comparison" / "RANKING.md").read_text(encoding="utf-8")
        tail = ranking.split("Not ranked", 1)[1]
        self.assertIn("Bad", tail)
        self.assertIn("number", tail)

    def test_string_adjusted(self):
        root = new_root()
        add_scorecard(root, "idea-text",
                      [{"idea": "Text", "lens": "founder", "adjusted": "72"}])
        add_scorecard(root, "idea-num",
                      [{"idea": "Num", "lens": "founder", "adjusted": 50}])
        proc = run_build(root, "founder")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ranking = (root / "_comparison" / "RANKING.md").read_text(encoding="utf-8")
        self.assertEqual(ranked_names(ranking), ["Text", "Num"])
        self.assertNotIn("Not ranked", ranking)

    def test_last_block_wins(self):
        root = new_root()
        add_scorecard(root, "idea-x", [
            {"idea": "X", "lens": "founder", "adjusted": 10},
            {"idea": "X", "lens": "founder", "adjusted": 90},
        ])
        add_scorecard(root, "idea-y",
                      [{"idea": "Y", "lens": "founder", "adjusted": 50}])
        proc = run_build(root, "founder")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ranking = (root / "_comparison" / "RANKING.md").read_text(encoding="utf-8")
        self.assertEqual(ranked_names(ranking), ["X", "Y"])


if __name__ == "__main__":
    suite = unittest.TestSuite()
    for cls in (Review_1_compare_lens, Review_2_unparseable_block, Review_3_deep_gate,
                Review_4_unconditional_read, Review_5_null_idea, Review_6_case_insensitive,
                Review_7_adjusted_and_last_block):
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(cls))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
