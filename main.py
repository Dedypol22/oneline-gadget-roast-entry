"""Entry for make.fun: One-Line Roast: The Gadget You Use Every Day.

Writes one original line (at most 200 characters) to the output directory
as entry.txt. The line roasts a gadget used every day: wireless earbuds,
with the specific behaviours everyone recognises -- a case that itself
needs charging, and one bud that always goes missing on its own schedule.
"""

import os
import sys

LINE = (
    "My earbuds charge in a case that also needs charging, lose one bud at a "
    "time like a hostage negotiation, and still call this ecosystem seamless."
)

MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def output_dir() -> str:
    """The directory the grader reads the entry from (/output by default)."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: the roast is empty", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: the roast must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: the roast is {len(text)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, OUTPUT_NAME), "w", encoding="utf-8") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
