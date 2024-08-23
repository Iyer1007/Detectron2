#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: ./run_process_image.sh <image_url>"
    exit 1
fi

# Store the image URL from the argument
IMAGE_URL=$1

# Run the Python script with the provided image URL
python3 main.py "$IMAGE_URL"
