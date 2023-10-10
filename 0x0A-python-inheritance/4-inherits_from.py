#!/usr/bin/python3
"""
inherits_from Module

This module defines a function inherits_from that checks if an object is an
instance of a class that inherited (directly or indirectly) from the specified
class.

Functions:
    inherits_from(obj, a_class): Checks if an object is an instance of a class
    that inherits (directly or indirectly) from the specified class.

Usage:
    import inherits_from

    result = inherits_from(my_object, MyClass)
"""


def inherits_from(obj, a_class):
    """
    inherits_from Function

    Checks if an object is an instance of a class that inherited (directly or
    indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class; otherwise, False.

    Usage:
        result = inherits_from(my_object, MyClass)
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
