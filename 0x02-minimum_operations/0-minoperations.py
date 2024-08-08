#!/usr/bin/python3
"""
This module defines a method that calculates the fewest number of operations
needed to result in exactly n H characters in a text file where there is a
single character H. The text editor can execute only two operations in this
file: Copy All and Paste
"""


def minOperations(n):
    """Calculates the minimum number of operations to get n H characters.

  Args:
    n: The desired number of H characters.

  Returns:
    The minimum number of operations, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
