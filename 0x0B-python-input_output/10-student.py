#!/usr/bin/python3
"""Defines a Student class with methods for dictionary conversion."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with personal information."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student's attributes.

        Args:
            attrs (list): Optional list of strings representing the attributes
            to include.

        Returns:
            dict: A dictionary containing specified attribute-value pairs.
        """
        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
