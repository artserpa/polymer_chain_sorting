from montecarlo.analysis import run_scaling_benchmark, plot_benchmark_results, save_results_to_csv
from montecarlo.visualization import plot_w_distribution
from montecarlo.simulation import generate_chains
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # 1️⃣ Benchmark de tempo
    n_chains_list = [100, 500, 1000]
    df_results = run_scaling_benchmark(n_chains_list, n_repeats=3, use_numba=True)
    
    # 2️⃣ Salvar resultados em CSV
    save_results_to_csv(df_results, "results/benchmark_with_numba.csv")
    
    # 3️⃣ Plotar gráficos de tempos
    plot_benchmark_results(df_results, metric="sorting_time", save_path="results/sorting_time.png")
    #plot_benchmark_results(df_results, metric="generation_time", save_path="results/generation_time.png")
    plot_benchmark_results(df_results, metric="total_time", save_path="results/total_time.png")
    
    # 4️⃣ Gerar cadeias para distribuição
    chain_lengths, freq_A, freq_B, freq_C = generate_chains(10000, use_numba=True)
    
    # 5️⃣ Plotar distribuições W
    plt.figure(figsize=(12, 6))
    plot_w_distribution(freq_A, chain_lengths, smooth_window=5, poly_order=2, label="A", color="blue")
    plt.xlim(left=0.84, right=1.0)
    plt.xlabel("Fraction of monomer")
    plt.ylabel("W")
    plt.legend()
    plt.savefig("results/distribution_WA.png", dpi=300)

    plt.figure(figsize=(12, 6))
    plot_w_distribution(freq_B, chain_lengths, smooth_window=5, poly_order=2, label="B", color="green")
    plot_w_distribution(freq_C, chain_lengths, smooth_window=5, poly_order=2, label="C", color="red")
    plt.xlim(left=0.0, right=0.12)
    plt.xlabel("Fraction of monomer")
    plt.ylabel("W")
    plt.legend()
    plt.savefig("results/distribution_WBC.png", dpi=300)
    plt.show()
