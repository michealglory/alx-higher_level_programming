#!/usr/bin/python3
"""
is_same_class Module

This module defines a function is_same_class that checks if an object is an
instance of a specified class.

Functions:
    is_same_class(obj, a_class): Checks if an object is an instance of a
    class.

Usage:
    import is_same_class

    result = is_same_class(my_object, MyClass)
"""


def is_same_class(obj, a_class):
    """
    is_same_class Function

    Checks if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class, otherwise False.

    Usage:
        result = is_same_class(my_object, MyClass)
    """
    return (type(obj) == a_class)
