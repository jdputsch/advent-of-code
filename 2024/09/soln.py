#! /usr/bin/env python3
from collections import defaultdict
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


def fat_map_to_str(fat_map):
    files = sorted(fat_map.items(), key=lambda item: item[1][0])
    disk_blocks = ["."] * sum(files[-1][1])
    for file in files:
        disk_blocks[file[1][0] : file[1][1]] = [str(file[0])] * file[1][1]
    return "".join(disk_blocks)


def compact_2(fat_map, free_map):
    for file_id in reversed(sorted(fat_map)):
        file_index, file_len = fat_map[file_id]
        if file_index == 0:
            continue
        # Find smallest index in free_map >= file_len, then
        # find smallest starting index in the set of indices that are free
        for fmi, (free_index, free_blocks) in enumerate(free_map):
            if free_index < file_index and free_blocks >= file_len:
                break
        else:
            continue
        fat_map[file_id] = [free_index, file_len]
        if free_blocks - file_len >= 0:
            # Adjust free space at destination
            free_map[fmi] = [free_index + file_len, free_blocks - file_len]
            # if adjusted entry has no space, remove it:
            if not free_map[fmi][1]:
                del free_map[fmi]
            # Adjust free map for new free space
            # Find insert point for new free space
            for idx in range(len(free_map)):
                if idx == 0 and file_index < free_map[idx + 1][0]:
                    # beginning of list
                    free_map.insert(idx, [file_index, file_len])
                    # merge with entry on right:
                    if (file_index + file_len) == free_map[idx + 1][0]:
                        free_map[idx][1] += free_map[idx + 1][1]
                        del free_map[idx + 1]
                    break
                elif idx == len(free_map) - 1:
                    # end of list
                    if file_index == free_map[idx][0] + free_map[idx][1]:
                        # merge with entry to left
                        free_map[idx][1] += file_len
                    else:
                        # append to list
                        free_map.append([file_index, file_len])
                    break
                elif (
                    free_map[idx - 1][0] < file_index and file_index < free_map[idx][0]
                ):
                    free_map.insert(idx, [file_index, file_len])
                    # merge with entry on right:
                    if (file_index + file_len) == free_map[idx + 1][0]:
                        free_map[idx][1] += free_map[idx + 1][1]
                        del free_map[idx + 1]
                    # merge with entry on the left:
                    if file_index == (free_map[idx - 1][0] + free_map[idx - 1][1]):
                        free_map[idx - 1][1] += free_map[idx][1]
                        del free_map[idx]
                    break
    return fat_map, free_map


def main(input_file):
    disk_map = input_file.open().read().strip()
    free_map = []  # [[start/index, size] ...]
    alloc_map = []  # [[start, size], ...]
    disk_blocks = []
    fat_map = {}
    id_no = 0
    idx = 0
    map_iterator = iter(disk_map)
    while pair := list(islice(map_iterator, 2)):
        if len(pair) == 1:
            pair.append(0)
        blocks, free = map(int, pair)
        alloc_map.append([len(disk_blocks), blocks])
        fat_map[id_no] = [idx, blocks]
        idx += blocks
        for i in range(0, blocks):
            disk_blocks.append(id_no)
        if free:
            free_map.append([idx, free])
        idx += free
        for i in range(0, free):
            disk_blocks.append(".")
        id_no += 1

    free_map = sorted(free_map)

    compacted_disk = compact_1(disk_blocks)
    part1_soln = sum(
        [x * i for x, i in zip(compacted_disk, range(len(compacted_disk)))]
    )

    print(f"Part 1: {part1_soln}")

    compact_2(fat_map, free_map)

    part2_soln = sum(
        [
            file_id * (file_idx + i)
            for file_id, (file_idx, file_len) in sorted(
                fat_map.items(), key=lambda item: item[1]
            )
            for i in range(file_len)
        ]
    )
    print(f"Part 2: {part2_soln}")


if __name__ == "__main__":
    try:
        if pathlib.Path(sys.argv[1]).resolve().exists():
            main(pathlib.Path(sys.argv[1]).resolve())
    except IndexError:
        main(pathlib.Path(__file__).parent / "example.in")
