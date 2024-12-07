#! /usr/bin/python3

import pathlib
import re
import sys

GOOD_INSTRUCTION_RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

with pathlib.Path(sys.argv[1]).open() as f:
    total = 0
    for line in f.readlines():
        # find all mul(N,M) in the line and get the answers...
        for match in re.findall(GOOD_INSTRUCTION_RE, line):
            total += int(match[0]) * int(match[1])
print(total)
