#! /usr/bin/env python3

import pathlib
import sys


def is_safe(record: list):
    deltas = [earlier - later for earlier, later in zip(record, record[1:])]
    mn = min(deltas)
    mx = max(deltas)
    return mn > 0 and mx <= 3 or mx < 0 and mn >= -3


with pathlib.Path(sys.argv[1]).open() as f:
    safe = 0
    for line in f.readlines():
        levels = list(map(int, line.strip().split()))
        if is_safe(levels):
            safe += 1
            continue
        # need to try removing one level to see if it becomes safe
        for i in range(len(levels)):
            levels_copy = levels.copy()
            levels_copy.pop(i)
            if is_safe(levels_copy):
                safe += 1
                break
print(safe)
