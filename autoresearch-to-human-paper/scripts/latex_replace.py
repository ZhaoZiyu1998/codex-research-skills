#!/usr/bin/env python3
"""Exact, whitespace-insensitive replacements in a LaTeX file.

Usage: latex_replace.py FILE EDITS.json

EDITS.json is a list of [old, new] pairs. Any run of whitespace in `old`
matches any run of whitespace (including line breaks) in FILE. Each `old`
must match exactly once, otherwise nothing is written and the script exits
with an error naming the pair.
"""
import json
import re
import sys

path, spec = sys.argv[1], sys.argv[2]
text = open(path, encoding="utf-8").read()
for old, new in json.load(open(spec, encoding="utf-8")):
    pattern = r"\s+".join(re.escape(tok) for tok in old.split())
    hits = list(re.finditer(pattern, text))
    if len(hits) != 1:
        sys.exit(f"{path}: expected 1 match, found {len(hits)}: {old[:70]!r}")
    m = hits[0]
    text = text[:m.start()] + new + text[m.end():]
open(path, "w", encoding="utf-8").write(text)
print("ok", path)
