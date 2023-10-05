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
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calculate Area

        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        Example:
            >>> rect = Rectangle(4, 5)
            >>> rect.area()
            20
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate Perimeter

        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle. If either width or height
            is zero, returns 0.

        Example:
            >>> rect = Rectangle(4, 5)
            >>> rect.perimeter()
            18
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """
        String Representation

        Returns a string representation of the rectangle, presenting it
        as a diagram
        consisting of '#' characters, with each '#' representing a unit
        of the rectangle's width and height.

        Returns:
            str: A string representing the rectangle's diagram.
            If either width or height is zero, returns an empty string.

        Example:
            >>> rect = Rectangle(4, 5)
            >>> print(rect)
            ####
            ####
            ####
            ####
            ####
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for col in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if col < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """
        Representation for Debugging

        Returns a string representation of the rectangle, formatted as a
        constructor
        call to create an identical Rectangle object. This is primarily used
        for debugging and can be used to recreate the object.

        Returns:
            str: A string representing the Rectangle object in constructor
            call format.

        Example:
            >>> rect = Rectangle(4, 5)
            >>> repr(rect)
            'Rectangle(4, 5)'
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Object Deletion

        Provides a message when an object of the Rectangle class is deleted.
        This message is printed to indicate that the object is being removed
        from memory.

        Example:
            >>> rect = Rectangle(4, 5)
            >>> del rect
            Bye rectangle...
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare Rectangles by Area

        Compares two Rectangle objects based on their areas and returns
        the larger or equal one.

        Args:
            rect_1 (Rectangle): The first Rectangle object to compare.
            rect_2 (Rectangle): The second Rectangle object to compare.

        Returns:
            Rectangle: The larger or equal Rectangle object.

        Raises:
            TypeError: If either `rect_1` or `rect_2` is not an instance
            of the Rectangle class.

        Example:
            >>> rect1 = Rectangle(4, 5)
            >>> rect2 = Rectangle(3, 6)
            >>> bigger = Rectangle.bigger_or_equal(rect1, rect2)
            >>> bigger
            Rectangle(4, 5)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a Square Rectangle

        Creates a square Rectangle object with the specified size.

        Args:
            cls (type): The class (Rectangle) to create the square object
            from.
            size (int, optional): The size of the square rectangle
            (default is 0).

        Returns:
            Rectangle: A square Rectangle object with equal width and height.

        Example:
            >>> square = Rectangle.square(4)
            >>> square
            Rectangle(4, 4)
        """
        return Rectangle(size, size)
