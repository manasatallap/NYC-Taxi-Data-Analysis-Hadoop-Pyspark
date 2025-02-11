#!/usr/bin/env python3
import sys
import heapq

top_distances = []

for line in sys.stdin:
    line = line.strip()
    try:
        distance = float(line)
        heapq.heappush(top_distances, distance)
        if len(top_distances) > 10:
            heapq.heappop(top_distances)
    except ValueError:
        continue

for distance in sorted(top_distances, reverse=True):
    print(f"{distance:.2f}")
