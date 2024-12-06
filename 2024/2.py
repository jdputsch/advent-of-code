#! /usr/bin/env python3

import pathlib
import sys

def is_safe(record: list):
    deltas = [earlier - later for earlier, later in zip(l, l[1:])]
    mn = min(deltas)
    mx = max(deltas)
    return mn > 0 and mx <= 3 or mx < 0 and mn >= -3
    

with pathlib.Path(sys.argv[1]).open() as f:
    safe = 0
    for line in f.readlines():
        l = list(map(int, line.strip().split()))
        if is_safe(l):
             safe += 1
print(safe)
