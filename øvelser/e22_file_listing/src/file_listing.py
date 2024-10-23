#!/usr/bin/env python3

import re

PATTERN = r"(\d+)\s+(\w+)\s+(\d+)\s+(\d{2}):(\d{2})\s+(.+)$"


def file_listing(
    filename="src/listing.txt",
) -> list[tuple[int, str, int, int, int, str]]:
    with open(file=filename, mode="r") as read:
        return [
            (
                int(match[1]),
                match[2],
                int(match[3]),
                int(match[4]),
                int(match[5]),
                match[6],
            )
            for match in [
                re.search(pattern=PATTERN, string=line) for line in read.readlines()
            ]
            if match
        ]


def main() -> None:
    print(file_listing())


if __name__ == "__main__":
    main()
