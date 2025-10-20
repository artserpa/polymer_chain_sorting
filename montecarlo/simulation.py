import numpy as np
from numba import njit, prange

def _generate_chain_python(num_chains: int):
    """
    Generate stationary Monte Carlo polymer chains with three monomer types (A, B, C).

    Parameters
    ----------
    num_chains : int
        Number of chains to generate.

    Returns
    -------
    chain_lengths : np.ndarray
        Array containing the length of each polymer chain.
    freq_A : np.ndarray
        Fraction of monomer A in each chain.
    freq_B : np.ndarray
        Fraction of monomer B in each chain.
    freq_C : np.ndarray
        Fraction of monomer C in each chain.
    """
    
    # --- Fixed parameters ---
    total_random_events = 1000  # Normalization factor
    prob_propagate_A = 0.6
    prob_propagate_B = 0.2
    prob_propagate_C = 0.2

    rate_AB = 5.0
    rate_AC = 10.0
    rate_BA = 0.2
    rate_BC = 2.0
    rate_CA = 0.1
    rate_CB = 0.5

    init_prob_A = 0.33
    init_prob_B = 0.33
    init_prob_C = 0.34

    freq_factor_A = 0.9091
    freq_factor_B = 0.0606
    freq_factor_C = 0.0303

    # Probabilities for starting a chain with each monomer
    start_prob_A = (freq_factor_A * total_random_events) / (freq_factor_A * total_random_events + init_prob_A)
    start_prob_B = (freq_factor_B * total_random_events) / (freq_factor_B * total_random_events + init_prob_B)
    start_prob_C = (freq_factor_C * total_random_events) / (freq_factor_C * total_random_events + init_prob_C)

    # Transition probabilities for monomer after last monomer
    P_AA = prob_propagate_A / (prob_propagate_A + prob_propagate_B / rate_AB + prob_propagate_C / rate_AC)
    P_AB = (prob_propagate_B / rate_AB) / (prob_propagate_A + prob_propagate_B / rate_AB + prob_propagate_C / rate_AC)
    P_AC = (prob_propagate_C / rate_AC) / (prob_propagate_A + prob_propagate_B / rate_AB + prob_propagate_C / rate_AC)

    P_BA = (prob_propagate_A / rate_BA) / (prob_propagate_B + prob_propagate_A / rate_BA + prob_propagate_C / rate_BC)
    P_BB = prob_propagate_B / (prob_propagate_B + prob_propagate_A / rate_BA + prob_propagate_C / rate_BC)
    P_BC = (prob_propagate_C / rate_BC) / (prob_propagate_B + prob_propagate_A / rate_BA + prob_propagate_C / rate_BC)

    P_CA = (prob_propagate_A / rate_CA) / (prob_propagate_C + prob_propagate_A / rate_CA + prob_propagate_B / rate_CB)
    P_CB = (prob_propagate_B / rate_CB) / (prob_propagate_C + prob_propagate_A / rate_CA + prob_propagate_B / rate_CB)
    P_CC = prob_propagate_C / (prob_propagate_C + prob_propagate_A / rate_CA + prob_propagate_B / rate_CB)

    # --- Initialization ---
    #np.random.seed(0)
    chain_lengths = []
    freq_A = []
    freq_B = []
    freq_C = []

    for _ in range(num_chains):
        chain_length = 1  # start with first monomer
        count_A = 1
        count_B = 0
        count_C = 0
        last_monomer = 1  # 1=A, 2=B, 3=C
        propagate_prob = start_prob_A

        while True:
            rnd = np.random.rand()

            if rnd > propagate_prob:  # terminate chain
                chain_lengths.append(chain_length)
                freq_A.append(count_A / chain_length)
                freq_B.append(count_B / chain_length)
                freq_C.append(count_C / chain_length)
                break
            else:  # propagate chain
                chain_length += 1
                rnd = np.random.rand()

                # --- Monomer generation ---
                if last_monomer == 1:  # last was A
                    if rnd <= P_AA:
                        count_A += 1
                        last_monomer = 1
                        propagate_prob = start_prob_A
                    elif rnd <= P_AA + P_AB:
                        count_B += 1
                        last_monomer = 2
                        propagate_prob = start_prob_B
                    else:
                        count_C += 1
                        last_monomer = 3
                        propagate_prob = start_prob_C

                elif last_monomer == 2:  # last was B
                    if rnd <= P_BA:
                        count_A += 1
                        last_monomer = 1
                        propagate_prob = start_prob_A
                    elif rnd <= P_BA + P_BB:
                        count_B += 1
                        last_monomer = 2
                        propagate_prob = start_prob_B
                    else:
                        count_C += 1
                        last_monomer = 3
                        propagate_prob = start_prob_C

                elif last_monomer == 3:  # last was C
                    if rnd <= P_CA:
                        count_A += 1
                        last_monomer = 1
                        propagate_prob = start_prob_A
                    elif rnd <= P_CA + P_CB:
                        count_B += 1
                        last_monomer = 2
                        propagate_prob = start_prob_B
                    else:
                        count_C += 1
                        last_monomer = 3
                        propagate_prob = start_prob_C

    return np.array(chain_lengths), np.array(freq_A), np.array(freq_B), np.array(freq_C)

