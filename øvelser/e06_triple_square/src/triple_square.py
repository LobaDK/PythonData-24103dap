#!/usr/bin/env python3


def triple(n: int) -> int:
    return n * 3


def square(n: int) -> int:
    return n**2


def main() -> None:
    for i in range(1, 11):
        _triple = triple(i)
        _square = square(i)
        if _square > _triple:
            break
        print(f"triple({i})=={_triple} square({i})=={_square}")


if __name__ == "__main__":
    main()
