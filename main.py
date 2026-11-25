"""Six Words to a Payday — make.fun entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Deterministic: same output on every run.
"""

import os

ENTRY = "First paycheck: bought myself a name."
OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str = ENTRY):
    """Check the entry meets the competition rules.

    Returns (True, []) when valid, else (False, [reasons]).
    """
    errors = []
    if not entry or not entry.strip():
        errors.append("entry is empty")
    lines = entry.splitlines()
    if len(lines) != 1:
        errors.append("entry must be exactly one line")
    if len(entry) > 60:
        errors.append("entry exceeds 60 characters")
    words = entry.split()
    if len(words) != 6:
        errors.append("entry must be exactly six words")
    return (not errors, errors)


def main():
    ok, errors = validate()
    if not ok:
        raise ValueError("invalid entry: " + "; ".join(errors))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
