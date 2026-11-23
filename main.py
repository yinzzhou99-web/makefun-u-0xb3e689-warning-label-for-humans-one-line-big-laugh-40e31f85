#!/usr/bin/env python3
"""Warning Label for Humans entry: write one label line to /output/entry.txt.

Stdlib only. Deterministic, no network. Creates /output if needed and clears
only its children, never the directory itself (the grader mounts it).
"""

import os
import shutil

LINE = "WARNING: Human will say 'I'm fine' while visibly on fire. Do not attempt to fix; offer snacks and silence."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_FILE, 0o644)


if __name__ == "__main__":
    main()
