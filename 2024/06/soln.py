#! /usr/bin/env python3

import os
import pathlib


# Direction deltas (x, y): up, right, down, left
DIRS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def patrol(obstructions, guard_location, map_height, map_width):


def main():
    os.chdir(pathlib.Path(__file__).resolve().parent)
    os.environ["PWD"] = str(pathlib.Path.cwd())

    obstructions = set()
    map_height = 0
    map_width = 0

    for row, line in enumerate(pathlib.Path("example.in").open().readlines()):
        map_height += 1
        map_width = len(line.strip())
        for col, char in enumerate(line.strip()):
            if char == "#":
                obstructions.add((row, col))
            elif char == "^":
                guard_location = (row, col)

    # part 1, walk the map, find how many locations were visisted
    visited = patrol(obstructions, guard_location, map_height, map_width)

    print("Map height:", map_height, "Map width:", map_width)
    print("Guard at:", guard_location)


if __name__ == "__main__":
    main()
