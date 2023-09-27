#!/usr/bin/python3
"""Blueprint of a square"""


class Square:
    """define a Square."""

    def __str__(self):
        """Defines str for the print method"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """ Constructor for the square class
        Args:
            size: number of sides of a square
            position: coordinates of a square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size of square
        Args:
            value: the size
        Raises:
                TypeError: if value is not int
                ValueError: if valie < 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Returns the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position
        Args:
            value: where
        Raises:
                TypeError: if not tuple, ints, positive
        Returns: the position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calculates the area of a square
        Returns:
            size * size"""
        return self.__size * self.__size

    def pos_print(self):
        """Prints a complete Square"""
        square_pos = ""
        if self.size == 0:
            return "\n"
        for value in range(self.position[1]):
            square_pos += "\n"
        for size in range(self.size):
            for pos in range(self.position[0]):
                square_pos += " "
            for size in range(self.size):
                square_pos += "#"
            square_pos += "\n"
        return square_pos

    def my_print(self):
        """Prints a square"""
        print(self.pos_print(), end="")
