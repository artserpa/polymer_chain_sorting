import numpy as np
from montecarlo.performance import benchmark_sorting_algorithms

def test_benchmark_basic():
    arr_test = np.array([5, 2, 9, 1, 5, 6])
    results = benchmark_sorting_algorithms(arr_test)

    for key, val in results.items():
        assert isinstance(val, float)
        assert val >= 0