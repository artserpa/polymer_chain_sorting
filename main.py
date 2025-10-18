from montecarlo.analysis import run_scaling_benchmark, plot_benchmark_results

if __name__ == "__main__":
    n_chains_list = [100, 500, 1000]  # você pode aumentar depois
    results = run_scaling_benchmark(n_chains_list)
    plot_benchmark_results(results, n_chains_list)