@njit
def _generate_chain_numba(num_chains):
    chain_lengths = np.zeros(num_chains, dtype=np.int64)
    freq_A = np.zeros(num_chains, dtype=np.float64)
    freq_B = np.zeros(num_chains, dtype=np.float64)
    freq_C = np.zeros(num_chains, dtype=np.float64)

    total_random_events = 1000
    prob_propagate_A, prob_propagate_B, prob_propagate_C = 0.6, 0.2, 0.2
    rate_AB, rate_AC, rate_BA, rate_BC, rate_CA, rate_CB = 5.0, 10.0, 0.2, 2.0, 0.1, 0.5
    start_prob_A, start_prob_B, start_prob_C = 0.33, 0.33, 0.34
    freq_factor_A, freq_factor_B, freq_factor_C = 0.9091, 0.0606, 0.0303

    Pa = (freq_factor_A * total_random_events) / (freq_factor_A * total_random_events + start_prob_A)
    Pb = (freq_factor_B * total_random_events) / (freq_factor_B * total_random_events + start_prob_B)
    Pc = (freq_factor_C * total_random_events) / (freq_factor_C * total_random_events + start_prob_C)

    P_AA = prob_propagate_A / (prob_propagate_A + prob_propagate_B / rate_AB + prob_propagate_C / rate_AC)
    P_AB = (prob_propagate_B / rate_AB) / (prob_propagate_A + prob_propagate_B / rate_AB + prob_propagate_C / rate_AC)
    P_AC = (prob_propagate_C / rate_AC) / (prob_propagate_A + prob_propagate_B / rate_AB + prob_propagate_C / rate_AC)

    P_BA = (prob_propagate_A / rate_BA) / (prob_propagate_B + prob_propagate_A / rate_BA + prob_propagate_C / rate_BC)
    P_BB = prob_propagate_B / (prob_propagate_B + prob_propagate_A / rate_BA + prob_propagate_C / rate_BC)
    P_BC = (prob_propagate_C / rate_BC) / (prob_propagate_B + prob_propagate_A / rate_BA + prob_propagate_C / rate_BC)

    P_CA = (prob_propagate_A / rate_CA) / (prob_propagate_C + prob_propagate_A / rate_CA + prob_propagate_B / rate_CB)
    P_CB = (prob_propagate_B / rate_CB) / (prob_propagate_C + prob_propagate_A / rate_CA + prob_propagate_B / rate_CB)
    P_CC = prob_propagate_C / (prob_propagate_C + prob_propagate_A / rate_CA + prob_propagate_B / rate_CB)

    #np.random.seed(0)
    for i in prange(num_chains):
        chain_length = 1
        count_A, count_B, count_C = 1, 0, 0
        last_monomer = 1
        propagate_prob = Pa

        while True:
            rnd = np.random.rand()
            if rnd > propagate_prob:
                chain_lengths[i] = chain_length
                freq_A[i] = count_A / chain_length
                freq_B[i] = count_B / chain_length
                freq_C[i] = count_C / chain_length
                break
            else:
                chain_length += 1
                rnd = np.random.rand()

                if last_monomer == 1:
                    if rnd <= P_AA:
                        count_A += 1
                        last_monomer = 1
                        propagate_prob = Pa
                    elif rnd <= P_AA + P_AB:
                        count_B += 1
                        last_monomer = 2
                        propagate_prob = Pb
                    else:
                        count_C += 1
                        last_monomer = 3
                        propagate_prob = Pc
                elif last_monomer == 2:
                    if rnd <= P_BA:
                        count_A += 1
                        last_monomer = 1
                        propagate_prob = Pa
                    elif rnd <= P_BA + P_BB:
                        count_B += 1
                        last_monomer = 2
                        propagate_prob = Pb
                    else:
                        count_C += 1
                        last_monomer = 3
                        propagate_prob = Pc
                else:  # last_monomer == 3
                    if rnd <= P_CA:
                        count_A += 1
                        last_monomer = 1
                        propagate_prob = Pa
                    elif rnd <= P_CA + P_CB:
                        count_B += 1
                        last_monomer = 2
                        propagate_prob = Pb
                    else:
                        count_C += 1
                        last_monomer = 3
                        propagate_prob = Pc

    return chain_lengths, freq_A, freq_B, freq_C


def generate_chains(num_chains: int, use_numba: bool = False):
    """
    Generate Monte Carlo chains with option to use Numba acceleration.

    Parameters
    ----------
    num_chains : int
        Number of chains to generate.
    use_numba : bool
        If True, use Numba JIT compilation for faster execution.

    Returns
    -------
    chain_lengths, freq_A, freq_B, freq_C : np.ndarray
    """
    if use_numba:
        return _generate_chain_numba(num_chains)
    else:
        return _generate_chain_python(num_chains)