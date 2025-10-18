import numpy as np
import matplotlib.pyplot as plt
from montecarlo.simulation import generate_chains
from montecarlo.performance import benchmark_sorting_algorithms

def run_scaling_benchmark(n_chains_list, random_seed=42):
    '''
    Executes the benchmark with different sorting algorithms with increasing number of chains

    Parameters
    ----------
    n_chains_list : list[int]
        List of number of chains.
    random_seed : int
        Seed for reproducibility.

    Returns
    -------
    dict
        Results in the format:
        {
            'bubble_python': [times...],
            'bubble_numba': [times...],
            ...
        }
    '''
    np.random.seed(random_seed)
    results = {}

    for n in n_chains_list:
        chains_lengths, _, _, _ = generate_chains(n, use_numba=False)
        benchmark = benchmark_sorting_algorithms(chains_lengths)

        for algo, time_val in benchmark.items():
            if algo not in results:
                results[algo] = []
            results[algo].append(time_val)
    return results

def plot_benchmark_results(results, n_chains_list, save_path=None):
    '''
    Plots the algorithms' benchmark results.

    Parameters
    ----------
    results : dict
        Benchmark results.
    n_chains_lit : list[int]
        List of the number of chains.
    save_path : str, optional
        Path for savefig.
    '''
    plt.figure(figsize=(10, 6))

    for algo, times in results.items():
        plt.plot(n_chains_list, times, label=algo)
    plt.xlabel('Number of chains')
    plt.ylabel('Execution time (s)')
    plt.legend()

    if save_path:
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()
