def dual_sum(energies, key):
    return sum(e for e in energies if e % key == 0)

# Example Tests
print(dual_sum([3, 6, 9, 12], 3))     # 30
print(dual_sum([4, 8, 13, 17], 2))    # 12
print(dual_sum([5, 10, 15], 4))       # 0
print(dual_sum([], 3))               # 0
