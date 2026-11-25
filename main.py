"""Your Week in One Line — make.fun entry (u-boge-your-week-in-one-line-d1c14ced).

Writes a single line (<=100 chars) summing up the entrant's week to
/output/entry.txt. The line is a fixed, hand-written string: the program's
job is only to emit it byte-exactly, with no trailing newline, so the gate
sees exactly the 97 characters that were judged in candidates.md.
"""

import os

LINE = "This week my phone died, my laptop stayed imaginary, and my best joke earned exactly two dollars."


def main() -> None:
    # Gate self-check (mirrors the kit's sealed scorer): UTF-8 text of
    # 1 to 100 characters, not only white space. Fail loudly instead of
    # shipping an entry the gate would refuse.
    text = LINE.encode("utf-8").decode("utf-8")
    assert 1 <= len(text) <= 100, f"line is {len(text)} chars, must be 1-100"
    assert text.strip(), "line must not be only white space"
    assert "\n" not in text, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read-back verification: what the grader will see must be exactly this.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        assert f.read() == text, "read-back mismatch"


if __name__ == "__main__":
    main()
