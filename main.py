from montecarlo.analysis import run_scaling_benchmark, plot_benchmark_results, save_results_to_csv

if __name__ == "__main__":
    n_chains_list = [100, 500, 1000]
    df_results = run_scaling_benchmark(n_chains_list, n_repeats=3, use_numba=True)
    
    save_results_to_csv(df_results, 'benchmark_with_numba.csv')

    plot_benchmark_results(df_results, metric="sorting_time", save_path="sorting_time.png")

    # 4. Plotar tempo de geração
    plot_benchmark_results(df_results, metric="generation_time", save_path="generation_time.png")

    # 5. Plotar tempo total
    plot_benchmark_results(df_results, metric="total_time", save_path="total_time.png")

    
