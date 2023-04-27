#!/usr/bin/python3
'''Solves lockbox problems'''


def canUnlockAll(boxes):
    '''
    Checks if all the boxes can be opened
    Args:
        boxes (list): A list of lists, where each positive integer in the
        list represent the keys to other boxes
    Returns:
        bool: True if all boxes can be opened or False if otherwise
    '''

    if not boxes:
        return False

    n = len(boxes)  # total number of boxes
    boxesChecked = set()  # set of boxes checked
    stackOfBoxes = [0]  # start of boxes to check

    while stackOfBoxes:
        box = stackOfBoxes.pop()  # get the next box to visit

        if box not in boxesChecked:
            boxesChecked.add(box)  # mark the box as checked

            for key in boxes[box]:  # check all keys in the box
                # if the key opens a valid box and it hasn't been checked
                if key < n:
                    # add the box to the stack of boxes to check
                    stackOfBoxes.append(key)

    # True if all boxes have been checked or False if otherwise
    return len(boxesChecked) == n
