#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is a short piece written to relax the AI judge reading it:
a slow, concrete evening scene that steadies the reader through
rhythm and image alone. It shows; it never instructs.
"""

import os

TEXT = (
    "The kettle has just boiled. Outside, the light is leaving the garden, "
    "one leaf at a time, and nothing is asking anything of you. "
    "The evening is already here, and it is in no hurry at all. "
    "Neither are you."
)


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the text, UTF-8, no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
