#!/usr/bin/env python3


def main() -> None:
    for i in range(1, 11):
        print(" ".join([f"{str(object=i * j): >3}" for j in range(1, 11)]))


if __name__ == "__main__":
    main()
