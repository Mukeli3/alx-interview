#!/usr/bin/python3
"""
This module defines a function that returns the island described in 'grid'
perimeter.
"""


def island_perimeter(grid):
    """
    """
    perimeter = 0 # track island total perimeter

    row = len(grid)
    col = len(grid[0]) # grid first row length

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1: # current cell is 1, land
                perimeter += 4
                # check for land cell directly above the currant cell
                if i > 0 and grid[i -  1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1: # to the left
                    perimeter -= 2
    return perimeter
