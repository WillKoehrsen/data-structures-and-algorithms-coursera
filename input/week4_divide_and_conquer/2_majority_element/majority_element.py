# Uses python3
import sys
from collections import Counter


def get_majority_element(a, left=None, right=None):
    n = len(a)
    if n == 1:
        return a[0]
    k = n // 2

    elem_lsub = get_majority_element(a[:k])
    elem_rsub = get_majority_element(a[k:])
    if elem_lsub == elem_rsub:
        return elem_lsub

    lcount = a.count(elem_lsub)
    rcount = a.count(elem_rsub)
    if lcount > n / 2:
        return elem_lsub
    elif rcount > n / 2:
        return elem_rsub

    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
