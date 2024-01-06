#!/bin/bash
# sends a silent HTTP POST request to the specified URL with form data
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
