#!/usr/bin/env python3
import sys

current_pulocation_id = None
total_distance = 0.0
results = {}

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue

    pulocation_id, trip_distance = parts
    pulocation_id = int(pulocation_id)
    trip_distance = float(trip_distance)

    if current_pulocation_id == pulocation_id:
        total_distance += trip_distance
    else:
        if current_pulocation_id is not None:
            results[current_pulocation_id] = total_distance
        current_pulocation_id = pulocation_id
        total_distance = trip_distance

if current_pulocation_id is not None:
    results[current_pulocation_id] = total_distance

for pulocation_id in sorted(results.keys()):
    print(f"{pulocation_id},{results[pulocation_id] :.2f}")
