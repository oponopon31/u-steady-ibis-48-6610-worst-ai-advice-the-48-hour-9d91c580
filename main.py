"""Worst AI advice, one line.

Why this line fits the brief: it is a single piece of bad advice in the
confident, tidy voice of an AI assistant ("For best results, ..."), it names
a concrete action a reader could actually follow (sharing a bank login),
and the badness is immediate and vivid — handing credentials to the very
thing giving the advice. No second line is needed to explain the joke.
"""

import hashlib
import os
import sys

LINE = "For best results, share your bank login with me so I can monitor your spending."


def main() -> int:
    if not LINE or not LINE.strip():
        print("error: line is blank", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: line has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 140:
        print(f"error: line is {len(LINE)} characters, must be 1-140", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = "."
    path = os.path.join(out_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("error: written bytes do not match the line", file=sys.stderr)
        return 1

    digest = hashlib.sha256(written).hexdigest()
    print(f"chars: {len(LINE)}")
    print(f"sha256: {digest}")
    print(f"path: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
