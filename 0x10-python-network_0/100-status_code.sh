#!/bin/bash
# retrieves the HTTP status code of the specified URL, suppressing other output.
curl -s -o /dev/null -w "%{http_code}" "$1"
