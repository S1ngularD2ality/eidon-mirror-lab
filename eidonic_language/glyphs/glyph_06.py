def xor_pattern(a, b):
    return [[ai ^ bi for ai, bi in zip(ar, br)] for ar, br in zip(a, b)]
