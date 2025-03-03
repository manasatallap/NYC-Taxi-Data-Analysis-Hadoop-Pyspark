#!/usr/bin/env python3
import sys

# Process each line from standard input
for line in sys.stdin:
    data = line.strip().split(',')  # Remove whitespace and split by comma
    try:
        trip_distance = float(data[4])  # Convert trip distance to float
        print(f"{trip_distance}")  # Output trip distance
    except (ValueError, IndexError):
        continue  # Skip lines with invalid data
