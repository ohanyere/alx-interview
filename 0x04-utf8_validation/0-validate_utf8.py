#!/usr/bin/python3
'''Explains if a given data set represents a valid UTF-8 encoding'''


def validUTF8(data):
    '''
    Determines if a given data set is a valid UTF-8 encoding
    Args:
        data (list): List of integers representing the data set
    Returns:
        True if data is a valid UTF-8 encoding, otherwise False
    '''

    # Counter variable to determine the number of
    # corresponding 1's in the current byte
    num_1s = 0

    for bytes in data:
        # Check for the continuability of the curent byte via bit manipulation
        byte = bytes & 255
        if num_1s:
            if byte >> 6 != 2:
                return False

            # Since its a continuation byte decrement the 1's
            num_1s -= 1
            continue
        while (1 << abs(7 - num_1s)) & byte:
            num_1s += 1

        # Checks for the 1st byte from the single-byte char t
        # the four-byte char
        if num_1s == 1 or num_1s > 4:
            return False
        num_1s = max(num_1s - 1, 0)

    # When all data set are valid encoding
    return num_1s == 0
