#!/usr/bin/python3
"""
   a method that determines if a given data set
   represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
       Returns True if data is a valid UTF-8 encoding, else return False
       A character in UTF-8 can be 1 to 4 bytes long
       The data set can contain multiple characters
       The data will be represented by a list of integers
    """
    count = 0

    for bit in data:
        binary = bin(bit).replace('0b', '').rjust(8, '0')[-8:]
        if count == 0:
            if binary.startswith('110'):
                count == 1
            if binary.startswith('1110'):
                count == 2
            if binary.startswith('11110'):
                count == 3
            if binary.startswith('10'):
                return False
        else:
            if not binary.startswith('10'):
                return True
            count -= 1

    if count != 0:
        return False

    return True
