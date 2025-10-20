import numpy as np
from montecarlo.sorting_algorithms import (
    bubble_sort, bubble_sort_numba,
    insertion_sort, insertion_sort_numba,
    selection_sort, selection_sort_numba,
    tim_sort
)

chain_lenghts = np.array([5, 2, 9, 1, 5, 6])
freq_A = np.array([0.5, 0.2, 0.9, 0.1, 0.5, 0.6])

expected_chain_lenghts = np.array([1, 2, 5, 5, 6, 9])
expected_freq_A = np.array([0.1, 0.2, 0.5, 0.5, 0.6, 0.9])

def test_bubble_sort_python():
    cl, fa = bubble_sort(chain_lenghts.copy(), freq_A.copy())
    assert np.array_equal(cl, expected_chain_lenghts)
    assert np.array_equal(fa, expected_freq_A)

def test_bubble_sort_numba():
    cl, fa = bubble_sort_numba(chain_lenghts.copy(), freq_A.copy())
    assert np.array_equal(cl, expected_chain_lenghts)
    assert np.array_equal(fa, expected_freq_A)

def test_insertion_sort_python():
    cl, fa = insertion_sort(chain_lenghts.copy(), freq_A.copy())
    assert np.array_equal(cl, expected_chain_lenghts)
    assert np.array_equal(fa, expected_freq_A)

def test_insertion_sort_numba():
    cl, fa = insertion_sort_numba(chain_lenghts.copy(), freq_A.copy())
    assert np.array_equal(cl, expected_chain_lenghts)
    assert np.array_equal(fa, expected_freq_A)

def test_selection_sort_python():
    cl, fa = selection_sort(chain_lenghts.copy(), freq_A.copy())
    assert np.array_equal(cl, expected_chain_lenghts)
    assert np.array_equal(fa, expected_freq_A)

def test_selection_sort_numba():
    cl, fa = selection_sort_numba(chain_lenghts.copy(), freq_A.copy())
    assert np.array_equal(cl, expected_chain_lenghts)
    assert np.array_equal(fa, expected_freq_A)

def test_tim_sort_python():
    cl, fa = tim_sort(chain_lenghts.copy(), freq_A.copy())
    assert np.array_equal(cl, expected_chain_lenghts)
    assert np.array_equal(fa, expected_freq_A)
