#!/usr/bin/python3
"""
BaseGeometry Module

This module defines a base geometry class called BaseGeometry.

Classes:
    BaseGeometry: A base class for geometry-related operations.

Usage:
    from base_geometry import BaseGeometry
    geometry = BaseGeometry()
"""


class BaseGeometry:
    """
    BaseGeometry Class

    A base class for geometry-related operations. It defines a placeholder
    method for calculating the area of a geometric shape and a method for
    validating integer values.

    Methods:
        area(): Placeholder method for calculating the area of a shape.
        integer_validator(name, value): Validates that a value is an integer
            greater than 0.

    Usage:
        geometry = BaseGeometry()
    """

    def area(self):
        """
        area() Method

        This method is a placeholder for calculating the area of a geometric
        shape. It raises an exception since it is not implemented in this
        base class.

        Raises:
            Exception: This method is not implemented in the base class.

        Usage:
            geometry = BaseGeometry()
            geometry.area()  # Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator() Method

        This method validates that a value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Usage:
            geometry = BaseGeometry()
            geometry.integer_validator("side_length", 5)  # Valid
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
