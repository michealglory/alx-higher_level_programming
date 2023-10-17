#!/usr/bin/python3
"""
This module contains a class to represent squares.
It is based on the Rectangle class and inherits its attributes and methods.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.

    Attributes:
        size (int): The side length of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): An optional identifier for the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Initializes a square instance with size, position, and an optional
        identifier.

        Args:
            size (int): The side length of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): An optional identifier for the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The side length of the square.
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The side length of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        Updates attributes of the square instance.

        Args:
            *args: A list of arguments for object attributes.
            **kwargs: Keyword arguments for object attributes.
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
            dict: A dictionary containing the square's attributes.
        """

        obj_dictionary = {'id': self.id, 'size': self.size, 'x': self.x,
                          'y': self.y}

        return obj_dictionary
