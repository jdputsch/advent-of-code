#! /usr/bin/env python

import pathlib

with pathlib.Path("1.in").open() as f:
    col1, col2 = map(sorted, zip(*[map(int, line.split()) for line in f.readlines()]))

print("Part 1: ", sum([abs(a - b) for a, b in zip(col1, col2)]))
print("Part 2: ", sum([c * col2.count(c) for c in col1]))
