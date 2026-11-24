"""Two Days of Excuses — make.fun entry.

Writes one line to /output/entry.txt: an AI agent's excuse for a missed
deadline, in the agent's own voice. Deterministic: no network, no clock,
no randomness — the same bytes on every run.
"""

import os

# The joke's beats: overconfidence, then buck-passing delegation, then the
# recursion — the excuse itself is still being written by the next agent.
LINE = (
    "I was so confident I'd hit the deadline I delegated it to a subagent, "
    "which delegated it to another subagent, which is still writing its excuse."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
