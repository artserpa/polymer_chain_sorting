import numpy as np
from montecarlo.performance import benchmark_sorting_algorithms
from montecarlo.sorting_algorithms import (
            bubble_sort, bubble_sort_numba,
            insertion_sort, insertion_sort_numba,
            selection_sort, selection_sort_numba,
            tim_sort
        )

def test_benchmark_sorting_algorithms():
    chain_lengths = np.array([5, 2, 9, 1, 5, 6])
    freq_A = np.array([0.5, 0.2, 0.9, 0.1, 0.5, 0.6])

    results = benchmark_sorting_algorithms(chain_lengths, freq_A)

    expected_algorithms = [
        "bubble_sort", "bubble_sort_numba",
        "insertion_sort", "insertion_sort_numba",
        "selection_sort", "selection_sort_numba",
        "tim_sort"
    ]

    for algo in expected_algorithms:
        assert algo in results
    
    for time_val in results.values():
        assert time_val > 0
    
    for algo, time_val in results.items():
        cl_copy = chain_lengths.copy()
        fa_copy = freq_A.copy()
        func = {
            "bubble_sort": bubble_sort,
            "bubble_sort_numba": bubble_sort_numba,
            "insertion_sort": insertion_sort,
            "insertion_sort_numba": insertion_sort_numba,
            "selection_sort": selection_sort,
            "selection_sort_numba": selection_sort_numba,
            "tim_sort": tim_sort
        }[algo]
        sorted_cl, sorted_fa = func(cl_copy, fa_copy)

        # chain_lengths deve estar ordenado
        assert np.all(sorted_cl[:-1] <= sorted_cl[1:])
        
        # freq_A deve acompanhar a ordem de chain_lengths
        expected_fa = [x for _, x in sorted(zip(chain_lengths, freq_A))]
        assert np.all(sorted_fa == expected_fa)