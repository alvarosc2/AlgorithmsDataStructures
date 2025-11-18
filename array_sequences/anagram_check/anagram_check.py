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
        return 'son iguales'
    else:
        return 'No son iguales'

resultado = anagram_check('Clint Eastwood', 'anagram')
print(resultado)