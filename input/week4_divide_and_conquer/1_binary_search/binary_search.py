# Uses python3
import sys


def binary_search(a, x, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(a) - 1

    while right >= left:
        mid_index = int(left + (right - left) / 2)
        mid_value = a[mid_index]

        if x == mid_value:
            return mid_index
        elif x > mid_value:
            left = mid_index + 1
        elif x < mid_value:
            right = mid_index - 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
