#!/bin/bash


# Check if URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send OPTIONS request to URL and display allowed methods
curl -s -i -X OPTIONS "$1" | awk '/Allow/{print $2}'
