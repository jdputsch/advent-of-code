#! /usr/bin/env python3.12
import pathlib
import re
import sys
from typing import List, Tuple, Union


def solveit(
    eqn1: Union[List[int], Tuple[int]],
    eqn2: Union[List[int], Tuple[int]],
    offset: int = 0,
) -> Tuple[int, int]:
    """Determine x,y for two simultaneous linear equations

    Two simulataneous linear equastion of the form:

        a1x + b1y = c1 + offset
        a2x + b2y = c2 + offset

    have the solution:

            b2c1 - b1c2
        x = -----------
            b2a1 - b1a2

            c2a1 - c1a2
        y = -----------
            b2a1 - b1a2

    where

        b2a1 - b1a2 != 0

    we are not checking other failure conditions

    Args:
        eqn1 (Union[List[int],Tuple[int]]): eqn2 (Union[List[int],Tuple[int]]):

    Returns:
        List[int,int]: The solution, x,y. When no solution can be found, (-1, -1) is
            returned.

    """
    a1, b1, c1 = eqn1
    a2, b2, c2 = eqn2
    c1 = c1 + offset
    c2 = c2 + offset
    det = b2 * a1 - b1 * a2

    if det == 0:
        return (-1, -1)
    else:
        xnum = b2 * c1 - b1 * c2
        ynum = c2 * a1 - c1 * a2
        if xnum % det == 0 and ynum % det == 0:
            # integer solutions only
            x = xnum // det
            y = ynum // det
            return (x, y)
        else:
            return (-1, -1)


def main(input_file):
    # extract list of equations from input file
    games = [
        (x[0::2], x[1::2])
        for x in map(
            lambda d: list(map(int, re.findall(r"\d+", d))),
            input_file.open().read().rstrip().split("\n\n"),
        )
    ]

    # games: [((eqn1), (eqn2)), ...] where (eqnX) is of the form (x,y,c) representing
    # the linear equation ax + by = c
    total_cost = 0
    for eqn1, eqn2 in games:
        a, b = solveit(eqn1, eqn2, offset=0)
        if (a, b) != (-1, -1):
            total_cost += a * 3 + b

    print(f"Part 1: {total_cost}")

    total_cost = 0
    for eqn1, eqn2 in games:
        a, b = solveit(eqn1, eqn2, offset=10000000000000)
        if (a, b) != (-1, -1):
            total_cost += a * 3 + b
    print(f"Part 2: {total_cost}")


if __name__ == "__main__":
    try:
        if pathlib.Path(sys.argv[1]).resolve().exists():
            main(pathlib.Path(sys.argv[1]).resolve())
    except IndexError:
        main(pathlib.Path(__file__).parent / "example.in")
