#!/usr/bin/env python3
"""Write the best summary of 11 November's world news: copies summary.txt to /output/entry.txt."""
import os, shutil
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "summary.txt")
DST = "/output/entry.txt"
os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)
print("wrote", DST)
