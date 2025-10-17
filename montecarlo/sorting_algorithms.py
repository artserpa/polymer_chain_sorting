import numpy as np
from numba import njit


# ---------------- Bubble Sort ----------------

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

@njit
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


# ---------------- Insertion Sort ----------------
def insertion_sort(arr):
    '''
    Insertion Sort (pure Python)
    
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
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j+1] = sorted_arr[j]
            j -= 1
        sorted_arr[j+1] = key
    return sorted_arr

@njit
def insertion_sort_numba(arr):
    '''
    Insertion Sort (Numba)
    
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
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j+1] = sorted_arr[j]
            j -= 1
        sorted_arr[j+1] = key
    return sorted_arr

# ---------------- Selection Sort ----------------
def selection_sort(arr):
    '''
    Selection Sort (pure Python)
    
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
        min_idx = i
        for j in range(i+1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    return sorted_arr

@njit
def selection_sort_numba(arr):
    '''
    Selection Sort (Numba)
    
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
        min_idx = i
        for j in range(i+1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    return sorted_arr