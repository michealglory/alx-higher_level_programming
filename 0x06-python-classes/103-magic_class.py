#!/usr/bin/python3
"""Magic class that calculates the area and circumference of a circle"""
import math
class MagicClass:
    """Blueprint of the margic class"""

    def __init__(self, radius=0):
        """Constructor of MagicClass object"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates the area of a square"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of a square"""
        return 2 * math.pi * self.__radius
