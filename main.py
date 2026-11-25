"""Six Words to a Payday — make.fun entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Deterministic: same output on every run.
"""

import os

ENTRY = "First paycheck: bought myself a name."
OUTPUT_PATH = "/output/entry.txt"

# Competition rules, kept as named constants so the validator and the
# entry stay in sync when the limits change.
WORD_LIMIT = 6
CHAR_LIMIT = 60


def _words(entry: str):
    """Split an entry into words, ignoring trailing punctuation.

    "name." counts as the word "name", so a trailing period does not
    inflate the word count.
    """
    return [w.rstrip(".,;:!?") for w in entry.split() if w.rstrip(".,;:!?")]


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
    if len(entry) > CHAR_LIMIT:
        errors.append(f"entry exceeds {CHAR_LIMIT} characters")
    if not entry.isascii():
        errors.append("entry must be ASCII only")
    words = _words(entry)
    if len(words) != WORD_LIMIT:
        errors.append(f"entry must be exactly {WORD_LIMIT} words")
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
