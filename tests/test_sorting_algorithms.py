import numpy as np
from montecarlo.sorting_algorithms import bubble_sort, bubble_sort_numba

def test_bubble_sort_python():
    arr = np.array([5, 2, 9, 1, 5, 6])
    sorted_arr = bubble_sort(arr)
    assert np.array_equal(sorted_arr, np.array([1, 2, 5, 5, 6, 9]))

def test_bubble_sort_numba():
    arr = np.array([5, 2, 9, 1, 5, 6])
    sorted_arr = bubble_sort_numba(arr)
    assert np.array_equal(sorted_arr, np.array([1, 2, 5, 5, 6, 9]))