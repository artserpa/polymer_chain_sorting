
# Polymer Chain Monte Carlo Simulation

This project simulates polymer chain formation using steady state Monte Carlo approach.

It is based on a published work by the GAAP research group from the Department of Chemical and Materials Engineering at PUC-Rio.

The work is entitled "Monte Carlo simulation of terpolymerization: Optimizing the simulation and post-processing times" and it was published at the Canadian Journal of Chemical Engineering. The online version can be reached in [here](https://onlinelibrary.wiley.com/doi/abs/10.1002/cjce.24889).

## Projet Structure

```bash
polymer_chain_sorting/
│
├── main.py                     # Main script to run benchmark and generate distributions
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview
├── docs/
│   └── methodology.md          # Detailed methodology description
├── montecarlo/
│   ├── __init__.py
│   ├── analysis.py             # Benchmarking and timing functions
│   ├── performance.py          # Sorting performance wrapper functions
│   ├── simulation.py           # Polymer chain generation
│   ├── sorting_algorithms.py   # Sorting algorithm functions
│   └── visualization.py        # Plotting and saving functions
├── tests/
│   ├── __init__.py
│   ├── test_analysis.py             
│   ├── test_performance.py          
│   ├── test_simulation.py           
│   ├── test_sorting_algorithms.py   
│   └── test_visualization.py        
└── results/                    # Output folder (CSV, PNG files)
```
### Installation
Create a Python environment and install the dependecies:

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

### Usage
Run the main script:

```bash
python main.py
```

This will:

1. Benchmark sorting algorithms for polymer chains of sizes [100, 500, 1000].
2. Save the benchmark results in `results/benchmark_with_numba.csv`
3. Generate plots for:
    - Sorting time (`results/sorting_time.png`)
    - Total time (`results/total_time.png`)
4. Generate polymer chains (10,000 chains by default) and save CSVs for distributions:
    - `results/distribution_WA.csv`
    - `results/distribution_WB.csv`
    - `results/distribution_WC.csv`
5. Plot monomer fraction distributions:
    - `results/distribution_WA.png`
    - `results/distribution_WBC.png`

### Running Tests
To run all tests:
```bash
pytest
```
All tests are located in the `tests/` folder.
