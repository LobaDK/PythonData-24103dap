#!/usr/bin/env python3


def main() -> None:
    dice_1 = range(1, 7)
    dice_2 = range(1, 7)
    expected_sum = 5

    for i in dice_1:
        for j in dice_2:
            if i + j == expected_sum:
                print(f"({i},{j})")


if __name__ == "__main__":
    main()
