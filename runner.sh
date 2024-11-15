#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: ./runner <hotel_ids> <destination_ids>"
    exit 1
fi

hotel_ids="$1"
destination_ids="$2"

python3 main.py "$hotel_ids" "$destination_ids"