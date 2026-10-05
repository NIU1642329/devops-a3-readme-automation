#!/usr/bin/env python3
"""Fail CI if the README activity markers are missing/malformed or a token leaked into it."""
import re
import sys
from pathlib import Path

START = "<!--START_SECTION:activity-->"
END = "<!--END_SECTION:activity-->"
TOKEN_RE = re.compile(r"\b(gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})")

text = Path("README.md").read_text(encoding="utf-8")
errors = []
if text.count(START) != 1:
    errors.append(f"expected exactly 1 start marker, found {text.count(START)}")
if text.count(END) != 1:
    errors.append(f"expected exactly 1 end marker, found {text.count(END)}")
if not errors and text.index(START) > text.index(END):
    errors.append("the start marker must come before the end marker")
if TOKEN_RE.search(text):
    errors.append("README.md contains something that looks like a GitHub token")

for error in errors:
    print(f"::error file=README.md::{error}")
if errors:
    sys.exit(1)
print("README markers OK, no token-like strings found")
