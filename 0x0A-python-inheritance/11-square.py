#!/usr/bin/python3
"""
Square Module

This module defines a Square class that inherits from the Rectangle
class and represents squares and their attributes.

Classes:
    Square: A class for representing squares and their attributes.

Usage:
    from square import Square
    square = Square(size)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square Class

    A class for representing squares and their attributes. It inherits
    from the Rectangle class and defines a constructor to initialize square
    dimensions, which are equal for both width and height.

    Attributes:
        __size (int): The size of the square (both width and height).

    Methods:
        __init__(self, size): Initializes a new Square instance.
        __str__(self): Returns a human-readable string representation of
        the square.

    Usage:
        square = Square(size)
    """

    def __init__(self, size):
        """
        __init__() Method

        Initializes a new Square instance with the specified size.

        Args:
            size (int): The size of the square (both width and height).

        Usage:
            square = Square(5)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        __str__() Method

        Returns a human-readable string representation of the square.

        Returns:
            str: A string representation of the square.

        Usage:
            print(square)
            str_representation = str(square)
        """
        square_string = "[" + str(self.__class__.__name__) + "] "
        square_string += str(self.__size)
        return square_string
