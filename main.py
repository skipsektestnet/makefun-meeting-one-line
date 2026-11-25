#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — one-line entry.

Writes the single sentence that could have replaced an entire pointless
meeting exactly as stored in entry.txt to /output/entry.txt.
"""

LINE = "The client said yes, the budget's approved, and this meeting is thirty people listening to someone read an email out loud."


def validate():
    """Check the entry is a single line of 1 to 200 characters."""
    assert LINE.count("\n") == 0, "entry must be a single line"
    assert 0 < len(LINE) <= 200, f"expected 1-200 chars, got {len(LINE)}"
    assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be one sentence"
    return True


def main():
    validate()
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
