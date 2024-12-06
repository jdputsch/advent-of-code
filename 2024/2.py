#! /usr/bin/env python

import pathlib
import sys


with pathlib.Path(sys.argv[1]).open() as f:
    safe = 0
    for line in f.readlines():
        l = list(map(int, line.strip().split()))
        if all(
            earlier > later and abs(earlier - later) <= 3
            for earlier, later in zip(l, l[1:])
        ) or all(
            earlier < later and abs(earlier - later) <= 3
            for earlier, later in zip(l, l[1:])
        ):
            safe += 1
print(safe)
