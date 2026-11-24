"""One Word, One Username, One Reward -- make.fun entry.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. Gate: UTF-8 text, 1-30 characters, not only
whitespace. "kace2122" is 8 characters, a single word, no padding.
"""

import os

USERNAME = "kace2122"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)

    # Self-check: the gate requires 1-30 chars, one word, not only whitespace.
    with open(os.path.join(out_dir, "entry.txt"), "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == USERNAME, "entry mismatch"
    assert 1 <= len(written) <= 30, "entry length outside 1-30 chars"
    assert written.strip() and " " not in written, "entry must be one word"


if __name__ == "__main__":
    main()
