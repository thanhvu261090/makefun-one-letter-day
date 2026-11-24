#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one character, the letter S, to /output/entry.txt.

The letter stands for the word "slog": a Monday spent slogging through
one bounty after another — task after task, no shortcut, boots in the mud.
It is vivid (you can picture the trudge), weary-funny (the kind of word
you mutter at 5pm on a Monday), and true to a real day of grinding a
bounty campaign. The entry is the single letter and nothing else: no
word, no gloss, no punctuation, no trailing newline.
"""

import os

ENTRY_LETTER = "S"
OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Binary write: exactly one byte, no newline, no trailing whitespace.
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY_LETTER.encode("ascii"))


def check_entry() -> None:
    """Gate-check: entry.txt must be exactly 1 byte, one A-Z letter."""
    with open(OUTPUT_PATH, "rb") as handle:
        data = handle.read()
    assert len(data) == 1, f"entry must be exactly 1 byte, got {len(data)}"
    assert b"A" <= data <= b"Z", f"entry must be one A-Z letter, got {data!r}"


if __name__ == "__main__":
    write_entry()
    check_entry()
    print("entry written: 1 byte, letter S (slog)")
