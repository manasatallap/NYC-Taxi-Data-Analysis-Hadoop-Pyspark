#!/usr/bin/env python3
import sys

current_hour = None
total_distance = 0.0

for line in sys.stdin:
    line = line.strip()

    try:
        hour, distance = line.split('\t')
        hour = int(hour)
        distance = float(distance)

        if current_hour == hour:
            total_distance += distance
        else:
            if current_hour is not None:
                print(f"{current_hour},{total_distance:.2f}")
            current_hour = hour
            total_distance = distance

    except ValueError:
        print(f"Error processing line: {line}", file=sys.stderr)
        continue

if current_hour is not None:
    print(f"{current_hour},{total_distance:.2f}")
