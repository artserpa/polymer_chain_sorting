import os
from montecarlo.analysis import run_scaling_benchmark, plot_benchmark_results, save_results_to_csv

if __name__ == "__main__":
    n_chains_list = [1000, 5000, 10000]
    df_results = run_scaling_benchmark(n_chains_list, n_repeats=3, use_numba=False)
    
    # Criar pasta results se não existir
    os.makedirs("results", exist_ok=True)

    save_results_to_csv(df_results, 'results/benchmark_with_numba.csv')

    plot_benchmark_results(df_results, metric="sorting_time", save_path="results/sorting_time.png")
    plot_benchmark_results(df_results, metric="generation_time", save_path="results/generation_time.png")
    plot_benchmark_results(df_results, metric="total_time", save_path="results/total_time.png")
