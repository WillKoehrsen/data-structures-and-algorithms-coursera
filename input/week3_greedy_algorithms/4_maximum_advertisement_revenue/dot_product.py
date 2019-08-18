# Uses python3

import sys


def max_dot_product(a, b):
    # write your code here
    res = 0
    a = sorted(a, reverse=True)
    for elem_a in a:
        max_prod = float("-inf")
        for elem_b in b:
            prod = elem_a * elem_b
            if prod > max_prod:
                largest_b = elem_b
                max_prod = prod
        res += max_prod
        b.remove(largest_b)
    return res


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1 : (n + 1)]
    b = data[(n + 1) :]
    print(max_dot_product(a, b))

