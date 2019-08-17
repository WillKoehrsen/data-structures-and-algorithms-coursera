# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge(n, m, return_arr=False):
    if n <= 1:
        return n

    arr = [0, 1]
    previous = 0
    current = 1

    for i in range(1, n):
        temp = previous
        previous = current % m
        current = (temp + current) % m
        arr.append(current)
        if current == 1 and previous == 0:
            index = n % i
            if return_arr:
                return arr
            return arr[index]

    if return_arr:
        return arr
    return current


if __name__ == "__main__":
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
