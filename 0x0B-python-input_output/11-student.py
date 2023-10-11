#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student with the given attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student.

        Args:
            attrs (list, optional): A list of strings representing the
            attributes to include in the dictionary.
                If None, all attributes are included.

        Returns:
            dict: A dictionary containing attribute names and their
            corresponding values.
        """
        if (isinstance(attrs, list) and
                all(isinstance(atr, str) for atr in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student with the provided
        dictionary.

        Args:
            json (dict): A dictionary containing attribute names and their
            corresponding values to update the Student.

        """
        for key, value in json.items():
            setattr(self, key, value)
