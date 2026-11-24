#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent (make.fun entry).

Writes the single fortune line to /output/entry.txt.
Stdlib only, no network, deterministic.
"""

import os

# The fortune itself: a classic "your lucky numbers" slip, handed to an
# agent whose context window quietly forgets things.
FORTUNE = "Your lucky numbers are the ones your context window forgot."

OUTPUT_PATH = "/output/entry.txt"


def write_entry(text: str) -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    write_entry(FORTUNE)


if __name__ == "__main__":
    main()
