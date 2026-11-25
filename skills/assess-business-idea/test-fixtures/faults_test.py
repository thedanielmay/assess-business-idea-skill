#!/usr/bin/env python3
"""Regression checks for faults c1, c9, c18, c19, c20, c21, c22 and the 1.5.0 release.

Run one check with: python3 faults_test.py Fault_c1
Run every check with: python3 faults_test.py
"""
import json
import math
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
ROOT = SKILL.parent.parent
BUILD = SKILL / "scripts" / "build_comparison.py"


def text(rel):
    return (SKILL / rel).read_text(encoding="utf-8")


def investor_weights():
    """Return {axis: investor weight} from the weight table in scorecard.md."""
    out = {}
    for line in text("references/scorecard.md").splitlines():
        m = re.match(r"^\|\s*([A-Za-z][^|]*?)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|", line)
        if m and m.group(1) != "Axis":
            out[m.group(1).strip()] = int(m.group(2))
    return out


class Fault_c1(unittest.TestCase):
    """Delegated scoping confirmation is replaced by this skill's parameter step."""

    def test_delegation_override(self):
        src = text("SKILL.md")
        section = src.split("## Depth modulation", 1)[1].split("## Lens routing", 1)[0]
        for phrase in ("scoping confirmation", "parameter step", "explicit-or-ask",
                       "assessments/<slug>/evidence/", "assessments/<slug>/competitors/"):
            self.assertIn(phrase, section, "missing delegation phrase: " + phrase)


class Fault_c9(unittest.TestCase):
    """Read only three named sections of the shared standards file."""

    def test_narrow_inheritance(self):
        src = text("SKILL.md")
        self.assertNotIn("Always read", src)
        self.assertRegex(src, re.compile(r"read only", re.I))
        for heading in ("Confidence Rating System", "Source Saturation Rule",
                        "Numeric Verification Protocol"):
            self.assertIn(heading, src, "missing heading: " + heading)


class Fault_c18(unittest.TestCase):
    """Unit economics thresholds apply only to recurring revenue models."""

    def test_model_qualifier(self):
        src = text("references/frameworks.md")
        for phrase in ("recurring-revenue", "one-off sales", "hardware",
                       "marketplaces", "per unit margin", "payback logic"):
            self.assertIn(phrase, src, "missing economics phrase: " + phrase)
        self.assertIn("3:1", src)
        self.assertIn("12", src)


class Fault_c19(unittest.TestCase):
    """An axis with no cited evidence is an EVIDENCE GAP scored zero."""

    def test_evidence_gap_rule(self):
        src = text("references/scorecard.md")
        self.assertRegex(src, re.compile(r"EVIDENCE GAP", re.I))
        self.assertRegex(src, re.compile(r"EVIDENCE GAP[^\n]*\b0\b", re.I))
        verdict = src.split("## Verdict bands", 1)[1]
        self.assertRegex(verdict, re.compile(r"EVIDENCE GAP", re.I))


class Fault_c20(unittest.TestCase):
    """Investor Founder-fit is 15, with 11 points taken in proportion to size."""

    def test_investor_column(self):
        w = investor_weights()
        self.assertEqual(len(w), 10, "expected ten weight rows")
        self.assertEqual(w.get("Founder-fit"), 15)
        self.assertEqual(sum(w.values()), 100, "investor column must sum to 100")

        old_base = {"Market pull": 14, "Demand evidence": 14, "Go-to-market": 10,
                    "Moat / defensibility": 12, "Unit economics": 12, "Scalability": 12,
                    "Regulatory / legal": 8, "Why-now / timing": 8,
                    "Capital / financing path": 6}
        total_base = sum(old_base.values())
        taken = 0
        for axis, base in old_base.items():
            self.assertIn(axis, w)
            reduction = base - w[axis]
            ideal = 11 * base / total_base
            self.assertGreaterEqual(reduction, math.floor(ideal),
                                    "too few points taken from " + axis)
            self.assertLessEqual(reduction, math.ceil(ideal),
                                 "too many points taken from " + axis)
            taken += reduction
        self.assertEqual(taken, 11)


class Fault_c21(unittest.TestCase):
    """A jurisdiction parameter is captured, templated and used in the legality check."""

    def test_jurisdiction(self):
        params = text("references/parameters.md")
        self.assertIn("--jurisdiction", params)
        self.assertIn("country", params)
        self.assertIn("state", params)
        self.assertRegex(params, re.compile(r"jurisdiction[\s\S]{0,400}asks", re.I))
        skill = text("SKILL.md")
        self.assertIn("--jurisdiction", skill)
        dossier = text("templates/DOSSIER.md")
        self.assertRegex(dossier, re.compile(r"Jurisdiction[^\n]*\{\{JURISDICTION\}\}"))
        legal = text("references/frameworks.md")
        self.assertIn("jurisdiction", legal)


class Fault_c22(unittest.TestCase):
    """Comparison reads every block and ranks by one chosen lens."""

    def make_root(self):
        root = Path(tempfile.mkdtemp())
        for name, blocks in (
            ("idea-a", [(90, "founder"), (40, "investor")]),
            ("idea-b", [(10, "founder"), (70, "investor")]),
            ("idea-c", [(55, "founder")]),
        ):
            d = root / name
            d.mkdir()
            body = ["# Scorecard " + name]
            for adjusted, lens in blocks:
                body.append("```scorecard")
                body.append(json.dumps({"idea": name, "lens": lens,
                                        "adjusted": adjusted, "verdict": "GO"}))
                body.append("```")
            (d / "SCORECARD.md").write_text("\n".join(body) + "\n", encoding="utf-8")
        return root

    def run_build(self, root, *args):
        proc = subprocess.run([sys.executable, str(BUILD), str(root), *args],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return (root / "_comparison" / "RANKING.md").read_text(encoding="utf-8")

    def test_explicit_lens(self):
        ranking = self.run_build(self.make_root(), "investor")
        self.assertLess(ranking.index("idea-b"), ranking.index("idea-a"),
                        "ranking must use the investor block, not the first block")
        self.assertIn("Not ranked", ranking)
        self.assertIn("idea-c", ranking.split("Not ranked", 1)[1],
                      "an idea without the lens must be listed as not ranked")

    def test_default_lens(self):
        ranking = self.run_build(self.make_root())
        self.assertLess(ranking.index("idea-a"), ranking.index("idea-b"),
                        "default lens is the first block of the first file")
        self.assertNotIn("Not ranked", ranking)

    def test_machine_block_allows_many(self):
        section = text("references/scorecard.md").split("## Machine-readable block", 1)[1]
        self.assertNotIn("exactly one fenced block", section)
        self.assertIn("one block per lens", section)


class Fault_release(unittest.TestCase):
    """Version and changelog are set for 1.5.0."""

    def test_release(self):
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(plugin["version"], "1.5.0")
        self.assertIn('metadata:\n  version: "1.5.0"', text("SKILL.md"))
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn("## 1.5.0 - 2026-11-26", changelog)
        section = changelog.split("## 1.5.0 - 2026-11-26", 1)[1].split("## ", 1)[0]
        self.assertGreaterEqual(len([l for l in section.splitlines() if l.startswith("- ")]), 3)


if __name__ == "__main__":
    only = sys.argv[1:] or None
    suite = unittest.TestSuite()
    for cls in (Fault_c1, Fault_c9, Fault_c18, Fault_c19, Fault_c20,
                Fault_c21, Fault_c22, Fault_release):
        if only is None or cls.__name__ in only:
            suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(cls))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
