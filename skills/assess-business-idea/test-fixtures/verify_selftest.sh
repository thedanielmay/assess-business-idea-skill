#!/usr/bin/env bash
# Self-test for verify.py. Exits 0 only if verify.py behaves correctly.
set -u
DIR="$(cd "$(dirname "$0")/.." && pwd)"
V="$DIR/scripts/verify.py"
TMP="$(mktemp)"
printf 'hello world\nsecond line\n' > "$TMP"

# Should PASS (both substrings present, case-insensitive)
python3 "$V" "$TMP" "HELLO" "second line" || { echo "FAIL: expected pass"; exit 1; }

# Should FAIL (missing substring) -> non-zero exit
if python3 "$V" "$TMP" "absent-token"; then echo "FAIL: expected non-zero"; exit 1; fi

echo "verify.py self-test OK"
