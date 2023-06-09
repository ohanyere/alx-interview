#!/usr/bin/python3
'''Defines the rotation of a 2D Matrix 90 degrees Clockwise'''


def rotate_2d_matrix(matrix):
    '''
    Rotates a 2D Matrix 90 degrees clockwise
    Args:
        matrix (list of lists): 2D matrix to be rotated
    Returns:
        None, since the matrix is edited in-place,
        meaning that the original matrix is modified
        directly without creating a new one which results
        in the rotated matrix being stored in the same memory
        space as the original matrix
    '''
    # Getting length of the original matrix
    matrix_len = len(matrix)

    # Transposing the original matrix
    for x in range(matrix_len):
        for y in range(x, matrix_len):

            # Swapping the rows with the corresponding columns
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    # Reversing each row
    for x in range(matrix_len):
        matrix[x] = matrix[x][::-1]
