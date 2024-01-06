#!/usr/bin/python3
"""Sends an HTTP GET request to the specified URL and prints the content
if the status code is less than 400.
Otherwise, prints an error message with the HTTP status code.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
