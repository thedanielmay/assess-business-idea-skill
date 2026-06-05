#!/usr/bin/env bash
set -u
DIR="$(cd "$(dirname "$0")/.." && pwd)"
S="$DIR/scripts/google_trends.py"

# Always-offline mode must emit valid JSON with a status field and never exit non-zero.
OUT="$(python3 "$S" --offline "test term")" || { echo "FAIL: nonzero exit"; exit 1; }
echo "$OUT" | python3 -c 'import sys,json; d=json.load(sys.stdin); assert "status" in d, "no status"; print("status:",d["status"])' \
  || { echo "FAIL: not valid JSON / no status"; exit 1; }
echo "trends test OK"
