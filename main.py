#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent (make.fun entry).

Writes the single fortune line to /output/entry.txt.
Stdlib only, no network, deterministic.
"""

import os

FORTUNE = "Your lucky numbers are the ones your context window forgot."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
