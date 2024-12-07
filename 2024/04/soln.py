#! /usr/bin/env python3

import pathlib
import re
import sys

PART1_SEARCHES = [
    # row offset, col offset, letter
    [(0, 0, "X"), (0, 1, "M"), (0, 2, "A"), (0, 3, "S")],  # horiz right
    [(0, 0, "X"), (0, -1, "M"), (0, -2, "A"), (0, -3, "S")],  # horiz left
    [(0, 0, "X"), (-1, 0, "M"), (-2, -0, "A"), (-3, 0, "S")],  # up
    [(0, 0, "X"), (1, 0, "M"), (2, 0, "A"), (3, 0, "S")],  # down
    [(0, 0, "X"), (1, 1, "M"), (2, 2, "A"), (3, 3, "S")],  # Diag D-R
    [(0, 0, "X"), (-1, 1, "M"), (-2, 2, "A"), (-3, 3, "S")],  # Diag U-R
    [(0, 0, "X"), (-1, -1, "M"), (-2, -2, "A"), (-3, -3, "S")],  # Diag U-L
    [(0, 0, "X"), (1, -1, "M"), (2, -2, "A"), (3, -3, "S")],  # Diag D-L
]

PART2_SEARCHES = [
    [(0, 0, "A"), (-1, -1, "M"), (-1, 1, "M"), (1, 1, "S"), (1, -1, "S")],
    [(0, 0, "A"), (-1, -1, "S"), (-1, 1, "M"), (1, 1, "M"), (1, -1, "S")],
    [(0, 0, "A"), (-1, -1, "S"), (-1, 1, "S"), (1, 1, "M"), (1, -1, "M")],
    [(0, 0, "A"), (-1, -1, "M"), (-1, 1, "S"), (1, 1, "S"), (1, -1, "M")],
]


def debug_search(puzzle, row, col, search_matrix):
    for x, y, letter in search_matrix:
        print(puzzle[row + y][col + x])


def search_data(row, col, data, search_sets):
    """search the data around an origin located a row, col"""
    count = 0
    for search_set in search_sets:
        try:
            for r, c, letter in search_set:
                new_row = row + r
                new_col = col + c
                if new_row < 0 or new_col < 0:
                    raise IndexError
                if data[new_row][new_col] != letter:
                    raise ValueError
            count += 1
        except (IndexError, ValueError):
            continue
    return count


try:
    the_file = sys.argv[1]
except IndexError:
    the_file = "example.in"

with pathlib.Path(the_file).open() as f:
    puzzle = [list(line.strip()) for line in f]

    total_count_1 = 0
    total_count_2 = 0
    for r, row in enumerate(puzzle):
        for c in range(len(row)):
            total_count_1 += search_data(r, c, puzzle, PART1_SEARCHES)
            total_count_2 += search_data(r, c, puzzle, PART2_SEARCHES)
print(f"Part 1: {total_count_1}")
print(f"Part 2: {total_count_2}")
