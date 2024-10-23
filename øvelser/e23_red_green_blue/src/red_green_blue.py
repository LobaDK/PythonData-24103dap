#!/usr/bin/env python3

import re

PATTERN = r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.+)$"


def red_green_blue(
    filename="/home/lobadk/Documents/PythonData-24103dap/øvelser/e23_red_green_blue/src/rgb.txt",
) -> list[str]:
    with open(file=filename, mode="r") as read:
        return [
            f"{match[1]}\t{match[2]}\t{match[3]}\t{match[4]}"
            for match in [
                re.search(pattern=PATTERN, string=line) for line in read.readlines()
            ]
            if match
        ]


def main() -> None:
    print(red_green_blue())


if __name__ == "__main__":
    main()
