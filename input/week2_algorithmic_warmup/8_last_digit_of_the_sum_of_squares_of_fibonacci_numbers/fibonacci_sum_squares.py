# Uses python3
from sys import stdin


def get_fib_last_digit(n):
    if n < 1:
        return n

    prev = 0
    curr = 1

    for _ in range(n - 1):
        prev, curr = curr % 10, (prev + curr) % 10
    return curr % 10


def get_fib_sum_squares(n):
    vertical_side = get_fib_last_digit(n % 60)
    horizontal_side = get_fib_last_digit((n + 1) % 60)
    return (vertical_side * horizontal_side) % 10


if __name__ == "__main__":
    n = int(stdin.read())
    print(get_fib_sum_squares(n))
