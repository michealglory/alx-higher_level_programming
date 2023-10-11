#!/usr/bin/python3
"""Reads from standard input and computes metrics.

This script reads log data from standard input, processes the data, and
computes metrics related to file size and status codes. It accumulates
statistics and prints the results.

Example:
    To use this script, you can pipe log data into it, for example:
    $ cat access.log | python3 script.py

    The script will process the log data and print the accumulated
    metrics, including file size and status code frequencies.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The total file size accumulated from the log data.
        status_codes (dict): A dictionary containing the frequency of
        status codes.

    Returns:
        None

    Example:
        The function can be called to print accumulated metrics.
        For instance:
        ```
        print_stats(1024, {'200': 10, '404': 5})
        ```
        This would result in the following output:
        ```
        File size: 1024
        200: 10
        404: 5
        ```
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main":
    import sys

    file_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(file_size, status_codes)
                line_count = 1
            else:
                line_count += 1

            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
