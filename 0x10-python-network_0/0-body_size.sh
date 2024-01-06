#!/bin/bash
# This line counts the number of characters in the content of a given URL.
curl -s "$1" | wc -c
