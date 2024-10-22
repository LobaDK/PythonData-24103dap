#!/usr/bin/env python3


def positive_list(L: list[int]) -> list[int]:
    return list(filter(lambda x: x > 0, L))


def main() -> None:
    test_list: list[int] = [2, -2, 0, 1, -7]
    print(positive_list(L=test_list))


if __name__ == "__main__":
    main()
