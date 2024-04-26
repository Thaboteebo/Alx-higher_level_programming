#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send request to URL and get the size of the body in bytes
body_size=$(curl -sI "$1" | grep -i Content-Length |awk '{print $2}')

# Print the body size
echo "$body_size"
