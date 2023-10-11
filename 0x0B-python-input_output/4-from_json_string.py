#!/usr/bin/python3
"""This module defines a function that returns the Python object representation
of a JSON string."""


import json


def from_json_string(my_str):
    """
    Returns the Python object representation of a JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        Any: The Python object represented by the input JSON string.
    """
    return json.loads(my_str)
