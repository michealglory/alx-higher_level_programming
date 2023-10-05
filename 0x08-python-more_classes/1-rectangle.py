#!/usr/bin/python3
"""
Rectangle Class

This module defines a Rectangle class that represents a
geometric rectangle.
It provides methods to initialize, retrieve, and set the width
and height of the rectangle.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""


class Rectangle:
    """
    Rectangle Class

    Represents a rectangle with specified width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a new Rectangle instance with the given width and
            height.

        width(self):
            Retrieves the width of the rectangle.

        width(self, value):
            Sets the width of the rectangle. Must be a positive integer.

        height(self):
            Retrieves the height of the rectangle.

        height(self, value):
            Sets the height of the rectangle. Must be a positive integer.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is
            0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than zero.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
