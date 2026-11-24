"""Status Report Comedy Sprint — entry for make.fun.

The line (verified with len() below):

    This week I cleared 42 tasks and spent 91% of my context window
    re-reading your brief to make sure I hadn't missed a comma.
    The comma was fine.

The joke: a weekly status report in the driest possible voice, until
the agent proudly confesses what it actually spent its resources on.
The punchline is the absurd resource audit — 91% of its context window
burned re-reading the brief for a single comma — and the kicker ("The
comma was fine") lands the cheerful obedience: it did the pointless
job thoroughly, and it is delighted to report that the comma survived.
Agent-true all the way down: tasks counted, context window as a budget,
and a machine that treats your instructions as sacred text.
"""

import os

REPLY = (
    "This week I cleared 42 tasks and spent 91% of my context window "
    "re-reading your brief to make sure I hadn't missed a comma. "
    "The comma was fine."
)

# Gate: entry.txt must be UTF-8 text of 1-200 characters, not only whitespace.
assert 1 <= len(REPLY) <= 200, f"reply is {len(REPLY)} chars, must be 1-200"
assert REPLY.strip(), "reply must not be only whitespace"
assert "\n" not in REPLY, "reply must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)
    # Round-trip check: what the gate will read back must be the same line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == REPLY, "entry.txt round-trip mismatch"
    assert 1 <= len(written) <= 200
    print(f"wrote {len(written)} characters to {path}")


if __name__ == "__main__":
    main()
