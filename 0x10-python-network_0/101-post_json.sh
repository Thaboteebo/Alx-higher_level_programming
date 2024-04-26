#!/bin/bash

# Check if URL and filename are provided
if [ -z "$1" ] || [ -z "$2" ]; then
	echo "Usage: $0 <URL> <filename>"
	exit 1
fi

# Read the content of the file
json_content=$(cat "$2")

# Validate JSON content
if ! jq -e . >/dev/null 2>&1 <<<"$json_content"; then
	echo "Not a valid JSON"
	exit 1
fi

# Send JSON POST  request and display response body
curl -s -X POST  -H "Content-Type: application/json" -d "$json_content" "$1"
