#!/bin/bash
# fetches a resource from a given URL using cURL, with silent mode and
# following redirects.
curl -sL "$1"
