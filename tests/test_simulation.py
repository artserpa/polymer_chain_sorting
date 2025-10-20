import numpy as np
from montecarlo.simulation import generate_chains

def test_generate_chain_small():
    num_chains = 5
    chain_lengths, freq_A, freq_B, freq_C = generate_chains(num_chains, use_numba=False)

    assert len(chain_lengths) == num_chains
    assert len(freq_A) == num_chains
    assert len(freq_B) == num_chains
    assert len(freq_C) == num_chains

    assert np.all(freq_A >= 0) and np.all(freq_A <= 1)
    assert np.all(freq_B >= 0) and np.all(freq_B <= 1)
    assert np.all(freq_C >= 0) and np.all(freq_C <= 1)

    assert np.all(chain_lengths >= 1)

    print('Test for chain generation (Python) passed!')

def test_generate_chain_numba():
    num_chains = 5
    chain_lengths, freq_A, freq_B, freq_C = generate_chains(num_chains, use_numba=True)

    assert len(chain_lengths) == num_chains
    assert len(freq_A) == num_chains
    assert len(freq_B) == num_chains
    assert len(freq_C) == num_chains

    assert np.all(freq_A >= 0) and np.all(freq_A <= 1)
    assert np.all(freq_B >= 0) and np.all(freq_B <= 1)
    assert np.all(freq_C >= 0) and np.all(freq_C <= 1)

    assert np.all(chain_lengths >= 1)

    print('Test for chain generation (Numba) passed!')

def test_generate_chains_shapes():
    D, Fa, Fb, Fc = generate_chains(100, use_numba=False)
    assert len(D) == 100
    assert len(Fa) == 100
    assert len(Fb) == 100
    assert len(Fc) == 100

def test_generate_chains_values():
    _, Fa, Fb, Fc = generate_chains(100)
    assert np.all(Fa >= 0) and np.all(Fa <= 1)
    assert np.all(Fb >= 0) and np.all(Fb <= 1)
    assert np.all(Fc >= 0) and np.all(Fc <= 1)