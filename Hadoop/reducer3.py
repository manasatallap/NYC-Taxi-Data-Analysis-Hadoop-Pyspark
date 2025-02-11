#!/usr/bin/env python3
import sys

distinct_ids = set()

for line in sys.stdin:
    line = line.strip()
    if line:
        distinct_ids.add(int(line))

for DOLocationID in sorted(distinct_ids):
    print(DOLocationID)
