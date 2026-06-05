#!/usr/bin/env bash
set -u
DIR="$(cd "$(dirname "$0")/.." && pwd)"
S="$DIR/scripts/build_comparison.py"
ROOT="$(mktemp -d)"
mkdir -p "$ROOT/idea-a" "$ROOT/idea-b"

cat > "$ROOT/idea-a/SCORECARD.md" <<'EOF'
# Scorecard: Idea A
```scorecard
{"idea":"Idea A","adjusted":58,"verdict":"CONDITIONAL"}
```
EOF
cat > "$ROOT/idea-b/SCORECARD.md" <<'EOF'
# Scorecard: Idea B
```scorecard
{"idea":"Idea B","adjusted":72,"verdict":"GO"}
```
EOF

python3 "$S" "$ROOT" || { echo "FAIL: nonzero"; exit 1; }
test -f "$ROOT/_comparison/RANKING.md" || { echo "FAIL: no RANKING.md"; exit 1; }
# Idea B (72) must rank above Idea A (58)
python3 - "$ROOT/_comparison/RANKING.md" <<'PY'
import sys
t=open(sys.argv[1]).read()
assert t.index("Idea B") < t.index("Idea A"), "ranking order wrong"
print("comparison test OK")
PY
