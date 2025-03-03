#!/usr/bin/env python3
import sys

# Process each line from standard input
for line in sys.stdin:

    line = line.strip()  # Remove leading/trailing whitespace
    if "DOLocationID" in line:
        continue  # Skip header line

    parts = line.split(',')  # Split line into parts
    DOLocationID = parts[8]  # Extract drop-off location ID

    print(DOLocationID)  # Output drop-off location ID
