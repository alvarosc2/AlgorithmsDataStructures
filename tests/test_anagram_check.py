import pytest
from ..section_10_array_sequences.anagram_check.anagram_check import anagram_check, anagram_check2, anagram_check3, compare_arrays

class TestAnagramCheck:
    def test_anagram_check_is_anagram(self):
        str1 = 'Clint Eastwood'
        str2 = 'old west action'

        assert anagram_check(str1, str2) == True

    def test_anagram_check_is_not_anagram(self):
        str1 = 'Clint Eastwood'
        str2 = 'Is not anagram'

        assert anagram_check(str1, str2) == False

    def test_anagram_check_str1_empty(self):
        str1 = ''
        str2 = 'Is not anagram'

        assert anagram_check(str1, str2) == False

    def test_anagram_check_str2_empty(self):
        str1 = 'Clint Eastwood'
        str2 = ''

        assert anagram_check(str1, str2) == False

    def test_anagram_check_both_strings_empty(self):
        str1 = ''
        str2 = ''

        assert anagram_check(str1, str2) == True
class TestAnagramCheck2:
    def test_anagram_check_is_anagram(self):
        str1 = 'Clint Eastwood'
        str2 = 'old west action'

        assert anagram_check2(str1, str2) == True

    def test_anagram_check_is_not_anagram(self):
        str1 = 'Clint Eastwood'
        str2 = 'Not an anagram'

        assert anagram_check2(str1, str2) == False


class TestAnagramCheck3:
    def test_anagram_check_is_anagram(self):
        str1 = 'Clint Eastwood'
        str2 = 'old west action'

        assert anagram_check3(str1, str2) == True

    def test_anagram_check_is_not_anagram(self):
        str1 = 'Clint Eastwood'
        str2 = 'Not an anagram'

        assert anagram_check3(str1, str2) == False

class TestCompareArrays:
    def test_compare_arrays_equal_length(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 5]

        assert compare_arrays(arr1, arr2) == True

    def test_compare_arrays_different_length(self):
        arr1 = [1, 2, 3, 4]
        arr2 = [1, 2, 3, 4, 5]

        assert compare_arrays(arr1, arr2) == False

    def test_compare_arrays_different_arrays(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [6, 7, 8, 9, 0]

        assert compare_arrays(arr1, arr2) == False