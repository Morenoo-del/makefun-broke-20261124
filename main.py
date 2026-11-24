#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single line of software error copy to /output/entry.txt:
it names the real failure (a full disk ate the save), tells the user
what to do next, and admits the brutal truth with a joke.
"""

import os


LINE = (
    "Your disk is full, so we saved your file nowhere. "
    "Free up some space \u2014 or keep typing into the void."
)


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 200, f"entry is {len(text)} chars, over the 200 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
