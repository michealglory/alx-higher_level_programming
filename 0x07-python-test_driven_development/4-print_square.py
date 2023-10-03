#!/usr/bin/python3
"""
Print Square Function
This module contains a function that prints a square made of '#' characters.

"""


def print_square(size):
    """
    Prints a square made of '#' characters.

    Args:
        size (int): The side length of the square.

    Raises:
        TypeError: If 'size' is not an integer.
        ValueError: If 'size' is less than zero.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        print("")
