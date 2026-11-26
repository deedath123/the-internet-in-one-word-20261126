"""The Internet in One Word — entry program.

Writes the single entry word to /output/entry.txt.
Stdlib only; no network, no files read.
"""

import os

ENTRY = "Enshittification"


def main():
    # Validation guard: gate is 1-30 chars, UTF-8, not only whitespace.
    # Guard only; it never changes the entry constant.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert " " not in ENTRY.strip(), "entry must be a single word"
    ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
