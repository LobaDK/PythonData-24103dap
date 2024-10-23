#!/usr/bin/env python3


def sum_equation(L: list[int]) -> str:
    return " + ".join(map(str, L)) + f" = {sum(L)}" if L else "0 = 0"


def main() -> None:
    print(sum_equation([1, 5, 7]))


if __name__ == "__main__":
    main()
