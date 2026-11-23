#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint — writes one line to /output/entry.txt.

Deterministic, no network, no randomness: the chosen line is embedded
below as a literal and written verbatim. One line, one useless gift: total
recall of every café Wi-Fi password, arriving exactly one visit too late —
the flaw is specific, vivid, and pays off in the last words.
"""

from pathlib import Path

TEXT = (
    "I can instantly recall the Wi-Fi password of any café — but only after "
    "I've paid, packed up, and sworn never to come back."
)


def main() -> None:
    # Gate: 1 to 200 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 200, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
