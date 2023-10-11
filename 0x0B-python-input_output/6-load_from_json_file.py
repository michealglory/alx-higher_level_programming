#!/usr/bin/python3
"""This module defines a functin that reads a JSON file and creates a
Python object from its contents."""


import json


def load_from_json_file(filename):
    """
    Reads a JSON file and creates a Python object from its contents.

    Args:
        filename (str): The name of the JSON file to be read.

    Returns:
        object: The Python object created from the JSON data in the file.
    """
    with open(filename) as f:
        return json.load(f)
