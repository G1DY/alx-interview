#!/usr/bin/python3
"""Defines a function canUnlockAll(boxes)"""


def canUnlockAll(boxes):
    """determines if all boxes can be opened"""
    num_boxes = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < num_boxes:
        prev_i = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < num_boxes and key not in opened_boxes:
                i = key
                break
        if prev_i != i:
            continue
        else:
            break

    for i in range(num_boxes):
        if i not in opened_boxes and i != 0:
            return False

    return True
