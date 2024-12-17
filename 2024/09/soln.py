#! /usr/bin/env python3
from itertools import islice
import pathlib
import sys


def compact_1(disk_blocks):
    disk_copy = disk_blocks.copy()
    # compact the disk_blocks
    # remove trailing "." entries
    while disk_copy[-1] == ".":
        disk_copy.pop()
    while "." in disk_copy:
        disk_copy[disk_copy.index(".")] = disk_copy.pop()
        while disk_copy[-1] == ".":
            disk_copy.pop()

    return disk_copy


def main(input_file):
    disk_map = input_file.open().read().strip()
    disk_blocks = []
    id_no = 0
    map_iterator = iter(disk_map)
    while pair := list(islice(map_iterator, 2)):
        if len(pair) == 1:
            pair.append(0)
        blocks, free = map(int, pair)
        for i in range(0, blocks):
            disk_blocks.append(id_no)
        for i in range(0, free):
            disk_blocks.append(".")
        id_no += 1

    compacted_disk = compact_1(disk_blocks)
    part1_soln = sum(
        [x * i for x, i in zip(compacted_disk, range(len(compacted_disk)))]
    )

    print(f"Part 1: {part1_soln}")


if __name__ == "__main__":
    try:
        if pathlib.Path(sys.argv[1]).resolve().exists():
            main(pathlib.Path(sys.argv[1]).resolve())
    except IndexError:
        main(pathlib.Path(__file__).parent / "example.in")
