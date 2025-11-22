def array_pair_sum(arr, k):
    perm = []

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            else:
                perm.append((arr[i], arr[j]))

    result = []
    for i in range(len(perm)):
        if perm[i][0] + perm[i][1] == k:
            result.append(perm[i])
        
    return result