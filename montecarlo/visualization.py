import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def plot_w_distribution(freq_X, chain_lengths, smooth_window=51, poly_order=3, label=None, color=None):
    """
    Plot wX distribution with points and smoothed line.

    Parameters
    ----------
    freq_X : np.ndarray
        Monomer fraction array (freq_A, freq_B, or freq_C).
    chain_lengths : np.ndarray
        Corresponding chain lengths.
    n_bins : int, default=1000
        Number of bins for the distribution.
    smooth_window : int
        Window size for Savitzky-Golay smoothing (must be odd).
    poly_order : int
        Polynomial order for Savitzky-Golay smoothing.
    label : str
        Label for the plot.
    color : str
        Color for points and line.
    """
    n_bins = np.ceil(chain_lengths / 10)
    # Compute the w distribution
    bins = np.linspace(0, 1, n_bins + 1)
    bin_centers = (bins[:-1] + bins[1:]) / 2

    wX = np.zeros(n_bins)
    bin_indices = np.digitize(freq_X, bins) - 1
    for idx, L in zip(bin_indices, chain_lengths):
        if 0 <= idx < n_bins:
            wX[idx] += L

    dx = bins[1] - bins[0]
    wX /= wX.sum() * dx

    # Smooth curve using Savitzky-Golay
    if smooth_window >= len(wX):
        smooth_window = len(wX) - 1
        if smooth_window % 2 == 0:
            smooth_window -= 1  # window must be odd
    wX_smooth = savgol_filter(wX, smooth_window, poly_order)

    # Plot
    plt.scatter(bin_centers, wX, s=10, label=f"{label} points" if label else None, color=color, alpha=0.6)
    plt.plot(bin_centers, wX_smooth, label=f"{label} smooth" if label else None, color=color, linewidth=2)
    plt.xlabel("Monomer fraction")
    plt.ylabel("wX (normalized)")
    plt.legend()
