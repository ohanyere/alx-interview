#!/usr/bin/python3
'''Creates Pascal’s triangle of n'''


def pascal_triangle(n):
    '''
    Returns a list of lists of integers representing the
    Pascal’s triangle of n
    '''
    # If n is negative or zero, return an empty list
    if n <= 0:
        return []

    # Create an empty list to store the triangle
    triangle = []

    # Generate each row of the triangle
    for x in range(n):
        row = [1] * (x + 1)
        if x > 1:
            for y in range(1, x):
                row[y] = triangle[x - 1][y - 1] + triangle[x - 1][y]
        triangle.append(row)

    return triangle

