#! /usr/bin/env python

from collections import defaultdict
import fileinput


def read_input():
    # -> Tuple[Dict[str, Dict[str, List[str]]], List[List[str]]]:
    """read input file, returning a lookuptable and a list of updates

    Returns:
        Tuple[Dict[str, Dict[str, List[str]]], List[List[str]]]:
            (lookup_table, updates), where
            lookup_table["before"][X] = [a , b, c] means that a, b, and c must come
                                                   before X
            lookup_table["after"][X] = [a , b, c] means that a, b, and c must come
                                                  after X
    """
    lookup_table = {"before": defaultdict(list), "after": defaultdict(list)}
    updates = []
    for line in fileinput.input(encoding="utf-8"):
        if "|" in line:
            a, b = line.strip().split("|")
            lookup_table["before"][b].append(a)
            lookup_table["after"][a].append(b)
        elif "," in line:
            updates.append(line.strip().split(","))
    return lookup_table, updates


def is_valid(
    lookup_table,  #: Dict[str, Dict[str, List[str]]], updates: List[List[str]]
    updates,
) -> bool:
    for i, page in enumerate(updates):
        # Find pages before this that must come after it
        if page in lookup_table["after"]:
            if (
                sum(
                    [
                        1
                        for entry in updates[:i]  # pages in update before this page
                        if entry
                        in lookup_table["after"][page]  # required to come after
                    ]
                )
                > 0
            ):
                return False
        # Find pages after this that must come before it
        if page in lookup_table["after"]:
            if (
                sum(
                    [
                        1
                        for entry in updates[i + 1 :]  # pages in update after this page
                        if entry
                        in lookup_table["before"][page]  # required to come before
                    ]
                )
                > 0
            ):
                return False

    return True


def reorder(lookup_table, update):
    new_update = []
    # repeat until we've placed every item into the correct position
    while update:
        # find the first item that can be placed, check "other" items to make
        # sure none of them are required to come before it
        for i, page in enumerate(update):
            others = update.copy()
            others.pop(i)  # remouve the current page from others
            out_of_order = 0
            # check for others that need to be before us
            if page in lookup_table["before"]:
                out_of_order += sum(
                    [1 for entry in others if entry in lookup_table["before"][page]]
                )
            # check for others that need to be after us
            for o in others:
                if o in lookup_table["after"] and page in lookup_table["after"][o]:
                    out_of_order += 1
                    break
            # no out of order pages, so stop searching
            if out_of_order == 0:
                break
        update.pop(i)  # remove the page from the update list, becase we've palced it
        new_update.append(page)  # add the page to the new update list
    return new_update


def main():
    lookup_table, updates = read_input()
    result_1 = 0
    result_2 = 0
    for i, update in enumerate(updates):
        if is_valid(lookup_table, update):
            result_1 += int(update[len(update) // 2])
        else:
            corrected_update = reorder(lookup_table, update)
            result_2 += int(corrected_update[len(corrected_update) // 2])
    print("Part 1: ", result_1)
    print("Part 2: ", result_2)


if __name__ == "__main__":
    main()
