#!/usr/bin/env bash
set -u
S="$HOME/.claude/skills/assess-business-idea"
fail=0

# 1. All expected files exist.
for f in SKILL.md references/parameters.md references/frameworks.md references/scorecard.md \
         references/trends-sources.md references/verification.md \
         references/plain-language-charter.md references/report-spec.md \
         templates/DOSSIER.md templates/REPORT.html \
         scripts/verify.py scripts/google_trends.py scripts/build_comparison.py; do
  [ -f "$S/$f" ] || { echo "MISSING $f"; fail=1; }
done

# 2. All script self-tests pass.
bash "$S/test-fixtures/verify_selftest.sh"   >/dev/null || { echo "verify selftest failed"; fail=1; }
bash "$S/test-fixtures/trends_test.sh"       >/dev/null || { echo "trends test failed"; fail=1; }
bash "$S/test-fixtures/comparison_test.sh"   >/dev/null || { echo "comparison test failed"; fail=1; }
node "$S/test-fixtures/report_render_test.mjs">/dev/null || { echo "report render failed"; fail=1; }

# 3. Cross-artifact consistency: orchestrator points to every reference file.
for ref in parameters scorecard report-spec verification frameworks trends-sources plain-language-charter; do
  grep -q "$ref" "$S/SKILL.md" || echo "NOTE: SKILL.md does not mention $ref.md"
done

[ "$fail" = 0 ] && echo "E2E OK" || { echo "E2E FAILED"; exit 1; }
