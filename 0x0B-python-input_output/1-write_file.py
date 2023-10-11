#!/usr/bin/python3
"""Defines a function that writes to a  Writes a string to a UTF-8
text file."""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text content to write to the file.

    Returns:
        int: The number of characters written to the file.

    Raises:
        Exception: If there's an issue writing to the file or encoding.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
