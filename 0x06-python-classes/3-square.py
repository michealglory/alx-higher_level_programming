#!/usr/bin/python3
"""Templates of a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Constructor for the square class
        Args:
            size: size of square. Default to 0.
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero"""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculates the area of the square
        Returns: size raised to the power of 2
        """

        return (self.__size ** 2)
