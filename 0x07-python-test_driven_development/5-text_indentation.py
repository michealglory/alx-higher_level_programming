#!/usr/bin/python3
"""
Text Indentation Function
This module contains a function that indents text by adding two new
lines after each ".", "?", or ":".

"""


def text_indentation(text):
    """
    Indents text by adding two new lines after each ".", "?", or ":".

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If 'text' is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    total = 0
    while total < len(text) and text[total] == " ":
        total = total + 1

    while total < len(text):
        print(text[total], end="")
        if text[total] == "\n" or text[total] in ".?:":
            if text[total] in ".?:":
                print("\n")
            total = total + 1
            while total < len(text) and text[total] == " ":
                total = total + 1
            continue
        total = total + 1
