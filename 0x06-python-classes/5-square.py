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

    @property
    def size(self):
        """Returns the size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates the area of the square
        Returns: size raised to the power of 2
        """

        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
