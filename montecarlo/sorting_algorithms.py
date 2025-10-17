import numpy as np
from numba import njit

def bubble_sort(arr):
    '''
    Bubble Sort implementation (pure Python)

    Parameters
    ----------
    arr : np.ndarray
        Array to sort.

    Returns
    -------
    np.ndarray
        Sorted array.
    '''
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    return sorted_arr

def bubble_sort_numba(arr):
    '''
    Bubble Sort implementation (Numba)

    Parameters
    ----------
    arr : np.ndarray
        Array to sort.

    Returns
    -------
    np.ndarray
        Sorted array.
    '''
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    return sorted_arr