#!/usr/bin/env python3
import sys

current_hour = None
total_distance = 0.0

# Process each line from standard input
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespace

    try:
        hour, distance = line.split('\t')  # Split line into hour and distance
        hour = int(hour)  # Convert hour to integer
        distance = float(distance)  # Convert distance to float

        if current_hour == hour:
            total_distance += distance  # Accumulate distance for the same hour
        else:
            if current_hour is not None:
                print(f"{current_hour},{total_distance:.2f}")  # Output total distance for the previous hour
            current_hour = hour  # Update current hour
            total_distance = distance  # Reset distance for the new hour

    except ValueError:
        print(f"Error processing line: {line}", file=sys.stderr)  # Print error message for malformed lines
        continue

# Output total distance for the last hour
if current_hour is not None:
    print(f"{current_hour},{total_distance:.2f}")
