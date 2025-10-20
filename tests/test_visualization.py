import numpy as np
import pytest
from montecarlo.visualization import plot_w_distribution
import matplotlib.pyplot as plt

def test_plot_w_distribution_runs():
    freq_X = np.array([0.1, 0.2, 0.5, 0.8])
    chain_lengths = np.array([5, 10, 2, 1])

    plot_w_distribution(freq_X, chain_lengths, n_bins=10, smooth_window=5, poly_order=2, label="Test", color="blue")

    plt.close()
