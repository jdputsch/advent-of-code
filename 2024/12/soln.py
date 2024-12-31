#! /usr/bin/env python3.12
import pathlib
import sys
from typing import Any, List


def map_fill(map: List[List[str]]) -> List[List[Any]]:
    """find all the plant groups using flood fill and get key infor about them.

    Args:
        map (List[List[str]]): The input map of the plant garden

    Returns:
        List[List[str, int, int, int]]: List of plant types with key information:
           [[plant_type, area, perimeter, num_corners]]
    """
    plant_groups = []
    xmax = len(map)
    ymax = len(map[0])
    visited = [[False for y in range(ymax)] for x in range(xmax)]
    visited_check = [["N" for y in range(ymax)] for x in range(xmax)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    corners = [
        [(-1, 0), (0, 1)],  # |^
        [(0, 1), (1, 0)],  # ^|
        [(1, 0), (0, -1)],  # |_
        [(0, -1), (-1, 0)],  # _|
    ]
    for i in range(xmax):
        for j in range(ymax):
            if visited[i][j]:
                continue
            plant_type = map[i][j]
            group_info = [
                plant_type,
                0,
                0,
                0,
            ]  # [plant_type, area, perimeter, num_corners]
            queue = [(i, j)]

            # flood fill for plant_type
            while queue:
                (x, y) = queue.pop()
                visited[x][y] = True
                visited_check[x][y] = "."
                group_info[1] += 1  # Increase area

                # check all four directions for
                for dx, dy in dirs:
                    newx, newy = x + dx, y + dy
                    if (
                        0 <= newx < xmax
                        and 0 <= newy < ymax
                        and map[newx][newy] == plant_type
                    ):
                        if (newx, newy) not in queue and not visited[newx][newy]:
                            queue.append((newx, newy))
                    else:
                        group_info[2] += 1  # edge found, increase permiter

                # Count corners
                for (dx1, dy1), (dx2, dy2) in corners:
                    newx1, newy1 = x + dx1, y + dy1
                    newx2, newy2 = x + dx2, y + dy2

                    # outside corner
                    if (
                        newx1 < 0
                        or newx1 >= xmax
                        or newy1 < 0
                        or newy1 >= ymax
                        or map[newx1][newy1] != plant_type
                    ) and (
                        newx2 < 0
                        or newx2 >= xmax
                        or newy2 < 0
                        or newy2 >= ymax
                        or map[newx2][newy2] != plant_type
                    ):
                        group_info[3] += 1  # + corner count

                    # inside corner
                    elif (
                        0 <= newx1 < xmax
                        and 0 <= newy1 < ymax
                        and map[newx1][newy1] == plant_type
                    ) and (
                        0 <= newx2 < xmax
                        and 0 <= newy2 < ymax
                        and map[newx2][newy2] == plant_type
                    ):
                        if map[x + dx1 + dx2][y + dy1 + dy2] != plant_type:
                            group_info[3] += 1  # + corner count
            plant_groups.append(group_info)
    # for row in visited_check:
    #     print("".join(row))
    for x in range(xmax):
        for y in range(ymax):
            if visited_check[x][y] == "N":
                print(f"Unvisited: ({x},{y})")

    return plant_groups


def part1_cost(groups: List[List[Any]]) -> int:
    """Calculate total cost for part 1

    For each plant group in `groups` multiply area and perimter to get the cost.
    Return the sum of all the group costs.

    Args:
        groups (List[List[Any]]): List of plant group information, each entry information
            about a plant group and has the following form:
            [plant_type, area, perimeter, num_corners]

    Returns:
        int: the total cost
    """
    total_cost = 0
    for group in groups:
        total_cost += group[1] * group[2]
    return total_cost


def part2_cost(groups: List[List[Any]]) -> int:
    """Calculate total cost for part 2

    For each plant group in `groups` multiply area and # sides (corners) to get the cost.
    Return the sum of all the group costs.

    Args:
        groups (List[List[Any]]): List of plant group information, each entry information
            about a plant group and has the following form:
            [plant_type, area, perimeter, num_corners]

    Returns:
        int: the total cost
    """
    total_cost = 0
    for group in groups:
        total_cost += group[1] * group[3]
    return total_cost


def main(input_file):
    map = [list(line.strip()) for line in input_file.open().readlines()]

    groups = map_fill(map)

    print(f"Part 1: {part1_cost(groups)}")
    print(f"Part 2: {part2_cost(groups)}")


if __name__ == "__main__":
    try:
        if pathlib.Path(sys.argv[1]).resolve().exists():
            main(pathlib.Path(sys.argv[1]).resolve())
    except IndexError:
        main(pathlib.Path(__file__).parent / "example.in")
