#!/bin/bash
# The command retrieves the "Allow" header from the HTTP headers of the
# specified URL.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
