#! /usr/bin/env python3.12
import math
import pathlib
import re
import sys
from typing import List, Tuple, Union


def move_robots(robots, secs, nx, ny):
    new_locations = []
    for [x, y], [vx, vy] in robots:
        # adjust x location
        newx = (x + vx * secs) % nx
        newy = (y + vy * secs) % ny
        new_locations.append([newx, newy])
    return new_locations


def count_robots_in_quadrants(locations, nx, ny):
    # sort into quadrantsw with respect to midpoints [[<,<], [>,<], [<,>], [<,>]]
    counts = [0] * 4
    xmid = nx // 2
    ymid = ny // 2
    for x, y in locations:
        if x < xmid and y < ymid:
            counts[0] += 1
        elif x > xmid and y < ymid:
            counts[1] += 1
        elif x < xmid and y > ymid:
            counts[2] += 1
        elif x > xmid and y > ymid:
            counts[3] += 1
    return counts


def build_map(robots, t, nx, ny):
    location_map = [["."] * ny for x in range(nx)]
    robot_locations = move_robots(robots, t, nx, ny)
    distinct_locations = True
    for x, y in robot_locations:
        if location_map[x][y] == "*":
            distinct_locations = False
        location_map[x][y] = "*"
    if distinct_locations:
        return location_map
    else:
        return []


def main(input_file):
    # extract list of equations from input file
    robots = list(
        map(
            lambda r: list(map(list, zip(r[0::2], r[1::2]))),
            map(
                lambda line: list(map(int, re.findall(r"-?\d+", line))),
                input_file.open().readlines(),
            ),
        )
    )

    if input_file.name != "example.in":
        nx = 101
        ny = 103
    else:
        nx = 11
        ny = 7

    # Part 1: move for 100 seconds
    new_locations = move_robots(robots, 100, nx, ny)
    robots_per_quadrant = count_robots_in_quadrants(new_locations, nx, ny)
    print(f"Part 1: {math.prod(robots_per_quadrant)}")

    # Part 2: make "images" to find xmas tree easter egg...
    # Soln for me: 8053
    images_dir: pathlib.Path = input_file.parent / "images"
    images_dir.mkdir(exist_ok=True)
    for t in range(10000):
        if locations_map := build_map(robots, t, nx, ny):
            with (images_dir / f"{t}.txt").open("w") as f:
                for x in range(nx):
                    f.write("".join(locations_map[x]))
                    f.write("\n")


if __name__ == "__main__":
    try:
        if pathlib.Path(sys.argv[1]).resolve().exists():
            main(pathlib.Path(sys.argv[1]).resolve())
    except IndexError:
        main(pathlib.Path(__file__).parent / "example.in")
