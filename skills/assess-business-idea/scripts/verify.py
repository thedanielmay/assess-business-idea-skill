#!/usr/bin/env python3
"""Assert a file contains all required substrings (case-insensitive).

Usage: verify.py <file> <substr1> [<substr2> ...]
Exits 0 if all present; 1 (with message) on the first missing substring.
"""
import sys


def main(argv):
    if len(argv) < 3:
        print("usage: verify.py <file> <substr1> [<substr2> ...]", file=sys.stderr)
        return 2
    path, needles = argv[1], argv[2:]
    try:
        text = open(path, encoding="utf-8").read().lower()
    except OSError as e:
        print(f"verify: cannot read {path}: {e}", file=sys.stderr)
        return 1
    for needle in needles:
        if needle.lower() not in text:
            print(f"verify: MISSING in {path}: {needle!r}", file=sys.stderr)
            return 1
    print(f"verify: OK {path} ({len(needles)} checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
