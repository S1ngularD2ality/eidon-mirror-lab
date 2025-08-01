def fill_hollow(grid):
    return [[cell if cell != 0 else 1 for cell in row] for row in grid]
