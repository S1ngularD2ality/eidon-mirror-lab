def emergence_spiral(n):
    return [i**2 + i for i in range(n) if (i % 3 == 0 or i % 5 == 0)]
