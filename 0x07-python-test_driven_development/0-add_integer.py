#!/usr/bin/python3
"""

A module that sums up two numbers.

"""


def add_integer(a, b=98):
    """Return the sum of two numbers (integers or floats) as integers

    Args:
        a: first number
        b: second number

    Returns:
        Sum of the two arguments

    Raises:
        TypeError: If either of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
