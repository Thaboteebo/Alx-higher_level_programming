#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then 
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send GET request to URL and display body only if response code is 200
curl -s -o /tmp/body.txt -w "%{http_code}" "$1" | {
	read response_code
	if [ "$response_code" -eq 200]; then
		cat /tmp/body.txt
	fi
}
