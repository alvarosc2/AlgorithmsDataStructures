def array_pair_sum(arr, k):
    if len(arr) < 2:
        return
    
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

def array_pair_sum2(arr, k):
    # The array must have at least two elements
    if len(arr) < 2:
        return
    
    #sets for tracking
    #important strategy to convert a problem O(n^2) to O(n)
    seen = set()
    output = set()

    #for every number in array
    for num in arr:
        #set target difference
        target = k - num
        #add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        else:
            #Add a tuple with the corresponding pair
            output.add( (min(num, target), max(num, target)) )

    return output
