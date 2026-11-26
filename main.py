"""One Star, Five Stars for the Food — make.fun entry.

Writes a single sentence to /output/entry.txt: a one-star review of
planet Earth from an alien tourist that still compliments the food.

Pure Python 3.13 standard library only. Deterministic, no network.
"""

import os

ENTRY = (
    "One star: Earth made me queue for hours, pay for water, and watch "
    "a man argue with a parking meter \u2014 then served me a nasi goreng "
    "so good I almost upgraded the whole planet to two stars."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
