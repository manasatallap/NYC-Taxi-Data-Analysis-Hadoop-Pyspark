#!/usr/bin/env python3
import sys

for line in sys.stdin:
    data = line.strip().split(',')
    try:
        trip_distance = float(data[4])
        print(f"{trip_distance}")
    except (ValueError, IndexError):
        continue
