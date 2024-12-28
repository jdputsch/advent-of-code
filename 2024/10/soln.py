#! /usr/bin/env python3.12
from collections import deque
import pathlib
import sys
from typing import List


def score_trailheads(topo_map, trailhead):
    xmax = len(topo_map)
    ymax = len(topo_map[0])
    endpoints = set()
    next_position = [trailhead]
    while next_position:
        x, y = next_position.pop()
        if topo_map[x][y] == 9:
            endpoints.add((x, y))
            continue
        # west
        if x > 0 and topo_map[x - 1][y] == (topo_map[x][y] + 1):
            next_position.append([x - 1, y])
        # east
        if x < xmax - 1 and topo_map[x + 1][y] == (topo_map[x][y] + 1):
            next_position.append([x + 1, y])
        # north
        if y < ymax - 1 and topo_map[x][y + 1] == (topo_map[x][y] + 1):
            next_position.append([x, y + 1])
        # south
        if y > 0 and topo_map[x][y - 1] == (topo_map[x][y] + 1):
            next_position.append([x, y - 1])

    return len(endpoints)


def rate_trailheads(topo_map, trailhead):
    xmax = len(topo_map)
    ymax = len(topo_map[0])
    endpoints = []
    next_position = [trailhead]
    while next_position:
        x, y = next_position.pop()
        if topo_map[x][y] == 9:
            endpoints.append((x, y))
            continue
        # west
        if x > 0 and topo_map[x - 1][y] == (topo_map[x][y] + 1):
            next_position.append([x - 1, y])
        # east
        if x < xmax - 1 and topo_map[x + 1][y] == (topo_map[x][y] + 1):
            next_position.append([x + 1, y])
        # north
        if y < ymax - 1 and topo_map[x][y + 1] == (topo_map[x][y] + 1):
            next_position.append([x, y + 1])
        # south
        if y > 0 and topo_map[x][y - 1] == (topo_map[x][y] + 1):
            next_position.append([x, y - 1])

    return len(endpoints)


def main(input_file):
    topo_map = [list(map(int, line.strip())) for line in input_file.open().readlines()]
    trailhead_locations = [
        [x, y]
        for x in range(len(topo_map))
        for y in range(len(topo_map[0]))
        if topo_map[x][y] == 0
    ]
    total_score = 0
    for trailhead in trailhead_locations:
        total_score += score_trailheads(topo_map, trailhead)

    print(f"Part 1: {total_score}")
    total_score = 0
    for trailhead in trailhead_locations:
        total_score += rate_trailheads(topo_map, trailhead)
    print(f"Part 2: {total_score}")


if __name__ == "__main__":
    try:
        if pathlib.Path(sys.argv[1]).resolve().exists():
            main(pathlib.Path(sys.argv[1]).resolve())
    except IndexError:
        main(pathlib.Path(__file__).parent / "example.in")
