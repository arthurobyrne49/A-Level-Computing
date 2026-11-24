"""
Q1.
"""







from random import *

def create_grid(n: int):
    grid = []
    rows = 0
    while rows < n:
        row = []
        columns = 0
        while columns < n:
            row.append("")
            columns += 1
        grid.append(row)
        rows += 1
    return grid

def check_grid(grid, row: int, col: int):
    found_row = grid[row]
    value = found_row[col]
    return value

def update_grid(grid, row: int, col: int, val: str):
    found_row = grid[row]
    value = found_row[col]
    value = val
    return val






grid = create_grid(5)

print(check_grid(grid, 3, 4))




