#!/usr/bin/env python3
"""Directional Google Trends fetch. Emits JSON to stdout. Never raises to caller.

Usage:
  google_trends.py [--offline] [--timeframe 'today 12-m'] <term> [<term> ...]

Output (success):
  {"status":"ok","timeframe":...,"terms":[...],"interest_over_time":[{"date":..,"values":{term:int}}]}
Output (failure / --offline):
  {"status":"unavailable","reason":"...","terms":[...]}

Trends data is DIRECTIONAL ONLY. The skill must triangulate, never rest on it.
"""
import json
import sys
import urllib.parse
import urllib.request


def _fail(terms, reason):
    return {"status": "unavailable", "reason": reason, "terms": terms}


def fetch(terms, timeframe):
    # Step 1: obtain a session token (widget config) from the explore endpoint.
    base = "https://trends.google.com/trends/api/explore"
    comparison = [{"keyword": t, "geo": "", "time": timeframe} for t in terms]
    req = (
        base
        + "?hl=en-US&tz=0&req="
        + urllib.parse.quote(json.dumps({"comparisonItem": comparison, "category": 0, "property": ""}))
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read().decode("utf-8", "replace")
        # Google prefixes the JSON with ")]}'," — strip to first '{'.
        token_payload = json.loads(raw[raw.index("{"):])
        widgets = token_payload["widgets"]
        tl = next(w for w in widgets if w.get("id") == "TIMESERIES")
    except Exception as e:  # network, parse, or shape failure -> directional gap
        return _fail(terms, f"explore endpoint failed: {e}")

    # Step 2: pull the timeseries using the widget token.
    mr = (
        "https://trends.google.com/trends/api/widgetdata/multiline"
        + "?hl=en-US&tz=0&req="
        + urllib.parse.quote(json.dumps(tl["request"]))
        + "&token="
        + urllib.parse.quote(tl["token"])
    )
    try:
        with urllib.request.urlopen(mr, timeout=20) as r:
            raw = r.read().decode("utf-8", "replace")
        data = json.loads(raw[raw.index("{"):])
        rows = []
        for pt in data["default"]["timelineData"]:
            rows.append({
                "date": pt.get("formattedTime", ""),
                "values": {t: v for t, v in zip(terms, pt.get("value", []))},
            })
        return {"status": "ok", "timeframe": timeframe, "terms": terms, "interest_over_time": rows}
    except Exception as e:
        return _fail(terms, f"timeseries endpoint failed: {e}")


def main(argv):
    args = argv[1:]
    offline = False
    timeframe = "today 12-m"
    terms = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--offline":
            offline = True
        elif a == "--timeframe":
            i += 1
            timeframe = args[i]
        else:
            terms.append(a)
        i += 1
    if not terms:
        print(json.dumps(_fail([], "no terms supplied")))
        return 0
    result = _fail(terms, "offline mode requested") if offline else fetch(terms, timeframe)
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
