#!/usr/bin/env python3
import sys

for line in sys.stdin:

    line = line.strip()
    if "DOLocationID" in line:
        continue

    parts = line.split(',')
    DOLocationID = parts[8]

    print(DOLocationID)
