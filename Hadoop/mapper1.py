#!/usr/bin/env python3
import sys

# Function to check if a value can be converted to a float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Flag to skip the header row in the input data
header = True

# Iterate over each line from the standard input
for line in sys.stdin:
    if header:
        # Skip the header row
        header = False
        continue

    # Split the line into columns based on comma delimiter
    data = line.strip().split(',')
    
    # Check if there are at least 8 columns, the 8th column is a digit, and the 5th column is a float
    if len(data) >= 8 and data[7].isdigit() and is_float(data[4]):
        # Extract the pickup location ID and trip distance
        pulocation_id = int(data[7])
        trip_distance = float(data[4])

        # Print the pickup location ID and trip distance as tab-separated values
        print(f"{pulocation_id}\t{trip_distance}")
