import numpy as np
import pandas as pd
from montecarlo.analysis import run_scaling_benchmark, save_results_to_csv

def test_run_scaling_benchmark():
    n_chains_list = [10, 20]
    df = run_scaling_benchmark(n_chains_list, n_repeats=2, use_numba=False)

    assert isinstance(df, pd.DataFrame)

    expected_cols = ["number_of_chains", "algorithm", "use_numba", "generation_time", "sorting_time", "repeat"]
    for col in expected_cols:
        assert col in df.columns
    
    assert (df["generation_time"] > 0).all()
    assert (df["sorting_time"] > 0).all()

    df["total_time"] = df["generation_time"] + df["sorting_time"]
    assert (df["total_time"] >= df["generation_time"]).all()
    assert (df["total_time"] >= df["sorting_time"]).all()
    


def test_save_results_to_csv(tmp_path):
    n_chains_list = [10]
    df = run_scaling_benchmark(n_chains_list, n_repeats=1, random_seed=42)

    csv_file = tmp_path / "results.csv"
    save_results_to_csv(df, filename=csv_file)

    df_loaded = pd.read_csv(csv_file)
    assert not df_loaded.empty
    assert set(df_loaded.columns) == {"number_of_chains", "algorithm", "use_numba", "generation_time", "sorting_time", "repeat"}