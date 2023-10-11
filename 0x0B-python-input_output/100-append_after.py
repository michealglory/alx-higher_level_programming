#!/usr/bin/python3
"""This module defines a function that inserts text after each line
containing a specified string in a text file."""


def append_after(filename, search_string, new_string):
    """Inserts text after each line containing a specified string
    in a text file.

    Args:
        filename (str): The name of the file to process.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line
        containing the search string.

    Returns:
        None

    Example:
        Given a file named 'example.txt' with the following content:
        ```
        Line 1: Hello
        Line 2: World
        Line 3: Hello again
        ```

        To insert ' (inserted)' after lines containing 'Hello':
        ```
        append_after('example.txt', 'Hello', ' (inserted)')
        ```

        The updated content of 'example.txt' will be:
        ```
        Line 1: Hello (inserted)
        Line 2: World
        Line 3: Hello again (inserted)
        ```
    """
    modified_text = ""
    with open(filename) as file:
        for line in file:
            modified_text += line
            if search_string in line:
                modified_text += new_string
    with open(filename, "w") as output_file:
        output_file.write(modified_text)
