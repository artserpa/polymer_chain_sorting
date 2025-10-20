import numpy as np
import pandas as pd
from montecarlo.analysis import run_scaling_benchmark, save_results_to_csv

def test_run_scaling_benchmark():
    n_chains_list = [10, 20]
    df = run_scaling_benchmark(n_chains_list, n_repeats=2, random_seed=123)

    assert isinstance(df, pd.DataFrame)

    expected_columns = {"number_of_chains", "algorithm", "time"}
    assert expected_columns.issubset(df.columns)

    assert set(df["number_of_chains"].unique()) == set(n_chains_list)

    assert df["time"].dtype.kind in {"f"}


def test_save_results_to_csv(tmp_path):
    n_chains_list = [10]
    df = run_scaling_benchmark(n_chains_list, n_repeats=1, random_seed=42)

    csv_file = tmp_path / "results.csv"
    save_results_to_csv(df, filename=csv_file)

    df_loaded = pd.read_csv(csv_file)
    assert not df_loaded.empty
    assert set(df_loaded.columns) == {"number_of_chains", "algorithm", "time"}