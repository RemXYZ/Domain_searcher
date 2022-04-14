def binary_search(lista, n: int, callback = None) -> int:
    l = 0
    r = len(lista)
    while l <= r:
        mid = (l+r)//2
        v = callback(lista[mid]) if callback is not None else lista[mid]

        if v == n:
            return mid

        if v > n:
            r = mid - 1
        else:
            l = mid + 1

    return 0

def qs_sort(T, left, right):
    i, j = left, right
    mid_i = (left + right) // 2
    mid = T[mid_i]
    while i <= j:
        el_i = T[i]
        el_j = T[j]
        while T[i] < mid:
            i += 1
            el_i = T[i]
        while T[j] > mid:
            j -= 1
            el_j = T[j]
        if i <= j:
            T[i], T[j] = T[j], T[i]
            i, j = i + 1, j - 1

    if left < j:
        qs_sort(T, left, j)
    if right > i:
        qs_sort(T, i, right)

def quicksort(T):
    n = len(T)
    qs_sort(T, 0, n - 1)
    return T


