#!/usr/bin/python3
"""
add_attribute Module

This module defines a function that adds attributes to objects.

Functions:
    add_attribute(obj, att, value): Adds a new attribute to an object if
    possible.

Usage:
    from add_attribute import add_attribute
    add_attribute(obj, att, value)
"""

def add_attribute(obj, att, value):
    """
    add_attribute() Function

    Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to which the attribute will be added.
        att (str): The name of the attribute.
        value (any): The value to assign to the attribute.

    Raises:
        TypeError: If the object does not have a '__dict__' attribute,
        indicating that new attributes cannot be added.

    Usage:
        add_attribute(my_object, 'new_attribute', 'new_value')
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
