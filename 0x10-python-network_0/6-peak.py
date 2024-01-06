#!/usr/bin/python3
""" Finds the peak in a list of integers that aren't sorted
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of unsorted integers
    Returns: peak or None
    """
    size = len(list_of_integers)
    center_e = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        center_e = center_e // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if center_e // 2 == 0:
                center_e = 2
            mid = mid + center_e // 2
        elif center_e > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if center_e // 2 == 0:
                center_e = 2
            mid = mid - center_e // 2
        else:
            return list_of_integers[mid]
