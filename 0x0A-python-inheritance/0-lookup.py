#!/usr/bin/python3
"""
    Lookup Module

    This module provides a function for inspecting and listing
    the attributes and methods of an object.

    Functions:
        lookup(obj): Returns a list of available attributes and methods
        of the given object.

    Usage:
        import lookup

        my_object = SomeClass()
        result = lookup.lookup(my_object)
        print(result)
"""


def lookup(obj):
    """
    Lookup Function

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings containing the names of all attributes
        and methods of the given object.
    """
    return dir(obj)
