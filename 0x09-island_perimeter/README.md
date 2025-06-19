markdown# 0x09. Island Perimeter

## Description
This project implements a solution to calculate the perimeter of an island represented in a 2D grid. The grid uses integers where 0 represents water and 1 represents land.

## Problem Statement
Create a function `island_perimeter(grid)` that returns the perimeter of the island described in the grid:
- `grid` is a list of list of integers
- 0 represents water, 1 represents land
- Each cell is square with side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- Grid is rectangular, width and height not exceeding 100
- Grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes"

## Algorithm
The solution iterates through each cell in the grid:
1. For each land cell (1), check its 4 neighbors (up, down, left, right)
2. For each neighbor that is water (0) or out of bounds, add 1 to the perimeter
3. Return the total perimeter count

## Time Complexity
- **Time Complexity**: O(m × n) where m is the number of rows and n is the number of columns
- **Space Complexity**: O(1) - only using constant extra space

## Files
- `0-island_perimeter.py`: Main implementation file
- `0-main.py`: Test file provided in the problem
- `README.md`: This file

## Usage
```python
#!/usr/bin/python3
island_perimeter = __import__('0-island_perimeter').island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
