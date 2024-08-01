#!/usr/bin/python3
"""
This module defines a method that determines if all the boxes can be opened.
Given n number of locked boxes, each box numbered sequentially from 0 to n - 1
and assuming each box may contain keys to the other boxes
The implementation uses Depth-First Search(DFS) since it uses a stack-like keys
behavior
"""


def canUnlockAll(boxes):
    """
    method determines if all boxes can be opened
    Args:
        boxes - a list of lists
    """
    n = len(boxes)  # number of boxes
    unlck_bxs = set()  # set, keep unlocked boxes track
    """ start with first unlocked box """
    keys = [0]

    """ performing DFS to unlock all boxes """
    while keys:
        c_key = keys.pop(0)  # take a key from queue
        """ Check whether key unclocks an unlocked box """
        if c_key not in unlck_bxs:
            unlck_bxs.add(c_key)  # unlock the box
            """ Add all keys found in the unlocked box to the queue """
            for key in boxes[c_key]:
                if key < n:  # Consider valid keys only
                    keys.append(key)

    return len(unlck_bxs) == n  # check whether all boxes ara unlocked
