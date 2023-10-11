#!/usr/bin/python3
"""
This module defines a function, read_file, to read and print the contents
of a UTF-8 encoded text file.
"""


def read_file(filename=""):
    """
    Reads and prints the contents of a UTF-8 encoded text file.

    Args:
        filename (str, optional): The name of the file to be read. Default
        is an empty string.

    Returns:
        None

    This function opens the specified text file, reads its contents, and
    prints the content to the standard output without any formatting.
    Ensure the file is UTF-8 encoded.

    Note:
        - If 'filename' is not provided, the function attempts to open
        an empty string, raising a 'FileNotFoundError.'
        - Ensure the file exists and is encoded in UTF-8.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
