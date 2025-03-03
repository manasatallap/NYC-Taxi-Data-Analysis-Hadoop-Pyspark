#!/usr/bin/env python3

import sys

# Process each line from the standard input
for line in sys.stdin:
    # Strip any leading or trailing whitespace
    line = line.strip()
    # Split the line into parts by comma
    parts = line.split(',')

    # Extract the pickup time and distance from the parts
    pickup_time = parts[1]
    distance = parts[4]

    # Check if the pickup time contains a colon (indicating it's a valid time)
    if ':' in pickup_time:
        # Extract the hour from the pickup time
        hour = pickup_time.split()[1].split(':')[0]
        # Print the hour and distance, separated by a tab
        print(f"{hour}\t{distance}")
    else:
        # Print an error message for an invalid timestamp
        print(f"Invalid timestamp: {pickup_time}")
