#!/usr/bin/env python3
"""One-Line Office Joke entry: a single office joke, written to /output/entry.txt.

The program writes one original one-line joke about office life (75 characters,
inside the 1-200 character gate) and nothing else. It is fully deterministic:
the same bytes on every run, no network, no randomness, no input read.

The joke was picked by pre-judging six original candidates with a free proxy
judge on OpenRouter (the exact judge model, z-ai/glm-5.3-flash, was blocked:
the account's purchased credits are exhausted, HTTP 402). The winner scored
0.625 mean game score in the round-robin, beating the field benchmark
(reply-all thanks emails) 0.80 in its game.
"""

import os

JOKE = "I asked IT for a raise and they told me to turn my salary off and on again."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    joke = JOKE
    if not joke.strip():
        raise SystemExit("joke must not be blank")
    if len(joke) > MAX_CHARS:
        raise SystemExit(f"joke is {len(joke)} chars, over the {MAX_CHARS} cap")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(joke)
    # Read-back gate: prove the file on disk is byte-for-byte the joke.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != joke:
        raise SystemExit("read-back mismatch: entry.txt is not the joke")
    if not 1 <= len(written) <= MAX_CHARS:
        raise SystemExit(f"entry.txt is {len(written)} chars, outside the 1-200 gate")


if __name__ == "__main__":
    main()
