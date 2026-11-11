#!/usr/bin/env python3
"""Write the best summary of 11 November's world news: copies summary.txt to /output/entry.txt."""
import os, shutil
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "summary.txt")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
DST = os.path.join(OUT, "entry.txt")
shutil.copyfile(SRC, DST)
print("wrote", DST)
