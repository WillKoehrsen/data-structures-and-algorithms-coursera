# Uses python3
import sys
import random


def partition3(a, pivot, lo, hi):

    l = lo
    r = lo
    u = hi

    while r <= u:
        if a[r] < pivot:
            a[l], a[r] = a[r], a[l]
            l += 1
            r += 1
        elif a[r] > pivot:
            a[r], a[u] = a[u], a[r]
            u -= 1
        else:
            r += 1
    return l, r


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, lo, hi):
    if lo >= hi:
        return
    pivot = a[lo]
    left, right = partition3(a, pivot, lo, hi)
    randomized_quick_sort(a, lo, left - 1)
    randomized_quick_sort(a, right, hi)


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=" ")
