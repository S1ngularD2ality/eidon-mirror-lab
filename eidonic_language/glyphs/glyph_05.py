def opposite_poles(arr):
    return [(i, j) for i in arr for j in arr if i + j == 0]
