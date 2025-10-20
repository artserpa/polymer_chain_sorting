import numpy as np
from numba import njit, prange


# ---------------- Bubble Sort ----------------

def bubble_sort(array1, array2):
    '''
    Bubble Sort implementation (pure Python)

    Parameters
    ----------
    array1 : np.ndarray
        Array to sort.
    array2 : np.ndarray
        Array to sort.

    Returns
    -------
    np.ndarray
        Sorted arrays.
    '''
    for passnum in range(len(array2) - 1 , 0, -1):
        for i in range(passnum):
            if array2[i] > array2[i+1]:
                # Swap in array1
                temp = array1[i]
                array1[i] = array1[i+1]
                array1[i+1] = temp
                # Swap in array2
                temp = array2[i]
                array2[i] = array2[i+1]
                array2[i+1] = temp
    return array1, array2

@njit
def bubble_sort_numba(array1, array2):
    '''
    Bubble Sort implementation (Numba)

    Parameters
    ----------
    array1 : np.ndarray
        Array to sort.
    array2 : np.ndarray
        Array to sort.

    Returns
    -------
    np.ndarray
        Sorted arrays.
    '''
    for passnum in range(len(array2) - 1 , 0, -1):
        for i in range(passnum):
            if array2[i] > array2[i+1]:
                # Swap in array1
                temp = array1[i]
                array1[i] = array1[i+1]
                array1[i+1] = temp
                # Swap in array2
                temp = array2[i]
                array2[i] = array2[i+1]
                array2[i+1] = temp
    return array1, array2


# ---------------- Insertion Sort ----------------
def insertion_sort(array1, array2):
    '''
    Insertion Sort (pure Python)
    
    Parameters
    ----------
    array1 : np.ndarray
        Array to sort.
    array2 : np.ndarray
        Array to sort.

    Returns
    -------
    np.ndarray
        Sorted arrays.
    '''
    n = len(array2)
    for index in prange(1, n):
        current_val2 = array2[index]
        current_val1 = array1[index]
        position = index
        while position > 0 and array2[position-1] > current_val2:
            array2[position] = array2[position-1]
            array1[position] = array1[position-1]
            position -= 1
        array2[position] = current_val2
        array1[position] = current_val1
    return array1, array2

@njit
def insertion_sort_numba(array1, array2):
    '''
    Insertion Sort (Numba)
    
    Parameters
    ----------
    array1 : np.ndarray
        Array to sort.
    array2 : np.ndarray
        Array to sort.

    Returns
    -------
    np.ndarray
        Sorted arrays.
    '''
    n = len(array2)
    for index in prange(1, n):
        current_val2 = array2[index]
        current_val1 = array1[index]
        position = index
        while position > 0 and array2[position-1] > current_val2:
            array2[position] = array2[position-1]
            array1[position] = array1[position-1]
            position -= 1
        array2[position] = current_val2
        array1[position] = current_val1
    return array1, array2

# ---------------- Selection Sort ----------------
def selection_sort(array1, array2):
    '''
    Selection Sort (pure Python)
    
    Parameters
    ----------
    array1 : np.ndarray
        Array to sort.
    array2 : np.ndarray
        Array to sort.
    
    Returns
    -------
    np.ndarray
        Sorted arrays.
    '''
    n = len(array2)
    for i in prange(n):
        min_idx = i
        for j in range(i+1, n):
            if array2[min_idx] > array2[j]:
                min_idx = j
        # Swap in array2
        temp = array2[i]
        array2[i] = array2[min_idx]
        array2[min_idx] = temp
        # Swap in array1
        temp1 = array1[i]
        array1[i] = array1[min_idx]
        array1[min_idx] = temp1
    return array1, array2

@njit
def selection_sort_numba(array1, array2):
    '''
    Selection Sort (Numba)
    
    Parameters
    ----------
    array1 : np.ndarray
        Array to sort.
    array2 : np.ndarray
        Array to sort.
    
    Returns
    -------
    np.ndarray
        Sorted arrays.
    '''
    n = len(array2)
    for i in prange(n):
        min_idx = i
        for j in range(i+1, n):
            if array2[min_idx] > array2[j]:
                min_idx = j
        # Swap in array2
        temp = array2[i]
        array2[i] = array2[min_idx]
        array2[min_idx] = temp
        # Swap in array1
        temp1 = array1[i]
        array1[i] = array1[min_idx]
        array1[min_idx] = temp1
    return array1, array2

# -------------------- TimSort  ------------------
def tim_sort(array1, array2):
    '''
    Tim Sort (pure Python)
    
    Parameters
    ----------
    array1 : np.ndarray
        Array to sort.
    array2 : np.ndarray
        Array to sort.
    
    Returns
    -------
    np.ndarray
        Sorted arrays.
    '''
    paired = sorted(zip(array2, array1))
    sorted_array2, sorted_array1 = zip(*paired)
    return list(sorted_array1), list(sorted_array2)
