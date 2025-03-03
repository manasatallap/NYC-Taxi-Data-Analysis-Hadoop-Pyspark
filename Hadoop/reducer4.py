#!/usr/bin/env python3
import sys
import heapq

top_distances = []

# Process each line from standard input
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespace
    try:
        distance = float(line)  # Convert distance to float
        heapq.heappush(top_distances, distance)  # Push distance onto the heap
        if len(top_distances) > 10:
            heapq.heappop(top_distances)  # Remove smallest element if heap size exceeds 10
    except ValueError:
        continue  # Skip lines with invalid data

# Output top 10 distances in descending order
for distance in sorted(top_distances, reverse=True):
    print(f"{distance:.2f}")
