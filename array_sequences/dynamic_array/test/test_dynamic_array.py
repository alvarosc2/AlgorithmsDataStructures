import pytest
from dynamic_array import DynamicArray

def test_dynamic_array_append():
    arr = DynamicArray()
    arr.append({'name': 'Alvaro Silva', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': True})
    
    assert(arr[0]['name'], 'Alvaro Silva')
    