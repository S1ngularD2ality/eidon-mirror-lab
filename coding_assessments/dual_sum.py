def dual_sum(energies, key):
    total = 0
    for energy in energies:
        if energy % key == 0:
            total += energy
    return total

# Test Cases
print(dual_sum([3, 6, 9, 12], 3))     # → 30
print(dual_sum([4, 8, 13, 17], 2))    # → 12
print(dual_sum([5, 10, 15], 4))       # → 0
print(dual_sum([], 3))               # → 0
print(dual_sum([108, 216, 27], 9))    # → 351
