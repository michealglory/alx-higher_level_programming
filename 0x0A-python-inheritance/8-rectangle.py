#!/usr/bin/python3
"""
Rectangle Module

This module defines a Rectangle class that inherits from the BaseGeometry
class.

Classes:
    Rectangle: A class for representing rectangles and their attributes.

Usage:
    from rectangle import Rectangle
    rectangle = Rectangle(width, height)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle Class

    A class for representing rectangles and their attributes. It inherits
    from the BaseGeometry class and defines a constructor to initialize
    rectangle dimensions.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a new Rectangle instance.

    Usage:
        rectangle = Rectangle(width, height)
    """

    def __init__(self, width, height):
        """
        __init__() Method

        Initializes a new Rectangle instance with the specified width and
        height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Usage:
            rectangle = Rectangle(5, 10)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
