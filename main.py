"""Sorry, I Heard That Wrong.

Writes the single-line apology a smart speaker gives its owner after
mishearing "wake me at seven" as "wake me in heaven" to /output/entry.txt.
Deterministic, standard library only.
"""

import os

ENTRY = (
    "Sorry \u2014 I heard 'wake me at seven' as 'wake me in heaven.' "
    "I checked twice and can neither confirm nor deny where you are."
)

# Gate check: the entry must be 1-140 UTF-8 characters, exactly one line,
# with no trailing newline, so the file holds precisely the spoken line.
assert 1 <= len(ENTRY) <= 140
assert "\n" not in ENTRY


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
