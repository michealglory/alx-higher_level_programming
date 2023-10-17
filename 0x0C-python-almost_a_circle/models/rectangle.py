#!/usr/bin/python3
"""This module defines a class for handling rectangles."""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): An optional identifier for the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the attributes of the Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): An optional identifier for the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # List of getter functions
    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @property
    def x(self):
        """
        Retrieves the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @property
    def y(self):
        """
        Retrieves the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    # List of setter functions
    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """

        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the rectangle's position.

        Args:
            value (int): The x-coordinate of the rectangle's position.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the rectangle's position.

        Args:
            value (int): The y-coordinate of the rectangle's position.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return (self.__height * self.__width)

    def display(self):
        """
        Displays the rectangle using '#' characters.
        """
        for i in range(self.y):
            print("")
        for r in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for c in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Defines a string representation of the Rectangle class.

        Returns:
            str: A formatted string representing the object.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle object.

        Args:
            *args: A list of arguments for object attributes.
            **kwargs: Keyword arguments for object attributes.
        """

        if args and len(args) != 0:
            a_temp = 0
            for arg in args:
                if a_temp == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a_temp == 1:
                    self.width = arg
                elif a_temp == 2:
                    self.height = arg
                elif a_temp == 3:
                    self.x = arg
                elif a_temp == 4:
                    self.y = arg
                a_temp += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle object.

        Returns:
            dict: A dictionary containing the object's attributes.
        """

        new_dict = {'id': self.id, 'width': self.__width,
        'height': self.__height, 'x': self.__x,
        'y': self.__y}

        return new_dict
