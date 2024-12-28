#! /usr/bin/env python3.12
from collections import defaultdict
import pathlib
import sys
from typing import Dict

EVOLVE_CONST = 2024


def update(stones: Dict[int, int]) -> Dict[int, int]:
    updated_stones = defaultdict(int)
    for stone, count in stones.items():
        str_stone = str(stone)
        if stone == 0:
            updated_stones[1] += count
        elif len(str_stone) % 2 == 0:
            l_stone = list(str_stone)
            mid = len(l_stone) // 2
            head = int("".join(l_stone[:mid]))
            tail = int("".join(l_stone[mid:]))
            updated_stones[head] += count
            updated_stones[tail] += count
        else:
            updated_stones[stone * EVOLVE_CONST] += count
    return updated_stones


def evolve_stones(stones: Dict[int, int], blinks: int) -> Dict[int, int]:
    tmp_stones = stones.copy()
    for i in range(blinks):
        tmp_stones = update(tmp_stones)
    return tmp_stones


def main(input_file):
    stones = {int(x): 1 for x in input_file.open().readline().split()}

    result = evolve_stones(stones, 25)
    print(f"Part 1: {sum(result.values())}")

    result = evolve_stones(stones, 75)
    print(f"Part 2: {sum(result.values())}")


if __name__ == "__main__":
    try:
        if pathlib.Path(sys.argv[1]).resolve().exists():
            main(pathlib.Path(sys.argv[1]).resolve())
    except IndexError:
        main(pathlib.Path(__file__).parent / "example.in")
