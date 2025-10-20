import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from montecarlo.simulation import generate_chains
from montecarlo.performance import benchmark_sorting_algorithms

def run_scaling_benchmark(n_chains_list, n_repeats=3, random_seed=42, use_numba=False):
    '''
    Executes the benchmark with different sorting algorithms with increasing number of chains

    Parameters
    ----------
    n_chains_list : list[int]
        List of number of chains.
    n_repeats : int
        Number of repetitions for each benchmark.
    random_seed : int
        Seed for reproducibility.
    use_numba : bool
        Wether to use Numba-accelerated version of generated_chains.

    Returns
    -------
    pd.Dataframe
        Results
        number_of_chains | algorithm | generation_time | sorting_time | use_numba
    '''
    np.random.seed(random_seed)
    records = []

    for n in n_chains_list:
        for _ in range(n_repeats):
            start_gen = time.perf_counter()
            chain_lengths, freq_A, _, _ = generate_chains(n, use_numba=use_numba)
            generation_time = time.perf_counter() - start_gen

            benchmark = benchmark_sorting_algorithms(chain_lengths, freq_A)
            for algo, sorting_time in benchmark.items():
                records.append({
                    "number_of_chains": n,
                    "algorithm": algo,
                    "generation_time": generation_time,
                    "sorting_time": sorting_time,
                    "use_numba": use_numba
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