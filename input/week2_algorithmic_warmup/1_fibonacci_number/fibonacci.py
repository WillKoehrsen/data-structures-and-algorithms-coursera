# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_iter(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for i in range(1, n):
        previous, current = current, previous + current
    return current


n = int(input())
print(calc_fib_iter(n))
