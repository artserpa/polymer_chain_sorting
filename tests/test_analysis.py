import numpy as np
from montecarlo.analysis import run_scaling_benchmark

def test_run_scaling_benchmark():
    n_chains_list = [10, 20]
    results = run_scaling_benchmark(n_chains_list, random_seed=123)

    assert 'bubble_python' in results
    assert 'bubble_numba' in results
    assert 'insertion_python' in results
    assert 'insertion_numba' in results
    assert 'selection_python' in results
    assert 'selection_numba' in results
    assert 'timsort_python' in results

    for algo, times in results.items():
        assert len(times) == len(n_chains_list)
        assert all(isinstance(t, float) for t in times)