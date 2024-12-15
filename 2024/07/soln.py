#! /usr/bin/env python3

from itertools import product
import pathlib
import sys


# Operators for Part 1
def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def concat(a, b):
    return int(str(a) + str(b))


PART1_OPERATORS = {add, mul}
PART2_OPERATORS = {add, mul, concat}


def can_solve(target_value, input_values, operator_orders):
    for operator_order in operator_orders:
        values = input_values.copy()
        total = values.pop(0)
        for i, operator in enumerate(operator_order):
            total = operator(total, values.pop(0))
        if total == target_value:
            return True
    return False


def main(input_file):
    sum = 0
    input_lines = [line.strip() for line in input_file.open().readlines()]

    for line in input_lines:
        target_value = int(line.split(":")[0])
        input_values = list(map(int, line.split(":")[1].split()))

        operator_orders = product(PART1_OPERATORS, repeat=len(input_values) - 1)
        if can_solve(target_value, input_values, operator_orders):
            sum += target_value

    print("Part 1:", sum)

    sum = 0
    for line in input_lines:
        target_value = int(line.split(":")[0])
        input_values = list(map(int, line.split(":")[1].split()))

        operator_orders = product(PART2_OPERATORS, repeat=len(input_values) - 1)
        if can_solve(target_value, input_values, operator_orders):
            sum += target_value

    print("Part 2:", sum)


if __name__ == "__main__":
    try:
        if pathlib.Path(sys.argv[1]).resolve().exists():
            main(pathlib.Path(sys.argv[1]).resolve())
    except IndexError:
        main(pathlib.Path(__file__).parent / "example.in")
