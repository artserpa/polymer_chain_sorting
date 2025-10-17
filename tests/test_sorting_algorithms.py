import numpy as np
from montecarlo.sorting_algorithms import (
    bubble_sort, bubble_sort_numba,
    insertion_sort, insertion_sort_numba,
    selection_sort, selection_sort_numba,
    tim_sort, tim_sort_numba
)

arr_test = np.array([5, 2, 9, 1, 5, 6])
arr_sorted = np.array([1, 2, 5, 5, 6, 9])

def test_bubble_sort_python():
    assert np.array_equal(bubble_sort(arr_test), arr_sorted)

def test_bubble_sort_numba():
    assert np.array_equal(bubble_sort_numba(arr_test), arr_sorted)

def test_insertion_sort_python():
    assert np.array_equal(insertion_sort(arr_test), arr_sorted)

def test_insertion_sort_numba():
    assert np.array_equal(insertion_sort_numba(arr_test), arr_sorted)

def test_selection_sort_python():
    assert np.array_equal(selection_sort(arr_test), arr_sorted)

def test_selection_sort_numba():
    assert np.array_equal(selection_sort_numba(arr_test), arr_sorted)

def test_tim_sort_python():
    assert np.array_equal(tim_sort(arr_test), arr_sorted)
