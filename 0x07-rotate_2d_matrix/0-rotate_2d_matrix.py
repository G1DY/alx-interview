#!/usr/bin/python3
"""Rotates a matrix"""


def rotate_2d_matrix(matrix):
    """functionto rotate a 2*2 matrix 90 clockwise"""
    _matrix = matrix[:]

    for i in range(len(matrix)):
        column = [row[i] for row in _matrix]
        matrix[i] = column[::-1]
