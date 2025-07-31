def threshold_check(values, threshold=50):
    return ["Enter" if val >= threshold else "Wait" for val in values]

# Example Tests
print(threshold_check([45, 55, 33, 80]))  # ['Wait', 'Enter', 'Wait', 'Enter']
print(threshold_check([50, 50, 49], 50))  # ['Enter', 'Enter', 'Wait']
print(threshold_check([], 70))           # []
