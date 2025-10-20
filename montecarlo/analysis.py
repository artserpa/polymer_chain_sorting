import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from montecarlo.simulation import generate_chains
from montecarlo.performance import (
    bubble_sort, bubble_sort_numba,
    insertion_sort, insertion_sort_numba,
    selection_sort, selection_sort_numba,
    tim_sort
)
import time

def run_scaling_benchmark(n_chains_list, n_repeats=3, use_numba=False, random_seed=42):
    """
    Runs benchmarks for increasing number of chains, including generation and sorting
    of freq_A, freq_B, freq_C along with chain_lengths.
    Supports both Python and Numba-accelerated sorting functions.

    Parameters
    ----------
    n_chains_list : int
        List of number of chians.
    n_repeats : int
        Number of repeats.
    use_numba : bool
        Wether use Numba or not.
    random_seed : int
        Set the seed number for the simulation.

    Returns
    -------
    DataFrame
        Information for the chain generation and sorting times.
        number_of_chains | algorithm | use_numba | generation_time | sorting_time | repeat
    """
    np.random.seed(random_seed)
    records = []

    for n in n_chains_list:
        # --- Chain generation ---
        start_gen = time.time()
        chain_lengths, freq_A, freq_B, freq_C = generate_chains(n, use_numba=use_numba)
        gen_time = time.time() - start_gen

        # --- Sorting algorithms ---
        sorting_algos = {
            'bubble_sort': bubble_sort_numba if use_numba else bubble_sort,
            'insertion_sort': insertion_sort_numba if use_numba else insertion_sort,
            'selection_sort': selection_sort_numba if use_numba else selection_sort,
            'tim_sort': tim_sort  # Tim sort does not support Numba
        }

        for algo_name, algo_func in sorting_algos.items():
            for repeat in range(n_repeats):
                D_copy = chain_lengths.copy()
                F_A_copy = freq_A.copy()
                F_B_copy = freq_B.copy()
                F_C_copy = freq_C.copy()

                start_sort = time.time()
                algo_func(D_copy, F_A_copy)
                algo_func(D_copy, F_B_copy)
                algo_func(D_copy, F_C_copy)
                sort_time = time.time() - start_sort

                records.append({
                    'number_of_chains': n,
                    'algorithm': algo_name,
                    'use_numba': use_numba,
                    'generation_time': gen_time,
                    'sorting_time': sort_time,
                    'repeat': repeat + 1
                })

    return pd.DataFrame(records)

def plot_benchmark_results(df_results, save_path=None, metric="sorting_time"):
    '''
    Plots the algorithms' benchmark results.

    Parameters
    ----------
    df_results : pd.DataFrame
        Benchmark results.
    save_path : str, optional
        Path for savefig.
    metric : str, default="sorting_time"
        Which metric to plot:
        - "sorting_time" : only sorting time
        - "generation_time" : only chain generation time
        - "total_time" : generation + sorting
    '''
    if metric == "total_time":
        df_results = df_results.copy()
        df_results["total_time"] = df_results["generation_time"] + df_results["sorting_time"]
        time_col = "total_time"
    elif metric in ["sorting_time", "generation_time"]:
        time_col = metric
    else:
        raise ValueError("metric must be one of ['sorting_time', 'generation_time', 'total_time']")


    grouped = (
        df_results.groupby(['number_of_chains', 'algorithm'])[time_col]
        .agg(['mean', 'std'])
        .reset_index()
    )

    algorithms = grouped['algorithm'].unique()
    x = np.arange(len(grouped['number_of_chains'].unique()))
    width = 0.1

    plt.figure(figsize=(12, 6))

    for i, algo in enumerate(algorithms):
        subset = grouped[grouped['algorithm'] == algo]
        plt.bar(
            x + i * width,
            subset['mean'],
            width,
            yerr=subset['std'],
            capsize=5,
            label=algo
        )

    plt.xticks(
        x + width * (len(algorithms) / 2), 
        grouped['number_of_chains'].unique()
    )
    plt.xlabel('Number of chains')
    ylabel_map = {
        "sorting_time" : "Average sorting time (s)",
        "generation_time" : "Average chain generation time (s)",
        "total_time" : "Average total time (s)",
    }
    plt.ylabel(ylabel_map[metric])
    plt.legend()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()

def save_results_to_csv(df_results, filename='benchmark_results.csv'):
    '''
    Save the results in csv format.

    Parameters
    ----------
    df_results : pd.DataFrame
        Benchmark results.
    filename : str
        csv filename.
    '''
    df = df_results.copy()
    df['total_time'] = df['generation_time'] + df['sorting_time']
    df_results.to_csv(filename, index=False)