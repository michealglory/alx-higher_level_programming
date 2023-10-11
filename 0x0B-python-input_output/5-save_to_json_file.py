#!/usr/bin/python3
"""This module defines a function that writes a Python object to a text
file using JSON format."""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON format.

    Args:
        my_obj (object): The Python object to be saved to the file.
        filename (str): The name of the file where the object will be saved.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
