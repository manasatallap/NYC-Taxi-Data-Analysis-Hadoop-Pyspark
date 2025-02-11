#!/usr/bin/env python3
import sys
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

header = True

for line in sys.stdin:
    if header:
        header = False
        continue

    data = line.strip().split(',')
    if len(data) >= 8 and data[7].isdigit() and is_float(data[4]):
        pulocation_id = int(data[7])
        trip_distance = float(data[4])

        print(f"{pulocation_id}\t{trip_distance}")
