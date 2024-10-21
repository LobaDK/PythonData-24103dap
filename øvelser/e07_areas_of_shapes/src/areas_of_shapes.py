#!/usr/bin/env python3

import math

shapes: list[str] = ["triangle", "rectangle", "circle"]


def calculate_area_of_triangle(base: float, height: float) -> float:
    return 0.5 * base * height


def calculate_area_of_rectangle(height: float, width: float) -> float:
    return height * width


def calculate_area_of_circle(radius: float) -> float:
    return math.pi * math.pow(radius, 2)


def main() -> None:
    while True:
        chosen_shape: str = input(f"Choose a shape ({", ".join(shapes)}): ").lower()
        if not chosen_shape:
            break

        if chosen_shape not in shapes:
            print("Unknown shape!")
            continue

        if chosen_shape == "triangle":
            tri_base = float(input("Give base of the triangle: "))
            tri_height = float(input("Give height of the triangle: "))
            area: float = calculate_area_of_triangle(base=tri_base, height=tri_height)

        elif chosen_shape == "rectangle":
            rect_width = float(input("Give width of the rectangle: "))
            rect_height = float(input("Give height of the rectangle: "))
            area = calculate_area_of_rectangle(rect_height, rect_width)

        elif chosen_shape == "circle":
            circ_radius = float(input("Give radius of the circle: "))
            area = calculate_area_of_circle(circ_radius)

        print(f"The area is {area}")


if __name__ == "__main__":
    main()
