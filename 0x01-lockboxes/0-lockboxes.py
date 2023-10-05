#!/usr/bin/env python3
"""Defines a function canUnlockAll(boxes)"""


def canUnlockAll(boxes):
    """determines if all boxes can be opened"""
    def depthFirstSearch(boxIndex, keys):
        """A key with the same number as box opens the box"""
        visited[boxIndex] = True

        for key in boxes[boxIndex]:
            if not visited[key]:
                keys.add(key)
                depthFirstSearch(key, keys)

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    keys = set()

    depthFirstSearch(0, keys)
    return all(visited)
