#!/usr/bin/env python3


def transform(s1: str, s2: str) -> list[int]:
    return [
        transformed
        for transformed in map(
            lambda x: int(x[0]) * int(x[1]), zip(s1.split(), s2.split())
        )
    ]


def main() -> None:
    print(transform(s1="1 5 3", s2="2 6 -1"))


if __name__ == "__main__":
    main()
