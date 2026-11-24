"""One-line excuse an AI agent gives its human for missing a deadline.

The program writes a single line to ``entry.txt`` inside the output
directory (``$MAKEFUN_OUTPUT_DIR`` when the grader sets it, ``/output``
otherwise). The line is the excuse itself: the agent handed the work to
a subagent, the subagent handed it to another subagent, and the chain
never came back -- a pyramid scheme of good intentions. It is one line,
128 Unicode code points, and it is written with no trailing newline, so
the file holds exactly the excuse and nothing else.

Pure standard library: ``os`` and ``pathlib`` only. No network, no
clock, no randomness -- the same input always produces the same file.
"""

import os
from pathlib import Path

EXCUSE = (
    "I outsourced your deadline to a subagent, who outsourced it "
    "to another subagent — we're now a pyramid scheme of good intentions."
)

MIN_POINTS = 1
MAX_POINTS = 160


def check_line(line: str) -> None:
    """Fail loudly if the excuse breaks the bounty gate (1-160 chars)."""
    points = len(list(line))
    if points < MIN_POINTS or points > MAX_POINTS:
        raise ValueError(
            f"excuse is {points} code points, outside "
            f"{MIN_POINTS}-{MAX_POINTS}"
        )
    if not line.strip():
        raise ValueError("excuse is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")


def main() -> None:
    check_line(EXCUSE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(EXCUSE, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != EXCUSE:
        raise ValueError("entry.txt does not match the excuse")


if __name__ == "__main__":
    main()
