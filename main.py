#!/usr/bin/env python3
"""One-Star Review of Something Essential — v3.

Writes a single deadpan one-star review of an everyday essential to
/output/entry.txt: one line, at most 160 characters, UTF-8, no trailing
newline, file mode 0644. Fully deterministic: the review is a constant,
so every run writes the same bytes.
"""

import os

REVIEW = "Water: eight glasses a day and it still tastes like nothing. One star."


def main() -> None:
    text = REVIEW
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() == text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
