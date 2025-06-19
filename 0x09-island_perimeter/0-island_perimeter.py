#!/usr/bin/python3
"""
Module for calculating island perimeter in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.
    
    Args:
        grid (list): A list of list of integers where:
                    - 0 represents water
                    - 1 represents land
                    
    Returns:
        int: The perimeter of the island
        
    The function iterates through each cell in the grid and for every
    land cell (1), it checks its four neighbors (up, down, left, right).
    For each neighbor that is either water (0) or out of bounds,
    it adds 1 to the perimeter count.
    """
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    # Directions for checking neighbors: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(rows):
        for j in range(cols):
            # Only process land cells
            if grid[i][j] == 1:
                # Check all 4 neighbors
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    
                    # If neighbor is out of bounds or is water, 
                    # this edge contributes to perimeter
                    if (ni < 0 or ni >= rows or 
                        nj < 0 or nj >= cols or 
                        grid[ni][nj] == 0):
                        perimeter += 1
    
    return perimeter
