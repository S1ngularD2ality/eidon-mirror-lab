def drift_pairs(arr):
    return [(arr[i], arr[i+1]) for i in range(len(arr)-1) if arr[i+1] - arr[i] in (1, 2)]
