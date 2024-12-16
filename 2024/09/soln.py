#! /usr/bin/env python3
from itertools import islice
import pathlib
import sys


def main(input_file):
    disk_map = input_file.open().read().strip()
    id_no = 0
    map_iterator = iter(disk_map)
    while pair := tuple(islice(map_iterator, 2)):
        if len(pair) > 1:
            blocks, free = pair
        else:
            blocks = pair[0]
            free = 0
        print(id_no, blocks, free)
        id_no += 1


if __name__ == "__main__":
    try:
        if pathlib.Path(sys.argv[1]).resolve().exists():
            main(pathlib.Path(sys.argv[1]).resolve())
    except IndexError:
        main(pathlib.Path(__file__).parent / "example.in")
