import numpy as np
import matplotlib
matplotlib.use("Agg")  # Prevents plot windows to open during test
import matplotlib.pyplot as plt

from montecarlo.visualization import plot_w_distribution
from montecarlo.simulation import generate_chains

def test_generate_chains_shapes():
    n = 100
    chain_lengths, freq_A, freq_B, freq_C = generate_chains(n, use_numba=False)
    
    assert len(chain_lengths) == n
    assert len(freq_A) == n
    assert len(freq_B) == n
    assert len(freq_C) == n

def test_plot_w_distribution_runs_without_error():
    n = 50
    chain_lengths = np.random.randint(1, 20, size=n)
    freq_A = np.random.rand(n)

    plt.figure()
    try:
        plot_w_distribution(freq_A, chain_lengths, smooth_window=5, poly_order=2)
    except Exception as e:
        assert False, f"plot_w_distribution levantou um erro: {e}"
    plt.close()
