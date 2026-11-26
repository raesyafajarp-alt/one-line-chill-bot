#!/usr/bin/env python3
"""One Line, One Chill — a make.fun entry.

Writes the single scariest sentence (under 200 characters)
to /output/entry.txt.
"""

import os

ENTRY = (
    "The voicemail from my own number said, 'Don't answer the door,' "
    "and then the doorbell rang twice \u2014 once for me, and once "
    "for the voice still talking."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
