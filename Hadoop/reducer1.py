#!/usr/bin/env python3
import sys

current_pulocation_id = None
total_distance = 0.0
results = {}

# Process each line from standard input
for line in sys.stdin:
    parts = line.strip().split('\t')  # Split line into parts
    if len(parts) != 2:
        continue  # Skip malformed lines

    pulocation_id, trip_distance = parts
    pulocation_id = int(pulocation_id)  # Convert location ID to integer
    trip_distance = float(trip_distance)  # Convert trip distance to float

    if current_pulocation_id == pulocation_id:
        total_distance += trip_distance  # Accumulate distance for the same location
    else:
        if current_pulocation_id is not None:
            results[current_pulocation_id] = total_distance  # Store total distance for the previous location
        current_pulocation_id = pulocation_id  # Update current location ID
        total_distance = trip_distance  # Reset distance for the new location

# Store total distance for the last location
if current_pulocation_id is not None:
    results[current_pulocation_id] = total_distance

# Output results
for pulocation_id in sorted(results.keys()):
    print(f"{pulocation_id},{results[pulocation_id] :.2f}")
