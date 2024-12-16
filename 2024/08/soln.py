#! /usr/bin/env python3

from collections import defaultdict
import pathlib
import sys


def find_antinodes(antennas, maxx, maxy):
    antinodes = defaultdict(list)
    for antenna_id, locations in antennas.items():
        for location in locations:
            locations_copy = locations.copy()
            locations_copy.remove(location)
            for other in locations_copy:
                antinode_1 = tuple(2 * x - y for x, y in zip(location, other))
                antinode_2 = tuple(2 * y - x for x, y in zip(location, other))
                if (
                    max(antinode_1) <= maxx
                    and max(antinode_1) <= maxy
                    and min(antinode_1) >= 0
                ):
                    antinodes[antinode_1].append(antenna_id)
                if (
                    max(antinode_2) <= maxx
                    and max(antinode_2) <= maxy
                    and min(antinode_2) >= 0
                ):
                    antinodes[antinode_2].append(antenna_id)
    return antinodes


def part2_antinodes(antennas, maxx, maxy):
    antinodes = defaultdict(list)
    for antenna_id, locations in antennas.items():
        for location in locations:
            locations_copy = locations.copy()
            locations_copy.remove(location)
            for other in locations_copy:
                n = 0
                while True:
                    antinode_1_good = False
                    antinode_2_good = False
                    n += 1
                    antinode_1 = tuple(
                        n * x - (n - 1) * y for x, y in zip(location, other)
                    )
                    antinode_2 = tuple(
                        n * y - (n - 1) * x for x, y in zip(location, other)
                    )
                    if (
                        max(antinode_1) <= maxx
                        and max(antinode_1) <= maxy
                        and min(antinode_1) >= 0
                    ):
                        antinodes[antinode_1].append(antenna_id)
                        antinode_1_good = True
                    if (
                        max(antinode_2) <= maxx
                        and max(antinode_2) <= maxy
                        and min(antinode_2) >= 0
                    ):
                        antinodes[antinode_2].append(antenna_id)
                        antinode_2_good = True
                    if not (antinode_1_good or antinode_2_good):
                        break
    return antinodes


def main(input_file: pathlib.Path):
    input_lines = [line.strip() for line in input_file.open().readlines()]

    # antennas[symbol] = set((x,y))
    antennas = defaultdict(set)
    maxy = 0
    maxx = 0
    for y, line in enumerate(input_lines):
        for x, char in enumerate(line):
            if char.isalnum():
                antennas[char].add((x, y))
            maxx = max(x, maxx)
        maxy = y

    antinodes = find_antinodes(antennas, maxx, maxy)

    print(f"Part 1: {len(antinodes)}")

    antinodes_2 = part2_antinodes(antennas, maxx, maxy)

    print(f"Part 2: {len(antinodes_2)}")


if __name__ == "__main__":
    try:
        if pathlib.Path(sys.argv[1]).resolve().exists():
            main(pathlib.Path(sys.argv[1]).resolve())
    except IndexError:
        main(pathlib.Path(__file__).parent / "example.in")
