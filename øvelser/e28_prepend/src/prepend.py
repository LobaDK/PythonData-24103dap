#!/usr/bin/env python3


class Prepend(object):
    def __init__(self, start: str) -> None:
        self.start: str = start

    def write(self, string: str) -> None:
        print(self.start + string)


def main() -> None:
    test = Prepend(start=">>> ")
    test.write(string="Python")


if __name__ == "__main__":
    main()
