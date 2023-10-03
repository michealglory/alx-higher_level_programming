#!/usr/bin/python3
"""
Max Integer Finder
This module contains a function to find the maximum integer in a list
of integers.

"""


def max_integer(list=[]):
    """
    Finds and returns the maximum integer in a list of integers.

    Args:
        list (list of int): The input list of integers.

    Returns:
        int or None: The maximum integer found in the list.
        Returns None if the list is empty.
    """

    if len(list) == 0:
        return None
    output = list[0]
    count = 1
    while count < len(list):
        if list[count] > output:
            output = list[count]
        count += 1
    return output
