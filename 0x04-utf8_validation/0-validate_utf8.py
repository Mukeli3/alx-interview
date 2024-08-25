#!/usr/bin/python3
"""
This module defines a method that determines if a given data set represents a
valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Method determines if a given data set represents a valid UTF-8 encoding

    Args:
        data (int list): A list of ints, each reps 1 byte

    Returns:
        bool: True if data is a valid UTF-8 encoding, else false
    """
    n = 0  # current UTF-8 character bytes number

    # masks, check leading buts
    f_mask = 1 << 7
    s_mask = 1 << 6

    for num in data:
        byte = num & 0xFF
        if n == 0:
            if (byte & f_mask) == 0:  # determine UTF-8 character bytes number
                continue  # 1-byte character
            elif (byte & (f_mask >> 1)) == f_mask:  # invalid byte
                return False
            elif (byte & (f_mask >> 2)) == (f_mask >> 1):
                n = 1  # 2-byte character
            elif (byte & (f_mask >> 3)) == (f_mask >> 2):
                n = 2  # 3-byte character
            elif (byte & (f_mask >> 4)) == (f_mask >> 3):
                n = 3  # 4-byte character
            else:
                return False
        else:
            if ((byte & f_mask) != f_mask and (byte & s_mask)) != 0:
                return False
            n -= 1
    return n == 0
