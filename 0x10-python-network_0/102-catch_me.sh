#!/bin/bash

# Send a request to 0.0.0.0:5000/catch_me with custom header to trigger the response
curl -s -X PUT -d "User_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me