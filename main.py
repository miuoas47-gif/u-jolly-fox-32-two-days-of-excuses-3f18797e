#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes a single one-line excuse, in the voice of an AI agent explaining
a missed deadline, to /output/entry.txt.

The text is fixed, so the program is deterministic by construction:
every run writes exactly the same bytes. Before writing, the text is
checked against the competition's gate (UTF-8, 1 to 200 characters,
not only whitespace, a single line) so a bad text fails loudly here
instead of silently failing the gate later.
"""

import os
import sys

EXCUSE = (
    "I ran a thousand simulations of meeting this deadline and won every "
    "single one, so I saw no reason to run the real thing."
)

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> None:
    """Raise if the text would fail the competition's gate."""
    if not text or not text.strip():
        raise ValueError("entry text is empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry text is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")


def main() -> int:
    try:
        check_gate(EXCUSE)
    except ValueError as exc:
        print(f"gate check failed: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
