def array_pair_sum(arr, k):
    perm = []
    for i in range(len(arr)):
        j = i + 1
        while j < len(arr):
            perm.append((arr[i], arr[j]))
            j += 1

    result = []
    for i in range(len(perm)):
        if perm[i][0] + perm[i][1] == k:
            result.append(perm[i])
        
    return result