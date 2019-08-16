# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def partial_fib_sum(m, n):
    if m > n:
        return

    a = [0, 1]
    for i in range(2, 60):
        a.append(a[i - 1] + a[i - 2])

    m = m % 60
    n = n % 60

    if n < m:
        n += 60

    sum_ = 0

    for j in range(m, n + 1):
        sum_ += a[j % 60]

    return sum_ % 10


if __name__ == "__main__":
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(partial_fib_sum(from_, to))
