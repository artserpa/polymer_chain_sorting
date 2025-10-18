import time
import numpy as np
from montecarlo.sorting_algorithms import (
    bubble_sort, bubble_sort_numba,
    insertion_sort, insertion_sort_numba,
    selection_sort, selection_sort_numba,
    tim_sort
)

def measure_sort_time(sort_func, array):
    '''
    Measures the execution time of a sorting function.

    Parameters
    ----------
    sort_func : callable
        Sorting fucntion to be tested.
    array : np.ndarray
        Input array

    Returns
    -------
    float
        Execution time in seconds.
    '''

    start = time.time()
    sort_func(array)
    end = time.time()
    return end-start

def benchmark_sorting_algorithms(chains_array):
    '''
    Compares execution times of different sorting algorithms (pure Python and Numba).

    Parameters
    ----------
    chains_array : np.ndarray
        Array of the polymer chains.

    Returns
    -------
    dict
        Execution times for each algorithm.
    '''
    results = {}

    results['bubble_python'] = measure_sort_time(bubble_sort, chains_array)
    results['bubble_numba'] = measure_sort_time(bubble_sort_numba, chains_array)
    results['insertion_python'] = measure_sort_time(insertion_sort, chains_array)
    results['insertion_numba'] = measure_sort_time(insertion_sort_numba, chains_array)
    results['selection_python'] = measure_sort_time(selection_sort, chains_array)
    results['selection_numba'] = measure_sort_time(selection_sort_numba, chains_array)
    results['timsort_python'] = measure_sort_time(tim_sort, chains_array)

    return results