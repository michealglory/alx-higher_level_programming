#!/usr/bin/python3
"""Sends an HTTP POST request to the specified URL with email data."""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email_value = {"email": sys.argv[2]}
    email_data = urllib.parse.urlencode(email_value).encode("ascii")

    request = urllib.request.Request(url, email_data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
