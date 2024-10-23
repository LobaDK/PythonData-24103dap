#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle


def main():
    print(triangle.hypothenuse(l1=3, l2=4))
    print(triangle.area(s1=3, s2=4))


if __name__ == "__main__":
    main()
