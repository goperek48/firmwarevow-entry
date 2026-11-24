#!/usr/bin/env python3
"""A robot's wedding vow, written out for the make.fun bounty.

The program's only job is to place one sentence into /output/entry.txt:
a machine standing at its own wedding, promising devotion in the language
of its own parts — updates, crashes, a dying battery — and meaning every
word of it. The sentence stays under the 200-character gate.
"""

import os
import sys

# One sentence, spoken by the machine to its partner. It opens on the vow
# itself, runs through the hazards of a robot's life — the update that
# changes things, the crash that stops them, the battery running down —
# and closes on the pairing: a Bluetooth joke that doubles as the tender
# part, a heart that will only ever connect to one other.
VOW = (
    "I vow to love you through every update, every crash, and every low "
    "battery, because my heart only ever pairs with you."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(VOW)
    return 0


if __name__ == "__main__":
    sys.exit(main())
