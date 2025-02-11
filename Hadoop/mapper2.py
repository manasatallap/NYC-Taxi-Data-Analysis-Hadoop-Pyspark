#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')

    pickup_time = parts[1]
    distance = parts[4]

    if ':' in pickup_time:
        hour = pickup_time.split()[1].split(':')[0]
        print(f"{hour}\t{distance}")
    else:

        print(f"Invalid timestamp: {pickup_time}")