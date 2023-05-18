#!/usr/bin/python3
'''Explains if a given data set represents a valid UTF-8 encoding'''


def validUTF8(data):
    '''
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers representing the
        bytes of the data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    '''
    # Loop through the data one byte at a time.
    i = 0
    while i < len(data):
        # Check whether the current byte is the start of a character.
        byte = data[i]
        if byte & 0x80 == 0x00:  # Single-byte character
            i += 1
        elif byte & 0xE0 == 0xC0:  # Two-byte character
            if i + 1 >= len(data) or data[i + 1] & 0xC0 != 0x80:
                return False
            i += 2
        elif byte & 0xF0 == 0xE0:  # Three-byte character
            if i + 2 >= len(data) or data[i + 1] & 0xC0 != 0x80 or
            data[i + 2] & 0xC0 != 0x80:
                return False
            i += 3
        elif byte & 0xF8 == 0xF0:  # Four-byte character
            if i + 3 >= len(data) or data[i + 1] & 0xC0 != 0x80 or
            data[i + 2] & 0xC0 != 0x80 or data[i + 3] & 0xC0 != 0x80:
                return False
            i += 4
        else:  # Invalid byte
            return False

    return True
