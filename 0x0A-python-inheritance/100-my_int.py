#!/usr/bin/python3
"""
MyInt Module

This module defines a MyInt class that inherits from the int class.
The MyInt class overrides the equality operators (== and !=) to invert
their behavior.

Classes:
    MyInt: A class for representing integers with inverted equality
    operators.

Usage:
    from myint import MyInt
    my_int = MyInt(value)
"""


class MyInt(int):
    """
    MyInt Class

    A class for representing integers with inverted equality operators
    (== and !=).
    It inherits from the int class and overrides these operators to invert
    their behavior.

    Attributes:
        N/A

    Methods:
        __eq__(self, value): Overrides the equality operator (==) with
        inequality behavior.
        __ne__(self, value): Overrides the inequality operator (!=) with
        equality behavior.

    Usage:
        my_int = MyInt(value)
    """

    def __eq__(self, value):
        """
        __eq__() Method

        Overrides the equality operator (==) to perform inequality behavior.

        Args:
            value (int): The value to compare against.

        Returns:
            bool: True if the values are not equal, False otherwise.

        Usage:
            result = my_int == value
        """
        return self.real != value

    def __ne__(self, value):
        """
        __ne__() Method

        Overrides the inequality operator (!=) to perform equality behavior.

        Args:
            value (int): The value to compare against.

        Returns:
            bool: True if the values are equal, False otherwise.

        Usage:
            result = my_int != value
        """
        return self.real == value
