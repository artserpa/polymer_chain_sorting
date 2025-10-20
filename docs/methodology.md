```markdown
# Methodology

This project implements a Monte Carlo simulation to model polymer chain formation with three monomer types: A, B, and C. The methodology consists of the following steps:

## 1. Polymer Chain Generation

- Chains are generated sequentially, with each monomer added based on conditional probabilities depending on the last monomer in the chain.
- Probabilities for starting a chain (`Pa`, `Pb`, `Pc`) are based on initial monomer fractions.
- Transition probabilities (`P_AA`, `P_AB`, etc.) account for different propagation rates between monomer types.
- Chains terminate probabilistically when a random number exceeds the current propagation probability.

The chain generation function returns:

- `chain_lengths`: array of chain sizes  
- `freq_A`, `freq_B`, `freq_C`: fraction of each monomer type per chain

Numba JIT compilation can optionally be used to accelerate generation.

## 2. Sorting Benchmark

- Multiple sorting algorithms are implemented: Bubble Sort, Selection Sort, Insertion Sort, and Tim Sort.  
- Sorting is applied to `chain_lengths` along with the corresponding monomer fractions (`freq_A`, `freq_B`, `freq_C`) simultaneously.  
- Benchmarks are run multiple times to gather average and standard deviation of execution times.  
- Sorting results, generation times, and total times are stored in a CSV file.

## 3. Distribution Calculation (W)

- After sorting, the polymer chains are binned to calculate the weighted fraction distributions (`W`) for each monomer type.  
- Weighted fractions are normalized so that the total area under the curve equals 1.  
- Smoothed distributions are computed using Savitzky–Golay filter to assess convergence visually.  

## 4. Visualization

- Scatter plots are created for each monomer type, showing computed `W` values.  
- Smoothed lines are plotted over the points to evaluate convergence.  
- Benchmark times are visualized as bar charts with mean ± standard deviation.

## 5. Outputs

- CSV files with benchmark results and W distributions  
- PNG plots for:
    - Sorting time
    - Total time
    - Monomer fraction distributions (A, B, C)

This methodology ensures reproducibility and allows a clear evaluation of chain statistics and sorting algorithm performance.
