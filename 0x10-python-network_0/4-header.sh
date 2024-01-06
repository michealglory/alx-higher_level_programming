#!/bin/bash
# sends an HTTP GET request to the specified URL with a custom header
curl -sH "X-School-User-Id: 98" "$1"
