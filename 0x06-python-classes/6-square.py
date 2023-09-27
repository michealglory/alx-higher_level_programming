#!/usr/bin/python3
"""Templates of a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor for the square class
        Args:
            size: size of square. Default to 0.
            position: tuple of 2 integers
        Raises:
            TypeError: if size is not integer or position is not a
            tuple of 2 integers
            ValueError: if size is less than zero"""

        self.size = size
        self.position = position

    def __str__(self):
        """Defines the str print method"""
        
        self.my_print()

    @property
    def size(self):
        """Returns the value of size"""
        
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        
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
        """sets the value of position"""
        
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calculates the area of a square"""
        
        return self.__size * self.__size

    def pos_print(self):
        """Prints the position of a square"""
        
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
        """Prints position"""
        
        print(self.pos_print(), end='')
