def rotate_inverse(grid):
    return [list(reversed(col)) for col in zip(*grid)]
