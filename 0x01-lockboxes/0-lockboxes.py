#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened
    """
    all_boxes = len(boxes)
    set_keys = [0]
    count = 0
    idx = 0

    while idx < len(set_keys):
        new_key = set_keys[idx]
        for key in boxes[new_key]:
            if 0 < key < all_boxes and key not in set_keys:
                set_keys.append(key)
                count += 1
        idx += 1

    return count == all_boxes - 1
