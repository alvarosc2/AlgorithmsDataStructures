from anagram_check import *

# The strings are not anagrams
if anagram_check('Clint Eastwood', 'anagram') == False:
    print('Las cadenas no son anagramas')

# The strings are anagrams
if anagram_check('Clint Eastwood', 'old west action') == True:
    print('Las cadenas son anagramas')