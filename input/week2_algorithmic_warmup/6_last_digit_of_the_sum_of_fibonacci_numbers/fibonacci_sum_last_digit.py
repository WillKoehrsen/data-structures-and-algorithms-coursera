# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fib(a):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for i in range(2, a):
        previous, current = current, previous + current
    return current


def fib_sum(n):
    if n <= 1:
        return n

    n = (n+2) % 60
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append((fib[i-1] % 10 + fib[i-2] % 10) % 10)

    if fib[n] == 0:
        return 9
    return fib[n] % 10 - 1


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    print(fib_sum(n))
