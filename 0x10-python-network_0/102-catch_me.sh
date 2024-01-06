#!/bin/bash
# sends a silent HTTP PUT request with the specified headers and data to the given URL.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
