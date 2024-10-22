#!/usr/bin/env python3


def reverse_dictionary(d: dict[str, list[str]]) -> dict[str, list[str]]:
    rd: dict[str, list[str]] = {}
    for key, value in d.items():
        for w in value:
            if w in rd:
                rd[w] += [key]
            else:
                rd[w] = [key]

    return rd


def main() -> None:
    d: dict[str, list[str]] = {
        "move": ["liikuttaa"],
        "hide": ["piilottaa", "salata"],
        "six": ["kuusi"],
        "fir": ["kuusi"],
    }

    print(reverse_dictionary(d=d))


if __name__ == "__main__":
    main()
