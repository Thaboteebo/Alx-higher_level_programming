#!/bin/bash

# check if URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send POST request with parameters and display body of response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
