#!/usr/bin/python3
"""
This script reads data from stdin line by line and computes
metrics on the input data.

Input format: <IP Address> - [<date>] "GET /projects/260
HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
it prints the following statistics since the beginning:
- Total file size: File size: <total size> (sum of all previous sizes)
- Number of lines by status code (in ascending order).
Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500.

Example:
    $ cat 101-generator.py | ./101-stats.py
    File size: 5213
    200: 2
    401: 1
    403: 2
    404: 1
    405: 1
    500: 3
    File size: 11320
    200: 3
    301: 2
    400: 1
    401: 2
    403: 3
    404: 4
    405: 2
    500: 3

Note:
- If a status code doesn't appear in the input, it won't be included in
the output.
- Status codes are printed in ascending order.
"""


import sys
from collections import defaultdict

total_size = 0
status_codes = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_size += file_size
            status_codes[status_code] += 1

        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
