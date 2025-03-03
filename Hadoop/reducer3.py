#!/usr/bin/env python3
import sys

distinct_ids = set()

# Process each line from standard input
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespace
    if line:
        distinct_ids.add(int(line))  # Add unique drop-off location ID to the set

# Output sorted unique drop-off location IDs
for DOLocationID in sorted(distinct_ids):
    print(DOLocationID)
