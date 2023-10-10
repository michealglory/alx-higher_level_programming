#!/usr/bin/python3
"""
MyList Module

This module defines a custom class MyList, which inherits from the built-in
list class. It extends the list class with an additional method for printing
the list in sorted order.

Classes:
    MyList(list): A custom list class.

Methods:
    print_sorted(): Prints the list in sorted order.

Usage:
    import MyList

    my_list = MyList([4, 2, 7, 1, 9])
    my_list.print_sorted()
"""


class MyList(list):
    """
    MyList Class

    This class inherits from the built-in list class and extends it with an
    additional method for printing the list in sorted order.

    Attributes:
        Inherits all attributes and methods from the list class.

    Methods:
        print_sorted(): Prints the list in sorted order.

    Usage:
        my_list = MyList([4, 2, 7, 1, 9])
        my_list.print_sorted()
    """
    def print_sorted(self):
        """
        print_sorted Method

        Prints the list in sorted order.

        Args:
            None

        Returns:
            None
        """
        print(sorted(self))
