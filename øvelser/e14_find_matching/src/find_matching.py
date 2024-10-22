#!/usr/bin/env python3


def find_matching(L, pattern) -> list[int]:
    matches: list[int] = []
    for index, word in enumerate(iterable=L):
        if pattern in word:
            matches.append(index)

    return matches


def main():
    print(find_matching(L=["sensitive", "engine", "rubbish", "comment"], pattern="en"))


if __name__ == "__main__":
    main()
