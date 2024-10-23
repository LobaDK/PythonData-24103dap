"""
This module provides functions to perform calculations related to right-angled triangles.

Functions:
    hypothenuse(l1: float, l2: float) -> float:

    area(s1: float, s2: float) -> float:

Attributes:
    __version__ (str): The version of the module.
    __author__ (str): The author of the module.
"""

__version__ = "0.1"
__author__ = "WhyDoesThisHaveToBeAtLeast5CharactersLong"
from math import sqrt


def hypothenuse(l1: float, l2: float) -> float:
    """
    Calculate the length of the hypotenuse of a right-angled triangle given the lengths of the other two sides.

    Args:
        l1 (float): The length of the first side of the triangle.
        l2 (float): The length of the second side of the triangle.

    Returns:
        float: The length of the hypotenuse.
    """
    return sqrt(l1**2 + l2**2)


def area(s1: float, s2: float) -> float:
    """
    Calculate the area of a right-angled triangle.

    Args:
        s1 (float): The length of one of the perpendicular sides of the triangle.
        s2 (float): The length of the other perpendicular side of the triangle.

    Returns:
        float: The area of the triangle.
    """
    return s1 * s2 / 2
