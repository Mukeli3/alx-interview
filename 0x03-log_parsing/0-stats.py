#!/usr/bin/python3
"""
"""
import sys


def print_stats(fsize, counts):
    """ """
    print(f"File size: {fsize}")
    for code in sorted(counts.keys()):
        if counts[code] > 0:
            print(f"{code}: {counts[code]}")

total_fsize = 0
counts = {200: 0, 301: 0, 400: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lcount = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            fsize = int(parts[-1])
            scode = int(parts[-2])
            total_fsize += fsize

            if scode in counts:
                counts[scode] += 1

        except(IndexError, ValueError):
            continue
        lcount += 1

        if lcount % 10 == 0:
            print_stats(total_fsize, counts)

except KeyboardInterrupt:
    print_stats(total_fsize, counts)
    raise

print_stats(total_fsize, counts)
