def anagram_check(str1, str2):
    # create two empty dictionaries that later will be compared
    dict1 = {}
    dict2 = {}
    
    # the whole string in lowercase and without spaces
    result1 = str1.lower().replace(' ', '')
    result2 = str2.lower().replace(' ', '')

    # put each character of each string in a dictionary and increment
    # the count if the character already exists.
    for i in range(len(result1)):
        if dict1.get(result1[i]) == None:
            dict1.update({result1[i]: 1})
        else:
            dict1[result1[i]] += 1

    for j in range(len(result2)):
        if dict2.get(result2[j]) == None:
            dict2.update({result2[j]: 1})
        else:
            dict2[result2[j]] += 1
        
    # compare both dictionaries, sames keys and same values
    if dict1 == dict2:
        return True
    else:
        return False

def anagram_check2(str1, str2):
    # each position represents one letter of the alphabet
    arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # the whole string in lowercase and without spaces
    result1 = str1.lower().replace(' ', '')
    result2 = str2.lower().replace(' ', '')
    
    for char in result1:
        arr1[ord(char) - 97] += 1
    
    for char in result2:
        arr2[ord(char) - 97] += 1

    if compare_arrays(result1, result2) == True:
        return True
    else:
        return False

def compare_arrays(arr1, arr2):
    # if the length of both arrays are different then the
    # arrays are not equal
    if len(arr1) != len(arr2):
        return False
    
    # compare both arrays element by element. They are 
    # equal if each element of arr1 is equal to each 
    # element of arr2
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
        
    return True