import pytest
import sys
from pathlib import Path
from array_pair_sum import array_pair_sum

# Add parent directory to path to import array_pair_sum module
sys.path.insert(0, str(Path(__file__).parent.parent))

class TestArrayPairSum:
    def test_array_pair_sum(self):
        arr = [1, 3, 2, 2]
        k = 4

        assert array_pair_sum(arr, k) == [(1, 3), (2, 2)]