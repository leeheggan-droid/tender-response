#!/usr/bin/env python3
"""Measure exact UTF-8 submission text; local conventions are explicit."""

import argparse
import json
from pathlib import Path


def nonnegative(value):
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("limits must be nonnegative")
    return number


def main():
    parser = argparse.ArgumentParser(
        description="Count whitespace words and characters, including headings and spaces.",
        epilog="CRLF/CR become LF. No trimming. The buyer's portal convention takes priority. "
        "Exit 0: within caps; 1: cap exceeded; 2: usage/input error. No network access.",
    )
    parser.add_argument("file", type=Path, help="UTF-8 text containing only the submission field")
    parser.add_argument("--max-words", type=nonnegative)
    parser.add_argument("--max-characters", type=nonnegative)
    parser.add_argument(
        "--character-unit", choices=["codepoints", "utf16", "utf8-bytes"],
        default="codepoints",
        help="default: codepoints; utf16 counts code units, utf8-bytes counts bytes",
    )
    args = parser.parse_args()
    try:
        text = args.file.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as error:
        parser.error(f"cannot read input: {error}")
    words = len(text.split())
    if args.character_unit == "utf16":
        characters = len(text.encode("utf-16-le")) // 2
    elif args.character_unit == "utf8-bytes":
        characters = len(text.encode("utf-8"))
    else:
        characters = len(text)
    within_limits = (
        (args.max_words is None or words <= args.max_words)
        and (args.max_characters is None or characters <= args.max_characters)
    )
    print(json.dumps({
        "words": words,
        "word_convention": "whitespace",
        "characters": characters,
        "character_unit": args.character_unit,
        "newline_convention": "LF",
        "max_words": args.max_words,
        "max_characters": args.max_characters,
        "within_limits": within_limits,
    }, indent=2))
    return 0 if within_limits else 1


if __name__ == "__main__":
    raise SystemExit(main())
