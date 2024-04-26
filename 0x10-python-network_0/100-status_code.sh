#!bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send request to URL and display only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
