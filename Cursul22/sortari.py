import random
import time

def timer_decorator(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Elapsed time: ", end - start)
        return result

    return wrapper

@timer_decorator
def sortare_simpla(numere: list[int]) -> list[int]:
    numere_copy = numere[:]

    for i in range (0, len(numere_copy) - 1):
        for j in range(i + 1, len(numere_copy)):
            if numere_copy[i] > numere_copy[j]:
                numere_copy[i], numere_copy[j] = numere_copy[j], numere_copy[i]

    return numere_copy

@timer_decorator
def sortare_eficienta(numere: list[int]) -> list[int]:
    numere_copy = numere[:]

    numere_copy.sort()

    return numere_copy

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

@timer_decorator
def merge_sort_manager(arr):
    arr_copy = arr[:]

    merge_sort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

if __name__ == '__main__':
    n = 50000
    unsorted_list = [random.randint(0, 100000) for _ in range(n)]
    # sorted_list_1 = sortare_simpla(unsorted_list)
    sorted_list_2 = merge_sort_manager(unsorted_list)
    sorted_list_3 = sortare_eficienta(unsorted_list)

