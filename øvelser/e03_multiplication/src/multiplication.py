#!/usr/bin/env python3


def main() -> None:
    number_to_multiply: int = 4
    for i in range(11):
        result: int = number_to_multiply * i
        print(f"{number_to_multiply} multiplied by {i} is {result}")


if __name__ == "__main__":
    main()
