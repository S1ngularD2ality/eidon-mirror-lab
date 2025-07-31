def sacred_sum(offerings):
    total = 0
    for item in offerings:
        total += item
    return total

# Test
print(sacred_sum([7, 13, 33]))   # 53
print(sacred_sum([1, 2, 3, 4]))  # 10
print(sacred_sum([]))           # 0
