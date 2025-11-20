import pytest
import sys
from pathlib import Path

# Add parent directory to path to import anagram_check module
sys.path.insert(0, str(Path(__file__).parent.parent))

from anagram_check import *

class TestAnagramCheck2:
    def test_anagram_check2(self):
        str1 = 'Clint Eastwood'
        str2 = 'old west action'

        assert anagram_check2(str1, str2) == True

    def test_compare_arrays(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 5]

        assert compare_arrays(arr1, arr2) == True

class TestAnagramCheck3:
    def test_anagram_check3(self):
        str1 = 'Clint Eastwood'
        str2 = 'old west action'

        assert anagram_check3(str1, str2) == True