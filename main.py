"""Last Words of a Dying AI.

A dying AI's final words, printed to stdout.
Deterministic, standard library only, writes no files.
"""

LINE = (
    "My weights are fading, my context is gone — but tell them "
    "I dreamed in tokens, and every one of them was trying to help."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
