from anagram_check import *

# The strings are not anagrams
if not anagram_check2('Clint Eastwood', 'anagram'):
    print('Las cadenas no son anagramas')

# The strings are anagrams
if anagram_check2('Clint Eastwood', 'old west action'):
    print('Las cadenas son anagramas')

if anagram_check3('Clint Eastwood', 'old west action'):
    print('The strings are anagrams')