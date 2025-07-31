def ascension_path(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ascension_path(n - 1) + ascension_path(n - 2)

# Test
print(ascension_path(0))   # 0
print(ascension_path(1))   # 1
print(ascension_path(5))   # 5
print(ascension_path(10))  # 55
