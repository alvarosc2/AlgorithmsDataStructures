import pytest
from anagram_check import compare_arrays

class testAnagramCheck2:
    def test_compare_arrays(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 5]

        assert compare_arrays(arr1, arr2) == True