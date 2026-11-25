#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one pitch sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

PITCH = (
    "For $2 a month, TermsGhost reads the 47-page terms of service your "
    "lazy agent keeps blindly accepting, then signs 'I have read and "
    "agree' so it never has to lie about it again."
)


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
