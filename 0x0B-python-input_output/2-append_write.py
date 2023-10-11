#!/usr/bin/python3
"""This module defines a function that appends a string to the end of
a UTF-8 text file."""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text content to append to the file.

    Returns:
        int: The number of characters appended to the file.

    Raises:
        Exception: If there's an issue appending to the file or encoding.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
