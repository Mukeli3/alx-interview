#!/usr/bin/python3
"""
This module provides a function that generates the Pascal's Triangle
Pascal's Triangle is n arrangement of binomial coefficients in triangular form
The time complexity of the triangle's algorithm is O(n2)
"""


def pascal_triangle(n):
    """
    function returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    """ initialize the first triangle row """
    tri = [[1]]

    for i in range(1, n):
        """ start each row with 1 """
        row = [1]
        for j in range(1, i):
            """ each row is the sum of the two elements above it """
            row.append(tri[i - 1][j - 1] + tri[i - 1][j])

        """ end each row with 1 """
        row.append(1)
        tri.append(row)

    return tri
