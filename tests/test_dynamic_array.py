'''
Test Coverage:

Initialization tests: Verify default values on creation
Length tests: Check __len__ method with empty and populated arrays
GetItem tests: Test indexing, boundary conditions, and error handling
Append tests: Verify adding elements, automatic resizing, different data types, and order preservation
Resize tests: Confirm capacity doubling and element preservation during resizing
MakeArray tests: Validate array creation with different sizes
Integration tests: Complex workflows with multiple operations and mixed data types
The tests cover edge cases like empty arrays, out-of-bounds access, negative indices, and verify the dynamic resizing behavior (1 → 2 → 4 → 8 → 16).
'''

import pytest
from ..10_array_sequences.dynamic_array import DynamicArray

class TestDynamicArrayInit:
    """Test initialization of DynamicArray"""
    
    def test_init_empty_array(self):
        """Test that a new array is initialized with correct default values"""
        arr = DynamicArray()
        assert len(arr) == 0
        assert arr.capacity == 1
        assert arr.n == 0
    

class TestDynamicArrayLen:
    """Test __len__ method"""
    
    def test_len_empty_array(self):
        """Test length of empty array"""
        arr = DynamicArray()
        assert len(arr) == 0
    
    def test_len_after_append(self):
        """Test length increases after append"""
        arr = DynamicArray()
        arr.append(1)
        assert len(arr) == 1
        arr.append(2)
        assert len(arr) == 2
    
    def test_len_after_multiple_appends(self):
        """Test length after multiple appends"""
        arr = DynamicArray()
        for i in range(10):
            arr.append(i)
        assert len(arr) == 10


class TestDynamicArrayGetItem:
    """Test __getitem__ method"""
    
    def test_getitem_single_element(self):
        """Test getting item from array with one element"""
        arr = DynamicArray()
        arr.append(42)
        assert arr[0] == 42
    
    def test_getitem_multiple_elements(self):
        """Test getting items from array with multiple elements"""
        arr = DynamicArray()
        for i in range(5):
            arr.append(i * 10)
        assert arr[0] == 0
        assert arr[2] == 20
        assert arr[4] == 40
    
    def test_getitem_out_of_bounds_positive(self):
        """Test getting item with index beyond array length"""
        arr = DynamicArray()
        arr.append(1)
        result = arr[5]
        assert isinstance(result, IndexError)
    
    def test_getitem_out_of_bounds_negative(self):
        """Test getting item with negative index"""
        arr = DynamicArray()
        arr.append(1)
        result = arr[-1]
        assert isinstance(result, IndexError)
    
    def test_getitem_empty_array(self):
        """Test getting item from empty array"""
        arr = DynamicArray()
        result = arr[0]
        assert isinstance(result, IndexError)
    
    def test_getitem_with_dict(self):
        """Test getting dictionary item from array"""
        arr = DynamicArray()
        arr.append({'name': 'Alvaro Silva', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': True})
        assert arr[0]['name'] == 'Alvaro Silva'
        assert arr[0]['coins'] == 100


class TestDynamicArrayAppend:
    """Test append method"""
    
    def test_append_single_integer(self):
        """Test appending a single integer"""
        arr = DynamicArray()
        arr.append(5)
        assert len(arr) == 1
        assert arr[0] == 5
    
    def test_append_multiple_integers(self):
        """Test appending multiple integers"""
        arr = DynamicArray()
        for i in range(5):
            arr.append(i)
        assert len(arr) == 5
        for i in range(5):
            assert arr[i] == i
    
    def test_append_triggers_resize(self):
        """Test that append triggers resize when capacity is reached"""
        arr = DynamicArray()
        initial_capacity = arr.capacity
        arr.append(1)  # n=1, capacity=1
        assert arr.capacity == initial_capacity
        arr.append(2)  # n=2, should trigger resize to capacity=2
        assert arr.capacity == 2
        arr.append(3)  # n=3, should trigger resize to capacity=4
        assert arr.capacity == 4
    
    def test_append_different_types(self):
        """Test appending different data types"""
        arr = DynamicArray()
        arr.append(42)
        arr.append("string")
        arr.append(3.14)
        arr.append([1, 2, 3])
        arr.append({'key': 'value'})
        arr.append(None)
        
        assert arr[0] == 42
        assert arr[1] == "string"
        assert arr[2] == 3.14
        assert arr[3] == [1, 2, 3]
        assert arr[4] == {'key': 'value'}
        assert arr[5] is None
    
    def test_append_maintains_order(self):
        """Test that append maintains insertion order"""
        arr = DynamicArray()
        values = [10, 20, 30, 40, 50]
        for val in values:
            arr.append(val)
        for i, val in enumerate(values):
            assert arr[i] == val
    
    def test_append_large_number_of_elements(self):
        """Test appending a large number of elements"""
        arr = DynamicArray()
        n = 1000
        for i in range(n):
            arr.append(i)
        assert len(arr) == n
        assert arr[0] == 0
        assert arr[n-1] == n-1


class TestDynamicArrayResize:
    """Test _resize method"""
    
    def test_resize_doubles_capacity(self):
        """Test that resize doubles the capacity"""
        arr = DynamicArray()
        arr.append(1)  # capacity = 1
        arr.append(2)  # triggers resize, capacity = 2
        assert arr.capacity == 2
        arr.append(3)  # triggers resize, capacity = 4
        assert arr.capacity == 4
        arr.append(4)
        arr.append(5)  # triggers resize, capacity = 8
        assert arr.capacity == 8
    
    def test_resize_preserves_elements(self):
        """Test that resize preserves all existing elements"""
        arr = DynamicArray()
        for i in range(10):
            arr.append(i)
        # Verify all elements are preserved
        for i in range(10):
            assert arr[i] == i
    
    def test_capacity_growth(self):
        """Test capacity grows exponentially"""
        arr = DynamicArray()
        capacities = [arr.capacity]
        for i in range(16):
            arr.append(i)
            if arr.capacity not in capacities:
                capacities.append(arr.capacity)
        # Capacity should grow: 1 -> 2 -> 4 -> 8 -> 16
        assert capacities == [1, 2, 4, 8, 16]


class TestDynamicArrayMakeArray:
    """Test make_array method"""
    
    def test_make_array_creates_array(self):
        """Test that make_array creates an array of specified capacity"""
        arr = DynamicArray()
        new_array = arr.make_array(5)
        # The array should be created (checking it's not None)
        assert new_array is not None
    
    def test_make_array_different_sizes(self):
        """Test make_array with different sizes"""
        arr = DynamicArray()
        for size in [1, 10, 100, 1000]:
            new_array = arr.make_array(size)
            assert new_array is not None


class TestDynamicArrayIntegration:
    """Integration tests for DynamicArray"""
    
    def test_complex_workflow(self):
        """Test complex workflow with multiple operations"""
        arr = DynamicArray()
        
        # Start empty
        assert len(arr) == 0
        
        # Add elements
        for i in range(20):
            arr.append(i * 2)
        
        # Check length
        assert len(arr) == 20
        
        # Check capacity grew appropriately
        assert arr.capacity >= 20
        
        # Verify all elements
        for i in range(20):
            assert arr[i] == i * 2
    
    def test_mixed_data_types_workflow(self):
        """Test workflow with mixed data types"""
        arr = DynamicArray()
        
        test_data = [
            42,
            "hello",
            3.14159,
            [1, 2, 3],
            {'name': 'test', 'value': 100},
            None,
            True,
            False
        ]
        
        for item in test_data:
            arr.append(item)
        
        assert len(arr) == len(test_data)
        
        for i, item in enumerate(test_data):
            assert arr[i] == item
