def binary_search(list: list, n: int, callback = None) -> int:
    l = 0
    r = len(list)
    while l <= r:
        sr = (l+r)//2
        v = callback(list[sr]) if callback is not None else list[sr]

        if v == n:
            return sr

        if v > n:
            r = sr - 1
        else:
            l = sr + 1

    return 0

