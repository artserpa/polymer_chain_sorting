import time
import numpy as np
from montecarlo.sorting_algorithms import (
    bubble_sort, bubble_sort_numba,
    insertion_sort, insertion_sort_numba,
    selection_sort, selection_sort_numba,
    tim_sort
)

def benchmark_sorting_algorithms(chains_array, freq_A):
    '''
    Compares execution times of different sorting algorithms (pure Python and Numba).

    Parameters
    ----------
    chains_array : np.ndarray
        Array of the polymer chains.
    freq_A : np.ndarray
        Array of frequencies of A, same length as chain_lengths.

    Returns
    -------
    dict
        Execution times for each algorithm.
    '''
    results = {}
    algorithms = {
        "bubble_sort": bubble_sort,
        "bubble_sort_numba": bubble_sort_numba,
        "insertion_sort": insertion_sort,
        "insertion_sort_numba": insertion_sort_numba,
        "selection_sort": selection_sort,
        "selection_sort_numba": selection_sort_numba,
        "tim_sort": tim_sort
    }

    for name, func in algorithms.items():
        cl_copy = chains_array.copy()
        fa_copy = freq_A.copy()

        start_time = time.perf_counter()
        func(cl_copy, fa_copy)
        elapsed = time.perf_counter() - start_time

        results[name] = elapsed

    return results