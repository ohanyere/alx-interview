#!/usr/bin/python3
'''Calculates the perimeter of the island described in the grid'''


def island_perimeter(grid):
    '''
    Returns the perimeter of the island described in the grid
    Args:
        grid (list of list): A list of lists representing the grid
    Returns:
        The perimeter of the island
    Raises:
        ValueError: If the grid is empty or not rectangular
    '''
    if not grid or not grid[0]:
        raise ValueError("Grid is empty.")

    rows = len(grid)
    columns = len(grid[0])

    # Calculate the perimeter
    perimeter = 0

    for n in range(rows):
        for m in range(columns):
            if grid[n][m] == 1:
                perimeter += 4  # Start with 4 sides

                # Check left cell
                if m > 0 and grid[n][m - 1] == 1:
                    perimeter -= 2

                # Check top cell
                if n > 0 and grid[n - 1][m] == 1:
                    perimeter -= 2

    return perimeter
