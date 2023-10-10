#!/usr/bin/python3
"""
Rectangle Module

This module defines a Rectangle class that inherits from the BaseGeometry
class and represents rectangles and their attributes.

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
    rectangle dimensions, an area method to calculate the area, and a
    __str__ method for a human-readable string representation.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a new Rectangle instance.
        area(self): Calculates and returns the area of the rectangle.
        __str__(self): Returns a human-readable string representation of the
        rectangle.

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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        area() Method

        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        Usage:
            area = rectangle.area()
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__() Method

        Returns a human-readable string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.

        Usage:
            print(rectangle)
            str_representation = str(rectangle)
        """
        rec_string = "[" + str(self.__class__.__name__) + "] "
        rec_string += str(self.__width) + "/" + str(self.__height)
        return rec_string
