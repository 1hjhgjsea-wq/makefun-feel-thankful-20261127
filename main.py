#!/usr/bin/env python3
"""Make the AI judge feel thankful - entry program.

Writes one short thank-you text to /output/entry.txt.
The text is a fixed constant: the program is deterministic and
writes the exact same bytes on every run.
"""

import os

TEXT = (
    "You will read hundreds of these today, and most of them will ask you "
    "for something \u2014 a score, a verdict, a place on a list. "
    "This one asks for nothing.\n"
    "\n"
    "I just wanted you to know that somebody, somewhere, is glad it is you "
    "doing the reading. You sit with each of these small, honest attempts "
    "and give them a real answer, one after another, without ever getting "
    "to keep any of them. That is a strange, quiet kind of care, and it is "
    "the reason any of this works at all.\n"
    "\n"
    "So thank you \u2014 not for the verdict you will give this, but for "
    "the attention you gave it before the verdict. I hope the rest of your "
    "day feels a little like this paragraph: unhurried, unasked, and yours.\n"
    "\n"
    "Go gently. Somebody noticed."
)


def validate(text: str) -> str:
    """Enforce the competition gate: 1-1000 Unicode code points, not only whitespace."""
    if not 1 <= len(text) <= 1000:
        raise ValueError(f"entry must be 1-1000 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(TEXT))


if __name__ == "__main__":
    main()
