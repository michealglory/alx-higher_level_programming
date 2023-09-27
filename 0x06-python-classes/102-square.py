#!/usr/bin/python3
"""Blueprints of a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Constructor for the square object
        Args: size: size of square
        """
        self.__size = size

    @property
    def size(self):
        """return the value of size"""
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
        """Calculates the area of a square"""
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
