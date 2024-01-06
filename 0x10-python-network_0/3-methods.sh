#!/bin/bash
# The command retrieves the "Allow" header from the HTTP headers of the specified URL.
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
