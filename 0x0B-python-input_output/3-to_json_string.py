#!/usr/bin/python3
"""This module defines a function that returns the JSON representation
of a Python object."""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object.

    Args:
        my_obj: The Python object to be converted to JSON.

    Returns:
        str: The JSON representation of the input Python object.
    """
    return json.dumps(my_obj)
