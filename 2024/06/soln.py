#! /usr/bin/env python3

import os
import pathlib


# Direction deltas (x, y)
DIRS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def patrol(obstructions, location, map_height, map_width):
    # Keep track of moves as a set of tuples of (pos, direction)
    moves = set()
    # current direction:
    direction = 0
    position = (location, DIRS[direction])
    # Loop until we get back to the same position (location & direction)
    loop = True
    while position not in moves:
        moves.add(position)
        curr_location = position[0]

        new_location = tuple(map(sum, zip(*position)))
        if (new_location[0] < 0 or new_location[0] >= map_width) or (
            new_location[1] < 0 or new_location[1] >= map_height
        ):
            # hit the edge, no loop
            loop = False
        elif new_location in obstructions:
            # hit an obstruction, don't move, but do rotate
            direction = (direction + 1) % len(DIRS)
            position = (curr_location, DIRS[direction])
        else:
            # move ...
            position = (new_location, DIRS[direction])

    # get the spaces we visited...
    visited = set([v for v, _ in moves])
    return loop, visited


def main():
    os.chdir(pathlib.Path(__file__).resolve().parent)
    os.environ["PWD"] = str(pathlib.Path.cwd())

    obstructions = set()
    map_height = 0
    map_width = 0

    for row, line in enumerate(pathlib.Path("6.in").open().readlines()):
        map_height += 1
        map_width = len(line.strip())
        for col, char in enumerate(line.strip()):
            if char == "#":
                obstructions.add((col, row))
            elif char == "^":
                guard_location = (col, row)

    # part 1, walk the map, find how many locations were visisted
    _, visited = patrol(obstructions, guard_location, map_height, map_width)

    print("Part 1:", len(visited))

    # try an obstacle at all the places we visited in part 1, see if a loop forms
    num_loops = 0
    for loc in visited:
        new_obstructions = obstructions.copy()
        new_obstructions.add(loc)
        loop, _ = patrol(new_obstructions, guard_location, map_height, map_width)
        if loop:
            num_loops += 1

    print("Part 2", num_loops)


if __name__ == "__main__":
    main()
