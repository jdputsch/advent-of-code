#! /usr/bin/python3

import pathlib
import re
import sys

GOOD_INSTRUCTION_RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|((?:do|don't)\(\))")

with pathlib.Path(sys.argv[1]).open() as f:
    total = 0
    doing = True
    for line in f.readlines():
        # find all mul(N,M) in the line and get the answers...
        for n, m, doit in re.findall(GOOD_INSTRUCTION_RE, line):
            if doit:
                if doit == "don't()":
                    doing = False
                else:
                    doing = True
                continue
            if doing:
                total += int(n) * int(m)
print(total)
