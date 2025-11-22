import pytest
from ..array_sequences.array_pair_sum import array_pair_sum

class TestArrayPairSum:
    def test_array_pair_sum(self):
        arr = [1, 3, 2, 2]
        k = 4

        assert array_pair_sum(arr, k) == [(1, 3), (2, 2)]