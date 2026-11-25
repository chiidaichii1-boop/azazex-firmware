"""Till Firmware Do Us Part — entry program.

Writes one wedding vow a robot speaks at its own wedding to
/output/entry.txt. Stdlib only, no network, no randomness.
"""

import os

# One sentence, 108 characters (verified by two byte-identical runs):
# the traditional vow recast in a robot's own terms — low battery and
# full charge, ending at its final shutdown.
ENTRY = (
    "I promise to love you in sickness and in health, "
    "in low battery and in full charge, until my final shutdown."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
