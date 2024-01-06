#!/bin/bash
# sends a silent HTTP POST request with a JSON payload 
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
