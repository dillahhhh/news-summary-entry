#!/usr/bin/env python3
"""Write the summary of 11 November 2026 world news to /output/entry.txt.

Entry for the make.fun news-summary-01 competition (program/v1). The
summary ships as ``summary.txt`` next to this file — fifteen stories, one
tight sentence each, ordered by importance, every one sourced — and this
program copies it, byte for byte, to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(``/output/entry.txt`` by default). Standard library only, no network,
fully deterministic: two runs write identical bytes.

Round 7 (2026-11-12): rebuilt from round 6 (95.68%, #399) — fixed the
Iran line (the seven conditions are Iran's, not the U.S.'s); sharpened
Nvidia to the board weighing ousting Huang (shares -8%); added Mississippi
(Colom, first Black senator since Reconstruction, Democrats to 55 seats),
El Salvador (Bukele's 400 Mawozo HQ strike) and COP31 (Guterres's "path to
destruction"); dropped Darchiev, Hegseth and Ebola for the three more
consequential stories. All figures verified against Reuters/AFP/AP/BBC/
CNN/CNBC/DOJ reporting of 11 November 2026. Final: 15 stories, 1,998
characters, deterministic output verified locally.

The competition gate requires the summary to be UTF-8, 1 to 2,000
characters, and not only white space, so this program checks those rules
before writing and refuses to ship a summary that would fail them.

Run locally:  ``MAKEFUN_OUTPUT_DIR=out python3 main.py``
"""

import os
import shutil
import sys

# The summary lives beside this file, so the program works wherever the
# repository is checked out (the grader mounts it read-only at /bot).
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "summary.txt")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")

# Competition gate: 1 to 2,000 characters, at least one non-white-space.
MAX_CHARS = 2000


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"error: {SOURCE} not found", file=sys.stderr)
        return 1
    with open(SOURCE, encoding="utf-8") as f:
        text = f.read()
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"error: summary is {len(text)} characters, "
              f"must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not any(not c.isspace() for c in text):
        print("error: summary is only white space", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    with open(DESTINATION, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        print("error: written bytes differ from summary.txt", file=sys.stderr)
        return 1
    print(f"wrote {DESTINATION} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
