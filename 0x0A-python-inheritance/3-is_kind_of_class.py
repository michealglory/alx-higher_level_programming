#!/usr/bin/python3
"""
is_kind_of_class Module

This module defines a function is_kind_of_class that checks if an object is an
instance of a specified class or any class that inherits from it.

Functions:
    is_kind_of_class(obj, a_class): Checks if an object is an instance of a
    class
    or any of its subclasses.

Usage:
    import is_kind_of_class

    result = is_kind_of_class(my_object, MyClass)
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class Function

    Checks if an object is an instance of a specified class or any class that
    inherits from it.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or its subclasses, otherwise
        False.

    Usage:
        result = is_kind_of_class(my_object, MyClass)
    """
    return (isinstance(obj, a_class))
